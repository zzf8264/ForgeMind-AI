from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router
from app.core.config import settings
from app.services.agent_runtime import AgentRuntime

app = FastAPI(
    title="ForgeMind AI Control Plane",
    description="Enterprise multi-agent coding platform API.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

runtime = AgentRuntime()
app.include_router(router, prefix="/api")


@app.websocket("/ws/agent-runs/{run_id}")
async def stream_agent_run(websocket: WebSocket, run_id: str) -> None:
    await websocket.accept()
    try:
        async for event in runtime.stream_run(run_id):
            await websocket.send_json(event)
    except WebSocketDisconnect:
        return
