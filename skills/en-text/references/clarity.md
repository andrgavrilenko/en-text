# Clarity — sentence and paragraph mechanics

Rules `C1`–`C22`. These are the load-bearing rules: a text that passes them reads
well even if every other file in this corpus is ignored.

Each rule has a **test** you can run mechanically on a sentence, a **fix**, and an
**exception** that names where the rule stops applying. The exception is not a
footnote. It is the half of the rule that keeps a checker from flattening a voice.

---

## Part 1 — Who is doing what (C1–C7)

The single most reliable predictor of a hard sentence: the grammatical subject is
not the thing acting, and the verb is not the action.

### C1 — Characters into subjects

**Test:** Ask "who is doing this?" If the answer is in the sentence but is not the
subject, the sentence is inside out.

**Fix:** Put the actor in the subject slot.

- `A decision was made by the committee to approve the proposal.`
- → `The committee approved the proposal.`

**Exception:** The actor is genuinely unknown, irrelevant, or deliberately withheld
(see C6). Also when the actor is an abstraction the passage is about: `The policy
failed` is fine when the policy, not the people, is the topic.

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
used as a noun. Each is a suspect, not a conviction.

**Fix:** Convert to a verb and give it a subject.

- `The introduction of the policy caused a reduction in usage.`
- → `After we introduced the policy, fewer people used it.`

**Exception:** A nominalization that names a known thing rather than an action is
fine, and often necessary: *the Reformation*, *an application* (the software), *a
decision* you are about to quote. Also fine as an old-information subject: `This
decision surprised everyone` refers back to something already described.

### C4 — Empty verbs

*Make*, *do*, *have*, *perform*, *conduct*, *provide*, *achieve*, and *undertake*
paired with a nominalization.

**Test:** Does the verb carry meaning, or is it a forklift carrying a noun?

**Fix:** `make a recommendation` → `recommend`; `provide assistance` → `help`;
`conduct an investigation` → `investigate`; `achieve improvements in` → `improve`;
`take into consideration` → `consider`.

**Exception:** When the noun carries a modifier the verb cannot: `make a tentative,
non-binding recommendation` has no clean verb form. Keep the noun, cut the empty
verb elsewhere.

### C5 — The paramedic method

For any sentence that feels heavy and will not resolve any other way, run Lanham's
drill in order:

1. Circle every preposition.
2. Circle every form of *to be* (`is`, `are`, `was`, `were`, `been`, `being`).
3. Ask: where is the action? Who is kicking who?
4. Put that action in a plain active verb.
5. Start fast: delete the wind-up.
6. Read it aloud.

**Test:** Three or more prepositions in an unbroken chain (`in the process of the
review of the implementation of`).

**Fix:** The chain always has a shorter form. Find the one verb hiding in it.

**Exception:** Chains that name a fixed path or hierarchy: `in the top-left corner
of the second page of the appendix`. Location, not action.

### C6 — Passive voice: when it earns its place

The passive is not an error. It is a tool for controlling what sits at the front of
a sentence.

**Test:** Can you append "by zombies" after the verb? That identifies the passive.
It does not condemn it. Then ask the real question: does the reader need to know
who acted?

**Fix:** Cut the passive when it hides an actor the reader needs (`mistakes were
made`), or when it exists only because the writer was reaching for formality.

**Exception:** Keep the passive when:

- The actor is unknown: `The server was compromised at 3 a.m.`
- The actor is irrelevant: `The samples were frozen overnight.`
- The object is the topic of the passage and belongs in the subject slot to keep
  the flow of C8: `The bill passed the House. It was then sent to the Senate.`
- You are deliberately withholding the actor and take responsibility for doing so.

### C7 — First seven or eight words

**Test:** Read only the first seven or eight words of a sentence. Do they name the
main character and start the action?

**Fix:** If those words are all throat-clearing (`In terms of the question of
whether it might be the case that`), the reader has spent a quarter of the sentence
learning nothing. Delete and restart on the actor.

**Exception:** A short orienting clause that carries real information the reader
needs first: `After the 3 a.m. failover, the primary came back with stale data.`
The wind-up is doing work.

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
passive, use the passive.

**Exception:** The first sentence of a document or section, which has no old
information to open on. And deliberate surprise, where the writer wants the new
element to land first.

### C9 — Stress position

The end of a sentence is where emphasis lands, whether you intend it or not.

**Test:** Read the sentence and note the last five words. Is that what you want the
reader to carry away?

**Fix:** Put the thing you want remembered at the end. Move qualifiers, citations,
and administrative detail forward.

- `Revenue doubled in the third quarter, according to the report we filed on Tuesday.`
- → `According to the report we filed on Tuesday, revenue doubled in the third quarter.`

**Exception:** When the qualifier *is* the point: `Revenue doubled, but only on
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

**Fix:** Move the point to the top. Long paragraphs that bury the point in the
middle are not richer; they are harder to skim, and most readers skim.

**Exception:** Narrative and argumentative build-ups that deliberately delay the
point. Deliberate is the operative word.

### C12 — Transitions must carry weight

**Test:** Delete the connective. Does the relationship between the two sentences
become unclear? If not, the connective was pacing filler.

**Fix:** Cut any connective that does not signal a real relationship.
`Additionally`, `Moreover`, and `Furthermore` at the head of three consecutive
paragraphs mean nothing. Keep a connective when it marks contrast (`but`, `still`,
`yet`), cause (`so`, `because`), or concession (`even so`, `granted`). Prefer the
short Anglo-Saxon ones: `but` over `however`, `so` over `consequently`, `also` over
`additionally`.

See also `S14`: formulaic transitions are an AI tell as well as a clarity problem.

**Exception:** A long argument where the reader genuinely needs to be told "this is
the third of four reasons". Signposting is not filler when the structure is real.

### C13 — Parallel structure

**Test:** In any list, series, or pair joined by `and` or `or`, do the items share a
grammatical shape?

**Fix:** Recast the odd item to match the others.

- `The tool validates input, error reporting, and it will retry failed jobs.`
- → `The tool validates input, reports errors, and retries failed jobs.`

**Exception:** A deliberate break in the pattern used for emphasis, once: `Fast,
cheap, and, as it turned out, wrong.` If it happens twice it is not deliberate.

---

## Part 3 — Weight and length (C14–C18)

### C14 — Sentence length: vary it, then check the long ones

There is no correct sentence length. There is a correct **distribution**. Prose
where every sentence runs 12 to 18 words is as tiring as prose where every sentence
runs 45.

**Test:** For any sentence over 35 words, ask whether the reader must hold more than
two clauses in memory before the main verb arrives. For any stretch of four or more
short sentences in a row, ask whether the rhythm is doing something or just
hammering.

**Fix:** Split the long sentence at the clause boundary where the reader's memory
is fullest. Merge or vary the short ones.

**Exception:** Long sentences whose clauses arrive in order and never stack, so the
reader is never holding more than one thing. Length is not the problem; load is.

### C15 — Subject and verb stay close

**Test:** Count the words between the grammatical subject and its verb. More than a
handful, and the reader is holding the subject in memory while parsing an
interruption.

**Fix:** Move the interruption out, before or after the main clause.

- `The proposal, which the committee had reviewed in March after three rounds of
  revisions and a long argument about scope, failed.`
- → `The committee reviewed the proposal in March, after three rounds of revisions
  and a long argument about scope. It failed.`

**Exception:** A short appositive that identifies the subject: `The proposal, the
third this year, failed.` Three words do not strain anyone.

### C16 — Front-load the main clause

**Test:** Does the sentence open with a subordinate clause longer than about ten
words before the main clause arrives? Does the paragraph do it three times?

**Fix:** Lead with the main clause and hang the condition off the end.

- `Because the migration had not completed and the fallback path was untested, the
  deploy failed.`
- → `The deploy failed: the migration had not completed and the fallback path was untested.`

**Exception:** When the subordinate clause is the old information (C8) and the main
clause is the news. One such sentence per paragraph is normal; three is a tic.

### C17 — Cut the metadiscourse

Sentences about the text rather than about the subject: `It is important to note
that`, `It should be mentioned that`, `In this section we will discuss`, `As we
have seen`, `The purpose of this paragraph is`.

**Test:** Delete the phrase. Does any meaning disappear?

**Fix:** Delete it. Start the sentence on the thing being noted.

**Exception:** Genuine signposting in a long technical document, used sparingly, and
real hedges that mark actual uncertainty (see C18).

### C18 — Hedging: keep the honest ones

`May`, `might`, `appears to`, `suggests`, and `in most cases` are load-bearing when
the evidence is genuinely partial. Cutting them makes the text more confident and
less true, which is the wrong trade.

**Test:** Would a domain expert defend this qualifier? If it is there because the
writer was being polite to a hypothetical objector, it is padding.

**Fix:** Cut hedges that are social padding, and collapse stacked hedges: `It seems
like it might possibly be the case that this could perhaps indicate` → `This may
indicate`.

**Exception:** The hedge is the claim. A paper reporting a weak effect, a status
update on an unconfirmed root cause, a forecast. Here the qualifier is the most
honest word in the sentence and removing it is a factual error.

---

## Part 4 — Word choice (C19–C22)

### C19 — The shorter word, unless the longer one is more exact

**Test:** Is there a shorter, more common word that means the same thing here?

**Fix:** `Use` over `utilize`. `Start` over `commence`. `About` over
`approximately` in prose.

**Exception:** The longer word is more exact. `Intermittent` says something
`sometimes` does not. `Approximately` is right in a spec where the imprecision is
the point. This is not a vocabulary size limit.

### C20 — Concrete over abstract

**Test:** Can the reader see it, count it, or do it?

**Fix:** Replace the abstraction with the number, the name, or the mechanism.

- `We improved operational efficiency in the deployment process.`
- → `Deploys went from 40 minutes to 6.`

Numbers, names, and times are the cheapest clarity available.

**Exception:** The abstraction is the subject under discussion, as in a policy
document that must speak about "efficiency" as a category, or when the concrete
figure is confidential and saying so is more honest than inventing one.

### C21 — Cut the intensifiers

`Very`, `really`, `quite`, `extremely`, `incredibly`, `truly`, `actually`,
`literally`, `basically`, `simply`, `just`.

**Test:** Delete the adverb. Is the sentence weaker or merely shorter?

**Fix:** Delete it. When something is genuinely extreme, a stronger noun or verb
carries it better than an adverb propping up a weak one: `very big` → `enormous`.

**Exception:** `Actually` and `just` when they mark a real contrast or limit: `It
takes just two steps` (against an expectation of more). `Literally` when the thing
is literal and a reader might assume metaphor.

### C22 — One meaning per term

**Test:** List every name the document uses for the same thing.

**Fix:** In technical writing, pick one name for each thing and never vary it for
elegance. `User`, `customer`, `account holder`, and `end user` in one document read
as four entities. Inconsistency costs more than repetition.

**Exception:** Prose written for pleasure, where repetition is the flaw and
variation is the point. And documents where the terms genuinely differ: a `customer`
who pays and a `user` who logs in are two entities, and should stay two words.
