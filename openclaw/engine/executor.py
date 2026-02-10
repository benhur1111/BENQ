import yaml
from pathlib import Path
import yaml

WORKFLOW_DIR = Path("openclaw/workflows")

class WorkflowExecutor:
    def __init__(self, registry):
        self.registry = registry

    def load(self, path):
        with open(path) as f:
            return yaml.safe_load(f)

    def run(self, workflow_path, user_query):
        workflow = self.load(workflow_path)
        state = {"user_query": user_query}

        for step in workflow["steps"]:
            component = self.registry.get(step["component"])
            inputs = {}

            for k, v in step.get("input", {}).items():
                if "." in v:
                    obj, attr = v.split(".")
                    inputs[k] = state[obj][attr]
                else:
                    inputs[k] = state[v]

            result = component.run(**inputs)
            state[step["name"]] = result

        return state
