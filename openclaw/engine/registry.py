from openclaw.cognition.planner import Planner
from openclaw.cognition.reasoner import Reasoner
from openclaw.cognition.verifier import Verifier
from openclaw.cognition.summarizer import Summarizer
from openclaw.tools.retriever import Retriever

class ComponentRegistry:
    def __init__(self, llm, vector_store):
        self.components = {
            "planner": Planner(),
            "retriever": Retriever(vector_store),
            "reasoner": Reasoner(llm),
            "verifier": Verifier(),
            "summarizer": Summarizer()
        }

    def get(self, name):
        return self.components[name]
