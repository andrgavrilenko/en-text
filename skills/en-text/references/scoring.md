# Scoring — how a number is derived

Used by `en-score`. The point of a number is repeatability: the same text scored
twice should land within about 0.3 of itself. That requires counting before judging.

## Procedure

1. Count the words of running prose. Exclude code blocks, tables, front matter, and
   quoted material.
2. Score each of the five dimensions below from 0.0 to 10.0 using its anchors.
3. Combine with the weights.
4. Report the total to one decimal, the five sub-scores, and the three findings that
   cost the most points.

Never report a number without the findings. A score with no reasons attached is
theater.

## The five dimensions

| # | Dimension | Rules |
|---|---|---|
| 1 | Sentence clarity | `C1`–`C7`, `C14`–`C18` |
| 2 | Flow and cohesion | `C8`–`C13` |
| 3 | Human voice | `S1`–`S24` |
| 4 | Correctness | `U1`–`U28` |
| 5 | Precision for the reader | `C19`–`C22`, `S2`, `S6`, `S13` |

## Weights

Each profile sums to 1.0. Use `default` unless the genre clearly matches another
row, and name the profile you used in the line above the score.

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

---

## 1. Sentence clarity (weight 0.25)

Count per 100 words: buried subjects (`C1`), nominalized actions (`C2`, `C3`),
empty verbs (`C4`), unearned passives (`C6`), sentences over 35 words that hold the
reader waiting (`C14`), split subject and verb (`C15`), metadiscourse (`C17`).

| Score | Anchor |
|---|---|
| 9–10 | Up to 1 finding per 100 words. Every sentence opens on its actor. |
| 7–8 | 1–2 per 100. Occasional heavy sentence, nothing that needs rereading. |
| 5–6 | 2–4 per 100. The reader rereads a sentence or two per page. |
| 3–4 | 4–7 per 100. Actors routinely hidden; several sentences must be parsed twice. |
| 0–2 | Over 7 per 100. Official style throughout. Meaning has to be reconstructed. |

Where a count sits on a boundary, the surrounding prose decides: a text whose heavy
sentences are all in one paragraph scores higher than one where they are spread.

## 2. Flow and cohesion (weight 0.20)

Judge at paragraph level, not sentence level. Check old-before-new (`C8`), stress
position (`C9`), topic strings (`C10`), paragraph focus (`C11`), transitions
(`C12`), parallelism (`C13`).

| Score | Anchor |
|---|---|
| 9–10 | Topic strings coherent throughout; each paragraph opens on known ground. |
| 7–8 | One or two paragraphs wander; emphasis occasionally lands on a qualifier. |
| 5–6 | Several paragraphs are lists of facts in arbitrary order. |
| 3–4 | Subjects change every sentence; the reader assembles the argument unaided. |
| 0–2 | No detectable order. Paragraph breaks are arbitrary. |

## 3. Human voice (weight 0.25)

Use the density table in `slop.md`. Normalize first (tells × 300 ÷ words of running
prose), then convert:

| Tells per 300 words | Score |
|---|---|
| 0–1 | 9–10 |
| 2–4 | 7–8 |
| 5–9 | 4–6 |
| 10–15 | 2–3 |
| 16+ | 0–1 |

Apply the two weightings from `slop.md` before converting: clustering multiplies,
structural tells (`S14`–`S20`) count double. Then adjust by at most one point for
the failure modes at the end of `slop.md` — a text scrubbed into flat declaratives
is not a 10.

## 4. Correctness (weight 0.15)

Count outright errors (`U2` splices, `U6` apostrophes, `U14` confusions, broken
parallelism, wrong dash) separately from inconsistencies (mixed spelling variant,
mixed list punctuation, mixed heading case).

| Score | Anchor |
|---|---|
| 9–10 | No errors. Conventions held consistently throughout. |
| 7–8 | No errors; one convention drifts (for example, serial comma). |
| 5–6 | One or two real errors, or several inconsistencies. |
| 3–4 | Errors on most pages; conventions unstable. |
| 0–2 | Errors dense enough to distract from the content. |

An error the house style permits is not an error. Say which style you assumed.

## 5. Precision for the reader (weight 0.15)

Does the text give the reader something to hold? Count abstractions where a fact
belongs (`C20`), decorative nouns (`S2`), hollow value statements (`S13`), false
scale (`S6`), inconsistent terminology (`C22`).

| Score | Anchor |
|---|---|
| 9–10 | Claims are specific: numbers, names, mechanisms. Terms used consistently. |
| 7–8 | Mostly concrete; a few paragraphs assert importance without evidence. |
| 5–6 | Half the claims could describe any product in the category. |
| 3–4 | Mostly category-level statements. The reader learns little that is checkable. |
| 0–2 | Nothing survives the "so what specifically?" test. |

---

## Reporting format

```
Reviewed as: business email, US spelling, default weights. 210 words.

Score: 6.1 / 10

  Sentence clarity       5.5   ██████░░░░
  Flow and cohesion      7.0   ███████░░░
  Human voice            4.0   ████░░░░░░
  Correctness            8.5   █████████░
  Precision              7.0   ███████░░░

Costing the most:
  [S16] Every bullet opens with a bolded label and runs the same length.
  [S11] "Whether you're a founder or an engineer" addresses two audiences at once.
  [C4]  Six empty verb + nominalization pairs in 210 words.
```

Check the arithmetic before you print it: 5.5 × 0.25 + 7.0 × 0.20 + 4.0 × 0.25 +
8.5 × 0.15 + 7.0 × 0.15 = 6.1. A total that does not follow from the sub-scores is
the fastest way to lose a reader's trust in every other number.

## Honesty rules

- **Do not grade on a curve.** A competent business email is a 7. Nines are rare and
  eights are good. If everything scores 8.5, the scale has stopped measuring.
- **Do not reward length or vocabulary.** A 90-word answer that lands can score 10.
- **Say what you assumed.** Genre, weights, spelling variant, and house style all
  change the number. State them in one line before the score.
- **Never edit the file.** `en-score` reports; it does not rewrite.
