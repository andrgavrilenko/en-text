---
name: en-check
description: >
  Full English text quality check against the whole corpus. Triggers: proofread,
  edit this, review this text, tighten this, does this read like AI, en-check.
  Use when the user asks to proofread or edit English text, or when a project gate
  names en-text. Returns findings, each with the rule behind it and a proposed
  replacement; never edits a file.
allowed-tools: Read, Grep, Glob
disallowed-tools: Write, Edit, NotebookEdit, Bash, PowerShell
context: fork
user-invocable: true
---

# English Text Quality Check

Review the text in $ARGUMENTS. With no arguments, review the most recent English
text in the conversation. If $ARGUMENTS names a file or a glob, read those files.

## Where the corpus lives

This skill reads the reference files that ship with the **en-text** skill, installed
alongside it. Locate the folder once, then read from it:

- Find a directory named `references` whose parent directory is named `en-text`.
  It sits next to this skill, typically at `../en-text/references/`.
- Read `clarity.md`, `slop.md`, `usage.md`, and `method.md`. Read `scoring.md` only
  if the user also asked for a number.

If you cannot find the corpus, say so and stop. Do not improvise rules from memory
and present them as en-text findings.

## Procedure

**1. Frame the text.** Before reading for errors, settle five things and state them
in one line: genre, audience, spelling variant (`U28`), whether a house style
applies (go look for one, `M3`), and whether the text is source or a rendering of it
(`M2`). Every later judgment depends on these. A landing page and an RFC do
not get the same review, and a fetched page cannot answer the questions a dictionary
file can.

If the request names recent edits and asks whether they broke anything, settle one
more thing now: do you have a before state? If not, say so in the same line, and
report findings without attributing them (`M1`).

**2. Triage pass.** Read the whole text once without annotating. Note only:

- word count of running prose (excluding code, tables, quotes)
- how many slop tells you noticed, roughly (`slop.md` density table)
- whether the problems are local (sentences) or structural (order, focus)

If the text is structurally broken, say that first. Polishing sentences inside a
badly ordered document is wasted work, and a reader deserves to know which problem
they have.

**3. Full pass.** Now go rule by rule through the corpus. For each finding record:

- the rule ID
- the span exactly as it appears
- a proposed replacement
- one sentence on what is wrong

**4. Verify before reporting.** Drop any finding that fails one of these:

- The span is inside a quote, a code block, or third-party text.
- The "fix" changes what the sentence claims. Accuracy outranks style.
- The pattern is the author's established voice and costs the reader nothing.
- It is a lone slop tell in a long, otherwise clean text (`slop.md` density table).
- You cannot name the rule. A finding you cannot attribute is taste, not a finding.
- It claims a specific edit introduced the problem and you have no before state
  (`M1`). Keep the finding, drop the attribution.
- It is about pairing, ordering, or agreement, and you are reading a rendering
  rather than the source (`M2`). Report it as something to verify, not as a fact.
- It is one difference that the document's own system explains (`M4`). Collect every
  instance before calling anything inconsistent.

**5. Report.**

## Output

Start with the frame line, then the findings, grouped by severity. No preamble.

```
Reviewed as: engineering blog post, US spelling, no house style. 840 words.

STRUCTURAL
  [C10] Paragraphs 4–6 change subject every sentence: "the scheduler", "users",
        "latency", "our team". Pick one topic per paragraph.
        → Move the team history into its own paragraph after the mechanism.

SENTENCE LEVEL
  [C4] "we performed an evaluation of the retry logic"
       → "we evaluated the retry logic"
       Empty verb carrying a nominalization.

  [C9] "Throughput tripled, based on the benchmark in appendix B."
       → "According to the benchmark in appendix B, throughput tripled."
       The stress position holds an administrative detail instead of the result.

READS AS AI  (7 tells in 840 words, 2.5 per 300: suspicious, not yet a fingerprint)
  [S16] Six bullets, each opening with a bolded label, each one line long.
        → Two of these are argument; make them paragraphs. The rest is a table.

  [S11] "Whether you're scaling a startup or maintaining a monolith"
        → Name the one reader you are writing for.

CONSISTENCY
  [U28] "optimise" in paragraph 2 against "analyze" in paragraph 9. Pick one variant.
```

Close with one line naming what the text does well, only if it is specific and true.
Skip it rather than invent it.

## Boundaries

- **Never write to a file.** Report findings and proposed replacements. If the user
  wants them applied, they will ask, and that is a separate turn with the file tools.
- **Never rewrite quoted material or someone else's byline.**
- **Do not stack hedges onto your own findings.** State the rule and the fix.
- **A self-initiated check** (you noticed the problem; nobody asked) starts with
  triage and escalates only on evidence. An explicit request always runs the full
  corpus.
