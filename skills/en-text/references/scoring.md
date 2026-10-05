# Scoring — how a number is derived

Used by `en-score`, and by `en-check` when a request also asks for a number. Every
sub-score below comes from a count, so that the same text scored twice gets close to
the same number.

How close, as measured on 2026-09-26 with the previous version of this file: six runs
on each of five test texts. For three texts the six totals spread over 0.3 to 0.5
points. For a slop-heavy post they spread over 0.9, and for a middling memo in the
Official Style over 1.4. During the final checks of this version, on 2026-09-27, the
slop-heavy post scored 4.8 and 4.7, and three runs on the memo gave 6.9, 7.7 and 8.0:
the runs agreed on what was wrong and differed on how many instances a dense sentence
holds. Read a single score as ±0.5, and a middling text's score as less certain than
that.

## Procedure

1. **Settle the frame.** Before counting, fix what the number depends on and state it
   in one line above the score: the genre and the weight profile it selects, the
   spelling variant (`U28`), the house style if the project has one (`M3`), whether
   the text is the source or a rendering of it (`M2`), and the words of running prose.
   Running prose excludes code, tables, quoted material, and front matter.
2. **Count** each dimension as its section below says. An instance is a span that a
   rule's test catches and its exception does not clear, so read the exception every
   time. Quoted material and a character's dialogue, direct or reported, are other
   people's words and produce no instances. Two more things are never instances,
   because `en-check` drops them and a score counts only what a review would
   report: a pattern that is part of the writer's voice and costs the reader
   nothing, and a span whose only fix would change what it claims.
3. **Convert** each count to a sub-score with the dimension's table.
4. **Combine.** Multiply each sub-score by its weight, add the five products, and
   round half up to one decimal. Work the sum out before printing: the total must
   follow from the five numbers shown.
5. **Name the findings** that cost at least half a point (see Reporting format).

## The five dimensions

| # | Dimension | Rules |
|---|---|---|
| 1 | Sentence clarity | `C1`–`C7`, `C14`–`C18` |
| 2 | Flow and cohesion | `C8`–`C13` |
| 3 | Human voice | `S1`–`S24` |
| 4 | Correctness | `U1`–`U28` |
| 5 | Precision for the reader | `C19`–`C23` |

**One defect, one count.** Some phrases sit on lists in two files. When two rules
flag the same words, count them once, under the S rule if one of them is an S rule:
`utilize` is an `S1` tell and not also a `C19` instance, and `at the end of the day`
is one tell whether it is read as `S4`, `S12`, or `U17`. For the same reason `S2`,
`S6`, and `S13` count in Human voice only. When the rules flag different spans, even
one inside the other, each keeps its own instance: `incredibly` inside `we're
incredibly excited to announce` is an `S3` tell, and the phrase around it is a `C17`
instance. So is `empower` inside an empty claim: replacing the word does not make
the claim checkable, so the word is a tell and the claim is judged under Precision.
Within Human voice, `slop.md` decides how nested tells count. Broken parallelism is
`C13` and counts in Flow, never in Correctness.

## Weights

Each profile sums to 1.0. Pick the profile the genre matches and name it in the frame
line. A genre that matches no row takes `default`; never make up weights.

| Profile | Clarity | Flow | Voice | Correctness | Precision |
|---|---|---|---|---|---|
| default | 0.25 | 0.20 | 0.25 | 0.15 | 0.15 |
| reference-docs | 0.25 | 0.20 | 0.15 | 0.25 | 0.15 |
| marketing | 0.25 | 0.15 | 0.35 | 0.10 | 0.15 |
| academic-legal | 0.25 | 0.15 | 0.10 | 0.25 | 0.25 |

`reference-docs` covers API references, manuals, runbooks. `marketing` covers
landing pages, product updates, social posts, sales email. `academic-legal` covers
papers, contracts, policy. Everything else, including business email, blog posts,
and internal memos, is `default`.

## From a count to a sub-score

Sentence clarity, Flow, Human voice, and Correctness count instances. Each turns its
count into a rate per 300 words of running prose (count × 300 ÷ words), rounded to
one decimal. Below 150 words the raw count stands in for the rate: this is the floor
that `slop.md` sets for tells, applied to all four, because in a few sentences a rate
would turn a single instance into a pattern. Precision works from a share of claims
instead (section 5).

Each table row pairs a range of rates, from `low` up to but not including `high`,
with a range of scores, from `top` down to `bottom`. Find the row that holds the
rate. Its lowest rate takes the row's top score, and the score falls in equal steps
toward the row's bottom score as the rate nears the next row:

    score = top − (top − bottom) × (rate − low) ÷ (high − low)

Round the result to one decimal. In the last row, `high` is the rate at which the
score reaches 0.0; any higher rate also scores 0.0.

Worked through: 11 clarity instances in 540 words are 6.1 per 300. The row "6 to
under 12" runs from 6.9 down to 5.0, so the sub-score is 6.9 − 1.9 × 0.1 ÷ 6 = 6.87,
printed as 6.9.

Every row also says what a reader meets at that level. When the description plainly
does not fit the text, recount; do not move the number to match the words. A
sub-score of 10.0 means the corpus found nothing in that dimension that costs the
reader.

## 1. Sentence clarity

Count one instance for each of these:

- an actor kept out of the subject slot (`C1`)
- an action frozen in a noun (`C2`, `C3`), once per noun whichever of the two names
  it; an empty verb and the noun it carries are one `C4` instance
- a chain of three or more prepositions (`C5`)
- a passive that hides an actor the reader needs (`C6`)
- a sentence whose first seven or eight words are wind-up (`C7`)
- a sentence over 35 words that makes the reader hold more than two clauses at once
  before the main verb, or a run of short sentences that hammers (`C14`)
- a subject held far from its verb (`C15`)
- a subordinate clause of more than about ten words before the main clause (`C16`),
  unless it carries old information and is the only one in its paragraph
- a phrase about the text rather than its subject (`C17`)
- a hedge that is social padding (`C18`)

Where these rules meet in one sentence, count the rewrites, not the rules. When the
subject slot holds a nominalization and the actor sits in a by-phrase or nowhere,
putting the actor in the subject also thaws that noun and any empty verb carrying
it: that is one `C1` instance, and the noun is not counted again under `C2`, `C3`,
or `C4`. `A review of the logs was carried out by the on-call engineer` is one
instance, because `The on-call engineer reviewed the logs` fixes all of it. The
merge takes only the subject noun and the verb carrying it. After it, list every
other noun in the sentence that hides an action: each needs a rewrite of its own
and counts on its own. So does any other rule the sentence breaks, such as a
wind-up opening (`C7`), a subject held far from its verb (`C15`), or a passive that
hides a second actor (`C6`).

| Instances per 300 words | Score | What the reader meets |
|---|---|---|
| under 3 | 10.0 to 9.0 | Every sentence opens on its actor; nothing needs a second reading. |
| 3 to under 6 | 8.9 to 7.0 | An occasional heavy sentence, none that needs rereading. |
| 6 to under 12 | 6.9 to 5.0 | A sentence or two per page needs a second reading. |
| 12 to under 21 | 4.9 to 3.0 | Actors routinely hidden; several sentences must be parsed twice. |
| 21 or more | 2.9 to 0.0 (0.0 at 30 or more) | Official Style throughout; the meaning has to be reconstructed. |

A text rewritten into short declaratives and fragments, the third failure mode listed
at the end of `slop.md`, is counted here: each run of short sentences that hammers is
one `C14` instance.

## 2. Flow and cohesion

Count one instance for each of these:

- a sentence that opens on new material when known material was available (`C8`)
- a sentence whose last words hold a qualifier or an administrative detail instead
  of its point (`C9`)
- a paragraph whose topic string wanders (`C10`), and a paragraph whose point arrives
  late or never (`C11`), once per paragraph for each rule
- a connective that marks no relation (`C12`), unless `S14` already counts it
- a series or pair whose items break form (`C13`)

| Instances per 300 words | Score | What the reader meets |
|---|---|---|
| under 1 | 10.0 to 9.0 | Each paragraph opens on known ground and keeps one topic. |
| 1 to under 3 | 8.9 to 7.0 | A paragraph wanders, or emphasis lands on a qualifier now and then. |
| 3 to under 6 | 6.9 to 5.0 | Several paragraphs read as facts in no particular order. |
| 6 to under 10 | 4.9 to 3.0 | The subject changes in nearly every sentence; the reader assembles the argument. |
| 10 or more | 2.9 to 0.0 (0.0 at 15 or more) | No detectable order; paragraph breaks fall anywhere. |

## 3. Human voice

A tell is an occurrence, not a rule. Count one tell for each of these:

- each listed word or phrase, every time it occurs: `leverage`, `unlock`, `empower`,
  and `navigating` in one text are four `S1` tells, not one
- each occurrence of any other rule's shape, such as a self-answered question or a
  bolded-label list
- each pattern that exists only across the whole document (`S15`, `S17`, `S20`,
  `S22`, `S23`), once for the document
- `S21`, once for the document, when its own threshold is met

Then weight and read the count as "How to use this file" in `slop.md` says: `S14`–`S20`
count double, one fix that removes two tells counts once, and the 150-word floor
holds. Before converting, check the list of document-level rules: a missed `S15` costs
two tells. The rate is the density from `slop.md`, and the rows are its bands.
Clusters decide what to show first and never change the count.

| Density in `slop.md` | Score |
|---|---|
| under 2 (Human) | 10.0, less 0.5 for each tell that does damage on its own; never below 9.0 |
| 2 to under 5 (Suspicious) | 8.9 to 7.0 |
| 5 to under 10 (Reads as AI) | 6.9 to 4.0 |
| 10 or more (Unmistakable) | 3.9 to 0.0 (0.0 at 15 or more) |

A text that `slop.md` reads as Human although its count reaches 2 (one or two tells
under the floor, or a single tell at any length) scores in the Human row. In that row
the count alone never lowers the score, because `slop.md` leaves a tell in the Human
band alone unless it does damage on its own.

## 4. Correctness

Count two kinds of instance:

- **Errors**, one per occurrence: a usage rule broken outright, such as a comma
  splice (`U2`), an apostrophe in a plural (`U6`), a confused pair (`U14`), a hyphen
  where a range needs an en dash (`U5`), a sentence that opens on a numeral (`U19`),
  a redundant pair (`U16`), a cliché (`U17`).
- **Mixes**, one per convention the document fails to hold, however many words break
  it: the spelling variant, the serial comma, heading case, list punctuation, dash
  style, number style. Collect every instance before calling a mix (`M4`); a single
  instance cannot be a mix, so one dash is consistent with itself. The page title
  belongs to the same heading system as the other headings (`U23`).

A house style (`M3`) decides what counts, and what it permits is not an instance. Say
which style you assumed. How many em dashes a text uses is `S21`, in Human voice; a
dash that is the wrong mark for its job is `U5`, counted here.

| Errors and mixes per 300 words | Score | What the reader meets |
|---|---|---|
| under 1 | 10.0 to 9.0 | No errors, or one in a long text; every convention held. |
| 1 to under 3 | 8.9 to 7.0 | An error or a mixed convention that a careful reader notices. |
| 3 to under 6 | 6.9 to 5.0 | Errors in several paragraphs, or several conventions left unsettled. |
| 6 to under 10 | 4.9 to 3.0 | Errors in most paragraphs; conventions unstable. |
| 10 or more | 2.9 to 0.0 (0.0 at 15 or more) | Errors dense enough to distract from the content. |

## 5. Precision for the reader

Precision judges the claims. A claim is a sentence, or a list item, that asserts
something about the world: what a product does, what happened, what is true.
Instructions, questions, and headings are not claims.

Count the claims, then the empty ones. An empty claim fails the `C20` test (the reader
cannot see, count, or do what it says) and could stand unchanged in any text about
the same kind of product, team, or situation. A claim made of nothing but an `S2`,
`S6`, or `S13` phrase is empty here, while the phrase itself counts once, as a tell,
in Human voice. The `C20` exception holds: an abstraction that is the subject under
discussion, or a figure the text says it cannot give, does not make a claim empty.
Nor does a summary claim that the text backs with specifics just before or just
after it: judge the claim together with the evidence the text gives for it.

Precision starts from the share of empty claims, as a whole percentage:

| Empty claims | Score | What the reader meets |
|---|---|---|
| under 10% | 10.0 to 9.0 | Claims come with numbers, names, and mechanisms. |
| 10% to under 25% | 8.9 to 7.0 | Mostly concrete; a claim or two asserts importance without evidence. |
| 25% to under 50% | 6.9 to 5.0 | A third or more of the claims could appear in any text on the topic. |
| 50% to under 75% | 4.9 to 3.0 | Half the claims or more could appear in any text on the topic. |
| 75% or more | 2.9 to 0.0 (0.0 at 100%) | Nothing survives the question "what, specifically?" |

Then subtract, stopping at 0.0:

- 2.0 for each fact the document states with two values (`C23`): a count, amount,
  date, limit, or offer. A reader who acts on the wrong value pays for it.
- 0.5 for each thing the document calls by two or more names (`C22`).
- 0.2 for each needless long word (`C19`) and each intensifier (`C21`) that no S rule
  already counts.

In a rendering, a count or pairing read from a flattened table is something to verify
in the source (`M2`, and the exception to `C23`); it is not subtracted.

## Reporting format

A report has these parts, in this order:

1. The frame line: `Reviewed as:` the genre, the spelling variant, the house style,
   source or rendering, `<profile> weights`, then the word count. When part of the
   text was left out of the score, the frame line says what.
2. The score: `Score: X.X / 10`.
3. The five sub-scores. Each has a bar of ten cells, one filled per whole point, and
   the count it came from.
4. The findings, or the line `No finding costs half a point.`
5. Optionally, the gain line.

**Which findings to name.** A finding is one rule with all its instances. Name it only
if fixing every instance would raise its dimension's sub-score by at least 0.5:
recount without those instances, convert again, and compare. When no single rule in
a dimension qualifies, but fixing all of that dimension's instances would raise its
sub-score by 0.5 or more, those instances form one finding instead: list its rules
with their counts. This covers a count far past the end of its table, such as a
dense slop post whose Human voice stays at 0.0 whichever single rule is fixed, and
points spread thinly over many rules. Name at most three findings, ordered by what
the fix adds to the total (the sub-score gain times the dimension's weight), largest
first. Each finding gives the rule ID, what and where, and the
sub-score before and after the fix. Never name something a rule's exception clears,
and never name anything in quoted material or in dialogue. When no finding qualifies,
print `No finding costs half a point.` and name none.

**The gain line** shows what fixing the named findings would do to the total, for
example `Fixing these three: 7.6 → 8.8.` Work it out by recounting with every
instance of the named findings removed. Leave it out when nothing is named.

`en-score` shows a full report with findings. A text with nothing worth naming
reports like this:

```
Reviewed as: README section for a command-line tool, US spelling, no house style found, source text, reference-docs weights. 470 words.

Score: 9.8 / 10

  Sentence clarity     9.6   █████████░   2 instances, 1.3 per 300
  Flow and cohesion   10.0   ██████████   none
  Human voice         10.0   ██████████   1 tell, 0.6 per 300: Human
  Correctness         10.0   ██████████   none
  Precision            9.4   █████████░   1 of 26 claims empty; one C21 word, −0.2

No finding costs half a point.
```

Check the arithmetic before printing: 9.6 × 0.25 + 10.0 × 0.20 + 10.0 × 0.15 +
10.0 × 0.25 + 9.4 × 0.15 = 9.81, reported as 9.8. No fix here reaches half a point:
the empty claim is worth 0.4 of Precision, the `C21` word 0.2, and either clarity
instance 0.2.

## Honesty rules

- **Count, and do not grade on a curve.** The tables set the number, not a view of
  the writer. A text you like can score 6.
- **A 10 means the corpus found nothing that costs the reader.** Nines are rare in
  real texts, because few texts count that clean; that is an observation about texts,
  not a cap. Never hold a score down to look strict, and never invent a finding to
  justify a lower one.
- **Never report a number without its reasons:** the findings that cost at least half
  a point, or the line saying that none does.
- **Do not reward length, vocabulary, or formatting effort.** A 90-word answer that
  lands can score 10.
- **Say what you assumed.** Genre, weights, spelling variant, house style, and source
  or rendering all change the number; they go in the frame line.
- **Score the copy in hand.** A rendering, such as a fetched or flattened page
  (`M2`), still gets a number. Name the artifact in the frame line, mark Flow and any
  sub-score whose count depends on layout as provisional, and leave out what the
  rendering may have lost, such as a price filled in at runtime. Never decline to
  score it.
- **Never edit the file.** `en-score` reports; fixes come from `en-check`.
