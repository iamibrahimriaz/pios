---
Title: CI-CD
Module: 09-technology
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Automate the checks that encode obligations, and keep the pipeline proportionate.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 09-technology/knowledge/Deployment.md
Outputs:
  - Pipeline definition within architecture
Related Modules:
  - 08-product
  - 13-operations
Tags:
  - Technology
  - CI
  - Concept
---

# CI-CD

---

# What It Is

The automated gate between a change and production.

Its value is not speed but **the checks it makes unavoidable**:

| Check | What it protects |
| --- | --- |
| Tests against `08-product`'s acceptance criteria | That the requirement still does what it was accepted for |
| Migration applies cleanly, forward | That a release can actually be deployed |
| Dependency and secret scanning | Move 4's obligations, continuously rather than once |
| Build reproducibility | That what was tested is what ships |
| Provenance and version pinning | Move 2's requirement, extended to dependencies |

For a regulated product the pipeline is also the **evidence producer** `13-operations` needs: a record that checks ran,
when, and with what result.

---

# When It Applies

In Move 5 (Choose), sized to the team. Its outputs feed `13-operations`' compliance schedule.

---

# How to Apply It Here

**Derive the test suite from acceptance criteria.** `08-product` wrote criteria in given/when/then form precisely so they
could become tests. Criteria that cannot become tests were probably not observable.

**Include the edge cases.** Module 08 worked five categories per MUST requirement. A suite covering only happy paths accepts
the half of the specification where products fail.

**Pin versions and record provenance.** Move 2 requires it for data; the same discipline applies to dependencies, and the
pipeline is where it is enforced.

**Make the pipeline produce evidence.** Timestamped results satisfying a compliance obligation are worth more than the same
checks run manually, because `13-operations` requires evidence produced on a cadence.

**Keep it proportionate.** A pipeline slower than the team's patience gets bypassed. Two minutes of checks that always run
beat twenty minutes that get skipped.

---

# Where It Misleads

**Coverage percentage is treated as the goal.** A suite testing implementation details resists refactoring and proves
little. Criteria-derived tests test behavior, which is what module 08 specified.

**The pipeline is built before there is anything to protect.** Elaborate automation for a product with three requirements
is effort not spent on the requirements. It should grow with the codebase.

**Secret scanning is added after the first leak.** It is a Move 4 obligation with a mechanism, and the mechanism is
cheapest to install before there are secrets to find.

**Green builds are read as working software.** They mean the specified behaviors still behave. Whether the product solves
the problem is `12-metrics`' question and no pipeline answers it.

**Manual steps remain undocumented.** Whatever is not automated must be written down as steps, because it becomes a
`13-operations` runbook whether anyone wrote it or not.

---

# Related

| | |
| --- | --- |
| `Deployment.md` | What the pipeline delivers into |
| `database/Migration.md` | The check that a release is deployable |
| `08-product` | Where acceptance criteria come from |
| `13-operations` | Compliance evidence on a cadence |

---

> **Concept Note**
>
> The pipeline's job is to make the important checks unavoidable — and
> to leave evidence that they ran.
>
> Twenty minutes of checks that get skipped protect nothing.
