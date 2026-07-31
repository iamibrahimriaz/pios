#!/usr/bin/env python3
"""
Product Intelligence OS — completed-run validator.

    python3 framework/engine/validate-run.py projects/<slug>

Checks a finished run against the contract: every required artifact present,
no template scaffolding left behind, claims tagged, gates recorded, and the
two chains the framework depends on actually carried.

This is the defense that does not rely on the operator being careful. The
framework's structural validator (validate.py) checks the framework itself;
this checks the output of using it.

Exit code 0 = deliverable. Non-zero = at least one check failed.
"""

import os
import re
import sys
import glob

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required:  pip3 install pyyaml")

if len(sys.argv) != 2:
    sys.exit(__doc__)

RUN = os.path.abspath(sys.argv[1])
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
FRAMEWORK = os.path.join(ROOT, "framework")

if not os.path.isdir(RUN):
    sys.exit(f"No such run directory: {RUN}")

failures = []
notes = []


def check(label, ok, detail=""):
    print(("  PASS  " if ok else "  FAIL  ") + label + ("" if ok else "\n         " + str(detail)))
    if not ok:
        failures.append(label)


print(f"\n  Run: {RUN}\n")

# ------------------------------------------------------------------ state
state_path = os.path.join(RUN, "state.yaml")
check("state.yaml exists", os.path.isfile(state_path))
if not os.path.isfile(state_path):
    sys.exit(1)

try:
    state = yaml.safe_load(open(state_path, encoding="utf8")) or {}
    parsed = True
except Exception as e:
    state, parsed = {}, False
check("state.yaml parses", parsed, "" if parsed else "invalid YAML")

raw = (state.get("project") or {}).get("raw_idea", "")
check("the operator's raw idea is recorded", bool(str(raw).strip()),
      "state.project.raw_idea is empty — it must be the operator's original words")

juris = (state.get("project") or {}).get("jurisdiction", "")
check("jurisdiction is set", bool(str(juris).strip()),
      "01-idea's gate requires it; without it the regulatory research is unanchored")

# ------------------------------------------------------------------ artifacts
man = yaml.safe_load(open(os.path.join(FRAMEWORK, "deliverables/manifest.yaml"), encoding="utf8"))
dl_dir = os.path.join(RUN, "deliverables")
required = [a for a in man["artifacts"] if a.get("required")]

missing = [a["file"] for a in required if not os.path.isfile(os.path.join(dl_dir, a["file"]))]
check(f"all {len(required)} required artifacts present", not missing, missing)

present = [a for a in man["artifacts"] if os.path.isfile(os.path.join(dl_dir, a["file"]))]
if not present:
    print("\n  No artifacts to inspect.")
    sys.exit(1)


def body(a):
    return open(os.path.join(dl_dir, a["file"]), encoding="utf8").read()


# ------------------------------------------------------------------ scaffolding
left = {"«placeholder»": [], "<!-- fill": [], "<!-- ACCEPTANCE": []}
for a in present:
    t = body(a)
    if re.search(r"«[^»]*»", t):
        left["«placeholder»"].append(a["file"])
    if "<!-- fill" in t:
        left["<!-- fill"].append(a["file"])
    if "<!-- ACCEPTANCE" in t:
        left["<!-- ACCEPTANCE"].append(a["file"])

for marker, files in left.items():
    check(f"no {marker} scaffolding remains", not files, files[:6])

# ------------------------------------------------------------------ evidence
TAG = re.compile(r"\[(verified|inferred|assumption)\b")
untagged = []
for a in present:
    t = body(a)
    if a["id"] in ("build-handoff", "engineering-setup", "api-contract", "data-model"):
        continue  # specification artifacts, not claim-bearing prose
    if not TAG.search(t):
        untagged.append(a["file"])
check("every claim-bearing artifact carries evidence tags", not untagged,
      f"no tag found in: {untagged}")

log = state.get("evidence_log") or []
check("evidence log is populated", bool(log),
      "state.evidence_log is empty — nothing downstream can be audited")

if log:
    bad_tag = [e.get("claim", "?") for e in log if e.get("tag") not in ("verified", "inferred", "assumption")]
    check("every evidence entry has exactly one valid tag", not bad_tag, bad_tag[:5])

    lb = [e for e in log if e.get("load_bearing")]
    check("at least one claim is marked load-bearing", bool(lb),
          "no entry carries load_bearing — the run cannot say what it rests on")

    verified_no_source = [e.get("claim", "?") for e in log
                          if e.get("tag") == "verified" and not str(e.get("source", "")).strip()]
    check("every [verified] claim names a source", not verified_no_source, verified_no_source[:5])

# ------------------------------------------------------------------ assumptions
assumptions = state.get("assumptions") or []
check("open assumptions are recorded", bool(assumptions),
      "state.assumptions is empty — a pre-launch run with no assumptions is not credible")
if assumptions:
    no_val = [a.get("id", "?") for a in assumptions
              if a.get("status", "open") == "open" and not str(a.get("validation", "")).strip()]
    check("every open assumption names a validation method", not no_val, no_val[:5])

# ------------------------------------------------------------------ gates
run = state.get("run") or {}
completed = run.get("completed_modules") or []
all_modules = sorted(yaml.safe_load(open(f, encoding="utf8"))["id"]
                     for f in glob.glob(os.path.join(FRAMEWORK, "modules/*/module.yaml")))
not_done = [m for m in all_modules if m not in completed]
check("every module completed and recorded", not not_done, not_done)

check("confidence is recorded", run.get("confidence") in ("high", "medium", "low"),
      f"state.run.confidence is '{run.get('confidence')}' — must be high, medium or low by delivery")

# ------------------------------------------------------------------ the two chains
text_all = "\n".join(body(a) for a in present)

shortfall = "declared_shortfall" in str(state) or "declared shortfall" in text_all.lower()
if shortfall:
    carried = re.search(r"shortfall", text_all, re.I) and re.search(
        r"weight|weighted|weighting", text_all, re.I)
    check("declared shortfall was carried into the strategy weighting", bool(carried),
          "a shortfall was declared and no weighting change is described — "
          "this is worse than never declaring it")
else:
    notes.append("No declared shortfall in this run — the 04→07 chain does not apply.")

breach = re.search(r"ceiling (is )?exceeded|exceeds the ceiling|ceiling breach", text_all, re.I)
if breach:
    regressed = re.search(r"regress|raise the price|reduce the scope|price change", text_all, re.I)
    check("cost ceiling breach produced a recorded regress", bool(regressed),
          "a breach is reported with no regress to 06-business or 07-strategy")
else:
    notes.append("No cost ceiling breach in this run — the 13→06/07 regress does not apply.")

# ------------------------------------------------------------------ blockers
blocked = re.search(r"BLOCKS LAUNCH|blocker", text_all, re.I)
if blocked:
    notes.append("This run carries at least one blocker. Confirm each has a named human owner.")

# ------------------------------------------------------------------ result
print()
for n in notes:
    print(f"  note   {n}")
print()
if failures:
    print(f"  {len(failures)} check(s) failed. The run is not deliverable.")
    sys.exit(1)
print("  All run checks pass.")
