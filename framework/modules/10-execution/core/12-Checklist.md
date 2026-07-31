---
Title: Checklist
Module: 10-execution
Section: core
Category: Verification
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Operational checklist for entering, running and exiting the Execution module.
Audience:
  - AI Agents
  - Delivery Leads
Prerequisites:
  - 10-execution/core/07-Workflow.md
  - 10-execution/core/11-Quality-Gate.md
Outputs:
  - Verified module completion
Related Modules:
  - 12-metrics
Tags:
  - Execution
  - Checklist
---

# Checklist

---

# Entry

- [ ] `08-product` and `09-technology` both in `state.run.completed_modules` with passing gates
- [ ] MUST requirements, edge cases and acceptance criteria read
- [ ] **First shippable slice** read from `08-product` §11
- [ ] Critical path read from `08-product` §11
- [ ] **One-way doors** read from `09-technology` §13
- [ ] Non-negotiables read from `09-technology` §10
- [ ] Roadmap and Milestone Zero requirement read from `07-strategy`
- [ ] Validation plan read from `04-problem`, if M0 is required
- [ ] Numbered workflow and persona constraints read from `03-user`
- [ ] Open questions and blockers collected from modules 08 and 09
- [ ] **Operator asked for team facts** — size and composition
- [ ] **Operator asked about any fixed deadline**
- [ ] `06-Framework.md` and `09-Research-Methodology.md` read
- [ ] `08-UX-Flows.md`, `09-Roadmap.md` and `12-Build-Handoff.md` templates read

---

# Move 1 — Flow

- [ ] Three to five design principles written
- [ ] Each names the research finding it derives from
- [ ] Two or three critical paths chosen — not every path
- [ ] Per path: trigger, persona, frequency, what success means
- [ ] Per path: step table — user sees, user does, system does, can fail
- [ ] Per path: step count stated
- [ ] Per path: requirements covered listed
- [ ] **Per path: failure and recovery table**
- [ ] **Per failure: whether work is preserved**
- [ ] No step invented — every step traces to `03-user` or is marked as an assumption

**Time to first value**

- [ ] "First value" defined as a specific moment
- [ ] Step count stated
- [ ] Target in minutes stated
- [ ] Longest unavoidable step named, with why it cannot be removed
- [ ] Migration requirement stated, and its position in the flow

**Screens and states**

- [ ] Every screen listed with its purpose
- [ ] Empty state per screen — what shows, what action is offered
- [ ] Loading state per screen
- [ ] Error state per screen — message and recovery
- [ ] Permission state per screen
- [ ] First-run state written
- [ ] Accessibility standard named, with the verification method
- [ ] Persona's context constraints written as concrete requirements

---

# Move 2 — Slice

- [ ] First milestone built around the first shippable slice
- [ ] **Demo test run per milestone, and the answer written down**
- [ ] Every answer describes a person doing something
- [ ] No milestone delivers only a layer
- [ ] Independence checked — each could stop and leave something usable
- [ ] What each milestone teaches, stated

---

# Move 3 — Sequence

- [ ] Sequencing principle stated in one sentence
- [ ] Why that principle and not the alternative
- [ ] Applied consistently across every milestone
- [ ] **Milestone Zero first, where the sharpest problem is assumed**
- [ ] M0 content taken from `04-problem`'s validation plan
- [ ] M0 states method, sample, proceed-if and stop-if
- [ ] **One-way doors placed, with the reasoning written**
- [ ] Independently shippable milestones identified
- [ ] Parallelizable work identified, with what it would require
- [ ] Longest chain stated
- [ ] Decision points written, each with the data needed
- [ ] **"Stop" is a possible outcome at each decision point**

---

# Move 4 — Define

Per milestone:

- [ ] What a user can do at the end that they could not before
- [ ] Requirements delivered
- [ ] Dependencies stated
- [ ] Relative size stated
- [ ] Acceptance criteria from `08-product` listed explicitly
- [ ] Non-functional bar stated — tests, environment, review
- [ ] **What is explicitly not done at this point**
- [ ] Ambiguity test run — two readers could not disagree about "done"
- [ ] Duration stated only if team facts exist, and then tagged

---

# Move 5 — Verify

- [ ] Each verification level assigned what it covers
- [ ] **Coverage table complete — every MUST requirement to a verification**
- [ ] Unverified requirements listed explicitly, with reasons
- [ ] Five edge categories per requirement covered, or gaps named
- [ ] Manual work identified with an owner
- [ ] **What is deliberately not tested, and why**
- [ ] No coverage level claimed

---

# Move 6 — Hand Over

- [ ] Blocked Work table written, or "None"
- [ ] Every blocker has a **named owner** — never "the team"
- [ ] Every blocker names the milestone that needs it
- [ ] Stated whether M1 can proceed with all blockers unresolved
- [ ] Non-negotiables carried from `09-technology` and `02-market`
- [ ] **No unresolved assumption anywhere in the build instructions**
- [ ] No "as discussed" / "per the research" / "as we agreed" anywhere
- [ ] **Cold-start check in §16 complete, with every answer yes**

---

# Estimates

- [ ] Assumed team stated, or explicitly recorded as not supplied
- [ ] Basis for every duration stated
- [ ] Operator estimates attributed to the operator
- [ ] Biggest estimation risk named
- [ ] If no team facts: relative sizes only, and §14 says so

---

# Assembly

- [ ] `13-Template.md` filled into `projects/<slug>/research/10-execution.md`
- [ ] §1 written last
- [ ] Deferred scope carried from `08-product` §10 with **triggers, not dates**
- [ ] Open questions recorded
- [ ] Every `«placeholder»` replaced
- [ ] Every guidance comment removed

---

# State

- [ ] `outputs.ux_flows` written
- [ ] `outputs.milestones` written
- [ ] `outputs.delivery_plan` written
- [ ] `outputs.qa_strategy` written
- [ ] `outputs.build_handoff` written
- [ ] `state.decisions` appended with every planning judgment and its rejected alternative
- [ ] `state.assumptions` appended with every unsupported duration
- [ ] `state.open_questions` appended with every blocker and its owner

---

# Review

- [ ] Completeness pass run
- [ ] Evidence pass run
- [ ] Adversarial pass run — and produced something
- [ ] Coherence pass run — first milestone matches the first shippable slice; one-way doors sequenced early
- [ ] Verdict recorded

---

# Gate

- [ ] Criterion 1 — critical paths mapped end to end, failures included
- [ ] Criterion 2 — vertical slices, sequenced by a stated principle
- [ ] Criterion 3 — cold-start ready
- [ ] Criterion 4 — definition of done per milestone, including what is not done
- [ ] Estimate boundary check
- [ ] Verification coverage check
- [ ] Invented-step check
- [ ] Deferred-scope check
- [ ] Universal gates U1–U7
- [ ] Milestone Zero status recorded
- [ ] Verdict recorded in `state.run`

---

# Exit

- [ ] `10-execution` appended to `state.run.completed_modules`
- [ ] Handoff satisfied for `11-growth`, `12-metrics`, `13-operations`
- [ ] Activation moment from §5 confirmed available to `11-growth`
- [ ] Noted that the build handoff deliverable is assembled **after** `12-metrics` names the events

---

# Red Flags

Re-run the module if any of these are true:

- [ ] A milestone is named after a layer
- [ ] Nothing is demonstrable until the final milestone
- [ ] No sequencing principle is stated
- [ ] The problem is assumed and there is no Milestone Zero
- [ ] A one-way door is committed in a late milestone
- [ ] A definition of done could be read two ways
- [ ] No milestone states what is not done
- [ ] A duration appears with no assumed team
- [ ] A MUST requirement has no verification and nothing says so
- [ ] The plan claims a coverage level
- [ ] A critical path has no failure rows
- [ ] A screen has only its populated state
- [ ] A flow contains a step nobody was observed performing
- [ ] An assumption sits in the build instructions
- [ ] A blocker is owned by "the team"
- [ ] Deferred scope carries dates
- [ ] Any row of the cold-start check is no

---

> **Checklist Principle**
>
> One item here decides whether the whole run was worth doing:
> whether a builder with no context could start today.
>
> Everything else is how that answer becomes yes.
