import os
from config import LLM_PROVIDER

# ---- MOCK ----
def mock_generate(prompt: str) -> str:
    return f"[MOCK RESPONSE]\n{prompt[:200]}..."


# ---- OLLAMA ----
def ollama_generate(prompt: str) -> str:
    import requests

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama3", "prompt": prompt, "stream": False},
        timeout=60,
    )
    return response.json()["response"]


# ---- OPENAI ----
def openai_generate(prompt: str) -> str:
    from openai import OpenAI

    client = OpenAI()

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content


def generate_answer(prompt: str) -> str:
    if LLM_PROVIDER == "mock":
        return mock_generate(prompt)
    if LLM_PROVIDER == "ollama":
        return ollama_generate(prompt)
    if LLM_PROVIDER == "openai":
        return openai_generate(prompt)

    raise ValueError("Invalid LLM_PROVIDER")
