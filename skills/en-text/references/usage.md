# Usage — grammar, punctuation, numbers, typography

Rules `U1`–`U28`. Load this file when proofreading, or when a specific mark, number,
or capital is in question.

The rules answer two kinds of question. Some have a right answer: a comma alone does
not join two sentences (`U2`); a plural takes no apostrophe (`U6`); a restrictive
clause takes no commas (`U11`); countable things take `fewer` (`U13`); and `affect`
is not `effect` (`U14`). Others are conventions, where style guides disagree and
each option is defensible: the serial comma, dash spacing, US or UK spelling, and
heading case. Two principles govern the whole file:

- **A house style beats this file.** If the project has a style guide, follow it and
  say so (`M3`). Where none exists, these rules are the defaults, drawn from the
  sources in `sources.md`.
- **Consistency beats correctness** for any choice this file leaves open. No option
  is wrong there, so the only finding is a mix: pick what the document already does
  and hold it.

---

## Part 1 — Punctuation (U1–U10)

### U1 — Serial comma

Default to using it: `red, white, and blue`. It prevents real ambiguity (`to my
parents, Ayn Rand and God`) and costs nothing.

If the document consistently omits it, keep omitting it. Do not switch mid-document.

### U2 — Comma splice

Two independent clauses joined by a comma alone: `The build failed, we rolled back.`

**Fix:** period, semicolon, or a conjunction. Keep a splice only in deliberately
fast, informal prose, and only when it is clearly a choice.

### U3 — Semicolon

Two uses, both narrow: joining independent clauses that belong in one breath, and
separating list items that already contain commas.

If a semicolon appears more than once or twice per page of technical prose, most of
them want to be periods.

### U4 — Colon

In running text, the part before a colon should be a complete clause. The part after
explains, lists, or delivers it.

- Wrong: `The tools we use are: Vale, Git, and Make.`
- Right: `We use three tools: Vale, Git, and Make.`

Labels and lead-ins are exempt: field labels, such as this corpus's own `**Test:**`,
`**Fix:**`, and `**Exception:**`; list and table labels (`**Speed**: ...`,
`Note:`); headings; and a short lead-in to a vertical list (`You need:` above the
bullets).

### U5 — Em dash, en dash, hyphen

- **Hyphen** (`-`): compound modifiers (`well-known problem`), prefixes where needed.
- **En dash** (`–`): ranges (`2019–2024`, `pages 10–14`), although some technical
  styles use a hyphen for them (`U21`). For a relationship between two equal terms,
  styles split between the en dash (`client–server`) and the hyphen
  (`client-server`).
- **Em dash** (`—`): a break in thought, an aside, an interruption.

Dash spacing is a house choice. AP spaces the em dash (`word — word`), Chicago
closes it up (`word—word`), and UK style often uses a spaced en dash in its place
(`word – word`). Any of the three is fine when held consistently. A single dash
cannot be inconsistent with itself, so a document with one dash gives no spacing
finding.

See `S21` for the frequency problem and the social-media caveat.

### U6 — Apostrophes

Possessive `its` has no apostrophe; `it's` is always `it is` or `it has`. Plurals
never take one (`the 1990s`, `several APIs`, `two PDFs`).

Singular nouns ending in `s` take `'s` in most modern styles (`the business's
model`); classical names often take the bare apostrophe (`Socrates'`). Be
consistent.

### U7 — Quotation marks

US: double quotes primary, single nested, commas and periods inside the closing
quote. UK: often single primary, punctuation placed by logic.

In technical writing, keep punctuation outside the quotes when the quoted string is
literal: `Type "deploy", then press Enter` — a trailing comma inside the quotes
would be part of the command.

### U8 — Parentheses vs commas vs dashes

Three weights for the same aside: parentheses are quietest, commas neutral, dashes
loudest. Varying them is the cure for `S21`.

Never nest parentheses in prose; rewrite.

### U9 — Exclamation marks

One per document, at most, in professional writing. None in reference documentation.
An exclamation mark cannot make a sentence exciting; it can only announce that the
writer hoped so.

### U10 — Ellipsis

Use it for omitted text in a quotation, or for a genuine trailing off, not as a
general pause. Set it as a single character (`…`) or as three spaced periods, per
house style.

When the omission follows a grammatically complete sentence, that sentence keeps its
period and the ellipsis comes after it, four dots in all:
`The tests passed. . . . We shipped anyway.` Chicago and AP both work this way. Five
dots are never right, and neither are four after text that is not a complete
sentence.

---

## Part 2 — Words that get misused (U11–U18)

### U11 — That vs which

Restrictive clause (narrows what you mean): `that`, no comma. Non-restrictive (adds
an aside): `, which`, with a comma.

- `The tests that fail on Windows are skipped.` (only those tests)
- `The tests, which fail on Windows, are skipped.` (all of them, and by the way)

UK usage permits restrictive `which`. In technical writing the distinction is worth
keeping anyway: it is load-bearing.

### U12 — Who vs that

`That` for people (`the engineer that wrote it`) is standard English;
Merriam-Webster and Garner both accept it. `Who` is a preference, not a rule: change
`that` to `who` only under a house style that asks for it, as AP and APA do.
Organizations take `that` or `which` in US usage; UK usage often takes `who` when
the organization acts as a group of people (`the committee, who are divided`).

### U13 — Fewer vs less

Countable things take `fewer` (`fewer requests`); mass quantities take `less`
(`less latency`, `less memory`). `Less` with numbers is standard for measured
amounts: `less than 5 ms`.

### U14 — Commonly confused pairs

`affect` (verb) / `effect` (noun, usually); `comprise` (the whole comprises the
parts) / `compose`; `principal` (chief) / `principle` (rule); `complement` /
`compliment`; `discreet` / `discrete`; `ensure` (make certain) / `insure` (cover
with insurance) / `assure` (tell someone, to remove a doubt); `i.e.` (that is) /
`e.g.` (for example); `imply` (speaker) / `infer` (listener).

US dictionaries also give `insure` the sense of making certain. Some usage guides
keep it for insurance, so treat that choice as house style rather than as an error.

### U15 — Latin abbreviations

Prefer English in running prose: `for example` over `e.g.`, `that is` over `i.e.`,
`and so on` over `etc.` Keep the abbreviations inside parentheses and tables where
space matters. In US style they take a following comma: `e.g., Git`.

### U16 — Redundant pairs

`each and every`, `first and foremost`, `full and complete`, `basic fundamentals`,
`advance planning`, `past history`, `end result`, `final outcome`, `close
proximity`, `added bonus`, `free gift`, `new innovation`, `completely eliminate`,
`absolutely essential`.

Cut one half of each.

### U17 — Clichés and worn-out metaphors

`low-hanging fruit`, `move the needle`, `boil the ocean`, `circle back`, `think
outside the box`, `paradigm shift`, `perfect storm`, `tip of the iceberg`, `the
elephant in the room`, `at the end of the day`, `take it to the next level`.

A worn-out metaphor no longer calls up a picture. The reader skims past it at no
cost and gets nothing from it. Replace it with the literal claim. A metaphor so old
that it is now the ordinary word for the thing (`bottleneck`, `deadline`, `bug`) is
not a finding.

### U18 — Inclusive and neutral wording

Default to the singular `they` for a person of unknown gender. AP accepts it only
where other wording would be awkward, so under AP reword first: make the noun
plural, or drop the pronoun. Prefer role-neutral terms (`chair`, `firefighter`,
`workforce`). In technical writing prefer `allowlist` / `blocklist`, `primary` /
`replica`, `placeholder`.

Say `people with disabilities` or follow the community's own stated preference; do
not invent euphemisms. Avoid `crazy`, `insane`, `lame`, `blind to`, `tone-deaf` as
casual intensifiers.

---

## Part 3 — Numbers, dates, capitals (U19–U24)

### U19 — Numerals vs words

General prose: spell out zero through nine, use numerals from 10 up. Technical and
scientific writing: numerals for anything measured, including single digits
(`5 ms`, `2 GB`).

Do not start a sentence with a numeral. Rewrite it, or spell the number out. Some
styles let a calendar year open a sentence (`2025 was a quiet year`).

### U20 — Units and spacing

A space between number and unit (`40 ms`, `16 GB`, `20 %` in SI style; `20%` closed
up is standard in US publishing). Pick one and hold it. Degrees and currency close
up in most styles (`$40`, `20°C` or `20 °C` per house rule).

### U21 — Large numbers and ranges

General US and UK prose separates thousands with a comma (`1,048,576`). SI style
groups the digits in threes with a small space and never with a comma
(`1 048 576`), so a document that follows SI units (`U20`) may follow SI grouping
too.

In a range, give the second number in full wherever a shortened one could be
misread (`1898–1901`, never `1898–901`). Shortening a range of years within one
century (`1990–95`) is fine where the house style allows it. Many styles set ranges
with an en dash (`U5`); others, Google's developer documentation style among them,
use a hyphen. Whichever the document uses, hold it.

### U22 — Dates

`ISO 8601` (`2026-09-21`) in logs, filenames, and data. In prose, spell the month:
`21 September 2026` (international) or `September 21, 2026` (US). Never the
ambiguous all-numeral forms `09/21/26` or `21/09/26` in text meant for a global
audience.

### U23 — Capitalization of headings

Two acceptable systems: sentence case (`Getting started with the API`) and title
case (`Getting Started with the API`; AP and APA capitalize any word of four or more
letters, so `With`). Sentence case is the modern default in technical documentation
and is easier to keep consistent.

Choose one system per document, and count the page title (the H1) as a heading like
any other. A title-case page title above sentence-case sections is a mix; the
pattern that describes it (title case for the title only) does not make it
consistent (`M4`). Only a written house style that sets page titles apart overrides
this (`M3`).

### U24 — Capitalization of terms

Do not capitalize a common noun to make it feel important: `the dashboard`, not `the
Dashboard`. Capitalize product names as their owners do, including lowercase ones
(`iPhone`, `npm`, `eBay`), but recast a sentence rather than open it with a
lowercase brand.

---

## Part 4 — Document mechanics (U25–U28)

### U25 — Headings describe, not tease

A heading is a navigation label. `Rate limits` beats `A word about limits`. Headings
should make sense read on their own as a table of contents.

### U26 — Lists

Use a list when the items are parallel and the order is either meaningful or
irrelevant. Do not use a list for a two-item sequence that is a sentence.

Punctuate consistently: either every item is a fragment with no terminal period, or
every item is a full sentence with one. Do not mix. Keep items grammatically
parallel (`C13`), and vary list length (`S15`).

### U27 — Links

Link text names the destination: `see the rate limit rules`, not `click here` or a
bare URL in running prose. Never link a whole sentence.

### U28 — Spelling variant

`US` (`color`, `organize`, `analyze`, `defense`) or `UK`/`Commonwealth` (`colour`,
`organise` or `organize`, `analyse`, `defence`). Detect which the document already
uses and match it; flag mixtures, including a mix that follows a pattern, such as
one variant in the body and the other in the captions (`M4`). Proper names and
quoted text keep their own spelling: `Labour Party` in a US document,
`World Health Organization` in a UK one. When there is no signal, default to US
spelling for software documentation, since the code, APIs, and other documentation
around it mostly use US spelling.
