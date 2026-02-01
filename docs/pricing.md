# Pricing (Double-Check Before Publishing)

Pricing changes frequently. This page is a snapshot of publicly listed pricing as of 2026-02-01.

## Claude subscriptions (includes Claude Code)

From Anthropic's pricing page (Individual plans):

- Free: $0
- Pro: $17/month with annual discount ($200 billed up front) or $20 billed monthly; includes access to Claude Code
- Max: from $100/month

Source: https://www.anthropic.com/pricing

## Claude API pricing (if you build custom tools)

From Anthropic's pricing page (API):

- Opus 4.5: $5/MTok input, $25/MTok output
- Sonnet 4.5: $3/MTok input and $15/MTok output for prompts <= 200K tokens (higher prices for >200K)
- Haiku 4.5: $1/MTok input, $5/MTok output

Tools pricing shown there also includes (examples):

- Web search: $10 / 1K searches (not including tokens)
- Code execution: $0.05 per hour per container (after free daily hours per org)

Source: https://www.anthropic.com/pricing

## Alternatives (for comparison)

- Cursor: Free tier; Pro $20/month; Pro+ $60/month; Ultra $200/month
  Source: https://cursor.com/pricing

- GitHub Copilot (individual): Free; Pro $10/month; Pro+ $39/month
  Source: https://github.com/features/copilot/plans

- ChatGPT plans are listed at: https://openai.com/pricing

## Cost control tips

- Prefer smaller tasks and incremental diffs (reduces rework).
- Save reusable instructions in a project-level "rules" file (reduces repeated context).
- Don't upload giant datasets when a small sample + schema is enough.
