from rag.retriever import retrieve_docs
from rag.generator import generate_answer


def rag_pipeline(query: str, embedding: list[float]) -> str:
    docs = retrieve_docs(embedding)

    context = "\n\n".join(docs)

    prompt = f"""
Use the context below to answer the question.

Context:
{context}

Question:
{query}
"""

    return generate_answer(prompt)
