---
Title: Future Improvements
Module: 14-ai-systems
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: State what the AI Systems module does not yet do well.
Audience:
  - Product Managers
  - Founders
  - Engineers
Prerequisites:
  - 14-ai-systems/learn/19-Related-Modules.md
Outputs:
  - A candid list of the module's limitations
Related Modules:
  - 08-product
  - 09-technology
Tags:
  - AI
  - Improvements
  - Learn
---

# Future Improvements

---

# Known Limitations

**The advocate check is guidance.** It is the module's best instrument and the gate only
requires that an alternative was considered. A straw man satisfies it exactly as well as
an argued case.

**Detectability has no field.** The principle that governs autonomy is carried in prose,
so an autonomy ceiling set from accuracy and one set from detectability are
indistinguishable in the output.

**Data availability, quality and rights are one criterion.** They fail independently and
the third is legal. Collapsing them lets a capability pass on availability alone.

**Nothing forces a version and date on model claims.** The module requires it and no gate
checks it, so a stale price can feed a cost ratio that feeds two arithmetic checks.

**Deferred and rejected are not structurally separated.** This module suffers most from
that gap, because capability lists get reviewed more often than any other part of a plan.

**The golden set has no stratification requirement.** A representative sample passes, and
a representative sample measures the average while hiding the consequential failures.

**No treatment of drift.** A capability that meets its bar at launch may not in a year —
because the population changes, the inputs change, or the model version is replaced.
Evaluation cadence is guidance rather than an obligation with an owner in module 13.

**Nothing checks that the cost ratio was forwarded.** Two downstream checks depend on it
and neither can tell whether it arrived.

---

# Candidate Improvements

| Candidate | What it would fix | Cost |
| --- | --- | --- |
| A required `alternative_advocate` sentence per capability | The straw man becomes visible | Small, and the best change available here |
| A `detectable` field on every failure mode | Autonomy reasoning becomes inspectable | Small |
| Three separate data criteria — availability, quality, rights | Legal questions stop passing as technical ones | Small |
| Version and date validation on model claims | The cost ratio stops decaying silently | Small |
| Separate `rejected` and `deferred` lists | Rejections stop being re-proposed | Small |
| A stratification requirement on the golden set | Hard cases stop being optional | Small |
| An evaluation cadence handed to module 13 as an obligation | Drift acquires an owner | Moderate |

Every one of these is small, which is unusual. This module's limitations are almost all
missing fields rather than missing disciplines — the disciplines are well described and
carried entirely by prose.

---

# What Should Not Change

**Every capability faces an alternative.** It is the module's reason for existing. A
version of this module without it is a feature list.

**Detectability governs autonomy.** Every review eventually proposes an accuracy-threshold
rule because accuracy is the number that exists. The substitution is precisely the error
this module was written to prevent.

**Data availability stays a blocker.** Softening it to a risk puts unbuildable
capabilities on roadmaps.

**The bar stays set before building.** Evaluated afterwards, it becomes whatever was
achieved — reliably, every time, without anyone intending it.

**The module stays last.** Its position is what allows a proposal to be checked against
ranked problems, a requirement list, a data model and a cost ceiling rather than against
enthusiasm.

**Proposing generously stays correct.** The discipline belongs in the elimination, not in
the proposal. A module that discouraged proposals would produce fewer good ideas and the
same number of bad adoptions.

---

> **Improvements Principle**
>
> This module's reasoning is sound and its structure is thin — nearly every discipline it
> teaches is carried by prose that a gate does not read.
>
> Seven small fields would make the whole module enforceable, and that is a better
> position than most modules in this framework are in.
