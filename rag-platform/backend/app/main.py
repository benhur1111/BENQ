from fastapi import FastAPI
from app.db.redis import create_vector_index

app = FastAPI(title="RAG Platform")

@app.on_event("startup")
async def startup():
    create_vector_index()

