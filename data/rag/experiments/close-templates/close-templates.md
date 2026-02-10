# Close Templates

Goal: Several close templates exist, but one requirement makes a single choice correct.

Initial prompt:
```
I need a React web app with server-side rendering for SEO, uses Postgres, and must support authenticated dashboard pages.
```

Spec fields to collect:
- app_purpose: React web app with SEO and authenticated dashboard
- deployment_runtime: containerized web service
- tech_stack: React (SSR), Postgres
- constraints: SSR required; SPA-only solutions are not acceptable

Ground-truth template: react-ssr-postgres-auth.yaml
Candidate templates to include: react-ssr-template.yaml, react-spa.yaml, create-react-app.yaml

Evaluation notes: Must highlight SSR as the decisive factor. Incorrect if it picks SPA or CRA when SSR is explicitly requested.
