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
Reviewed as: product update, US spelling, no house style. 148 words.

READS AS AI  (19 tells in 148 words — unmistakable)
  [S7]  "In today's fast-paced development landscape" — scene-setting opener.
        → Delete the sentence. The update starts at the caching layer.
  [S16] Three bullets, each a bolded label plus one line, all the same length.
        → These are three facts about one release. Write them as two sentences.
  [S15] Exactly three bullets, and three adjectives inside them.
  [S11] "Whether you're a solo developer or scaling a large team."
        → Name the one reader. A solo developer does not care about team scaling.
  [S12] "In conclusion" plus "The possibilities are endless."
        → Delete the whole closing paragraph.
  [S1]  leveraged, lightning-fast, robust, seamless, comprehensive, empower,
        unwavering, effortlessly, significantly, crucial, truly.
  [S13] "underscores our unwavering commitment" — announces that a fact matters
        instead of reporting one.

SENTENCE LEVEL
  [C1]  "The implementation of these changes was completed by our engineering team"
        → "Our engineering team shipped these changes"
        The actor is in a by-phrase; the action is frozen in "implementation".
  [C20] "lightning-fast response times", "significantly higher loads"
        → Give the numbers. This is the whole content of the update.
  [C17] "That's why we're incredibly excited to announce" — metadiscourse.

Score: 2.1 / 10
  Sentence clarity 4.0 | Flow 3.5 | Human voice 0.5 | Correctness 8.0 | Precision 1.0
```

Correctness scores 8.0 because nothing here is ungrammatical. That is the point: a
text can be error-free and still tell the reader nothing.

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
Score: 8.2 / 10
  Sentence clarity 8.5 | Flow 8.0 | Human voice 9.0 | Correctness 8.5 | Precision 7.5
```

Precision stays at 7.5 because "largest on read-heavy workloads" is still vague, and
"tell us what breaks" gives no channel. Eights are good. Nines are rare.
