from fastapi import APIRouter
from rag.pipeline import rag_pipeline

router = APIRouter(prefix="/ai", tags=["AI"])


@router.post("/search")
async def ai_search(query: str):
    # TEMP embedding (mock)
    fake_embedding = [0.0] * 1536

    response = rag_pipeline(query, fake_embedding)
    return {"response": response}
