from app.db.redis import redis_client
from rag.embeddings import embed_text
import uuid

def ingest_document(text: str):
    doc_id = f"doc:{uuid.uuid4()}"

    redis_client.hset(
        doc_id,
        mapping={
            "content": text,
            "embedding": embed_text(text)
        }
    )
