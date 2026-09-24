#!/usr/bin/env python3
"""Structural checks for the en-text corpus.

Standard library only. Exit code 1 on any failure.

What is checked:
  1. Plugin manifests parse, and their versions agree with the changelog.
  2. Every skill has valid frontmatter; the review skills cannot write files.
  3. Rule IDs in each reference file are sequential and unique, and the
     counts match what SKILL.md and README claim.
  4. Every clarity (C) and slop (S) rule has a Test, a Fix, and an Exception.
  5. Every rule ID cited anywhere in the repo exists.
  6. Every scoring weight profile sums to 1.0.
  7. Every worked score in the repo follows from its sub-scores and weights.
  8. The repo's own prose passes its own slop density and em dash thresholds.
  9. Local links in README resolve.
 10. Fixtures named in tests/EVAL.md exist.
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


@section("skill frontmatter valid; review skills cannot write")
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
            allowed = fm.get("allowed-tools", "")
            for bad in ("Write", "Edit", "Bash", "PowerShell"):
                if re.search(rf"\b{bad}\b", allowed):
                    fail(f"{d.name}: allowed-tools must not include {bad}")
            disallowed = fm.get("disallowed-tools", "")
            for must in ("Write", "Edit"):
                if not re.search(rf"\b{must}\b", disallowed):
                    fail(f"{d.name}: disallowed-tools must include {must}")


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


@section("scoring weight profiles sum to 1.0")
def check_weights():
    text = read(REF / "scoring.md")
    rows = re.findall(
        r"^\| ([a-z-]+) \| ([\d.]+) \| ([\d.]+) \| ([\d.]+) \| ([\d.]+) \| ([\d.]+) \|$",
        text, re.M,
    )
    if not rows:
        fail("scoring.md: no weight profile rows found")
    for name, *ws in rows:
        w = [float(x) for x in ws]
        WEIGHTS[name] = w
        if abs(sum(w) - 1.0) > 1e-9:
            fail(f"scoring.md: profile {name} sums to {sum(w):.3f}, not 1.0")
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


@section("worked scores follow from sub-scores and weights")
def check_worked_scores():
    files = [
        REF / "scoring.md",
        SKILLS / "en-score" / "SKILL.md",
        ROOT / "examples" / "before-after.md",
    ]
    found = 0
    for p in files:
        text = read(p)
        for m in re.finditer(r"Score: ([\d.]+) / 10", text):
            found += 1
            stated = Decimal(m.group(1))
            window = text[m.end(): m.end() + 600]
            before = text[: m.start()]
            # the nearest preceding "<profile> weights" mention governs
            profile, last_pos = "default", -1
            for name in WEIGHTS:
                for pm in re.finditer(rf"\b{name} weights\b", before):
                    if pm.start() > last_pos:
                        profile, last_pos = name, pm.start()
            subs = []
            for rx in SUB:
                sm = rx.search(window)
                if not sm:
                    break
                subs.append(Decimal(sm.group(1)))
            if len(subs) != 5:
                fail(f"{p.name}: Score {stated} has no parsable sub-scores")
                continue
            w = [Decimal(str(x)) for x in WEIGHTS.get(profile, [])]
            if len(w) != 5:
                fail(f"{p.name}: no weights for profile {profile}")
                continue
            total = sum(s * wi for s, wi in zip(subs, w))
            rounded = total.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)
            if rounded != stated:
                fail(
                    f"{p.name}: Score {stated} stated, but {profile} weights give "
                    f"{total:.3f} -> {rounded}"
                )
    if found < 3:
        fail(f"expected at least 3 worked scores, found {found}")


# --------------------------------------------------- 8 the repo's own prose

def tell_list(prefix_num: str) -> list[str]:
    """Backticked tokens in a rule section, up to its **Test:** line."""
    prefix, num = prefix_num[0], int(prefix_num[1:])
    body = rule_sections[prefix][num]
    body = body.split("**Test:**")[0]
    toks = re.findall(r"`([^`]+)`", body)
    out = []
    for t in toks:
        t = re.sub(r"\s*\(.*?\)\s*$", "", t).strip()
        if t and " " not in t or len(t.split()) <= 3:
            out.append(t.lower())
    return out


def running_prose(text: str) -> str:
    text = strip_fences(text)
    text = re.sub(r"`[^`]*`", " ", text)          # inline code (mentions)
    text = re.sub(r"\*[^*\n]+\*", " ", text)       # italic mentions
    lines = [
        ln for ln in text.splitlines()
        if not ln.startswith(">") and not ln.startswith("#") and not ln.startswith("|")
    ]
    return "\n".join(lines)


@section("repo prose passes its own slop and em dash thresholds")
def check_self_slop():
    words = set(tell_list("S1")) | set(tell_list("S2"))
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
        both = re.search(r"\bwhether you(?:'re| are)\b", prose, re.I)
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
