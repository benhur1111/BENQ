from app.db.redis import redis_client
import json
from typing import List, Dict

MEMORY_LIMIT = 10  # last N messages

def _memory_key(session_id: str) -> str:
    return f"memory:{session_id}"

def load_memory(session_id: str) -> List[Dict]:
    key = _memory_key(session_id)
    data = redis_client.get(key)
    if not data:
        return []
    return json.loads(data)

def save_memory(session_id: str, role: str, content: str):
    key = _memory_key(session_id)
    memory = load_memory(session_id)

    memory.append({
        "role": role,
        "content": content
    })

    # keep last N messages only
    memory = memory[-MEMORY_LIMIT:]

    redis_client.set(key, json.dumps(memory))
