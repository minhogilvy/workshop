# Simple RAG Implementation with LangChain and FAISS
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA

# 1. Document Processing
def process_documents(docs_dir):
    """Load, chunk and create embeddings for documents."""
    print("Step 1: Processing documents...")

    # Load documents from directory
    loader = DirectoryLoader(docs_dir, glob="**/*.pdf")
    documents = loader.load()

    # Split documents into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = text_splitter.split_documents(documents)

    print(f"Processed {len(documents)} documents into {len(chunks)} chunks")
    return chunks

# 2. Vector Storage
def create_vector_store(chunks):
    """Create and store document vectors."""
    print("Step 2: Creating vector store...")

    # Create embeddings
    embeddings = OpenAIEmbeddings()

    # Create vector store
    vector_store = FAISS.from_documents(chunks, embeddings)

    # Save vector store locally
    vector_store.save_local("faiss_index")

    print("Vector store created and saved")
    return vector_store

# 3. Query Pipeline
def create_qa_chain(vector_store):
    """Set up the question-answering chain."""
    print("Step 3: Setting up query pipeline...")

    # Create retriever
    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 5}  # Retrieve top 5 most similar chunks
    )

    # Create LLM
    llm = OpenAI(temperature=0)

    # Create QA chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",  # Simple approach: stuff all context into prompt
        retriever=retriever,
        return_source_documents=True  # Include sources in response
    )

    print("Query pipeline ready")
    return qa_chain

# Main RAG application
def main():
    # Process documents
    chunks = process_documents("./knowledge_base")

    # Create vector store
    vector_store = create_vector_store(chunks)

    # Create QA chain
    qa_chain = create_qa_chain(vector_store)

    # Interactive query loop
    while True:
        query = input("\nEnter your question (or 'quit' to exit): ")
        if query.lower() == "quit":
            break

        # Get response
        result = qa_chain({"query": query})

        # Print answer and sources
        print("\nAnswer:", result["result"])
        print("\nSources:")
        for i, doc in enumerate(result["source_documents"]):
            print(f"{i+1}. {doc.metadata.get('source', 'Unknown')}")

if __name__ == "__main__":
    main()
