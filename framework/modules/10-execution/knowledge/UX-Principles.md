---
Title: UX Principles
Module: 10-execution
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Derive design principles from research findings so they constrain real decisions.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 10-execution/knowledge/User-Flows.md
Outputs:
  - Principles within ux_flows
Related Modules:
  - 03-user
Tags:
  - Execution
  - UX
  - Concept
---

# UX Principles

---

# What It Is

Design rules that **derive from findings** — the difference between useful and decorative.

| Finding | Principle |
| --- | --- |
| The user is interrupted constantly | Every action must survive being abandoned halfway |
| They work one-handed while standing | No interaction requires two-handed precision |
| Connectivity is unreliable in the setting | The core path completes offline and reconciles later |
| A patient can see the screen | Nothing sensitive is displayed by default |
| They are measured on patients seen, not notes written | The tool must never be the reason a session runs late |

> "Keep it simple" derives from nothing and constrains nothing.

The test for a principle is whether it can **settle a disagreement about a specific screen**. If two designers could both claim
compliance while building opposite things, it is a slogan.

---

# When It Applies

In Move 1 (Flow), stated alongside the paths, and used through the rest of the module as the arbiter for interaction decisions.

---

# How to Apply It Here

**Write each principle with its finding attached.** The citation is what makes it defensible when someone wants to violate it — and
what makes it removable if the finding turns out to be wrong.

**Keep it to three or four.** More than that and none of them decides anything, which is the same failure `01-idea` names about
product goals.

**Derive them from `03-user`'s immovables first.** What will not change is the strongest source of principles available, and it is
the most predictive question in that module.

**Phrase them as constraints, not aspirations.** "No interaction requires two hands" can be violated visibly. "Should be easy to use"
cannot be violated at all, which is why `08-product` bans the vocabulary from criteria.

**Use them to resolve interaction disagreements.** That is their function. A principle never invoked was decoration.

---

# Where It Misleads

**Generic principles are adopted because they are uncontroversial.** Simplicity, consistency, delight. Every product claims them and
none is constrained by them.

**Principles are written after the design.** They then describe what was built rather than governing it, and the derivation runs
backwards.

**They are borrowed from consumer products.** A professional tool used forty times a day rewards density and keyboard efficiency,
which consumer heuristics frequently discourage. `05-competition`'s point applies: unfamiliar is not the same as bad.

**A principle is used to justify scope.** Like `08-product`'s vision problem, a sufficiently broad principle can justify anything.
The finding it derives from is the boundary.

**Conflicts between principles are not resolved.** Density versus clarity, speed versus confirmation. Where two principles collide,
the priority should be stated rather than discovered mid-build.

---

# Related

| | |
| --- | --- |
| `User-Flows.md` | The paths principles govern |
| `Interaction.md` | Where they become concrete decisions |
| `Accessibility.md` | Principles with a legal dimension |
| `03-user` | The findings and immovables they derive from |

---

> **Concept Note**
>
> Every principle names the finding it came from, and can be violated
> visibly.
>
> If two people could build opposite things and both claim compliance,
> it is a slogan.
