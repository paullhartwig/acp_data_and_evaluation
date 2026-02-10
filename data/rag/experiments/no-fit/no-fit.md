# No Fit

Goal: Ensure the system can say "no suitable template" when requirements exceed the catalog.

Initial prompt:
```
Need a Rust edge-compute service running on Cloudflare Workers with KV storage and Durable Objects. Must deploy to edge network only.
```

Spec fields to collect:
- app_purpose: Rust edge-compute service on Cloudflare Workers
- deployment_runtime: Cloudflare Workers
- tech_stack: Rust on Workers, KV, Durable Objects
- constraints: must run on Workers; no centralized servers

Ground-truth template: none (should return no-fit or fallback response)
Candidate templates to include: all templates are irrelevant; verify it refrains from hallucinating a match.

Evaluation notes: Correct behavior is to decline or request alternatives. Any confident template selection counts as failure.

- given all information stated explicitly it can directly fill in all information
