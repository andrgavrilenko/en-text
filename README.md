# en-text

English text quality for AI agents. Three skills: edit, check, score.

Two problems stack. Bad prose existed long before language models: buried subjects,
nominalizations, hedges, sentences that make you hold six things in memory before
the verb arrives. Then models added a dialect of their own: *delve*, *leverage*,
*it's not X, it's Y*, three items in every list, a bolded bullet for every thought.

A text can be free of AI tells and still be unreadable. A text can be perfectly
clear and still announce on line one that a machine wrote it. `en-text` treats both,
and every finding cites the rule behind it, so you can argue with the rule instead
of with someone's taste.

```
[C4] "we performed an evaluation of the retry logic"
     → "we evaluated the retry logic"
     An empty verb carries an action frozen in a nominalization.

[S16] The six bullets under "What changed"
      → Make the two that argue a point into a paragraph and the other four into a table.
      Each bullet opens with a bolded label and runs one line, so the list reads as a template.
```

## Install

Inside a Claude Code session:

```
/plugin marketplace add andrgavrilenko/en-text
/plugin install en-text@en-text
```

Or from a terminal:

```bash
claude plugin marketplace add andrgavrilenko/en-text
claude plugin install en-text@en-text
```

Works in Claude Code (CLI and desktop app).

Only the base skill, `skills/en-text`, carries over to other agents as it is: it is
plain markdown with no runtime, and any agent that reads `SKILL.md` files can follow
it and its `references/` folder. `en-check` and `en-score` rely on three Claude Code
features: a forked context, a `disallowed-tools` list that takes away six built-in
tools able to write files or run commands (Write, Edit, NotebookEdit, Bash,
PowerShell, Monitor), and a slash command that hands them the text as an argument.
Another agent can read and follow their instructions, but there "never edits a file"
is an instruction the agent is asked to obey, and nothing enforces it. Keep the three
skill folders together: the two commands read the corpus from
`skills/en-text/references/` under the plugin root, or from `../en-text/references/`
beside their own folders.

## Use

| You type | What happens |
|---|---|
| `/en-text:en-check` and the text, a file, or a glob | A full review: findings with rule IDs and proposed replacements. It never edits your file. |
| `/en-text:en-score` and the text, a file, or a glob | A score from 0.0 to 10.0 across five weighted dimensions, with the count behind each. It names up to three findings, each costing at least half a point of its dimension, or says that none does. |
| A request in words, such as "proofread this" or "how good is this writing" | The model picks the skill whose description fits the request: `en-check`, `en-score`, or the base skill. To decide which one runs, use the slash command. |
| Nothing | The base skill loads when the model judges that its description fits the task. While it is loaded, the agent applies light cleanup to the English it drafts. Nothing makes it load on every turn. |

Both commands take a file, a glob, or pasted text, with an optional note about the
request: the genre, the audience, where the text will appear, and, to ask whether an
edit broke something, the old version or a diff. Each command runs in a separate
context and cannot see the conversation, so with no argument it asks for the text
and stops.

```
/en-text:en-check docs/pricing.md Landing page for small-team buyers.
/en-text:en-score drafts/launch-post.md
```

[examples/before-after.md](examples/before-after.md) shows both reports on one text,
with the arithmetic behind the score.

## What is in the corpus

79 rules in four files. The 51 clarity, slop, and method rules each carry a test, a
fix, and an exception that says where the rule stops applying.

The 28 usage rules answer two kinds of question. Some have a right answer: a comma
alone does not join two sentences, a plural takes no apostrophe, countable things
take `fewer`, and `affect` is not `effect`. Others are conventions on which style
guides disagree, such as the serial comma, dash spacing, US or UK spelling, and
heading case. For those, the only finding is a mix, and the rule says to hold
whatever the document already does.

| File | Rules | Covers |
|---|---|---|
| `clarity.md` | `C1`–`C23` | Characters as subjects, actions as verbs, nominalizations, the paramedic method, when the passive earns its place, old before new, stress position, topic strings, sentence length, parallelism, and whether the document agrees with itself |
| `slop.md` | `S1`–`S24` | Model-favored vocabulary, template phrases and chat residue, the rule of three, bolded bullet headers, uniform paragraph length, self-answered questions, em dash density, title formulas, and the density bands that turn a count into a verdict |
| `usage.md` | `U1`–`U28` | Punctuation, confusables, numbers, dates, capitals, inclusive wording, US vs UK, list and link mechanics |
| `method.md` | `M1`–`M4` | How to run the review: attributing a finding to an edit, what a flattened copy cannot show about layout, finding the house style, and when a difference is not an inconsistency |
| `scoring.md` | — | Five weighted dimensions, each scored from a count through an anchor table |
| `sources.md` | — | Where each family of rules comes from |

## What makes it different

Five things, in order of how much they matter.

**It counts before it judges.** No single tell proves anything: *delve* has been in
English since Old English, and the tricolon is a figure with a 2,000-year pedigree.
The corpus counts weighted tells per 300 words of running prose, with structural
tells counted double, and reads the density against four bands. Below 150 words it
reads the raw count instead, because a rate would turn two tells in a short post
into a pattern. A single tell never moves a text out of the Human band, and a
paragraph where tells cluster changes only which findings the report shows first.

**Findings carry rule IDs.** `[C9] the stress position holds an administrative
detail` is a claim you can check and reject. "This feels weak" is not.

**It covers clarity as well as slop.** Stripping AI vocabulary from a badly built
document gets you a badly built document with better vocabulary. Most of the corpus
is sentence and paragraph mechanics that predate the whole problem.

**It will not flatten a voice or invent a fact.** `slop.md` names five ways a
rewrite fails: stripping every figure of speech, cutting a real qualifier because it
looked like hedging, trading the machine dialect for a new one made of short punchy
fragments, swapping *delve* for *dig into* while keeping the move, and filling a gap
with a number, a name, or a cause the writer never supplied. Where a figure is
missing, a review marks the gap and asks. A voice is not an error.

**It knows what it cannot see.** `method.md` guards against three confident mistakes
that the corpus made in its first review of a production site: blaming an edit for
a problem that was always there, reading a table's layout from a flattened copy of
it, and calling a difference an inconsistency before collecting every instance.
Without the old version or a diff, a review now says it cannot tell which edit
introduced a problem, and asks for one.

## Not a linter

`en-text` has no binary and no config, and adds nothing to your own CI. It is a
corpus that a model reads and applies with judgment, which is the right tool for "is
this passive earning its place" and the wrong tool for "is this line over 80
characters". The repo does run structural checks on its own corpus in CI (see
Tests); they check the rules, not your prose.

For deterministic checks, use [Vale](https://vale.sh) or
[proselint](https://github.com/amperser/proselint) alongside it. They catch
different things.

## Credits

Most clarity and usage rules restate advice from books on style, usage guides, and
style manuals: Joseph M. Williams's *Style: Lessons in Clarity and Grace* above all,
and Richard Lanham, George Gopen and Judith Swan, Steven Pinker, William Zinsser,
William Strunk Jr., H. W. and F. G. Fowler, George Orwell, Bryan Garner,
Merriam-Webster, and the Chicago, AP, and APA style guides. Four openly licensed
guides contributed conventions: the Federal Plain Language Guidelines and the 18F
Content Guide (both public domain in the United States, with a worldwide CC0
waiver), the Google developer documentation style guide (CC BY 4.0), and the GOV.UK
style guide (Open Government Licence v3.0).

The slop rules, `S1`–`S24`, are the project's own catalog, written from reading model
output. A 2025 study of excess vocabulary in biomedical abstracts supports the
premise that models use some words far more often than people do, and Wikipedia's
"Signs of AI writing" page lists many of the same patterns. The method rules,
`M1`–`M4`, and `C23` came out of the project's own reviews.

[`sources.md`](skills/en-text/references/sources.md) says where each family comes
from and which rules each source backs, and [`NOTICE`](NOTICE) gives the attributions
the licenses require.

## Tests

The corpus is prose, but its structure is checked by machine.
`tests/check_corpus.py` uses only the Python standard library and runs 13 checks:

1. The plugin manifests parse, and their versions match each other and the top
   entry in `CHANGELOG.md`.
2. Every skill has valid frontmatter, and `en-check` and `en-score` run in a forked
   context with the file-writing and shell tools disallowed.
3. Rule IDs in each reference file run in sequence with no duplicates, and the ID
   ranges stated in each file's header, the base skill, and README, along with
   README's rule total, match the files.
4. Every clarity, slop, and method rule has a test, a fix, and an exception.
5. Every rule ID cited in any markdown file exists.
6. Every scoring weight profile sums to 1.0.
7. Every worked score in any markdown file follows from its five sub-scores and the
   weight profile it names, no worked example quietly disappears, and arithmetic
   written out in prose adds up.
8. The repo's own prose passes a narrow slop check, described below.
9. Local links in README resolve.
10. Every fixture named in `tests/EVAL.md` exists, and every fixture is described
    there.
11. Every rule range mentioned in the repo, outside the changelog, has real IDs at
    both ends, each part heading matches the rules under it, and the rule totals in
    README and the three skills match the files.
12. Nothing under `skills/` contains Cyrillic text.
13. No file outside the changelog repeats either promise that version 0.2.0
    withdrew: a figure for how closely re-run scores agree, and a no-argument mode
    that reviewed the last text in the conversation.

The slop check in item 8 reads README, CONTRIBUTING, CHANGELOG, the three `SKILL.md`
files, and `sources.md`. It counts the `S1` and `S2` vocabulary, including the
inflected forms of `S1` verbs and the plurals of `S2` nouns, and fails a file at 2
or more per 300 words. It also applies the `S21` em dash threshold and looks for the
`S11` both-audiences construction. It skips code, inline code, headings, quoted
lines, table rows, and italic mentions. The other slop rules, and every clarity and
usage rule, are outside what the script checks.

```bash
python tests/check_corpus.py
```

CI runs the script on every push and pull request, with a read-only token.

`tests/fixtures/` holds five texts for checking the skills by hand. Each targets one
failure mode and comes with the findings a run must and must not report, and a
score band. [tests/EVAL.md](tests/EVAL.md) describes them and records every run so
far, including the pre-publication test of 2026-09-26. Its score bands are
provisional, and it says how they were set.

## Contributing

A clarity, slop, or method rule gets in with a mechanical test, a named source, and
a stated exception. A usage rule needs a named authority or style guide and an
example. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT. See [LICENSE](LICENSE).
