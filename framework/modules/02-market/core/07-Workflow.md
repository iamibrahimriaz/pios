---
Title: Workflow
Module: 02-market
Section: core
Category: Procedure
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: The executable step-by-step procedure for running the Market module.
Audience:
  - AI Agents
Prerequisites:
  - 02-market/core/06-Framework.md
  - engine/state-schema.yaml
Outputs:
  - projects/<slug>/research/02-market.md
  - state.outputs.market_definition
Related Modules:
  - 03-user
  - 05-competition
Tags:
  - Market
  - Workflow
  - Procedure
---

# Workflow

---

# Overview

`06-Framework.md` defines the method. This document is the procedure.

This is the first research module. Unlike `01-idea`, it does not end at a human
checkpoint — it hands directly to the rest of the research stage.

---

# Position in the Run

```
01-idea → ⏸ checkpoint → [ 02-market ] → 03-user → 04-problem → 05-competition
```

| | |
| --- | --- |
| Stage | `research` |
| Depends on | `01-idea` |
| Consumes | `idea_brief`, `scope_boundaries` |
| Produces | `market_definition`, `tam_sam_som`, `trends`, `regulatory_landscape`, `market_gaps` |
| On fail | return to `01-idea` |
| Human checkpoint | none |

`03-user` may run in parallel with this module. `05-competition` may not — it needs this
module's output.

---

# Step 1 — Verify Upstream

Before starting:

1. Confirm `01-idea` appears in `state.run.completed_modules`.
2. Confirm `state.project.jurisdiction` is set. **If it is empty, stop** — return to
   `01-idea`. Do not proceed by inferring a jurisdiction.
3. Confirm no blocking question remains open in `state.open_questions`.
4. Read `idea_brief` and `scope_boundaries` from state.

> If the brief's problem statement is vague, this module will produce a vague market.
> Returning now costs minutes. Discovering it at module 06 costs four modules.

---

# Step 2 — Read Before Writing

1. `engine/evidence-policy.md` — the tagging rules
2. `02-market/core/03-Core-Principles.md`
3. `02-market/core/06-Framework.md` — the Five Frames
4. `02-market/core/08-Questions-To-Answer.md`
5. `02-market/core/09-Research-Methodology.md` — sourcing rules for this domain
6. `02-market/knowledge/` — as needed: TAM, SAM, SOM, PESTEL, Five-Forces
7. `framework/packs/<vertical>/` if a pack is loaded for this domain

---

# Step 3 — Run the Five Frames

Execute `06-Framework.md` in order. Write as you go.

| Frame | Writes to |
| --- | --- |
| 1. Bound | draft — market definition |
| 2. Regulate | draft — regulatory landscape |
| 3. Size | draft — TAM/SAM/SOM with derivations |
| 4. Trend | draft — trends |
| 5. Gap | draft — market gaps |

**Frame 2 has an early exit.** If regulation excludes a segment named in the idea brief,
stop and return to `01-idea` rather than completing the remaining frames on a segment
that cannot be served.

---

# Step 4 — Assemble

Fill `13-Template.md` into `projects/<slug>/research/02-market.md`.

Every factual claim carries exactly one tag. Every `[verified]` claim resolves to an
entry in the Sources table — if a reader cannot retrieve it, it was not verified.

---

# Step 5 — Write to State

```yaml
outputs:
  market_definition:     # boundary, inclusions, exclusions, category name
  tam_sam_som:           # figures with derivations and tags
  trends:                # list, each with direction and evidence
  regulatory_landscape:  # regimes, obligations, barriers, direction
  market_gaps:           # each with the reason it persists
```

Append to `state.evidence_log` — every claim, its tag, its source, and whether it is
load-bearing.

Append to `state.assumptions` — every unsourced figure, with a validation method.

Append to `state.open_questions` — anything that could not be established.

---

# Step 6 — Review

Run all four passes of `engine/review-loop.md`.

The adversarial pass for this module asks:

- Is my market boundary drawn to make the number look good?
- Did I adopt a market report's TAM without checking what boundary it used?
- Which of my trends would a skeptic say I selected?
- Is there a structural reason this market has stayed unserved that I have not found?
- If this market is actually unattractive, which claim in my analysis is the giveaway?

The coherence pass matters here specifically: does anything in this analysis contradict
the idea brief? If the brief named a segment and the market work quietly widened it,
that is a defect — resolve it explicitly.

---

# Step 7 — Gate

Evaluate against `11-Quality-Gate.md` and universal gates U1–U6.

| Verdict | Action |
| --- | --- |
| Pass | Continue to Step 8 |
| Fail | Revise, or `return to 01-idea` if the defect is upstream. Three attempts, then halt |

---

# Step 8 — Hand Off

1. Append `02-market` to `state.run.completed_modules`.
2. Record the domain vocabulary learned — it improves search quality in every later module.
3. Hand to `03-user` and `05-competition`.

---

# Handoff Contract

| Consumer | Reads | Uses it for |
| --- | --- | --- |
| `03-user` | `market_definition` | Bounding which segments are in scope |
| `05-competition` | `market_definition`, `market_gaps`, `trends` | Identifying who competes, and where the opening is |
| `06-business` | `tam_sam_som` | Revenue modeling and price positioning |
| `09-technology` | `regulatory_landscape` | Structural constraints on data model and architecture |

The handoff to `09-technology` is easy to under-serve. It happens seven modules later, and
by then nobody will re-read this document. Write the regulatory section so an engineer
can act on it: concrete obligations, not regime names.

---

# Failure Modes

| Symptom | Cause | Fix |
| --- | --- | --- |
| Market is an adjective, not a boundary | Frame 1 rushed | Apply the borderline-case test |
| TAM from a report, no derivation | Frame 3 shortcut | Rebuild bottom-up |
| Every trend supports the idea | Adversarial pass skipped | Find the counter-trend |
| Regulatory section names regimes only | Frame 2 too shallow | State concrete obligations |
| Competitor names and features appear | Doing module 05's job | Move it to 05, keep this at market level |
| Jurisdiction inferred | Step 1 skipped | Return to `01-idea` |

---

# When Retrieval Is Unavailable

State it plainly, size bottom-up from stated assumptions, tag every figure
`[assumption: needs validation]`, set confidence to `low`, and add the sizing to
`state.open_questions`.

An honest unsourced market analysis is workable. A fabricated one poisons every module
that consumes it.

---

> **Workflow Principle**
>
> This module hands a boundary to four other modules.
>
> Draw it carelessly and four modules inherit the error without ever seeing it.
