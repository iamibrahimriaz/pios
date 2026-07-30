---
Title: Acceptance Criteria
Module: 08-product
Section: knowledge/features
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Write criteria that could fail, and ban the vocabulary that cannot be observed.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 08-product/knowledge/features/Edge-Cases.md
Outputs:
  - acceptance_criteria
Related Modules:
  - 10-execution
  - 14-ai-systems
Tags:
  - Product
  - Acceptance
  - Method
---

# Acceptance Criteria

---

# What It Is

The statements that decide whether a requirement is done.

A criterion is acceptable only if **a person with no context could observe the system and say yes or no without
interpretation.** The form that produces this reliably:

> **Given** «state», **when** «action», **then** «observable result».

**The banned words.** None of these can be observed:

| Banned | Replace with |
| --- | --- |
| fast, performant | a figure — "within «n» seconds" |
| intuitive, easy, user-friendly | a completion rate, or a step count |
| seamless | the absence of a specific interruption |
| robust, reliable | behavior under a named failure |
| appropriate, sensible | the specific thing that happens |

> This is not a style preference. An aspirational criterion cannot be failed, and a criterion that cannot be failed is
> not a criterion — it is a hope in checkbox form.

---

# When It Applies

In Move 6 (Prove), last — because criteria written before behavior test the description rather than the product.

---

# How to Apply It Here

**Write one criterion per behavior, including the edge behaviors.** The five categories from Move 4 each produce
criteria. Happy-path-only criteria accept a half-built requirement.

**Put a number wherever a quality is implied.** If speed matters, the figure comes from `03-user`'s conditions — how long
the user actually has. Invented thresholds are better than adjectives and worse than derived ones.

**Make the "given" state reachable.** A criterion whose precondition cannot be set up cannot be tested, which makes it
decorative.

**For nondeterministic capabilities, write both kinds.** `14-ai-systems` requires a statistical criterion — accuracy
across a set — **and** a per-instance criterion, and it hands the per-instance guarantee back here to be built. A single
average-based criterion accepts a system that fails badly on individual cases.

**Keep implementation out.** A criterion naming a technology tests the build rather than the behavior, and it locks a
`09-technology` decision into a test.

---

# Where It Misleads

**Banned words survive because they read as requirements.** "The interface should be intuitive" looks like a standard
and cannot be failed by anything. The vocabulary list exists because judgment does not catch these reliably.

**Criteria restate the requirement.** "Given the user submits a note, then the note is submitted" is circular. The
observable result must be something distinct from the action.

**Averages accept bad individual cases.** For AI features especially, 92% accuracy is compatible with catastrophic
failures on a recognizable subset. This is why the per-instance criterion is required.

**Criteria are written by the person who wrote the requirement, testing what they meant.** The two-builder standard
applies: name the point where two readings diverge, rather than asking whether it is clear.

**Only MUST requirements get criteria and the edge states are skipped.** Then acceptance is a check that the happy path
works, which is the state most products ship in.

---

# Related

| | |
| --- | --- |
| `Edge-Cases.md` | The behaviors criteria must cover |
| `08-product` `Requirements.md` | Where aspirational language must already be absent |
| `14-ai-systems` | Statistical and per-instance criteria |
| `10-execution` | Where criteria define done |

---

> **Concept Note**
>
> Given, when, then — with a number wherever a quality is implied.
>
> If no plausible observation could fail it, it is not a criterion. It
> is a hope with a checkbox.
