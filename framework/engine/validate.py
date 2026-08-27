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
import json
import subprocess

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required:  pip3 install pyyaml")

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
os.chdir(ROOT)

failures = []
notes = []


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

# The check above compares criterion HEADINGS. It does not read the two other places in the same
# file that also enumerate criteria: the Evaluation Procedure's "Evaluate criteria 1-N" line and
# the worked verdict block's `criteria:` mapping.
#
# Adding a criterion updates the headings, because the author writes a new "# Criterion N" section
# to explain it. It leaves the other two stale, and nothing notices. Three modules were found in
# that state at once, two of them created by an earlier authoring pass that added a criterion and
# updated only module.yaml and the headings.
#
# The cost is not cosmetic. An agent following the Evaluation Procedure literally evaluates the
# range it names, records a pass, and the skipped criteria are never assessed by anyone. A gate
# that can be under-evaluated by reading its own instructions is not a gate.
proc_drift = []
for i, d in modules.items():
    qg = f"modules/{i}/core/11-Quality-Gate.md"
    if not os.path.isfile(qg):
        continue
    body = open(qg, encoding="utf8").read()
    n = len(d.get("gate", []))

    m = re.search(r"Evaluate criteria\s+1\s*[-–—]\s*(\d+)", body)
    if m and int(m.group(1)) != n:
        proc_drift.append(
            f"{i}: Evaluation Procedure says 'criteria 1-{m.group(1)}', module.yaml declares {n}")

    for block in re.findall(r"```yaml\n(.*?)```", body, re.S):
        try:
            parsed = yaml.safe_load(block)
        except yaml.YAMLError:
            continue
        if not isinstance(parsed, dict):
            continue
        g = parsed.get("gate")
        if isinstance(g, dict) and isinstance(g.get("criteria"), dict):
            got = len(g["criteria"])
            # Fewer keys than criteria is the defect: the agent copies this block's shape and the
            # missing criteria are never recorded by anyone. MORE keys is permitted — 04-problem
            # legitimately records `shortfall_declared` alongside its four, because the declared
            # shortfall is a real verdict field and not a gate criterion.
            if got < n:
                proc_drift.append(
                    f"{i}: worked verdict block records {got} criteria, module.yaml declares {n}")
            break
check("11-Quality-Gate.md evaluates every criterion it declares",
      not proc_drift, "\n         ".join(proc_drift[:8]))

# A gate criterion that requires something to be RECORDED needs somewhere in the template to
# record it. Nothing enforced that: gate parity is checked between module.yaml and the
# Quality-Gate file, but neither is checked against 13-Template.md. A criterion could
# therefore be added with no home, and an agent filling every section faithfully would
# satisfy the template and still fail the gate.
#
# Matching criterion wording to section headings cannot be exact, so this REPORTS rather than
# fails. A false positive here would block the build on a synonym; a missed one costs a
# template gap that the authoring checklist also covers.
RECORDING = re.compile(r"\brecorded\b|\bdocumented\b|\blogged\b|\bregistered\b", re.I)
STOP = {"recorded", "documented", "logged", "registered", "before", "research", "begins",
        "which", "would", "these", "their", "there", "with", "that", "this", "each",
        "every", "from", "into", "onto", "than", "then", "when", "what", "make", "made",
        "worth", "doing", "against", "carrying", "marked", "state", "stated"}
template_gaps = []
for i, d in sorted(modules.items()):
    tpl_path = f"modules/{i}/core/13-Template.md"
    if not os.path.isfile(tpl_path):
        continue
    tpl = open(tpl_path, encoding="utf8").read().lower()
    for c in [str(x) for x in d.get("gate", [])]:
        if not RECORDING.search(c):
            continue
        words = {w for w in re.findall(r"[a-z]{5,}", c.lower()) if w not in STOP}
        if words and not any(w in tpl for w in words):
            template_gaps.append(f"{i}: \"{c[:64]}\" has no matching section in 13-Template.md")
if template_gaps:
    notes.append("Gate criteria requiring a recorded output, with no obvious home in the "
                 "module template:\n         " + "\n         ".join(template_gaps[:6]))

# 12-Checklist.md is what an agent works through BEFORE reaching the gate — "the gate should
# confirm what the checklist already established". A criterion with no checklist line is one
# the agent never verifies until the gate rejects it, which inverts that relationship.
#
# This is the same drift the Evaluation-Procedure check catches, one file further on: adding a
# criterion updates module.yaml and the Quality-Gate section, because those are where you are
# already typing. The checklist is a separate file and is silently left behind. Seven criteria
# across five modules were missing a line when this check was written — none of them recent,
# and none of them caught by anything.
#
# Numbering only. The wording is a paraphrase by design, so matching text would produce false
# positives on every well-written checklist.
checklist_gaps = []
for i, d in sorted(modules.items()):
    path = f"modules/{i}/core/12-Checklist.md"
    if not os.path.isfile(path):
        continue
    listed = {int(x) for x in re.findall(r"Criterion (\d+)", open(path, encoding="utf8").read())}
    absent = [n for n in range(1, len(d.get("gate", [])) + 1) if n not in listed]
    if absent:
        one = len(absent) == 1
        checklist_gaps.append(
            f"{i}: criteri{'on' if one else 'a'} {', '.join(map(str, absent))} "
            f"{'has' if one else 'have'} no line in 12-Checklist.md")
check("12-Checklist.md lists every gate criterion", not checklist_gaps,
      "\n         ".join(checklist_gaps[:8]))

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

# ---------------------------------------------------------------- folder layout
# Artifacts are grouped into folders so a builder can open one and be finished with it. A
# folder an artifact names but the layout does not define produces a directory nothing
# describes, no _acceptance.md, and a file the run writes somewhere the manifest never
# declared — which is exactly the unowned-path case the collision check below exists for.
layout = man.get("folder_layout") or {}
declared_folders = [f.get("id") for f in (layout.get("folders") or [])]
check("the manifest declares a folder layout", bool(declared_folders),
      "deliverables/manifest.yaml has no folder_layout.folders — every artifact path would "
      "resolve to the bare deliverables/ root and no folder could carry its acceptance file")

bad_folder = [f"{a['id']}: folder '{a.get('folder')}'" for a in man["artifacts"]
              if a.get("folder") not in declared_folders]
check("every artifact names a folder the layout defines", not bad_folder,
      f"{bad_folder[:8]}\n         declared: {declared_folders}")

# A folder that receives an artifact and no reader is a directory whose purpose the builder
# has to infer from its name.
thin_folders = [f.get("id") for f in (layout.get("folders") or [])
                if not str(f.get("purpose", "")).strip() or not str(f.get("reader", "")).strip()]
check("every declared folder states its purpose and its reader", not thin_folders, thin_folders)

# The folder acceptance file is COPIED from the manifest, so a run needs the shape to copy into.
acc_tpl = layout.get("acceptance_template")
check("the folder acceptance template exists",
      bool(acc_tpl) and os.path.isfile(os.path.join("deliverables/templates", acc_tpl)),
      f"folder_layout.acceptance_template is '{acc_tpl}' — no such file under "
      "deliverables/templates/. Without it a run has nothing to write into each folder")

# A folder declared and never used is not a defect the run can fix — it is a layout that
# describes a package the manifest does not produce.
used_folders = {a.get("folder") for a in man["artifacts"]}
unused = [f for f in declared_folders if f not in used_folders]
check("every declared folder receives at least one artifact", not unused,
      f"{unused} — declared in folder_layout and claimed by no artifact")

# The manifest OWNS every path it declares, and a run writes into a directory that is not
# under version control. Two artifacts sharing a filename means the second silently destroys
# the first, and the loss is undetectable afterwards because the file is present and
# well-formed. A completed run lost a deliverable exactly this way — one collision out of
# fourteen filenames, discovered after the original was unrecoverable.
#
# Here the collision is cheap to prevent; in a run it is not repairable at all.
#
# Folders add a second way to collide and remove none of the first. Two artifacts may not
# share a full path, and they may not share a BARE FILENAME either even in different folders:
# the number in `03-PRD.md` is the document's identity in every cross-reference the framework
# carries, and a second file by that name makes every one of those citations ambiguous.
seen, by_name, collisions = {}, {}, []
for a in man["artifacts"]:
    f = a["file"]
    path = f"{a['folder']}/{f}" if a.get("folder") else f
    if path in seen:
        collisions.append(f"deliverables/{path}: claimed by both {seen[path]} and {a['id']}")
    seen[path] = a["id"]
    if f in by_name:
        collisions.append(f"{f}: used by both {by_name[f]} and {a['id']} — filenames are the "
                          "identity used by cross-references and must be unique across folders")
    by_name[f] = a["id"]

comp_paths = {}
for a in man.get("completion_artifacts") or []:
    p = str(a.get("path", "")).rstrip("/")
    if p.startswith("deliverables/") and p.split("/", 1)[1] in seen:
        collisions.append(f"{p}: completion artifact {a['id']} collides with deliverable "
                          f"{seen[p.split('/', 1)[1]]}")
    if p in comp_paths:
        collisions.append(f"{p}: claimed by completion artifacts {comp_paths[p]} and {a['id']}")
    comp_paths[p] = a["id"]
check("no two manifest artifacts claim the same path", not collisions, collisions[:6])

# ---------------------------------------------------------------- completion artifacts
# One artifact per audience — decision maker, engineering team, AI implementation agent.
# They live outside deliverables/, so none of the checks above reaches them, and a missing
# template or method file would surface only when a run tried to produce one.
completion = man.get("completion_artifacts") or []
check("completion artifacts declared (one per audience)", len(completion) >= 3,
      f"found {len(completion)} — the manifest declares fewer than the three audiences")

comp_problems = []
for a in completion:
    aid = a.get("id", "<no id>")
    for field in ("path", "format", "template", "method", "audience", "acceptance"):
        if not a.get(field):
            comp_problems.append(f"{aid}: no {field}")
    tpl = a.get("template")
    if tpl and not os.path.isfile(os.path.join("deliverables/templates", tpl)):
        comp_problems.append(f"{aid}: template deliverables/templates/{tpl} does not exist")
    meth = a.get("method")
    if meth and not os.path.isfile(meth):
        comp_problems.append(f"{aid}: method {meth} does not exist")
    if str(a.get("path", "")).startswith(("/", "..")):
        comp_problems.append(f"{aid}: path must be relative to the run root")
check("every completion artifact has a template, a method and acceptance criteria",
      not comp_problems, comp_problems[:10])

# The manifest version is what lets an older run be judged against the contract it was
# produced under rather than this one. Without the field in the schema, that is impossible
# and every completed run has to be rewritten whenever the manifest grows.
schema_txt = open("engine/state-schema.yaml", encoding="utf8").read()
check("state schema records the manifest version a run was produced under",
      "framework_version" in schema_txt,
      "engine/state-schema.yaml has no framework_version — completed runs cannot be "
      "exempted from checks introduced after them")

check("state schema records the era its own checks are gated on",
      "version: 2" in schema_txt.split("\n\n")[0] or schema_txt.lstrip().startswith("#"),
      "engine/state-schema.yaml must carry a top-level `version` — it is what lets a new "
      "REQUIRED key be added without retroactively invalidating a completed run")

run_order = open("engine/run-order.yaml", encoding="utf8").read()
absent = [i for i in modules if i not in run_order]
check("run-order references every module", not absent, absent)

# The manifest decides which completion artifacts are OWED. run-order.yaml is what an agent
# actually walks at the end of a run. When the two disagree the artifact is simply never
# produced, the run reports success, and the omission surfaces only when someone goes looking
# for a file they were told exists.
#
# run-order listed three methods while the manifest declared five, for as long as both files
# existed. Neither document is wrong on its own face, which is why nobody noticed.
unrouted = [f"{a['id']} -> {a['method']}" for a in completion
            if a.get("method") and a["method"] not in run_order]
check("every completion artifact's method is routed from the run order", not unrouted,
      f"{unrouted}\n         declared in deliverables/manifest.yaml and named nowhere in "
      "engine/run-order.yaml — an agent walking the run order never produces these")

# An engine method file nothing points at is a file no agent will ever open. The run skill
# and AGENTS.md route the agent through engine/; a method added without a route is authored
# work that never executes.
engine_docs = sorted(f for f in os.listdir("engine") if f.endswith(".md"))
routable = []
for base in (".", ".."):
    for dirpath, dirs, files in os.walk(base):
        dirs[:] = [d for d in dirs if d not in (".git", "projects", "examples", "node_modules")]
        for f in files:
            if f.endswith((".md", ".yaml", ".yml", ".py")):
                routable.append(os.path.normpath(os.path.join(dirpath, f)))
orphan_docs = []
for d in engine_docs:
    me = os.path.normpath(os.path.join("engine", d))
    if not any(d in open(p, encoding="utf8", errors="ignore").read()
               for p in routable if os.path.normpath(p) != me):
        orphan_docs.append(f"engine/{d}")
check("every engine method file is referenced from somewhere an agent reads",
      not orphan_docs,
      f"{orphan_docs} — nothing routes an agent to these, so they will not be read")

# ---------------------------------------------------------------- frontmatter
# A Prerequisite is either a path that resolves, or a semantic precondition
# of the form "<module> gate passed". Paths resolve relative to modules/,
# constitution/, the framework root, or the citing file's own directory.
SEMANTIC = re.compile(r"gate[s]? passed")
def exists_exact(path):
    """os.path.isfile with the case sensitivity of the strictest filesystem.

    macOS and Windows resolve `01-Idea/README.md` against a directory named
    `01-idea`; Linux does not. So a reference authored on a laptop passes every
    local check and fails in CI — or, worse, fails for a user on Linux while the
    maintainer cannot reproduce it. Four Prerequisites shipped with exactly this
    defect and only the Ubuntu runner ever saw them.

    Checked here rather than trusted to CI, because the point of a local
    validator is that the author finds their own defect.
    """
    if not os.path.isfile(path):
        return False
    cur = os.path.abspath(path)
    stop = os.path.abspath(ROOT)
    while cur != stop and os.path.dirname(cur) != cur:
        parent, name = os.path.split(cur)
        try:
            if name not in os.listdir(parent):
                return False
        except OSError:
            return False
        cur = parent
    return True


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
        if not any(exists_exact(os.path.normpath(os.path.join(b, p))) for b in bases):
            unresolved.append(f"{f} -> {p}")

check(f"all path Prerequisites resolve ({semantic_count} semantic preconditions)",
      not unresolved, unresolved[:10])
check("no vague non-path Prerequisites", not vague, vague[:10])
check("no stale directory or module identifiers", not stale_ids, stale_ids[:10])

# The skills are the shipped interface. A broken name or a missing description
# means the skill silently does not load, and the repository looks inert.
skill_problems = []
skills = sorted(glob.glob("../skills/*/SKILL.md"))
if not skills:
    skill_problems.append("no skills found under skills/")
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

# A skill that rewrites itself during a run makes every installation diverge and
# conflicts on `git pull`. Editors and hooks inject these blocks automatically,
# so this is checked rather than trusted. Changes to a skill belong in a commit.
SELF_MOD = re.compile(r"self-learning mode|improves? itself|update this skill|rewrite this skill", re.I)
self_mod = []
for sf in skills:
    for n, line in enumerate(open(sf, encoding="utf8"), 1):
        if SELF_MOD.search(line):
            self_mod.append(f"{sf}:{n}: {line.strip()[:70]}")
check("no self-modification instructions in skills", not self_mod, self_mod[:10])

# gates.yaml owns the controlled vocabularies — the six failure classes and the three
# question classes. The skills quote them so the operator meets them in plain language, and a
# quoted vocabulary is a second copy: rename a class here and the skill keeps instructing an
# agent to record a value validate-run.py will reject.
#
# This is the same defect the failure-class work exists to fix, one level up. Two homes for
# one record means the unchecked one goes stale, and the run only finds out when a validator
# fails at delivery.
#
# Checked FORWARD — every declared value must appear in a skill — not backward. Scanning the
# skills for unknown tokens looked equivalent and was not: gates.yaml discusses its own class
# names in prose, so a renamed class stays "known" via the sentence warning against confusing
# it with another, and the check passes while the skill teaches a value the validator rejects.
#
# Forward, a rename fails twice over: the old name is gone from the vocabulary, and the new
# name is in no skill. Both halves point at the edit that was left half-done.
gates_path = "engine/gates.yaml"
vocab, undocumented = {}, []
if os.path.isfile(gates_path):
    _g = yaml.safe_load(open(gates_path, encoding="utf8")) or {}
    for group in ("failure_classes", "operator_question_classes"):
        vocab[group] = set((_g.get(group) or {}).get("values", {}) or {})

skill_text = "\n".join(open(sf, encoding="utf8").read() for sf in skills)
for group, values in vocab.items():
    for v in sorted(values):
        if f"`{v}`" not in skill_text:
            undocumented.append(f"{group}: `{v}` is declared in gates.yaml and quoted in no "
                                "skill — an agent is never told the value exists")
check("every controlled-vocabulary value reaches the skill that has to teach it",
      not undocumented, undocumented[:10])

# Runs are private. The framework is open; the research people put through it is
# not. .gitignore excludes projects/ and examples/, but a `git add -f`, a merge,
# or a file committed before the ignore rule existed all bypass it silently — and
# the leak is someone's unreleased strategy, not a stray build artifact.
tracked_runs = []
try:
    out = subprocess.run(["git", "ls-files", "projects", "examples"],
                         cwd="..", capture_output=True, text=True, timeout=20)
    if out.returncode == 0:
        tracked_runs = [f for f in out.stdout.split()
                        if os.path.basename(f) != "README.md"]
except Exception:
    pass  # not a git checkout, or git unavailable — nothing to leak from
check("no run content tracked by git", not tracked_runs, tracked_runs[:10])

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

# ------------------------------------------------- framework path portability
# EVERY framework path must be written repo-relative — `framework/engine/gates.yaml`.
# The skills and AGENTS.md teach exactly one resolution rule: strip the leading
# `framework/` and prefix the absolute path resolved at startup.
#
# WHY THIS IS CHECKED RATHER THAN TRUSTED. In-repo the working directory IS the
# repository, so `./framework/x`, `../framework/x` and `framework/x` all open the
# same file and nothing looks wrong. Installed as a plugin the working directory is
# the OPERATOR'S PROJECT, where nothing named `framework/` exists — and only the
# canonical form survives the one rule an agent was taught.
#
# The failure is silent and it is the worst kind: a gate criterion points at a
# method document, the read returns nothing, and the run continues without the
# method. It reaches delivery having skipped the document that would have failed
# it, and every artifact looks complete. This is the U7 defect class — a rule
# stated everywhere and enforced nowhere — reproduced in the framework's own
# plumbing, so it gets the framework's own answer: name the enforcement point.
BAD_FW_PATH = re.compile(r"(?<![\w/`.-])(?:\./|\.\./|~/|/)+framework/(?![a-z-]*\.\.\.)")
bad_paths = []
for f in glob.glob("**/*.md", recursive=True) + glob.glob("**/*.yaml", recursive=True):
    for n, line in enumerate(open(f, encoding="utf8", errors="ignore"), 1):
        hit = BAD_FW_PATH.search(line)
        if hit:
            bad_paths.append(f"{f}:{n}: {hit.group(0)} — write it as `framework/…`")
for f in ("../AGENTS.md",):
    if os.path.isfile(f):
        for n, line in enumerate(open(f, encoding="utf8", errors="ignore"), 1):
            hit = BAD_FW_PATH.search(line)
            if hit and "$CLAUDE_PLUGIN_ROOT" not in line and "$PIOS_HOME" not in line:
                bad_paths.append(f"{f}:{n}: {hit.group(0)} — write it as `framework/…`")
check("every framework path is written repo-relative (portable to plugin install)",
      not bad_paths, bad_paths[:10])

# The resolution rule itself must reach an agent, in both places one starts reading.
# Without it, the canonical form above is a convention nobody was told how to apply.
rule_missing = []
for f, label in (("../AGENTS.md", "AGENTS.md"), ("../skills/pios/SKILL.md", "skills/pios")):
    if not os.path.isfile(f):
        rule_missing.append(f"{label}: missing")
        continue
    body = open(f, encoding="utf8").read()
    if "CLAUDE_PLUGIN_ROOT" not in body:
        rule_missing.append(f"{label}: never checks CLAUDE_PLUGIN_ROOT — plugin installs "
                            "cannot locate the framework")
check("plugin-mode framework resolution is taught where agents start reading",
      not rule_missing, rule_missing)

# Four files declare the release version and a package manager reads each of them. They
# drift silently: a bump touches the one you remembered, and an install serves a version
# string that disagrees with the tag it came from. This is the same drift class the manifest
# and module gates are checked for — it just crosses out of the framework into distribution.
version_files = {
    "../.claude-plugin/plugin.json":      lambda d: d.get("version"),
    "../.claude-plugin/marketplace.json": lambda d: (d.get("plugins") or [{}])[0].get("version"),
    "../package.json":                    lambda d: d.get("version"),
    "../gemini-extension.json":           lambda d: d.get("version"),
}
found, version_problems = {}, []
for path, get in version_files.items():
    if not os.path.isfile(path):
        version_problems.append(f"{os.path.basename(path)}: missing — the install manifests "
                                "are part of the shipped interface")
        continue
    try:
        found[os.path.basename(path)] = get(json.load(open(path, encoding="utf8")))
    except Exception as e:
        version_problems.append(f"{os.path.basename(path)}: does not parse — {e}")
if len(set(found.values())) > 1:
    version_problems.append("versions disagree: "
                            + ", ".join(f"{k}={v}" for k, v in sorted(found.items())))
check(f"install manifests agree on one version ({sorted(set(found.values()))[0] if len(set(found.values())) == 1 else 'drift'})",
      not version_problems, version_problems)

# ---------------------------------------------------------------- result
print()
for n in notes:
    print(f"  note   {n}")
if notes:
    print()
if failures:
    print(f"  {len(failures)} check(s) failed.")
    sys.exit(1)
print("  All structural checks pass.")
