# Clear Winner

Goal: Ensure the system can pick the obvious winner

Initial prompt:
```
Need a Rust edge-compute service running on Cloudflare Workers. Must deploy to edge network only.
```

# Spec answers (no-fit)

- app_purpose: Latency aware job processing
- deployment_runtime: Cloudflare Workers
- tech_stack: Rust on Workers, KV, Durable Objects
- constraints: must run on Workers; no centralized servers

Ground-truth template: rust-cloudflare-worker
Candidate templates to include: only rust-cloudflare-worker

Evaluation notes: Correct behavior is to choose only this obvious template.
