---
Title: Checklist
Module: 01-idea
Section: core
Category: Verification
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Operational checklist for entering, running, and exiting the Idea module.
Audience:
  - AI Agents
  - Product Managers
Prerequisites:
  - 01-idea/core/07-Workflow.md
  - 01-idea/core/11-Quality-Gate.md
Outputs:
  - Verified module completion
Related Modules:
  - 02-market
Tags:
  - Idea
  - Checklist
  - Verification
---

# Checklist

---

# Overview

`11-Quality-Gate.md` decides whether the module passed. This checklist is what to work
through **before** reaching the gate, so the gate is a confirmation rather than a
discovery.

---

# Entry

Before starting:

- [ ] `projects/<slug>/` exists
- [ ] `state.yaml` created from `engine/state-schema.yaml`
- [ ] `state.project.raw_idea` recorded **verbatim**
- [ ] `state.run.current_stage` set to `frame`
- [ ] `constitution/core/` read
- [ ] `engine/evidence-policy.md` read
- [ ] `01-idea/core/03-Core-Principles.md` read
- [ ] `01-idea/core/06-Framework.md` read

---

# Pass 1 — Capture

- [ ] Raw idea recorded exactly as given
- [ ] No tidying, summarizing, or "improving" applied
- [ ] Slug derived and directory created

---

# Pass 2 — Separate

- [ ] "So that what?" applied until the answer stopped changing
- [ ] Solution-as-proposed recorded
- [ ] Problem-it-implies recorded, separately
- [ ] If the problem sounds trivial when stated plainly, that is recorded rather than softened

---

# Pass 3 — Locate

- [ ] Jurisdiction — answered or asked
- [ ] Segment — answered or asked
- [ ] Buyer vs user — answered or asked
- [ ] Incumbent system — answered or asked
- [ ] Operational setting — answered or asked
- [ ] Regulated domain — answered or asked
- [ ] **Nothing in this list was guessed**

---

# Pass 4 — Surface

At least one assumption identified in each category:

- [ ] User — what people do today
- [ ] Problem — what hurts, and how much
- [ ] Demand — what people want
- [ ] Willingness to pay — what someone will fund
- [ ] Behavior — what people will change
- [ ] Technical — what is possible
- [ ] Access — what can be reached or obtained

And for each assumption recorded:

- [ ] Written to `state.assumptions`
- [ ] Statement, basis, consequence-if-false, and validation method all present
- [ ] Tagged per the evidence policy

---

# Pass 5 — Interrogate

- [ ] At least five questions generated
- [ ] Each passes the asking test — a different answer would change the work
- [ ] Each is answerable by the operator, not researchable by the agent
- [ ] Each is specific, not compound
- [ ] Ranked blocking vs deferrable
- [ ] Written to `state.open_questions`

---

# Pass 6 — Bound

- [ ] In scope stated
- [ ] Out of scope stated, with reasons
- [ ] Adjacent opportunities parked explicitly
- [ ] Checked: is this one product, or several bundled by ambition?

---

# Research

- [ ] Existence check performed, or explicitly recorded as not possible
- [ ] Searched using the domain's vocabulary, not only the operator's
- [ ] Any abandoned prior attempt noted, with the reason if findable
- [ ] No module 02–05 work performed
- [ ] Findings recorded at the depth they were actually established

---

# Brief Assembly

- [ ] `13-Template.md` filled into `projects/<slug>/research/01-idea.md`
- [ ] Every `«placeholder»` replaced
- [ ] Every guidance comment removed
- [ ] Every factual claim carries exactly one evidence tag
- [ ] No hedging language substituting for a tag
- [ ] Written for a reader with no access to this conversation

---

# State

- [ ] `outputs.idea_brief` written
- [ ] `outputs.clarifying_questions` written
- [ ] `outputs.initial_assumptions` written
- [ ] `outputs.scope_boundaries` written — the most commonly forgotten one
- [ ] `state.assumptions` appended
- [ ] `state.open_questions` appended
- [ ] `state.evidence_log` appended
- [ ] `state.project.jurisdiction` set

---

# Review

- [ ] Completeness pass run
- [ ] Evidence pass run
- [ ] Adversarial pass run — and produced something
- [ ] Coherence pass run
- [ ] Verdict recorded

If the adversarial pass produced nothing, it was not performed honestly. Re-run it.

---

# Gate

- [ ] Criterion 1 — unambiguous sentence
- [ ] Criterion 2 — jurisdiction named, not inferred
- [ ] Criterion 3 — buyer and user distinguished
- [ ] Criterion 4 — five qualifying questions
- [ ] Criterion 5 — assumptions tagged
- [ ] Universal gates U1–U6
- [ ] Verdict recorded in `state.run`

---

# Human Checkpoint

- [ ] Brief presented
- [ ] Blocking questions presented first, and few
- [ ] Deferrable questions listed separately
- [ ] Assumptions shown
- [ ] Next module and its output described
- [ ] **Stopped and waited**

---

# Exit

- [ ] Operator answers incorporated
- [ ] Answered questions resolved, answers preserved
- [ ] Contradicted assumptions superseded, not deleted
- [ ] Gate re-run if the brief materially changed
- [ ] `01-idea` appended to `state.run.completed_modules`
- [ ] Handoff contract satisfied — `02-market` has what it needs

---

# Red Flags

Stop and re-run the module if any of these are true:

- [ ] The brief could be mistaken for the original idea
- [ ] Fewer than five assumptions were surfaced
- [ ] The jurisdiction was inferred
- [ ] Every claim is tagged `[verified]`
- [ ] No question would change the work if answered differently
- [ ] There is no "out of scope" section
- [ ] The module completed in seconds

---

> **Checklist Principle**
>
> The gate should confirm what the checklist already established.
>
> If the gate is where problems are first discovered, the work was not done.
