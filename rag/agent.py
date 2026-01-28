from rag.pipeline import rag_answer

class RAGAgent:
    def __init__(self, max_steps=3):
        self.max_steps = max_steps

    def run(self, user_query: str):
        thoughts = []
        observation = None

        for step in range(self.max_steps):
            thought = f"Step {step+1}: I should retrieve relevant information."
            thoughts.append(thought)

            observation = rag_answer(user_query)

            # Simple stop condition
            if observation:
                break

        return {
            "final_answer": observation,
            "thoughts": thoughts
        }
