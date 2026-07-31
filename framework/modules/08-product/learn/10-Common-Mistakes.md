---
Title: Common Mistakes
Module: 08-product
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Name the recurring failures in specification and what each costs.
Audience:
  - Product Managers
  - Founders
  - Researchers
Prerequisites:
  - 08-product/learn/01-Why-It-Matters.md
Outputs:
  - Recognition of specification failure patterns
Related Modules:
  - 07-strategy
  - 10-execution
Tags:
  - Product
  - Mistakes
  - Learn
---

# Common Mistakes

---

# Overview

Specification failures are quiet. The document reads well, everyone approves it, and the
cost appears weeks later as a series of small decisions made by whoever was building at
the time.

---

# 1. The Orphan Requirement

**What it looks like.** A requirement with a long, persuasive rationale and no trace to
any ranked problem.

**Why it is tempting.** It is usually a good idea. Somebody experienced knows the product
needs it, and they are often right.

**What it costs.** It consumes MVP effort that the evidence did not justify. Individually
each orphan is defensible; collectively they are the mechanism by which an MVP becomes a
product.

**Instead.** Check the trace. If it does not exist, the requirement can still be
included — as an explicitly justified exception, with the reason stated. What must not
happen is that it enters looking like every other requirement.

> The orphan always has the best paragraph in the document, because it is the only one
> that has to argue.

---

# 2. Aspirational Acceptance Criteria

**What it looks like.** "The onboarding flow should be smooth and intuitive."

**Why it is tempting.** It captures the intent, and the observable version feels
reductive.

**What it costs.** It cannot fail, so it will be marked met. Everyone will have a
different view of whether it actually was, and that disagreement surfaces at the worst
possible time — during release.

**Instead.** Write the observation. If you cannot state what "not met" looks like, you
have written a goal rather than a criterion, and goals belong in module 12.

---

# 3. The Happy Path as the Specification

**What it looks like.** A complete, clear description of what happens when everything
works.

**Why it is tempting.** It is the part everyone can visualize and agree on, and it feels
like the product.

**What it costs.** The other four fifths get decided during build, inconsistently, by
people without the context to decide well.

**Instead.** For each requirement, write the empty, the boundary, the failure, the
concurrent and the hostile case. Most will be one line. The exercise takes an hour and
prevents weeks.

---

# 4. Irreversibility Left Unstated

**What it looks like.** An action that cannot be undone, specified exactly like actions
that can.

**Why it is tempting.** The author knows it is irreversible, so the document does not
need to say it.

**What it costs.** The builder implements it without a confirmation, the interface never
communicates it, and a user discovers the rule by breaking it. In the worked example this
appears as approval of a clinical note — irreversible, and invisible in the interface
until the operations module found it in the support queue.

**Instead.** State reversibility on every state-changing requirement. It is one word per
requirement and it changes the design.

---

# 5. Silent Drops

**What it looks like.** A capability discussed for weeks that is simply absent from the
final document.

**Why it is tempting.** Writing "we decided not to do this" invites the argument again.

**What it costs.** Three months later nobody can distinguish a decision from an
oversight. The item comes back, is re-debated with less information, and often gets
built.

**Instead.** Record it, with a destination — roadmap, or rejected. The gate requires
this and it is the criterion most often satisfied in spirit and skipped in practice.

---

# 6. Scope Laundering, Completed

**What it looks like.** An MVP that, once specified, turns out to contain the whole
product under phase labels.

**Why it is tempting.** It arrives from module 07 that way, and re-opening the cut is a
conversation nobody wants.

**What it costs.** Module 10 sequences it, the first honest estimate lands in build, and
the cut happens anyway — later, under pressure, with worse information.

**Instead.** Report it back. Discovering during specification that the cut was not real
is a legitimate and useful finding. Writing a larger MVP to accommodate it is the
laundering completing itself.

---

# 7. Design Decisions Disguised as Requirements

**What it looks like.** "The list shall be displayed as a sortable table with filters in
the left sidebar."

**Why it is tempting.** The author can picture it, and the picture feels like clarity.

**What it costs.** It constrains module 10's flow design and module 09's implementation
for no stated reason, and it ages badly — the requirement survives long after the
interface it assumed is gone.

**Instead.** Specify what the user must be able to accomplish and what must be true of
the result. Leave the arrangement to the module that owns it, unless a specific
arrangement is genuinely required — in which case say why.

---

# 8. Requirements That Cannot Be Tested Because They Have No Subject

**What it looks like.** "The system should handle errors gracefully."

**Why it is tempting.** It sounds responsible and covers everything.

**What it costs.** It covers nothing. Which errors, detected how, and what does the user
see? Three questions, none answered, all of which someone will answer during build.

**Instead.** Name the error, the detection, and the user-visible result. This is the same
discipline module 14 applies to failure modes, for the same reason.

---

# The Pattern

| Mistake | Underlying move |
| --- | --- |
| Orphan requirement | A good idea entering without evidence |
| Aspirational criteria | Writing intent instead of a test |
| Happy path only | Specifying the part everyone can picture |
| Irreversibility unstated | The author holding a decision privately |
| Silent drops | Avoiding a repeat argument |
| Scope laundering completed | Accommodating an unreal cut |
| Design as requirement | Over-specifying what you can visualize |
| Subjectless requirements | Covering everything by naming nothing |

Five of the eight are the same underlying thing: **the author knows something the
document does not say.** That is the entire failure mode of specification work, and the
two-builder test is the only reliable way to find it.

---

> **Mistakes Principle**
>
> Every one of these produces a document that reads well.
>
> The cost appears later, in decisions made by people who did not know what you knew and
> had no way to find out.
