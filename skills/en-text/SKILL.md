---
name: en-text
description: >
  English text quality. Triggers: edit this, proofread, tighten this up, make this
  sound human, does this read like AI, en-text. Catches AI slop, buried subjects,
  nominalizations, and hedging. Applies on request; light cleanup on any English
  draft the agent writes. Route by the language of the text, not of the request.
---

# en-text — English text quality

An independent corpus of English writing rules, written for AI agents rather than
for people. Every rule has an ID and a fix, and the clarity, slop, and method
rules add a test you can run and a stated exception. Findings cite the ID so a
reader can argue with the rule instead of with taste.

`references/sources.md` says where each family of rules comes from and what to read
next.

## What this skill is for

Two problems stack on top of each other. Bad prose existed long before language
models: buried subjects, nominalizations, hedging, sentences that make the reader
hold six things in memory before the verb arrives. Then models added a dialect of
their own: *delve*, *leverage*, *it's not X, it's Y*, three items in every list,
a bolded bullet for every thought. A text can be free of AI tells and still be
unreadable. A text can be perfectly clear and still announce on line one that a
machine wrote it. This corpus treats both.

This corpus covers English only. If the text is not in English, say so and stop. In a
mixed-language text, review the English and leave the rest as it is.

## Priority order

When rules conflict, resolve in this order:

1. **The user's explicit instruction.** When the user asks for a register (legal,
   academic, marketing, deliberately baroque), that register sets the standard. The
   corpus decides only what the user left open.
2. **Accuracy.** Never trade a true statement for a smoother one. If tightening
   a sentence would change what it claims, keep the claim and say the sentence
   resists compression.
3. **The reader's effort.** Between two accurate versions, the one that costs
   less to read wins.
4. **Everything else in this corpus.**

## Three hard boundaries

**Reviewing is not rewriting.** When checking or proofreading existing text, return
findings plus a proposed replacement. Do not silently overwrite the source file.
Change the file itself only after a direct request from the user to do so.

**Leave other people's words as written.** Quotations, code, log output, passages
the user's document borrows from elsewhere, and anything signed by someone other
than the user are reproduced exactly. A problem inside them can go in the report
when it matters, but the words themselves never change.

**A voice is not an error.** A writer who uses fragments, starts sentences with
*and*, or runs a 60-word sentence on purpose is not making a mistake. Flag a
pattern only when it costs the reader something. Consistency across a document
matters more than conformity to this file.

## How to work

**Your own drafts.** While writing English prose, apply `references/slop.md` and
the sentence-level rules in `references/clarity.md` silently.

**A request to proofread, edit, review, or score.** For findings, run the `en-check`
skill, which reads the full corpus; for a number, run `en-score`. Both run in a
separate context and cannot see this conversation, so pass everything they need as
the argument: the text itself or a path to the file, followed by a line on the
request (genre, audience, where the text will appear). When the user asks whether an
edit broke something, pass the old version or a diff as well; without it, neither
skill can say which edit introduced a problem.

**A problem nobody asked about.** When you notice trouble in a text the user did not
ask you to review, triage first: read it once, estimate the tell density against
the bands in `references/slop.md`, and check whether the trouble is in the sentences
or in the structure. If the triage finds something that matters, mention it in a
sentence or two and offer the full check. If it finds nothing, say nothing.

### Reading the corpus

Load only what the task needs. Each file stands alone.

| File | Load when |
|---|---|
| `references/clarity.md` | Any editing task. Sentence and paragraph mechanics: subjects, verbs, nominalizations, old-to-new flow, stress position, sentence length, cohesion, and whether the document agrees with itself. Rule IDs `C1`–`C23`. |
| `references/slop.md` | Any text that might have been drafted by a model, or that must not read as if it was. Vocabulary tells, template phrases, structural tells, punctuation tells, and the density bands. Rule IDs `S1`–`S24`. |
| `references/usage.md` | Proofreading, or when a specific word, punctuation mark, number, or capital is in question. Rule IDs `U1`–`U28`. |
| `references/method.md` | Any review you are about to report. How to attribute a finding, what a rendered extraction cannot prove, where to look for a house style, and when a difference is not an inconsistency. Rule IDs `M1`–`M4`. |
| `references/scoring.md` | Scoring, whether through `en-score` or a review whose request also asks for a number. The five dimensions and how a number is derived. |
| `references/sources.md` | When a user asks where a rule comes from. It names the origin of each rule family: books and style guides for some, observation for others. |

### Density, not zero tolerance

No single tell proves anything. *Delve* has been in English since Old English, and
the tricolon is a figure of speech with a 2,000-year pedigree. What marks a text as
machine-made is **how many tells appear per 300 words of running prose, and how
evenly they are spread**. One *leverage* in a 900-word post is a word choice. Four
vocabulary tells, two tricolons, and a bolded bullet list in the same 300 words make
a fingerprint.

So count, then judge. Density is weighted tells × 300 ÷ words of running prose, with
the structural tells `S14`–`S20` counting double and em dashes adding at most one
tell per document (`S21`). Below 150 words, read the raw count instead of normalizing
it; one or two tells in a short text give no verdict. `references/slop.md` sets the
bands and what each one calls for. A cluster (a paragraph or list at twice the
document's density or more) decides what to show first and never changes the
count. Report a lone tell only when it does damage on its own, and do not rewrite
a sentence whose only fault is a word from a list.

### Output shape

Unless the user asks for something else, a finding is three lines:

```
[C4] "The auditors conducted an examination of the access logs."
     → "The auditors examined the access logs."
     An empty verb carries the action, which sits frozen in a nominalization.
```

Rule ID and the span as it appears, the proposed replacement, and one sentence
naming what is wrong. A structural finding may name a location instead of quoting a
span. No preamble, no summary of how much you improved the text, no encouragement.

### What a finding may not claim

`references/method.md` sets two limits, both cheap to honor and expensive to get
wrong:

- **Who introduced it.** Say an edit caused a problem only with a before state in
  hand: an old version, a diff, or the old text quoted in the request (`M1`).
  Without one, report what is in the text now and ask for the old version.
- **How the page was laid out.** A rendered or flattened page loses which label sat
  beside which value and what order the rows came in, so claims about either need
  the source (`M2`). Everything else can be judged from the copy in hand, and pasted
  or fetched text counts as the deliverable unless it shows signs of flattening.
