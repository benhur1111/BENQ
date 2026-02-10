class Planner:
    """
    Minimal cognitive planner.
    Decides how to route a request into a workflow.
    """

    def __init__(self, registry):
        self.registry = registry

    def plan(self, user_query: str):
        """
        For now: always run the game loop workflow.
        """
        return {
            "workflow": "opus_rag.yaml",
            "input": user_query
        }
