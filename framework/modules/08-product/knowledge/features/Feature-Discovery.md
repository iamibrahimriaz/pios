---
Title: Feature Discovery
Module: 08-product
Section: knowledge/features
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Build the traceability spine first, so parents are chosen before requirements are written.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 08-product/core/06-Framework.md
Outputs:
  - The traceability spine
Related Modules:
  - 03-user
  - 04-problem
Tags:
  - Product
  - Traceability
  - Method
---

# Feature Discovery

---

# What It Is

The spine: every step of the core job, laid against the problem it belongs to and the MVP boundary.

| Input | From | Role |
| --- | --- | --- |
| Ranked problems | `04-problem` | The parents. Nothing exists without one |
| The core job, step by step | `03-user` | The spine. Every step is served or explicitly left alone |
| The MVP line | `07-strategy` | The boundary. Above it is MUST territory |

**Why first.** A requirement written before the spine exists gets its parent assigned afterwards, which is how
unattached features acquire retrospective justification.

Two failures the spine catches, in both directions:

| Failure | What it means |
| --- | --- |
| **Orphan** — a capability with no parent problem | It came from somewhere other than the research. **Delete it** |
| **Unserved problem** — a ranked problem above the line with no capability | Either the cut was wrong or the spec is incomplete |

> An orphan is deleted, not justified. That rule matters because an orphan can almost always be justified — the
> justification is written after the fact and sounds entirely reasonable.

---

# When It Applies

In Move 1 (Trace), before a single requirement is written.

---

# How to Apply It Here

**Lay it out as a table and keep it in the PRD.** Job step, parent problem, served in this release, requirement
identifier. It is the artifact a reviewer checks the gate against.

**Check both directions explicitly.** Orphans are easy to spot; unserved problems are absences and require the reverse
read. The gate requires both.

**Mark steps deliberately left alone.** A job step the release does not serve is a decision, and recording it is what
distinguishes it from an omission.

**Treat an unserved above-line problem as a regress candidate.** It means either `07-strategy` cut wrongly or the spec
has a gap. Both are findings; neither is fixed by adding a MUST quietly.

**Discover from the job, not from the imagination.** Every capability should be traceable to a step in
`03-user`'s workflow. Anything arriving from elsewhere is an orphan by definition, however good it is.

---

# Where It Misleads

**Justification is available for everything, which is why the rule is deletion.** A competent writer can attach a
plausible parent to any capability. The defense is that the parent is chosen *before* the requirement exists.

**The spine gets built after the requirements, as documentation.** Then it records the retrospective parents rather than
catching them, and the whole mechanism inverts.

**Unserved problems are absorbed as "covered implicitly".** If no requirement names the problem, nothing serves it. The
trace is a list comparison, not an interpretation.

**Orphans arrive from customers and stakeholders with social weight attached.** A request from a named customer is still
an orphan if no ranked problem supports it. `04-problem`'s `Feedback.md` covers how to decode it into a problem first.

**The spine is treated as overhead.** It is the shortest section of the PRD and the only one that makes the gate
checkable mechanically.

---

# Related

| | |
| --- | --- |
| `08-product` `Requirements.md` | What gets written once the spine exists |
| `Feature-Prioritization.md` | Ordering what the spine admitted |
| `03-user`, `04-problem` | The job steps and the ranked problems |
| `07-strategy` | The binding line |

---

> **Concept Note**
>
> Choose the parent before writing the requirement, or the parent gets
> chosen to fit.
>
> Orphans are deleted rather than justified — because the
> justification always works.
