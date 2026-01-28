import numpy as np
from redis.commands.search.query import Query
from db.redis import get_redis, REDIS_INDEX


def retrieve_docs(query_embedding, top_k: int = 3):
    redis_client = get_redis()

    q = Query(
        f"*=>[KNN {top_k} @embedding $vec AS score]"
    ).sort_by("score").return_fields("content").dialect(2)

    params = {"vec": np.array(query_embedding, dtype=np.float32).tobytes()}

    results = redis_client.ft(REDIS_INDEX).search(q, query_params=params)

    return [doc.content.decode("utf-8") for doc in results.docs]
