---
Title: Future Improvements
Module: 04-problem
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: State what the Problem module does not yet do well.
Audience:
  - Product Managers
  - Founders
  - Researchers
Prerequisites:
  - 04-problem/learn/19-Related-Modules.md
Outputs:
  - A candid list of the module's limitations
Related Modules:
  - 07-strategy
  - 10-execution
Tags:
  - Problem
  - Improvements
  - Learn
---

# Future Improvements

---

# Known Limitations

**Evidence strength is a tag, not a scale.** `[verified: 4 interviews]` and
`[verified: 200-response survey with observed behavior]` carry the same weight in the
ranking. The distinction exists in the note and disappears in the arithmetic.

**Sample size is optional in practice.** Nothing requires an `n`. A finding from one
conversation and a finding from twenty are formatted identically, and the ranking
treats them the same.

**Nothing verifies that a shortfall was carried.** Module 07 is required to weight a
declared shortfall, and no mechanism checks that it did. The chain depends on
discipline at three separate points, and a run can declare, ignore, and pass every gate.

**The three axes are combined by judgment, not by rule.** Frequency, severity and
workaround produce three scores and one ranking, with no stated method for combining
them. That flexibility is deliberate — a fixed weighting would be wrong in most
domains — and it is also where a reverse-engineered ranking hides.

**Problems that belong to an organization rather than a person are handled poorly.**
The scoring axes are individual: how often does *this person* encounter it. A problem
that costs an organization heavily while inconveniencing no individual scores low and
may be the most valuable one available.

**The validation plan has no owner or date.** It is produced and then depends on
somebody deciding to run it. Module 10 can sequence it as Milestone Zero, but only if
someone connects the two.

---

# Candidate Improvements

| Candidate | What it would fix | Cost |
| --- | --- | --- |
| Require `n` on every evidence entry | Sample size stops being invisible | Small, and uncomfortable — most honest answers are small |
| An evidence-strength scale feeding the score | Strong and weak verification stop being equal | Moderate; any scale is arguable |
| A shortfall-carried check in module 07's gate | The chain stops depending on memory | Small and high value — probably the best change on this page |
| An organizational-impact axis | Aggregate-cost problems stop being underranked | Moderate; adds a fourth axis, and axes multiply |
| Owner and date on the validation plan | Plans stop evaporating | Small |
| A stated method for combining the three axes | Reverse-engineering gets harder | Contentious — a fixed formula would be wrong in many domains, and gameable in the rest |

The third row deserves emphasis. The `declared_shortfall` mechanism is the framework's
most distinctive feature and its weakest link is not the declaration — it is the
absence of any check that anything downstream responded.

---

# What Should Not Change

**`declared_shortfall` stays an exception.** Every review eventually asks why other
modules cannot declare shortfalls too. Because the moment a gate can be waived by
declaration everywhere, no gate is binding anywhere. This module has it because it is
the one place where the honest answer before launch is frequently "not enough evidence
yet," and the alternative is either halting most runs or inviting manufactured proof.

**Solutions stay three modules away.** The friction is the point.

**Workaround stays one of the three axes.** It is the axis that catches the real,
severe, frequent, and already adequately solved problem — a case nothing else in the
framework detects at this stage.

**The verified/inferred distinction stays absolute.** No partial credit, no "strongly
inferred" tier. Every intermediate category invented for this purpose becomes the
default within a few runs.

---

> **Improvements Principle**
>
> The mechanism that makes this module honest — declaring what is missing — has no
> enforcement at the other end.
>
> That is the most important unfixed thing in the framework, and it is fixable with one
> criterion in module 07's gate.
