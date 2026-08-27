---
Title: Checklist
Module: 04-problem
Section: core
Category: Verification
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Operational checklist for entering, running and exiting the Problem module.
Audience:
  - AI Agents
  - Researchers
Prerequisites:
  - 04-problem/core/07-Workflow.md
  - 04-problem/core/11-Quality-Gate.md
Outputs:
  - Verified module completion
Related Modules:
  - 07-strategy
Tags:
  - Problem
  - Checklist
  - Verification
---

# Checklist

---

# Entry

- [ ] `03-user` in `state.run.completed_modules`
- [ ] `current_workflow` read — and contains actual friction points
- [ ] `jobs_to_be_done` read
- [ ] `personas` read
- [ ] `NEEDS USER` questions from `03-user` collected
- [ ] Research mode declared by `03-user` noted — it caps what can be verified here
- [ ] `engine/evidence-policy.md` read
- [ ] `06-Framework.md` and `09-Research-Methodology.md` read

---

# Stage 1 — Harvest

- [ ] Every workflow friction point mined
- [ ] Every poorly-served job mined
- [ ] The step they most want removed captured
- [ ] Switching-cost pain mined
- [ ] Review and forum complaints mined
- [ ] Workarounds identified — each is a gap with evidence attached
- [ ] **Substitute workflows enumerated BY NAME** — the manual routine, the general-purpose
      tool bent to the job, the thing they built themselves, the adjacent product, tolerating
      it. Section 2a of the template
- [ ] **Each substitute measured where a measure exists** — downloads, installs, tutorial
      views, forum answers recommending it
- [ ] **The silent majority accounted for.** Every other source in this stage is a complaint,
      and complaints only come from people who adopted something and were disappointed
- [ ] Out-of-hours cost captured
- [ ] Problems recorded in the person's own framing
- [ ] No filtering applied during collection

---

# Stage 2 — Classify

- [ ] Every statement classified: problem, symptom, or preference
- [ ] Cost check applied — nothing without a cost is a problem
- [ ] Every symptom traced to the problem beneath it
- [ ] Excluded preferences kept on the page with reasons

---

# Stage 3 — Score

- [ ] Frequency scored for every problem
- [ ] Severity scored for every problem
- [ ] **Workaround scored for every problem**
- [ ] Scales stated
- [ ] Arithmetic visible
- [ ] Cost per occurrence recorded where establishable
- [ ] Cost derivations shown, not asserted

---

# Stage 4 — Sort

- [ ] Validated and assumed lists created
- [ ] They are **visually separate** in the document
- [ ] Only `[verified]` evidence at ladder rank 1–3 qualifies as validated
- [ ] Assumed section carries an explicit warning
- [ ] If the validated list is empty, that is stated plainly
- [ ] Counts recorded for the verdict

---

# Stage 5 — Sharpen

- [ ] Exactly one sharpest problem chosen
- [ ] Choice defended against the scoring table
- [ ] Comparable scorers addressed
- [ ] If the top scorer was passed over, the reason is stated
- [ ] **Evidence standing stated explicitly — verified or assumed**
- [ ] Why nobody has solved it recorded
- [ ] Root cause check performed
- [ ] Root-vs-symptom decision stated

---

# Stage 6 — Plan

- [ ] Every assumed problem has a test
- [ ] Tests ordered by cheapest-test-of-most-load-bearing-belief
- [ ] Each test names method, sample, effort
- [ ] **Each test names what result would invalidate the assumption**
- [ ] `NEEDS USER` questions carried forward
- [ ] "Test this first" identified
- [ ] Stop-and-rethink trigger defined

---

# Assembly

- [ ] `13-Template.md` filled into `projects/<slug>/research/04-problem.md`
- [ ] **Verdict stated first**
- [ ] Verdict is no softer than the evidence supports
- [ ] Every `«placeholder»` replaced
- [ ] Every guidance comment removed
- [ ] Every claim carries exactly one tag
- [ ] Every `[verified]` resolves to a row in Sources
- [ ] Contradicting Evidence section non-empty
- [ ] Prior failed attempts recorded, if any were found

---

# State

- [ ] `outputs.problem_inventory` written
- [ ] `outputs.ranked_problems` written, with the validated/assumed split
- [ ] `outputs.validation_plan` written
- [ ] Sharpest problem and its evidence standing recorded prominently
- [ ] `state.evidence_log` appended
- [ ] `state.assumptions` appended
- [ ] `state.open_questions` appended
- [ ] If the sharpest problem is assumed, flagged for `07-strategy` and `09-Roadmap`

---

# Review

- [ ] Completeness pass run
- [ ] Evidence pass run
- [ ] Adversarial pass run — and produced something
- [ ] Coherence pass run — problems attributable to the `03-user` persona
- [ ] Verdict recorded

---

# Gate

- [ ] Criterion 1 — all three dimensions scored
- [ ] Criterion 2 — three verified problems, **or shortfall declared honestly**
- [ ] Criterion 3 — sharpest problem identified and defended
- [ ] Criterion 4 — unvalidated problems listed separately
- [ ] Criterion 5 — substitute workflows enumerated by name, including what people who use nothing do
- [ ] Criterion 6 — the corpus states its selection rule, and the independence test is answered in writing
- [ ] Counts are normalized, or cross-source comparison is explicitly refused
- [ ] All six biases in `knowledge/Corpus-Selection.md` addressed, each with what was done about it
- [ ] Universal gates U1–U7
- [ ] Verdict recorded in `state.run`

---

# Exit

- [ ] `04-problem` appended to `state.run.completed_modules`
- [ ] Handoff satisfied for `05-competition`, `07-strategy`, `08-product`
- [ ] Every problem module 08 might build against appears in `ranked_problems`

---

# Red Flags

Re-run the module if any of these are true:

- [ ] Only three or four problems harvested from a multi-step workflow
- [ ] A preference appears in the scoring table
- [ ] A symptom is being treated as the problem
- [ ] The workaround dimension is missing
- [ ] **The workaround column is scored but section 2a names no substitute that justifies it**
- [ ] **A substitute larger than the entire product category was found and recorded as a
      footnote rather than put in front of the operator**
- [ ] Validated and assumed problems share a section
- [ ] The validated list was padded with inference
- [ ] No single sharpest problem was chosen
- [ ] The validation plan contains a test that cannot fail
- [ ] No stop-and-rethink trigger is defined
- [ ] The verdict is more optimistic than the evidence counts support

---

> **Checklist Principle**
>
> The temptation in this module is to make the news better than it is.
>
> Every item here exists to make that temptation visible.
