---
Title: Checklist
Module: 02-market
Section: core
Category: Verification
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Operational checklist for entering, running and exiting the Market module.
Audience:
  - AI Agents
  - Researchers
Prerequisites:
  - 02-market/core/07-Workflow.md
  - 02-market/core/11-Quality-Gate.md
Outputs:
  - Verified module completion
Related Modules:
  - 05-competition
Tags:
  - Market
  - Checklist
  - Verification
---

# Checklist

---

# Overview

`11-Quality-Gate.md` decides whether the module passed. This checklist is what to work
through **before** reaching the gate, so the gate confirms rather than discovers.

---

# Entry

- [ ] `01-idea` present in `state.run.completed_modules`
- [ ] `state.project.jurisdiction` is set — **not inferred**
- [ ] No blocking question open in `state.open_questions`
- [ ] `idea_brief` read
- [ ] `scope_boundaries` read
- [ ] `engine/evidence-policy.md` read
- [ ] `06-Framework.md` read
- [ ] `09-Research-Methodology.md` read
- [ ] Vertical pack loaded, if one exists for this domain

---

# Frame 1 — Bound

- [ ] Who — the population named
- [ ] What need — stated precisely, not as an adjective
- [ ] Where — jurisdiction, inherited from the brief
- [ ] Explicit exclusions listed, with reasons
- [ ] One borderline case ruled in or out
- [ ] Category name found, or its absence recorded as a finding
- [ ] Boundary does not exceed `scope_boundaries` from the brief

---

# Frame 2 — Regulate

- [ ] Applicable regimes identified
- [ ] Trigger stated for each regime
- [ ] **Concrete obligations** stated, not just regime names
- [ ] Licensing or certification requirements checked
- [ ] Cost and time to clear any barrier estimated
- [ ] Data residency and cross-border constraints checked
- [ ] Direction of travel assessed
- [ ] **Explicitly answered:** does regulation exclude a segment from the brief?
- [ ] Written so module 09 can act on it without re-reading this document

---

# Frame 3 — Size

- [ ] TAM produced
- [ ] SAM produced
- [ ] SOM produced
- [ ] Every figure shows its derivation
- [ ] Every input in every derivation carries a tag
- [ ] Method stated — bottom-up, top-down, or both
- [ ] Any external figure had its boundary compared to Frame 1
- [ ] Where both methods were used, disagreement recorded rather than resolved silently
- [ ] Load-bearing input identified
- [ ] Honest assessment of how much weight the sizing can bear

---

# Frame 4 — Trend

- [ ] At least three trends
- [ ] Each states a direction
- [ ] Each carries evidence
- [ ] Each states an implication
- [ ] **At least one trend argues against the idea**
- [ ] Any decision-critical trend has two independent sources
- [ ] Timing assessment made — early, on time, or late

---

# Frame 5 — Gap

- [ ] Underserved segments identified
- [ ] Each gap states **why it persists**
- [ ] Any prior failed attempt found and its reason recorded
- [ ] Structural vs temporary assessed
- [ ] Most promising gap named
- [ ] No competitor names, features, or pricing tables — that is module 05

---

# Assembly

- [ ] `13-Template.md` filled into `projects/<slug>/research/02-market.md`
- [ ] Every `«placeholder»` replaced
- [ ] Every guidance comment removed
- [ ] Every factual claim carries exactly one tag
- [ ] Every `[verified]` resolves to a row in the Sources table
- [ ] Contradicting Evidence section non-empty
- [ ] Written for a reader with no access to this conversation

---

# State

- [ ] `outputs.market_definition` written
- [ ] `outputs.tam_sam_som` written
- [ ] `outputs.trends` written
- [ ] `outputs.regulatory_landscape` written
- [ ] `outputs.market_gaps` written
- [ ] `state.evidence_log` appended
- [ ] `state.assumptions` appended — every unsourced figure, with a validation method
- [ ] `state.open_questions` appended
- [ ] Domain vocabulary recorded for later modules

---

# Review

- [ ] Completeness pass run
- [ ] Evidence pass run
- [ ] Adversarial pass run — and produced something
- [ ] Coherence pass run — checked against `idea_brief` specifically
- [ ] Verdict recorded

---

# Gate

- [ ] Criterion 1 — boundary, not adjective
- [ ] Criterion 2 — sizing sourced or explicitly assumed
- [ ] Criterion 3 — three trends with direction, including one unfavorable
- [ ] Criterion 4 — regulatory constraints identified concretely
- [ ] Universal gates U1–U7
- [ ] Verdict recorded in `state.run`

---

# Exit

- [ ] `02-market` appended to `state.run.completed_modules`
- [ ] Handoff contract satisfied for `03-user`, `05-competition`, `06-business`, `09-technology`
- [ ] Regulatory section written for an engineer who will read it seven modules later

---

# Red Flags

Re-run the module if any of these are true:

- [ ] The market definition contains no exclusions
- [ ] A figure appears with no arithmetic behind it
- [ ] An analyst TAM was adopted without checking its boundary
- [ ] Every trend is favorable
- [ ] A gap has no explanation for why it persists
- [ ] The regulatory section is a list of acronyms
- [ ] Competitor names appear with feature comparisons
- [ ] The market described is broader than the brief's segment

---

> **Checklist Principle**
>
> The gate should confirm what the checklist already established.
>
> If the gate is where problems are first discovered, the work was not done.
