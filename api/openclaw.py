from fastapi import APIRouter
from openclaw.engine.executor import WorkflowExecutor
from api.schemas import OpenClawRunRequest, OpenClawRunResponse

router = APIRouter(prefix="/openclaw", tags=["OpenCLaW"])

@router.post("/run", response_model=OpenClawRunResponse)
def run_workflow(request: OpenClawRunRequest):
    executor = WorkflowExecutor("app/openclaw/workflows")

    result = executor.run(
        workflow_name=request.workflow_name,
        inputs={"query": request.query}
    )

    return {
        "status": "success",
        "result": result
    }
