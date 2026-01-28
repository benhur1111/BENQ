from rag.pipeline import rag_answer

def rag_tool(query: str) -> str:
    """
    Tool: Use RAG to answer knowledge-based questions.
    """
    return rag_answer(query)
TOOLS = {
    "rag_tool": {
        "description": "Answer questions using internal knowledge base",
        "function": rag_tool
    }
}
