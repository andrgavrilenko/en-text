# Changelog

All notable changes to this project are documented here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and
this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-09-21

### Added

- **Three skills.** `en-text` applies light cleanup as the agent drafts; `en-check`
  runs the full corpus and returns findings; `en-score` returns a number across five
  weighted dimensions. Both commands run in a forked context and cannot write files.
- **`clarity.md`, rules C1-C22.** Sentence and paragraph mechanics: characters into
  subjects, actions into verbs, nominalizations, empty verbs, the paramedic method,
  the conditions under which a passive earns its place, old-before-new, stress
  position, topic strings, sentence length distribution, parallelism, word choice.
- **`slop.md`, rules S1-S24.** The machine dialect, organized as vocabulary, phrase
  templates, structure, and typography. Structural tells count double because a
  reader forgives an odd word long before a shape that repeats.
- **A density table instead of a banned-word list.** Tells are counted per 300 words
  and weighted for clustering before anything is reported. One flagged word never
  triggers a rewrite, which is the failure mode of every wordlist-based checker.
- **`usage.md`, rules U1-U28.** Punctuation, confusables, numbers, dates, capitals,
  inclusive wording, US versus UK, list and link mechanics. Consistency outranks
  correctness for anything genuinely optional.
- **`scoring.md`.** Five dimensions with anchor tables and genre-dependent weights,
  built so the same text scores within about 0.3 of itself on a re-run.
- **Named failure modes for rewrites.** Flattening, truncating a real qualifier, and
  substituting one recognizable dialect for another are called out as errors, so an
  edit cannot succeed by making prose bland.
