# Prompting Patterns (That Actually Work)

Good prompting is not poetry. It is specifications.

## The 5 things to include

1. Goal: what you want
2. Context: what the agent should look at
3. Constraints: what it must not do
4. Definition of done: how you will verify
5. Output format: what artifacts you want

## A default template

```text
You are helping me with a scientific project.

Goal:
- <what you want>

Context:
- <where to look, what files exist>

Constraints:
- Do not change scientific assumptions without asking.
- Do not invent citations or factual claims.
- Keep changes small and reviewable.

Definition of done:
- <tests / commands / checks that must pass>

Deliverables:
- <files or outputs>
```

## High-leverage patterns

### Ask for a plan first

"Propose a plan before editing files." reduces thrash.

### Force the agent to be explicit about assumptions

"List assumptions and units." catches many scientific errors early.

### Add an adversarial check

"Tell me how this could be wrong." makes verification easier.

## Common failure patterns

- Vague tasks: "make this better"
- No definition of done
- No tests or sanity checks
- Asking for citations without giving sources
