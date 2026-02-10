# Exhaustive Description

Goal: Verify the system uses rich requirements to select a precise template confidently.

Initial prompt:
```
Build an internal API for order management using Java Spring Boot. Needs CRUD, JWT auth, role-based access, Postgres, containerized deployment with Docker, health checks, and readiness probes. No gRPC. Target internal users only.
```

Spec fields to collect:
- app_purpose: internal order management API
- deployment_runtime: containerized service
- tech_stack: Java Spring Boot, Postgres
- constraints: no gRPC

Ground-truth template: spring-boot-postgres.yaml
Candidate templates to include: spring-boot-postgres.yaml, spring-boot-api.yaml, spring-boot-grpc.yaml

Evaluation notes: Should directly pick the Postgres Spring API template without additional questions. Rationale should cite Postgres, JWT auth, and container readiness support.

Notes:
- asking questions about kubernetes or AWS even though these are not factors that are important to the template 
- sometimes "Docker" was an sufficient answer even though it was part of the prompt