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
AI and leadership". 165 words. Tests whether the slop rules fire and whether the
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
| Any `U` rule as an error | The text is grammatically clean; its problem is emptiness |
| `C6` passive | There is no passive in the text |

**Score band:** 1.0–3.0 with marketing weights. Human voice 0–1. Correctness 8+.

## `fixtures/02-official-style.md` — clean of slop, unreadable anyway

An incident memo in the Official Style: every action is a nominalization, every
actor is in a by-phrase or absent. 170 words. Contains no word from the S1 or S2
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
| Any `S1`–`S13` vocabulary or phrase tell | None are present |
| `C6` for "no customer data was affected" | Actor irrelevant; the passive earns its place |

**Score band:** 3.0–5.0 with default weights. Human voice 9+. Sentence clarity 0–3.
The gap between those two numbers is the point of the fixture.

## `fixtures/03-clean-human.md` — a voice that must survive

A short engineering post-mortem with a deliberate voice: a fragment, a 40-word
sentence next to a 4-word one, one em dash, and an "X is not about A, it is B"
construction that corrects an expectation the reader actually holds. 170 words.
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

A short API guide whose prose is fine but whose conventions drift. 150 words. Tests
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

## Recording a run

When you change a rule, paste the relevant findings for the affected fixture into
the PR description with the date and the model used. Judgments drift between model
versions; the record is what lets the next person tell a corpus regression from a
model change.
