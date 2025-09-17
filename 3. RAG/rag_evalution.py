import os
import json
import pandas as pd
import numpy as np
from typing import List, Dict, Any, Optional, Tuple
from tqdm import tqdm
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.retrievers.base import BaseRetriever
from langchain.schema import Document
from langchain.prompts import ChatPromptTemplate

class RAGEvaluator:
    """Framework for evaluating RAG system performance."""

    def __init__(
        self,
        eval_llm: str = "gpt-4",
        api_key: Optional[str] = None,
        results_dir: str = "evaluation_results"
    ):
        """Initialize the RAG evaluator.

        Args:
            eval_llm: LLM to use for evaluation
            api_key: OpenAI API key
            results_dir: Directory to save evaluation results
        """
        # Set API key
        if api_key:
            os.environ["OPENAI_API_KEY"] = api_key

        # Initialize LLM for evaluation
        self.eval_llm = ChatOpenAI(model=eval_llm, temperature=0)

        # Create results directory
        os.makedirs(results_dir, exist_ok=True)
        self.results_dir = results_dir

    def evaluate_retrieval(
        self,
        retriever: BaseRetriever,
        test_queries: List[Dict[str, Any]],
        k_values: List[int] = [1, 3, 5, 10]
    ) -> Dict[str, Any]:
        """Evaluate retrieval performance.

        Args:
            retriever: The retriever to evaluate
            test_queries: List of test queries with ground truth
            k_values: List of k values for precision/recall@k

        Returns:
            Dictionary with evaluation metrics
        """
        results = {
            "precision": {f"p@{k}": [] for k in k_values},
            "recall": {f"r@{k}": [] for k in k_values},
            "ndcg": {f"ndcg@{k}": [] for k in k_values},
            "context_relevance": []
        }

        for query_item in tqdm(test_queries, desc="Evaluating retrieval"):
            query = query_item["query"]
            expected_docs = query_item.get("relevant_docs", [])

            # Get retrieved documents
            retrieved_docs = retriever.get_relevant_documents(query)

            # Evaluate precision and recall for each k
            for k in k_values:
                if k <= len(retrieved_docs):
                    topk_docs = retrieved_docs[:k]

                    # Calculate precision@k
                    relevant_retrieved = sum(1 for doc in topk_docs
                                           if self._is_relevant(doc, expected_docs))
                    precision_k = relevant_retrieved / k if k > 0 else 0
                    results["precision"][f"p@{k}"].append(precision_k)

                    # Calculate recall@k
                    recall_k = relevant_retrieved / len(expected_docs) if expected_docs else 1.0
                    results["recall"][f"r@{k}"].append(recall_k)

                    # Calculate NDCG@k
                    ndcg_k = self._calculate_ndcg(topk_docs, expected_docs, k)
                    results["ndcg"][f"ndcg@{k}"].append(ndcg_k)

            # Evaluate context relevance using LLM
            context_relevance = self._evaluate_context_relevance(query, retrieved_docs[:5])
            results["context_relevance"].append(context_relevance)

        # Calculate averages
        for metric_type, metrics in results.items():
            if metric_type != "context_relevance":
                for metric_name, values in metrics.items():
                    results[metric_type][metric_name] = np.mean(values)
            else:
                results[metric_type] = np.mean(results[metric_type])

        return results

    def _is_relevant(self, doc: Document, expected_docs: List[str]) -> bool:
        """Check if a document is in the list of expected documents."""
        # Simple check - could be enhanced with semantic similarity
        for expected in expected_docs:
            if expected in doc.page_content:
                return True
        return False

    def _calculate_ndcg(
        self,
        retrieved_docs: List[Document],
        expected_docs: List[str],
        k: int
    ) -> float:
        """Calculate NDCG@k for retrieved documents."""
        relevance = [1 if self._is_relevant(doc, expected_docs) else 0
                     for doc in retrieved_docs[:k]]

        # DCG calculation
        dcg = 0
        for i, rel in enumerate(relevance):
            dcg += rel / np.log2(i + 2)  # i+2 because i is 0-indexed

        # Ideal DCG (all relevant docs ranked first)
        ideal_relevance = sorted(relevance, reverse=True)
        idcg = 0
        for i, rel in enumerate(ideal_relevance):
            idcg += rel / np.log2(i + 2)

        # NDCG calculation
        return dcg / idcg if idcg > 0 else 0

    def _evaluate_context_relevance(
        self,
        query: str,
        docs: List[Document]
    ) -> float:
        """Evaluate relevance of retrieved context to query using LLM."""
        context = "\n\n".join([doc.page_content for doc in docs])

        prompt_template = """
        Evaluate the relevance of the following context to the query.
        Rate the relevance on a scale of 0 to 10, where:
        - 0: Completely irrelevant
        - 5: Somewhat relevant but missing key information
        - 10: Perfectly relevant, containing all needed information

        Provide only the numeric score.

        Query: {query}

        Context:
        {context}

        Relevance score (0-10):
        """

        prompt = ChatPromptTemplate.from_template(prompt_template)

        result = self.eval_llm(
            prompt.format_messages(
                query=query,
                context=context
            )
        )

        try:
            score = float(result.content.strip())
            return score / 10.0  # Normalize to 0-1
        except ValueError:
            return 0.0

    def evaluate_answer_quality(
        self,
        query: str,
        answer: str,
        retrieved_docs: List[Document]
    ) -> Dict[str, float]:
        """Evaluate the quality of a generated answer.

        Args:
            query: User query
            answer: Generated answer
            retrieved_docs: Retrieved documents used for generation

        Returns:
            Dictionary with quality metrics
        """
        context = "\n\n".join([doc.page_content for doc in retrieved_docs])

        # Evaluate faithfulness
        faithfulness_prompt = """
        Evaluate if the answer is faithful to the provided context.
        Faithfulness means the answer does not contain claims that cannot be derived from the context.

        Rate faithfulness on a scale of 0 to 10, where:
        - 0: Contains many claims not supported by context
        - 5: Contains some unsupported claims
        - 10: All claims are directly supported by the context

        Provide only the numeric score.

        Context:
        {context}

        Answer:
        {answer}

        Faithfulness score (0-10):
        """

        faithfulness_result = self.eval_llm(
            ChatPromptTemplate.from_template(faithfulness_prompt).format_messages(
                context=context,
                answer=answer
            )
        )

        # Evaluate relevance
        relevance_prompt = """
        Evaluate if the answer is relevant to the query.
        Relevance means the answer directly addresses what was asked.

        Rate relevance on a scale of 0 to 10, where:
        - 0: Completely unrelated to the query
        - 5: Partially addresses the query
        - 10: Perfectly addresses the query

        Provide only the numeric score.

        Query:
        {query}

        Answer:
        {answer}

        Relevance score (0-10):
        """

        relevance_result = self.eval_llm(
            ChatPromptTemplate.from_template(relevance_prompt).format_messages(
                query=query,
                answer=answer
            )
        )

        # Evaluate coherence
        coherence_prompt = """
        Evaluate the coherence of the answer.
        Coherence means the answer is logically structured, clear, and reads naturally.

        Rate coherence on a scale of 0 to 10, where:
        - 0: Incoherent, disjointed text
        - 5: Somewhat coherent with some logical issues
        - 10: Perfectly coherent, clear, and well-structured

        Provide only the numeric score.

        Answer:
        {answer}

        Coherence score (0-10):
        """

        coherence_result = self.eval_llm(
            ChatPromptTemplate.from_template(coherence_prompt).format_messages(
                answer=answer
            )
        )

        # Parse scores
        try:
            faithfulness = float(faithfulness_result.content.strip()) / 10.0
            relevance = float(relevance_result.content.strip()) / 10.0
            coherence = float(coherence_result.content.strip()) / 10.0

            # Calculate overall quality score
            overall = (faithfulness + relevance + coherence) / 3

            return {
                "faithfulness": faithfulness,
                "relevance": relevance,
                "coherence": coherence,
                "overall": overall
            }
        except ValueError:
            return {
                "faithfulness": 0.0,
                "relevance": 0.0,
                "coherence": 0.0,
                "overall": 0.0
            }

    def evaluate_rag_system(
        self,
        rag_system: Any,
        test_cases: List[Dict[str, Any]],
        system_name: str = "rag_system"
    ) -> Dict[str, Any]:
        """Evaluate entire RAG system end-to-end.

        Args:
            rag_system: RAG system with query method
            test_cases: List of test cases with queries and expected answers
            system_name: Name to use for saved results

        Returns:
            Dictionary with evaluation metrics
        """
        results = {
            "system_name": system_name,
            "test_cases": [],
            "aggregate_metrics": {}
        }

        answer_quality_metrics = {
            "faithfulness": [],
            "relevance": [],
            "coherence": [],
            "overall": []
        }

        answer_correctness = []

        for i, test_case in enumerate(tqdm(test_cases, desc="Evaluating RAG system")):
            query = test_case["query"]
            expected_answer = test_case.get("expected_answer", "")

            # Get system response
            response = rag_system.query(query)
            answer = response.get("answer", "")
            retrieved_docs = response.get("sources", [])

            # Convert sources to Document objects if needed
            if retrieved_docs and not isinstance(retrieved_docs[0], Document):
                docs = []
                for src in retrieved_docs:
                    if isinstance(src, dict) and "content" in src:
                        docs.append(Document(
                            page_content=src["content"],
                            metadata=src.get("metadata", {})
                        ))
                retrieved_docs = docs

            # Evaluate answer quality
            quality_metrics = self.evaluate_answer_quality(query, answer, retrieved_docs)

            # Evaluate answer correctness if expected answer is provided
            correctness = 0.0
            if expected_answer:
                correctness_prompt = """
                Evaluate if the generated answer is factually correct compared to the expected answer.

                Rate correctness on a scale of 0 to 10, where:
                - 0: Completely incorrect
                - 5: Partially correct with some errors
                - 10: Completely correct and complete

                Provide only the numeric score.

                Query: {query}

                Expected answer:
                {expected_answer}

                Generated answer:
                {answer}

                Correctness score (0-10):
                """

                correctness_result = self.eval_llm(
                    ChatPromptTemplate.from_template(correctness_prompt).format_messages(
                        query=query,
                        expected_answer=expected_answer,
                        answer=answer
                    )
                )

                try:
                    correctness = float(correctness_result.content.strip()) / 10.0
                except ValueError:
                    correctness = 0.0

            # Collect metrics
            for metric, value in quality_metrics.items():
                answer_quality_metrics[metric].append(value)

            answer_correctness.append(correctness)

            # Save individual test case results
            results["test_cases"].append({
                "query": query,
                "answer": answer,
                "quality_metrics": quality_metrics,
                "correctness": correctness
            })

        # Calculate aggregate metrics
        for metric, values in answer_quality_metrics.items():
            results["aggregate_metrics"][f"avg_{metric}"] = np.mean(values)

        results["aggregate_metrics"]["avg_correctness"] = np.mean(answer_correctness)

        # Calculate RAGAS-inspired score
        ragas_score = np.mean([
            np.mean(answer_quality_metrics["faithfulness"]),
            np.mean(answer_quality_metrics["relevance"]),
            np.mean(answer_correctness)
        ])

        results["aggregate_metrics"]["ragas_score"] = ragas_score

        # Save results
        output_file = os.path.join(self.results_dir, f"{system_name}_evaluation.json")
        with open(output_file, "w") as f:
            json.dump(results, f, indent=2)

        return results

    def compare_systems(
        self,
        system_results: List[Dict[str, Any]]
    ) -> pd.DataFrame:
        """Compare multiple RAG systems.

        Args:
            system_results: List of evaluation results from evaluate_rag_system

        Returns:
            DataFrame with comparative metrics
        """
        comparison = []

        for result in system_results:
            metrics = result["aggregate_metrics"]
            system_name = result["system_name"]

            comparison.append({
                "System": system_name,
                "Faithfulness": metrics.get("avg_faithfulness", 0),
                "Relevance": metrics.get("avg_relevance", 0),
                "Coherence": metrics.get("avg_coherence", 0),
                "Correctness": metrics.get("avg_correctness", 0),
                "RAGAS Score": metrics.get("ragas_score", 0)
            })

        return pd.DataFrame(comparison)

# Example usage
if __name__ == "__main__":
    from langchain.retrievers import ContextualCompressionRetriever
    from langchain.retrievers.document_compressors import LLMChainExtractor

    # Initialize evaluator
    evaluator = RAGEvaluator(api_key="your-api-key")

    # Define test queries with relevant docs
    test_queries = [
        {
            "query": "What are the environmental benefits of electric vehicles?",
            "relevant_docs": [
                "Electric vehicles produce zero direct emissions",
                "Studies show EVs reduce greenhouse gas emissions by 30-70%",
                "Electric vehicles help reduce air pollution in urban areas"
            ]
        },
        # Add more test queries...
    ]

    # Initialize retriever to evaluate
    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma(collection_name="your_collection", embedding_function=embeddings)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 10})

    # Evaluate retrieval
    retrieval_results = evaluator.evaluate_retrieval(
        retriever=retriever,
        test_queries=test_queries
    )

    print("Retrieval Evaluation:")
    print(f"Precision@5: {retrieval_results['precision']['p@5']:.3f}")
    print(f"Recall@5: {retrieval_results['recall']['r@5']:.3f}")
    print(f"NDCG@5: {retrieval_results['ndcg']['ndcg@5']:.3f}")
    print(f"Context Relevance: {retrieval_results['context_relevance']:.3f}")

    # Full RAG system evaluation would be similar:
    # evaluator.evaluate_rag_system(rag_system, test_cases, "base_rag")
