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

surface = (state.get("project") or {}).get("delivery_surface", "")
check("delivery surface is set", bool(str(surface).strip()),
      "state.project.delivery_surface is empty — 01-idea gate criterion 3. Eight modules "
      "read it as settled context and none re-examines it, so an unstated surface is a "
      "default that was inherited rather than chosen")

# ------------------------------------------------------------------ schema conformance
# A run can record exactly the right content under a key this schema does not define, and
# every check that reads the defined key sees an absent field. The content is present, the
# reasoning was done, and the validator reports the work as missing — or worse, passes,
# because the check keys off something else.
#
# Only top-level keys and the keys of `project` and `run` are compared. Going deeper would
# reject the per-run fields a module legitimately adds to a list entry.
schema = yaml.safe_load(open(os.path.join(FRAMEWORK, "engine/state-schema.yaml"), encoding="utf8")) or {}

def unknown_keys(actual, expected, path):
    if not isinstance(actual, dict) or not isinstance(expected, dict):
        return []
    return [f"{path}{k}" for k in actual if k not in expected]

stray = unknown_keys(state, schema, "")
for section in ("project", "run"):
    stray += unknown_keys(state.get(section), schema.get(section), f"{section}.")

check("state.yaml uses only keys the schema defines", not stray,
      f"undefined key(s): {stray[:6]}\n         "
      "content recorded under an invented key is invisible to every check that reads the "
      "defined one — see engine/state-schema.yaml")

# ------------------------------------------------------------------ schema era
# Which version of engine/state-schema.yaml this run was written against. New REQUIRED checks
# are gated on it, so a run produced under an older contract is reported as out of scope
# rather than as failing. Checks that fire only when a mechanism is actually USED are not
# gated — they apply to every run, because a run using a mechanism wrongly is wrong whenever
# it was made.
ERA = state.get("version", 1)
SCHEMA_ERA = schema.get("version", 1)
if ERA < SCHEMA_ERA:
    notes.append(
        f"This run was written against state schema v{ERA}; the framework is now "
        f"v{SCHEMA_ERA}. Checks introduced since are not required of it, and it is not to be "
        "rewritten to satisfy them.")

# The controlled vocabularies — failure classes and question classes — live in gates.yaml
# and are read from it rather than duplicated here. A second copy is a second thing to keep
# in step, and the copy nobody edits is the one that goes stale.
gates = yaml.safe_load(open(os.path.join(FRAMEWORK, "engine/gates.yaml"), encoding="utf8")) or {}

# ------------------------------------------------------------------ artifacts
man = yaml.safe_load(open(os.path.join(FRAMEWORK, "deliverables/manifest.yaml"), encoding="utf8"))
MANIFEST_VERSION = man.get("version", 1)
run_version = (state.get("project") or {}).get("framework_version", 1)

# Manifest v4 grouped the artifacts into folders under deliverables/. A run produced under an
# earlier manifest wrote them flat, and it is judged against the layout it was produced under.
# Resolving every path through the current manifest instead would report a complete v3 run as
# having lost all fifteen artifacts — and the only repair available would be to restructure a
# finished record to satisfy a validator that grew after it.
FOLDERED = run_version >= 4
LAYOUT = man.get("folder_layout") or {}
ACCEPTANCE_FILE = LAYOUT.get("acceptance_file") or "_acceptance.md"
DECLARED_FOLDERS = [f.get("id") for f in (LAYOUT.get("folders") or [])]


def rel(a):
    """Where this artifact lives under deliverables/, in the layout the run was produced under."""
    return f"{a['folder']}/{a['file']}" if FOLDERED and a.get("folder") else a["file"]


dl_dir = os.path.join(RUN, "deliverables")
required = [a for a in man["artifacts"] if a.get("required")]

missing = [rel(a) for a in required if not os.path.isfile(os.path.join(dl_dir, rel(a)))]

# A v4 run that wrote the artifacts flat fails every path above and gives no reason why — the
# failure is a layout mismatch, not fifteen missing documents, and the two are repaired very
# differently.
#
# The diagnosis goes in THIS check's detail rather than in the notes, because the run exits a
# few lines below when nothing resolves and the notes at the bottom are never reached. Deferring
# it there put the explanation in the one place it could not be printed.
diagnosis = ""
if missing and FOLDERED:
    flat = [a["file"] for a in required if os.path.isfile(os.path.join(dl_dir, a["file"]))]
    if flat:
        diagnosis = (
            f"\n         {len(flat)} of these exist at the OLD flat path under deliverables/. "
            "This run declares framework_version >= 4, which places every artifact in a "
            "folder — see folder_layout in deliverables/manifest.yaml. Either move them into "
            "their folders, or record the framework_version the run was actually produced "
            "under.")
check(f"all {len(required)} required artifacts present", not missing,
      f"{missing}{diagnosis}")

present = [a for a in man["artifacts"] if os.path.isfile(os.path.join(dl_dir, rel(a)))]
if not present:
    print("\n  No artifacts to inspect.")
    for n in notes:
        print(f"  note   {n}")
    sys.exit(1)

# ------------------------------------------------------- what else is in deliverables/
# The manifest OWNS every filename it declares under deliverables/. A run that writes a second
# package there — a revised specification, a superseded set, a branch produced after the
# recommendation changed — silently overwrites any artifact whose name it reuses, and the
# overwrite is undetectable afterwards because the file is present and well-formed.
#
# This happened on a completed run: one filename collided out of fourteen, one step after the
# agent asserted that none did, and the original was unrecoverable because runs are not under
# version control.
#
# The validator cannot prevent it — it runs after the write. What it can do is make the second
# package VISIBLE, which is the condition under which the collision gets noticed at all. The
# prevention is the write-time rule in AGENTS.md: a second package is namespaced in its own
# subdirectory, and a manifest filename is never written to except as that artifact.
#
# Walking rather than listing, because under v4 the artifacts are one level down and a flat
# listing would see only the folders. An unowned file INSIDE a declared folder is the dangerous
# case — that is where a collision can land. A file under some other subdirectory is the
# sanctioned second-package pattern and is left alone, which is the whole point of namespacing it.
owned = {rel(a) for a in man["artifacts"]}
extra = []
for dirpath, dirs, files in os.walk(dl_dir):
    dirs[:] = [d for d in dirs if not d.startswith(".")]
    for f in files:
        r = os.path.relpath(os.path.join(dirpath, f), dl_dir)
        top = r.split(os.sep)[0] if os.sep in r else ""
        if top and top not in DECLARED_FOLDERS:
            continue  # namespaced second package — not a collision risk
        if r in owned or os.path.basename(r).lower() == "readme.md" \
                or os.path.basename(r) == ACCEPTANCE_FILE:
            continue
        extra.append(r)
extra = sorted(extra)
if extra:
    notes.append(
        f"{len(extra)} file(s) in deliverables/ that the manifest does not declare: "
        + ", ".join(extra[:8]) + (" …" if len(extra) > 8 else "")
        + " — if these are a second package, confirm none of them overwrote a manifest "
          "artifact. A second package belongs in its own subdirectory.")


def body(a):
    return open(os.path.join(dl_dir, rel(a)), encoding="utf8").read()


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


def norm(s):
    """Whitespace-folded, so a criterion wrapped into a table cell still compares equal."""
    return re.sub(r"\s+", " ", str(s)).replace("\\|", "|").strip()


# ------------------------------------------------------------------ folder acceptance
# Each folder carries a copy of its artifacts' acceptance criteria, so the criteria sit beside
# the work instead of in a YAML file nobody opens mid-build.
#
# That is only worth anything if it IS a copy. A criterion reworded on the way in becomes the
# version the builder works to while the manifest still says something else, and nothing in the
# run can see the two diverge. It drifts toward softer, every time, because the file is written
# while looking at the artifact that has to satisfy it.
if FOLDERED and present:
    by_folder = {}
    for a in present:
        by_folder.setdefault(a.get("folder"), []).append(a)

    absent_acc, drifted, compared = [], [], 0
    for folder, arts in sorted(by_folder.items()):
        if not folder:
            continue
        p = os.path.join(dl_dir, folder, ACCEPTANCE_FILE)
        if not os.path.isfile(p):
            absent_acc.append(f"deliverables/{folder}/{ACCEPTANCE_FILE}")
            continue
        got = norm(open(p, encoding="utf8").read())
        for a in arts:
            for c in a.get("acceptance", []):
                compared += 1
                if norm(c) not in got:
                    drifted.append(f"{folder}/{ACCEPTANCE_FILE}: {a['id']} — \"{norm(c)[:70]}\"")
    check("every folder that received an artifact carries its acceptance file",
          not absent_acc, absent_acc)

    # Reported only when it actually compared something. With no acceptance files on disk this
    # check has an empty drift list and would print PASS — a validator claiming a property it
    # never examined, one line under the check that just said the files are missing.
    if compared:
        check(f"every folder acceptance criterion is the manifest's, character for character "
              f"({compared} compared)", not drifted,
              "\n         ".join(drifted[:8])
              + "\n         copied from deliverables/manifest.yaml, never rewritten")
    else:
        notes.append("No folder acceptance file could be read, so no criterion was compared "
                     "against the manifest. This check did not run.")

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

# ------------------------------------------------------- conditional continuation
# A gate may fail because the evidence it requires does not exist in any source the run can
# reach. engine/gates.yaml `conditional_continuation` defines that state. A module in it is
# CORRECTLY absent from completed_modules — a failed gate remains failed — so the completion
# check must recognise it rather than demanding the module be marked complete, which is the
# confidence laundering the evidence policy exists to prevent.
verdicts = run.get("gate_verdicts") or []
conditional = sorted({v.get("module") for v in verdicts
                      if isinstance(v, dict) and v.get("verdict") == "conditional_pass"
                      and v.get("module")})
CONDITIONAL = bool(conditional)

if CONDITIONAL:
    unexplained = [m for m in not_done if m not in conditional]
    check("every module completed, or conditionally continued and recorded as such",
          not unexplained, unexplained)
else:
    check("every module completed and recorded", not not_done, not_done)

check("confidence is recorded", run.get("confidence") in ("high", "medium", "low"),
      f"state.run.confidence is '{run.get('confidence')}' — must be high, medium or low by delivery")

if CONDITIONAL:
    named = ", ".join(conditional)

    # 1 — a failed gate remains failed
    still_failed = [m for m in conditional if m not in not_done]
    check("a conditionally continued gate is NOT recorded as complete", not still_failed,
          f"{still_failed} appear in completed_modules. A failed gate remains failed; "
          "adding it to satisfy this validator is the laundering the evidence policy forbids")

    # 2 — the Research Exhaustion Report exists and is complete
    REQUIRED = ["question", "methods_attempted", "evidence_still_unavailable",
                "why_further_desk_research_will_not_help", "what_would_resolve_it"]
    reports = state.get("research_exhaustion") or []
    covered = {r.get("module") for r in reports if isinstance(r, dict)}
    missing_report = [m for m in conditional if m not in covered]
    check("every conditionally continued gate has a Research Exhaustion Report",
          not missing_report,
          f"state.research_exhaustion has no entry for {missing_report}. The report is the "
          "precondition for this state, not a byproduct of it")

    gaps = []
    for r in reports:
        if not isinstance(r, dict):
            continue
        m = r.get("module", "?")
        for f in REQUIRED:
            if not str(r.get(f) or "").strip() and not (isinstance(r.get(f), list) and r.get(f)):
                gaps.append(f"{m}: {f} is empty")
        for meth in (r.get("methods_attempted") or []):
            if not isinstance(meth, dict):
                gaps.append(f"{m}: methods_attempted must itemise each method, not summarise")
                continue
            if not str(meth.get("method") or "").strip():
                gaps.append(f"{m}: a method_attempted entry has no name")
            if meth.get("failed") and not str(meth.get("why_failed") or "").strip():
                gaps.append(f"{m}: '{meth.get('method')}' failed with no structural reason given")
    if reports:
        check("the Research Exhaustion Report is complete", not gaps,
              "\n         ".join(gaps[:8]))

    # 3 — one attempt reserved, against a named method
    unreserved = [v.get("module") for v in verdicts
                  if isinstance(v, dict) and v.get("verdict") == "conditional_pass"
                  and not (v.get("attempt_reserved") and
                           str(v.get("reserved_against_method") or "").strip())]
    check("one gate attempt is reserved, against a named failed method", not unreserved,
          f"{unreserved} record no reserved attempt. The gate is postponed against a specific "
          "future input, not abandoned")

    # 4 — confidence capped, and the artifacts say so
    check("confidence is capped at low while a gate is conditionally continued",
          run.get("confidence") == "low",
          f"state.run.confidence is '{run.get('confidence')}'. It cannot be raised by later "
          "modules, a favourable finding, or the volume of work completed — only by evidence "
          "closing the gate")

    # Only the declaration is machine-checkable. Whether the wording CLAIMS validation is a
    # judgement a regex cannot make — "not a validated case" contains the same words as a
    # claim to be one — so this checks that conditionality is stated and leaves the rest to
    # review rather than producing a confident false verdict.
    summary = next((body(a) for a in present
                    if "executive-summary" in a["file"].lower()), "")
    check("the Executive Summary declares the run conditional",
          bool(re.search(r"conditional", summary, re.I)),
          "It must state that this is a conditional blueprint rather than a validated case, "
          f"and name the unresolved gate ({named})")

# -------------------------------------------------- U4: decisions have one home
# U4 says every decision records the alternatives it rejected. A module can satisfy that by
# writing a sentence into its gate verdict — which reads as compliance, is not queryable, and
# is exactly what happened for fourteen consecutive modules in a completed run while
# state.decisions stayed empty. The run validated, because nothing checked the two agreed.
#
# Two homes for one record means the unchecked one goes empty. There is now one home, and
# gate_verdicts[].decisions is the reference into it.
decisions = state.get("decisions") or []
by_id = {str(d.get("id")): d for d in decisions if isinstance(d, dict) and d.get("id")}

# Ungated: U4 has always required this, so an entry missing it was wrong whenever it was
# written. Only the REFERENCE below is new, and only that is era-gated.
if decisions:
    no_alts = [str(d.get("id", "?")) for d in decisions
               if isinstance(d, dict)
               and not (isinstance(d.get("alternatives_rejected"), list)
                        and d.get("alternatives_rejected"))]
    check("every decision records the alternatives it rejected", not no_alts,
          f"{no_alts[:6]} — U4. A choice with no rejected alternative was not a decision, "
          "it was a description")

DECISIONS_ERA = 3
if ERA >= DECISIONS_ERA:
    silent, dangling = [], []
    for v in verdicts:
        if not isinstance(v, dict):
            continue
        m = v.get("module", "?")
        d = v.get("decisions")
        # `none` is a legitimate value and must be stated. A module that made no recordable
        # decision is a different state from a module that did not say, and only one of them
        # is worth investigating.
        if isinstance(d, str):
            if d.strip().lower() != "none":
                silent.append(f"{m}: decisions is '{d}' — expected a list of ids, or `none`")
            continue
        if not isinstance(d, list) or not d:
            silent.append(f"{m}: no `decisions` recorded")
            continue
        for i in d:
            if str(i) not in by_id:
                dangling.append(f"{m} names {i}, which is not in state.decisions")

    check("every gate verdict names the decisions it recorded, or `none`", not silent,
          "\n         ".join(silent[:8]) + "\n         U4 is satisfied by an entry in "
          "state.decisions and by nothing else. A verdict describing decisions in prose has "
          "recorded them nowhere a later reader or another run can find them.")
    check("every decision id named by a gate verdict resolves", not dangling,
          "\n         ".join(dangling[:8]))
elif verdicts and not decisions:
    notes.append("state.decisions is empty and this run predates the schema era that requires "
                 "gate verdicts to name their decision ids. Nothing is required of it — but if "
                 "U4 was satisfied by prose inside the verdicts, those decisions exist only "
                 "there, and no later run can read them.")

# ------------------------------------------- a shortfall names WHICH KIND of shortfall
# A gate falling short is not one thing. Failed assumption, insufficient evidence, failed
# validation, technical impossibility, business weakness and unresolved question each imply a
# different next action — stop, spend a week, spend an hour, ask a person — and reporting all
# six in the same register is what leaves an operator unable to tell whether the product is
# wrong, unproven, or merely under-researched.
FAILURE_CLASSES = set(gates.get("failure_classes", {}).get("values", {}) or {})
CLASS_ERA = 3
unclassified, bad_class = [], []
for v in verdicts:
    if not isinstance(v, dict):
        continue
    if v.get("verdict") == "pass" and not v.get("shortfall_declared"):
        continue
    m, fc = v.get("module", "?"), str(v.get("failure_class") or "").strip()
    why = "verdict is not `pass`" if v.get("verdict") != "pass" else "shortfall_declared"
    if not fc:
        unclassified.append(f"{m} ({why}) records no failure_class")
    elif fc not in FAILURE_CLASSES:
        bad_class.append(f"{m}: failure_class '{fc}' is not one of {sorted(FAILURE_CLASSES)}")

if ERA >= CLASS_ERA:
    check("every shortfall or non-pass verdict names its failure class", not unclassified,
          "\n         ".join(unclassified[:8]) + "\n         engine/gates.yaml "
          "`failure_classes`. Recorded with the verdict, never chosen later to fit the "
          "recommendation.")
    check("every recorded failure class is one of the six", not bad_class,
          "\n         ".join(bad_class[:8]))
elif unclassified:
    notes.append("This run reports a shortfall or a non-pass gate without a failure class. The "
                 "vocabulary postdates its schema era, so nothing is required of it — but a "
                 "reader cannot tell from the record whether the product is wrong, unproven, "
                 "or under-researched, and those imply different next actions.")

# --------------------------------------- questions declare what kind of question they are
# Only `operator_only` may stop the run. Without the class on the question, every question
# looks equally obligatory to the operator, and the ones research could have closed spend the
# attention budget before the one nothing else can answer arrives.
QUESTION_CLASSES = set(gates.get("operator_question_classes", {}).get("values", {}) or {})
oq = state.get("open_questions") or []
if ERA >= 3 and oq:
    unclassed = [str(q.get("question", "?"))[:60] for q in oq
                 if isinstance(q, dict)
                 and str(q.get("class") or "").strip() not in QUESTION_CLASSES]
    check("every open question declares its class", not unclassed,
          f"{unclassed[:5]} — must be one of {sorted(QUESTION_CLASSES)} "
          "(engine/gates.yaml `operator_question_classes`)")

    # `assumable` means "worth asking later". Later is a module, not a mood.
    no_ask_at = [str(q.get("question", "?"))[:60] for q in oq
                 if isinstance(q, dict) and str(q.get("class") or "").strip() == "assumable"
                 and not str(q.get("ask_at") or "").strip()]
    check("every deferred question names the module where it is asked", not no_ask_at,
          f"{no_ask_at[:5]} — class `assumable` with no ask_at is a deferral no gate ever "
          "collects")

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

# ------------------------------------------------------------------ identifiers
# Every name a code block operates on must be a name some code block creates. A schema
# that defines `order` while the grant, the index and the trigger constrain `orders` is
# four documents agreeing with each other and none of them agreeing with the database.
#
# The statement that breaks is reliably the one protecting the product's central
# guarantee, because it is written last, in its own block, after the naming has drifted —
# and it fails at the first migration, not at review.
#
# Fenced blocks of any language are scanned: the damaging case is SQL embedded in an
# application-language block, which is where a framework's migration DSL puts it.
SQL_DDL = re.compile(r"\b(CREATE\s+TABLE|ALTER\s+TABLE|CREATE\s+(UNIQUE\s+)?INDEX|"
                     r"CREATE\s+TRIGGER|REVOKE|GRANT)\b", re.I)
CREATES = re.compile(r"\bCREATE\s+(?:TABLE|(?:MATERIALIZED\s+)?VIEW)\s+"
                     r"(?:IF\s+NOT\s+EXISTS\s+)?(?:\w+\.)?([a-z_][a-z0-9_]*)", re.I)
REFS = [
    re.compile(r"\bON\s+(?:\w+\.)?([a-z_][a-z0-9_]*)\s*(?:\(|FOR\s+EACH\b|FROM\b|TO\b)", re.I),
    re.compile(r"\bALTER\s+TABLE\s+(?:ONLY\s+)?(?:\w+\.)?([a-z_][a-z0-9_]*)", re.I),
    re.compile(r"\bREFERENCES\s+(?:\w+\.)?([a-z_][a-z0-9_]*)", re.I),
    re.compile(r"\bINSERT\s+INTO\s+(?:\w+\.)?([a-z_][a-z0-9_]*)", re.I),
]

created, referenced = set(), {}
for a in present:
    for block in re.findall(r"```[a-zA-Z0-9_+-]*\n(.*?)```", body(a), re.S):
        if not SQL_DDL.search(block):
            continue
        created.update(m.lower() for m in CREATES.findall(block))
        for rx in REFS:
            for name in rx.findall(block):
                referenced.setdefault(name.lower(), a["file"])

def stem(n):
    """Fold the spellings that differ only by convention, so the message can say which."""
    n = n.replace("_", "")
    if n.endswith("ies"):
        return n[:-3] + "y"
    return n[:-1] if n.endswith("s") else n


if created:
    unresolved = []
    for name, where in sorted(referenced.items()):
        if name in created:
            continue
        near = [c for c in created if stem(c) == stem(name)]
        hint = f"  (defined as `{near[0]}`)" if near else ""
        unresolved.append(f"{where}: `{name}` is used and never created{hint}")
    check(f"every identifier used in a code block is defined ({len(created)} defined)",
          not unresolved, "\n         ".join(unresolved[:8]))
else:
    notes.append("No schema definitions found in the artifacts — the identifier check does "
                 "not apply.")

# ------------------------------------------------------------------ late answers
# The trigger — a blocking question answered after its module passed — is the agent's to
# detect; engine/gates.yaml `late_answer_rederivation` defines it. What is checkable here
# is that the record left behind is a re-derivation and not a note saying one happened.
questions = state.get("open_questions") or []
rederivations = state.get("rederivations") or []

owed = [q.get("question", "?") for q in questions
        if q.get("blocking") and str(q.get("substitute_assumption") or "").strip()]
if owed:
    check("a substituted blocking answer produced a recorded re-derivation",
          bool(rederivations),
          "modules ran on a substitute assumption and state.rederivations is empty — "
          f"the conclusions were corrected in wording only: {owed[:3]}")

if rederivations:
    thin = [r.get("trigger", "?")[:60] for r in rederivations
            if not (r.get("conclusions_retested") and
                    all(c.get("verdict") in ("survived", "changed", "withdrawn")
                        for c in r["conclusions_retested"]))]
    check("every re-derivation retested named conclusions to a verdict", not thin,
          "a re-derivation records no retested conclusion, or one without a verdict of "
          f"survived / changed / withdrawn: {thin[:3]}")

unanswered = [q.get("question", "?") for q in questions
              if q.get("blocking") and not str(q.get("answer") or "").strip()]
if unanswered:
    notes.append(f"{len(unanswered)} blocking question(s) unanswered at delivery. Each must "
                 "carry a named owner in Risks-and-Assumptions.")

# ------------------------------------------------------------------ stated counts
# A deliverable that reports "23 open assumptions" while state carries 26 is not a rounding
# difference. The register is the artifact a reader uses to judge how much is unresolved,
# and a count drifting below the truth understates exactly that. It drifts silently: the
# figure is written once, more assumptions are added later, and nothing rereads the sentence.
#
# Only fires when a number is actually stated. A run that gives no count is not penalized —
# but a run that gives a wrong one is, because a stated figure is read as authoritative.
def stated(metric_pattern):
    """Numbers written next to a metric name, in prose or in a summary table cell."""
    out = []
    for a in present:
        t = body(a)
        for rx in (rf"(\d+)\s+(?:currently\s+)?{metric_pattern}",
                   rf"{metric_pattern}[^|\n]*\|\s*\*{{0,2}}(\d+)"):
            for m in re.finditer(rx, t, re.I):
                out.append((a["file"], int(m.group(1))))
    return out


COUNTS = [
    ("open assumptions",
     len([a for a in assumptions if a.get("status", "open") == "open"]),
     r"open assumptions"),
    ("load-bearing assumptions",
     len([a for a in assumptions if a.get("load_bearing")]),
     r"load[- ]bearing assumptions"),
]

drift = []
for label, actual, pattern in COUNTS:
    for where, said in stated(pattern):
        if said != actual:
            drift.append(f"{where}: says {said} {label}, state.yaml has {actual}")

if any(stated(p) for _, _, p in COUNTS):
    check("counts stated in the deliverables match state.yaml", not drift,
          "\n         ".join(drift[:6]))
else:
    notes.append("No assumption counts stated in the deliverables — the drift check does "
                 "not apply.")

# ------------------------------------------------- prose importance vs the recorded flag
# A run keeps two lists of what it rests on: `load_bearing` in state, which checks read, and
# the prose in the deliverables, which humans read. They drift, and the drift is invisible
# from either side — the reader counts the ones described as decisive, a check counts the
# ones flagged, and neither sees the other's number.
#
# Found on a completed run whose two lists differed by exactly one assumption: the one whose
# own record called it "the strongest single piece of counter-evidence in the run".
#
# The prose is authoritative about importance, because that is what a person acts on. So a
# mismatch is a missing flag, not an overstated sentence.
#
# READ BOTH LAYOUTS. Matching only lines that contain the phrase AND an assumption id catches
# "A1 is load-bearing" and misses the far more common shape: a register table with a
# Load-bearing COLUMN, where the phrase is in the header row and the id is in the data rows,
# never together on one line.
#
# A structure-test run written to the templates hit exactly that. The document marked both of
# its load-bearing assumptions correctly, the check found no line carrying both, and it
# reported "does not apply" — a silent skip of the parity guarantee on the layout the templates
# actually produce.
LB_PHRASE = re.compile(r"load[- ]bearing", re.I)
AFFIRM = re.compile(r"^\**\s*(yes|true|y|✓|x)\s*\**$", re.I)

prose_lb = {}
for a in present:
    lb_col = None  # index of a Load-bearing column in the table currently being read
    for line in body(a).splitlines():
        if LB_PHRASE.search(line):
            for aid in re.findall(r"\bA\d+\b", line):
                prose_lb.setdefault(aid, a["file"])

        if "|" not in line:
            lb_col = None  # the table ended; a later table needs its own header
            continue

        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if LB_PHRASE.search(line):
            lb_col = next((i for i, c in enumerate(cells) if LB_PHRASE.search(c)), None)
            continue
        if lb_col is not None and lb_col < len(cells) and AFFIRM.match(cells[lb_col]):
            for aid in re.findall(r"\bA\d+\b", line):
                prose_lb.setdefault(aid, a["file"])

flagged = {str(a.get("id")) for a in assumptions if a.get("load_bearing")}
unflagged = [f"{aid}: called load-bearing in {where}, no load_bearing flag in state.yaml"
             for aid, where in sorted(prose_lb.items()) if aid not in flagged]
if prose_lb:
    check("assumptions called load-bearing in the deliverables carry the flag in state",
          not unflagged, "\n         ".join(unflagged[:6]))
else:
    notes.append("No assumption is described as load-bearing in the deliverables — the "
                 "flag-parity check does not apply.")

# --------------------------------------------- every kill criterion has a stop condition
# Milestone Zero tests carry a `kills_the_plan_if`. Stop conditions carry a threshold and an
# action. They are two lists of failure criteria maintained separately, and they drift.
#
# On the run that produced this check, two of three tests were wired to a stop condition and
# the third was not — so the run could have received its most decisive negative result and
# had no written rule for acting on it. The failure mode is not a wrong decision. It is an
# unmade one: the result arrives, there is no threshold to test it against, and it is
# absorbed as context.
outputs = state.get("outputs") or {}
m0 = outputs.get("roadmap") or {}
tests = (m0.get("milestone_zero_tests") or []) if isinstance(m0, dict) else []
sc_block = outputs.get("stop_conditions") or {}
sc = (sc_block.get("items") or []) if isinstance(sc_block, dict) else []
if tests and sc:
    sc_text = " ".join(str(s.get("signal", "")) + " " + str(s.get("means", "")) for s in sc)
    sc_ids = {str(s.get("id")) for s in sc}
    orphans = []
    for t in tests:
        tid = str(t.get("id", "?"))
        kill = str(t.get("kills_the_plan_if", "")).strip()
        if not kill:
            continue
        # Wired either way round: the stop condition names the test, or the kill criterion
        # names the stop condition.
        if tid in sc_text or any(re.search(rf"\b{re.escape(i)}\b", kill) for i in sc_ids):
            continue
        orphans.append(f"{tid}: kills_the_plan_if resolves to no stop condition -> {kill[:70]}")
    check("every Milestone Zero kill criterion resolves to a stop condition",
          not orphans, "\n         ".join(orphans[:6]))
elif isinstance(m0, dict) and m0.get("milestone_zero_present"):
    # The run says it committed to a Milestone Zero. With the tests unrecorded, the wiring check
    # above cannot run at all — and it reports "does not apply", which reads as nothing to check
    # rather than as a check that was switched off.
    #
    # Same shape as an unmarked `chosen` option silently disabling the generated-option
    # asymmetry rule: the state file looks identical either way, and the guarantee is gone.
    #
    # NOT gated on a schema era. This fires only when the mechanism is actually in use, and a
    # run using Milestone Zero without recording its tests is wrong whenever it was made —
    # engine/AUTHORING.md's rule for use-triggered checks.
    missing_part = []
    if not tests:
        missing_part.append("state.outputs.roadmap.milestone_zero_tests is empty")
    if not sc:
        missing_part.append("state.outputs.stop_conditions.items is empty")
    check("a run committing to Milestone Zero records its tests and stop conditions",
          False,
          "; ".join(missing_part) + ".\n         "
          "roadmap.milestone_zero_present is true, so the validation week exists — but with "
          "these unrecorded, every kill criterion in it resolves to nothing and the wiring "
          "check silently does not run. See engine/milestone-zero.md")
else:
    notes.append("No Milestone Zero in this run — the kill-criterion wiring check does not "
                 "apply.")

# ------------------------------------------------------------- operator directive ids
# Operators cannot see state.yaml, so a directive offered as "D-15" may collide with one
# already recorded. A silent overwrite loses the earlier directive and the analysis it drove,
# and nothing downstream can detect the loss. The run assigns ids; this checks it did.
directives = run.get("operator_directives") or []
if directives:
    ids = [str(d.get("id")) for d in directives if isinstance(d, dict)]
    dupes = sorted({i for i in ids if ids.count(i) > 1})
    check("operator directive ids are unique", not dupes,
          f"duplicated: {dupes}" if dupes else "")

# ------------------------------------------------------------------ completion artifacts
# One per audience: the five-minute decision maker, the approver, the engineering team, the
# AI agent that opens the folder — plus the validation package, when the strategy committed to
# validating before building. A run that produced the specification and none of these has
# finished the research and not finished the job.
#
# Judged against the manifest version the run was PRODUCED under, not the current one. A
# completed run is a historical record; rewriting one to satisfy a validator that grew after
# it would destroy the property that makes the record worth keeping. An older run is reported
# as out of scope, never as failing.
completion = man.get("completion_artifacts") or []

# `required: conditional` means the artifact is owed only when the run's own state says it is.
# The Milestone Zero package is the case: a run that recommends building outright, or not
# building at all, has no validation week to write out, and its absence is then correct rather
# than a gap. Treating "conditional" as truthy would demand it of every run.
roadmap_out = outputs.get("roadmap") or {}
CONDITIONS = {
    "milestone-zero-package": bool(isinstance(roadmap_out, dict)
                                   and roadmap_out.get("milestone_zero_present")),
}
required_completion = [
    a for a in completion
    if a.get("required") is True
    or (a.get("required") == "conditional" and CONDITIONS.get(a.get("id"), False))
]
skipped_conditional = [
    a["id"] for a in completion
    if a.get("required") == "conditional" and not CONDITIONS.get(a.get("id"), False)
]
for cid in skipped_conditional:
    notes.append(f"Completion artifact '{cid}' is conditional and its condition is not met "
                 "in this run — not required, and its absence is not a gap.")

if not required_completion:
    pass  # the manifest declares none — nothing to check
elif run_version < MANIFEST_VERSION:
    notes.append(
        f"This run was produced under manifest v{run_version}; the framework is now "
        f"v{MANIFEST_VERSION}. The completion artifacts introduced since are not required "
        "of it, and it is not to be rewritten to add them.")
else:
    # Presence is tested against the format the MANIFEST declares, not against an assumption
    # that every artifact is a file. `milestone-zero-package` is declared `format: directory`
    # and can never satisfy os.path.isfile, so a correctly-built package was reported absent
    # on every run that produced one — and the only two repairs available were faking a file
    # at that path or collapsing the package against its own format declaration. Both satisfy
    # the check by damaging the artifact.
    #
    # A validator that cannot be satisfied by correct work teaches operators to ignore
    # validators, which is the one outcome it cannot survive.
    def artifact_present(a):
        p = os.path.join(RUN, a["path"])
        if str(a.get("format", "")).lower() == "directory":
            return os.path.isdir(p) and bool(os.listdir(p))
        return os.path.isfile(p)

    absent = [a["path"] for a in required_completion if not artifact_present(a)]
    check(f"all {len(required_completion)} completion artifacts present "
          "(one per audience)", not absent, absent)

    empty_dirs = [a["path"] for a in required_completion
                  if str(a.get("format", "")).lower() == "directory"
                  and os.path.isdir(os.path.join(RUN, a["path"]))
                  and not os.listdir(os.path.join(RUN, a["path"]))]
    if empty_dirs:
        notes.append("Declared as a directory and present but empty: "
                     + ", ".join(empty_dirs) + " — an empty package is not a package.")

    # Scaffolding left in a completion artifact is worse than in a deliverable: these are the
    # files that travel outside the team.
    #
    # TEXT FORMATS ONLY, taken from the manifest's `format`. A .pptx is a zip, and decoding one
    # as text produces byte sequences that match these markers by coincidence — which reported
    # a finished deck as unfinished. Never infer a format from a file that was opened anyway.
    # A `format: directory` artifact is scanned by walking the text files inside it. Skipping
    # it because the path is not a file leaves the package that travels to the operator as the
    # only artifact nothing checks.
    TEXT_FORMATS = {"markdown", "md", "html", "text", "txt"}
    TEXT_SUFFIXES = (".md", ".markdown", ".html", ".txt", ".csv", ".yaml", ".yml")
    MARKERS = (("«placeholder»", r"«[^»]*»"),
               ("<!-- fill", r"<!-- fill"),
               ("<!-- ACCEPTANCE", r"<!-- ACCEPTANCE"))

    def scan(path, label, out):
        try:
            t = open(path, encoding="utf8").read()
        except (UnicodeDecodeError, OSError):
            return
        for marker, pattern in MARKERS:
            if re.search(pattern, t):
                out.append(f"{label}: {marker}")

    scaffold, unscannable = [], []
    for a in required_completion:
        p = os.path.join(RUN, a["path"])
        fmt = str(a.get("format", "")).lower()
        if fmt == "directory":
            if not os.path.isdir(p):
                continue
            for dirpath, _, files in os.walk(p):
                for f in sorted(files):
                    if f.lower().endswith(TEXT_SUFFIXES):
                        # NOT `rel` — that is the artifact path helper defined above, and
                        # rebinding it here breaks every later call to it.
                        label = os.path.relpath(os.path.join(dirpath, f), RUN)
                        scan(os.path.join(dirpath, f), label, scaffold)
            continue
        if not os.path.isfile(p):
            continue
        if fmt not in TEXT_FORMATS:
            unscannable.append(a["path"])
            continue
        scan(p, a["path"], scaffold)
    check("no scaffolding remains in the text completion artifacts", not scaffold, scaffold[:6])
    if unscannable:
        notes.append("Not text, so not scanned for leftover scaffolding: "
                     + ", ".join(unscannable) + " — check it by opening it.")

    # The entry file's whole purpose is that the folder can move. A path pointing at the
    # framework, at PIOS_HOME, or at an absolute location on this machine breaks that
    # silently — it keeps working here and fails the first time the folder is copied.
    entry = next((a for a in required_completion if a["id"] == "ai-entry-file"), None)
    if entry and os.path.isfile(os.path.join(RUN, entry["path"])):
        t = open(os.path.join(RUN, entry["path"]), encoding="utf8").read()
        escapes = re.findall(r"PIOS_HOME|`/(?:Users|home|opt|var)/[^`]*`|<FRAMEWORK>", t)
        check("the entry file points nowhere outside the run directory",
              not escapes, sorted(set(escapes))[:6])

# ------------------------------------------------------------------ phase plan
# The board is what a builder works from, which makes it where drift from the roadmap does the
# most damage and is least visible. A milestone with no phase document is not reported by
# anything that reads the roadmap — the roadmap still lists it, every review of it passes, and
# the phase nobody wrote is simply never started.
PHASES_ERA = 4  # the manifest version that introduced phases/
if run_version >= PHASES_ERA:
    ph_dir = os.path.join(RUN, "phases")
    roadmap_block = outputs.get("roadmap") or {}
    milestones = (roadmap_block.get("milestones") or []) if isinstance(roadmap_block, dict) else []

    check("the roadmap's milestones are recorded in state", bool(milestones),
          "state.outputs.roadmap.milestones is empty or absent. engine/phases.md requires one "
          "phase document per milestone, and that cannot be checked against a list which does "
          "not exist — leaving a dropped milestone as the one kind of scope loss nothing sees")

    if os.path.isdir(ph_dir):
        check("the phase board exists", os.path.isfile(os.path.join(ph_dir, "README.md")),
              "phases/README.md is missing. The folder holds phase documents and nothing that "
              "says which one may be started")

        docs = sorted(f for f in os.listdir(ph_dir) if re.match(r"^phase-\d+.*\.md$", f))
        check("the phase folder contains phase documents", bool(docs),
              "no phase-NN-*.md files in phases/ — an empty package is not a package")

        text = {f: open(os.path.join(ph_dir, f), encoding="utf8").read() for f in docs}

        if milestones and docs:
            ids = [str(m.get("id")) for m in milestones if isinstance(m, dict) and m.get("id")]
            joined = "\n".join(text.values())
            unwritten = [i for i in ids if not re.search(rf"\b{re.escape(i)}\b", joined)]
            check("every roadmap milestone has a phase document", not unwritten,
                  f"{unwritten[:6]} are recorded in state.outputs.roadmap.milestones and named "
                  "in no phase document")
            check("the phase count matches the milestone count", len(docs) == len(milestones),
                  f"{len(docs)} phase document(s), {len(milestones)} milestone(s). A phase with "
                  "no milestone behind it is scope the roadmap never authorized, and it will be "
                  "built")

        currents = [f for f, t in text.items()
                    if re.search(r"^\*\*Status:\*\*\s*current\b", t, re.M | re.I)]
        check("at most one phase is marked current", len(currents) <= 1,
              f"{currents} are all marked current. One phase is startable at a time; a board "
              "with two is read as permission for both")
        if docs and not currents:
            notes.append("No phase is marked current. That is correct where the verdict does "
                         "not support building — confirm phases/README.md says so on its first "
                         "line, rather than the board having stalled silently.")

        # The headline rule of engine/phases.md, and the one no single document can show: a
        # definition of done sharpened while writing the phase plan reads entirely reasonably
        # on the page it lands on, and the roadmap it contradicts is not open at the time.
        #
        # COMPARED CONDITION BY CONDITION, not as one block. 09-Roadmap.md writes a definition
        # of done as a checkbox list of several conditions; the phase document reproduces that
        # list. Matching the whole section as a single string fails on the list markers sitting
        # between the conditions — so the check would reject a correctly copied phase plan, and
        # a validator that cannot be satisfied by correct work teaches operators to ignore
        # validators, which is the one outcome it does not survive.
        #
        # Per-condition also localizes the finding. One softened condition out of four is the
        # realistic defect, and it is the one a whole-block comparison reports as "the section
        # does not match".
        # The bullet alternatives require TRAILING WHITESPACE. Without it `*` matches the first
        # character of `**Source:**`, the line survives as `*Source:**`, every startswith test
        # for it misses, and the source pointer is compared against the roadmap as though it
        # were a condition — which fails every correctly written phase document.
        MARKER = re.compile(r"^\s*(?:>\s+)?(?:[-*+]\s+)?(?:\[[ xX]\]\s+)?", re.M)

        def conditions(block):
            """The individual conditions in a definition-of-done block, markers stripped."""
            out = []
            for line in block.splitlines():
                line = MARKER.sub("", line).strip()
                if not line or line.lower().startswith(("**source", "source:", "<!--")):
                    continue
                out.append(norm(line))
            return out

        rm = next((a for a in present if a["id"] == "roadmap"), None)
        if rm and docs:
            roadmap_text = norm(MARKER.sub("", body(rm)))
            rederived, unparsed = [], []
            for f, t in sorted(text.items()):
                m = re.search(r"^#+\s*Definition of done\s*$\n+(.*?)(?=^#|\Z)",
                              t, re.M | re.S | re.I)
                if not m or not conditions(m.group(1)):
                    unparsed.append(f)
                    continue
                for c in conditions(m.group(1)):
                    if c not in roadmap_text:
                        rederived.append(f"{f}: \"{c[:66]}\"")
            check("every definition-of-done condition is reproduced from 09-Roadmap.md",
                  not rederived,
                  "\n         ".join(rederived[:6])
                  + "\n         not found in 09-Roadmap.md — conditions are copied word for "
                    "word and never re-derived, see engine/phases.md")
            if unparsed:
                notes.append("No 'Definition of done' conditions could be read from: "
                             + ", ".join(unparsed[:6])
                             + " — the reproduction check could not run on these.")

# ------------------------------------------------------------------ validation results
# Milestone Zero and anything with its shape. A validation outcome can overturn a delivered
# recommendation, so the states it may take are constrained and the two that must never be
# merged are checked by name.
VALID_OUTCOMES = {"pass", "fail", "revise", "inconclusive", "blocked", "not_applicable"}
validations = state.get("validation") or []

if validations:
    bad_state = [f"{v.get('id', '?')}: outcome '{v.get('outcome')}'" for v in validations
                 if isinstance(v, dict) and v.get("outcome") not in VALID_OUTCOMES]
    check("every validation outcome is one of the six defined states", not bad_state,
          f"{bad_state[:5]}\n         "
          f"permitted: {', '.join(sorted(VALID_OUTCOMES))} — engine/gates.yaml "
          "`validation_outcomes`")

    # `inconclusive` says the test ran and the sample cannot carry the reading. `blocked` says
    # it could not run at all. Neither is a finding about the product, and both are worthless
    # to the operator without the reason — which is the action they are owed.
    no_reason = [v.get("id", "?") for v in validations
                 if isinstance(v, dict)
                 and v.get("outcome") in ("inconclusive", "blocked")
                 and not str(v.get("outcome_reason") or "").strip()]
    check("every inconclusive or blocked test states why, and whose action obtains it",
          not no_reason,
          f"{no_reason[:5]} record no outcome_reason. A blocked test is an item the operator "
          "is owed, not evidence about the product")

    # A stop condition that fires and changes nothing is worse than no stop condition: the run
    # now carries a record of having checked.
    no_action = [v.get("id", "?") for v in validations
                 if isinstance(v, dict) and v.get("stop_condition_fired")
                 and not str(v.get("required_action") or "").strip()]
    check("every fired stop condition names a required action", not no_action,
          f"{no_action[:5]} fired a stop condition with no required_action recorded")

    # A test recorded only as a method cannot be substituted, compared, or said to be about
    # anything. See engine/instrument-substitution.md.
    no_measure = [v.get("id", "?") for v in validations
                  if isinstance(v, dict) and not str(v.get("measures") or "").strip()]
    check("every validation test declares what it measures, not only how", not no_measure,
          f"{no_measure[:5]} record no `measures`. Without it the test cannot be judged "
          "against an alternative instrument, which is the common case")

    # Swapping the instrument without arguing the equivalence is the laundering this mechanism
    # exists to prevent: the method changes and the confidence does not.
    no_equiv = [v.get("id", "?") for v in validations
                if isinstance(v, dict) and str(v.get("substituted_for") or "").strip()
                and not str(v.get("equivalence_argument") or "").strip()]
    check("every substituted instrument carries its equivalence argument", not no_equiv,
          f"{no_equiv[:5]} replaced the specified instrument with no equivalence_argument — "
          "engine/instrument-substitution.md")

    # Criteria that can fire independently need a precedence rule fixed in advance. Two firing
    # with opposite implications is ordinary; without a rule, which governs is settled in the
    # write-up by whoever preferred an answer.
    multi = [v.get("id", "?") for v in validations
             if isinstance(v, dict) and len(v.get("criteria") or []) > 1
             and not str(v.get("precedence") or "").strip()]
    if multi:
        notes.append(f"Validation test(s) {multi[:5]} declare more than one criterion and no "
                     "precedence rule. Confirm a rule was fixed before collection.")
else:
    notes.append("No validation results recorded — the validation-outcome checks do not apply.")

# ------------------------------------------------------- differentiation stance
# 01-idea criterion 9. `category` — a clear category idea with no differentiating position
# yet — is a VALID starting state, and what makes it valid is that something eventually closes
# it. Unclosed, it is a deferral no gate ever collects, and the run delivers a recommendation
# for a product with no stated reason to exist.
stance = (state.get("project") or {}).get("differentiation_stance", "")
if ERA >= 2:
    check("differentiation stance is recorded", str(stance).strip() in ("category", "committed"),
          f"state.project.differentiation_stance is '{stance}' — must be `category` or "
          "`committed` (01-idea criterion 9). `vague` is a gate failure, not a delivery state")

if str(stance).strip() == "category":
    resolved = (state.get("project") or {}).get("differentiation_resolved_by", "")
    check("a `category` stance was resolved, or the research is stated to have found none",
          bool(str(resolved).strip()),
          "differentiation_resolved_by is empty. The stance was recorded as `category` — the "
          "operator asked the research to find the differentiation — and 07-strategy must name "
          "the option that supplies it, or record `not found` as a finding")

# --------------------------------------------------- late-generated solution options
# Modules 02-06 research one direction; 07-strategy then generates options. A generated option
# that wins is frequently the RIGHT answer — it is what a run looks like when the evidence
# redirected it. What it is not is comparably evidenced, and the scores look identical on the
# page either way.
opts = outputs.get("solution_options") or []
if isinstance(opts, list) and opts:
    no_prov = [o.get("id", "?") for o in opts
               if isinstance(o, dict)
               and o.get("provenance") not in ("carried_from_research", "generated_here")]
    if ERA >= 2:
        check("every solution option records its provenance", not no_prov,
              f"{no_prov[:5]} — must be `carried_from_research` or `generated_here` "
              "(07-strategy criterion 8)")
    elif no_prov:
        notes.append("Solution options carry no provenance. The mechanism postdates this run's "
                     "schema era, so it is not required of it — but if any option was generated "
                     "in 07-strategy rather than researched by 02-06, it was scored against "
                     "options that had five modules each and nothing said so.")

    generated = [o for o in opts
                 if isinstance(o, dict) and o.get("provenance") == "generated_here"]
    if generated:
        thin = [o.get("id", "?") for o in generated if not (o.get("unresearched") or [])]
        check("every generated option names the research it did not receive", not thin,
              f"{thin[:5]} are marked generated_here with an empty `unresearched` list. The "
              "asymmetry against options that had five modules each is the comparison's own "
              "strongest objection and it is invisible unless written down")

    # The asymmetry rule fires on the WINNER, so an unmarked winner switches it off silently
    # and the state file looks identical either way. Requiring the mark is what makes the rule
    # unbypassable by omission rather than by argument.
    marked = [o for o in opts if isinstance(o, dict) and o.get("chosen")]
    if ERA >= 2:
        check("exactly one solution option is marked chosen", len(marked) == 1,
              f"{len(marked)} options carry `chosen: true`. The generated-option asymmetry rule "
              "fires on the winner — with no winner marked it never fires, and nothing in the "
              "run looks wrong")
    elif not marked:
        notes.append("No solution option is marked `chosen`. The mechanism postdates this run's "
                     "schema era, so it is not required of it — but the generated-option "
                     "asymmetry rule cannot fire without it.")

    winners = [o for o in marked if o.get("provenance") == "generated_here"]
    unstated = [o.get("id", "?") for o in winners
                if not str(o.get("asymmetry_effect") or "").strip()]
    if winners:
        check("a generated option that wins states whether the win survives the missing research",
              not unstated,
              f"{unstated[:5]} won without `asymmetry_effect`. Re-score with its unresearched "
              "criteria at the lowest value any researched option scored: if it still wins the "
              "result is robust, and if it does not, the win rests on the gap")

# ------------------------------------------------------------- directive tension
# A directive is honored, never overridden. Evidence that one is costing the opportunity is
# the operator's to act on, and they cannot act on what they were not told.
for d in directives:
    if not isinstance(d, dict):
        continue
    t = d.get("tension")
    if not isinstance(t, dict):
        continue
    if not t.get("surfaced_to_operator"):
        notes.append(f"Directive {d.get('id', '?')} has recorded tension that was never "
                     "surfaced to the operator. Evidence a constraint is costing the "
                     "opportunity is theirs to act on.")
    if not str(t.get("what_it_costs") or "").strip():
        notes.append(f"Directive {d.get('id', '?')} records a tension with no size. A "
                     "directive kept without a number attached is kept without a decision.")

# ------------------------------------------------------------------ readiness
# A complete specification is not permission to build. The two are confused every time,
# because they arrive together — the package is finished, it looks finished, and finished
# reads as authorized.
readiness = run.get("readiness")
if isinstance(readiness, dict):
    if readiness.get("development_authorized") and not isinstance(readiness.get("override"), dict):
        check("development_authorized is not set by the run", False,
              "state.run.readiness.development_authorized is true with no recorded operator "
              "override. No run sets this field. An operator may authorize without the "
              "commercial gate — recorded as {by, at, basis}, never inferred from the "
              "specification being complete")
    incomplete = [k for k in ("research_ready", "product_definition_ready", "engineering_ready")
                  if not readiness.get(k)]
    if not incomplete and not readiness.get("commercially_validated") \
            and not str(readiness.get("blocked_on") or "").strip():
        check("an engineering-ready, commercially unvalidated run names what it is blocked on",
              False,
              "readiness reports the specification complete and the commercial gate not passed, "
              "and blocked_on is empty. A count of ticked engineering boxes says the product is "
              "specified; it says nothing about whether anyone will pay for it")
elif ERA >= 2:
    notes.append("state.run.readiness is not recorded. engine/handoff.md defines five states, "
                 "and only three of them are the run's to establish.")

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

# Three outcomes, not two. A run that entered conditional_continuation has a complete and
# honestly marked artifact set AND an unresolved gate. Reporting that as a plain pass would
# claim a validation the run does not have; reporting it as a failure would say the work is
# unusable, which is equally untrue. Exit 2 is neither success nor failure.
if CONDITIONAL:
    print("  All run checks pass — DELIVERABLE, CONDITIONALLY.")
    print(f"  Gate unresolved and deliberately open: {', '.join(conditional)}")
    print("  The artifact set is complete and honestly marked. The run is NOT validated.")
    print("  Exit 2 is not 0 and not 1. Automation must treat it as neither.")
    sys.exit(2)

print("  All run checks pass.")
