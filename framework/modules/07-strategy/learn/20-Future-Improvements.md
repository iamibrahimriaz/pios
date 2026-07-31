---
Title: Future Improvements
Module: 07-strategy
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: State what the Strategy module does not yet do well.
Audience:
  - Product Managers
  - Founders
  - Researchers
Prerequisites:
  - 07-strategy/learn/19-Related-Modules.md
Outputs:
  - A candid list of the module's limitations
Related Modules:
  - 04-problem
  - 08-product
Tags:
  - Strategy
  - Improvements
  - Learn
---

# Future Improvements

---

# Known Limitations

**Confidence laundering has no detection.** The framework names the failure and offers
procedural defenses. Nothing in the output distinguishes a laundered choice from a real
one, and nothing can — the artifacts are identical.

**Nothing verifies that a declared shortfall was weighted.** This is the framework's
most important unenforced rule. Module 04 can declare, this module can ignore, and every
gate passes. One criterion here — "if a shortfall was declared, name the weight it
changed" — would close it.

**Option distinctness is unchecked.** The gate counts three options. Three variants of
the same premise satisfy it exactly as well as three structurally different approaches.

**Weights have no required justification.** They are where judgment legitimately enters
and where laundering hides, and the schema treats them as numbers.

**The MVP has no required learning objective.** "Draw the cut line with the reasoning
recorded" permits reasoning about effort rather than about what the release will teach.

**Non-goals and deferrals are one list in practice.** The distinction matters to modules
08 and 14 and is maintained by convention.

**No reconsideration point.** A strategy chosen here is elaborated by six modules and
never revisited unless a cost check forces a regress. Findings that accumulate in
modules 09 and 10 — an unresolved blocker, a much larger build estimate — do not trigger
a re-comparison.

---

# Candidate Improvements

| Candidate | What it would fix | Cost |
| --- | --- | --- |
| A gate criterion naming the weight a shortfall changed | Closes the framework's biggest unenforced chain | Small, and the single best change available |
| Required justification text per weight | Laundering gets harder to perform unconsciously | Small |
| A distinctness test on options — at least one non-build | Three-costume option sets stop passing | Moderate; "distinct" is a judgment |
| A required `mvp_learning_objective` field | MVPs stop being small products | Small |
| Separate `non_goals` and `deferred` lists in the schema | Modules 08 and 14 stop relying on convention | Small |
| A reconsideration trigger from modules 09/10 | A strategy invalidated by build reality gets revisited | Large; the engine has no re-entry mechanism |

The first row is worth stating twice. The `declared_shortfall` mechanism is the
framework's most distinctive feature, and its entire value depends on something
happening here that nothing checks.

---

# What Should Not Change

**Three options stays a hard requirement.** Every proposal to relax it comes from a run
where the answer felt obvious. Those are exactly the runs where a second option is worth
the most.

**The ranked problems stay the criterion.** Alternatives get proposed — strategic fit,
team capability, market attractiveness — and each of them is a place a preference can
hide. The ranking is the only criterion in the framework that is external to the person
choosing.

**Non-goals stay mandatory.** A strategy without them is a plan, and the framework
already has a module for plans.

**The module stays the only decision point.** Distributing decisions across modules 08
through 10 would make each one locally sensible and the whole unaccountable.

---

> **Improvements Principle**
>
> This module names a failure it cannot detect and depends on a chain it does not
> enforce.
>
> Both are fixable in the same place — a gate criterion that asks what the shortfall
> changed — and until that exists, the defense is entirely the discipline of the person
> doing the work.
