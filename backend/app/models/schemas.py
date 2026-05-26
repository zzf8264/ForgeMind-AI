from pydantic import BaseModel, Field


class LoginRequest(BaseModel):
    email: str
    password: str


class TaskRequest(BaseModel):
    objective: str = Field(..., examples=["Analyze repository and open a remediation plan"])
    repository: str = Field(default="github.com/forgemind/monorepo")
    agent: str = Field(default="CodingAgent")
    priority: str = Field(default="normal")
