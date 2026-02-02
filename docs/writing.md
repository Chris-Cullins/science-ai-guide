# Writing and Grants

AI is very good at clarity and structure. It's also very good at sounding confident while being wrong.

This page covers how to use AI for scientific writing without introducing errors or compromising integrity.

## What AI does well

### Improving clarity

AI excels at making dense prose more readable:

- Shortening long sentences
- Breaking up walls of text
- Improving flow between paragraphs
- Making passive voice active
- Removing jargon where simpler words work

### Improving structure

AI can help organize your thoughts:

- Suggesting better section order
- Identifying gaps in logic
- Creating outlines from rough notes
- Ensuring consistent formatting

### Mechanical tasks

AI handles tedious formatting:

- LaTeX syntax and equation formatting
- Citation formatting (but not finding citations!)
- Table formatting
- Consistent capitalization and style

## What AI does poorly

### Adding factual claims

AI will confidently generate false information. Never let it add claims you haven't verified.

**Dangerous:**
```text
Expand this methods section with more detail.
```

**Safe:**
```text
Improve the clarity of this methods section.
Do not add any new claims or details.
If something is unclear, ask me to provide the information.
```

### Citations

AI invents plausible-sounding but nonexistent references. Every single citation must be verified by a human.

**Bad:**
```text
Add citations to support these claims.
```

**Good:**
```text
Flag where citations are needed. I will add them myself.
```

### Summarizing sources you didn't provide

If you ask AI to summarize "the literature on X," it will make things up. Only ask it to summarize documents you've actually provided.

### Evaluating scientific correctness

AI can't reliably tell if your science is right. It can make your prose clearer, but you must verify the content.

## A workflow that works

### Step 1: You provide the facts

Write a rough draft with all the key points, even if it's messy:

- Your results (numbers, figures, findings)
- Your methods (what you actually did)
- Your interpretations (what you think it means)
- Your references (papers you actually read)

### Step 2: AI improves clarity and structure

```text
Edit this draft for clarity and structure.

Rules:
- Do not add any new claims or information
- Do not add or modify citations
- Do not change scientific conclusions
- If something is unclear, ask me rather than guessing
- Preserve my voice and style

Focus on:
- Sentence clarity
- Paragraph flow
- Removing redundancy
- Consistent terminology
```

### Step 3: You verify everything

Read the edited version carefully:
- Did it change any meanings?
- Did it add anything that wasn't in the original?
- Does every claim still match your data?

This step is not optional.

## Prompts for different writing tasks

### Abstract editing

```text
Edit this abstract for clarity and impact.

Rules:
- Keep it under [X] words
- Do not change any claims or numbers
- Preserve the structure: background, methods, results, conclusion
- Make every sentence earn its place
```

### Methods section

```text
Improve the clarity of this methods section.

Rules:
- Do not add details I haven't provided
- If something is unclear or missing, note it with [NEED: ...]
- Ensure consistent past tense
- Use active voice where appropriate
```

### Introduction structure

```text
Suggest a better structure for this introduction.

Current content: [paste your draft]

I want to:
- Start with [broad context]
- Narrow to [specific problem]
- End with [our contribution]

Give me an outline, then I'll fill in the details.
```

### Results description

```text
Help me describe this figure clearly.

Figure shows: [describe what the figure shows]
Key finding: [what I want readers to take away]

Write a clear paragraph describing this result.
Do not add interpretation beyond what I've stated.
I will add the actual numbers.
```

### Response to reviewers

```text
Help me draft a response to this reviewer comment.

Reviewer said: [paste comment]

My response points:
- [point 1]
- [point 2]
- [what we changed]

Write a professional, clear response.
Keep it respectful but don't be obsequious.
```

## Grant writing

Grant writing has additional considerations: you're making promises about future work.

### What AI can help with

- Structuring the narrative
- Clarifying aims and significance
- Improving readability scores
- Formatting and compliance checks

### What AI should not do

- Claim capabilities you don't have
- Promise results you can't deliver
- Generate preliminary data descriptions
- Write letters of support

### A grant-specific prompt

```text
Edit this grant section for clarity and persuasiveness.

Rules:
- Do not add claims about our capabilities
- Do not add or modify any preliminary data descriptions
- Do not change budget justifications
- Flag any claims that seem unsupported with [VERIFY: ...]

Focus on:
- Clear, active prose
- Logical flow between sections
- Strong topic sentences
- Eliminating jargon
```

## Disclosure

When you use AI for writing, you may need to disclose it. See [Disclosure and Attribution](disclosure.md) for guidance.

Short version:
- Check your target journal/funder's policy
- When in doubt, disclose
- Common language: "AI writing assistance was used for clarity editing. All scientific content is the work of the authors."

## Red flags

Stop and reconsider if:

- The AI added a citation you don't recognize
- The AI made a claim you didn't provide
- The AI "improved" a number or statistic
- The AI changed the meaning of a result
- You're not sure if a sentence is true

When in doubt: check the original, or delete the addition.

## The bottom line

AI is a good editor, not a good author.

- **Use it for:** clarity, structure, formatting, mechanical tasks
- **Don't use it for:** adding content, finding sources, making claims
- **Always:** verify the output against your original intent

Your name is on the paper. You are responsible for every word.

## See also

- [Disclosure and Attribution](disclosure.md)
- [Literature and Notes](literature.md)
- [Prompt Templates](prompts.md)
- [Safety, Privacy, and Policy](safety-privacy.md)
