# Disclosure and Attribution

Using AI in research raises questions about transparency. What do you need to disclose? When? To whom? The norms are still evolving, but this page covers the current best practices.

## The core principle

**Be honest about how your work was produced.**

If AI assistance materially contributed to your code, analysis, or writing, say so. Not because AI is bad, but because transparency is a scientific value.

## What to disclose

### Definitely disclose

- AI-generated text that appears in the manuscript
- AI-assisted code that produced key results or figures
- AI-generated figures or visualizations
- Significant refactoring or debugging done by AI

### Probably disclose

- AI-assisted literature review or summarization
- AI help with LaTeX formatting or equation typesetting
- AI-generated boilerplate (Makefiles, configs, tests)

### Usually not necessary to disclose

- Using AI for grammar/spelling checks (similar to Grammarly)
- Asking AI to explain a concept you then applied yourself
- Using AI as a search engine or documentation lookup

The line is: did the AI do substantive intellectual work that appears in the final output?

## How to disclose

### In papers and manuscripts

Most journals now have specific policies. Check your target journal first.

If they don't have a policy, add a disclosure in the methods or acknowledgments:

**Example (minimal):**
```text
We used AI-assisted tools (Claude Code) for code refactoring and debugging.
All scientific analyses and conclusions were performed and verified by the authors.
```

**Example (detailed):**
```text
AI assistance was used in the following ways:
- Code refactoring and test generation (Claude Code)
- Clarity editing of manuscript text (Claude)
- LaTeX formatting of equations

All scientific claims, analyses, statistical interpretations, and conclusions
were performed by the authors. AI-generated code was reviewed via diff and
verified against expected outputs. No AI-generated citations were used; all
references were verified by the authors.
```

### In grant proposals

Check your funding agency's policy. NSF, NIH, and others are developing guidelines.

A safe default:
```text
AI writing assistance was used to improve clarity and structure.
All scientific content, proposed methods, and claims of novelty are the
original work of the investigators.
```

### In code repositories

Add a note to your README:

```markdown
## AI Assistance

This codebase was developed with assistance from Claude Code.
AI-generated code was reviewed and tested by the authors.
Commit history shows the evolution of AI-assisted changes.
```

## What NOT to do

### Don't list AI as an author

AI systems cannot take responsibility for the work, respond to reviewer comments, or be held accountable for errors. Author status requires accountability.

### Don't let AI invent citations

AI will confidently generate plausible-looking citations that don't exist. Every reference must be verified by a human.

**Bad:** "According to Smith et al. (2023)..." [AI generated this]

**Good:** [You found and read the actual paper, then cited it]

### Don't hide AI involvement

If reviewers or readers later discover significant AI involvement that wasn't disclosed, it damages trust. Be upfront.

### Don't over-claim AI contribution

If you used AI for spell-checking, you don't need a paragraph about it. Match the disclosure to the significance.

## Journal policies (as of 2026)

Policies vary by journal and change frequently. Check your target journal directly.

**Common patterns:**

- **Nature family:** Requires disclosure of AI use; AI cannot be an author
- **Science family:** Similar requirements; emphasis on human accountability
- **PNAS:** Requires disclosure; provides template language
- **IEEE/ACM:** Varies by specific journal; check guidelines
- **arXiv:** No specific policy; use your judgment

**To find a journal's policy:**

1. Check the "Instructions for Authors" or "Author Guidelines"
2. Search for "AI" or "artificial intelligence" or "language model"
3. If nothing found, contact the editor

## Reproducibility as a form of transparency

The best disclosure is reproducibility. If your code is public and your workflow is documented:

- Others can see exactly what the AI did (via commit history)
- Others can verify results independently
- The AI's contribution is implicitly visible

This is better than a vague disclosure statement.

## When you're unsure

Ask yourself:

1. Would I be comfortable if a reviewer knew exactly how this was produced?
2. Would I be comfortable if it appeared in a news story?
3. Does the disclosure match what I would want to read if I were the reader?

If the answer is "no" to any of these, add more transparency.

## The evolving landscape

AI use in research is new. Norms will shift. The safe approach:

- Be more transparent than you think necessary
- Keep records of how AI was used
- Stay informed about your field's evolving standards
- When in doubt, disclose

In five years, this will all be clearer. For now, err on the side of openness.

## See also

- [Safety, Privacy, and Policy](safety-privacy.md)
- [Reproducibility](reproducibility.md)
- [Lab Policy Template](lab-policy-template.md)
