# A completed run cannot record that events superseded it

**Date:** 2026-09-14
**Source:** One completed run whose product was subsequently built, where the build reversed the differentiator the run had selected
**Produced by:** Claude Opus 5 (1M context), Claude Code. **Grounded in a completed run, not reasoned from documentation.**

> **No project content appears in this document.** The run is referred to as Run 2. No product, market, sector, customer, competitor, vendor, figure or recognizable idea is named, and the defect is stated so that it stands without the run in front of you.

---

## Decision summary

| # | Defect | Owner | Blast radius | Recommendation | Status |
| --- | --- | --- | --- | --- | --- |
| **D11** | A completed run has no way to record that it was superseded by events, so it keeps reading as current after it stops being true | `state-schema` | **Whole run** | **Adopt** | ### ✅ Implemented |

---

## D11 — Supersession by events is unrecordable

### The defect

**A run records what was established as true at the moment it completed. Nothing in the schema lets it record that the world moved afterwards.**

Every status field a run carries describes the *research*: which modules completed, which gates passed, which assumptions are bets, whether development is authorized. There is no field, marker or convention that answers a different question — **is this package still a description of the thing it specified?**

The consequence is silent and one-directional. A completed run reads as current forever. A reader — human or agent — opening `CLAUDE.md` or the executive summary has no signal that the specification and reality have parted, and **the more confident the run's prose, the more convincingly it misleads.** Strong assertions age worst: a document that says a property holds *by construction* is exactly the document a reader will not think to verify.

### Why the existing mechanisms do not cover it

| Mechanism | Why it does not apply |
| --- | --- |
| `_superseded-*/` archive | Records supersession **within** the research — a strategy re-entry replacing an earlier option. It has no vocabulary for supersession **from outside** the run |
| `friction_log` | Records where the framework blocked the agent **during** the run. It is closed when the run is |
| `declared_shortfall` | Scoped to one module, and to evidence that was never obtained — not to evidence that expired |
| `corrections` | A defect found **during** the run, by review, checkpoint, operator or a later module. Closed when the run is |
| `rederivations` | **The closest existing mechanism, and it does not reach.** A premise that moved at a checkpoint, with conclusions retested and deliverables reissued. It is the right *shape* and the wrong *lifecycle*: it assumes modules can be re-run. After delivery nobody is re-running anything, so "retest the conclusions" is the wrong response — the right one is to stop the package being read as current |
| Readiness states | Describe whether the package is ready to hand over, not whether it still matches what was handed over |

### Why this is in scope

The framework produces the pre-development package **and stops there**, and this proposal does not move that boundary. It adds **no** capability to describe, direct or verify development work. It adds one thing only: **the ability for a run to state that it can no longer be relied upon as current.**

That is Principle 16 — *accurate uncertainty outranks unsupported confidence* — applied to time. A run that has been overtaken and cannot say so is asserting unsupported confidence, and doing it passively, which is worse than doing it in prose.

### What must not be built instead

**The obvious fix is the wrong one.** The tempting version is a re-sync mechanism: a module, step or skill that reads the built system and updates the deliverables to match. That is the prohibited class — it produces a working system's documentation rather than establishing what is true, and it would arrive with exactly the reasonable framing the authoring guidance warns about.

**The distinction to hold:** recording *that* a package was superseded is research hygiene. Recording *what it was superseded by* is engineering documentation, and belongs to the project that received the package.

### Proposed change

A single optional state key, and one line of guidance.

```yaml
superseded:
  recorded: "«date»"
  by: "development" | "market" | "operator_decision" | "external_event"
  summary: >-
    «One paragraph, written so a reader knows what not to rely on.»
  still_current: ["«deliverable»", "…"]      # optional, default: nothing asserted
  no_longer_current: ["«deliverable»", "…"]
  authority_now: "«where the current description lives, if anywhere»"
```

- **Optional and additive.** Absent on every existing run. **No `state.version` bump** — `AUTHORING.md` line 85 reserves that for keys that become *required*, and this one never is. No older run can fail for lacking it.
- **`authority_now` is a pointer, never content.** It names where the current truth lives; it does not import it. This is the field that keeps the boundary.
- **No validator check was added**, and the earlier draft of this proposal was wrong to suggest one. Enforcing that entry documents carry a notice would require the validator to know which files are entry documents — a layout assumption it deliberately does not make. The marker earns its value by being read, not by being enforced.

### What was changed

`framework/engine/state-schema.yaml` — one optional commented block, 31 lines, placed immediately after `corrections` so the distinction between in-run and post-delivery change is visible at the point of use. `validate.py` exits 0 before and after.

### What it would break

Nothing. No gate changes, no vocabulary changes, no readiness state changes, no module changes. `development_authorized` is untouched and still never set by a run.

### The argument against adopting it

**A run that has been overtaken could simply be left alone**, with the current description kept in the receiving project. That is defensible and costs nothing to implement.

It fails on the case that produced this proposal: **the run is what gets handed to the next person.** A new engineer is given the research package, not a tour of which parts to disbelieve. Absent a marker, they build the superseded product — and the run's own strength of assertion is what convinces them to.

### Evidence for the reduction in uncertainty this change permits

Per the authoring rule, a change that alters what a run records must name its evidence. This change **increases** recorded uncertainty rather than reducing it: it adds a way to say *"this is no longer reliable"* and adds no way to say anything is more certain than before. No evidence is required to justify a reduction, because none is claimed.

---

## Not proposed

**A re-sync module, step, template or skill.** See above. **A field that imports as-built detail into the run.** `authority_now` is a pointer by design; widening it to carry content is how this becomes the thing the framework refuses to be.
