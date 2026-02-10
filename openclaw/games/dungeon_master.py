from openclaw.engine.executor import WorkflowExecutor
from openclaw.engine.registry import ComponentRegistry


class DungeonMaster:
    def __init__(self, llm, vector_store):
        self.registry = ComponentRegistry(llm, vector_store)
        self.executor = WorkflowExecutor(self.registry)

        # workflow file
        self.workflow_path = "openclaw/workflows/opus_rag.yaml"

    def turn(self, player_input: str):
        """
        One game turn:
        Player input → AI reasoning → response
        """
        result = self.executor.run(
            workflow_path=self.workflow_path,
            user_query=player_input
        )
        return result
