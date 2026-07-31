---
Title: Future Improvements
Module: 10-execution
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: State what the Execution module does not yet do well.
Audience:
  - Product Managers
  - Founders
  - Engineers
Prerequisites:
  - 10-execution/learn/19-Related-Modules.md
Outputs:
  - A candid list of the module's limitations
Related Modules:
  - 08-product
  - 13-operations
Tags:
  - Execution
  - Improvements
  - Learn
---

# Future Improvements

---

# Known Limitations

**The no-context standard is untestable inside the framework.** "Readable by an agent
with no prior context" is the right bar and only a human can check it, by handing the
document to someone. Nothing in the gate approximates it.

**No estimation at all.** The module sequences work and says nothing about how long it
takes. That is a deliberate scope choice and it leaves a real gap: a plan can be
perfectly sequenced and wildly infeasible, and nothing in the framework notices.

**Cold start is guidance, not a required output.** The most-used screen in a new product
has no slot.

**Milestone Zero's placement is unverified.** Module 04 declares, module 07 binds, this
module is supposed to sequence it first, and nothing checks that it did.

**Accessibility has no required artifact.** The knowledge layer covers it well and the
plan has no place to record a keyboard path, a focus order, or a decision about
contrast — so it lands in a later audit, which finds violations rather than preventing
them.

**The QA strategy is not traced to acceptance criteria.** It should be derived from module
08's criteria and module 09's failure modes. Nothing requires the derivation, so a test
plan can cover a different set entirely and look complete.

**No feedback path from operations.** Module 13 routinely discovers flow problems in the
support queue. Returning them here is a convention with no mechanism, so the roadmap item
depends on somebody remembering.

---

# Candidate Improvements

| Candidate | What it would fix | Cost |
| --- | --- | --- |
| A required cold-start section per flow | The most-used screen gets designed | Small |
| A Milestone Zero placement check | The four-link chain gets an enforcement point | Small |
| QA strategy traced to acceptance criteria and failure modes | Test coverage stops drifting from what was decided | Small |
| An accessibility record per flow — keyboard path, focus order | Structure stops being deferred to audit | Moderate |
| A stranger-test attestation | The handoff standard gets something checkable, however weak | Small, and gameable |
| A feedback path from `13-operations` | Support-derived product changes stop depending on memory | Moderate |
| Estimation support | Infeasible plans become visible | Large, and possibly out of scope — estimation depends on a team the framework cannot see |

---

# What Should Not Change

**The demo test stays the milestone standard.** It is the only defense against the
two-month 90%, and every alternative — story points, percentage complete, phase gates —
can be satisfied without anything existing.

**The handoff stays written for no prior context.** Lowering it to "readable by the team"
would make it untestable and would remove the property that lets an agent build from it.

**The knowledge layer stays about UX.** Every review suggests adding project management
material here. Sequencing is the part people already know how to do; the empty state is
the part that decides whether anything gets used.

**Flows stay separate from the specification.** Merging them into module 08 would put
interface structure into a document that is supposed to constrain behavior, and both
would age badly.

---

> **Improvements Principle**
>
> The module's central standard — a stranger can start — cannot be automated, and the
> module is honest about that.
>
> The fixable gaps are smaller and worth doing anyway: a cold-start slot, a Milestone
> Zero check, and a traced QA strategy would each take an afternoon.
