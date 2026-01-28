import os
import redis
from redis.commands.search.field import TextField, VectorField
from redis.commands.search.indexDefinition import IndexDefinition, IndexType

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
REDIS_INDEX = "rag_index"
VECTOR_DIM = 1536  # OpenAI embedding size (safe default)

redis_client = redis.Redis.from_url(REDIS_URL, decode_responses=False)


def get_redis():
    return redis_client


def create_vector_index():
    """
    Creates a Redis vector index if it does not exist.
    Safe to call multiple times.
    """
    try:
        redis_client.ft(REDIS_INDEX).info()
    except Exception:
        schema = (
            TextField("content"),
            VectorField(
                "embedding",
                "FLAT",
                {
                    "TYPE": "FLOAT32",
                    "DIM": VECTOR_DIM,
                    "DISTANCE_METRIC": "COSINE",
                },
            ),
        )

        redis_client.ft(REDIS_INDEX).create_index(
            schema,
            definition=IndexDefinition(prefix=["doc:"], index_type=IndexType.HASH),
        )
