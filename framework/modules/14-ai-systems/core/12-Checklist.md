---
Title: Checklist
Module: 14-ai-systems
Section: core
Category: Verification
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Operational checklist for entering, running and exiting the AI Systems module.
Audience:
  - AI Agents
  - Engineers
Prerequisites:
  - 14-ai-systems/core/07-Workflow.md
  - 14-ai-systems/core/11-Quality-Gate.md
Outputs:
  - Verified module completion
Related Modules:
  - 12-metrics
  - 13-operations
Tags:
  - AI Systems
  - Checklist
---

# Checklist

---

# Step 0 — Applicability

- [ ] Asked whether any requirement needs judgment, generation, extraction or prediction that cannot
      be a rule
- [ ] If none does, **recorded plainly in §1 and §2, with the comparison that established it**
- [ ] If none does, exited the module — an empty result is a legitimate one

---

# Entry

- [ ] `08-product` and `09-technology` in `state.run.completed_modules`
- [ ] Requirements read from `08-product` §7
- [ ] Edge cases and failure-state expectations read from `08-product` §8
- [ ] Jobs read from `03-user`, with the persona's real error tolerance
- [ ] **Data classification read from `09-technology` §3** — PII and regulated fields
- [ ] Architecture read from `09-technology` §8
- [ ] Cost model read from `09-technology` §12
- [ ] Regulatory landscape and disclosure obligations read from `02-market`
- [ ] **Revenue per user per month read from `06-business`**
- [ ] Latency expectations read from `10-execution` §4, if complete
- [ ] `06-Framework.md` and `09-Research-Methodology.md` read

---

# Move 1 — Propose

- [ ] Candidates listed generously
- [ ] Each names the job it serves
- [ ] Each names the requirement it serves
- [ ] Candidates serving no requirement removed, or taken to `08-product`

---

# Move 2 — Compare

Per candidate:

- [ ] **Non-AI alternative written** — a rule, lookup, sorted list, better form, default, or asking a
      different party
- [ ] **Advocate check run** — a competent person could argue for it in one sentence
- [ ] Straw men rewritten, then compared again
- [ ] Verdict recorded: build or drop
- [ ] Where the alternative wins on quality but loses on effort, stated as such
- [ ] **Dropped capabilities recorded, with what was adopted instead**
- [ ] Proposed and kept counts recorded

---

# Move 3 — Ground

Per data need:

- [ ] Source stated
- [ ] **Availability confirmed now, with evidence**
- [ ] Volume stated
- [ ] Quality assessed
- [ ] Blocker stated

And:

- [ ] **Unconfirmed needs listed as blockers, not risks**
- [ ] **Cold-start behavior stated**

**Data rights**

- [ ] Right to use the data this way, with the regime cited
- [ ] Consent requirement answered, and whether it is held
- [ ] Whether data leaves the system, to whom, in which jurisdiction
- [ ] Provider training on our data — disabled, and contracted
- [ ] **Regulated and PII list from `09-technology` §3 checked against every model input**
- [ ] "None — verified" recorded, or the overlap removed

---

# Move 4 — Bound

Per capability:

- [ ] User-visible behavior stated
- [ ] **What one wrong output costs, in the user's terms**
- [ ] **Who bears that cost**
- [ ] **Whether the user can detect it is wrong**
- [ ] Recoverability stated
- [ ] Autonomy level chosen, and justified against the above
- [ ] Rule applied — no autonomy above "suggests" where the user bears an undetectable error, without
      a visibility mechanism
- [ ] Review: always, sampled or never
- [ ] Who reviews, and what qualifies them
- [ ] Whether the user can override
- [ ] Whether the override is recorded
- [ ] Audit trail for generated content
- [ ] Disclosure to the user
- [ ] Labeling of generated content
- [ ] Whether the user can see why
- [ ] Regulatory disclosure obligation checked against `02-market`

---

# Move 5 — Evaluate

Per capability:

- [ ] Metric stated
- [ ] Method stated
- [ ] **Passing bar stated — before any build**
- [ ] Sample size stated
- [ ] Cadence stated
- [ ] Golden set construction described
- [ ] **Golden set quarantined from tuning**
- [ ] **Judge named, with their qualification**
- [ ] **Ship gate stated**
- [ ] What happens if the bar is missed — it does not ship
- [ ] Regression check for model or prompt changes
- [ ] **Statistical criteria written**
- [ ] **Per-instance guarantees written**
- [ ] Per-instance guarantees handed to `08-product`

---

# Move 6 — Fail

- [ ] Failure modes **specific to this product**
- [ ] Likelihood per mode
- [ ] What each costs the user
- [ ] **Detection per mode**
- [ ] **Guardrail per mode — not a better prompt**
- [ ] **Worst realistic outcome stated plainly**
- [ ] Whether we would know it happened
- [ ] **Silent, plausible failures identified**
- [ ] **Non-AI fallback specified as a requirement**, and handed to `08-product`
- [ ] Provider outage behavior stated
- [ ] Model version pinned and cited with a date
- [ ] Deprecation exposure stated
- [ ] Fallback model stated
- [ ] Vendor lock-in assessed
- [ ] Failure modes needing alerts or runbooks handed to `13-operations`

---

# Cost

- [ ] Cost per operation, cited with a date
- [ ] Operations per user per month, with a basis
- [ ] AI cost per user per month derived
- [ ] **Share of revenue per user computed**
- [ ] Acceptability stated
- [ ] If the share is large, **a lever chosen** — approach, volume, price, or drop
- [ ] Figure handed to `09-technology` §12 and `13-operations` §11
- [ ] Latency budget checked against `10-execution` §4

---

# Assembly

- [ ] `13-Template.md` filled into `projects/<slug>/research/14-ai-systems.md`
- [ ] §1 written last
- [ ] §12 contradicting evidence non-empty
- [ ] §13 confidence stated separately for capability choices and quality expectations
- [ ] Every quality expectation tagged as an assumption
- [ ] No benchmark or demo cited as evidence of this product's quality
- [ ] Every `«placeholder»` replaced
- [ ] Every guidance comment removed

---

# State

- [ ] `outputs.ai_opportunities` written, including dropped
- [ ] `outputs.model_strategy` written
- [ ] `outputs.data_requirements` written
- [ ] `outputs.evaluation_plan` written
- [ ] `outputs.failure_modes` written
- [ ] `state.decisions` appended with every verdict and its rejected alternative
- [ ] `state.assumptions` appended with every quality expectation, operation count and cost estimate
- [ ] `state.open_questions` appended with unconfirmed data needs and unresolved rights questions, as
      blockers

---

# Review

- [ ] Completeness pass run
- [ ] Evidence pass run
- [ ] Adversarial pass run — and produced something
- [ ] Coherence pass run — latency fits the flow, cost fits the ceiling, autonomy fits the persona
- [ ] Verdict recorded

---

# Gate

- [ ] Criterion 1 — justified against a genuine non-AI alternative
- [ ] Criterion 2 — data availability confirmed
- [ ] Criterion 3 — evaluation defined before commitment
- [ ] Criterion 4 — failure modes and fallback specified
- [ ] Criterion 5 — each alternative carries a one-sentence case written as its advocate would write it
- [ ] Criterion 6 — every failure mode states whether the user can detect it, including when the answer is no
- [ ] Data rights check — no regulated model input
- [ ] Detectability check
- [ ] Cost ratio check
- [ ] Version pin check
- [ ] Fallback-is-scope check
- [ ] Universal gates U1–U7
- [ ] `proposed` and `kept` counts recorded
- [ ] Verdict recorded in `state.run`

---

# Exit

- [ ] `14-ai-systems` appended to `state.run.completed_modules`
- [ ] Per-instance guarantees and non-AI fallbacks handed to `08-product` as requirements
- [ ] Cost line handed to `09-technology` and `13-operations`
- [ ] Quality metrics handed to `12-metrics`
- [ ] Failure modes handed to `13-operations`
- [ ] Noted whether the AI strategy deliverable is in scope — it is optional

---

# Red Flags

Re-run the module if any of these are true:

- [ ] Every proposed capability was kept
- [ ] Any non-AI alternative could not be argued for
- [ ] A capability serves no requirement
- [ ] Nothing was dropped and no reason is given
- [ ] A data need is projected rather than confirmed
- [ ] Cold start is unaddressed
- [ ] A data-rights question is unresolved
- [ ] A regulated or PII field is a model input
- [ ] Autonomy exceeds "suggests" where the error is undetectable and the user pays
- [ ] The build team is judging domain quality
- [ ] The passing bar was set after seeing outputs
- [ ] The golden set is used for tuning
- [ ] There is no ship gate
- [ ] Only statistical criteria exist, with no per-instance guarantees
- [ ] A failure mode could apply to any product
- [ ] A failure has no detection
- [ ] A better prompt is offered as a guardrail
- [ ] The worst realistic outcome is unstated
- [ ] The non-AI fallback exists only in this document
- [ ] The model version is unpinned
- [ ] The cost ratio was never computed
- [ ] A large revenue share is noted with no lever chosen
- [ ] A benchmark or demo is cited as evidence of quality

---

> **Checklist Principle**
>
> One line decides whether this module was worth running:
> whether anything was dropped.
>
> A module that keeps everything it proposed asked the question
> without waiting for the answer.
