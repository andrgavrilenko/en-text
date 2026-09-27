# A worked example

A product update of the kind a model writes from a one-line brief: 117 words of
running prose. Below are the review `en-check` gives it, the score `en-score` gives
it, the author's revision, and the revision's score. Every number follows from a
count, through the tables in `scoring.md`.

## Before

> In today's fast-paced development landscape, shipping reliable software has never
> been more crucial. That's why we're incredibly excited to announce our most
> comprehensive release yet.
>
> - **Performance**: We've leveraged a new caching layer to deliver lightning-fast
>   response times.
> - **Reliability**: Our robust retry logic ensures seamless recovery from
>   transient failures.
> - **Scalability**: The system now effortlessly handles significantly higher loads.
>
> Whether you're a solo developer or scaling a large team, these improvements will
> empower you to focus on what truly matters: building great products. The
> implementation of these changes was completed by our engineering team over the
> past quarter, and the results speak for themselves.
>
> In conclusion, this release underscores our unwavering commitment to developer
> experience. The possibilities are endless.

## The review

```
Reviewed as: product update for developers, US spelling, no house style found, source text. 117 words.

SENTENCE LEVEL
  [C1]  "The implementation of these changes was completed by our engineering team"
        → "Our engineering team implemented these changes"
        The actor sits in a by-phrase, and the action is frozen in "implementation".

  [C17] "That's why we're incredibly excited to announce"
        → Cut the phrase and open on the release: "This release adds a new caching layer ..."
        The phrase is about the announcement and says nothing about the release.

  [C20] "deliver lightning-fast response times", "handles significantly higher loads"
        → Ask the author for the figures: response time before and after, and the load the system now handles.
        These are the two claims a reader could check, and neither gives a number.

READS AS AI  (18 weighted tells in 117 words; under the 150-word floor, read raw: Unmistakable)
  [S7]  "In today's fast-paced development landscape, shipping reliable software has never been more crucial."
        → Delete the sentence.
        Scenery: it makes no claim a reader could dispute.

  [S16] The three bullets
        → Write each change as a sentence of prose.
        Each bullet opens with a bolded one-word label and a colon, and all three share one shape.

  [S11] "Whether you're a solo developer or scaling a large team"
        → Cut the clause.
        It addresses a range of readers instead of the one this update is for.

  [S13] "underscores our unwavering commitment to developer experience", "the results speak for themselves"
        → Cut both, and report the results once the author supplies them.
        Each announces that something matters without saying what happened.

  [S12] "In conclusion", "The possibilities are endless."
        → End on the sentence about the engineering team.
        The closing paragraph adds nothing the body has not said.

  [S1]  "comprehensive", "leveraged", "robust", "seamless", "empower"
        → Cut each; where a word stood in for a fact, such as what the retry logic survives, ask the author for it.
        Five model-favored words in 117 words.

  [S3]  "incredibly", "effortlessly", "significantly", "truly"
        → Delete all four.
        Each adds emphasis and no information.

  [S5]  "lightning-fast"
        → The measured response time, once the author gives it (C20).
        A modifier that cannot be checked stands where a number belongs.

  Proposed rewrite:
    This release adds a new caching layer that cuts response times from
    [old figure] to [new figure]. Our retry logic recovers from transient
    failures, and the system now handles [new load] instead of [old load].
    Our engineering team implemented these changes over the past quarter.
  It removes every tell above and clears C1 and C17. The bracketed gaps are the
  author's to fill (C20).

Does well: no usage errors; the grammar and punctuation are clean throughout.
```

## The score

```
Reviewed as: product update for developers, US spelling, no house style found, source text, marketing weights. 117 words.

Score: 5.2 / 10

  Sentence clarity     9.3   █████████░   2 instances (raw count, under 150 words)
  Flow and cohesion   10.0   ██████████   none
  Human voice          0.0   ░░░░░░░░░░   18 weighted tells: Unmistakable
  Correctness         10.0   ██████████   none
  Precision            2.6   ██░░░░░░░░   7 of 9 claims empty

Costing the most:
  [C20] Seven of the nine claims give the reader nothing to check, from the
        opening sentence to "The possibilities are endless."
        Precision 2.6 → 10.0.
  [S1]  Five model-favored words: "comprehensive", "leveraged", "robust",
        "seamless", "empower".
        Human voice 0.0 → 1.6.
  [S3]  Four intensifiers: "incredibly", "effortlessly", "significantly", "truly".
        Human voice 0.0 → 0.8.
```

At 117 words the text is under the 150-word floor, so each raw count stands in for
its rate per 300 words. The counts:

- **Human voice: 18 weighted tells, 0.0.** They are the READS AS AI findings: one
  `S7`, two for the `S16` list because structural tells count double, one `S11`, two
  `S13`, two `S12`, five `S1`, four `S3`, and one `S5`. A tell inside another tell
  counts once, so "landscape" (`S2`) and "crucial" (`S1`) belong to the `S7`
  sentence, "endless" (`S6`) to the `S12` line, and "underscores" and "unwavering"
  (`S1`) to the `S13` phrase. `S15` does not fire: the bullets are the only list,
  and one triad is not a pattern. The table reaches 0.0 at 15.
- **Sentence clarity: 2 instances, 9.3.** `C1` and `C17`. The opening sentence is
  also a `C7` wind-up, and the `S11` clause also breaks a pair (`C13`). Deleting the
  sentence or the clause clears both rules at once, so each counts once, under its S
  rule. Deleting "incredibly" leaves the `C17` phrase in place, so that phrase and
  the `S3` word each count. A rate of 2.0 sits in the first row, which runs from 10.0
  at 0 to 9.0 at 3: 10.0 − 1.0 × 2 ÷ 3 = 9.3.
- **Flow and cohesion, and Correctness: nothing counts, 10.0 each.** "That's why" is
  part of the `C17` phrase. Nothing in the text is ungrammatical.
- **Precision: 7 of 9 claims empty, 2.6.** The empty ones are the opening sentence,
  "our most comprehensive release yet", the retry and load bullets, and the three
  sentences of reader address and closing. The caching bullet names a mechanism, and
  the sentence about the engineering team says who and when. 78% sits in the last
  row, which runs from 2.9 at 75% to 0.0 at 100%: 2.9 − 2.9 × 3 ÷ 25 = 2.6.

With marketing weights (0.25 / 0.15 / 0.35 / 0.10 / 0.15):
9.3 × 0.25 + 10.0 × 0.15 + 0.0 × 0.35 + 10.0 × 0.10 + 2.6 × 0.15 = 5.215, reported
as 5.2.

A text can be clear and error-free and still tell the reader nothing. In the score,
that shows as two numbers: Human voice and Precision.

The findings are the three that add the most to the total. Concrete claims, or no
empty ones, would lift Precision to 10.0 and the total by 1.1. Without the five `S1`
words the voice count falls to 13, a sub-score of 1.6; without the four `S3` words,
to 14 and 0.8. `S16` is the most visible tell and is not named: without its two
tells the count is still 16, and Human voice stays at 0.0 until the count drops
below 15. `C1` and `C17` together would lift clarity from 9.3 to 10.0, which makes
them one finding under the half-point rule, but a smaller one than the three shown.

## After

The author's revision. Its figures are the author's: the review marked where they
were missing and asked for them.

> This release is mostly about latency.
>
> The improvement comes from a new caching layer in front of the database. On our
> read-heavy benchmark, P95 response time dropped from 840 ms to 120 ms.
>
> The release also changes how retries work: the old logic retried at once and kept
> hammering a struggling service, which is how one transient failure became the
> outage on August 3. Retries now back off exponentially.
>
> We load-tested this release to 12,000 requests per second, up from 4,000. Past
> that we have not looked, so if you run heavier loads, open an issue and tell us
> what breaks.
>
> Our engineering team implemented these changes over the past quarter. The full
> diff is in the changelog.

118 words against 117, and every claim in it can be checked. Note what the revision
did not do: it kept an honest hedge ("we have not looked"), set a 31-word sentence
next to a 5-word one, and did not chop the rest into fragments, which would only
trade one dialect for another (`slop.md`, "What a rewrite must not do").

```
Reviewed as: product update for developers, US spelling, no house style found, source text, marketing weights. 118 words.

Score: 10.0 / 10

  Sentence clarity    10.0   ██████████   none
  Flow and cohesion   10.0   ██████████   none
  Human voice         10.0   ██████████   none: Human
  Correctness         10.0   ██████████   none
  Precision           10.0   ██████████   0 of 9 claims empty

No finding costs half a point.
```

Every count is zero. "This release is mostly about latency" is a summary claim, and
the sentences after it back it with figures, so it is not empty (the exception to
`C20`). With every sub-score at 10.0, the same weights give 10.0. A 10 says only
that the counts found nothing the reader pays for. It comes easier to a short text
revised with the rules at hand than to most real ones, which is why real texts
rarely get one.
