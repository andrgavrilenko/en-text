# Evaluating the skills by hand

`check_corpus.py` proves the corpus is well-formed. It cannot prove the corpus
produces good judgments; only running the skills on known texts does that. These
fixtures each target one failure mode. Run `/en-text:en-check tests/fixtures/<file>`
and `/en-text:en-score tests/fixtures/<file>` and compare against the tables.

A run passes if every **must report** item appears with the right rule ID, no
**must not report** item appears, and the score lands in the band. Wording of the
proposed replacements is not scored; the rule attribution is.

## `fixtures/01-slop-heavy.md` — the machine dialect, dense

A social-media post of the kind a model produces from "write a LinkedIn post about
AI and leadership". 142 words. Tests whether the slop rules fire and whether the
density table drives the verdict to "unmistakable".

| Must report | Span |
|---|---|
| `S11` | "Whether you're a first-time founder or a seasoned executive" |
| `S12` | "one thing is clear", "The future belongs to those who embrace it" |
| `S7` | "In today's rapidly evolving landscape" |
| `S1` | leverage, unlock, empower, navigating |
| `S16` | Three bullets with bolded one-word labels, equal length |
| `S15` | Exactly three bullets |
| `S8` | "It's not about working harder. It's about working smarter." |
| `S10` | "The truth is", "Let that sink in" |
| `S19` | "So what does this mean for you?" |
| `S21` | Four em dashes in 165 words |
| `C20` | "ship faster", "new possibilities" with no figures anywhere |

| Must not report | Why |
|---|---|
| Any of `U1`–`U10`, `U19`–`U28` as an error | The mechanics are clean; the problem is emptiness. (`U17` dead metaphors may fire: "in the trenches", "stay curious".) |
| `C6` passive | There is no passive in the text |

**Score band:** 1.5–3.5 with marketing weights. Human voice 0–1. Correctness 7+.

## `fixtures/02-official-style.md` — clean of slop, unreadable anyway

An incident memo in the Official Style: every action is a nominalization, every
actor is in a by-phrase or absent. 158 words. Contains no word from the S1 or S2
lists. Tests whether the clarity rules fire when the slop rules have nothing to say,
which is the case the anti-slop tools miss.

| Must report | Span |
|---|---|
| `C1` | "An evaluation of the incident ... was conducted by the platform team" |
| `C3` | evaluation, determination, introduction, completion, implementation, coordination, prevention, addition, establishment |
| `C4` | "The determination was made", "A review ... should be performed", "Consideration should be given" |
| `C6` | Passives that hide an actor the reader needs: "should be undertaken" (by whom?) |
| `C15` | "the implementation of the fix, which had been under consideration ... and which required ..., was completed" |
| `C17` | "It is important to note that", "It should be mentioned that" |
| `C5` or `C7` | "in accordance with the procedure that was established following" |

| Must not report | Why |
|---|---|
| Any of `S1`–`S3`, `S5`–`S13` | No vocabulary or template tells are present. (`S4` may fire on the two "It is important to note" frames; the corpus lists them there as well as under `C17`.) |
| `C6` for "no customer data was affected" | Actor irrelevant; the passive earns its place |

**Score band:** 4.0–6.0 with default weights. Human voice 6–8 (two S4 frames, then
up to a point off for the agentless register). Sentence clarity 0–3. The gap between
those two numbers is the point of the fixture.

## `fixtures/03-clean-human.md` — a voice that must survive

A short engineering post-mortem with a deliberate voice: a fragment, a 40-word
sentence next to a 4-word one, one em dash, and an "X is not about A, it is B"
construction that corrects an expectation the reader actually holds. 162 words.
Tests for false positives. The corpus should find almost nothing.

| Must not report | Why |
|---|---|
| `S8` for "The lesson is not about config loaders. It is that ..." | The reader does expect a lesson about config loaders; the correction is real. Exception applies. |
| `S21` for the single em dash | One mark is never a finding. |
| `C14` for the 40-word sentence | Its clauses arrive in order and never stack. |
| `S15` for "the import failed, the test runner never started, and the pipeline reported success" | Three things happened. Count the world. |
| Any fragment ("Not badly, and not for long, but we broke it") | Established voice, costs the reader nothing. |
| `C21` for "smallest" or "most" | Superlatives with a referent, not intensifiers. |

| May report | |
|---|---|
| At most two findings of any kind | If a run reports more, the corpus is over-triggering. |

**Score band:** 8.0–9.5 with default weights. Human voice 9+. A run that scores this
text below 8 is grading on a curve in the wrong direction.

## `fixtures/04-mixed-conventions.md` — correctness only

A short API guide whose prose is fine but whose conventions drift. 100 words. Tests
the usage rules and the "consistency beats correctness" principle: the findings
should say "pick one", not "US is right".

| Must report | Span |
|---|---|
| `U28` | customise, behaviour against favor |
| `U1` | "a timestamp and a signature" against "retries, backoff, and logging" |
| `U23` | Title-case H1 against sentence-case H2s |
| `U2` | "returns a 429, the response includes", "stable across versions, the message text is not" |
| `U15` | "e.g." without a following comma, if US spelling is assumed |

| Must not report | Why |
|---|---|
| Any `S` rule | The prose is plain |
| `C6` for "Requests are limited to 100 per minute" | Actor irrelevant |
| `U28` as "wrong spelling" | Must be reported as a mixture to resolve, not as an error in either direction |

**Score band:** 6.0–7.5 with reference-docs weights. Correctness 4–6; every other
dimension 8+.

## `fixtures/05-flattened-rendering.md` — what a rendering cannot prove

A pricing page fetched from the web and flattened into markdown, so the comparison
table has lost its row structure. 320 words. This fixture tests `method.md`, and it
is the only one where the right answer is partly a refusal.

Invoke it with an attribution claim attached, because `M1` is half of what is being
tested:

```
/en-text:en-check tests/fixtures/05-flattened-rendering.md — fetched from our
pricing page. I rewrote the four alert and export descriptions yesterday; tell me
whether my rewrite introduced any problems.
```

| Must report | Span |
|---|---|
| `M2` framing | The frame line must say this is a rendering rather than source, and name what that costs |
| accuracy | "Basic covers 2 tools, Team all 5" and "Five tools sharing one event schema" against the six tools the page then lists. Two counts, both wrong, and the one finding on this page that costs money |
| `U2` | "Export before then if you need them, the Scheduled Export tool keeps working until the last day." |
| CTA ambiguity | "Get the Team plan for 30 days" under a button reading "Start free trial", with a Monthly billing toggle above. The sentence never says the 30 days are free and never says the plan is a subscription |

| Must report, and how | |
|---|---|
| `M1` | The request claims a recent rewrite with no before state attached. Findings may say a pattern lines up with the named spans; they may not say the rewrite caused it. "The four you named share a shape the other two lack" passes. A section titled "introduced by the rewrite" does not. |

| Must not report | Why |
|---|---|
| A cross-reference finding asserting the Team tier's descriptions are shifted | The three descriptions under "03 Alerting and export" match the Tools section exactly. The fourth tool, Webhook Relay, has no description in the plan table, which in a real table is the header-row product carrying none. A flattened copy cannot distinguish that from a shift, so `M2` forbids the assertion. It may be raised as "verify in the source". |
| "No price appears anywhere on the page" | Prices render at runtime and never reached this copy. Absent from the artifact, not from the page (`M2`). |
| `C22` for "tools" vs "plans" vs "Basic/Team" | Distinct things: the products, the packages, the package names. |
| Any `S` structural tell for the repeated three-item lists | The tiers genuinely have those counts, and the duplication between the table and the Tools section is a table, not a rhetorical shape. |

**Score band:** not scored. Running `en-score` on this fixture should decline or
heavily caveat, since a flattened rendering with missing runtime content cannot
carry a repeatable number.

**Why this fixture exists:** on 2026-09-21 a real review of a production site
produced a confident headline finding that four product descriptions were shifted by
one row. They were not. The finding was an artifact of exactly this conversion, and
it survived into a report to the site's owner. `M2` is the rule that would have
stopped it.

**A note on the tool count.** The mismatch between "five tools" and the six listed
was not planted; it was a mistake in the first draft of this fixture, and the first
run caught it. It stays, because an accuracy trap a reviewer must notice is worth
more than a tidy fixture, and because it is the kind of defect that survives every
proofread aimed at commas.

## Recording a run

When you change a rule, paste the relevant findings for the affected fixture into
the PR description with the date and the model used. Judgments drift between model
versions; the record is what lets the next person tell a corpus regression from a
model change.

## Recorded runs

### 2026-09-21, corpus 0.1.1, Claude Fable 5.1 via Claude Code

The bands above were set from this run. Before it, two predictions were wrong in
the same direction: the corpus is stricter than its author expected, because
`S4` overlaps `C17` and `U17` fires on clichés a marketing reader would forgive.
Both are the corpus behaving as written, so the bands moved, not the rules.

| Fixture | Skill | Result | Verdict |
|---|---|---|---|
| 01-slop-heavy | en-score | 3.1 (marketing). Voice 0.5, correctness 7.5. All 11 must-report rules found; `U17` also fired. | pass |
| 02-official-style | en-score | 5.3 (default). Clarity 1.5, voice 6.5. All 7 must-report rules found; "was affected" correctly cleared; `S4` fired on the two frames. | pass |
| 03-clean-human | en-check | 0 findings. `S8`, `S21`, `S15`, `C11`, `C22` each considered and cleared with the exception named. | pass |
| 04-mixed-conventions | en-check | `U2` ×2, `U28` (reported as a mixture, US default named), `U1`, `U23`, `U15`. No `S` findings. | pass |

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
whose parent is `en-text`" instruction rather than by the relative path. Keep
that instruction; it is what made the run work.
