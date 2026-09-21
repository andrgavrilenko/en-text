# Slop — the machine dialect

Rules `S1`–`S24`. These catch the patterns that make a text read as machine-made.

## How to use this file

**Nothing here is an error in itself.** Every item below appears in good human
writing. What marks text as model output is density and evenness: many tells, spread
uniformly, with no stretch of plain sentences between them.

Count first. Per 300 words of running prose:

| Tells found | Read as | Action |
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
voice includes the pattern.

---

## Part 1 — Words (S1–S6)

### S1 — Core banned verbs and adjectives

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

**Fix:** the plain word. `leverage` → `use`. `utilize` → `use`. `facilitate` →
`help` or `run`. `robust` → say what it survives. `comprehensive` → say what it
covers. `seamless` → say what step disappeared.

**Exception:** the technical sense. `Leverage` in finance, `robust` in statistics,
`dynamic` in programming, `delve` in a geological paper. Judge by domain, not by
string match.

### S2 — Abstract nouns that say nothing

`landscape`, `realm`, `tapestry`, `journey`, `ecosystem`, `paradigm`, `synergy`,
`framework` (when it frames nothing), `insights`, `learnings`, `takeaways`,
`best practices`, `game-changer`, `deep dive`, `treasure trove`, `wealth of`,
`testament to`, `beacon of`, `cornerstone of`, `the fabric of`.

**Test:** replace the noun with "thing". If the sentence loses nothing, the noun was
decoration.

### S3 — The intensifier stack

`truly`, `deeply`, `incredibly`, `remarkably`, `notably`, `significantly`,
`substantially`, `fundamentally`, `undoubtedly`, `certainly`, `absolutely`,
`genuinely`, `particularly`.

One is fine. Three in a paragraph is a tic. See also `C21`.

### S4 — Corporate hedging

`arguably`, `it is worth noting that`, `it is important to remember that`,
`that said`, `at the end of the day`, `when all is said and done`, `in many ways`,
`to some extent`, `more often than not`.

Distinguish from honest hedges (`C18`). These say nothing about the evidence; they
buy time.

### S5 — Compound modifier soup

`carefully crafted`, `thoughtfully designed`, `expertly curated`, `purpose-built`,
`battle-tested`, `industry-leading`, `best-in-class`, `world-class`, `next-level`,
`rock-solid`, `lightning-fast`, `razor-sharp`, `laser-focused`.

**Fix:** replace with the fact. `lightning-fast` → `responds in 40 ms`.

### S6 — False precision about scale

`countless`, `endless`, `infinite`, `a myriad of`, `untold`, `a staggering number
of`, `exponentially` (used for any growth), `orders of magnitude` (used loosely).

**Fix:** give the number, or say you do not know it.

---

## Part 2 — Phrases and sentence templates (S7–S13)

### S7 — The scene-setting opener

`In today's fast-paced world`, `In an era of`, `In the ever-evolving landscape of`,
`Now more than ever`, `In recent years, there has been growing interest in`,
`As technology continues to advance`, `Since the dawn of`.

**Fix:** delete the sentence. The article almost always starts better at sentence
two.

### S8 — "It's not X, it's Y"

`It's not just a tool, it's a philosophy.` `This isn't about code, it's about
people.` `The question isn't whether, it's when.`

The construction has a real use: correcting an expectation the reader actually
holds. It becomes a tell when nobody made the claim being corrected, and when it
appears more than once in a piece.

**Fix:** state Y. Drop the invented X.

### S9 — The negative-parallel flourish

`Not because it is easy, but because it is hard.` `Less a X than a Y.` `Not only
does it A, it also B.`

Same test as `S8`: is the contrast real, or manufactured for cadence?

### S10 — Conversational glue

`Let's dive in`, `Let's break it down`, `Here's the thing`, `Here's the kicker`,
`But wait, there's more`, `Spoiler alert`, `Plot twist`, `The truth is`,
`Let that sink in`, `Buckle up`.

### S11 — The reader address

`Whether you're a seasoned developer or just starting out`, `If you're like most
people`, `We've all been there`, `You might be wondering`, `Sound familiar?`

The both-audiences construction (`Whether you're X or Y`) is the strongest single
tell in this file. It appears almost nowhere in edited human prose.

### S12 — Closing boilerplate

`In conclusion`, `To sum up`, `At the end of the day`, `Ultimately, the key
takeaway is`, `Only time will tell`, `The possibilities are endless`,
`One thing is clear:`, `The future of X is bright`.

**Fix:** end on the last real sentence. Most pieces improve by deleting the final
paragraph entirely.

### S13 — Hollow value statements

`plays a crucial role in`, `is a testament to`, `serves as a reminder that`,
`highlights the importance of`, `underscores the need for`, `is key to
understanding`, `cannot be overstated`, `has revolutionized the way we`.

**Test:** does the sentence report a fact, or announce that a fact matters? The
second is filler in almost every case.

---

## Part 3 — Structure (S14–S20)

These count double. A reader forgives a word; a shape repeats and becomes obvious.

### S14 — Formulaic transitions

`Furthermore`, `Moreover`, `Additionally`, `Consequently`, `Nevertheless`,
`In addition to this` used as paragraph openers, especially two or three in a row.

**Fix:** see `C12`. Most can be deleted outright; the rest become `but`, `so`, or
`also`.

### S15 — The rule of three

Three adjectives, three examples, three clauses, three bullets, over and over.
`fast, reliable, and secure`. `plan, build, and ship`. `It is clear, concise, and
compelling.`

The tricolon is an ancient and good figure. The tell is **exclusive** use of it:
every list in the document has exactly three items because three sounds finished.

**Test:** count the list lengths in the document. If nearly all are three, vary
them. A list of two is fine. A list of five is fine. A list of one is a sentence.

### S16 — Bolded bullet headers

```
- **Performance**: the system is faster.
- **Reliability**: the system is stable.
- **Scalability**: the system grows.
```

A bullet list where every item opens with a bolded one-word label and a colon, and
every item has the same length. This is the single most recognizable formatting tell
in model output.

**Fix:** if the items are parallel facts, use a table. If they are argument, use
paragraphs. Keep the bolded-label form only for a genuine glossary or reference
list, where lookup is the point.

### S17 — Uniform paragraph length

Every paragraph running three to four sentences, every section running three
paragraphs. Human writing is lumpy: a one-sentence paragraph, then a long one, then
two medium.

**Test:** count sentences per paragraph across the document. Low variance is a tell
even when every individual paragraph is fine.

### S18 — The summary that repeats the body

A closing section that restates, in order, what the reader just read, adding
nothing. Related to `S12` but structural: whole sections rather than a phrase.

### S19 — Rhetorical question as a section opener

`So what does this actually mean for your team?` `But why does this matter?`
`What if there were a better way?`

One in a piece can work. As the opener of every section it is a formula.

### S20 — Symmetric everything

Every section with the same number of subsections, every example with the same shape
(problem, solution, benefit), every comparison with exactly the same number of
points on each side. Real material is asymmetric because reality is.

---

## Part 4 — Punctuation and typography (S21–S24)

### S21 — Em dash density

Models reach for the em dash where a human would use a comma, a colon, a period, or
parentheses. The mark itself is correct English and often the best choice.

**Test:** count em dashes per 500 words. Two or more, especially as the only
mid-sentence break in a document, reads as model output to anyone who has looked at
much of it.

**Fix:** vary the punctuation, do not eliminate the mark. Replace some with a colon
(the second half explains the first), some with parentheses (an aside), some with a
period (two thoughts).

**Note for public-facing copy:** on social platforms a single em dash is now read by
many people as proof of AI authorship, fairly or not. For posts published under a
real name, prefer a comma, a colon, parentheses, or a fresh sentence. In technical
documentation, internal writing, and books this concern does not apply.

### S22 — Emoji as structure

A leading emoji on every heading, bullet, or section (🚀 ✨ 🔑 💡 ⚡). Occasional
emoji in informal writing is human. One per heading, systematically, is not.

### S23 — Bold as emphasis spray

Bold applied to several phrases per paragraph. When everything is emphasized,
nothing is. Keep bold for terms a scanner must find, not for whatever felt
important mid-sentence.

### S24 — Title formula

`X: The Complete Guide to Y`. `Mastering X: A Deep Dive into Y`. `The Ultimate Guide
to X`. `X 101: Everything You Need to Know`. `Why X Matters More Than Ever`.

**Fix:** name the specific claim or the specific thing. `How we cut deploy time from
40 minutes to 6` beats `Optimizing CI/CD: A Comprehensive Guide`.

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
