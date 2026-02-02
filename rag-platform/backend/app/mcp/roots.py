from fastapi import APIRouter
from app.agents.agent import ClaudeStyleAgent


router = APIRouter(prefix="/ai", tags=["AI"])

agent = ClaudeStyleAgent()

@router.post("/agent")
def agent_endpoint(session_id: str, query: str):
    return {
        "response": agent.run(session_id, query)
    }

