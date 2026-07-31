#!/usr/bin/env python3
"""
Product Intelligence OS — structural validator.

Run from the repository root:

    python3 framework/engine/validate.py

Checks the machine-readable contract only. It does not judge writing quality —
that is what `framework/AUTHORING.md` and the review loop are for.

Exit code 0 = all checks pass. Non-zero = at least one check failed.
"""

import os
import re
import sys
import glob

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required:  pip3 install pyyaml")

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
os.chdir(ROOT)

failures = []


def check(label, ok, detail=""):
    print(("  PASS  " if ok else "  FAIL  ") + label + ("" if ok else "\n         " + str(detail)))
    if not ok:
        failures.append(label)


# ---------------------------------------------------------------- yaml parses
yaml_files = sorted(glob.glob("**/*.yaml", recursive=True))
unparseable = []
for f in yaml_files:
    try:
        yaml.safe_load(open(f, encoding="utf8"))
    except Exception as e:
        unparseable.append(f"{f}: {str(e).splitlines()[0]}")
check(f"all {len(yaml_files)} yaml files parse", not unparseable, "\n         ".join(unparseable))

if unparseable:
    print("\n  Cannot continue while module.yaml files are unparseable.")
    sys.exit(1)

modules = {}
for f in sorted(glob.glob("modules/*/module.yaml")):
    d = yaml.safe_load(open(f, encoding="utf8"))
    modules[d["id"]] = d

# ---------------------------------------------------------------- structure
check("14 modules present", len(modules) == 14, sorted(modules))

CORE = ["00-Purpose", "03-Core-Principles", "04-Mental-Models", "05-Best-Practices",
        "06-Framework", "07-Workflow", "08-Questions-To-Answer", "09-Research-Methodology",
        "11-Quality-Gate", "12-Checklist", "13-Template"]
LEARN = ["01-Why-It-Matters", "02-Learning-Objectives", "10-Common-Mistakes", "16-Evaluation",
         "17-Reflection", "19-Related-Modules", "20-Future-Improvements", "README"]
RESOURCES = ["14-Examples", "15-Anti-Examples", "18-References"]

missing = []
for m in modules:
    for name in CORE:
        if not os.path.isfile(f"modules/{m}/core/{name}.md"):
            missing.append(f"modules/{m}/core/{name}.md")
    for name in LEARN:
        if not os.path.isfile(f"modules/{m}/learn/{name}.md"):
            missing.append(f"modules/{m}/learn/{name}.md")
    for name in RESOURCES:
        if not os.path.isfile(f"modules/{m}/resources/{name}.md"):
            missing.append(f"modules/{m}/resources/{name}.md")
check("every module has its required core / learn / resources files", not missing, missing[:10])

empty = [f for f in glob.glob("**/*.md", recursive=True) if os.path.getsize(f) == 0]
check("no empty markdown files", not empty, empty[:10])

# ---------------------------------------------------------------- dependency graph
produces = {}
for i, d in modules.items():
    for p in d.get("produces", []):
        produces.setdefault(p, []).append(i)

orphan_consumes = [(i, c) for i, d in modules.items() for c in d.get("consumes", [])
                   if c not in produces and not c.startswith("state.")]
check("every `consumes` has a producer", not orphan_consumes, orphan_consumes)

incomplete = []
for i, d in modules.items():
    need = {s for c in d.get("consumes", []) for s in produces.get(c, [])} - {i}
    gap = sorted(need - set(d.get("depends_on", [])))
    if gap:
        incomplete.append((i, gap))
check("`depends_on` lists every module it consumes from", not incomplete, incomplete)

forward = [(i, x) for i, d in modules.items() for x in d.get("depends_on", []) if x >= i]
check("no module depends on a later module", not forward, forward)

# AUTHORING.md requires the criteria in 11-Quality-Gate.md to match module.yaml exactly.
# Drift here means the agent reads one list and is judged against another.
gate_drift = []
for i, d in modules.items():
    qg = f"modules/{i}/core/11-Quality-Gate.md"
    if not os.path.isfile(qg):
        gate_drift.append(f"{i}: 11-Quality-Gate.md missing")
        continue
    documented = re.findall(r"^# Criterion \d+ — (.+?)\s*$", open(qg, encoding="utf8").read(), re.M)
    declared = [str(c) for c in d.get("gate", [])]
    norm = lambda s: re.sub(r"\s+", " ", s).strip().rstrip(".")
    missing = [c for c in declared if norm(c) not in [norm(x) for x in documented]]
    extra = [c for c in documented if norm(c) not in [norm(x) for x in declared]]
    if missing:
        gate_drift.append(f"{i}: in module.yaml but not documented -> {missing}")
    if extra:
        gate_drift.append(f"{i}: documented but not in module.yaml -> {extra}")
check("module.yaml gate criteria match 11-Quality-Gate.md", not gate_drift, "\n         ".join(gate_drift[:6]))

unresolved_fail = [(i, d.get("on_fail")) for i, d in modules.items()
                   if not any(x in str(d.get("on_fail", "")) for x in modules)
                   and "halt" not in str(d.get("on_fail", ""))]
check("every `on_fail` names a real module or halts", not unresolved_fail, unresolved_fail)

# ---------------------------------------------------------------- deliverables
man = yaml.safe_load(open("deliverables/manifest.yaml", encoding="utf8"))
artifacts = {a["id"]: a for a in man["artifacts"]}

mismatch = []
for aid, a in artifacts.items():
    for m in a.get("fed_by", []):
        if m == "all":
            continue
        if m not in modules:
            mismatch.append(f"artifact {aid}: fed_by unknown module {m}")
        elif aid not in modules[m].get("feeds_deliverables", []):
            mismatch.append(f"{aid}.fed_by has {m}, but {m}.feeds_deliverables does not")
for i, d in modules.items():
    for aid in d.get("feeds_deliverables", []):
        if aid not in artifacts:
            mismatch.append(f"{i}.feeds_deliverables names unknown artifact {aid}")
        elif i not in artifacts[aid].get("fed_by", []):
            mismatch.append(f"{i}.feeds_deliverables has {aid}, but {aid}.fed_by does not")
check("manifest `fed_by` and module `feeds_deliverables` agree", not mismatch, mismatch[:10])

no_template = [a["file"] for a in man["artifacts"]
               if not os.path.isfile(os.path.join("deliverables/templates", a["file"]))]
check("every artifact has its template file", not no_template, no_template)

# An artifact without acceptance criteria cannot fail its own gate, which makes it
# undeliverable in the only sense the framework cares about.
no_acceptance = [a["id"] for a in man["artifacts"] if not a.get("acceptance")]
check("every artifact has acceptance criteria", not no_acceptance, no_acceptance)

no_audience = [a["id"] for a in man["artifacts"] if not a.get("audience")]
check("every artifact names its audience", not no_audience, no_audience)

run_order = open("engine/run-order.yaml", encoding="utf8").read()
absent = [i for i in modules if i not in run_order]
check("run-order references every module", not absent, absent)

# ---------------------------------------------------------------- frontmatter
# A Prerequisite is either a path that resolves, or a semantic precondition
# of the form "<module> gate passed". Paths resolve relative to modules/,
# constitution/, the framework root, or the citing file's own directory.
SEMANTIC = re.compile(r"gate[s]? passed")
unresolved, vague, semantic_count = [], [], 0
stale_ids = []

for f in glob.glob("**/*.md", recursive=True):
    text = open(f, encoding="utf8").read()
    if re.search(r"00-AI-Constitution|^Module: 01-Idea$", text, re.M):
        stale_ids.append(f)
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        continue
    block = re.search(r"^Prerequisites:\n((?:  - .*\n)+)", m.group(1), re.M)
    if not block:
        continue
    here = os.path.dirname(f)
    for line in block.group(1).strip().split("\n"):
        p = line.strip()[2:].strip()
        if not p.endswith((".md", ".yaml")):
            semantic_count += 1
            if not SEMANTIC.search(p):
                vague.append(f"{f} -> {p}")
            continue
        bases = ("modules", ".", "constitution", here)
        if not any(os.path.isfile(os.path.normpath(os.path.join(b, p))) for b in bases):
            unresolved.append(f"{f} -> {p}")

check(f"all path Prerequisites resolve ({semantic_count} semantic preconditions)",
      not unresolved, unresolved[:10])
check("no vague non-path Prerequisites", not vague, vague[:10])
check("no stale directory or module identifiers", not stale_ids, stale_ids[:10])

# The skills are the shipped interface. A broken name or a missing description
# means the skill silently does not load, and the repository looks inert.
skill_problems = []
skills = sorted(glob.glob("../.claude/skills/*/SKILL.md"))
if not skills:
    skill_problems.append("no skills found under .claude/skills/")
for sf in skills:
    directory = os.path.basename(os.path.dirname(sf))
    m = re.match(r"^---\n(.*?)\n---\n", open(sf, encoding="utf8").read(), re.S)
    if not m:
        skill_problems.append(f"{directory}: no frontmatter")
        continue
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except Exception as e:
        skill_problems.append(f"{directory}: frontmatter does not parse — {e}")
        continue
    if fm.get("name") != directory:
        skill_problems.append(f"{directory}: name is '{fm.get('name')}' — must match the directory")
    if not str(fm.get("description", "")).strip():
        skill_problems.append(f"{directory}: no description — it will never be matched")
check(f"Claude Code skills valid ({len(skills)} found)", not skill_problems, skill_problems)

placeholders = [f for f in glob.glob("**/*.md", recursive=True)
                if re.search(r"^(Created|Last Updated):\s*YYYY-MM-DD", open(f, encoding="utf8").read(), re.M)]
check("no YYYY-MM-DD frontmatter placeholders", not placeholders, placeholders[:10])

# ---------------------------------------------------------------- house style
# NOTE: "analyses" is the correct American plural of "analysis" and is not listed.
# Only the verb forms are British.
BRITISH = re.compile(
    r"\b(analyse|analysed|analysing|organis\w+|behaviour\w*|colour\w*|licence|favour\w*|labour\w*|"
    r"prioritis\w+|recognis\w+|programme|whilst|amongst|sceptic\w*|defence|catalogue|"
    r"modelling|judgement)\b", re.I)
british = []
for f in glob.glob("**/*.md", recursive=True):
    for n, line in enumerate(open(f, encoding="utf8"), 1):
        hit = BRITISH.search(line)
        if hit:
            british.append(f"{f}:{n} {hit.group(0)}")
check("American spelling throughout", not british, british[:10])

# ---------------------------------------------------------------- result
print()
if failures:
    print(f"  {len(failures)} check(s) failed.")
    sys.exit(1)
print("  All structural checks pass.")
