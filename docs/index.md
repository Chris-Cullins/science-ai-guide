# Agentic AI for Scientists

This guide is for scientists who are *not* professional software developers, but who do write code, analyze data, and produce papers.

The core idea: instead of using an AI model like a chat box, you use an *agent* that can take actions (read/write files, run commands, iterate) with you supervising.

## Recommended reading path

If you are new:

1. `docs/overview.md`
2. `docs/why-agentic.md`
3. `docs/tooling.md`
4. `docs/first-hour.md`
5. `docs/workflows.md`
6. `docs/verification.md`

If you are leading a lab:

1. `docs/lab-rollout.md`
2. `docs/lab-policy-template.md`
3. `docs/reproducibility.md`
4. `docs/safety-privacy.md`

## Where to start

1. Install and try Claude Code on a small, non-sensitive project: `docs/claude-code.md`
2. Learn the core workflow loop (plan -> do -> verify): `docs/workflows.md`
3. Set guardrails for privacy, safety, and reproducibility: `docs/safety-privacy.md`
4. Copy/paste prompt templates you can actually use: `docs/prompts.md`
5. Understand costs and avoid surprises: `docs/pricing.md`

If you are onboarding a lab:

- First hour checklist: `docs/first-hour.md`
- Lab rollout: `docs/lab-rollout.md`
- Disclosure/attribution: `docs/disclosure.md`
- Reproducibility habits: `docs/reproducibility.md`

## A quick mental model

- Chat-only AI: you ask questions; you copy/paste results.
- Agentic AI: you give a task; it edits files and runs commands; you review diffs and outputs.

If you can supervise work and verify results, agentic tools can compress days of "yak shaving" (setup, plumbing, debugging, refactors) into hours.
