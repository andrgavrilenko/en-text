# Method — how to run a review

Rules `M1`–`M4`. These govern the review, not the prose. The corpus can be right
about a sentence and still produce a bad finding: one that blames the wrong edit,
asserts what a flattened copy cannot show, applies a default the house style
overrides, or calls a coherent system inconsistent.

The rules share the shape of the clarity and slop rules: a test, a fix, and an
exception. All four come from the project's own reviews. `M1`, `M2`, and `M4` were
each written after a review made the mistake the rule now prevents. `M3` records a
step a review took by chance and got right.

---

### M1 — Attribute a finding only with evidence

Requests often arrive as "I just changed these spans; did my changes break
anything?" The corpus can tell you what is in the text. It cannot tell you what
arrived with a particular change. The history is usually out of reach as well: a
review sees only what the request passes to it, and without access to version
control a reviewer cannot fetch the old version.

**Test:** Does the finding claim that a specific edit *introduced* the problem? If
so, do you hold a before state? A diff, a previous version, or the old text quoted
in the request each counts.

**Fix:** With a before state, compare the two versions and attribute. Without one,
say once, before the findings, that you cannot tell which of them the edit
introduced. Ask in the same place for the before state: the previous version, or a
diff passed with the request (for a file under version control, the output of
`git diff` on it). Then report what is in the text now, without attribution, and do
not repeat the caveat on each finding.

**Exception:** The requester asks for your best guess and accepts that it is
inference. Give it, labeled as inference and kept apart from the findings.

A reviewer who confidently misattributes sends the writer hunting through their own
change for something that was always there, and the error spreads doubt onto the
findings that were correct.

There is a middle case worth handling well. The request names which spans changed,
and a pattern lines up with exactly those spans. The match is worth stating, and it
is still not evidence. Describe what you observed and let the writer draw the
conclusion: "the four you named share a shape the other two lack" beats "your
rewrite left the other two stranded." The first survives the request being wrong
about which spans actually changed; the second does not.

### M2 — Layout claims need source-level text

Some findings depend on layout: which label sits beside which value, the order of
rows or columns, which items belong to which group. Layout is the first thing lost
when a page is fetched, scraped, transcribed, or flattened into prose. A flattened
table can move a label away from its value while every word survives.

Findings that do not depend on layout survive flattening, and this rule leaves them
alone: a count stated in the text against a plain list of the items, a spelling, a
term, a number format. Report those as fact from any copy.

**Test:** Does the finding depend on layout? If so, does the text show signs that
its layout was lost: a conversion banner, labels cut off from their values, a
table's repeated headers turned into prose, cells from different rows run together?
Pasted or fetched text with no such sign counts as the deliverable.

**Fix:** When the signs are there, do not assert the layout claim. Report what you
observed and name the artifact to check against: "the fetched page pairs A with B;
verify in the source, because a flattened table loses its rows."

**Exception:** The requester says the flat text is what ships, such as an email body
or a plain-text notice. Then the layout you see is the layout the reader gets, and
claims about it stand.

A rendering can also lack content the page shows: a price injected at runtime, a
section that loads on scroll. That content is missing from your copy and may still
be on the page, so do not report it missing.

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
narrower than the corpus default and stay coherent under it.

`M4` never licenses a mix that a usage rule forbids. Where a usage rule says to pick
one system per document (heading case in `U23`, spelling variant in `U28`), a rule
you derive must stay inside one of its systems. A title-case page title above
sentence-case sections follows a describable rule, title case for the title only,
and is still two heading systems in one document.

**Test:** Collect every instance of the pattern across the document, not the two you
happened to notice. Does one rule explain all of them? If a usage rule covers the
pattern and says to pick one system, does your rule stay inside one of its systems?

**Fix:** If it does, the document is consistent. Say what the rule is and report
only the instances that break it. If the only rule that fits mixes two systems that
a usage rule asks you to choose between, report the mix under that usage rule.

**Exception:** The inferred rule is itself the defect: it follows position or
authorship rather than a kind of thing, such as numerals in the first half and words
in the second. Then report the system rather than the instances.

When a review covers several files, derive the system per file, and report any
difference between files once, as one finding about the set that says which files
use which convention. Files published as one document, such as pages assembled from
includes, count as one document.

Worked example from a real review: a file mixed `four tools` with `30 days` and
`7 days`. Two tokens suggest a numerals-versus-words inconsistency. Collecting all
of them shows one rule that nothing in the file breaks: counts are spelled out, and
measured durations are in numerals. There was no finding.
