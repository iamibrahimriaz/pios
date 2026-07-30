---
Title: Solution Exploration
Module: 07-strategy
Section: knowledge/solutions
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Generate genuinely different approaches, and guard against the straw man.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 07-strategy/core/06-Framework.md
Outputs:
  - solution_options
Related Modules:
  - 04-problem
  - 05-competition
Tags:
  - Strategy
  - Options
  - Method
---

# Solution Exploration

---

# What It Is

The generation of at least three approaches to the sharpest problem, subject to one test:

> **Would each option produce a different first build?**

If all three start by building the same thing and differ only in what comes after, they are one option described
three ways.

Five shapes worth exploring deliberately, because they produce genuinely different first builds:

| Shape | Question it answers |
| --- | --- |
| **Narrow tool** | What if we solved only the sharpest problem, completely? |
| **Workflow replacement** | What if we replaced the whole process? |
| **Layer on top** | What if we sat on the incumbent instead of replacing it? |
| **Service, not software** | What if a person did this and software came later? |
| **Different segment first** | What if we started with the second-priority segment? |

For each option: what it is, which problems it solves, what the first build would be, the price it supports, its
defensibility, and its biggest risk.

---

# When It Applies

In Move 1 (Diverge), before any comparison. The gate requires three options generated **before** one is chosen.

---

# How to Apply It Here

**Guard against the straw man.** Generating one real option and two obviously worse ones satisfies the count and
defeats the purpose. **Each option must be one a competent person could reasonably choose** — the same rule
`14-ai-systems` applies to its non-AI alternative, and for the same reason.

**Include the service option honestly.** For many problems, a person doing the work is faster to start, proves
demand, and produces the data a later automation needs. `04-problem`'s Wizard of Oz method is its validation
counterpart.

**Include the layer option where an incumbent owns the system of record.** `03-user`'s immovables usually say whether
replacement is even available, and a layer avoids the switching cost that defeats most entrants.

**Write the first build for each, concretely.** That is what makes the difference test checkable. If two first builds
are the same, merge the options and generate another.

**Let an option be the one that follows from `05-competition`'s gap.** The gap analysis pointed somewhere; at least
one option should go there, and if none does, the module has drifted from its inputs.

---

# Where It Misleads

**Options get generated after the decision has been made.** The tell is two options with visible flaws and one
without. This is the module's named failure, and the gate ordering — three before one — exists to make it detectable.

**Three feature scopes of the same product get presented as three options.** Small, medium and large versions of one
approach differ in scope, not in shape. None of the five shapes above is a scope.

**The service option is dismissed as not being a product.** It is a route to a product with revenue and evidence
attached. Dismissing it early removes the only option that can start this month.

**Exploration continues past usefulness.** Three genuinely different options is the requirement; ten is a way of
avoiding Move 3. The purpose is a decision.

**Options are shaped to fit the technology already chosen.** If every option requires the same mechanism, the
mechanism was decided before the problem was examined — and `14-ai-systems` will have to unwind it.

---

# Related

| | |
| --- | --- |
| `Alternative-Solutions.md` | Non-obvious and non-software approaches |
| `Tradeoffs.md` | Comparing and choosing between them |
| `MVP-Solution.md` | The narrow-tool shape in detail |
| `05-competition` | Where the gap points |

---

> **Concept Note**
>
> Different options produce different first builds. Everything else is
> one option with three descriptions.
>
> And every option must be one a competent person could choose — a
> straw man invalidates the comparison, not just the option.
