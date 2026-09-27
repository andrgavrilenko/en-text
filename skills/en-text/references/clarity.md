# Clarity — sentence and paragraph mechanics

Rules `C1`–`C23`. These are the load-bearing rules: a text that passes them is easy
to follow even if every other file in this corpus is ignored. It can still read as
machine-made; `slop.md` covers that half.

Each rule has a **test**, a **fix**, and an **exception** that names where the rule
stops applying. Most tests run on a single sentence. C8 and C10–C12 read a
paragraph, C22 and C23 the whole document, and a few, such as C11 and C18, call for
judgment rather than a count. The exception is half of the rule: it keeps a checker
from flattening a voice.

---

## Part 1 — Who is doing what (C1–C7)

Check this first in any hard sentence: is the grammatical subject the thing acting,
and is the verb the action?

### C1 — Characters into subjects

**Test:** Ask "who is doing this?" If the answer is in the sentence but is not the
subject, the sentence is inside out.

**Fix:** Put the actor in the subject slot.

- `A decision was made by the committee to approve the proposal.`
- → `The committee approved the proposal.`

**Exception:** The actor is unknown, irrelevant, or withheld for a reason the text
gives (see C6). The same holds when the actor is an abstraction the passage is
about: `The policy failed` is fine in a passage about the policy.

### C2 — Actions into verbs

**Test:** Find the action the sentence is about. Is it a verb, or has it been
frozen into a noun?

**Fix:** Thaw it back into a verb.

- `We performed an analysis of the data.` → `We analyzed the data.`
- `Their reaction to the news was one of surprise.` → `The news surprised them.`

**Exception:** The noun form is the established term of art and the verb would
sound odd or mean something else: `run a regression`, `file a motion`, `raise an
exception`.

### C3 — Nominalizations

A nominalization is a verb or adjective wearing a noun costume: *investigate →
investigation*, *decide → decision*, *apply → application*, *careless →
carelessness*.

**Test:** Scan for `-tion`, `-ment`, `-ance`, `-ence`, `-ity`, `-ness`, and `-ing`
used as a noun. Each hit is a suspect to check against the exception.

**Fix:** Convert to a verb and give it a subject taken from the text. If the text
names no actor, do not invent one: a gerund that takes an object (`introducing the
policy`) is still a verb and can hold the subject slot.

- `The introduction of the policy caused a reduction in usage.`
- → `Introducing the policy reduced usage.`

**Exception:** A nominalization that names a known thing rather than an action is
fine, and often necessary: *the Reformation*, *an application* (the software), *a
decision* you are about to quote. It also works as an old-information subject:
`This decision surprised everyone` refers back to something already described.

### C4 — Empty verbs

*Make*, *do*, *have*, *perform*, *conduct*, *provide*, *achieve*, *take*, and
*undertake* paired with a nominalization.

**Test:** Does the verb carry meaning, or is it a forklift carrying a noun?

**Fix:** `make a recommendation` → `recommend`; `provide assistance` → `help`;
`conduct an investigation` → `investigate`; `achieve improvements in` → `improve`;
`take into consideration` → `consider`.

**Exception:** The noun carries a modifier the verb cannot: `make a tentative,
non-binding recommendation` has no clean verb form. Keep that pair, and apply the
rule to the other pairs in the text.

### C5 — The paramedic method

For any sentence that feels heavy and will not resolve any other way, run this
adaptation of Lanham's paramedic method, in order:

1. Circle every preposition.
2. Circle every form of *to be* (`is`, `are`, `was`, `were`, `been`, `being`).
3. Ask: where is the action? Who is kicking who?
4. Put that action in a plain active verb.
5. Start fast: delete the wind-up.
6. Read it aloud.

**Test:** Three or more prepositions in an unbroken chain (`in the process of the
review of the implementation of`).

**Fix:** A chain that buries an action has a shorter form. Find the one verb hiding
in it.

**Exception:** The chain names a fixed path or hierarchy: `in the top-left corner of
the second page of the appendix`. Each link narrows the location, so the chain
stays.

### C6 — Passive voice: when it earns its place

The passive is not an error. It is a tool for controlling what sits at the front of
a sentence.

**Test:** Can you append "by zombies" after the verb? Then the verb is passive, and
the real question follows: does the reader need to know who acted?

In rules, policies, contracts, terms, and permissions, the answer is yes whenever the
passive describes a party granting, limiting, or removing access or rights: `may be
read`, `will be shared`, `can be suspended`. The reader must know who holds that
power, and the text names the holder only when the reader can point to it without
guessing. After `Send appeals to the grants committee`, the line `Late appeals may
be refused` names the committee. After `Tenants report maintenance problems to the
landlord`, the line `The apartment may be entered for inspections` names no one:
the landlord was named for a different act. A fixed rule that applies to everyone
the same way involves no party's decision and gets the ordinary question: `Uploads
are limited to 50 MB per file`.

**Fix:** Cut the passive when it hides an actor the reader needs (`mistakes were
made`), or when it exists only because the writer was reaching for formality. For
an access-and-rights passive, name the party in the clause, either in the active
voice or in a `by` phrase that keeps the topic in front for C8: `Your account can
be suspended` → `We can suspend your account` or `Your account can be suspended by
your workspace admin`, whichever is true. If the text does not say who holds the
power, ask the author rather than pick the likeliest party.

**Exception:** Keep the passive in these cases:

- The actor is unknown: `The server was compromised at 3 a.m.`
- The actor is irrelevant: `The samples were frozen overnight.`
- The object is the topic of the passage and belongs in the subject slot to keep
  the flow of C8: `The bill passed the House. It was then sent to the Senate.`
- The text withholds the actor and gives the reason, such as an open investigation
  or a source who asked not to be named. `Mistakes were made` gives none, so the
  Fix applies.

None of these covers an access-and-rights passive. If its actor is unknown, ask the
author; if its topic must stay in front, add a `by` phrase.

### C7 — First seven or eight words

**Test:** Read only the first seven or eight words of a sentence. Do they name the
main character and start the action?

**Fix:** If those words are all throat-clearing (`In terms of the question of
whether it might be the case that`), the reader has spent a quarter of the sentence
learning nothing. Delete and restart on the actor.

**Exception:** An orienting clause the reader needs first can push the actor past
the eighth word: `After the 3 a.m. failover to the standby region, the primary came
back with stale data.` The wind-up is doing work.

---

## Part 2 — How sentences connect (C8–C13)

### C8 — Old before new

**Test:** Does each sentence open with information the reader already has, and close
with what is new?

English readers use the start of a sentence to orient and the end to absorb. A
paragraph where every sentence opens with new material forces the reader to hold
fragments in memory until the connection arrives.

**Fix:** Move the known element to the front, even at the cost of a passive.

- `A new caching layer sits in front of the database. Latency dropped by 60% because of it.`
- → `A new caching layer sits in front of the database. It cut latency by 60%.`

This rule outranks C6: if keeping old information in the subject slot requires a
passive, use the passive. An access-and-rights passive (C6) still names its actor,
in a `by` phrase.

**Exception:** The first sentence of a document or section, which has no old
information to open on. And deliberate surprise, where the writer wants the new
element to land first.

### C9 — Stress position

The end of a sentence is where emphasis lands, whether you intend it or not.

**Test:** Read the sentence and note the last five words. Is that what you want the
reader to carry away?

**Fix:** Put the thing you want remembered at the end. Move qualifiers, citations,
and administrative detail forward, and keep what you move short: C7 still wants the
actor within the first eight words, and C16 still wants the main clause early.

- `Revenue doubled in the third quarter, according to Tuesday's report.`
- → `According to Tuesday's report, revenue doubled in the third quarter.`

**Exception:** The qualifier can be the point: `Revenue doubled, but only on
paper.` The reservation belongs in the stress position because it is the news.

### C10 — Topic strings

**Test:** List the grammatical subject of every sentence in a paragraph. Read the
list on its own.

If the list is coherent (`The compiler… It… The compiler's output… That output…`),
the paragraph will feel focused. If it wanders (`The compiler… Developers…
Performance… Our team… The 2019 rewrite…`), the paragraph is about five things and
the reader is doing the work of sorting them.

**Fix:** Choose one topic and make it the subject of most sentences. Move the others
into predicates or into their own paragraph.

**Exception:** A paragraph whose job is to introduce several actors before the
document follows each in turn. The list of subjects wanders on purpose, once.

### C11 — One idea per paragraph, stated early

**Test:** Can a reader answer "what is this paragraph about?" from its first
sentence or two?

**Fix:** Move the point to the top. A point buried in the middle of a long paragraph
is hard to find by skimming, and most readers skim.

**Exception:** Narrative and argumentative build-ups that deliberately delay the
point. Deliberate is the operative word.

### C12 — Transitions must carry weight

**Test:** Delete the connective. Does the relationship between the two sentences
become unclear? If not, the connective was pacing filler.

**Fix:** Cut any connective that does not signal a real relationship.
`Additionally`, `Moreover`, and `Furthermore` at the head of a paragraph rarely do.
Keep a connective when it marks contrast (`but`, `still`, `yet`), cause (`so`,
`because`), or concession (`even so`, `granted`). Prefer the shorter word: `but`
over `however`, `so` over `consequently`, `also` over `additionally`.

See also `S14`, which counts paragraph-opening connectives as an AI tell; there, two
in a row already make a pattern. C12 judges each connective on its own.

**Exception:** A long argument where the reader needs to be told "this is the third
of four reasons". Signposting earns its place when the structure is real.

### C13 — Parallel structure

**Test:** In any list, series, or pair joined by `and` or `or`, do the items share a
grammatical shape?

**Fix:** Recast the odd item to match the others.

- `The tool validates input, error reporting, and it will retry failed jobs.`
- → `The tool validates input, reports errors, and retries failed jobs.`

**Exception:** A writer may break the shape once, on purpose, to make the last item
land: `The migration was quick, cheap, and a mistake.` Two adjectives set the
pattern, and the noun phrase that breaks it carries the verdict. If it happens
twice, it is a habit.

---

## Part 3 — Weight and length (C14–C18)

### C14 — Sentence length: vary it, then check the long ones

Judge sentence length across a passage, by its **distribution**. Prose where every
sentence runs 12 to 18 words is as tiring as prose where every sentence runs 45.

**Test:** For any sentence over 35 words, ask whether the reader must hold more than
two clauses in memory before the main verb arrives. For any stretch of four or more
short sentences in a row, ask whether the rhythm is doing something or just
hammering.

**Fix:** Split the long sentence at the clause boundary where the reader's memory
is fullest. Merge or vary the short ones.

**Exception:** A long sentence whose clauses arrive in order and never stack, so the
reader never holds more than two at once. Length says where to look; load decides.

### C15 — Subject and verb stay close

**Test:** Count the words between the grammatical subject and its verb. More than a
handful, and the reader is holding the subject in memory while parsing an
interruption.

**Fix:** Move the interruption out, before or after the main clause.

- `The proposal, which the committee had reviewed in March after three rounds of
  revisions and a long argument about scope, failed.`
- → `The committee reviewed the proposal in March, after three rounds of revisions
  and a long argument about scope. It failed.`

**Exception:** A short appositive that identifies the subject is fine: `The
proposal, the third this year, failed.` Four words do not strain anyone.

### C16 — Front-load the main clause

**Test:** Does the sentence open with a subordinate clause longer than about ten
words before the main clause arrives? Does the paragraph do it three times?

**Fix:** Lead with the main clause and hang the condition off the end.

- `Because the migration had not completed and the fallback path was untested, the
  deploy failed.`
- → `The deploy failed because the migration had not completed and the fallback path
  was untested.`

**Exception:** When the subordinate clause is the old information (C8) and the main
clause is the news. One such sentence per paragraph is normal; three is a tic.

### C17 — Cut the metadiscourse

Metadiscourse is prose about the text itself: `It is important to note that`, `It
should be mentioned that`, `In this section we will discuss`, `As we have seen`,
`The purpose of this paragraph is`.

**Test:** Delete the phrase. Does any meaning disappear?

**Fix:** Delete it. Start the sentence on the thing being noted.

See also `S4`, whose hedging frames overlap these.

**Exception:** Signposting in a long technical document, used sparingly, and real
hedges that mark actual uncertainty (see C18).

### C18 — Hedging: keep the honest ones

`May`, `might`, `appears to`, `suggests`, and `in most cases` are load-bearing when
the evidence is partial. Cutting them makes the text more confident and less true,
which is the wrong trade.

**Test:** Would a domain expert defend this qualifier? If it is there because the
writer was being polite to a hypothetical objector, it is padding.

**Fix:** Cut hedges that are social padding, and collapse stacked hedges: `It seems
like it might possibly be the case that this could perhaps indicate` → `This may
indicate`.

See also `S4`, the list of hedges that say nothing about the evidence.

**Exception:** The hedge is the claim. A paper reporting a weak effect, a status
update on an unconfirmed root cause, a forecast. Here the qualifier is the most
honest word in the sentence and removing it is a factual error.

---

## Part 4 — Word choice and consistency (C19–C23)

### C19 — The shorter word, unless the longer one is more exact

**Test:** Is there a shorter, more common word that means the same thing here?

**Fix:** `Use` over `utilize`. `Start` over `commence`. `About` over
`approximately` in prose.

**Exception:** The longer word is more exact. `Intermittent` says something
`sometimes` does not. `Approximately` is right where `about` could be read as
`concerning`: `a report about 300 incidents` can mean either.

### C20 — Concrete over abstract

**Test:** Can the reader see it, count it, or do it?

**Fix:** Replace the abstraction with the number, the name, or the mechanism.

- `We improved operational efficiency in the deployment process.`
- → `We cut deploy time from 40 minutes to 6.`

The figures in that fix have to come from the author or a source. When the text
gives none, ask for them rather than invent them: a made-up number is a false claim,
however concrete it looks. With real figures in hand, numbers, names, and times are
the cheapest clarity available.

**Exception:** The abstraction is the subject under discussion, as in a policy
document that must speak about "efficiency" as a category, or when the concrete
figure is confidential and saying so is more honest than inventing one. Also a
summary line that the sentences around it make concrete: `The launch went badly` is
fine when the paragraph goes on to say what broke and for how long, and a closing
line that sums up figures already given is fine for the same reason.

### C21 — Cut the intensifiers

`Very`, `really`, `quite`, `extremely`, `incredibly`, `truly`, `actually`,
`literally`, `basically`, `simply`, `just`.

**Test:** Delete the adverb. Is the sentence weaker or merely shorter?

**Fix:** Delete it. When something is extreme, a stronger word carries it better
than an adverb propping up a weak one: `very big` → `huge`.

See also `S3`, which counts intensifiers as an AI tell.

**Exception:** `Actually` and `just` stay when they mark a real contrast or limit:
`It takes just two steps` (against an expectation of more). `Literally` stays when
the thing is literal and a reader might assume metaphor.

### C22 — One meaning per term

**Test:** List every name the document uses for the same thing.

**Fix:** In technical writing, pick one name for each thing and never vary it for
elegance. `User`, `customer`, `account holder`, and `end user` in one document read
as four entities. Inconsistency costs more than repetition.

**Exception:** Prose written for pleasure, where repetition is the flaw and
variation is the point. Terms also stay distinct when they name different things: a
`customer` who pays and a `user` who logs in are two entities, and should stay two
words.

### C23 — The document agrees with itself

A fact stated in two places must have the same value in both.

**Test:** List every count, amount, date, limit, and offer the document states, with
each place it appears. Pair two places only when they describe the same thing: the
same subject and the same measure. Does any of them take two values? Does every count over a
list match the list? Does every button or link label promise what the sentence
beside it says? A `Buy Pro` button under `Try Pro free for 14 days` leaves the
reader unsure whether the click charges them.

**Fix:** Make them agree. When the text does not say which version is right, ask the
author rather than choose. Once the author confirms that all four steps belong, the
fix is one word:

- `Setup takes three steps.` above a numbered list of four
- → `Setup takes four steps.`

**Exception:** A count or pairing read from a flattened table (a fetched page, a
pasted spreadsheet) is something to verify in the source before it becomes a finding
(`M2`). A list written as a list, in the same text as its count, gets the full
check. A difference the text explains also passes: `Refunds within 30 days, or 60
on annual plans` sets two limits on purpose. So do two figures for two different
things, however close they sit: a 14-day trial and a 30-day refund window are two
limits, each stated once.
