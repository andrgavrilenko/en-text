# Changelog

All notable changes to this project are documented here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and
this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.3.0] - 2026-10-01

The first runs of 0.2.0 through Claude Code's own skill mechanism, recorded in
`tests/EVAL.md` under 2026-09-28, found one counting defect in `en-score` and a
pattern of misses in `en-check`: the corpus overlooked defects rather than inventing
them. This release fixes the count, makes `en-check` search for what it tended to
miss, and closes two routing gaps.

Every fix was accepted by live runs, recorded in `tests/EVAL.md` under 2026-10-01
to 2026-10-05: fixture 01 now scores 4.5 to 4.7 with Human voice at 0.0, fixture 02
holds its Sentence clarity counts within 3 of each other, `en-check` names every
must-report rule on fixtures 02 and 04 in three runs of three, the clean fixture 03
drew no finding in six runs, and routing went 32/32 with two classifiers. Total
scores stay uncapped: a text that fails one dimension badly still scores the
weighted sum of the five numbers it shows.

One thing did not close. On fixture 05, `en-check` names the quiet mismatch between
"Get the Team plan for 30 days" and a "Start free trial" button in one run of three,
and a comma splice on the same page likewise. The blunt version of the button case is
caught every time.

### Fixed

- **Human voice counted rules, not occurrences.** On the slop-heavy fixture
  `en-score` counted `S1` once for four listed words and lost `S15`, scoring Human
  voice 3.1 against a band of 0 to 2. Every other dimension in `scoring.md` restates
  what one instance is; Human voice only pointed to `slop.md`. It now says it
  outright: each listed word counts every time it occurs, and a pattern that exists
  only across the document (`S15`, `S17`, `S20`, `S22`, `S23`) counts once.
- **One heavy sentence could count as three clarity instances.** A nominalized
  subject with its actor in a by-phrase is one `C1` instance, not also a `C3` and a
  `C4`, because one rewrite fixes all of it. Every other frozen action in the
  sentence still counts on its own. A noun is counted once whichever of `C2` and `C3`
  names it.
- **`en-check` filed one finding inside another.** Runs described nominalizations
  inside a `C1` explanation without ever reporting `C3`. A problem named while
  explaining a finding is now reported under its own ID, and when `C1` or `C4` fires,
  the whole text is tested for `C3`, `C6` and `C7`, and a wind-up opening on a
  nominalized subject is reported as `C7` beside the `C1` finding, not inside it. A
  closing sweep collects each usage convention across the document, since a mix
  shows only when all its instances sit side by side; for the serial comma it lists
  every series of three or more, including one inside a sentence that already
  carries another finding. It then reads every comma that joins two clauses (`U2`).
  The sweep skips anything read from a flattened table, which stays under `M2`.
- **`C23` missed buttons.** The pairing of a button or link label with the sentence
  beside it lived in one clause of the test and was skipped once the count half had
  found something. It is now a step of its own in `clarity.md`, which also reads any
  control that sets the click's terms, such as a billing toggle, and `en-check` runs
  it on every pricing or offer page even after the count step has found a defect.
- **The corpus path.** The commands now read the corpus from
  `${CLAUDE_PLUGIN_ROOT}/skills/en-text/references/` first, and fall back to
  `${CLAUDE_SKILL_DIR}/../en-text/references/` passed to the tools as written, then
  to the search by folder name. One run in eighteen reported the relative path missing
  and reached the corpus only through that search.
- **Routing.** All three descriptions say that the language of the text decides, not
  the language of the request. The `en-score` trigger is now "score how much this
  reads like AI", so that it no longer collides with the `en-text` and `en-check`
  trigger "does this read like AI".
- `check_corpus.py`: an operator-precedence slip in the tell-list parser could pass
  an empty string on.

### Changed

- `tests/EVAL.md` says what counts as a heading for its word counts: a line opening
  with `#`, or a title alone on the first line with no closing punctuation. Fixture
  02 is 156 words by that convention, not 160.
- `tests/EVAL.md` records the nine runs of 2026-09-28 that this release answers.

## [0.2.0] - 2026-09-27

This release answers the pre-publication test of 2026-09-26, recorded in
`tests/EVAL.md`. The test ran the skills on the five fixtures and on 19
new cases, scored each fixture six times, and gave the corpus to 11 reviewers, whose
186 findings went to independent skeptics; 136 were upheld. It found six problems
that blocked submission to the plugin directory, listed in `tests/EVAL.md` as B1 to
B6. This release fixes all six and many of the smaller findings. A blind rerun on
2026-09-27, also recorded in `tests/EVAL.md`, checked the fixes on the cases that
had failed: 12 of the 14 case and skill pairs now pass, and the other two pass in
part.

Two promises made by earlier versions are withdrawn, because they did not hold.
`scoring.md` promised that a text scored twice lands within about 0.3 of itself;
six runs on one fixture spread by 1.4. And `en-check` and `en-score` promised to
work, given no argument, on "the most recent English text in the conversation",
which a forked skill cannot see.

### Fixed

- **The commands had nothing to read without an argument (B1).** Both run with
  `context: fork`, and a forked skill does not see the conversation. Given no
  argument, each now asks for the text or a path to a file, and stops. Both
  descriptions say that the text, or a path, is passed as the argument, followed by
  an optional note on the request: the genre, the audience, where the text will
  appear, and the old version when the question is whether an edit broke something.
  `$ARGUMENTS` appears once in each body, because every occurrence is replaced by
  the whole argument. `Monitor` joins the disallowed tools, since it runs shell
  commands. The corpus is read from `${CLAUDE_SKILL_DIR}/../en-text/references/`,
  and the fallback search by folder name never mixes files from two installed
  versions.
- **A provenance claim was untrue (B2).** The skill descriptions and several
  scaffolding sentences of `en-check` and `en-score` followed another project's
  skill files closely, which made the README's claim that `en-text` shares no text
  with that project untrue. Both files are rewritten in this project's own words,
  and the README paragraph and the `sources.md` entry that made the claim are gone.
- **`en-score` invented findings on clean text (B3).** It had to name three
  findings, and on clean text it made them up, some of them cleared by the rules'
  own exceptions. It now names up to three, each a rule whose fix would raise its
  dimension's sub-score by at least half a point, and prints
  `No finding costs half a point.` when none qualifies. When no single rule in a
  dimension reaches half a point but all its instances together do, they are named
  as one finding. A score no longer counts what `en-check` would drop: a pattern
  that is part of the writer's voice and costs the reader nothing, or a span whose
  only fix would change what it claims. A number always comes with its reasons, and
  the old "Cheapest N points" line becomes an optional gain line.
- **Slop density had no floor and a multiplier nobody could apply (B4).**
  Normalizing to 300 words turned two em dashes in a 167-word post into a
  Suspicious verdict, "clustering multiplies" gave no factor, and the top band told
  a read-only skill to rewrite the text. The bands are now continuous (under 2, 2 to
  under 5, 5 to under 10, 10 or more). Below 150 words of running prose the raw
  weighted count is read against them, and one or two tells in a short text give no
  verdict. A cluster changes only which tells the report shows first, and the top
  band proposes a rewrite inside the report. `S21` adds one tell per document once
  its own threshold is met, counts a spaced en dash doing an em dash's job, and
  gives its note on public posts apart from the verdict.
- **Repeatability was promised, not measured (B5).** Six `en-score` runs per
  fixture spread by 0.3 to 1.4 points. `scoring.md` now states that spread and asks
  for a single score to be read as ±0.5. The counted tables did not close the gap on
  a dense middling text: three runs of the Official Style fixture on this version
  still spread by 1.1. Every counted dimension converts a rate
  per 300 words through a table with no gaps between rows and a formula for placing
  a value inside a row, and Correctness is normalized to length like the others.
  `S2`, `S6`, and `S13` count once, in Human voice, where they used to count in
  Precision too; two rules that flag the same words count once, and different
  spans, even one inside the other, count separately. Precision is the share of empty claims, less fixed amounts for a
  fact stated with two values (`C23`), a thing called by two names (`C22`), and a
  needless long word or intensifier.
- **Examples broke the corpus's own accuracy rule (B6).** The `C3` example turned a
  cause into a sequence and invented an actor. The `C20` example invented figures;
  it now says that figures come from the author or a source. The base skill's `[C4]`
  example had no empty verb and changed "completed" to "shipped". `U10` forbade the
  four-dot ellipsis that Chicago and AP use after a complete sentence, `U12` treated
  `that` for people as an error although Merriam-Webster and Garner accept it, `S4`
  listed "more often than not", an honest qualifier of the kind `C18` protects, and
  `sources.md` said Orwell attacked dead metaphors, where he attacked worn-out,
  dying ones.
- **The worked example.** `examples/before-after.md` is recounted under the new
  rules, and every number in it now follows from a stated count. Its word count was
  wrong (117 words, not 148), and its `C1` replacement also changed "completed" to
  "shipped".

### Added

- **`C23`, the document agrees with itself.** A count, amount, date, limit, or offer
  stated in two places must take one value, including a count over a list and a
  button label against the sentence beside it. Two places are compared only when
  they describe the same subject and the same measure. When the text does not say
  which value is right, the fix is to ask the author. Fixture 05 prompted it: the page
  promised five tools and listed six, and offered a plan "for 30 days" above a
  "Start free trial" button, and no rule covered either. The corpus now has 79
  rules.
- **English-only scope.** The base skill and `en-check` say that the corpus covers
  English only: a text in another language is named as such and left alone, and in
  a mixed-language text only the English is reviewed. `en-score` scores only the
  English and says in its frame line what it left out.
- **A search directed by genre in `en-check`.** In a policy, terms, a contract, or
  a text that grants permissions, every passive that gives, limits, or removes
  access is tested for its actor (`C6`). On a pricing, product, or offer page, every
  count, price, limit, date, and offer stated more than once is set side by side,
  button labels included (`C23`).
- **A fifth way for a rewrite to fail.** `slop.md` adds "Inventing": filling a gap
  with a number, a name, an example, or a cause the writer never supplied. A
  proposed replacement keeps every claim and adds none, and where a figure is
  missing the review marks the gap for the writer.

### Changed

- **Clarity rules.** `C6` requires the actor of any passive that grants, limits, or
  removes access or rights in rules, policies, contracts, and permissions
  (`may be read`, `can be suspended`), and says to ask the author when the text does
  not name one. `C20`'s exception now covers a summary claim that the next sentences
  make concrete, and Precision follows it. The `C9` example no longer breaks `C7`,
  the `C13` exception example now breaks the pattern it describes, and the file's
  own prose no longer leans on the construction that `S8` calls a formula.
- **Slop rules.** `S1` counts a listed word in any form (`leveraging`) and in
  British spelling (`utilise`), and counts a paraphrase that does its job
  (`dig deep into`) when the paragraph already holds two other tells; it adds
  `embrace`, `boast`, `shed light on`, `ever-evolving`, `commendable`, and
  `noteworthy`. `S8` catches the form split over two sentences. `S10`, now
  "Conversational glue and chat residue", covers stock openers and sign-offs and
  unfilled template slots. `S13` covers a trailing participle clause that only
  comments, and `stands as` or `serves as` in place of `is`. `S15` names only
  invented triads and leaves a real three-step process alone. `S17` has a test that
  can be run: at least four paragraphs, the longest at most one sentence longer than
  the shortest, and none under three sentences. `S19`, now "Self-answered
  questions", covers the question and clipped answer inside a paragraph, and exempts
  a FAQ. `S11` no longer claims that edited human prose almost never uses the
  both-audiences construction. `S4` leaves alone a qualifier that says how often or
  how surely a claim holds (`C18`), and `S6`, now "Inflated scale", covers false
  ranges.
- **Usage rules.** `usage.md` now separates questions that have a right answer from
  conventions. `U4` exempts labels, headings, and a short lead-in to a list. `U5`
  accepts AP's spaced em dash, Chicago's closed one, and the UK's spaced en dash,
  each held consistently, and a single dash cannot be inconsistent with itself.
  `U12` is now "Who vs that", and `U17` is now "Clichés and worn-out metaphors" and
  leaves alone a metaphor that has become the ordinary word. `U23` counts the page
  title as a heading like any other. `U14`, `U18`, `U19`, `U21`, and `U28` have
  smaller corrections.
- **Method rules.** Without a before state, a review now says once that it cannot
  tell which edit introduced a problem, and asks for the old version or a diff
  (`M1`). `M2`, now "Layout claims need source-level text", covers only claims that
  depend on layout: a count against a plain list, a spelling, or a term stands from
  any copy, and pasted or fetched text with no sign of flattening counts as the
  deliverable. `en-check` reports a layout claim read from a rendering under TO
  VERIFY and nowhere else. `M4` never licenses a mix that `U23` or `U28` forbids.
  `method.md` no longer says that every rule came from a review that went wrong:
  `M3` records a step a review got right.
- **Skills.** The trigger phrases in all three descriptions are unchanged; routing
  chose the right skill 128 times out of 128 in the test. `en-check` settles five
  things in its frame line, and its example now shows all five; findings are
  grouped by kind, each in three lines. `en-score` shows the count behind each
  sub-score, and its worked example is recomputed from stated counts: it had kept
  the sub-scores of a 210-word example under an 840-word frame. On a fetched or
  flattened page, `en-score` names the artifact it scored and marks Flow, and any
  sub-score that depends on layout, as provisional; it does not decline. The base
  skill counts tells per 300 words, where it said per hundred, and tells the agent
  to pass the text, the request, and any old version as the argument.
- **Tests.** `check_corpus.py` runs 13 checks instead of 10. It now requires
  `Monitor` among the disallowed tools, each write tool as a bare entry that a
  path-scoped entry cannot stand in for. It checks rule ranges and totals wherever
  they appear, part headings included, checks worked scores in every markdown file
  with a minimum per file, and checks arithmetic written out in prose.
  A weights row that does not parse fails instead of being skipped. The self-check
  matches inflected forms and no longer skips the text between bold labels. Two new
  guards keep Cyrillic out of `skills/` and stop either withdrawn promise from
  coming back. Each new check was broken on purpose in a scratch copy to confirm
  that the script then fails. CI runs with a read-only token. `tests/EVAL.md`
  corrects the fixture facts: fixture 01 has 142 words and three em dashes, and its
  `S19` question moves to may-report, since the exception allows one. Fixture 02's
  `S4` expectation now matches what `S4` lists. One sentence of fixture 03 is
  lengthened to 38 words so that `C14` is tested, fixture 04's band is now
  reachable, and fixture 05's findings name a rule (`C23`). The bands come from the
  six runs per fixture and are marked provisional, and the 2026-09-26 test is
  recorded in full, including what it left unfinished.
- **Documents.** README: the table of uses matches what the commands do, only the
  base skill is described as portable to other agents, the counts read 79 rules and
  51 with a test, a fix, and an exception, the credits match `sources.md`, the
  self-check is described at its real scope, and "Licence" becomes "License".
  `sources.md` credits each family: books and style manuals for most clarity and
  usage rules, observation of model output for the slop rules, and the project's own
  reviews for the method rules and `C23`. `NOTICE` gives working addresses for the
  Federal Plain Language Guidelines and the 18F Content Guide, both now archived on
  GitHub, and for the GOV.UK style guide; adds the Open Government Licence statement
  and both license links; and says which attributions a license requires and which
  are a courtesy. `CONTRIBUTING.md` sets the bar for a new rule by family and
  describes the checks the script runs.

### Removed

- The no-argument mode of `en-check` and `en-score`.
- The clustering multiplier in the slop density count.
- The promise that re-run scores land within about 0.3 of each other.

## [0.1.3] - 2026-09-24

### Changed

- **`M1` now handles the middle case.** The first run of fixture 05 showed the rule
  working at the edges and failing in between: the reviewer correctly kept an
  unrelated defect outside the spans the request named, then headed a section
  "introduced by the rewrite" with no before state in hand. Inferring from the spans
  a request names is useful and should not be banned; asserting causation from it
  should. The rule now separates the two and gives the phrasing that survives being
  wrong about which spans actually changed.

### Fixed

- `tests/EVAL.md` now describes fixture 05 as it actually behaves. Two expectations
  in the first draft were wrong: the `U19` numeral finding is subordinate to a real
  accuracy defect (the page claims five tools and lists six), and the CTA reads as a
  free-trial ambiguity rather than the billing contradiction it was modelled on,
  because the fixture also carries a "Start free trial" button. The tool-count error
  was an accident in the fixture's first draft that the first run caught; it stays,
  documented, because it is the kind of defect a comma-hunting proofread never finds.

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

[0.2.0]: https://github.com/andrgavrilenko/en-text/compare/v0.1.3...v0.2.0
[0.1.3]: https://github.com/andrgavrilenko/en-text/compare/v0.1.2...v0.1.3
[0.1.2]: https://github.com/andrgavrilenko/en-text/compare/v0.1.1...v0.1.2
[0.1.1]: https://github.com/andrgavrilenko/en-text/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/andrgavrilenko/en-text/releases/tag/v0.1.0
