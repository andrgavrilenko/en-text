#!/usr/bin/env python3
"""Structural checks for the en-text corpus.

Standard library only. Exit code 1 on any failure.

What is checked:
  1. Plugin manifests parse, and their versions agree with the changelog.
  2. Every skill has valid frontmatter; the review skills cannot write files,
     touch git or a shell, or drive Monitor (Write, Edit, NotebookEdit, Bash,
     PowerShell, Monitor all disallowed), and cannot reach the network, start
     another agent or skill, send a message, or call an MCP server (WebFetch,
     WebSearch, Agent, Task, Skill, SendMessage, the MCP resource tools and
     mcp__* all disallowed).
  3. Rule IDs in each reference file are sequential and unique, and the
     counts match what SKILL.md and README claim.
  4. Every clarity (C), slop (S) and method (M) rule has a Test, a Fix, and
     an Exception.
  5. Every rule ID cited anywhere in the repo exists.
  6. Every scoring weight profile sums to 1.0.
  7. Every worked score in the repo follows from its sub-scores and weights,
     each file with worked examples keeps its minimum number of them, and
     arithmetic written out in prose adds up and rounds half up.
  8. The repo's own prose passes its own slop density and em dash
     thresholds, matching inflected forms of the vocabulary tells (not just
     their bare dictionary form).
  9. Local links in README resolve.
 10. Fixtures named in tests/EVAL.md exist.
 11. Every rule range mentioned anywhere in the repo (`C1`-`C23`, S14-S20,
     M1-M4, ...) has real IDs at both ends. Each reference file's own
     "## Part N (Xa-Xb)" headings are checked against the rule headings
     actually under them, and a range mention elsewhere that starts at a
     part's (or the family's) first ID must reach some part's last ID or
     the family's highest ID -- outside a bulleted or numbered list, which
     may cite an arbitrary sourced subset. The "N rules" / "N usage rules"
     / "N clarity, slop and method rules" totals in README and the three
     SKILL.md files match the actual counts.
 12. Nothing under skills/ mentions Russian or ru-text, or contains a
     Cyrillic character.
 13. No stale "within about 0.3" repeatability promise outside CHANGELOG,
     and no promise of a no-argument mode in skills/ or README.
"""

import json
import re
import sys
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:  # noqa: BLE001
    pass

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
REF = SKILLS / "en-text" / "references"

errors: list[str] = []
checks_run = 0


def fail(msg: str) -> None:
    errors.append(msg)


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def section(name: str):
    """Decorator that counts checks and prints a heading."""
    def wrap(fn):
        def inner():
            global checks_run
            checks_run += 1
            before = len(errors)
            fn()
            status = "ok" if len(errors) == before else f"FAIL ({len(errors) - before})"
            print(f"  {name:<58} {status}")
        return inner
    return wrap


# ---------------------------------------------------------------- 1 manifests

@section("manifests parse and versions agree")
def check_manifests():
    plugin = json.loads(read(ROOT / ".claude-plugin" / "plugin.json"))
    mkt = json.loads(read(ROOT / ".claude-plugin" / "marketplace.json"))
    ver = plugin.get("version")
    if not re.fullmatch(r"\d+\.\d+\.\d+", ver or ""):
        fail(f"plugin.json version is not semver: {ver!r}")
    if mkt.get("metadata", {}).get("version") != ver:
        fail("marketplace.json metadata.version != plugin.json version")
    plugins = mkt.get("plugins") or []
    if not plugins or plugins[0].get("version") != ver:
        fail("marketplace.json plugins[0].version != plugin.json version")
    if plugins and plugins[0].get("name") != plugin.get("name"):
        fail("marketplace.json plugin name != plugin.json name")
    changelog = read(ROOT / "CHANGELOG.md")
    m = re.search(r"^## \[(\d+\.\d+\.\d+)\]", changelog, re.M)
    if not m:
        fail("CHANGELOG.md has no versioned entry")
    elif m.group(1) != ver:
        fail(f"CHANGELOG.md top entry {m.group(1)} != plugin version {ver}")
    if plugin.get("license") != "MIT":
        fail("plugin.json license should be MIT (matches LICENSE file)")


# -------------------------------------------------------------- 2 frontmatter

def frontmatter(text: str) -> dict:
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}
    out = {}
    key = None
    for line in m.group(1).splitlines():
        if re.match(r"^[A-Za-z][\w-]*:", line):
            key, _, val = line.partition(":")
            out[key.strip()] = val.strip()
        elif key and line.startswith(" "):
            out[key] = (out[key] + " " + line.strip()).strip()
    return out


# Tools that can write files or run commands. The review skills must deny
# every one of them as a bare entry.
WRITE_TOOLS = ("Write", "Edit", "NotebookEdit", "Bash", "PowerShell", "Monitor")

# Tools a text under review could use to carry data out or act elsewhere: the
# network, another agent or skill, messages, and every MCP server. A forked
# skill inherits all of them from the session unless it denies them.
REACH_TOOLS = ("WebFetch", "WebSearch", "Agent", "Task", "Skill", "SendMessage",
               "ListMcpResourcesTool", "ReadMcpResourceTool", "mcp__*")


def tool_entries(value: str) -> list[str]:
    """Split a frontmatter tool list into its comma-separated entries."""
    return [e.strip() for e in value.split(",") if e.strip()]


@section("frontmatter valid; review skills cannot write or reach out")
def check_frontmatter():
    for d in sorted(SKILLS.iterdir()):
        if not d.is_dir():
            continue
        p = d / "SKILL.md"
        if not p.exists():
            fail(f"{d.name}: missing SKILL.md")
            continue
        fm = frontmatter(read(p))
        if not fm:
            fail(f"{d.name}: no frontmatter")
            continue
        if fm.get("name") != d.name:
            fail(f"{d.name}: frontmatter name {fm.get('name')!r} != folder name")
        desc = fm.get("description", "").lstrip("> ").strip()
        if len(desc) < 40:
            fail(f"{d.name}: description too short to trigger on")
        if len(desc) > 1024:
            fail(f"{d.name}: description over 1024 chars ({len(desc)})")
        if d.name in ("en-check", "en-score"):
            if fm.get("context") != "fork":
                fail(f"{d.name}: expected context: fork")
            if fm.get("user-invocable") != "true":
                fail(f"{d.name}: expected user-invocable: true")
            allowed = tool_entries(fm.get("allowed-tools", ""))
            for bad in WRITE_TOOLS:
                if any(e == bad or e.startswith(bad + "(") for e in allowed):
                    fail(f"{d.name}: allowed-tools must not include {bad}")
            disallowed = tool_entries(fm.get("disallowed-tools", ""))
            for must in WRITE_TOOLS + REACH_TOOLS:
                if must not in disallowed:
                    fail(f"{d.name}: disallowed-tools must list {must} as a bare "
                         f"entry (a scoped {must}(...) entry does not block it)")


# ------------------------------------------------------------- 3 rule IDs

RULE_FILES = {
    "C": "clarity.md",
    "S": "slop.md",
    "U": "usage.md",
    "M": "method.md",
}
HEADING = re.compile(r"^### ([CSUM])(\d+) — (.+)$", re.M)
rule_ids: dict[str, list[int]] = {}
rule_sections: dict[str, dict[int, str]] = {}


@section("rule IDs sequential, unique, counts match claims")
def check_rule_ids():
    total = 0
    skill_md = read(SKILLS / "en-text" / "SKILL.md")
    readme = read(ROOT / "README.md")
    for prefix, fname in RULE_FILES.items():
        text = read(REF / fname)
        heads = HEADING.findall(text)
        nums = [int(n) for p, n, _ in heads if p == prefix]
        wrong_prefix = [f"{p}{n}" for p, n, _ in heads if p != prefix]
        if wrong_prefix:
            fail(f"{fname}: headings with foreign prefix: {wrong_prefix}")
        if nums != list(range(1, len(nums) + 1)):
            fail(f"{fname}: IDs not sequential 1..N: {nums}")
        if len(set(nums)) != len(nums):
            fail(f"{fname}: duplicate IDs")
        n = len(nums)
        rule_ids[prefix] = nums
        total += n
        claim = f"`{prefix}1`–`{prefix}{n}`"
        header = text.split("\n", 4)[:4]
        if claim not in "\n".join(header):
            fail(f"{fname}: header does not state {claim}")
        if claim not in skill_md:
            fail(f"SKILL.md does not state {claim}")
        if claim not in readme:
            fail(f"README.md does not state {claim}")
        # split sections for later checks
        parts = re.split(r"^### (?=[CSUM]\d+ — )", text, flags=re.M)
        secs = {}
        for part in parts[1:]:
            m = re.match(r"([CSUM])(\d+) — ", part)
            if m:
                secs[int(m.group(2))] = part
        rule_sections[prefix] = secs
    if f"{total} rules" not in readme:
        fail(f"README.md does not state '{total} rules'")


# ------------------------------------------------- 4 test / fix / exception

@section("every C, S and M rule has Test, Fix, Exception")
def check_rule_parts():
    for prefix in ("C", "S", "M"):
        for n, body in rule_sections.get(prefix, {}).items():
            for part in ("**Test:**", "**Fix:**", "**Exception:**"):
                if part not in body:
                    fail(f"{prefix}{n}: missing {part}")


# ------------------------------------------------------- 5 citations exist

CITE = re.compile(r"(?<![A-Za-z0-9/+.-])([CSUM])(\d{1,2})(?![A-Za-z0-9])")


def strip_fences(text: str) -> str:
    return re.sub(r"```.*?```", "", text, flags=re.S)


@section("every cited rule ID exists")
def check_citations():
    for p in ROOT.rglob("*.md"):
        if ".git" in p.parts:
            continue
        text = read(p)
        if p.name == "CONTRIBUTING.md":
            text = strip_fences(text)  # the format template cites a placeholder ID
        for prefix, num in CITE.findall(text):
            if int(num) not in rule_ids.get(prefix, []):
                fail(f"{p.relative_to(ROOT)}: cites {prefix}{num}, which does not exist")


# ---------------------------------------------------------- 6 weights sum

WEIGHTS: dict[str, list[float]] = {}
WEIGHTS_HEADER = re.compile(r"^\|\s*Profile\s*\|\s*Clarity\s*\|")


@section("scoring weight profiles sum to 1.0")
def check_weights():
    text = read(REF / "scoring.md")
    lines = text.splitlines()
    header_idx = None
    for i, line in enumerate(lines):
        if WEIGHTS_HEADER.match(line):
            header_idx = i
            break
    if header_idx is None:
        fail("scoring.md: no weights table found (no 'Profile | Clarity | ...' header)")
        return
    rows_seen = 0
    for line in lines[header_idx + 1:]:
        stripped = line.strip()
        if not stripped.startswith("|"):
            break  # table ended
        cells = [c.strip() for c in stripped.strip("|").split("|")]
        if all(re.fullmatch(r":?-+:?", c) for c in cells):
            continue  # the markdown header-separator row
        rows_seen += 1
        if len(cells) != 6:
            fail(
                f"scoring.md: weights row does not parse (expected 6 cells, "
                f"found {len(cells)}): {stripped!r}"
            )
            continue
        name, *ws = cells
        parsed: list[float] = []
        ok = True
        for c in ws:
            try:
                parsed.append(float(c))
            except ValueError:
                fail(
                    f"scoring.md: weights row for {name!r} has a non-numeric "
                    f"cell {c!r}: {stripped!r}"
                )
                ok = False
                break
        if not ok:
            continue
        WEIGHTS[name] = parsed
        if abs(sum(parsed) - 1.0) > 1e-9:
            fail(f"scoring.md: profile {name} sums to {sum(parsed):.3f}, not 1.0")
    if rows_seen == 0:
        fail("scoring.md: weights table has no data rows")
    if "default" not in WEIGHTS:
        fail("scoring.md: no 'default' weight profile")


# ------------------------------------------------------ 7 worked scores

SUB = [
    re.compile(r"Sentence clarity\s+([\d.]+)"),
    re.compile(r"Flow(?: and cohesion)?\s+([\d.]+)"),
    re.compile(r"Human voice\s+([\d.]+)"),
    re.compile(r"Correctness\s+([\d.]+)"),
    re.compile(r"Precision\s+([\d.]+)"),
]
SCORE_LINE = re.compile(r"Score:\s*([\d.]+)\s*/\s*10\b")


# Files that carry worked scores, and how many each must keep: a worked
# example that disappears should fail the check, not pass it silently.
WORKED_MIN = {
    "skills/en-text/references/scoring.md": 1,
    "skills/en-score/SKILL.md": 1,
    "examples/before-after.md": 2,
}
# Arithmetic written out in prose: "6.9 × 0.25 + ... = 7.63, printed as 7.6".
ARITH = re.compile(
    r"((?:\d+(?:\.\d+)?\s*×\s*\d+(?:\.\d+)?\s*\+\s*)+"
    r"\d+(?:\.\d+)?\s*×\s*\d+(?:\.\d+)?)"
    r"\s*=\s*(\d+(?:\.\d+)?)"
    r"(?:,?\s*(?:reported|printed)\s+as\s+(\d+(?:\.\d+)?))?"
)


@section("worked scores follow from sub-scores and weights")
def check_worked_scores():
    found = 0
    for p in sorted(ROOT.rglob("*.md")):
        if ".git" in p.parts:
            continue
        text = read(p)
        rel = p.relative_to(ROOT)
        for m in SCORE_LINE.finditer(text):
            found += 1
            try:
                stated = Decimal(m.group(1))
            except Exception:
                fail(f"{rel}: 'Score: {m.group(1)} / 10' is not a parsable number")
                continue
            window = text[m.end(): m.end() + 600]
            before = text[: m.start()]
            # the nearest preceding "<profile> weights" mention governs
            profile, last_pos = "default", -1
            for name in WEIGHTS:
                for pm in re.finditer(rf"\b{re.escape(name)} weights\b", before):
                    if pm.start() > last_pos:
                        profile, last_pos = name, pm.start()
            subs = []
            for rx in SUB:
                sm = rx.search(window)
                if not sm:
                    break
                try:
                    subs.append(Decimal(sm.group(1)))
                except Exception:
                    break
            if len(subs) != 5:
                fail(f"{rel}: Score {stated} has no parsable sub-scores")
                continue
            w = [Decimal(str(x)) for x in WEIGHTS.get(profile, [])]
            if len(w) != 5:
                fail(f"{rel}: no weights for profile {profile}")
                continue
            total = sum(s * wi for s, wi in zip(subs, w))
            rounded = total.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)
            if rounded != stated:
                fail(
                    f"{rel}: Score {stated} stated, but {profile} weights give "
                    f"{total:.3f} -> {rounded}"
                )
        want = WORKED_MIN.get(rel.as_posix(), 0)
        have = len(SCORE_LINE.findall(text))
        if have < want:
            fail(f"{rel}: expected at least {want} worked score(s), found {have}")
        for am in ARITH.finditer(text):
            terms = re.findall(r"(\d+(?:\.\d+)?)\s*×\s*(\d+(?:\.\d+)?)", am.group(1))
            total = sum(Decimal(a) * Decimal(b) for a, b in terms)
            stated = Decimal(am.group(2))
            if total.quantize(stated, rounding=ROUND_HALF_UP) != stated:
                fail(f"{rel}: arithmetic '... = {stated}' should be {total}")
            if am.group(3):
                shown = Decimal(am.group(3))
                if total.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP) != shown:
                    fail(f"{rel}: {total} is reported as {shown}, which does not "
                         f"follow by rounding half up")
    if found < sum(WORKED_MIN.values()):
        fail(f"expected at least {sum(WORKED_MIN.values())} worked scores, "
             f"found {found}")


# --------------------------------------------------- 8 the repo's own prose

# S1 tokens that this corpus uses as verbs (as opposed to the adjectives and
# nouns that make up the rest of S1). Only these take verb inflections;
# extend this set when slop.md adds a new verb-type S1 tell. Adjectives
# (robust, seamless, dynamic, ...) have no real-rule -s/-ed/-ing forms, so
# blind suffixing would invent non-words (or, worse, real ones like
# "dynamics" that would false-positive on this repo's own prose).
S1_VERB_TELLS = {
    "delve", "leverage", "utilize", "harness", "showcase", "underscore",
    "unpack", "unlock", "elevate", "empower", "foster", "facilitate",
    "navigate", "spearhead", "streamline", "bolster", "cultivate", "embark",
    "resonate", "illuminate", "amplify", "curate", "champion",
    "usher in", "pave the way",
}


def verb_forms(verb: str) -> set[str]:
    """Real-rule inflections of a regular English verb: -s/-es, -d/-ed, -ing.

    Also generates the -ise spelling for a verb ending in -ize, and inflects
    that too, since both spellings are live in edited English.
    """
    bases = {verb}
    if verb.endswith("ize"):
        bases.add(verb[:-3] + "ise")
    forms: set[str] = set()
    for b in bases:
        forms.add(b)
        if re.search(r"[^aeiou]y$", b):
            stem = b[:-1]
            forms.update({stem + "ies", stem + "ied", b + "ing"})
        elif b.endswith("e") and not b.endswith("ee"):
            forms.update({b + "s", b + "d", b[:-1] + "ing"})
        elif b.endswith(("s", "x", "z", "ch", "sh")):
            forms.update({b + "es", b + "ed", b + "ing"})
        else:
            forms.update({b + "s", b + "ed", b + "ing"})
    return forms


def verb_phrase_forms(phrase: str) -> set[str]:
    """Inflect the first word of a multiword phrasal-verb tell (S1's
    "usher in", "pave the way"): "ushers in", "paved the way", ..."""
    words = phrase.split()
    return {" ".join([f] + words[1:]) for f in verb_forms(words[0])}


def noun_plural(noun: str) -> str:
    """The real-rule plural of a regular English noun."""
    if noun.endswith("s"):
        return noun  # already looks plural; nothing to add
    if re.search(r"[^aeiou]y$", noun):
        return noun[:-1] + "ies"
    if noun.endswith(("x", "z", "ch", "sh")):
        return noun + "es"
    return noun + "s"


def noun_phrase_plural(phrase: str) -> str:
    """The plural of a (possibly multiword) S2 noun tell. The head noun is
    the word right before a trailing preposition ("wealth OF", "testament
    TO"); otherwise it is the last word ("deep DIVE")."""
    words = phrase.split()
    idx = -2 if len(words) > 1 and words[-1] in ("of", "to") else -1
    words[idx] = noun_plural(words[idx])
    return " ".join(words)


def tell_list(prefix_num: str) -> list[str]:
    """Backticked tokens in a rule section, up to its **Test:** line."""
    prefix, num = prefix_num[0], int(prefix_num[1:])
    body = rule_sections[prefix][num]
    body = body.split("**Test:**")[0]
    toks = re.findall(r"`([^`]+)`", body)
    out = []
    for t in toks:
        t = re.sub(r"\s*\(.*?\)\s*$", "", t).strip()
        if t and len(t.split()) <= 3:
            out.append(t.lower())
    return out


def tell_forms(rule_id: str) -> set[str]:
    """Every literal form of a rule's tells: the base word or phrase plus,
    for S1's verbs and S2's nouns, the real-rule inflected forms."""
    forms: set[str] = set()
    for base in tell_list(rule_id):
        forms.add(base)
        if rule_id == "S1" and base in S1_VERB_TELLS:
            words = base.split()
            forms |= verb_phrase_forms(base) if len(words) > 1 else verb_forms(base)
        elif rule_id == "S2":
            forms.add(noun_phrase_plural(base))
    return forms


def running_prose(text: str) -> str:
    text = strip_fences(text)
    # Inline code (mentions): replace with a digit placeholder, not a space.
    # A bare-space replacement would manufacture whitespace next to whatever
    # follows the code span -- "`S14`-`S20`" (tight in the source, no spaces
    # anywhere near the dash) would become " - " (space-dash-space), which
    # reads as D2's spaced-en-dash-as-em-dash tell even though the source
    # never had a space there. A digit is not whitespace (so it can't create
    # that pattern) and is not `[A-Za-z]` (so it never inflates the word
    # count the way a placeholder word would).
    text = re.sub(r"`[^`]*`", "0", text)
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)      # unwrap bold, keep the words
    text = re.sub(
        r"(?<![*\w])\*(?!\s)[^*\n]+?(?<!\s)\*(?![*\w])", " ", text,
    )  # strip true single-asterisk italic mentions only, word-boundary guarded
    lines = [
        ln for ln in text.splitlines()
        if not ln.startswith(">") and not ln.startswith("#") and not ln.startswith("|")
    ]
    return "\n".join(lines)


@section("repo prose passes its own slop and em dash thresholds")
def check_self_slop():
    words = tell_forms("S1") | tell_forms("S2")
    words = {w for w in words if w}
    targets = [
        ROOT / "README.md",
        ROOT / "CONTRIBUTING.md",
        ROOT / "CHANGELOG.md",
        SKILLS / "en-text" / "SKILL.md",
        SKILLS / "en-check" / "SKILL.md",
        SKILLS / "en-score" / "SKILL.md",
        REF / "sources.md",
    ]
    for p in targets:
        prose = running_prose(read(p))
        wc = len(re.findall(r"[A-Za-z][A-Za-z'-]*", prose))
        if wc == 0:
            continue
        hits = []
        for w in words:
            for m in re.finditer(rf"\b{re.escape(w)}\b", prose, re.I):
                hits.append(m.group(0))
        per300 = len(hits) * 300 / wc
        if per300 >= 2:
            fail(f"{p.relative_to(ROOT)}: {len(hits)} vocabulary tells in {wc} words "
                 f"({per300:.1f}/300): {sorted(set(h.lower() for h in hits))}")
        dashes = prose.count("—")
        per500 = dashes * 500 / wc
        if dashes >= 2 and per500 >= 2:
            fail(f"{p.relative_to(ROOT)}: {dashes} em dashes in {wc} words "
                 f"({per500:.1f}/500) exceeds S21")
        # The tell is the both-audiences construction specifically ("Whether
        # you're X OR Y"), not any "whether you" -- an honest conditional
        # ("whether you're not sure, ask") is not S11. Require an "or" within
        # a short same-sentence window after the trigger phrase.
        both = re.search(r"\bwhether you(?:'re| are)\b[^.!?\n]{0,80}\bor\b", prose, re.I)
        if both:
            fail(f"{p.relative_to(ROOT)}: S11 both-audiences construction in own prose")


# ---------------------------------------------------------- 9 README links

@section("local links in README resolve")
def check_links():
    text = read(ROOT / "README.md")
    for label, target in re.findall(r"\[([^\]]+)\]\(([^)]+)\)", text):
        if re.match(r"https?://", target):
            continue
        if not (ROOT / target).exists():
            fail(f"README.md: link '{label}' -> {target} does not exist")


# ------------------------------------------------------- 10 fixtures exist

@section("fixtures named in tests/EVAL.md exist")
def check_fixtures():
    p = ROOT / "tests" / "EVAL.md"
    if not p.exists():
        fail("tests/EVAL.md missing")
        return
    text = read(p)
    names = set(re.findall(r"`(fixtures/[\w.-]+\.md)`", text))
    if not names:
        fail("tests/EVAL.md names no fixtures")
    for n in sorted(names):
        if not (ROOT / "tests" / n).exists():
            fail(f"tests/EVAL.md names {n}, which does not exist")
    for f in sorted((ROOT / "tests" / "fixtures").glob("*.md")):
        if f"fixtures/{f.name}" not in names:
            fail(f"fixture {f.name} exists but tests/EVAL.md does not describe it")


# ------------------------------------------------ 11 rule ranges and counts

RANGE_BACKTICKED = re.compile(r"`([CSUM])(\d{1,2})`\s*[–-]\s*`([CSUM])(\d{1,2})`")
RANGE_BARE = re.compile(r"\b([CSUM])(\d{1,2})\s*[–-]\s*([CSUM])(\d{1,2})\b")
PART_HEADING = re.compile(
    r"^##\s*Part\s+\d+\s*[–—-]\s*.+?\(([CSUM])(\d+)[–-]([CSUM])(\d+)\)\s*$", re.M
)

BARE_N_RULES = re.compile(r"\b(\d+)\s+rules\b")
USAGE_N_RULES = re.compile(r"\b(\d+)\s+usage rules\b")
CSM_N_RULES = re.compile(r"\b(\d+)\s+clarity,\s*slop,?\s*and\s*method rules\b")


def _file_parts(prefix: str, text: str) -> list[tuple[int, int]]:
    """(start, end) for every "## Part N -- Name (Xa-Xb)" heading in one
    reference file, cross-checked against the rule headings actually found
    between it and the next Part heading (or end of file). method.md has
    no Part headings, so this returns [] for "M"."""
    fname = RULE_FILES[prefix]
    matches = list(PART_HEADING.finditer(text))
    parts: list[tuple[int, int]] = []
    for i, m in enumerate(matches):
        p1, n1, p2, n2 = m.groups()
        if p1 != prefix or p2 != prefix:
            fail(f"{fname}: part heading {m.group(0)!r} does not use the {prefix} prefix")
            continue
        start, end = int(n1), int(n2)
        parts.append((start, end))
        section_end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        section_text = text[m.end():section_end]
        actual = sorted(int(n) for p, n, _ in HEADING.findall(section_text) if p == prefix)
        expected = list(range(start, end + 1))
        if actual != expected:
            got = [f"{prefix}{a}" for a in actual] or "none"
            fail(
                f"{fname}: part heading claims {prefix}{start}-{prefix}{end}, but "
                f"the rules found under it are {got}"
            )
    return parts


def _family_bounds() -> dict[str, tuple[set[int], set[int]]]:
    """Per prefix, the legitimate range starts (1 and every part start) and
    legitimate range ends (the family max and every part end). Also runs
    the part-heading-accuracy check above as a side effect, once per file."""
    bounds = {}
    for prefix, fname in RULE_FILES.items():
        valid = rule_ids.get(prefix, [])
        family_max = max(valid) if valid else None
        parts = _file_parts(prefix, strip_fences(read(REF / fname)))
        starts = {1} | {s for s, _ in parts}
        ends = ({family_max} if family_max is not None else set()) | {e for _, e in parts}
        bounds[prefix] = (starts, ends)
    return bounds


def _list_item_skip_map(text: str) -> list[bool]:
    """For each line, whether the paragraph it belongs to opens with a
    bulleted or numbered list marker. A range mention there is *usually* a
    sourced, curated subset of rules ("Williams backs `C1`-`C4`") rather
    than a claim about where a part or the family ends, so a range
    starting at a part/family start is not read as "claims that whole
    stretch" inside one. Continuation lines of a wrapped list item inherit
    the verdict of their opening line.

    This is deliberately not applied to a range that starts at the
    family's first ID and ends only 1-3 short of its last one (see
    check_rule_ranges_and_counts): that shape is a stale full-family claim
    almost every time, not a curated subset, and a genuine attribution
    like `C1`-`C4` (18+ short of a 22-24-rule family) is never mistaken
    for one.
    """
    lines = text.splitlines()
    skip = [False] * len(lines)
    in_paragraph = False
    current = False
    for i, line in enumerate(lines):
        s = line.strip()
        if not s:
            in_paragraph = False
            skip[i] = True
            continue
        if not in_paragraph:
            current = bool(s.startswith("-") or s.startswith("*") or re.match(r"\d+[.)]\s", s))
            in_paragraph = True
        skip[i] = current
    return skip


@section("rule ranges and rule-count totals agree across the repo")
def check_rule_ranges_and_counts():
    # -- part headings must match the rules under them (side effect below),
    #    then: every range mention -- both ends must exist; a range whose
    #    start is a part's (or the family's) first ID must reach some
    #    part's last ID or the family's highest ID. A range that starts
    #    mid-part (C10-C12) only needs both ends to exist.
    bounds = _family_bounds()
    for p in sorted(ROOT.rglob("*.md")):
        if ".git" in p.parts or p.name == "CHANGELOG.md":
            continue  # history may cite ranges that were valid at the time
        rel = p.relative_to(ROOT)
        text = strip_fences(read(p))
        lines = text.splitlines()
        skip_map = _list_item_skip_map(text)
        for i, line in enumerate(lines):
            for rx in (RANGE_BACKTICKED, RANGE_BARE):
                for m in rx.finditer(line):
                    p1, n1, p2, n2 = m.groups()
                    if p1 != p2:
                        continue  # not a same-family range
                    start, end = int(n1), int(n2)
                    valid = rule_ids.get(p1)
                    if not valid:
                        continue
                    mention = m.group(0)
                    if start not in valid:
                        fail(f"{rel}: range {mention!r} starts at {p1}{start}, "
                             f"which does not exist")
                        continue
                    if end not in valid:
                        fail(f"{rel}: range {mention!r} ends at {p1}{end}, "
                             f"which does not exist")
                        continue
                    starts, ends = bounds.get(p1, (set(), set()))
                    if start in starts and end not in ends:
                        family_max = max(valid)
                        # A range starting at the family's very first ID
                        # and landing just short (1-3) of its last one reads
                        # as a stale "the whole family" claim even inside a
                        # list -- unlike a real curated subset, which sits
                        # nowhere near the top.
                        near_full_stale = start == 1 and 0 < family_max - end <= 3
                        if not skip_map[i] or near_full_stale:
                            fail(
                                f"{rel}: range {mention!r} starts a {p1} part (or "
                                f"the family) at {p1}{start}, but {p1}{end} is not "
                                f"any part's last rule or the family's highest ID"
                            )

    # -- "N rules" totals in README.md and the three SKILL.md files
    total = sum(len(v) for v in rule_ids.values())
    u_count = len(rule_ids.get("U", []))
    csm_count = (
        len(rule_ids.get("C", [])) + len(rule_ids.get("S", [])) + len(rule_ids.get("M", []))
    )
    targets = [
        ROOT / "README.md",
        SKILLS / "en-text" / "SKILL.md",
        SKILLS / "en-check" / "SKILL.md",
        SKILLS / "en-score" / "SKILL.md",
    ]
    for p in targets:
        if not p.exists():
            continue
        text = read(p)
        rel = p.relative_to(ROOT)
        for m in CSM_N_RULES.finditer(text):
            n = int(m.group(1))
            if n != csm_count:
                fail(f"{rel}: '{m.group(0)}' does not match C+S+M = {csm_count}")
        for m in USAGE_N_RULES.finditer(text):
            n = int(m.group(1))
            if n != u_count:
                fail(f"{rel}: '{m.group(0)}' does not match U = {u_count}")
        for m in BARE_N_RULES.finditer(text):
            n = int(m.group(1))
            if n != total:
                fail(f"{rel}: '{m.group(0)}' does not match the total {total}")


# --------------------------------------------- 12 no Russian under skills/

@section("no Russian, ru-text or Cyrillic under skills/")
def check_no_russian_in_skills():
    for p in sorted(SKILLS.rglob("*")):
        if p.is_dir() or ".git" in p.parts:
            continue
        try:
            text = read(p)
        except UnicodeDecodeError:
            continue
        rel = p.relative_to(ROOT)
        for m in re.finditer(r"russian|ru-text", text, re.I):
            fail(f"{rel}: contains {m.group(0)!r}, which is forbidden under skills/")
        m = re.search(r"[Ѐ-ӿ]", text)
        if m:
            fail(f"{rel}: contains Cyrillic character {m.group(0)!r}, "
                 f"which is forbidden under skills/")


# --------------------------------------------------- 13 regression guards

@section("no stale 0.3 promise or no-argument-mode promise")
def check_regression_guards():
    for p in ROOT.rglob("*.md"):
        if ".git" in p.parts or p.name == "CHANGELOG.md":
            continue
        text = read(p)
        rel = p.relative_to(ROOT)
        if re.search(r"within about 0\.3", text, re.I):
            fail(f"{rel}: still promises repeatability 'within about 0.3'")

    no_arg_phrases = (
        "most recent English text in the conversation",
        "the last English text in the conversation",
    )
    for p in list(sorted(SKILLS.rglob("*.md"))) + [ROOT / "README.md"]:
        if not p.exists() or ".git" in p.parts:
            continue
        text = read(p)
        rel = p.relative_to(ROOT)
        for phrase in no_arg_phrases:
            if re.search(re.escape(phrase), text, re.I):
                fail(f"{rel}: still promises a no-argument mode ({phrase!r})")


# --------------------------------------------------------------------- main

def main() -> int:
    print(f"en-text corpus checks  ({ROOT})")
    check_manifests()
    check_frontmatter()
    check_rule_ids()
    check_rule_parts()
    check_citations()
    check_weights()
    check_worked_scores()
    check_self_slop()
    check_links()
    check_fixtures()
    check_rule_ranges_and_counts()
    check_no_russian_in_skills()
    check_regression_guards()
    print()
    if errors:
        print(f"{len(errors)} problem(s):")
        for e in errors:
            print(f"  - {e}")
        return 1
    n = sum(len(v) for v in rule_ids.values())
    print(f"all {checks_run} checks passed; {n} rules "
          + ", ".join(f"{k}{len(v)}" for k, v in rule_ids.items()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
