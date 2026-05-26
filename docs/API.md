# API

Base URL: `http://localhost:8000/api`

## Health

`GET /health`

Returns service and dependency health.

## Login

`POST /auth/login`

```json
{
  "email": "admin@forgemind.ai",
  "password": "forgemind"
}
```

## Agents

`GET /agents`

Lists available enterprise agents and capabilities.

## Tasks

`POST /tasks`

```json
{
  "agent": "CodingAgent",
  "repository": "github.com/acme/platform",
  "objective": "Refactor retry handling and add focused tests",
  "priority": "critical"
}
```

## Usage

`GET /usage`

Returns monthly tokens, daily agent runs, spend, concurrent tasks, and workload breakdown.

## WebSocket Streaming

`ws://localhost:8000/ws/agent-runs/{run_id}`

Streams phase updates and token counters for a live agent run.
