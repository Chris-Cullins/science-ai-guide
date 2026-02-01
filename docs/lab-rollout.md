# Lab Rollout Playbook

This is a lightweight way to adopt agentic AI tools without creating chaos.

## 1) Decide what is allowed

- Allowed: public papers, public code, synthetic data, toy examples
- Caution: unpublished results, collaborator material, embargoed data
- Usually not allowed without explicit approval: human-subject data, patient data, credentials, proprietary industry data

Write the decision down (one page) and make it easy to follow.

## 2) Standardize the workflow

- Use repos for analysis (even if small).
- Require diffs and "verification commands" for code changes.
- Prefer small PRs / small changes.

## 3) Standardize prompts (seriously)

Put a few prompt templates in a shared doc and encourage people to reuse them.
See: `docs/prompts.md`.

## 4) Track what the tool did

- For analysis: record parameters, versions, seeds, and data hashes.
- For writing: record which sections were AI-assisted and how you validated claims.

## 5) Teach "verification thinking"

- Always ask: "What would prove this wrong?"
- Build tiny checks: limiting cases, invariants, synthetic datasets.
