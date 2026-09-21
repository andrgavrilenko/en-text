# A worked example

A product update, 148 words, of the kind a model produces from a one-line brief.

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

## Findings

```
Reviewed as: product update, US spelling, no house style, marketing weights. 148 words.

READS AS AI  (23 weighted tells in 148 words, 47 per 300: unmistakable)
  [S7]  "In today's fast-paced development landscape" — scene-setting opener.
        → Delete the sentence. The update starts at the caching layer.
  [S16] Three bullets, each a bolded label plus one line, all the same length.
        → These are three facts about one release. Write them as two sentences.
  [S15] Exactly three bullets, and three adjectives inside them.
  [S11] "Whether you're a solo developer or scaling a large team."
        → Name the one reader. A solo developer does not care about team scaling.
  [S12] "In conclusion" plus "The possibilities are endless."
        → Delete the whole closing paragraph.
  [S1]  leveraged, robust, seamless, comprehensive, empower, unwavering,
        crucial, underscores.
  [S3]  incredibly, effortlessly, significantly, truly.
  [S5]  "lightning-fast response times" — modifier in place of a number.
  [S13] "underscores our unwavering commitment", "the results speak for themselves"
        — announce that a fact matters instead of reporting one.

SENTENCE LEVEL
  [C1]  "The implementation of these changes was completed by our engineering team"
        → "Our engineering team shipped these changes"
        The actor is in a by-phrase; the action is frozen in "implementation".
  [C20] "lightning-fast response times", "significantly higher loads"
        → Give the numbers. This is the whole content of the update.
  [C17] "That's why we're incredibly excited to announce" — metadiscourse.

Score: 2.8 / 10
  Sentence clarity 4.0 | Flow 3.5 | Human voice 0.5 | Correctness 9.0 | Precision 1.0
```

The count: 13 vocabulary and intensifier tells, 6 phrase-level tells, and 2
structural rules (S15, S16) that count double, for 23. Correctness scores 9.0
because nothing here is ungrammatical. That is the point: a text can be error-free
and still tell the reader nothing.

The arithmetic, with marketing weights (0.25 / 0.15 / 0.35 / 0.10 / 0.15):
4.0 × 0.25 + 3.5 × 0.15 + 0.5 × 0.35 + 9.0 × 0.10 + 1.0 × 0.15 = 2.75, reported
as 2.8.

## After

> This release is mostly about latency.
>
> A caching layer now sits in front of the database. P95 response time dropped from
> 840 ms to 120 ms on our benchmark, and the effect is largest on read-heavy
> workloads. Retries also changed: transient failures now back off exponentially
> instead of hammering a struggling service, which is what caused the outage on
> 3 August.
>
> We tested to 12,000 requests per second, up from 4,000. Past that we have not
> looked, so if you are running heavier than that, tell us what breaks.
>
> Our team shipped this over the last quarter. The full diff is in the changelog.

97 words instead of 148, and every claim is now checkable. Note what the rewrite did
**not** do: it kept a hedge ("we have not looked"), kept a long sentence next to a
short one, and did not chop everything into punchy fragments. Flattening is its own
failure mode.

```
Score: 8.5 / 10
  Sentence clarity 8.5 | Flow 8.0 | Human voice 9.0 | Correctness 9.0 | Precision 7.5
```

Same weights: 8.5 × 0.25 + 8.0 × 0.15 + 9.0 × 0.35 + 9.0 × 0.10 + 7.5 × 0.15 = 8.45,
reported as 8.5. Precision stays at 7.5 because "largest on read-heavy workloads" is
still vague, and "tell us what breaks" gives no channel. Eights are good. Nines are
rare.
