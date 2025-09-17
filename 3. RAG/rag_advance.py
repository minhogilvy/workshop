import os
from typing import List, Dict, Any, Optional, Tuple
from enum import Enum

import numpy as np
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.chains.query_constructor.base import AttributeInfo
from langchain.retrievers.self_query.base import SelfQueryRetriever

class RAGStrategy(Enum):
    """Available RAG implementation strategies."""
    BASIC = "basic"
    QUERY_REWRITING = "query_rewriting"
    MULTI_STEP = "multi_step"
    RERANKING = "reranking"
    HYDE = "hyde"

class AdvancedRAG:
    """Advanced RAG implementation with multiple strategies."""

    def __init__(
        self,
        documents_dir: str,
        embedding_model: str = "text-embedding-ada-002",
        llm_model: str = "gpt-4",
        strategy: RAGStrategy = RAGStrategy.BASIC,
        api_key: Optional[str] = None
    ):
        """Initialize the RAG system.

        Args:
            documents_dir: Directory containing documents
            embedding_model: Embedding model to use
            llm_model: LLM model to use
            strategy: RAG strategy to employ
            api_key: OpenAI API key (optional, can use env var)
        """
        self.documents_dir = documents_dir
        self.embedding_model = embedding_model
        self.llm_model = llm_model
        self.strategy = strategy

        # Set API key
        if api_key:
            os.environ["OPENAI_API_KEY"] = api_key

        # Initialize components
        self.embeddings = OpenAIEmbeddings(model=embedding_model)
        self.llm = ChatOpenAI(model=llm_model, temperature=0)

        # Create vector store
        self.vector_store = self._create_vector_store()

        # Initialize strategy components
        self._init_strategy_components()

    def _create_vector_store(self) -> Chroma:
        """Process documents and create vector store."""
        # Check if vector store exists
        persist_directory = "chroma_db"
        if os.path.exists(persist_directory) and os.path.isdir(persist_directory):
            print("Loading existing vector store...")
            return Chroma(persist_directory=persist_directory, embedding_function=self.embeddings)

        # Load documents
        print("Loading documents...")
        loader = DirectoryLoader(
            self.documents_dir,
            glob="**/*.txt",
            loader_cls=TextLoader
        )
        documents = loader.load()

        # Split documents
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        chunks = text_splitter.split_documents(documents)

        # Create vector store
        print(f"Creating vector store with {len(chunks)} chunks...")
        vector_store = Chroma.from_documents(
            documents=chunks,
            embedding=self.embeddings,
            persist_directory=persist_directory
        )
        vector_store.persist()

        return vector_store

    def _init_strategy_components(self):
        """Initialize components based on selected strategy."""
        # Basic retriever
        self.retriever = self.vector_store.as_retriever(search_kwargs={"k": 5})

        if self.strategy == RAGStrategy.QUERY_REWRITING:
            # Initialize query rewriting chain
            query_rewrite_template = """
            You are an expert at interpreting user questions.
            Your task is to rewrite the user's query to make it more effective for retrieval from a knowledge base.
            Include different phrasings, synonyms, and related concepts.
            Output 3 different versions of the query, separated by |||.

            Original query: {query}
            """
            self.query_rewriter = LLMChain(
                llm=self.llm,
                prompt=ChatPromptTemplate.from_template(query_rewrite_template)
            )

        elif self.strategy == RAGStrategy.MULTI_STEP:
            # Initialize follow-up question generator
            followup_template = """
            Based on the user's question and the initial retrieved context, generate 2-3 follow-up questions
            that would help gather more relevant information. These questions should address aspects not covered
            in the initial context or dive deeper into specific details.

            User question: {query}
            Retrieved context: {context}

            Output only the questions, separated by |||.
            """
            self.followup_generator = LLMChain(
                llm=self.llm,
                prompt=ChatPromptTemplate.from_template(followup_template)
            )

        elif self.strategy == RAGStrategy.RERANKING:
            # Initialize reranker using LLM
            rerank_template = """
            You are an expert at determining the relevance of documents to a query.
            Rate the following document's relevance to the query on a scale of 1-10,
            where 10 is most relevant. Provide only the numeric score.

            Query: {query}
            Document: {document}

            Relevance score (1-10):
            """
            self.rerank_chain = LLMChain(
                llm=self.llm,
                prompt=ChatPromptTemplate.from_template(rerank_template)
            )
            # Use more documents initially
            self.retriever = self.vector_store.as_retriever(search_kwargs={"k": 20})

        elif self.strategy == RAGStrategy.HYDE:
            # Initialize hypothetical document generator
            hyde_template = """
            Based on the user's question, generate a hypothetical document that would perfectly answer it.
            This document should be detailed and specific, as it will be used to retrieve relevant information.

            User question: {query}

            Hypothetical document:
            """
            self.hyde_generator = LLMChain(
                llm=self.llm,
                prompt=ChatPromptTemplate.from_template(hyde_template)
            )

    async def _query_rewriting_strategy(self, query: str) -> Tuple[List[Dict], str]:
        """Implement query rewriting strategy."""
        # Generate variations of the query
        rewrite_result = await self.query_rewriter.arun(query=query)
        query_variations = rewrite_result.split("|||")
        query_variations = [q.strip() for q in query_variations]

        # Add the original query
        query_variations.append(query)

        # Retrieve documents for each query variation
        all_docs = []
        for q in query_variations:
            docs = await self.retriever.aget_relevant_documents(q)
            all_docs.extend(docs)

        # Remove duplicates
        unique_docs = []
        unique_contents = set()
        for doc in all_docs:
            if doc.page_content not in unique_contents:
                unique_contents.add(doc.page_content)
                unique_docs.append(doc)

        # Select top docs
        unique_docs = unique_docs[:5]

        # Create context
        context = "\n\n".join([doc.page_content for doc in unique_docs])

        return unique_docs, context

    async def _multi_step_strategy(self, query: str) -> Tuple[List[Dict], str]:
        """Implement multi-step retrieval strategy."""
        # Initial retrieval
        initial_docs = await self.retriever.aget_relevant_documents(query)
        initial_context = "\n\n".join([doc.page_content for doc in initial_docs])

        # Generate follow-up questions
        followup_result = await self.followup_generator.arun(
            query=query,
            context=initial_context
        )
        followup_questions = followup_result.split("|||")
        followup_questions = [q.strip() for q in followup_questions]

        # Retrieve documents for follow-up questions
        all_docs = initial_docs.copy()
        for q in followup_questions:
            docs = await self.retriever.aget_relevant_documents(q)
            all_docs.extend(docs)

        # Remove duplicates
        unique_docs = []
        unique_contents = set()
        for doc in all_docs:
            if doc.page_content not in unique_contents:
                unique_contents.add(doc.page_content)
                unique_docs.append(doc)

        # Select top docs
        unique_docs = unique_docs[:7]  # Allow more context for multi-step

        # Create context
        context = "\n\n".join([doc.page_content for doc in unique_docs])

        return unique_docs, context

    async def _reranking_strategy(self, query: str) -> Tuple[List[Dict], str]:
        """Implement reranking strategy."""
        # Retrieve larger set of documents
        docs = await self.retriever.aget_relevant_documents(query)

        # Rerank documents
        scored_docs = []
        for doc in docs:
            score_text = await self.rerank_chain.arun(
                query=query,
                document=doc.page_content
            )
            try:
                score = float(score_text.strip())
                scored_docs.append((doc, score))
            except ValueError:
                # Handle case where LLM doesn't return a valid number
                scored_docs.append((doc, 0))

        # Sort by score descending
        scored_docs.sort(key=lambda x: x[1], reverse=True)

        # Take top 5
        top_docs = [doc for doc, _ in scored_docs[:5]]

        # Create context
        context = "\n\n".join([doc.page_content for doc in top_docs])

        return top_docs, context

    async def _hyde_strategy(self, query: str) -> Tuple[List[Dict], str]:
        """Implement Hypothetical Document Embeddings strategy."""
        # Generate hypothetical document
        hypothetical_doc = await self.hyde_generator.arun(query=query)

        # Use hypothetical doc as query for retrieval
        docs = await self.retriever.aget_relevant_documents(hypothetical_doc)

        # Create context
        context = "\n\n".join([doc.page_content for doc in docs])

        return docs, context

    async def _basic_strategy(self, query: str) -> Tuple[List[Dict], str]:
        """Implement basic RAG strategy."""
        docs = await self.retriever.aget_relevant_documents(query)
        context = "\n\n".join([doc.page_content for doc in docs])
        return docs, context

    async def query(self, query: str) -> Dict[str, Any]:
        """Process query using the selected RAG strategy.

        Args:
            query: User query string

        Returns:
            Dict containing answer and metadata
        """
        # Select retrieval strategy
        if self.strategy == RAGStrategy.QUERY_REWRITING:
            docs, context = await self._query_rewriting_strategy(query)
        elif self.strategy == RAGStrategy.MULTI_STEP:
            docs, context = await self._multi_step_strategy(query)
        elif self.strategy == RAGStrategy.RERANKING:
            docs, context = await self._reranking_strategy(query)
        elif self.strategy == RAGStrategy.HYDE:
            docs, context = await self._hyde_strategy(query)
        else:  # Basic strategy
            docs, context = await self._basic_strategy(query)

        # Create answer generation prompt
        answer_template = """
        You are a helpful AI assistant that answers questions based on the provided context.
        If the context doesn't contain relevant information, admit that you don't know.
        Always cite your sources using [Source X] notation when referring to specific content.

        Context:
        {context}

        User question: {query}
        """

        answer_prompt = ChatPromptTemplate.from_messages([
            SystemMessagePromptTemplate.from_template(answer_template),
            HumanMessagePromptTemplate.from_template("{query}")
        ])

        # Generate answer
        answer_chain = LLMChain(llm=self.llm, prompt=answer_prompt)
        answer = await answer_chain.arun(query=query, context=context)

        # Prepare source metadata
        sources = []
        for i, doc in enumerate(docs):
            source = {
                "content": doc.page_content[:200] + "...",  # Truncate for readability
                "metadata": doc.metadata
            }
            sources.append(source)

        return {
            "query": query,
            "answer": answer,
            "sources": sources,
            "strategy": self.strategy.value
        }

# Example usage
import asyncio

async def main():
    # Initialize RAG with HyDE strategy
    rag = AdvancedRAG(
        documents_dir="./knowledge_base",
        strategy=RAGStrategy.HYDE,
        api_key="your-api-key"  # Or use environment variable
    )

    # Process query
    result = await rag.query("What are the environmental impacts of electric vehicles?")

    # Print answer
    print(f"Query: {result['query']}")
    print(f"Strategy: {result['strategy']}")
    print(f"\nAnswer: {result['answer']}")
    print("\nSources:")
    for i, source in enumerate(result['sources']):
        print(f"[Source {i+1}] {source['metadata'].get('source', 'Unknown')}")

if __name__ == "__main__":
    asyncio.run(main())
