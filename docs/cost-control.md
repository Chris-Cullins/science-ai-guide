# Cost Control (Avoid Surprises)

AI tools cost money. Costs can creep up, especially if you use multiple tools, run long sessions, or feed large contexts. This page covers how to manage costs without sacrificing productivity.

## Understanding the costs

### Subscription models

Most agentic tools use subscriptions:

| Tool | Free tier | Paid tier | Notes |
|------|-----------|-----------|-------|
| Claude Code | Limited | $20/mo (Pro), $100/mo (Max) | Max includes 5x more usage |
| Cursor | Limited | $20/mo (Pro), $40/mo (Business) | Pro includes fast requests |
| Codex CLI | Limited | Uses existing OpenAI/ChatGPT plan | $20/mo ChatGPT Plus |
| GitHub Copilot | None | $10/mo (Individual), $19/mo (Business) | Free for students/OSS |

For most scientists, a single $20/month subscription is sufficient to start.

### API/usage-based costs

Some tools (or advanced usage) charge per token:

- **Input tokens**: The context you provide (code, docs, conversation history)
- **Output tokens**: What the model generates (usually more expensive)

Rough pricing (varies by model):
- Claude Opus 4.5: ~$15 per million input tokens, ~$75 per million output tokens
- GPT-5.2: Similar range
- Smaller models: 10-50x cheaper

For most interactive use, subscription plans are more predictable. API pricing matters for automation or heavy usage.

## The two main cost drivers

### 1. Volume: How many requests you make

Each back-and-forth with the agent costs something. More iterations = more cost.

**Cost-saving strategies:**
- Be specific upfront (fewer clarification rounds)
- Batch related requests together
- Don't start over unnecessarily—resume existing sessions

### 2. Size: How much context you feed

Every time you ask something, the model sees your entire conversation history plus any files it's reading. Long contexts = higher costs.

**Cost-saving strategies:**
- Keep conversations focused
- Start fresh sessions for unrelated tasks
- Don't dump entire codebases—point to specific files
- Use project instructions (CLAUDE.md) instead of repeating context

## Practical ways to reduce cost

### Keep tasks small and incremental

Instead of:
```text
Refactor this entire codebase for better organization
```

Try:
```text
Refactor the data loading functions in src/data.py
```

Smaller tasks = less context = fewer iterations = lower cost.

### Reuse instructions instead of repeating context

If you always want the agent to follow certain rules, put them in your project configuration (CLAUDE.md, .cursorrules, etc.) rather than repeating them each time.

**Expensive (repeated every time):**
```text
Remember, don't change scientific logic without asking.
Also, always run tests after changes.
And use numpy, not loops.
...
[50 lines of instructions]
```

**Cheap (set once):**
```markdown
# CLAUDE.md
- Never change scientific logic without approval
- Run pytest after each code change
- Prefer numpy vectorization over loops
```

### Provide small samples instead of full datasets

Don't paste 10,000 lines of data. Give a representative sample:

```text
Here's a sample of the data format (first 20 rows):
[paste sample]

The full file has 50,000 rows in the same format.
Process data/full_dataset.csv using this format.
```

### Ask for a plan before expensive execution

Before the agent spends tokens on implementation:

```text
Before writing code, outline your approach.
I'll review and we can adjust before you implement.
```

This catches misunderstandings before they become expensive rewrites.

### Use appropriate models for each task

Not every task needs the most powerful (expensive) model.

**Use powerful models (Opus 4.5, GPT-5.2 High) for:**
- Complex debugging
- Tricky algorithmic problems
- Tasks where correctness is critical
- Multi-step reasoning

**Use faster/cheaper models for:**
- Simple refactoring
- Writing tests for existing code
- Generating boilerplate
- Formatting and cleanup

Some tools let you switch models mid-session. Others require configuration.

## Tier your work

A good default strategy:

| Task type | Model tier | Example |
|-----------|------------|---------|
| Drafting, exploration | Cheap/fast | "What approaches could work for X?" |
| Implementation | Standard | "Write a function that does Y" |
| Critical debugging | Premium | "This calculation is wrong and I can't figure out why" |
| Final review | Premium | "Review this for correctness before I publish" |

## Watch for runaway costs

### Signs of trouble

- Very long conversations (100+ turns)
- Repeatedly pasting large files
- The agent going in circles
- Sessions that span multiple days without progress

### What to do

1. **Start fresh**: Long conversations accumulate context. A new session is often more efficient.
2. **Be more specific**: Vague prompts lead to more back-and-forth.
3. **Check your understanding**: If the agent keeps misunderstanding, the problem might be your prompt.
4. **Take a break**: Sometimes stepping away and returning with fresh eyes is the most cost-effective solution.

## Institutional budgeting

If your lab or institution is paying:

### Pick a primary tool

Don't let everyone use different tools. Standardize on one to:
- Simplify billing
- Enable shared knowledge
- Make support easier

### Track usage monthly

Most tools provide usage dashboards. Review them:
- Who's using how much?
- Are costs stable or growing?
- Is the value worth the cost?

### Set expectations

Decide in advance:
- What tier of subscription is standard?
- What usage is "normal" vs. concerning?
- How to handle requests for upgrades?

### Consider institutional licenses

Some tools offer team/institutional pricing that's cheaper per-seat than individual subscriptions. Worth asking about for groups of 5+.

## Cost vs. value

Remember: the goal isn't minimizing cost, it's maximizing value per dollar.

A $100/month subscription that saves 10 hours/month is a great deal ($10/hour for your time back). A $20/month subscription you never use is a waste.

**Questions to ask:**
- Is this tool saving me time?
- Am I using it regularly?
- Could a cheaper option work as well?
- Is the premium tier worth 5x the cost?

## See also

- [Which Models to Use](model-recommendations.md)
- [Pick Your Tools](tooling.md)
- [Lab Rollout](lab-rollout.md)
