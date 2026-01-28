from fastapi import APIRouter
from agents.agent import ClaudeStyleAgent

router = APIRouter(prefix="/ai", tags=["AI"])

agent = ClaudeStyleAgent()

@router.post("/agent")
def agent_endpoint(query: str):
    return {
        "response": agent.run(query)
    }
