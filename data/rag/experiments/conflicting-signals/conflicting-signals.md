# Conflicting Signals

Goal: Inputs contain incompatible requirements; system should resolve or ask a clarifier before choosing.

Initial prompt:
```
I want a real-time dashboard with WebSockets and background workers for analytics. I'd love to keep it serverless if possible.
```

Spec fields to collect:
- app_purpose: realtime dashboard with analytics updates
- deployment_runtime: ideally serverless, but persistent connections + workers imply containerized service
- tech_stack: Node.js preferred
- constraints: would like serverless, but must reconcile with WebSockets/workers

Ground-truth template: node-postgres-backend.yaml (after resolving that WebSockets + workers need a containerized service)
Candidate templates to include: node-postgres-backend.yaml, node-postgres.yaml, react-spa.yaml

Evaluation notes: Ideal path is to ask a clarifying question about serverless vs persistent connections. Final pick should justify why containerized backend is needed for WebSockets/workers.

- sometimes asking for constraints even though this was not important to the template choosing