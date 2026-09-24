# Method — how to run a review

Rules `M1`–`M4`. These govern the review, not the prose. They exist because the
corpus can be right about a sentence and still produce a finding that is
misattributed, unverifiable, or not a finding at all.

Same shape as every other rule: a test, a fix, and an exception. Every rule here was
written after a real review got it wrong.

---

### M1 — Attribute a finding only with evidence

Requests often arrive as "I just changed these spans, did my changes break
anything?" The corpus can tell you what is in the text. It cannot tell you what
arrived with a particular change.

**Test:** Does the finding claim that a specific edit *introduced* the problem? If
so, can you point to a before state: a diff, a previous version, the old text quoted
in the request?

**Fix:** With a before state, verify and attribute. Without one, report what is in
the text now and label it as such: "present in the current text; I cannot tell
whether your edit introduced it."

**Exception:** The request contains both versions. Then attribution rests on
evidence and belongs in the finding.

A reviewer who confidently misattributes sends the writer hunting through their own
change for something that was always there, and the error spreads doubt onto the
findings that were correct.

There is a middle case worth handling well. The request names which spans changed,
and a pattern lines up with exactly those spans. That inference is worth stating and
it is still not evidence. Describe what you observed and let the writer draw the
conclusion: "the four you named share a shape the other two lack" beats "your
rewrite left the other two stranded." The first survives being wrong about which
spans you actually changed; the second does not.

### M2 — Cross-reference findings need source-level text

Claims about which label sits beside which value, what order items appear in, or
whether two lists agree all depend on structure. Structure is the first thing lost
when a page is rendered, fetched, scraped, or flattened into prose.

**Test:** Is the finding about pairing, ordering, or agreement between two places in
the document? And are you reading the source (a dictionary file, a template, markup)
or a rendering of it (fetched page text, a transcription, a copy-paste)?

**Fix:** From a rendering, do not assert the mismatch. Report what you observed and
name the artifact to check against: "the fetched page pairs A with B; verify in the
source, because a rendered table loses its row structure when flattened."

**Exception:** The rendering is the deliverable. An email body, a plain-text file, a
pasted message with nothing behind it. Then what you read is what ships, and
ordering claims stand.

Content a rendering never received (a price injected at runtime, a lazily loaded
section) is absent from your copy, not from the page. Do not report it missing.

### M3 — Find the house style before applying the default

**Test:** Before judging an optional convention, have you looked for a style guide
in the project? Usual homes: `STYLE.md`, `CONTRIBUTING.md`, a `.claude/` agent or
skill that gates copy, a brand section in `README.md` or `CLAUDE.md`, a glossary
beside the content files.

**Fix:** Read it, follow it, and name it in the frame line. A house rule outranks
every default in this corpus, `usage.md` included. Where the house style is silent,
the corpus default applies.

**Exception:** The user pasted loose text with no project around it, or asked for
this corpus's defaults on purpose.

### M4 — Derive the document's own system before calling it inconsistent

Two tokens that differ are not yet an inconsistency. Documents often follow a rule
narrower than the corpus default, and perfectly coherent.

**Test:** Collect every instance of the pattern across the document, not the two you
happened to notice. Does one rule explain all of them?

**Fix:** If a rule explains them, the document is consistent. Say what the rule is
and move on, reporting only the instances that break it.

**Exception:** The inferred rule is itself the defect, such as a "system" that turns
out to be one spelling in the first half and another in the second. Then report the
system rather than the instances.

Worked example from a real review: a file mixed `four tools` with `30 days` and
`7 days`. Two tokens suggest a numerals-versus-words inconsistency. Collecting all of
them shows a coherent rule, counts spelled out and measured durations in numerals,
which nothing in the file breaks. There was no finding.
