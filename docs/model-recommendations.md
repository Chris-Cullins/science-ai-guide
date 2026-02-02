# Which Models Should I Use?

The short answer: use the best model your tool supports. As of early 2026, two models stand out for agentic coding work.

## The top tier

### Claude Opus 4.5 (Anthropic)

**Use with:** Claude Code, GitHub Copilot, Cursor

Opus 4.5 is currently the best model for agentic coding tasks. It leads on real-world software engineering benchmarks (80.9% on SWE-bench Verified) and handles complex, multi-step workflows with fewer dead-ends than competitors.

Why it works well for scientists:

- **Fewer tokens, better results**: Opus 4.5 uses dramatically fewer tokens than predecessors to reach the same outcomes—76% fewer in some benchmarks. This means lower costs and faster responses.
- **Strong reasoning**: Major improvements in abstract reasoning make it effective for task decomposition, planning, and multi-file changes.
- **Reliable for long tasks**: Designed for sustained work over hours, not just quick answers.

Pricing: $5 / $25 per million tokens (input/output)—significantly cheaper than earlier Opus models.

### GPT-5.2 High Thinking (OpenAI)

**Use with:** Codex CLI

If you're using OpenAI's Codex CLI (because you already have a ChatGPT subscription), GPT-5.2 with high reasoning effort is the model to use.

Why it works well for scientists:

- **Optimized for agentic coding**: GPT-5.2-Codex is specifically tuned for long-horizon coding tasks, with improvements in context handling and large refactors.
- **Strong on math**: Achieves 100% on AIME 2025 mathematical reasoning benchmarks.
- **Reasoning effort settings**: You can dial up "thinking" effort (low/medium/high/xhigh) depending on task complexity.

Use `high` or `xhigh` reasoning effort for complex scientific code. Use `medium` for routine tasks to save tokens.

## How to set the model

### Claude Code

Claude Code uses Opus 4.5 by default on Pro/Max plans. You can verify or change your model:

```bash
claude config get model
claude config set model claude-opus-4-5-20251101
```

For lighter tasks (drafts, simple refactors), you can switch to Sonnet to save costs:

```bash
claude config set model claude-sonnet-4-20250514
```

### Codex CLI

Codex CLI uses GPT-5.2-Codex by default for paid ChatGPT users. To set reasoning effort:

```bash
codex --reasoning high
```

Or in your config file, set `reasoning: high` as the default.

### Cursor

In Cursor settings, select "claude-opus-4-5" as your primary model. Cursor supports multiple providers, so you can also configure fallbacks.

### GitHub Copilot

GitHub Copilot's agent mode uses Claude Opus 4.5 when available. Check your Copilot settings to ensure you're on a plan that supports it (Pro or Enterprise).

## Other models worth knowing

### Gemini 3 Pro (Google)

Gemini 3 Pro has a massive 1 million token context window (5x larger than Claude, 2.5x larger than GPT-5.2). This is useful for:

- Processing entire codebases in one session
- Very long documents or research papers
- Multimodal tasks involving images

However, for pure coding reliability, Opus 4.5 and GPT-5.2 currently outperform it on most benchmarks.

### Sonnet 4.5 (Anthropic)

Anthropic's mid-tier model. Use it for:

- Routine refactors where you don't need maximum reasoning power
- Cost-sensitive work (significantly cheaper than Opus)
- Tasks where you'll verify results anyway

A good workflow: use Sonnet for drafts and exploration, switch to Opus for final implementation and complex debugging.

## Model selection by task

| Task | Recommended model |
|------|-------------------|
| Complex debugging, multi-file refactors | Opus 4.5 or GPT-5.2 High |
| Math-heavy code, numerical methods | GPT-5.2 High or Opus 4.5 |
| Routine refactors, simple scripts | Sonnet 4.5 or GPT-5.2 Medium |
| Processing very long documents | Gemini 3 Pro |
| Quick drafts, exploration | Sonnet 4.5 |
| High-stakes final implementation | Opus 4.5 |

## The model landscape changes fast

This page reflects the state of things in early 2026. Model capabilities shift every few months. The general principle holds: use the best model your budget and tooling support for important work, and drop to cheaper models for routine tasks.

Check the official pricing and model pages for current information:

- [Anthropic models and pricing](https://www.anthropic.com/pricing)
- [OpenAI models](https://platform.openai.com/docs/models)
- [Google AI models](https://ai.google.dev/models)

## See also

- [Multi-Model Strategy](multi-model.md)
- [Cost Control](cost-control.md)
- [Pick Your Tools](tooling.md)
