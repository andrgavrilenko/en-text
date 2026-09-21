---
name: en-score
description: >
  Score English text 0.0-10.0 across five dimensions: sentence clarity, flow and
  cohesion, human voice, correctness, precision for the reader. Triggers: score
  this, rate this text, how good is this writing, how much does this read like AI,
  en-score. Use when the user wants a number rather than a list of findings.
  Never edits a file.
allowed-tools: Read, Grep, Glob
disallowed-tools: Write, Edit, NotebookEdit, Bash, PowerShell
context: fork
user-invocable: true
---

# English Text Quality Score

Score the text in $ARGUMENTS. With no arguments, score the most recent English text
in the conversation. If $ARGUMENTS names a file or a glob, read those files.

## Where the corpus lives

Find a directory named `references` whose parent directory is named `en-text`. It
sits next to this skill, typically at `../en-text/references/`. Read `scoring.md`
first; it governs everything below. Read `slop.md` for the density table, and
`clarity.md` and `usage.md` as needed to identify what you are counting.

If the corpus is missing, say so and stop. A number produced from memory is not an
en-text score.

## Procedure

1. **Count.** Words of running prose, excluding code blocks, tables, front matter,
   and quoted material. State the count.
2. **Identify the genre and weights.** Default weights are in `scoring.md`. If the
   genre shifts them, say which weights you used and why.
3. **Score each dimension** against its anchor table. Count instances before
   assigning a number; do not score by impression.
4. **Combine** with the weights and report to one decimal. Show the arithmetic to
   yourself before printing: the total must follow from the sub-scores.
5. **Name the three findings that cost the most points**, each with its rule ID.

## Output

```
Reviewed as: engineering blog post, US spelling, default weights. 840 words.

Score: 6.1 / 10

  Sentence clarity       5.5   ██████░░░░
  Flow and cohesion      7.0   ███████░░░
  Human voice            4.0   ████░░░░░░
  Correctness            8.5   █████████░
  Precision              7.0   ███████░░░

Costing the most:
  [S16] Every bullet opens with a bolded label and runs the same length.
  [C4]  Six empty verb plus nominalization pairs in 840 words.
  [S11] "Whether you're scaling a startup or maintaining a monolith."

Cheapest 2 points: rewrite the bullet list as prose and fix the empty verbs.
```

## Honesty rules

- **Do not grade on a curve.** A competent business email is a 7. Eight is good.
  Nine is rare. If your scores cluster above 8, the scale has stopped measuring.
- **Never report a number without findings.** A bare score is theater.
- **Do not reward length, vocabulary, or formatting effort.** A 90-word answer that
  lands can score 10.
- **State your assumptions** (genre, weights, spelling variant, house style) in the
  line above the score. They change the number, so the reader must see them.
- **Never edit the file.** This skill reports; it does not rewrite. If the user
  wants the text fixed, point them at `en-check`.
