from fastapi import FastAPI
from app.db.redis import create_vector_index
from app.rag.code_reasoning import router as code_router
from api.openclaw import router as openclaw_router

app = FastAPI(title="RAG Platform")

# Register routers
app.include_router(code_router)
app.include_router(openclaw_router)

@app.on_event("startup")
async def startup():
    create_vector_index()
