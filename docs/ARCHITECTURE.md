# Architecture

ForgeMind AI is organized around a control-plane and worker-plane architecture.

```mermaid
flowchart TB
  Console[Next.js Console] --> Control[FastAPI Control Plane]
  Control --> Ledger[(PostgreSQL)]
  Control --> Queue[(Redis Queues)]
  Control --> Vectors[(Qdrant)]
  Queue --> Agents[Agent Worker Pool]
  Agents --> Sandbox[Terminal Sandbox]
  Agents --> Repo[Repository Indexer]
  Agents --> Tooling[Tool Calling]
  Repo --> Vectors
  Control --> Stream[WebSocket Streams]
```

## Core Components

- Frontend console: operational dashboard, agent run explorer, token usage, repositories, and settings.
- FastAPI control plane: authentication, task submission, run metadata, usage snapshots, and streaming.
- Agent runtime: coding, review, repo analysis, DevOps, and documentation agents.
- RAG pipeline: repository discovery, chunking, embedding, and vector upsert.
- Data plane: PostgreSQL for ledgers, Redis for scheduling, Qdrant for semantic retrieval.
- Observability: Prometheus scrape config and Grafana dashboard provisioning.

## Scaling Model

The system supports horizontal API replicas and distributed worker pools. Redis queues separate critical tasks, indexing workloads, and sandbox execution. Kubernetes HPA config scales the backend based on resource utilization, while production worker pools should scale from queue lag and token throughput.
