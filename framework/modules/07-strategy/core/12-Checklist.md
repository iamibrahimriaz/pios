---
Title: Checklist
Module: 07-strategy
Section: core
Category: Verification
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Operational checklist for entering, running and exiting the Strategy module.
Audience:
  - AI Agents
  - Product Managers
Prerequisites:
  - 07-strategy/core/07-Workflow.md
  - 07-strategy/core/11-Quality-Gate.md
Outputs:
  - Verified module completion
Related Modules:
  - 08-product
Tags:
  - Strategy
  - Checklist
---

# Checklist

---

# Entry

- [ ] `04-problem`, `05-competition`, `06-business` in `state.run.completed_modules`
- [ ] Sharpest problem read, **with its evidence standing**
- [ ] `gap_analysis` read, **with the defensibility verdict**
- [ ] `business_model` read, **with the viability verdict and price**
- [ ] `state.run` checked for a **declared shortfall** from module 04
- [ ] Three inherited conditions recorded before any work begins
- [ ] `06-Framework.md` and `09-Research-Methodology.md` read

---

# Move 1 — Diverge

- [ ] At least three options generated
- [ ] Shapes worked deliberately — narrow tool, replacement, layer, service, segment
- [ ] Each states what would be built **first**
- [ ] **Different-first-build test passed** — the first builds differ
- [ ] **Advocate test passed** — a genuine case can be made for each
- [ ] Each records problems solved, price supported, defensibility, biggest risk

---

# Move 2 — Compare

- [ ] Criteria drawn from modules 04, 05, 06
- [ ] Weights assigned and stated
- [ ] Every scoring cell traces to a research finding
- [ ] "Survives if the assumed problem is wrong" included where module 04 declared a shortfall

---

# Move 3 — Choose

- [ ] One option chosen
- [ ] Reasoning references the comparison and the ranked problems
- [ ] **What we lose by rejecting each option recorded**
- [ ] The bet stated — the belief this depends on
- [ ] Reversal trigger stated
- [ ] Reversibility and its cost assessed
- [ ] Decision written to `state.decisions` with alternatives rejected

---

# Move 4 — Cut

- [ ] Capabilities sorted above and below the line
- [ ] Cut principle stated in one sentence
- [ ] **Workflow walked step by step against included capabilities**
- [ ] **End-to-end test answered — and the answer is yes**
- [ ] Minimality checked — the line is a cut, not a ranking
- [ ] What the MVP proves stated
- [ ] **What the MVP does not prove stated**
- [ ] Hardest capability to cut, and why it went, recorded
- [ ] Everything below the line carried to the roadmap

---

# Move 5 — Bound

- [ ] Capabilities not being built listed
- [ ] Segments not being served listed
- [ ] Real problems from module 04 not being solved listed
- [ ] Integrations not being built listed
- [ ] Each has a reason
- [ ] Each has a reconsider trigger, or is marked permanent

---

# Move 6 — Register

**Risks**

- [ ] Commercial, technical, regulatory and market risks covered
- [ ] Likelihood rated **before** impact
- [ ] Ratings differentiated — not all medium
- [ ] Mitigation stated per risk
- [ ] **Early warning sign stated per risk**
- [ ] Accepted risks marked as accepted
- [ ] Inherited risk: assumed problem, if applicable
- [ ] Inherited risk: undefensible gap with a timescale, if applicable
- [ ] Inherited risk: module 06's viability conditions

**Sequence**

- [ ] **Milestone Zero present if the sharpest problem is assumed**
- [ ] M0 built from module 04's validation plan
- [ ] Each milestone states what it teaches
- [ ] Independently shippable milestones identified
- [ ] Critical path stated

**Stop conditions**

- [ ] Observable signal named
- [ ] Specific threshold stated
- [ ] Owner and review point named
- [ ] Falsifiable — a real result could trigger it

---

# Assembly

- [ ] `13-Template.md` filled into `projects/<slug>/research/07-strategy.md`
- [ ] §1 written last
- [ ] Every claim either derived with a citation, or declared as a bet
- [ ] **Confidence language checked against source modules** — no laundering
- [ ] Contradicting evidence section non-empty
- [ ] Every `«placeholder»` replaced
- [ ] Every guidance comment removed

---

# State

- [ ] `outputs.solution_options` written, including rejected
- [ ] `outputs.chosen_approach` written
- [ ] `outputs.mvp_definition` written
- [ ] `outputs.non_goals` written
- [ ] `outputs.risk_register` written
- [ ] `outputs.roadmap` written
- [ ] `state.decisions` appended with alternatives rejected
- [ ] `state.assumptions` appended with every bet
- [ ] `state.open_questions` appended with checkpoint decisions

---

# Review

- [ ] Completeness pass run
- [ ] Evidence pass run
- [ ] Adversarial pass run — and produced something
- [ ] Coherence pass run — approach fits the inherited price and gap
- [ ] Verdict recorded

---

# Gate

- [ ] Criterion 1 — three genuinely distinct options
- [ ] Criterion 2 — choice traced to ranked problems
- [ ] Criterion 3 — MVP cut with reasoning and a passing end-to-end test
- [ ] Criterion 4 — explicit non-goals
- [ ] Criterion 5 — risks rated, mitigated, with early warnings
- [ ] Criterion 6 — expected winner recorded before scoring, **with `independence` set**
- [ ] Criterion 7 — if 04-problem declared a shortfall, the weight it changed is named
- [ ] Criterion 8 — every option marked `carried_from_research` or `generated_here`
- [ ] A generated option lists which modules never examined it and what each would have tested
- [ ] If a generated option WINS: the re-score test run, `asymmetry_effect` recorded, and a path chosen — research pass, or a validation milestone placed first and blocking
- [ ] Criterion 9 — if 01-idea recorded `category`, the option supplying the differentiation is named, or `not found` is stated as a finding
- [ ] Milestone Zero check
- [ ] Confidence laundering check
- [ ] Universal gates U1–U7
- [ ] Verdict recorded in `state.run`

---

# Human Checkpoint

- [ ] §13 written and decidable
- [ ] Proposal stated in one sentence
- [ ] Non-goals stated
- [ ] Load-bearing assumption named
- [ ] Weak foundations stated plainly — assumed problem, undefensible gap, conditional viability
- [ ] Decisions presented as **options with a recommendation**, not as conclusions
- [ ] **Stopped and waited**

---

# Exit

- [ ] Operator decisions applied
- [ ] Cut re-tested end-to-end if it changed
- [ ] Approved decisions recorded in `state.decisions`
- [ ] `07-strategy` appended to `state.run.completed_modules`
- [ ] Handoff satisfied for `08-product`, `09-technology`, `10-execution`

---

# Red Flags

Re-run the module if any of these are true:

- [ ] Two options exist only to lose
- [ ] All options would begin by building the same thing
- [ ] The chosen option's reasoning cites nothing
- [ ] No record of what rejected options offered
- [ ] More than a third of capabilities sit above the MVP line
- [ ] The end-to-end test is asserted rather than walked
- [ ] "What the MVP does not prove" is missing
- [ ] There are no non-goals
- [ ] Every risk is rated medium
- [ ] Any risk lacks an early warning sign
- [ ] The problem is assumed and there is no Milestone Zero
- [ ] This document sounds more confident than modules 04, 05 or 06
- [ ] The checkpoint presents a conclusion rather than a decision

---

> **Checklist Principle**
>
> The last item is the most important one.
>
> A checkpoint that presents a decision already made is not a checkpoint.
