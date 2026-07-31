---
Title: Checklist
Module: 05-competition
Section: core
Category: Verification
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Operational checklist for entering, running and exiting the Competition module.
Audience:
  - AI Agents
  - Researchers
Prerequisites:
  - 05-competition/core/07-Workflow.md
  - 05-competition/core/11-Quality-Gate.md
Outputs:
  - Verified module completion
Related Modules:
  - 06-business
  - 07-strategy
Tags:
  - Competition
  - Checklist
---

# Checklist

---

# Entry

- [ ] `02-market`, `03-user`, `04-problem` all in `state.run.completed_modules`
- [ ] `market_definition` read
- [ ] `market_gaps` and `trends` read
- [ ] `segments` read — the prioritized one identified
- [ ] `ranked_problems` read
- [ ] `current_workflow` read — this supplies the status quo competitor
- [ ] Module 04 verdict noted — if `UNVALIDATED`, the gap analysis inherits that
- [ ] Domain vocabulary from module 02 collected for search

**Upstream consistency**

- [ ] The prioritized segment sits inside `market_definition`
- [ ] `ranked_problems` belong to that segment's persona
- [ ] `market_gaps` relate to `ranked_problems`

---

# Move 1 — Enumerate

- [ ] Direct competitors searched
- [ ] Indirect competitors searched
- [ ] Substitutes searched — services, agencies, people, spreadsheets
- [ ] **Status quo taken from `current_workflow`**
- [ ] **Non-consumption considered** — those with the problem using nothing
- [ ] "Alternatives to X" pages checked
- [ ] Job postings checked for tools in use
- [ ] Forum recommendations checked
- [ ] At least five entries total
- [ ] At least three of the five types represented
- [ ] Every entry sourced

---

# Move 2 — Classify

- [ ] Every entry typed
- [ ] Displacement bar noted per type — better, or worth the disruption
- [ ] Scale estimated per competitor where findable

---

# Move 3 — Test

- [ ] Problem coverage table built against `ranked_problems`
- [ ] Every competitor scored on every ranked problem
- [ ] **Status quo scored like any other competitor**
- [ ] Scores based on user evidence, not vendor claims
- [ ] "Who solves P1 best today" answered
- [ ] "Which problems does nobody solve well" answered
- [ ] Residual pain noted where a competitor solves a problem *partly*

---

# Move 4 — Price

- [ ] Every competitor: price sourced, or explicitly marked unavailable
- [ ] **Every price dated**
- [ ] Pricing model recorded per competitor
- [ ] Tiers recorded where they exist
- [ ] "Contact us" pricing noted with its implication
- [ ] Free products: funding model identified
- [ ] Market price range stated
- [ ] **No silent estimates** — every approximation carries a source or `[inferred]` tag

---

# Move 5 — Locate

- [ ] Gap identified
- [ ] Gap maps to a specific ranked problem
- [ ] Gap applies to a specific segment
- [ ] Reason the gap exists stated
- [ ] Reason incumbents have not closed it stated
- [ ] **Six-month question answered:** what stops them shipping this?
- [ ] Defensibility verdict recorded — including "not defensible" if true
- [ ] What protects us, if anything, named

---

# Move 6 — Position

- [ ] Positioning statement written in full form
- [ ] **Competitor-claim test applied** — could C1 say the same thing?
- [ ] Category decision made — existing or new
- [ ] Education cost noted if creating a new category

---

# Additional

- [ ] Strengths and weaknesses assessed for the two or three that matter
- [ ] Structural reason for each weakness identified
- [ ] Threats table completed with early warning signs
- [ ] **Graveyard searched** — and search terms recorded if nothing found
- [ ] Reason each dead product stopped, where findable
- [ ] Contradicting evidence section non-empty

---

# Assembly

- [ ] `13-Template.md` filled into `projects/<slug>/research/05-competition.md`
- [ ] §1 written last, summarizing the competitive position
- [ ] Every `«placeholder»` replaced
- [ ] Every guidance comment removed
- [ ] Vendor claims distinguished from user-reported capability
- [ ] Every claim carries exactly one tag
- [ ] Every `[verified]` resolves to a row in Sources

---

# State

- [ ] `outputs.competitor_matrix` written
- [ ] `outputs.feature_comparison` written
- [ ] `outputs.pricing_comparison` written
- [ ] `outputs.gap_analysis` written, with the defensibility verdict
- [ ] `outputs.positioning` written
- [ ] `state.evidence_log` appended
- [ ] `state.assumptions` appended
- [ ] `state.open_questions` appended
- [ ] Defensibility verdict recorded prominently for `07-strategy`

---

# Review

- [ ] Completeness pass run
- [ ] Evidence pass run
- [ ] Adversarial pass run — and produced something
- [ ] Coherence pass run — gap maps to a ranked problem
- [ ] Verdict recorded

---

# Gate

- [ ] Criterion 1 — five competitors across types, sourced
- [ ] Criterion 2 — pricing sourced and dated, or marked unavailable
- [ ] Criterion 3 — status quo evaluated, not just listed
- [ ] Criterion 4 — gap articulated with the six-month question answered
- [ ] Cross-module coherence checks
- [ ] Universal gates U1–U7
- [ ] Verdict recorded in `state.run`

---

# Exit

- [ ] `05-competition` appended to `state.run.completed_modules`
- [ ] Handoff satisfied for `06-business`, `07-strategy`, `08-product`, `11-growth`
- [ ] Research stage complete — the run now moves to commitment

---

# Red Flags

Re-run the module if any of these are true:

- [ ] Every competitor is a funded software product
- [ ] The status quo appears in the matrix but nowhere else
- [ ] Non-consumption was never considered
- [ ] The feature table is larger than the problem coverage table
- [ ] A price appears with no source or date
- [ ] Vendor marketing is quoted as capability
- [ ] The gap has no stated reason for existing
- [ ] The six-month question is unanswered
- [ ] The positioning statement could appear on a competitor's homepage
- [ ] No graveyard search was performed
- [ ] The gap does not correspond to any ranked problem

---

> **Checklist Principle**
>
> The competitors that beat new products are the ones a category search
> never returns.
>
> Half this list exists to make sure they were looked for.
