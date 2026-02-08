import ast
from pathlib import Path

class CodeReasoningAgent:
    """
    Claude-like agent that understands Python code structure
    """

    def analyze_file(self, file_path: str, question: str):
        code = self._load_code(file_path)
        tree = ast.parse(code)

        structure = self._extract_structure(tree)
        insights = self._reason(question, structure)

        return {
            "structure": structure,
            "insights": insights
        }

    def _load_code(self, file_path: str) -> str:
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError("File not found")
        return path.read_text()

    def _extract_structure(self, tree):
        return {
            "functions": [
                n.name for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)
            ],
            "classes": [
                n.name for n in ast.walk(tree) if isinstance(n, ast.ClassDef)
            ],
            "imports": [
                ast.unparse(n) for n in ast.walk(tree)
                if isinstance(n, (ast.Import, ast.ImportFrom))
            ],
        }

    def _reason(self, question: str, structure: dict):
        if "function" in question.lower():
            return f"Functions detected: {structure['functions']}"

        if "class" in question.lower():
            return f"Classes detected: {structure['classes']}"

        return "Code analyzed successfully."
