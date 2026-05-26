from fastapi import APIRouter, Depends, HTTPException

from app.core.auth import create_access_token, verify_password
from app.models.schemas import LoginRequest, TaskRequest
from app.services.agent_runtime import AgentRuntime
from app.services.metrics import usage_snapshot
from app.services.repository_service import repositories_snapshot
from app.services.tool_registry import ToolRegistry

router = APIRouter()
runtime = AgentRuntime()
tools = ToolRegistry()


@router.get("/health")
def health() -> dict:
    return {
        "status": "ok",
        "service": "forgemind-control-plane",
        "region": "us-east-1",
        "dependencies": {
            "postgres": "ready",
            "redis": "ready",
            "qdrant": "ready",
        },
    }


@router.post("/auth/login")
def login(payload: LoginRequest) -> dict:
    if payload.email != "admin@forgemind.ai" or not verify_password(payload.password, "forgemind"):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {
        "access_token": create_access_token({"sub": payload.email, "role": "platform-admin"}),
        "token_type": "bearer",
    }


@router.get("/agents")
def list_agents() -> dict:
    return {"agents": runtime.catalog()}


@router.post("/tasks")
async def create_task(payload: TaskRequest) -> dict:
    return await runtime.dispatch(payload)


@router.get("/tasks")
def list_tasks() -> dict:
    return {"tasks": runtime.recent_runs()}


@router.get("/usage")
def usage() -> dict:
    return usage_snapshot()


@router.get("/repositories")
def repositories() -> dict:
    return repositories_snapshot()


@router.get("/tools")
def list_tools() -> dict:
    return {"tools": tools.list_tools()}
