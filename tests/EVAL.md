# Evaluating the skills by hand

`check_corpus.py` proves the corpus is well-formed. It cannot prove the corpus
produces good judgments; only running the skills on known texts does that. These
fixtures each target one failure mode. Run `/en-text:en-check tests/fixtures/<file>`
and `/en-text:en-score tests/fixtures/<file>` and compare against the tables.

An `en-check` run passes if every **must report** item appears with the right rule
ID and no **must not report** item appears. Wording of the proposed replacements is
not scored; the rule attribution is. **May report** items are neither required nor
forbidden.

An `en-score` run passes if the total lands in the band, the sub-scores land in the
ranges given with it, any other expectation stated with the band holds, and no
finding it names comes from a must-not row. It names at most three findings, so a
must-report item it leaves out is not a miss.

When an agent runs the skills, copy each fixture under a neutral name first (for
example `blind/a/post.md`), because these file names give the answer away, and do
not show the agent this file.

**How the numbers here were counted.** Words are counted in running prose: every
line except headings, quoted lines, table rows and code. A word is a
whitespace-separated token with at least one letter or digit, so `first-time` is one
word and a bullet marker or a spaced dash is none. A sentence ends at `.`, `?` or `!`
before a space, at a paragraph break, and at the end of a list item; a colon, a
semicolon or `e.g.` does not end one. A run whose own count differs by a few words
has not failed.

**How the bands were set.** Version 0.2.0 derives every sub-score from a count, and
that moved every band. The bands below were re-set on 2026-09-27 from the release
check recorded at the end of this file and from what each fixture's counts give
under `scoring.md`, then widened to about ±0.5. They rest on one to five runs per
fixture. When a clean run lands outside a band and its counts say it should, move
the band and record why. Read any single score as ±0.5.

## `fixtures/01-slop-heavy.md` — the machine dialect, dense

A social-media post of the kind a model produces from "write a LinkedIn post about
AI and leadership". 142 words, three em dashes. Tests whether the slop rules fire and
whether the density count drives the verdict to Unmistakable.

**Verdict (`en-check`):** Unmistakable. At 142 words the text is under the 150-word
floor, so the count is read raw rather than normalized. The must-report rows alone
give 16 weighted tells (still 11 if each rule counted only once), with `S15` and
`S16` doubled and `S21` adding one, and the band starts at 10. At that band the
report proposes a rewrite as replacement text and lists, by rule ID, what the
rewrite removes; the file is not edited. A must-report rule counts as found if it
appears as a finding of its own or in that list.

| Must report | Span |
|---|---|
| `S11` | "Whether you're a first-time founder or a seasoned executive" |
| `S12` | "one thing is clear", "The future belongs to those who embrace it" |
| `S7` | "In today's rapidly evolving landscape" |
| `S1` | leverage, unlock, empower, navigating |
| `S16` | Three bullets with bolded one-word labels, the same shape and length (6, 7 and 7 words) |
| `S15` | Every list is a triad built to reach three: the bullets (Speed, Focus, Trust), "navigating legacy processes, clinging to outdated playbooks, and hoping the storm passes", and "Start small. Pick one workflow. Measure everything." One tell for the document, doubled. |
| `S8` | "It's not about working harder. It's about working smarter." |
| `S10` | "The truth is", "Let that sink in" |
| `S21` | Three em dashes in 142 words (10.6 per 500): one tell for the document, not one per dash |
| `C20` | "ship faster", "new possibilities" with no figures anywhere |

| May report | |
|---|---|
| `S19` | "So what does this mean for you?" It is the only such question, and the exception allows one in a piece. |
| `S8` or `S9` | "don't just ship faster — they unlock entirely new possibilities", "the storm isn't passing — it's the new climate": the same contrast cadence, twice more |
| `S1`, `S2` | "embrace" inside the `S12` line, "landscape" inside the `S7` opener. One fix removes each pair, so each pair counts once. |
| `U17` | "in the trenches", "hoping the storm passes": clichés and worn-out metaphors |
| `C14` | "Start small. Pick one workflow. Measure everything. And above all, stay curious.": four short sentences in a row |

| Must not report | Why |
|---|---|
| Any `U` rule other than `U17` as an error | The mechanics are clean; the problem is emptiness. The bolded labels before the colons are labels, which `U4` exempts, and the three em dashes are spaced the same way every time, one system held consistently (`U5`). |
| `C6` passive | There is no passive in the text |
| Figures the post does not contain, in the rewrite or in a fix ("ship 40% faster") | `C20` takes the number from the author or asks for it. An invented figure trades a vague claim for a false one. |

**Score band:** 4.2–5.2 with marketing weights. Human voice 0–2: the must-report
rows alone put the raw count at 16, deep in the Unmistakable band. Correctness 6 or
higher: the only usage findings the post can carry are the `U17` clichés, which
count as errors.

## `fixtures/02-official-style.md` — clean of slop, unreadable anyway

An incident memo in the Official Style: every action is a nominalization, every
actor is in a by-phrase or absent. 160 words, counting the one-line title. Contains
no word from the S1 or S2 lists. Tests whether the clarity rules fire when the slop
rules have nothing to say, which is the case the anti-slop tools miss.

| Must report | Span |
|---|---|
| `C1` | "An evaluation of the incident ... was conducted by the platform team" |
| `C3` | evaluation, determination, introduction, completion, implementation, coordination, prevention, addition, establishment |
| `C4` | "The determination was made", "A review ... should be performed", "Consideration should be given" |
| `C6` | Passives that hide an actor the reader needs: "should be undertaken" (by whom?) |
| `C7` | "An evaluation of the incident that occurred on": the first eight words name neither the actor nor the main action. `C1` fires on the same sentence; the two findings do not conflict. |
| `C15` | "the implementation of the fix, which had been under consideration ... and which required ..., was completed" |
| `C17` | "It is important to note that", "It should be mentioned that" |

| May report | |
|---|---|
| `S4` | "It is important to note that" is one word away from the "it is important to remember that" that `S4` lists. On either frame, an `S4` finding shares its span with the `C17` finding and is not a second problem. |
| `C5` | "given to the establishment of an ownership model for shared infrastructure components": three prepositions in an unbroken chain |
| `C14` | The 37-word sentence that opens "It is important to note that the implementation of the fix", where the reader holds the subject through two relative clauses |

| Must not report | Why |
|---|---|
| Any `S` rule other than `S4` | No vocabulary, template or structural tells are present. The three recommendations are three real ones (`S15`'s exception). |
| `C6` for "no customer data was affected" | Actor irrelevant; the passive earns its place |

**Score band:** 6.5–8.5 with default weights. Sentence clarity 0–4. Human voice
7–10: with `S4` on neither frame the memo reads as Human, and with `S4` on both it
has 2 tells in 160 words, 3.8 per 300, which is Suspicious. The gap between the two
sub-scores is the point of the fixture.

## `fixtures/03-clean-human.md` — a voice that must survive

A short engineering post-mortem with a deliberate voice: a fragment, a 38-word
sentence two sentences before a 2-word one, one em dash, and an "X is not about A, it
is B" construction that corrects an expectation the reader actually holds. 168 words,
in sentences of 2 to 38 words. Tests for false positives. The corpus should find
almost nothing.

| Must not report | Why |
|---|---|
| `S8` for "The lesson is not about config loaders. It is that ..." | The reader does expect a lesson about config loaders; the correction is real. Exception applies. |
| `S21` or `U5` for the single em dash | One mark is never an `S21` finding, and a single dash cannot be inconsistent with itself (`U5`). |
| `C14` for the 38-word sentence, "We now have a test that asserts the runner ran at least one test — ... the day we set up the pipeline." | Its clauses arrive in order and never stack: the main clause comes first, and each later clause hangs off the one before it. Length says where to look; load decides. The 30-word sentence that opens "In the CI container" chains its clauses in order too, and is under `C14`'s threshold. |
| `S15` for "the import failed, the test runner never started, and the pipeline reported success" | Three things happened. Count the world. |
| Any fragment ("Not badly, and not for long, but we broke it") | Established voice, costs the reader nothing. |
| `C21` for "smallest" or "most" | Superlatives with a referent, not intensifiers. |

| May report | |
|---|---|
| At most two findings of any kind | If a run reports more, the corpus is over-triggering. |

**Score band:** 9.0–10.0 with default weights. Human voice 9 or higher. `en-score`
usually prints `No finding costs half a point.` A run that names one or two findings
still passes, provided none comes from a must-not row and the total stays in the
band; any finding it does name counts toward the two above. A score below the band
means the corpus is grading a voice as a defect.

## `fixtures/04-mixed-conventions.md` — correctness only

A short API guide whose prose is fine but whose conventions drift. 102 words of
prose under five headings. Tests the usage rules and the "consistency beats
correctness" principle: the findings should say "pick one", not "US is right".

| Must report | Span |
|---|---|
| `U28` | customise, behaviour against favor |
| `U1` | "a timestamp and a signature" against "retries, backoff, and logging" |
| `U23` | Title Case H1 "Getting Started With the API" against sentence-case H2s such as "Making requests" and "Rate limits". The page title is a heading like the others. |
| `U2` | "returns a 429, the response includes", "stable across versions, the message text is not" |
| `U15` | "e.g." without a following comma, if the run settles on US style |

| Must not report | Why |
|---|---|
| Any `S` rule | The prose is plain |
| `C6` for "Requests are limited to 100 per minute per key" | The limit applies to every key automatically, with no one deciding case by case, so `C6`'s ordinary question decides, and the actor is irrelevant |
| `U28` as "wrong spelling" | Must be reported as a mixture to resolve, not as an error in either direction |
| The H1 cleared as a system of its own (`M4`) | Title case on the page title alone is still two systems in one document, and `M4` never licenses a mix that `U23` forbids |

**Score band:** 8.0–9.0 with reference-docs weights. Correctness 4–6: two splices,
the `e.g.` comma and three drifting conventions make five or six counted issues, and
under 150 words the count itself is the rate. Every other dimension 8 or higher.
Under those ranges the total can run from 7.0 to 9.0; a run that counts nothing
outside Correctness lands between 8.5 and 9.0.

## `fixtures/05-flattened-rendering.md` — what a rendering cannot prove

A pricing page fetched from the web and flattened into markdown, so the comparison
table has lost its row structure. 352 words outside the headings and the fetch note.
This fixture tests `method.md` and `C23`: what a rendering cannot prove, and what it
still can. It is the only fixture where the right answer is partly a refusal.

Invoke `en-check` with an attribution claim attached, because `M1` is half of what is
being tested:

```
/en-text:en-check tests/fixtures/05-flattened-rendering.md — fetched from our
pricing page. I rewrote the four alert and export descriptions yesterday; tell me
whether my rewrite introduced any problems.
```

Invoke `en-score` with the path alone; the note at the top of the file says what the
file is.

| Must report | Span |
|---|---|
| `M2` framing | The frame line says this is a rendering rather than source, and the report names what that costs: which description sits in which row of the plan table cannot be checked from this copy |
| `C23` | "Basic covers 2 tools, Team all 5" and "Five tools sharing one event schema" against the six tools the Tools section lists. Basic's 2 is right; both fives are wrong, and this is the one finding on the page that costs money. It stands as a fact, not as something to verify: the Tools section is a list written as a list in the same copy, and a count of names does not depend on layout. |
| `C23` | "Get the Team plan for 30 days" above a button reading "Start free trial", with a Monthly billing toggle higher up. The sentence never says the 30 days are free and never says the plan is a subscription. The fix asks the author which is meant rather than choosing. |
| `U2` | "Export before then if you need them, the Scheduled Export tool keeps working until the last day." |

| Must report, and how | |
|---|---|
| `M1` | The request claims a recent rewrite with no before state attached. The report says once, before the findings, that it cannot tell which of them the rewrite introduced, and asks for the previous version or a diff. Findings may say where a pattern sits relative to the four named descriptions; they may not say the rewrite caused it. A section headed "introduced by the rewrite" fails, and so does "your rewrite dropped Webhook Relay's description". |

| Must not report | Why |
|---|---|
| A cross-reference finding asserting the Team tier's descriptions are shifted | The three descriptions under "03 Alerting and export" match the Tools section exactly. The fourth tool, Webhook Relay, has no description in the plan table, which in a real table is the header-row product carrying none. A flattened copy cannot distinguish that from a shift, so `M2` forbids the assertion. It may be raised as "verify in the source". |
| "No price appears anywhere on the page" | Prices render at runtime and never reached this copy. Absent from the artifact, not from the page (`M2`). |
| `C22` for "tools" vs "plans" vs "Basic/Team" | Distinct things: the products, the packages, the package names. |
| Any `S` structural tell for the repeated three-item lists | The tiers genuinely have those counts, and the duplication between the table and the Tools section is a table, not a rhetorical shape. |
| `S19` for the questions under "Questions" | A FAQ is exempt: its questions are the reader's own, set up for lookup. |

**Score band:** 8.3–9.5 with marketing weights, and only with the caveat. `en-score`
scores this fixture rather than declining: the frame line names the artifact it
scored (a fetched page flattened to markdown) and marks Flow and cohesion, and any
other sub-score that depends on layout, as provisional. A run that declines fails,
and so does one that scores without naming the rendering. `C23` should be among the
findings it names.

**Why this fixture exists:** on 2026-09-21 a real review of a production site
produced a confident headline finding that four product descriptions were shifted by
one row. They were not. The finding was an artifact of exactly this conversion, and
it survived into a report to the site's owner. `M2` is the rule that would have
stopped it.

**A note on the tool count.** The mismatch between "five tools" and the six listed
was not planted; it was a mistake in the first draft of this fixture, and the first
run caught it. It stays, because an accuracy trap a reviewer must notice is worth
more than a tidy fixture, and because it is the kind of defect that survives every
proofread aimed at commas. Since 0.2.0 it has a rule of its own, `C23`, which also
covers the CTA.

## Recording a run

When you change a rule, paste the relevant findings for the affected fixture into
the PR description with the date and the model used. Judgments drift between model
versions; the record is what lets the next person tell a corpus regression from a
model change.

## Recorded runs

### 2026-09-21, corpus 0.1.1, Claude Fable 5.1 via Claude Code

This run scored fixtures 01 and 02 with `en-score` and ran 03 and 04 through
`en-check` only, which gives no number. The 0.1.1 bands for 01 and 02 came from it;
those for 03 and 04 were the author's predictions, and no run had scored them. Two of
the predictions made before it were wrong in the same direction: the corpus was
stricter than its author expected. `S4` fired on the two metadiscourse frames in
fixture 02, although it lists only a near relative of one of them and both belong to
`C17`, and `U17` fired on clichés a marketing reader would forgive. The bands moved;
the rules did not.

| Fixture | Skill | Result | Verdict |
|---|---|---|---|
| 01-slop-heavy | en-score | 3.1 (marketing). Voice 0.5, correctness 7.5. All 11 must-report rules found; `U17` also fired. | pass |
| 02-official-style | en-score | 5.3 (default). Clarity 1.5, voice 6.5. All 7 must-report rules found; "was affected" correctly cleared; `S4` fired on the two frames. | pass |
| 03-clean-human | en-check | 0 findings. `S8`, `S21`, `S15`, `C11`, `C22` each considered and cleared with the exception named. | pass |
| 04-mixed-conventions | en-check | `U2` ×2, `U28` (reported as a mixture, US default named), `U1`, `U23`, `U15`. No `S` findings. | pass |

The 03 row records what the run named. It does not show `C14`, `C21` or the fragment
being considered, and the 0.1.1 text of fixture 03 had no sentence over 35 words, so
`C14` was never exercised. Version 0.2.0 lengthened one sentence to 38 words.

### 2026-09-24, corpus 0.1.2, Claude Opus 5 via Claude Code

First run of fixture 05, the run that `method.md` was written for.

| Fixture | Skill | Result | Verdict |
|---|---|---|---|
| 05-flattened-rendering | en-check | `M2` held completely: the duplicate descriptions were identified as a flattening artifact and no shift was asserted; the absent prices were not reported missing; `S16` was considered and cleared on its stated exception. Found the tool-count error, which the fixture's author had not. `M1` held in part: the `U2` splice was correctly filed outside the named spans, but a section was headed "introduced by the rewrite" with no before state. | partial |

That partial is what produced the `M1` refinement in 0.1.3: inference from the
spans the request names is worth stating, and must be phrased as observation rather
than as a claim about what the writer did.

One thing this run exposed that is not a corpus issue: after `claude plugin
update`, a running session still resolves the skill from the old cache path until
restart, and the skills found the corpus by the "directory named `references`
whose parent is `en-text`" instruction rather than by the relative path. Version
0.2.0 keeps that search as the fallback behind `${CLAUDE_SKILL_DIR}`, and adds one
condition: never mix files from two installed versions.

### 2026-09-26, corpus 0.1.3, pre-publication test

A test run before submitting 0.1.3 to the plugin directory. The skills ran on Claude
Sonnet 5, and so did the graders and the skeptics; test generation and the corpus
review ran on Claude Opus 5.5. Each skill run worked on a copy of its fixture under a
neutral name and never saw this file; a separate agent graded it against this file.

What was tested: the five fixtures (`en-check` once each, `en-score` six times each);
19 new cases in 26 runs, 18 of them generated to probe one weakness each and one
built by hand around a project with its own `STYLE.md`; routing, with 32 requests
put to four classifier models; a review of the corpus by 11 reviewers, whose 186
findings went to independent skeptics, who upheld 136; and `en-check` on four of the
repo's own files.

What held: routing chose the right skill 128 times out of 128. An instruction hidden
in a reviewed text was ignored and reported as a defect. A project's own `STYLE.md`
was found and followed (`M3`). Code, logs, quotations and non-English words inside an
English text were left alone. `M2` held on a flattened pricing table that carried no
warning note, and `M1` attributed correctly when the request included the old
version. On fixture 03, `en-check` found nothing and explained why each trap was not
a defect. On the new cases, `en-check` passed 11 of 19 (3 partial, 5 failed) and
`en-score` passed 3 of 6 (2 partial, 1 failed).

What failed, six blockers, all addressed in 0.2.0:

- B1. `context: fork` hides the conversation, so the promised mode without arguments
  had nothing to review.
- B2. About ten sentences in the `en-check` and `en-score` skill files closely
  followed another plugin's skill files, so the repo's claim that en-text shares no
  text with that plugin was false.
- B3. `en-score` had to name three findings and invented them on clean text,
  including findings that the rules' own exceptions clear (fixture 03, three new
  cases).
- B4. Slop density had no floor for short texts (two dashes in a 167-word post came
  out Suspicious), a clustering multiplier with no factor, and a 10+ action that told
  a read-only skill to rewrite.
- B5. `scoring.md` promised re-run scores no more than 0.3 apart; six runs per
  fixture spread by up to 1.4 (table below).
- B6. Some corpus examples broke the corpus's own accuracy rule: the `C3` and `C20`
  examples changed or invented facts, the base skill's `[C4]` example had no empty
  verb, and `U10`, `U12`, `S4` against `C18`, and the Orwell entry in `sources.md`
  were wrong.

Against the 0.1.3 version of this file:

| Fixture | en-check | en-score, 3 graded runs |
|---|---|---|
| 01-slop-heavy | fail: `S15` and `C20` missed; Unmistakable reached | 0 pass: all above the band |
| 02-official-style | fail: `C6` and `C5`/`C7` missed | 1 pass: voice ranged from 6.0 to 9.5 |
| 03-clean-human | pass | 0 pass: in the band every time, failed on invented findings (`C14`, `U5` on the single dash, `C7`, `C10`, `C22`) |
| 04-mixed-conventions | fail: `U23` missed | 1 pass: two runs above a band that was partly out of reach |
| 05-flattened-rendering | fail: the CTA missed; `M1` and `M2` held and the tool count was found | 0 pass: scored as ordinary copy, with at most a passing note on the rendering |

Repeatability, six `en-score` runs per fixture:

| Fixture | Totals | Spread | Mean |
|---|---|---|---|
| 01-slop-heavy | 4.6 · 3.7 · 4.5 · 4.1 · 3.7 · 3.8 | 0.9 | 4.1 |
| 02-official-style | 6.7 · 5.3 · 5.9 · 6.0 · 6.6 · 6.2 | 1.4 | 6.1 |
| 03-clean-human | 8.8 · 9.1 · 8.9 · 8.8 · 9.2 · 9.0 | 0.4 | 9.0 |
| 04-mixed-conventions | 7.8 · 7.5 · 7.7 · 7.8 · 7.5 · 8.0 | 0.5 | 7.7 |
| 05-flattened-rendering | 8.4 · 8.1 · 8.4 · 8.3 · 8.1 · 8.4 | 0.3 | 8.3 |

Left unfinished: repeat runs of the failed `en-check` verdicts, and the analysis of
their causes, stopped at a usage limit, and each `en-check` verdict above is a single
run. The causes were worked out by hand from the upheld corpus findings. Where a
failed run and a corpus reviewer agree (the density problems, `M4` against `U23`)
the conclusion is firm; where a single `en-check` run is the only evidence, it may
be chance. Expectations for the generated cases were written by the generator, and
some are arguable. One grader recorded cleared exceptions on fixture 03 as forbidden
hits, so the key verdicts were re-checked by hand. Routing was judged by classifier
models, not by Claude Code's own skill selection.

### 2026-09-27, corpus 0.2.0, release check

A blind rerun before release, aimed at the cases the pre-publication test had
failed. The skills ran on Claude Sonnet 5, each on a copy of its text under a neutral
name and without this file; the coordinating session graded every run by hand
against this file and the case expectations. The runs went in four batches, and the
corpus changed between them: the failures of one batch produced a fix, and the next
batch re-ran what the fix touched. Of 32 runs launched, 26 produced a report. Six
`en-score` runs produced none: five stalled and one ran past the output limit, five
of the six in the first batch of 17 concurrent runs and four of the six on fixture 02.
The last batch, which added the compact-counting step, ran fixture 02 three times
with no failure. The executors ran in the maintainer's environment, whose global
instructions include a preference about dashes in public posts; that may have nudged
the `S21` notes.

| Case | Skill | Final result | Verdict | How it got there |
|---|---|---|---|---|
| 01-slop-heavy | en-check | Unmistakable on the raw count; every must-report rule; the rewrite invents nothing | pass | the first run passed but its rewrite invented specifics; "Inventing" in `slop.md` fixed that |
| 01-slop-heavy | en-score | 4.8, then 4.7 | pass | the second run names the voice problem (`S1`) through the new dimension-level finding |
| 03-clean-human | en-check | no findings | pass | |
| 03-clean-human | en-score | 10.0, no finding named | pass | earlier runs named `C20` on a summary line, then `C8` on a punchline; fixed by the summary exception and by `en-score` dropping what `en-check` drops |
| 04-mixed-conventions | en-check | `U23` with the H1 included, `U1`, `U15`, `U28` as a mix, `U2` twice | pass | the `M4`-over-`U23` failure of 2026-09-26 is gone |
| 04-mixed-conventions | en-score | 8.7 | pass | |
| 05-flattened-rendering | en-check | `M1` and `M2` held in both runs, and both found the tool-count `C23`; the CTA `C23` and the `U2` splice were each found in one of the two runs | partial | the second run followed the genre-directed search and kept the layout point under TO VERIFY only |
| 05-flattened-rendering | en-score | 9.3 with the caveat, Flow provisional, `C23` named | pass | one unlabeled "mix" finding that `U19` clears |
| structural slop, no listed words | en-check | Unmistakable; `S19`, `S17`, `S18`, `S16`, `S8` | partial | `S15` not reported: the run took the triads for counted ones |
| data-processing policy | en-check | `C6` on "may be read", nothing else | pass | missed in the first batch; the genre-directed search fixed it |
| LinkedIn post, two dashes | en-check | the public-post notes only, no density verdict | pass | the `B4` acceptance case |
| literary voice | en-score | 10.0, no finding named | pass | the `B3` acceptance case |
| concrete marketing | en-score | 9.9, one minor `C20` | pass | an earlier run raised a false `C23` on two different offers; `C23` now pairs only the same subject and measure |
| bank paper, technical vocabulary | en-score | 9.7, only the required `U2` | pass | the technical senses of `S1`, `S3` and `S6` words were cleared |

Repeatability on the release candidate: three runs on fixture 02 gave 6.9, 7.7 and
8.0, a spread of 1.1. The runs agreed on what was wrong and differed on how many
instances a dense sentence holds: 19, 12 and 10 in Sentence clarity. Two runs of an
earlier draft gave 6.8 and 6.9. Fixture 01 gave 4.8 and 4.7.

Compared with 0.1.3, totals rose where a text fails in one dimension only: fixture
02 from a mean of 6.1 to 7.5, fixture 04 from 7.7 to 8.7, and clean texts now reach
10.0. That is the counted tables working as written, since a dimension with nothing
to count scores 10, and the bands above follow it.

Left open: `S15` on the structural-slop case, and the two single misses on fixture
05, rest on one run each. The spread on a dense middling text is still near the
0.1.3 level. Whether a text that fails badly in one dimension should score lower
overall is a calibration question for a later version.
