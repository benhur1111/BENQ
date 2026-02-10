from openclaw.engine.executor import WorkflowExecutor
from openclaw.engine.registry import ComponentRegistry
from openclaw.memory.short_term import ShortTermMemory
from openclaw.memory.long_term import LongTermMemory

class DungeonMaster:
    def __init__(self, llm, vector_store):
        self.short_memory = ShortTermMemory()
        self.long_memory = LongTermMemory()
        self.registry = ComponentRegistry(llm, vector_store)
        self.executor = WorkflowExecutor(self.registry)

        self.world_state = {
            "location": "ruined city gate",
            "danger": "medium",
            "npcs": ["guard"]
        }

    def turn(self, player_input: str):
        context = {
            "player_input": player_input,
            "world_state": self.world_state,
            "short_memory": self.short_memory.dump(),
            "long_memory": self.long_memory.recall()
        }

        result = self.executor.run(
            workflow_path="openclaw/workflows/opus_rag.yaml",
            user_query=context
        )

        self._apply_result(result)
        return result["narration"]

    def _apply_result(self, result):
        if "memory" in result:
            self.short_memory.add(result["memory"])

        if "world_update" in result:
            self.world_state.update(result["world_update"])
