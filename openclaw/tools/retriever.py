from app.rag.retriever import RagRetriever

class Retriever:
    def __init__(self, vector_store):
        self.rag = RagRetriever(vector_store)

    def run(self, sub_queries):
        docs = []
        for q in sub_queries:
            docs.extend(self.rag.retrieve(q))
        return {"documents": docs}
