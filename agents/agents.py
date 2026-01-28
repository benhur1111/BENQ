import ollama
from agents.tools import TOOLS

SYSTEM_PROMPT = """
You are an AI agent.

You can:
- Answer directly if the question is simple
- Use tools if external knowledge is required

Available tools:
- rag_tool: Use when question requires stored knowledge

Decide the best action.
"""

class ClaudeStyleAgent:
    def __init__(self, model="mistral"):
        self.model = model

    def run(self, user_query: str):
        decision_prompt = f"""
Question: {user_query}

Should you use a tool?
Respond in JSON:
{{
  "action": "tool_name or answer",
  "tool": "rag_tool or null",
  "input": "tool input or final answer"
}}
"""

        response = ollama.chat(
            model=self.model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": decision_prompt}
            ]
        )

        decision = response["message"]["content"]

        # ⚠️ simple safe parse
        if "rag_tool" in decision:
            return TOOLS["rag_tool"]["function"](user_query)

        return decision
