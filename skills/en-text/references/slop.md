# Slop — the machine dialect

Rules `S1`–`S24`. These catch the patterns that make a text read as machine-made.

## How to use this file

**Nothing here is an error in itself.** Every item below appears in good human
writing. What marks text as model output is density and evenness: many tells, spread
uniformly, with no stretch of plain sentences between them.

Count first. Normalize to 300 words of running prose (tells × 300 ÷ word count):

| Tells per 300 words | Read as | Action |
|---|---|---|
| 0–1 | Human | Leave it alone |
| 2–4 | Suspicious | Report the worst one or two |
| 5–9 | Reads as AI to an attentive reader | Report all, propose a rewrite |
| 10+ | Unmistakable | Rewrite, then report what changed |

Two weightings adjust the count:

- **Clustering multiplies.** Three tells in one paragraph is worse than six spread
  over a 2000-word article.
- **Structural tells (S14–S20) count double.** A reader forgives an odd word much
  sooner than a shape that repeats.

Never flag a tell inside quoted material, and never flag an author whose established
voice includes the pattern. Every rule below has a stated exception; they are not
optional reading.

---

## Part 1 — Words (S1–S6)

### S1 — Model-favored verbs and adjectives

These are the load-bearing vocabulary of model prose. Each is a real English word;
each is used by models far more often than by people.

`delve`, `leverage` (as a verb), `utilize`, `harness`, `showcase`, `underscore`,
`unpack` (a concept), `unlock` (potential), `elevate`, `empower`, `foster`,
`facilitate`, `navigate` (a challenge), `spearhead`, `streamline`, `bolster`,
`cultivate`, `embark`, `resonate`, `illuminate`, `amplify`, `curate`, `champion`
(as a verb), `usher in`, `pave the way`.

`robust`, `seamless`, `crucial`, `pivotal`, `vital`, `comprehensive`, `holistic`,
`nuanced`, `multifaceted`, `intricate`, `myriad`, `plethora`, `vibrant`, `dynamic`,
`innovative`, `cutting-edge`, `state-of-the-art`, `transformative`, `groundbreaking`,
`unparalleled`, `unwavering`, `meticulous`, `profound`, `compelling`, `invaluable`.

**Test:** Count occurrences across the running prose. One is a word choice. A
cluster is a fingerprint.

**Fix:** The plain word. `leverage` → `use`. `utilize` → `use`. `facilitate` →
`help` or `run`. `robust` → say what it survives. `comprehensive` → say what it
covers. `seamless` → say what step disappeared.

**Exception:** The technical sense. `Leverage` in finance, `robust` in statistics,
`dynamic` in programming, `delve` in a geological paper. Judge by domain, not by
string match.

### S2 — Abstract nouns that say nothing

`landscape`, `realm`, `tapestry`, `journey`, `ecosystem`, `paradigm`, `synergy`,
`framework` (when it frames nothing), `insights`, `learnings`, `takeaways`,
`best practices`, `game-changer`, `deep dive`, `treasure trove`, `wealth of`,
`testament to`, `beacon of`, `cornerstone of`, `the fabric of`.

**Test:** Replace the noun with "thing". If the sentence loses nothing, the noun was
decoration.

**Fix:** Name the specific thing, or cut the phrase.

**Exception:** The literal sense. A `landscape` with hills in it, an `ecosystem`
with organisms, a `framework` that is a piece of software with that word in its
name.

### S3 — The intensifier stack

`truly`, `deeply`, `incredibly`, `remarkably`, `notably`, `significantly`,
`substantially`, `fundamentally`, `undoubtedly`, `certainly`, `absolutely`,
`genuinely`, `particularly`, `effortlessly`, `seamlessly`.

**Test:** Count per paragraph. One is fine. Three is a tic. See also `C21`.

**Fix:** Delete. If the sentence then reads as weak, the fix is a stronger verb or
noun, not the adverb back.

**Exception:** `Significantly` and `substantially` in their technical senses
(statistical significance, a material change in a contract). `Notably` when it
introduces a specific exception to a general claim.

### S4 — Corporate hedging

`arguably`, `it is worth noting that`, `it is important to remember that`,
`that said`, `at the end of the day`, `when all is said and done`, `in many ways`,
`to some extent`, `more often than not`.

**Test:** Does the hedge say anything about the evidence? These do not; they buy
time. Distinguish from honest hedges (`C18`).

**Fix:** Delete the phrase and start the sentence on its content.

**Exception:** `That said` and `to some extent` when they introduce a real
concession that the next sentence actually delivers.

### S5 — Compound modifier soup

`carefully crafted`, `thoughtfully designed`, `expertly curated`, `purpose-built`,
`battle-tested`, `industry-leading`, `best-in-class`, `world-class`, `next-level`,
`rock-solid`, `lightning-fast`, `razor-sharp`, `laser-focused`.

**Test:** Can the modifier be verified? `lightning-fast` cannot. `40 ms` can.

**Fix:** Replace with the fact. `lightning-fast` → `responds in 40 ms`.

**Exception:** A modifier backed by a fact in the same sentence: `battle-tested
across 400 production deployments` is a claim with evidence attached.

### S6 — False precision about scale

`countless`, `endless`, `infinite`, `a myriad of`, `untold`, `a staggering number
of`, `exponentially` (used for any growth), `orders of magnitude` (used loosely).

**Test:** Is the number known? If yes, it is being withheld. If no, the word is
pretending.

**Fix:** Give the number, or say you do not know it.

**Exception:** The literal sense. `Exponentially` for growth that is actually
exponential. `Orders of magnitude` when the ratio really is a power of ten.

---

## Part 2 — Phrases and sentence templates (S7–S13)

### S7 — The scene-setting opener

`In today's fast-paced world`, `In an era of`, `In the ever-evolving landscape of`,
`Now more than ever`, `In recent years, there has been growing interest in`,
`As technology continues to advance`, `Since the dawn of`.

**Test:** Does the first sentence contain a claim the reader could disagree with?
If not, it is scenery.

**Fix:** Delete the sentence. The article almost always starts better at sentence
two.

**Exception:** A historical piece where the era genuinely is the subject and the
opener names a specific date or event rather than a mood.

### S8 — "It's not X, it's Y"

`It's not just a tool, it's a philosophy.` `This isn't about code, it's about
people.` `The question isn't whether, it's when.`

**Test:** Did anyone claim X? If nobody holds the expectation being corrected, the
construction is manufactured for cadence. Count occurrences: more than one per
piece is a formula.

**Fix:** State Y. Drop the invented X.

**Exception:** The reader actually holds the expectation X, and the sentence is
doing the work of correcting it. Once.

### S9 — The negative-parallel flourish

`Not because it is easy, but because it is hard.` `Less a X than a Y.` `Not only
does it A, it also B.`

**Test:** Same as `S8`: is the contrast real, or manufactured for cadence?

**Fix:** State the positive claim plainly.

**Exception:** A genuine two-part claim where both halves are true and the reader
needs both: `Not only did the test pass, it passed faster than the old one.`

### S10 — Conversational glue

`Let's dive in`, `Let's break it down`, `Here's the thing`, `Here's the kicker`,
`But wait, there's more`, `Spoiler alert`, `Plot twist`, `The truth is`,
`Let that sink in`, `Buckle up`.

**Test:** Delete the phrase. Nothing changes except the word count.

**Fix:** Delete it.

**Exception:** A deliberately chatty register the author holds consistently, such as
a personal newsletter, where the reader has opted into the voice.

### S11 — The reader address

`Whether you're a seasoned developer or just starting out`, `If you're like most
people`, `We've all been there`, `You might be wondering`, `Sound familiar?`

The both-audiences construction (`Whether you're X or Y`) is the strongest single
tell in this file. It appears almost nowhere in edited human prose.

**Test:** Does the sentence name a reader, or a range of readers? A range is the
tell.

**Fix:** Name the one reader you are writing for, or say nothing about the reader.

**Exception:** Instructions that genuinely branch on the reader's situation, where
the branch is then followed: `If you are on Windows, run X. On macOS, run Y.`

### S12 — Closing boilerplate

`In conclusion`, `To sum up`, `At the end of the day`, `Ultimately, the key
takeaway is`, `Only time will tell`, `The possibilities are endless`,
`One thing is clear:`, `The future of X is bright`.

**Test:** Does the final paragraph contain anything not already said above it?

**Fix:** End on the last real sentence. Most pieces improve by deleting the final
paragraph entirely.

**Exception:** A long document with a genuine summary that a reader might jump to,
such as an executive summary or an abstract, labeled as such.

### S13 — Hollow value statements

`plays a crucial role in`, `is a testament to`, `serves as a reminder that`,
`highlights the importance of`, `underscores the need for`, `is key to
understanding`, `cannot be overstated`, `has revolutionized the way we`.

**Test:** Does the sentence report a fact, or announce that a fact matters? The
second is filler in almost every case.

**Fix:** Replace the announcement with the fact it was announcing.

**Exception:** When the importance is contested and the sentence goes on to argue
it. `X matters because Y` is a claim; `X plays a crucial role` alone is not.

---

## Part 3 — Structure (S14–S20)

These count double. A reader forgives a word; a shape repeats and becomes obvious.

### S14 — Formulaic transitions

`Furthermore`, `Moreover`, `Additionally`, `Consequently`, `Nevertheless`,
`In addition to this` used as paragraph openers, especially two or three in a row.

**Test:** Count paragraph-initial connectives. Two consecutive is a pattern.

**Fix:** See `C12`. Most can be deleted outright; the rest become `but`, `so`, or
`also`.

**Exception:** `Consequently` and `nevertheless` when the causal or concessive link
is real and the shorter word would be ambiguous.

### S15 — The rule of three

Three adjectives, three examples, three clauses, three bullets, over and over.
`fast, reliable, and secure`. `plan, build, and ship`. `It is clear, concise, and
compelling.`

The tricolon is an ancient and good figure. The tell is **exclusive** use of it:
every list in the document has exactly three items because three sounds finished.

**Test:** Count the list lengths in the document. If nearly all are three, vary
them.

**Fix:** Cut the weakest item or add the fourth real one. A list of two is fine. A
list of five is fine. A list of one is a sentence.

**Exception:** There genuinely are three. Three steps in the process, three
options, three authors. Count the world, not the sentence.

### S16 — Bolded bullet headers

```
- **Performance**: the system is faster.
- **Reliability**: the system is stable.
- **Scalability**: the system grows.
```

A bullet list where every item opens with a bolded one-word label and a colon, and
every item has the same length. This is the single most recognizable formatting tell
in model output.

**Test:** Do all items in the list share the label-colon-sentence shape and roughly
the same length?

**Fix:** If the items are parallel facts, use a table. If they are argument, use
paragraphs.

**Exception:** A genuine glossary, changelog, or reference list, where lookup by
label is the point and the reader will scan rather than read.

### S17 — Uniform paragraph length

Every paragraph running three to four sentences, every section running three
paragraphs. Human writing is lumpy: a one-sentence paragraph, then a long one, then
two medium.

**Test:** Count sentences per paragraph across the document. Low variance is a tell
even when every individual paragraph is fine.

**Fix:** Merge two paragraphs that belong together; split one where the point turns;
let a single sentence stand alone when it is the point.

**Exception:** Formats that impose uniformity: a FAQ, a numbered procedure, a
glossary. The reader expects the shape.

### S18 — The summary that repeats the body

A closing section that restates, in order, what the reader just read, adding
nothing. Related to `S12` but structural: whole sections rather than a phrase.

**Test:** Delete the section. Has the reader lost anything?

**Fix:** Delete it, or replace it with the one thing the body did not say: what to
do next.

**Exception:** Documents read out of order, where the summary is the entry point
for most readers: an abstract, an executive summary, a release note's TL;DR.

### S19 — Rhetorical question as a section opener

`So what does this actually mean for your team?` `But why does this matter?`
`What if there were a better way?`

**Test:** Count section openers that are questions the author immediately answers.

**Fix:** State the answer. The question was a drumroll.

**Exception:** One in a piece can work, especially when the question is one the
reader is actually asking. As the opener of every section it is a formula.

### S20 — Symmetric everything

Every section with the same number of subsections, every example with the same shape
(problem, solution, benefit), every comparison with exactly the same number of
points on each side.

**Test:** Map the document's outline. Is every branch the same shape?

**Fix:** Let the structure follow the material. Real material is asymmetric because
reality is.

**Exception:** Formats where symmetry is a promise to the reader: a comparison table,
a set of API endpoints documented to one template, a rubric.

---

## Part 4 — Punctuation and typography (S21–S24)

### S21 — Em dash density

Models reach for the em dash where a human would use a comma, a colon, a period, or
parentheses. The mark itself is correct English and often the best choice.

**Test:** Count em dashes per 500 words of running prose. Two or more, especially as
the only mid-sentence break in a document, reads as model output to anyone who has
looked at much of it. A single em dash is never a finding, whatever the word count:
normalizing one mark in a short text produces a number, not evidence.

**Fix:** Vary the punctuation, do not eliminate the mark. Replace some with a colon
(the second half explains the first), some with parentheses (an aside), some with a
period (two thoughts).

**Exception:** Authors whose established style runs on the dash, and genres where it
is conventional (some literary and journalistic registers). In technical
documentation, internal writing, and books the density concern is mild.

**Note for public-facing copy:** on social platforms a single em dash is now read by
many people as proof of AI authorship, fairly or not. For posts published under a
real name, prefer a comma, a colon, parentheses, or a fresh sentence.

### S22 — Emoji as structure

A leading emoji on every heading, bullet, or section (🚀 ✨ 🔑 💡 ⚡).

**Test:** Is the emoji systematic, one per structural element, rather than
occasional?

**Fix:** Remove the systematic ones. Keep any that carry meaning on their own.

**Exception:** Platforms where the convention is established and readers expect it,
such as some changelogs and chat announcements, applied consistently and sparingly.

### S23 — Bold as emphasis spray

Bold applied to several phrases per paragraph. When everything is emphasized,
nothing is.

**Test:** Count bolded spans per paragraph. More than one, in most paragraphs, is
spray.

**Fix:** Keep bold for terms a scanner must find, not for whatever felt important
mid-sentence.

**Exception:** Reference material designed for scanning, where the bolded spans are
the lookup keys and the prose around them is secondary.

### S24 — Title formula

`X: The Complete Guide to Y`. `Mastering X: A Deep Dive into Y`. `The Ultimate Guide
to X`. `X 101: Everything You Need to Know`. `Why X Matters More Than Ever`.

**Test:** Could the title be attached to any article on the topic? Then it names the
topic, not the piece.

**Fix:** Name the specific claim or the specific thing. `How we cut deploy time from
40 minutes to 6` beats `Optimizing CI/CD: A Comprehensive Guide`.

**Exception:** Reference documentation, where the title's job is to name the topic
and nothing else: `Rate limits` is the right title for the page about rate limits.

---

## What a rewrite must not do

Removing slop is not removing personality. Three failure modes to avoid:

1. **Flattening.** Stripping every figure of speech until the text is a spec sheet.
   Metaphor, rhythm, and humor are not tells.
2. **Truncating.** Cutting a real qualifier (`C18`) or a necessary caveat because it
   looked like hedging. Accuracy outranks concision.
3. **Substituting one dialect for another.** A text rewritten entirely into short
   declaratives with sentence fragments for punch has its own fingerprint. Varied is
   the goal, not terse.
