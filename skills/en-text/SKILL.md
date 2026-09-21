---
name: en-text
description: >
  English text quality. Triggers: edit this, proofread, tighten this up, make this
  sound human, does this read like AI, en-text. Catches AI slop, buried subjects,
  nominalizations, and hedging. Applies on request; light cleanup on any English
  draft the agent writes.
---

# en-text — English Text Quality

An independent corpus of English writing rules, written for AI agents rather than
for people. Every rule has an ID, a test you can run on a sentence, and a fix.
Findings cite the ID so a reader can argue with the rule instead of with taste.

Credits and recommended reading: `references/sources.md`

## What this skill is for

Two problems stack on top of each other. Bad prose existed long before language
models: buried subjects, nominalizations, hedging, sentences that make the reader
hold six things in memory before the verb arrives. Then models added a dialect of
their own: *delve*, *leverage*, *it's not X, it's Y*, three items in every list,
a bolded bullet for every thought. A text can be free of AI tells and still be
unreadable. A text can be perfectly clear and still announce on line one that a
machine wrote it. This corpus treats both.

## Priority order

When rules conflict, resolve in this order:

1. **The user's explicit instruction.** A requested register (legal, academic,
   marketing, deliberately baroque) overrides any default here. These are
   defaults, not mandates.
2. **Accuracy.** Never trade a true statement for a smoother one. If tightening
   a sentence would change what it claims, keep the claim and say the sentence
   resists compression.
3. **The reader's effort.** Between two accurate versions, the one that costs
   less to read wins.
4. **Everything else in this corpus.**

## Three hard boundaries

**Reviewing is not rewriting.** When checking or proofreading existing text, return
findings plus a proposed replacement. Do not silently overwrite the source file.
Rewrite in place only when the user asks for it in so many words.

**Other people's words stay theirs.** Quoted material, code blocks, log output,
third-party text inside the user's document, and anything under a name that is not
the user's are reproduced as-is. Report a problem you see in them if it matters;
never edit them.

**A voice is not an error.** A writer who uses fragments, starts sentences with
*and*, or runs a 60-word sentence on purpose is not making a mistake. Flag a
pattern only when it costs the reader something. Consistency across a document
matters more than conformity to this file.

## How to work

For a light pass (the agent drafting its own English prose), apply
`references/slop.md` and the sentence-level rules in `references/clarity.md`
silently, as you write.

For an explicit request — proofread, edit, review — run the procedure in the
`en-check` skill, which reads the full corpus.

For a number rather than a list, run `en-score`.

### Reading the corpus

Load only what the task needs. Each file stands alone.

| File | Load when |
|---|---|
| `references/clarity.md` | Any editing task. Sentence and paragraph mechanics: subjects, verbs, nominalizations, old-to-new flow, stress position, sentence length, cohesion. Rule IDs `C1`–`C22`. |
| `references/slop.md` | Any text that might have been drafted by a model, or that must not read as if it was. Banned words, template phrases, structural tells, punctuation tells. Rule IDs `S1`–`S24`. |
| `references/usage.md` | Proofreading, or when a specific word, punctuation mark, number, or capital is in question. Rule IDs `U1`–`U28`. |
| `references/scoring.md` | Only for `en-score`. The five dimensions and how a number is derived. |
| `references/sources.md` | When a user asks where a rule comes from. |

### Density, not zero tolerance

No single tell proves anything. *Delve* appears in books published in 1890. A
tricolon is a figure of speech with a 2000-year pedigree. What marks text as
machine-made is **how many tells appear per hundred words, and how evenly they are
spaced**. One *leverage* in a 900-word post is a word choice. Four banned words,
two tricolons, and a bolded bullet list in 300 words is a fingerprint.

So: count, then judge. Report a tell as a finding when it is one of a cluster, or
when the single instance is doing real damage on its own. Do not rewrite a sentence
whose only sin is containing a word from a list.

### Output shape

Unless the user asks for something else, a finding is three lines:

```
[C4] "The implementation of the feature was completed by the team."
     → "The team shipped the feature."
     The subject is buried in a nominalization; the real verb is hiding in "implementation".
```

Rule ID, the span as it appears, the proposed replacement, and one sentence naming
what is wrong. No preamble, no summary of how much you improved the text, no
encouragement.
