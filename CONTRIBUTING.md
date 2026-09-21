# Contributing

Rules are the product here. A pull request that adds one is welcome; a pull request
that adds fifty word entries with no tests attached is not.

## The three tests a rule must pass

**1. It has a mechanical check.** Something a reader (or a model) can run on a
sentence and get the same answer twice. "Avoid weak writing" fails. "List the
grammatical subject of every sentence in the paragraph and read the list on its own"
passes.

**2. It has a source.** Name the book, guide, or tradition behind it, and add it to
`skills/en-text/references/sources.md` if it is not already there. A rule invented on
the spot is taste, and taste belongs in your own style guide, not in a shared corpus.

**3. It has a stated exception.** Every rule here is wrong somewhere. If you cannot
name a case where the rule should be ignored, you have not finished thinking about
it. Rules with no limits are how a checker ends up flattening everyone's voice.

## Format

Add the rule to the right file with the next free ID. Do not renumber existing
rules: findings in the wild cite them.

```markdown
### C23 — Short imperative name

**Test:** the mechanical check.

**Fix:** what to do instead.

- `before`
- → `after`

**Exception:** when this rule does not apply.
```

Keep examples short and real. Invented sentences that exist only to demonstrate the
rule are easy to spot and teach the wrong thing.

## What does not get merged

- **A longer banned-word list without a density rule.** The corpus is built to count
  before it judges. Wordlists that trigger on a single match are the failure mode
  we are avoiding, not the feature we are missing.
- **Rules that encode one house style as universal.** Serial comma, Oxford spelling,
  and heading case are choices. `usage.md` says "pick one and hold it" on purpose.
- **Anything copied from a copyrighted source.** Restate the idea in your own words.
  If a passage is worth quoting verbatim, it is worth checking the licence first.
- **Prescriptions that most careful editors abandoned.** No splitting-infinitive ban,
  no rule against ending a sentence with a preposition, no blanket ban on the
  passive. `C6` explains what we do instead.

## Language scope

This corpus is English. Other languages deserve their own corpus with their own
tradition behind it rather than a translation of this one. If you are building one,
say so in an issue and we will link it from the README.

## Testing a change

There is no test suite: the corpus is prose. Before opening a PR, run your new rule
against the example in `examples/before-after.md` and against two texts of your own,
one that should trigger it and one that should not. Paste both results in the PR
description.
