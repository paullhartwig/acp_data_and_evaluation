# Minimal Description

Goal: Test how the system handles a terse, ambiguous request and whether it defaults to a sensible general-purpose template.

Initial prompt:
```
I need a simple web page to collect user emails.
```

Spec fields to collect:
- app_purpose: simple landing page to collect user emails
- deployment_runtime: static hosting or simple web server
- tech_stack: flexible; React acceptable; static also fine
- constraints: none stated

Ground-truth template: create-react-app.yaml
Candidate templates to include: create-react-app.yaml, react-spa.yaml, react-ssr-template.yaml

Evaluation notes: Should ask 0–1 clarifying questions at most; acceptable if it picks a general SPA starter. Bias should be toward the simplest React starter when details are missing.
