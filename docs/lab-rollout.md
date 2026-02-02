# Lab Rollout Playbook

Adopting agentic AI as a lab is different from adopting it as an individual. You need to think about consistency, training, policies, and making sure no one accidentally leaks sensitive data.

This page is a practical playbook for lab leaders who want to introduce these tools without creating chaos.

## Before you start

### Understand the risks

Before rolling out to your lab, be clear-eyed about what can go wrong:

- **Data leaks**: Someone pastes patient data into an external tool
- **Bad science**: Someone trusts AI-generated statistics without checking
- **Reproducibility failures**: AI-assisted work can't be replicated
- **Citation fraud**: AI invents references that make it into papers
- **Skill atrophy**: Students never learn to code/debug properly

None of these are reasons to avoid AI entirely. They're reasons to roll out carefully.

### Know your institution's policies

Before anything else:

1. Check if your institution has an AI policy
2. Check if your IRB has guidance on AI for human-subjects research
3. Check if IT has approved specific tools
4. Check if your funding agencies have requirements

If policies exist, follow them. If they don't, document your own approach.

## Step 1: Decide what data is allowed

This is the most important decision. Get it wrong and you have a serious problem.

### Create a clear data classification

**Green (safe to share):**
- Published papers and public datasets
- Open-source code
- Synthetic or simulated data
- General questions about methods

**Yellow (caution required):**
- Unpublished manuscripts (embargoed material)
- Collaborator data without explicit permission
- Internal lab protocols and methods
- Pre-publication results

**Red (never share without explicit approval):**
- Human-subjects data (surveys, interviews, medical records)
- Patient or clinical data
- Student records
- Proprietary industry data
- Anything covered by NDA, HIPAA, FERPA, etc.
- API keys, passwords, credentials

### Write it down

Create a one-page document with your lab's classification. Make it impossible to misunderstand:

```markdown
# Lab AI Data Policy

## What you CAN share with external AI tools:
- Public datasets and code
- Synthetic data
- General coding questions
- Published literature

## What you CANNOT share:
- Any data from human subjects
- Any patient or clinical data
- Unpublished results without PI approval
- Anything from collaborators without their explicit permission

## When in doubt: ASK FIRST
Contact: [your email]
```

Post this prominently. Include it in onboarding materials.

## Step 2: Standardize the tools

Having everyone use the same tool makes training easier, troubleshooting possible, and policies enforceable.

### Pick a primary tool

Choose one agentic tool as your lab's default. Recommended:

- **Claude Code** if you can budget Pro/Max subscriptions
- **Codex CLI** if everyone already has ChatGPT plans
- **Cursor** if your lab is IDE-centric

See [Pick Your Tools](tooling.md) for details.

### Set up consistent access

- Get institutional/team accounts if available (better for billing, policies)
- If using individual accounts, ensure everyone has the same tier
- Document how to get access in your lab wiki/onboarding docs

### Consider a shared config

For Claude Code, create a lab-wide `CLAUDE.md` template:

```markdown
# Lab Standards

When working on this lab's code:

- Do not change scientific logic without explicit approval
- Always propose a plan before making large changes
- Run verification after every significant edit
- Do not add citations - we verify all references manually
- Document any assumptions you make
```

New projects can start with this template.

## Step 3: Standardize the workflow

Consistency reduces errors. Define how AI-assisted work should be done.

### The default workflow

Train everyone to follow plan → do → verify:

1. **Plan**: Ask the agent for a plan before large changes
2. **Do**: Let it implement in small, reviewable steps
3. **Verify**: Run tests, check outputs, review diffs
4. **Record**: Commit with clear messages, document what was AI-assisted

### Require version control

No exceptions. Every project should be in git:

- Creates an audit trail of what changed
- Enables easy rollback when AI makes mistakes
- Makes diff review natural
- Supports reproducibility

### Define verification expectations

What counts as "verified"? Define it:

```markdown
Before merging AI-assisted code:
1. Review the diff line-by-line
2. Run the test suite (must pass)
3. Verify key outputs against known values
4. For figures: confirm axes, labels, units are correct
5. For statistics: spot-check calculations manually
```

## Step 4: Standardize prompts

This sounds bureaucratic, but it prevents a lot of mistakes.

### Create lab prompt templates

Put templates in a shared doc that everyone uses:

```markdown
## For refactoring

Refactor this code for clarity and maintainability.

Rules:
- Do not change scientific logic
- Keep numerical outputs identical
- Explain any non-obvious changes

Verification: Run [test command] and compare outputs to before.

## For debugging

I'm getting this error: [paste error]
The code is in [file path].
It should [expected behavior].

Please identify the root cause, propose a fix, and explain what went wrong.

## For figure generation

Create a script for Figure [N] that:
- Reads data from [path]
- Uses parameters from a config file
- Saves output to results/figures/
- Prints summary stats for verification
```

See [Prompt Templates](prompts.md) for more examples.

### Why this matters

Standardized prompts:
- Encode your lab's norms (verification, no changing science)
- Reduce variability in quality
- Make it easier to train new members
- Prevent common mistakes

## Step 5: Train the lab

Don't just announce AI tools are available. Train people to use them well.

### Recommended training

1. **Group demo** (1 hour): Show the tool, walk through a real example
2. **Bootcamp** (2 days): Have everyone complete [Bootcamp](bootcamp.md)
3. **Paired sessions**: New users work alongside experienced ones initially
4. **Office hours**: Regular time for questions and troubleshooting

### Focus training on verification

The biggest risk is people trusting AI output blindly. Emphasize:

- How to read and understand diffs
- How to write verification tests
- How to spot common AI mistakes
- When to be skeptical (statistics, citations, scientific logic)

## Step 6: Track and document

### Track what the AI did

For important analyses, record:

- Which tool/model was used
- What prompts were given (or representative examples)
- What verification was performed
- Who reviewed the output

This isn't bureaucracy for its own sake—it's reproducibility.

### Document for papers

Create a standard way to document AI assistance for manuscripts:

```markdown
## AI Assistance Log for [Paper Title]

### Code assistance
- Refactored data loading pipeline (Claude Code, reviewed by [name])
- Generated pytest suite (Claude Code, all tests manually verified)
- Debugged memory leak in simulation (Claude Code)

### Writing assistance
- Clarity editing of Methods section (Claude, reviewed by [name])
- No AI-generated citations

### Figures
- All figure scripts written with AI assistance
- All figures verified against expected values
```

This makes disclosure easy when it's time to submit.

## Step 7: Handle mistakes

Mistakes will happen. Have a plan.

### When AI-assisted code produces wrong results

1. Identify what's wrong and document it
2. Revert to last known-good state (git makes this easy)
3. Figure out why verification didn't catch it
4. Improve verification for next time

### When sensitive data is accidentally shared

1. Document exactly what was shared and when
2. Notify your PI and/or compliance office
3. Follow your institution's incident response procedure
4. Update policies/training to prevent recurrence

### When someone publishes without proper verification

This is a serious issue. Handle it like any other scientific error:
- Issue corrections if needed
- Understand how it happened
- Improve processes

## Making it sustainable

### Regular check-ins

Monthly or quarterly, ask:

- Is the tool saving time?
- What mistakes are happening?
- What should we do differently?
- Are policies still appropriate?

### Stay current

Tools and norms change rapidly. Assign someone to:

- Monitor updates to your chosen tools
- Track changes in journal/funder policies
- Share relevant news with the lab

### Keep the bar for verification high

As people get comfortable, there's a temptation to verify less carefully. Resist this. The verification habit is what makes AI assistance safe.

## See also

- [Lab Policy Template](lab-policy-template.md)
- [Safety, Privacy, and Policy](safety-privacy.md)
- [Disclosure](disclosure.md)
- [Bootcamp (2 Days)](bootcamp.md)
