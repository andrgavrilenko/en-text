# Changelog

All notable changes to this project are documented here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and
this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.2] - 2026-09-24

Everything here came from the first use of this corpus on a production site: a
five-language marketing site with about 1,000 words of English copy. The corpus
found nine real defects, including a billing contradiction that promised two
incompatible cancellation models in one sentence. It also made three confident
mistakes, and those are what this release is about.

### Added

- **`method.md`, rules M1-M4.** The first rules in this corpus about the review
  rather than the prose. A finding can be correct about a sentence and still be
  false, misattributed, or unprovable from what the reviewer was handed.
- **`M1`, attribution needs evidence.** Asked "did my edits break anything", the
  corpus twice answered that an edit had introduced a problem that predated it, once
  as the headline of the report. It cannot see history; now it says so instead of
  guessing, unless the request carries a before state.
- **`M2`, cross-reference findings need source-level text.** The first review ran on
  a markdown reconstruction of a rendered HTML table and reported that four product
  descriptions had shifted by one row. They had not; the conversion had dropped the
  row structure. Pairing, ordering, and agreement claims now require the source, and
  content a rendering never received is no longer reported as missing.
- **`M3`, find the house style before applying the default.** The review located the
  project's own copy-review agent unprompted and applied its em dash ban, which
  produced better findings than any default would have. Now it is a rule rather than
  luck.
- **`M4`, derive the document's own system before calling it inconsistent.** A file
  mixing "four tools" with "7 days" looks inconsistent from two tokens and is
  coherent from all of them: counts spelled out, durations in numerals. Collect every
  instance first.
- **`tests/fixtures/05-flattened-rendering.md` and its eval entry.** A flattened
  pricing page carrying the exact trap that produced the false headline, invoked with
  an attribution claim so `M1` and `M2` are both exercised. It is the only fixture
  where part of the correct answer is a refusal.

### Changed

- `en-check` now settles five things in its frame line instead of four, including
  whether it holds source or a rendering, and states up front when it has no before
  state for an attribution claim.
- Three new grounds for dropping a finding in the verify step: unprovable
  attribution, structure claims from a rendering, and differences the document's own
  system explains.
- `en-score` states which artifact it scored and does not penalize writing for
  content that never reached its copy.
- `check_corpus.py` covers the `M` prefix: sequence, citations, and the test, fix and
  exception requirement now apply to method rules too.

## [0.1.1] - 2026-09-21

### Fixed

- **Worked scores did not follow from their sub-scores.** The example in `scoring.md`
  and `en-score` claimed 6.4 where the weights give 6.1; the before/after example
  claimed 2.1 where nothing gave 2.1. Both now show the arithmetic.
- **Two genre weight profiles summed to 1.05.** Marketing and academic-legal now
  sum to 1.0, and all four profiles are a single table so the sums can be checked.
- **C1's example changed the claim.** "A decision was reached" had become
  "approved", which violates the corpus's own accuracy rule. The example now
  preserves the claim.
- **The example's `[S1]` finding listed intensifiers and a word from no list.** Split
  into S1, S3, S5, and S13 findings that each cite the right rule.
- **`en-score`'s own text and `sources.md` failed S21** (em dash density). Reworded.
- **S21 normalized a single em dash in a short text into a finding.** One mark is now
  never a finding, whatever the word count.

### Added

- **Every C and S rule now has an explicit Test, Fix, and Exception.** Fourteen
  clarity rules and sixteen slop rules were missing one or more. The README and
  CONTRIBUTING claimed the property; now it is true and machine-checked.
- **`tests/check_corpus.py`.** Ten structural checks, standard library only:
  manifests, frontmatter, ID sequence, rule parts, citations, weight sums, worked
  score arithmetic, self-slop, links, fixtures. Runs in CI on every push.
- **`tests/fixtures/` and `tests/EVAL.md`.** Four texts with expected findings,
  expected non-findings, and score bands: dense slop, Official Style with no slop,
  a human voice that must survive, and drifting conventions.
- **"Model-favored" replaces "banned"** throughout. A banned-word list is the design
  the density table exists to avoid.

## [0.1.0] - 2026-09-21

### Added

- **Three skills.** `en-text` applies light cleanup as the agent drafts; `en-check`
  runs the full corpus and returns findings; `en-score` returns a number across five
  weighted dimensions. Both commands run in a forked context and cannot write files.
- **`clarity.md`, rules C1-C22.** Sentence and paragraph mechanics: characters into
  subjects, actions into verbs, nominalizations, empty verbs, the paramedic method,
  the conditions under which a passive earns its place, old-before-new, stress
  position, topic strings, sentence length distribution, parallelism, word choice.
- **`slop.md`, rules S1-S24.** The machine dialect, organized as vocabulary, phrase
  templates, structure, and typography. Structural tells count double because a
  reader forgives an odd word long before a shape that repeats.
- **A density table instead of a banned-word list.** Tells are counted per 300 words
  and weighted for clustering before anything is reported. One flagged word never
  triggers a rewrite, which is the failure mode of every wordlist-based checker.
- **`usage.md`, rules U1-U28.** Punctuation, confusables, numbers, dates, capitals,
  inclusive wording, US versus UK, list and link mechanics. Consistency outranks
  correctness for anything genuinely optional.
- **`scoring.md`.** Five dimensions with anchor tables and genre-dependent weights,
  built so the same text scores within about 0.3 of itself on a re-run.
- **Named failure modes for rewrites.** Flattening, truncating a real qualifier, and
  substituting one recognizable dialect for another are called out as errors, so an
  edit cannot succeed by making prose bland.
