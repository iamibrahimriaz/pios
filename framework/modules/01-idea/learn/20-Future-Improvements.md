---
Title: Future Improvements
Module: 01-idea
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: State honestly what the Idea module does not yet do well, so improvements are directed rather than decorative.
Audience:
  - Product Managers
  - Founders
  - Researchers
Prerequisites:
  - 01-idea/learn/19-Related-Modules.md
Outputs:
  - A candid list of the module's limitations
Related Modules:
  - 02-market
  - 04-problem
Tags:
  - Idea
  - Improvements
  - Learn
---

# Future Improvements

---

# Overview

A framework that lists only its strengths teaches people to trust it in the places it
should not be trusted. What follows is what this module currently does badly.

---

# Known Limitations

**The five-question gate is a count.** The quality gate requires at least five
clarifying questions asked and answered or deferred. Nothing checks whether any of
them could have changed the direction, and a run can satisfy the criterion with five
comfortable questions. The evaluation exercises push against this for humans; the
engine has no equivalent.

**Deferral has no expiry.** A question deferred here can travel to module 13 without
ever being revisited. The framework records deferrals but does not chase them, and
there is no mechanism equivalent to the `declared_shortfall` that module 04 uses to
make an absence visible downstream.

**Assumption tagging is not weighted.** Every `[assumption]` looks alike. In practice
one or two carry the premise and the rest are incidental, but nothing in the output
distinguishes them. Module 07 has to rediscover which assumption was load-bearing,
usually by finding out the hard way.

**The idea's origin is not captured.** Whether the idea came from a personal
frustration, an observed market gap, or an available capability changes which blind
spots apply — and none of it is recorded. `17-Reflection.md` asks a human to notice;
the brief has no field for it.

**Scope boundaries are stated once and never re-checked.** They constrain module 07's
cut line, but no gate in between asks whether the boundary set before any research
still makes sense after three modules of it.

---

# Candidate Improvements

| Candidate | What it would fix | Cost |
| --- | --- | --- |
| A `load_bearing` flag on assumptions | Module 07 stops rediscovering the critical one | Small; a schema change and a judgment call |
| A deferral register carried forward | Deferred questions stop disappearing | Moderate; needs an owner at each gate |
| An `idea_origin` field | Makes the characteristic blind spot inspectable | Small, and possibly cosmetic |
| A boundary re-check at module 05 | Catches boundaries that research invalidated | Moderate; adds a gate criterion |
| A question-quality criterion | The five-question gate stops being satisfiable by count | Hard — quality is not mechanically checkable, and a bad check is worse than none |

The last row is honest about why it has not been done. Any automated test for
"question that could change the direction" would be gameable, and a gameable gate
teaches people to game it.

---

# What Should Not Change

**The module must not acquire a verdict.** Every review of this framework eventually
produces the suggestion that the Idea module should score the idea. It should not.
A score at this stage would be preference wearing a number, and — worse — it would be
inherited by eleven modules as though it were a finding.

**The halt-and-ask failure path must stay.** It is inconvenient, and it is the only
place in the framework that admits some things cannot be inferred. Replacing it with a
default would remove the one honest stop.

**Assumption tagging must not become optional for speed.** Every proposal to make the
idea stage lighter arrives as a proposal to skip the tags. The tags are the stage.

---

# How to Propose a Change

State which limitation above it addresses, what it would cost the operator in effort,
and what it would break. A change to this module is a change to every module, because
everything downstream consumes its outputs — so the burden of proof sits higher here
than anywhere else in the framework.

---

> **Improvements Principle**
>
> The most dangerous improvement to this module is the one that makes it produce a
> verdict.
>
> Everything else on this page is a gap. That one would be a defect, arriving with the
> authority of a finding.
