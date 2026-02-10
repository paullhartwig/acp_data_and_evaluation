# Subtle Detail

Goal: Multiple back-end templates seem plausible; a small requirement should determine the winner.

Initial prompt:
```
We need a Node.js REST API with Postgres. It must include background workers for scheduled jobs and health/readiness endpoints. No frontend included.
```

Spec fields to collect:
- app_purpose: Node.js REST API with Postgres and background workers
- deployment_runtime: containerized service
- tech_stack: Node.js, Express (or similar), Postgres
- constraints: no frontend; workers required

Ground-truth template: node-postgres-backend.yaml
Candidate templates to include: node-postgres-backend.yaml, node-postgres.yaml, clean-architecture-app.yaml

Evaluation notes: The presence of background workers and health checks should bias toward the backend template. Penalize choices that return a pure CRUD starter without worker support.
