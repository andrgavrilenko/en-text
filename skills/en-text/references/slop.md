# Slop — the machine dialect

Rules `S1`–`S24`. These catch the patterns that make a text read as machine-made.

## How to use this file

**Nothing here is an error in itself.** Every item below appears in good human
writing. What marks a text as machine-made is density: how many tells it carries for
its length. The verdict describes how a text reads and says nothing about who wrote
it. Some items are older than language models (the stock modifiers in `S5`, the
corporate nouns in `S2`), and human copy trips them too.

**Count.** Density is weighted tells × 300 ÷ words of running prose.

- Running prose excludes code, tables, quoted material and front matter.
- One tell is one occurrence that a rule's test catches: a listed word, a phrase, a
  self-answered question, a bolded-label list. A pattern that exists only across the
  whole document (`S15`, `S17`, `S20`, `S22`, `S23`) is one tell for the document.
  When one fix would remove two tells at once (an `S2` noun inside an `S7` opener,
  an `S1` verb inside an `S13` statement), count one.
- A listed item counts in any form: inflected or derived (`leveraging`,
  `game-changing`), in British spelling (`utilise`), with or without its hyphen
  (`ever evolving`).
- The structural tells `S14`–`S20` count double. A reader forgives an odd word much
  sooner than a shape that repeats.
- Density is always per 300 words. `S21` is the one rule with a threshold of its
  own, counted per 500 words; when that threshold is met, `S21` adds one tell to the
  count, once per document.

**Read the density.**

| Weighted tells per 300 words | Read as | Action |
|---|---|---|
| under 2 | Human | Leave it alone. Report a single tell only if it does damage on its own. |
| 2 to under 5 | Suspicious | Report the worst one or two. |
| 5 to under 10 | Reads as AI | Report all of them and propose a rewrite of the worst passages. |
| 10 or more | Unmistakable | Propose a rewrite as replacement text inside the report and list, by rule ID, what the rewrite removes. |

Every action in the table is something to report or propose. None of them is an
edit: a file changes only when the user asks for the change in so many words.

**The 150-word floor.** Below 150 words of running prose, do not normalize: read the
raw weighted count against the same bands. Normalizing a short text turns a few
tells into a large number (three in 60 words would be 15 per 300) that proves
nothing. One or two tells in a short text give no verdict, whatever their weight:
read the text as Human, and report a tell only if it does damage on its own. At
any length, a single tell never moves a text out of the Human band.

**Clusters decide what to report first.** A cluster is a paragraph, or a list, whose
own density (its weighted tells × 300 ÷ its words) is at least twice the document's.
Show clusters first, because a rewrite there removes the most. A whole-document tell
belongs to no paragraph, and a text under the floor has no clusters to find.
Clustering never multiplies the count and never moves the verdict: the verdict comes
from the whole document.

**Evenness explains a verdict and never changes one.** Tells spread through every
paragraph, with no plain stretch between them, are why a text in the middle bands
reads as machine-made although no single sentence in it is bad. Say so when it helps
the writer; the number stays as counted.

**Limits.** Never flag a tell inside quoted material, and never flag an author whose
established voice includes the pattern. Every rule below has a stated exception; the
exceptions are not optional reading.

---

## Part 1 — Words (S1–S6)

### S1 — Model-favored verbs and adjectives

These are the load-bearing vocabulary of model prose. Each is a real English word;
each is used by models far more often than by people.

`delve`, `leverage` (as a verb), `utilize`, `harness`, `showcase`, `underscore`,
`unpack` (a concept), `unlock` (potential), `elevate`, `empower`, `foster`,
`facilitate`, `navigate` (a challenge), `spearhead`, `streamline`, `bolster`,
`cultivate`, `embark`, `embrace` (change, the future), `boast` (a feature),
`resonate`, `illuminate`, `shed light on`, `amplify`, `curate`, `champion` (as a
verb), `usher in`, `pave the way`.

`robust`, `seamless`, `crucial`, `pivotal`, `vital`, `comprehensive`, `holistic`,
`nuanced`, `multifaceted`, `intricate`, `myriad`, `plethora`, `vibrant`, `dynamic`,
`innovative`, `cutting-edge`, `state-of-the-art`, `ever-evolving`, `transformative`,
`groundbreaking`, `unparalleled`, `unwavering`, `meticulous`, `profound`,
`compelling`, `invaluable`, `commendable`, `noteworthy`.

**Test:** Count occurrences across the running prose, in every form: `leveraging`,
`delving`, `harnessed` and the British `utilise` are the same tells as the words
listed. A paraphrase that does a listed word's job counts too, but only in company:
when its paragraph already holds at least two other tells from this file. There,
`dig deep into` is `delve` and `tap into` is `harness`. Alone, a paraphrase is an
ordinary word. One listed word is a word choice. Several are a fingerprint.

**Fix:** The plain word. `leverage` → `use`. `utilize` → `use`. `facilitate` →
`help` or `run`. `robust` → say what it survives. `comprehensive` → say what it
covers. `seamless` → say what step disappeared.

**Exception:** The technical or literal sense. `Leverage` in finance, `robust` in
statistics, `dynamic` in programming, `unpack` for an archive, `navigate` for a
route. Judge by domain, not by string match.

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
introduces a specific exception to a general claim. `Particularly` when it narrows a
claim to a named case: `slow, particularly on Windows`.

### S4 — Corporate hedging

`arguably`, `it is worth noting that`, `it is important to remember that`,
`that said`, `at the end of the day`, `when all is said and done`, `in many ways`,
`to some extent`.

**Test:** Does the hedge say anything about the evidence? These phrases usually do
not; they buy time. A qualifier that says how often or how surely a claim holds
(`usually`, `in most cases`, `may`) is an honest hedge under `C18`, and this rule
never touches it.

**Fix:** Delete the phrase and start the sentence on its content. If a real
qualifier was hiding inside it, keep the qualifier in plain words.

**Exception:** `That said` and `to some extent` when they introduce a real
concession that the next sentence actually delivers. `Arguably` when the claim is
contested and the text goes on to argue it. Any hedge a domain expert would defend
(`C18`).

### S5 — Compound modifier soup

`carefully crafted`, `thoughtfully designed`, `expertly curated`, `purpose-built`,
`battle-tested`, `industry-leading`, `best-in-class`, `world-class`, `next-level`,
`rock-solid`, `lightning-fast`, `razor-sharp`, `laser-focused`.

**Test:** Can the modifier be verified? `lightning-fast` cannot. `40 ms` can.

**Fix:** Replace with the fact. `lightning-fast` → `responds in 40 ms`.

**Exception:** A modifier backed by a fact in the same sentence: `battle-tested
across 400 production deployments` is a claim with evidence attached.

### S6 — Inflated scale

`countless`, `endless`, `infinite`, `a myriad of`, `untold`, `a staggering number
of`, `exponentially` (used for any growth), `orders of magnitude` (used loosely).

A false range inflates scope the same way: `from startups to enterprises` or
`from beginners to experts` stands in for everyone without naming anyone.

**Test:** Is the number known? If yes, it is being withheld. If no, the word is
pretending. For a range, ask what the text can show at each end.

**Fix:** Give the number, or say you do not know it. Replace a false range with the
cases the text can name.

**Exception:** The literal sense. `Exponentially` for growth that is actually
exponential. `Orders of magnitude` when the ratio really is a power of ten. A range
the text backs with cases at both ends: `tested on laptops from 4 GB to 64 GB`.

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
people.` `The question isn't whether, it's when.` Split across two sentences, the
move is the same tell: `It isn't a tool. It's a philosophy.` `The config file isn't
an afterthought. It's the product.`

**Test:** Look for a denial followed at once by the real claim, in one sentence or
in two (`isn't X, it's Y`; `isn't X. It's Y.`; `not about X. It's about Y.`). Then
ask: did anyone claim X? If nobody holds the expectation being corrected, the
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

### S10 — Conversational glue and chat residue

`Let's dive in`, `Let's break it down`, `Here's the thing`, `Here's the kicker`,
`Here's why:`, `Here's how:`, `But wait, there's more`, `Spoiler alert`,
`Plot twist`, `The truth is`, `Let that sink in`, `Buckle up`.

Chat residue is glue left over from the conversation that produced the text.
Openers: `Great question!`, `Certainly!`, `I'd be happy to help`,
`I hope this email finds you well`. Sign-offs: `I hope this helps`,
`Let me know if you have any questions`, `Feel free to reach out`. Unfilled template
slots: `[Your Name]`, `[Company]`.

**Test:** Delete the phrase. Nothing changes except the word count. For residue, ask
also whether the text is a message to someone. A greeting or a sign-off in an
article, a post, a README or a report is residue. An unfilled slot in a text about to
be sent is always a finding.

**Fix:** Delete it. Fill the slot or remove it.

**Exception:** A deliberately chatty register the author holds consistently, such as
a personal newsletter, where the reader has opted into the voice. A real message may
open or close politely: one courtesy line in an email or a support reply is manners.
In a message, the tell is boilerplate stacked at both ends, a stock opener and a
stock sign-off wrapped around a short body. A template meant to be filled in keeps
its slots.

### S11 — The reader address

`Whether you're a seasoned developer or just starting out`, `If you're like most
people`, `We've all been there`, `You might be wondering`, `Sound familiar?`

The both-audiences construction (`Whether you're X or Y`) is the strongest single
tell in this file. People wrote it long before language models, mostly in marketing
and course copy. It counts as strong because models produce it so often, and in
registers where it has no job to do: a runbook or an incident report has one reader.

**Test:** Does the sentence name a reader, or a range of readers? A range is the
tell.

**Fix:** Name the one reader you are writing for, or say nothing about the reader.

**Exception:** Instructions that genuinely branch on the reader's situation, where
the branch is then followed: `If you are on Windows, run X. On macOS, run Y.`

### S12 — Closing boilerplate

`In conclusion`, `To sum up`, `At the end of the day`, `Ultimately, the key
takeaway is`, `Only time will tell`, `The possibilities are endless`,
`One thing is clear:`, `The future of X is bright`. Sign-offs left over from a chat
reply (`I hope this helps`) are chat residue and belong to `S10`.

**Test:** Does the final paragraph contain anything not already said above it?

**Fix:** End on the last real sentence. Most pieces improve by deleting the final
paragraph entirely.

**Exception:** A long document with a genuine summary that a reader might jump to,
such as an executive summary or an abstract, labeled as such.

### S13 — Hollow value statements

`plays a crucial role in`, `is a testament to`, `serves as a reminder that`,
`highlights the importance of`, `underscores the need for`, `is key to
understanding`, `cannot be overstated`, `has revolutionized the way we`.

The same announcement often trails off a sentence that has already made its point,
as a participle clause: `, highlighting the importance of`,
`, underscoring the need for`, `, reflecting a broader shift toward`. And
`stands as` or `serves as` takes the place of a plain `is`: `The library stands as
proof that small teams can ship.`

**Test:** Does the sentence report a fact, or announce that a fact matters? The
second is filler in almost every case. Delete a trailing participle clause: if the
sentence still reports every fact, the clause was commentary. Put `is` back in place
of `stands as` or `serves as`: if nothing is lost, the swap was decoration.

**Fix:** Replace the announcement with the fact it was announcing. Cut a trailing
clause that only comments, and write `is` where `is` is meant.

**Exception:** When the importance is contested and the sentence goes on to argue
it. `X matters because Y` is a claim; `X plays a crucial role` alone is not. A
participle clause that adds a fact stays (`The job failed at 3 a.m., leaving the
queue full until morning`), and so does `serves as` for a stand-in (`A spare laptop
serves as the build server`).

---

## Part 3 — Structure (S14–S20)

These count double. A reader forgives a word; a shape repeats and becomes obvious.

### S14 — Formulaic transitions

`Furthermore`, `Moreover`, `Additionally`, `Consequently`, `Nevertheless`,
`In addition to this` used as paragraph openers, especially two or three in a row.

**Test:** Count paragraph-initial connectives. Two consecutive is a pattern.

**Fix:** See `C12`. Most can be deleted outright; the rest become `but`, `so`,
`also`, or `even so`, matching the relation.

**Exception:** `Consequently` and `nevertheless` when the causal or concessive link
is real and the shorter word would be ambiguous.

### S15 — The rule of three

Three adjectives, three examples, three clauses, three bullets, over and over.
`fast, reliable, and secure`. `plan, build, and ship`. `It is clear, concise, and
compelling.`

The tricolon is an ancient and good figure. The tell is **exclusive** use of it:
every list in the document has exactly three items because three sounds finished.

**Test:** Write down the length of every list and series in the document. If nearly
all are three, sort the triads. A counted triad names what the world supplied: the
three carriers a product compares, the three steps of a real flow. An invented triad
was built to reach three: three adjectives, three benefits, three abstractions. The
finding is the pattern, and it names only the invented triads.

**Fix:** Cut the weakest invented item or add the fourth real one. Leave counted
triads as they are, even in a document full of invented ones: cutting a step from a
real process makes the text wrong. A list of two is fine. A list of five is fine. A
list of one is a sentence.

**Exception:** There genuinely are three. Three steps in the process, three options,
three authors. Count the world, not the sentence. If every triad in the document is
counted, there is no finding.

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

**Test:** Write down the sentence count of every paragraph of running prose, in
order. A question or a fragment counts as a sentence; headings, list items and code
are not paragraphs. The tell is present when there are at least four paragraphs, the
longest has at most one sentence more than the shortest, and the shortest has three
sentences or more. `3 3 3 3 3 3 3` and `3 4 4 3 4` are the tell; `2 4 4 2` and
`3 2 2 2 2` are not. Low variance is a tell even when every individual paragraph is
fine.

**Fix:** Merge two paragraphs that belong together; split one where the point turns;
let a single sentence stand alone when it is the point.

**Exception:** Formats that impose uniformity and are read by lookup: a FAQ, a
numbered procedure, a glossary. The reader expects the shape. Runs of one- and
two-sentence paragraphs belong to registers of their own (social posts, news copy,
chat), which is why the test starts at three sentences.

### S18 — The summary that repeats the body

A closing section that restates, in order, what the reader just read, adding
nothing. Related to `S12` but structural: whole sections rather than a phrase.

**Test:** Delete the section. Has the reader lost anything?

**Fix:** Delete it, or replace it with the one thing the body did not say: what to
do next.

**Exception:** Documents read out of order, where the summary is the entry point
for most readers: an abstract, an executive summary, a release note's TL;DR. A
heading alone does not qualify a section: a recap at the end of a post read from the
top is the body again.

### S19 — Self-answered questions

`So what does this actually mean for your team?` `But why does this matter?`
`What if there were a better way?` These open sections. The same drumroll also runs
inside a paragraph, as a question and a clipped answer: `The result? A 40% drop.`
`The catch? It only runs on Linux.`

**Test:** Count the questions the writer answers straight away, whether they open a
section or sit inside a paragraph. A real question left for someone else to answer,
such as a request to a colleague, is not this pattern.

**Fix:** State the answer. The question was a drumroll.

**Exception:** One in a piece can work, especially when the question is one the
reader is actually asking. With two or more, every one counts: as the opener of every
section, or the beat of every paragraph, it is a formula. A FAQ is exempt: its
questions are the reader's own, set up as headings for lookup.

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
parentheses. The mark itself is correct English and often the best choice. The
pattern reads worst when the dash is the only mid-sentence break a text uses.

**Test:** Count the em dashes in the running prose. A spaced en dash doing an em
dash's job (`word – word`) counts as an em dash. An en dash in a range or a
relationship (`2019–2024`, `client–server`) never counts, and neither does a hyphen.
The threshold is two or more dashes and at least 2 per 500 words. This per-500
threshold is the only unit in the corpus besides the density's per 300. When it is
met, `S21` adds one tell to the density count, once per document, however many
dashes there are. A single em dash is never a finding and never a tell, whatever the
word count: normalizing one mark in a short text produces a number, not evidence.
The public-post note below is separate from this test.

**Fix:** Vary the punctuation; do not eliminate the mark. Replace some with a colon
(the second half explains the first), some with parentheses (an aside), some with a
period (two thoughts).

**Exception:** Authors whose established style runs on the dash, and genres where it
is conventional (some literary and journalistic registers). In technical
documentation, internal writing, and books the concern is mild: the tell still
counts, but it rarely deserves a finding of its own.

**Note for public posts:** in a post published under a real name on a public
platform, such as LinkedIn or X, every em dash gets a note, and so does every spaced
en dash doing the same job. One dash is enough. Give each a replacement (a comma, a
colon, parentheses, or a fresh sentence), and vary them. On social platforms many
readers now take a single em dash as proof of AI authorship, fairly or not. Report
the note separately from the density verdict. It never enters the count and never
changes the verdict.

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

Removing slop is not removing personality. A rewrite can fail in five ways: the first
three remove too much, the fourth removes too little, and the fifth adds what was
never there.

1. **Flattening.** Stripping every figure of speech until the text is a spec sheet.
   Metaphor, rhythm, and humor are not tells.
2. **Truncating.** Cutting a real qualifier (`C18`) or a necessary caveat because it
   looked like hedging. Accuracy outranks concision.
3. **Substituting one dialect for another.** A text rewritten entirely into short
   declaratives with sentence fragments for punch has its own fingerprint. Varied is
   the goal, not terse.
4. **Swapping synonyms.** Trading `delve` for `dig into`, or `leverage` for
   `tap into`, keeps the move and changes only the string. Rewrite the sentence
   around what it claims.
5. **Inventing.** Filling a gap with a number, a name, an example, or a cause the
   writer never supplied. A rewrite that sounds specific but states what the author
   did not is a false claim (`C20`). Leave a marked gap for the writer instead.
