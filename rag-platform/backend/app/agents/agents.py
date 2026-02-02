import ollama
from app.agents.tools import TOOLS


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
    def __init__(sself, session_id: str, user_query: str):
        memory = load_memory(session_id)

        messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        messages.extend(memory)
        messages.append({"role": "user", "content": user_query})

        response = ollama.chat(
            model=self.model,
            messages=messages
        )

        answer = response["message"]["content"]

        # Save memory
        save_memory(session_id, "user", user_query)
        save_memory(session_id, "assistant", answer)

        return answer
