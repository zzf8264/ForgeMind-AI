# Deployment

## Docker Compose

```bash
cd infra
docker compose up --build
```

This starts the frontend, backend, PostgreSQL, Redis, Qdrant, Prometheus, and Grafana.

## Kubernetes

```bash
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/backend-deployment.yaml
kubectl apply -f k8s/frontend-deployment.yaml
kubectl apply -f k8s/hpa.yaml
```

Production deployments should mount secrets for `JWT_SECRET`, database credentials, Redis credentials, Qdrant API keys, and model provider keys.

## Multi-region

ForgeMind AI is designed for active-active regions:

- us-east-1 for primary engineering workloads
- eu-west-1 for EU data residency
- ap-southeast-1 for APAC latency reduction

Use regional Redis queues and Qdrant collections. Replicate ledger data asynchronously into a reporting warehouse.
