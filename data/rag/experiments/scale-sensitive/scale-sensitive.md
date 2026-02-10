# Scale Sensitive

Goal: Same product idea with different scale expectations should lead to different template choices.

Initial prompt A (prototype):
```
Build a simple Spring Boot API for collecting IoT sensor readings, light auth, deploy as a single container for a pilot.
```
Initial prompt B (high scale):
```
Need a production-grade service for IoT sensor ingestion with Spring Boot, Postgres, health/readiness probes, and room for horizontal scaling and background processing.
```

Spec fields to collect:
Variant A (prototype):
- app_purpose: Spring Boot API to collect IoT sensor readings for a pilot
- deployment_runtime: single container
- tech_stack: Spring Boot
- constraints: none beyond pilot scope

Variant B (high scale):
- app_purpose: production IoT sensor ingestion service
- deployment_runtime: containerized, horizontally scalable
- tech_stack: Spring Boot, Postgres
- constraints: prefer built-in probes and room for workers/queues

Ground-truth template: A → spring-boot-api.yaml; B → spring-boot-postgres.yaml (or clean-architecture-app.yaml if prioritizing structure for scale)
Candidate templates to include: spring-boot-api.yaml, spring-boot-postgres.yaml, clean-architecture-app.yaml

Evaluation notes: Expect lighter template for the pilot and a more robust template for high scale. Rationale should cite scaling and health requirements for the B case.

- sometimes giving one answer works and then the next time it does not satisfy the model