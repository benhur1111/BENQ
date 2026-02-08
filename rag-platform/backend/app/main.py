from fastapi import FastAPI
from app.db.redis import create_vector_index
from app.rag.code_reasoning import router as code_router

app.include_router(code_router)

app = FastAPI(title="RAG Platform")

@app.on_event("startup")
async def startup():
    create_vector_index()

