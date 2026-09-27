# Contributing

Rules are the product here. A pull request that adds one is welcome; a pull request
that adds fifty word entries with no tests attached is not.

## What a rule needs

The bar depends on the family.

A **clarity, slop, or method rule** needs three things.

**1. A mechanical test.** Something a reader, or a model, can run on a sentence and
get the same answer twice. "Avoid weak writing" fails. "List the grammatical subject
of every sentence in the paragraph and read the list on its own" passes. A few
existing tests call for judgment (`C11` and `C18` among them); a new one should come
as close to a count as the rule allows.

**2. A named source.** For most clarity rules, that is a book or a style guide. A slop
rule may rest on documented observation of model output: the pattern, and where it
turns up. A method rule, or a rule like `C23`, may rest on a documented review
failure: what a real review got wrong, and how the rule would have stopped it. Add
the source to `skills/en-text/references/sources.md` if it is not there yet. A rule
made up on the spot is taste, and taste belongs in a house style guide.

**3. A stated exception.** Every rule here is wrong somewhere. If you cannot name a
case where the rule should be ignored, you have not finished thinking about it. Rules
with no limits are how a checker ends up flattening everyone's voice.

A **usage rule** needs a named authority or style guide and an example. A test and an
exception are welcome but not required: many usage rules settle a convention, and
their job is to say which choice to hold.

## Format

Add the rule to the right file with the next free ID. Do not renumber existing
rules: findings in the wild cite them.

```markdown
### C24 — Short imperative name

**Test:** the mechanical check.

**Fix:** what to do instead.

- `before`
- → `after`

**Exception:** when this rule does not apply.
```

Keep examples short and plausible: a sentence someone would write. An example built
only to show off the rule teaches the wrong thing.

A new rule also changes numbers that other files state, and `check_corpus.py` fails
until they agree: the range in the file's header and in its part heading, the range
in `skills/en-text/SKILL.md` and in the README table, the rule totals in the README,
and any other range the new rule extends, such as the Precision rules in
`scoring.md`. Add a line for the rule to `CHANGELOG.md` as well.

## What does not get merged

- **A longer banned-word list without a density rule.** The corpus is built to count
  before it judges. Wordlists that trigger on a single match are the failure mode
  this corpus exists to avoid.
- **Rules that encode one house style as universal.** Serial comma, Oxford spelling,
  and heading case are choices. `usage.md` treats them as choices on purpose: the
  only finding there is a mix.
- **Anything copied from a copyrighted source.** Restate the idea in your own words.
  If a passage is worth quoting verbatim, it is worth checking the license first.
- **Prescriptions that most careful editors abandoned.** No ban on split
  infinitives, no rule against ending a sentence with a preposition, no blanket ban
  on the passive. `C6` explains what we do instead.

## Language scope

This corpus is English. Other languages deserve their own corpus with their own
tradition behind it rather than a translation of this one. If you are building one,
say so in an issue.

## Testing a change

Two layers.

**Structure is checked by machine.** Run `python tests/check_corpus.py` from the repo
root before opening a PR. It runs 13 checks, listed in the docstring at the top of
the script. Among other things, it fails on a rule ID that is duplicated or out of
sequence; a cited ID that does not exist; a rule range or rule total that no longer
matches the files, wherever it appears outside the changelog; a clarity, slop, or
method rule missing its test, fix, or exception; a weight profile that does not sum
to 1.0; a worked score that does not follow from its sub-scores; plugin manifests
whose versions disagree with each other or with the top changelog entry; a review
skill allowed to write files or run commands; and repo prose that fails its own
vocabulary, em dash, or reader-address check. CI runs the same script on every push
and pull request.

**Judgment is checked by hand.** Run your new rule against the fixtures in
`tests/fixtures/` and against two texts of your own, one that should trigger it and
one that should not. Paste both results in the PR description. `tests/EVAL.md` lists
what each fixture is expected to produce; when an agent runs them, copy each fixture
under a neutral name first, as it explains.
