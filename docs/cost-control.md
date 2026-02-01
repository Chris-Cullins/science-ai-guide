# Cost Control (Avoid Surprises)

Costs can creep up, especially if you use multiple tools or run big jobs.

## The two main cost drivers

1. Volume: how many requests you make
2. Size: how much context you feed each request (tokens)

## Practical ways to reduce cost

- Keep tasks small and incremental.
- Reuse instructions instead of repeating long context.
- Provide small samples instead of full datasets.
- Ask for a plan before expensive execution.

## A good default: tier your work

- Cheap model for drafting/refactors
- Strong model for final reasoning and tricky debugging

## Institutional budgeting

If your lab is paying:

- pick a single primary tool
- track usage monthly
- decide in advance when to approve upgrades

See also: `docs/pricing.md`
