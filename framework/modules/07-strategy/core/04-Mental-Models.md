---
Title: Mental Models
Module: 07-strategy
Section: core
Category: Thinking Framework
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define the lenses through which strategic options should be examined.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 07-strategy/core/03-Core-Principles.md
Outputs:
  - Multi-perspective strategic analysis
Related Modules:
  - 08-product
Tags:
  - Strategy
  - Mental Models
---

# Mental Models

---

# Model Statement

> A decision looks obvious once made.
>
> These lenses exist to make it non-obvious for long enough to examine it.

---

# 1. The Shape Catalog

**Reveals:** options you would not have generated.

Most option lists contain one idea at three sizes. Working a catalog of *shapes* forces
genuine alternatives:

| Shape | The question |
| --- | --- |
| Narrow tool | What if we solved only the sharpest problem, completely? |
| Workflow replacement | What if we replaced the whole process? |
| Layer on top | What if we sat on the incumbent instead of fighting it? |
| Service first | What if a person did this and software came later? |
| Different segment | What if we started with the second-priority segment? |
| Different buyer | What if we sold to the employer rather than the user? |

**Hides:** the catalog can generate options nobody would choose. Shape is a prompt, not a
justification — each still has to survive the advocate test.

---

# 2. The Advocate Test

**Reveals:** straw men.

For each rejected option, write the strongest honest case *for* it in one sentence.

If the sentence cannot be written, the option was decoration and the choice was made
before the module ran.

**Hides:** a good advocate sentence can be written for almost anything. It filters
decoration, not weak strategy.

---

# 3. The End-to-End Test

**Reveals:** whether the MVP is a product or a fragment.

Walk the persona's workflow, step by step, against the capabilities above the line.

Can they complete the core job? If not, the cut is wrong — however much was included.

**Hides:** it says nothing about whether they would *want* to. Completeness is necessary,
not sufficient.

---

# 4. What This Release Answers

**Reveals:** the question the MVP is actually asking.

Every release is an experiment. State in advance:

| | |
| --- | --- |
| What it proves | The specific belief it tests |
| What it does not prove | What remains unknown afterward |

Without the second line, weak adoption gets read as "the problem was not real" when the
release never tested that.

**Hides:** the framing can be too narrow. A release can also fail for reasons nobody
listed — usability, timing, trust.

---

# 5. Regret Minimization

**Reveals:** which mistake is more survivable.

Ask, for each option: *if this is wrong, what does it cost, and can we recover?*

| | |
| --- | --- |
| Cheap to be wrong | Prefer, when uncertainty is high |
| Expensive to be wrong | Requires stronger evidence first |

Under high uncertainty — an assumed problem, a thin business model — the option that
survives being wrong is often worth more than the one that scores highest when right.

**Hides:** minimizing regret can become minimizing ambition. Some products only exist
because someone made an unrecoverable bet.

---

# 6. Reversibility

**Reveals:** how much evidence a decision needs.

| Type | Standard of evidence |
| --- | --- |
| Reversible | Decide quickly, learn by doing |
| Expensive to reverse | Require evidence first |
| Irreversible | Requires the highest bar, and a stated bet |

Most product decisions are reversible and get treated as though they were not. A few —
data model shape, regulatory posture, market positioning — genuinely are not, and get
treated casually.

**Hides:** reversibility is often assessed optimistically. Ask what it would cost in
practice, not in principle.

---

# 7. The Clock

**Reveals:** how long the opportunity lasts.

From module 05's defensibility verdict. If an incumbent could close the gap in six months,
the strategy must include what happens then.

| Defensibility | Strategic implication |
| --- | --- |
| Strong | Build carefully; time is available |
| Moderate | Move fast on the wedge, build the moat behind it |
| None | The plan is speed and a specific segment relationship, or it is a feature |

**Hides:** incumbents are frequently slower than the model assumes. The point is to plan
for the clock, not to assume it always runs.

---

# 8. Inversion — the Pre-Mortem

**Reveals:** risks that a forward-looking register misses.

Imagine it is eighteen months from now and the product failed. Write the explanation.

Working backwards from failure produces different risks than working forwards from the
plan — usually organizational, commercial, or about attention rather than technology.

**Hides:** it can generate an unbounded list. Keep the ones with an observable early
warning; those are the actionable ones.

---

# 9. Confidence Inheritance

**Reveals:** where certainty was manufactured.

Read the strategy against the modules it came from. Is any statement more confident than
its source?

| Source said | Strategy must not say |
| --- | --- |
| The problem is assumed | "The problem is" |
| The gap could be closed quickly | "Our defensible advantage" |
| Viable under conditions | "Viable" |

**Hides:** nothing. It is a mechanical check and it catches the module's most common
failure.

---

# 10. The Refusal Test

**Reveals:** whether a strategy exists at all.

Read the document and list what it refuses to do.

If the list is empty or generic, there is no strategy — only a summary of research with a
build order attached.

**Hides:** refusals can be performative. "We will not build an enterprise tier" is only a
refusal if someone was arguing for one.

---

# Combining Models

| Situation | Model |
| --- | --- |
| Generating real alternatives | The Shape Catalog |
| Detecting decoration | The Advocate Test |
| Validating the cut | The End-to-End Test |
| Making the release readable | What This Release Answers |
| Choosing under high uncertainty | Regret Minimization |
| Setting the evidence bar | Reversibility |
| Pacing the plan | The Clock |
| Finding missed risks | The Pre-Mortem |
| Checking honesty | Confidence Inheritance |
| Checking whether this is a strategy | The Refusal Test |

Apply the Shape Catalog first, Confidence Inheritance and the Refusal Test last.

---

# Self Assessment

- Did I work the shape catalog, or generate three sizes of one idea?
- Can I write an honest advocate sentence for each rejected option?
- Did I walk the workflow to test the cut?
- Do I know what this release does not answer?
- Under my uncertainty, did I weigh survivability as well as score?
- Do I know which of my decisions are irreversible?
- Have I planned for the clock, if there is one?
- Did the pre-mortem find anything the forward register missed?
- Is anything here more confident than its source?
- What does this strategy refuse to do?

---

> **Mental Model Principle**
>
> The last question is the whole module.
>
> If the answer is "nothing much", the work is not finished.
