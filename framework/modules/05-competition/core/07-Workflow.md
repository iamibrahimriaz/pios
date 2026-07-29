---
Title: Workflow
Module: 05-competition
Section: core
Category: Procedure
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: The executable step-by-step procedure for running the Competition module.
Audience:
  - AI Agents
Prerequisites:
  - 05-competition/core/06-Framework.md
  - engine/state-schema.yaml
Outputs:
  - projects/<slug>/research/05-competition.md
  - state.outputs.competitor_matrix
Related Modules:
  - 06-business
  - 07-strategy
Tags:
  - Competition
  - Workflow
  - Procedure
---

# Workflow

---

# Overview

`06-Framework.md` defines the method — the Contest. This document is the procedure.

This is the last research module, and the first with five upstream inputs. Before doing
anything else, verify that those five inputs are consistent with each other. A market, a
segment and a problem set that disagree will produce a competitor list that looks
reasonable and answers the wrong question.

---

# Position in the Run

```
02-market ┐
03-user   ├→ [ 05-competition ] → 06-business → 07-strategy
04-problem┘
```

| | |
| --- | --- |
| Stage | `research` |
| Depends on | `02-market`, `03-user`, `04-problem` |
| Consumes | `market_definition`, `market_gaps`, `trends`, `segments`, `ranked_problems` |
| Produces | `competitor_matrix`, `feature_comparison`, `pricing_comparison`, `gap_analysis`, `positioning` |
| On fail | return to `02-market` |
| Human checkpoint | none — the `decide` stage checkpoint follows module 07 |

---

# Step 1 — Verify Upstream Consistency

All three upstream modules must be complete. Then check they agree:

| Check | Fails when |
| --- | --- |
| The prioritized segment sits inside `market_definition` | Module 03 drifted outside module 02's boundary |
| `ranked_problems` are attributed to that segment's persona | Module 04 ranked problems for a different user |
| `market_gaps` from module 02 relate to `ranked_problems` from module 04 | The market-level gap and the user-level problem are unconnected |

An inconsistency here is an upstream defect. Return rather than reconciling it silently —
this module is the first place the three research threads meet, and it is the last cheap
opportunity to notice they diverged.

Also read the module 04 verdict. If problems are `UNVALIDATED`, this module's gap analysis
inherits that uncertainty and must say so.

---

# Step 2 — Read Before Writing

1. `engine/evidence-policy.md`
2. `05-competition/core/03-Core-Principles.md`
3. `05-competition/core/06-Framework.md` — the Six Moves
4. `05-competition/core/09-Research-Methodology.md`
5. `05-competition/core/08-Questions-To-Answer.md`
6. `05-competition/knowledge/` — Competitor-Identification, Gap-Analysis, Pricing-Comparison
7. Domain vocabulary recorded by module 02 — search quality depends on it

---

# Step 3 — Enumerate and Classify

Work Moves 1 and 2.

Two mandatory entries that are not products:

- **Status quo** — taken directly from `current_workflow` in module 03
- **Non-consumption** — people with the problem who use nothing

Both need a row, a scale estimate, and serious treatment. Listing the status quo as a
formality and then ignoring it is the most common way this module misleads.

---

# Step 4 — Test Against Ranked Problems

Move 3. Build the problem coverage table.

This is the step to spend time on. If effort must be traded, take it from the feature
comparison — that table is secondary and exists only to establish table stakes.

Answer explicitly:

- Who solves P1 best today?
- Which ranked problems does nobody solve well?

---

# Step 5 — Price

Move 4. For each competitor: capture, or mark unavailable.

Date every pricing observation. Pricing pages change, and an undated figure is unusable
within a year.

Never write an unsourced estimate. Module 06 will treat any number here as an input to
the revenue model.

---

# Step 6 — Locate and Position

Moves 5 and 6.

The defensibility question is not optional: **if this works, what stops the incumbent
shipping it in six months?**

Answer honestly. "Nothing" is a valid and important finding — it means the opportunity is
a feature rather than a company, which module 07 must know before it commits to a
strategy.

Then write the positioning statement and run the competitor-claim test on it.

---

# Step 7 — Search the Graveyard

Who tried this and stopped?

Search for shutdowns rather than launches: "shutting down", "sunset", "no longer
maintained", "acquired and discontinued", plus the category vocabulary.

For each, record why — the reason is usually structural rather than executional, and it is
the cheapest lesson available in the run.

If nothing is found, record the search terms used. "No abandoned attempts found" means
something different from "did not look".

---

# Step 8 — Assemble and Write to State

Fill `13-Template.md` into `projects/<slug>/research/05-competition.md`.

```yaml
outputs:
  competitor_matrix:    # including status quo and non-consumption
  feature_comparison:   # table stakes
  pricing_comparison:   # sourced and dated, or marked unavailable
  gap_analysis:         # the gap, its cause, and its defensibility verdict
  positioning:          # one sentence, competitor-claim tested
```

Append to `state.evidence_log`, `state.assumptions`, `state.open_questions`.

---

# Step 9 — Review

Run all four passes of `engine/review-loop.md`.

The adversarial pass for this module:

- Did I find the competitors, or the ones that were easiest to find?
- Did I take the status quo seriously, or list it and move on?
- Is my gap real, or an artifact of a competitor list that missed someone?
- If the incumbent shipped this next quarter, what would we have left?
- Could my positioning statement appear on a competitor's homepage?
- Is the market already well served, and am I avoiding saying so?

The coherence pass: does the gap identified here correspond to a ranked problem from
module 04? A gap that does not map to a real problem is a market observation, not an
opportunity.

---

# Step 10 — Gate

Evaluate against `11-Quality-Gate.md` and universal gates U1–U6.

| Verdict | Action |
| --- | --- |
| Pass | Continue to Step 11 |
| Fail | Revise, or `return to 02-market` if the boundary is wrong. Three attempts, then halt |

---

# Step 11 — Hand Off

1. Append `05-competition` to `state.run.completed_modules`.
2. Record the defensibility verdict prominently — module 07 builds strategy on it.
3. Hand to `06-business`.

---

# Handoff Contract

| Consumer | Reads | Uses it for |
| --- | --- | --- |
| `06-business` | `pricing_comparison`, `competitor_matrix` | Price positioning and unit economics |
| `07-strategy` | `gap_analysis`, `positioning`, `competitor_matrix` | Choosing the approach and the MVP cut |
| `08-product` | `feature_comparison` | Table stakes that must exist |
| `11-growth` | `positioning`, category decision | Channel and messaging strategy |

The defensibility verdict is the single most consequential output. A strategy built on an
undefensible gap is a strategy with a six-month clock on it — module 07 must be able to
see that clock.

---

# Failure Modes

| Symptom | Cause | Fix |
| --- | --- | --- |
| Only direct competitors listed | Move 1 too narrow | Add substitutes, status quo, non-consumption |
| Status quo listed but not assessed | Treated as a formality | Score it in the coverage table like any competitor |
| Large feature table, no conclusion | Move 3 skipped | Score against ranked problems |
| Unsourced price figures | Move 4 shortcut | Source and date, or mark unavailable |
| Gap with no defensibility answer | Move 5 incomplete | Ask the six-month question |
| Generic positioning | Move 6 rushed | Apply the competitor-claim test |
| Gap does not map to any ranked problem | Coherence not checked | Reconcile with module 04 |

---

# When Evidence Is Thin

Competitors are among the most researchable subjects in the framework — public pricing,
public marketing, public reviews. Thin evidence here usually means the search was narrow,
not that the information does not exist.

Before declaring a competitor unresearchable, try: the domain vocabulary from module 02,
"alternatives to «product»" pages, review-site category listings, and forum threads where
the problem is discussed.

If pricing genuinely is not public, mark it unavailable and note what that implies — a
sales-led motion and a price floor.

---

> **Workflow Principle**
>
> Five inputs arrive at this module and one verdict leaves it.
>
> Check that the five agree before trusting the one.
