from pydantic import BaseModel
from typing import Dict, Any

class OpenClawRunRequest(BaseModel):
    workflow_name: str
    query: str

class OpenClawRunResponse(BaseModel):
    status: str
    result: Dict[str, Any]
