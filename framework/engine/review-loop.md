---
Title: Review Loop
Layer: Engine
Version: 1.0.0
Status: Approved
Purpose: Define the self-review an agent performs before submitting any module output to its gate.
Binding: Mandatory before every gate evaluation.
---

# Review Loop

Generation and review are different tasks. An agent that reviews in the same pass it writes
will approve its own reasoning, because the reasoning is still what it believes.

The review loop forces a separate pass with a different posture: **the writer argues for the
output, the reviewer argues against it.**

---

# The Four Passes

Run in order. Each pass has one job.

## Pass 1 — Completeness

*Is anything missing?*

- Does every item in `produces` exist?
- Was every question in `core/08-Questions-To-Answer.md` addressed, or explicitly deferred?
- Are there sections that exist but say nothing?

A section written to satisfy a template, containing no information, is worse than an absent
section — it hides the gap.

## Pass 2 — Evidence

*Can this be trusted?*

Apply the checklist in `evidence-policy.md`. Specifically hunt for claims that read as fact
but were never sourced. These hide in confident prose.

## Pass 3 — Adversarial

*Why is this wrong?*

The most valuable pass. Argue against the module's own conclusion:

- What would have to be true for this to fail?
- What is the strongest case for the opposite conclusion?
- Which competitor or incumbent already tried this, and what happened?
- What is being assumed about user behaviour that has never been observed?
- If this recommendation is wrong, which claim was the weak link?

If the adversarial pass produces nothing, it was not performed honestly. Every real
conclusion has a case against it.

## Pass 4 — Coherence

*Does this contradict what we already established?*

Read `state.evidence_log` and `state.decisions`. Does this module's output conflict with an
earlier one? Contradictions between modules are the most common defect in a long run, and
the least visible — each module reads fine alone.

If a contradiction is found, resolve it explicitly. Supersede the earlier claim with a
reason recorded, or correct this one. Never leave both standing.

---

# Output of the Loop

The loop produces a verdict, not a feeling:

```yaml
review:
  module: 05-competition
  completeness: pass
  evidence: pass
  adversarial:
    strongest_counterargument: >
      Incumbents already ship ambient capture as an add-on; the gap may be
      distribution, not capability.
    resolved: true
    resolution: Repositioned the gap as workflow-native rather than feature-new.
  coherence: pass
  verdict: proceed
```

`verdict` is one of:

| Verdict | Meaning |
| --- | --- |
| `proceed` | All four passes clean. Submit to gate. |
| `revise` | Fixable within this module. Revise and re-run the loop. |
| `regress` | The defect originates upstream. Follow `on_fail`. |

---

# What This Is Not

This is not a quality checklist to tick. It is a deliberate attempt to break the work while
it is still cheap to break.

The framework's value comes from catching a wrong assumption at module 04 rather than after
six months of building on it.

---

> **Engine Principle**
>
> The reviewer's job is not to approve the work.
> It is to find the reason the work should not be approved — and to say so when it finds one.
