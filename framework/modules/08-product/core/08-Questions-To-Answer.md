---
Title: Questions To Answer
Module: 08-product
Section: core
Category: Inquiry
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: The complete question set this module must answer before its gate can pass.
Audience:
  - AI Agents
  - Product Managers
Prerequisites:
  - 08-product/core/06-Framework.md
Outputs:
  - Answered question set
Related Modules:
  - 09-technology
Tags:
  - Product
  - Questions
  - Requirements
---

# Questions To Answer

---

# Overview

This module asks almost no research questions. It asks **precision** questions.

Every question below is answered from the material modules 03, 04 and 07 already produced,
or by a judgment made here and labeled as one. A question in this module that requires new
research is a sign that an earlier module left something open.

Questions marked **OPERATOR** or **NEEDS USER** cannot be answered by inference. They go to
`state.open_questions` and appear in the deliverables as open.

---

# 1. Inherited Boundary

| # | Question | If unanswered |
| --- | --- | --- |
| 1.1 | What is above module 07's MVP line? | The MUST list has no basis |
| 1.2 | What is below it? | Scope laundering becomes undetectable |
| 1.3 | Was the cut approved at the checkpoint? | Specifying against an unapproved boundary |
| 1.4 | Who is the primary persona, and what is the core job? | The spec has no subject |
| 1.5 | Is the sharpest problem verified or assumed? | Requirement confidence is overstated |
| 1.6 | What did module 07 declare as non-goals? | Exclusions get re-litigated in the PRD |
| 1.7 | What does the MVP deliberately not prove? | Success criteria overreach |

---

# 2. Tracing

| # | Question | If unanswered |
| --- | --- | --- |
| 2.1 | What are the numbered steps of the core job? | The spine does not exist |
| 2.2 | For each step, which problem does it belong to? | Requirements cannot be traced |
| 2.3 | Which steps does this release serve? | Coverage is unknown |
| 2.4 | Which steps are left to the existing workaround? | The user hits a hole and nobody predicted it |
| 2.5 | **Does any capability above the line lack a parent problem?** | Orphans enter the spec |
| 2.6 | **Does any problem above the line lack a capability?** | The cut or the spine is broken |
| 2.7 | Can the persona complete the job with the served steps plus the stated fallbacks? | Module 07's test fails silently here |

> 2.5 and 2.6 are the two directions of traceability. Both are gate criteria. An orphan is
> deleted, not justified — an orphan can always be justified, and that is the problem.

---

# 3. Requirements

| # | Question | If unanswered |
| --- | --- | --- |
| 3.1 | What must the product do for each served step? | No requirements |
| 3.2 | For each requirement, which problem is its parent? | Traceability incomplete |
| 3.3 | Is each requirement MUST, SHOULD or COULD — and why? | Priority is decoration |
| 3.4 | **Does any MUST map to a capability below the line?** | The approved cut has moved |
| 3.5 | Is the MUST list meaningfully shorter than the requirement list? | Nothing was prioritized |
| 3.6 | Which requirements are derived, and which are judgments made here? | Design decisions unregistered |
| 3.7 | What did a requirement's parent problem's evidence tag say? | Assumed problems get written as certainties |
| 3.8 | Which capabilities surfaced only while specifying? | Scope grows with no record |
| 3.9 | For each of those, is the core job impossible without it? | Regress-versus-defer decision unmade |

---

# 4. Behavior

| # | Question | If unanswered |
| --- | --- | --- |
| 4.1 | What triggers this requirement? | The entry point is guessed |
| 4.2 | What does the user provide, and what is optional? | Input contract undefined |
| 4.3 | What does the system do, including what the user cannot see? | Side effects invented downstream |
| 4.4 | What is true afterwards that was not before? | State transition undefined |
| 4.5 | How does the user know it worked? | Feedback omitted; a real defect |
| 4.6 | **Where would two engineers read this differently?** | The requirement is underspecified |
| 4.7 | Does this text name a technology, database or screen layout? | A decision was taken from 09-technology or design |
| 4.8 | What is deliberately not part of this requirement? | Assumed inclusions cause rework |

---

# 5. Failure and Edge States

Asked for every MUST requirement.

| # | Question | If unanswered |
| --- | --- | --- |
| 5.1 | First use, no data — what does the user see and do? | Empty state improvised in build |
| 5.2 | Invalid or incomplete input — what are they told? | Error text invented, often badly |
| 5.3 | Is their work preserved when input is rejected? | Silent data loss |
| 5.4 | The operation cannot complete — what happens? | Failure behavior improvised |
| 5.5 | **Can work be lost, and when?** | The most expensive unwritten answer in most products |
| 5.6 | Can they retry, and is retrying safe? | Duplicates |
| 5.7 | The user lacks permission — what do they see? | Authorization behavior undefined |
| 5.8 | Does the refusal reveal something it should not? | Information leak by error message |
| 5.9 | Too many, too large, two at once, offline, interrupted — what then? | Limits discovered by users |
| 5.10 | Which category did I mark "not applicable" without thinking? | A blank posing as an answer |

---

# 6. Ordering

| # | Question | If unanswered |
| --- | --- | --- |
| 6.1 | What scoring method is used, and is it applied to every row? | Prioritization is assertion |
| 6.2 | Which requirements score highly but sit below the line? | The disagreement is hidden |
| 6.3 | Which score low but are above it, and why? | Usually a dependency — say so |
| 6.4 | What must exist before what? | Build order unknown |
| 6.5 | What is the critical path? | Module 10 cannot sequence |
| 6.6 | What is the **first shippable slice** a real user could use? | The team builds for months with no contact |
| 6.7 | Which requirements can ship independently? | Parallel work invisible |

---

# 7. Acceptance

| # | Question | If unanswered |
| --- | --- | --- |
| 7.1 | For each requirement, what observation proves it works? | Nothing is testable |
| 7.2 | For each criterion, what observation would **fail** it? | It is a hope, not a criterion |
| 7.3 | Does any criterion use fast, easy, intuitive, seamless, robust? | Aspiration in criterion form |
| 7.4 | Is there a criterion for the failure states, not only the happy path? | Half the behavior is unverified |
| 7.5 | Could someone with no context judge pass or fail? | Acceptance requires the author present |

---

# 8. Constraints and Fit

| # | Question | If unanswered |
| --- | --- | --- |
| 8.1 | What regulatory constraints from module 02 bind this product? | Compliance discovered in build |
| 8.2 | Does this requirement set fit the cost-to-serve ceiling from module 06? | The business model breaks |
| 8.3 | Does it fit the user's real environment from module 03? | Built for conditions that do not exist |
| 8.4 | Does it fit the price the business model assumed? | Value and price diverge |
| 8.5 | What does the product depend on that we do not control? | External dependency unregistered |

---

# 9. Exclusions

| # | Question | If unanswered |
| --- | --- | --- |
| 9.1 | Is every capability considered accounted for in the ledger? | Things dropped silently |
| 9.2 | For each, why was it excluded? | Reason lost; re-proposed monthly |
| 9.3 | For each, what would make us reconsider? | Exclusion becomes permanent by accident |
| 9.4 | Is every Fast-follow and Deferred row carried to the roadmap? | The gate criterion fails |
| 9.5 | What would a reader reasonably expect that is not here? | Surprise at handoff |

---

# 10. Open

| # | Question | Category |
| --- | --- | --- |
| 10.1 | Which requirements depend on a fact only a real user can supply? | **NEEDS USER** |
| 10.2 | Is any workflow step's real-world sequence unverified? | **NEEDS USER** |
| 10.3 | Are there constraints in the operating environment we have not been told? | **OPERATOR** |
| 10.4 | Is there a requirement the operator considers non-negotiable that is not here? | **OPERATOR** |
| 10.5 | Which design decisions made here would the operator want to make instead? | **OPERATOR** |

> This module has no checkpoint of its own. That makes 10.3–10.5 easy to skip. They still go
> to `state.open_questions`, and they still appear in the PRD as open.

---

# Question Coverage

| Section | Feeds |
| --- | --- |
| 1 | §2 Inherited Scope |
| 2 | §5 Core Job, §13 Traceability |
| 3 | §7 Requirements |
| 4 | §7 Behavior |
| 5 | §8 Failure and Edge States |
| 6 | §11 Prioritization |
| 7 | §7 Acceptance criteria |
| 8 | §9 Constraints |
| 9 | §10 Deferral Ledger |
| 10 | §12 Open Questions |

---

# Self Assessment

- Did I answer 2.5 and 2.6 in both directions?
- Did I answer 3.4 honestly, or by looking at the answer I wanted?
- Can I name the divergence point for every requirement, per 4.6?
- Did I work all five edge categories, or three?
- Can every acceptance criterion fail?
- Is anything in the ledger missing a revisit trigger?
- Did I record the operator questions, given that nobody will ask me for them?

---

> **Question Principle**
>
> Every question here is one a builder would otherwise have to ask you.
>
> They cannot. That is the whole reason the list is this long.
