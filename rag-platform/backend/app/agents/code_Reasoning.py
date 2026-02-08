from fastapi import APIRouter
from app.agents.code_reasoning_agent import CodeReasoningAgent

router = APIRouter(prefix="/code", tags=["Code Reasoning"])
agent = CodeReasoningAgent()

@router.post("/analyze")
def analyze_code(payload: dict):
    return agent.analyze_file(
        file_path=payload["file_path"],
        question=payload.get("question", "")
    )
