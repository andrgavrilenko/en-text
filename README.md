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
     Empty verb carrying a nominalization.

[S16] Six bullets, each opening with a bolded label, each one line long.
      → Two of these are argument; make them paragraphs. The rest is a table.
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

Works in Claude Code (CLI and desktop app). The skills are plain markdown with no
runtime, so they also work by copying the whole `skills/` folder into any agent
that reads `SKILL.md` files. Keep the three skill folders together: `en-check` and
`en-score` read the corpus from `../en-text/references/`.

## Use

| You type | What happens |
|---|---|
| `/en-text:en-check` | Full review. Findings with rule IDs and proposed replacements. Never edits your file. |
| `/en-text:en-score` | A number, 0.0–10.0, across five dimensions, with the three findings that cost the most. |
| "proofread this", "does this read like AI", "tighten this up" | Same thing, without the slash. |
| Nothing | The base skill applies light cleanup to English the agent drafts itself. |

Both commands take an argument: a file, a glob, or pasted text. With no argument
they take the last English text in the conversation.

## What is in the corpus

74 rules. The 46 clarity and slop rules each carry a test you can run on a
sentence, a fix, and a stated exception. The 28 usage rules are conventions, and
say which choice to hold rather than which is right.

| File | Rules | Covers |
|---|---|---|
| `clarity.md` | `C1`–`C22` | Characters as subjects, actions as verbs, nominalizations, the paramedic method, when the passive earns its place, old-before-new, stress position, topic strings, sentence length, parallelism |
| `slop.md` | `S1`–`S24` | Model-favored vocabulary, template phrases, the rule of three, bolded bullet headers, uniform paragraph length, rhetorical-question openers, em dash density, title formulas |
| `usage.md` | `U1`–`U28` | Punctuation, confusables, numbers, dates, capitals, inclusive wording, US vs UK, list and link mechanics |
| `scoring.md` | — | Five weighted dimensions with anchor tables |
| `sources.md` | — | Where every rule comes from |

## What makes it different

Four things, in order of how much they matter.

**Density, not zero tolerance.** *Delve* appears in books from 1890. A tricolon is a
figure of speech with a 2000-year pedigree. What marks a text as machine-made is how
many tells appear per hundred words and how evenly they are spaced. The corpus
counts first and judges second, so a single flagged word never triggers a rewrite.

**Findings carry rule IDs.** `[C9] the stress position holds an administrative
detail` is a claim you can check and reject. "This feels weak" is not.

**Clarity, not only anti-slop.** Stripping AI vocabulary from a badly built document
gets you a badly built document with better vocabulary. Most of the corpus is
sentence and paragraph mechanics that predate the whole problem.

**It refuses to flatten you.** The corpus names its own failure modes: flattening
every figure of speech, cutting real qualifiers because they looked like hedging,
and swapping one dialect for another dialect of short punchy fragments. A voice is
not an error.

## Not a linter

`en-text` has no binary, no config, no CI step. It is a corpus that a model reads
and applies with judgment, which is the right tool for "is this passive earning its
place" and the wrong tool for "is this line over 80 characters".

For deterministic checks in CI, use [Vale](https://vale.sh) or
[proselint](https://github.com/amperser/proselint) alongside it. They catch
different things and they never disagree about a rule they both encode.

## Credits

No rule here is original. The clarity rules restate Joseph Williams, Richard Lanham,
George Gopen, Steven Pinker, and William Zinsser; the usage rules follow Garner,
Strunk, and Fowler; the conventions come from plainlanguage.gov (public domain), the
18F Content Guide (public domain), the Google developer documentation style guide
(CC BY 4.0), and the GOV.UK style guide (OGL v3.0). Full attribution in
[`sources.md`](skills/en-text/references/sources.md) and [`NOTICE`](NOTICE).

The idea of packaging a language's editorial tradition as an agent skill comes from
[`talkstream/ru-text`](https://github.com/talkstream/ru-text), which does this for
Russian. `en-text` shares no code or text with it.

## Tests

The corpus is prose, but its structure is checked by machine. `tests/check_corpus.py`
(standard library only) verifies that rule IDs are sequential and unique, that
every ID cited anywhere in the repo exists, that every clarity and slop rule has a
test, a fix, and an exception, that the scoring weights sum to 1.0, that every
worked score follows from its sub-scores, and that the repo's own prose passes its
own slop density threshold. It runs on every push.

```bash
python tests/check_corpus.py
```

`tests/fixtures/` holds texts with known findings for checking the skills by hand.
See [tests/EVAL.md](tests/EVAL.md).

## Contributing

A rule gets in if it passes three tests: you can state a mechanical check for it,
you can name where it comes from, and you can name a case where it should be
ignored. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Licence

MIT. See [LICENSE](LICENSE).
