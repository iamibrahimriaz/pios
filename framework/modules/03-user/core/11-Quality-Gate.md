---
Title: Quality Gate
Module: 03-user
Section: core
Category: Gate
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define how the User module's gate is evaluated, criterion by criterion.
Audience:
  - AI Agents
Prerequisites:
  - 03-user/module.yaml
  - engine/gates.yaml
Outputs:
  - Gate verdict recorded in state.run
Related Modules:
  - 02-market
  - 04-problem
Tags:
  - User
  - Quality
  - Gate
---

# Quality Gate

---

# Overview

`module.yaml` states the gate criteria. This document explains how to evaluate each one.

Six modules build on the person described here. This gate is where an invented user is
caught — or permanently absorbed into the blueprint.

---

# Governing Rule

> A gate is failed by default when its status cannot be determined.
>
> Uncertainty is a fail, not a pass.

---

# Criterion 1 — >= 2 segments with a stated reason for prioritizing one

**Passes when:** two or more segments exist, they differ **behaviorally**, each is scored
on pain intensity, ability to pay and reachability, one is chosen, and the choice
references the scoring rather than preference.

**Test:** would these two segments buy, use, or reject the product for different reasons?
If not, they are one segment written twice, and the criterion fails regardless of how many
rows the table has.

| Fails | Passes |
| --- | --- |
| "Small practices" and "practices aged under 10 years" | "Solo practices with no shared records" and "two-to-five doctor practices with a shared system" — the second has a migration problem and an internal approver; the first has neither |

**Also required:** if a larger segment was passed over, the reason is stated. A
prioritization that ignores the biggest group without explaining why is incomplete.

---

# Criterion 2 — Jobs stated as jobs, not features

**Passes when:** every job follows `When «situation», I want to «motivation», so I can
«outcome»`, and **none names a product, tool, or feature**.

**Test:** read each job aloud and ask whether it would still be true if the product were
built completely differently. A job survives changes of solution. A feature does not.

| Fails | Passes |
| --- | --- |
| "They want voice dictation" | "When a patient is describing symptoms, I want to capture what they said without breaking eye contact, so I can stay present in the consultation" |
| "They need a dashboard" | "When I start my week, I want to know which accounts are at risk, so I can act before they leave" |

One feature-shaped job fails the criterion. It is the mechanism by which a predetermined
solution enters the blueprint disguised as a user need.

---

# Criterion 3 — Current workflow documented including the tools being replaced

**Passes when:** the workflow is broken into steps, each step names the tool used, friction
points are identified, and the products being replaced are **named**.

**Fails when:** the workflow is described in general terms, or tools are referred to
generically ("their existing system") rather than named.

**Why naming matters:** the tool being replaced is usually the real competitor. Module 05
needs the name. "Paper" and "spreadsheet" are valid, important answers — the status quo
is a competitor and often the strongest one.

**Also required:** per-step confidence. A workflow where step 3 is evidenced and step 4 is
inferred must say so.

---

# Criterion 4 — Cost of switching named

**Passes when:** all five dimensions are assessed — data migration, retraining, workflow
disruption, contractual lock-in, and perceived risk — each with a magnitude, and the bar
the product must clear is stated.

**Fails when:** switching cost is absent, or asserted as "low" without reasoning.

A product that ignores switching cost gets built, launched, and loses to an inferior tool
that is already installed. This criterion exists because that failure is both common and
entirely predictable at this stage.

---

# Criterion 5 — Each user finding marked observed or reported

**Passes when:** every workflow and behavior claim states whether it was watched or
described.

**Fails when:** interview statements and observations are formatted identically. They are
not equivalent evidence, and module 04 currently weights them the same.

**Note.** Marking everything `reported` is a passing answer. It is also a finding about the
run's evidence base, which is the point.

---

# Criterion 6 — Switching cost broken into its five components, not carried as one figure

**Passes when:** data migration, retraining, workflow disruption, contractual lock-in and
perceived risk each carry a value or an explicit unknown.

**Fails when:** a single number is given. The composition is what module 11 needs — an
adoption barrier caused by retraining is addressed differently from one caused by contract
timing.

---

# Module-Specific Check — Evidence Honesty

Not in `module.yaml`, but enforced by universal gate U1 and the evidence policy. In this
module it deserves separate attention:

| Check | Fails if |
| --- | --- |
| Research mode declared | The header does not state Primary, Proxy, or Inferred |
| No invented quotes | Any user voice lacks a source |
| No invented statistics | Any figure lacks a source or an assumption tag |
| Persona rows traceable | Any attribute is presented as fact without a tag |
| Confidence matches mode | Confidence is `high` while mode is Proxy or Inferred |
| Gaps section present | "What we do not know" is missing |

**A fabricated user quote fails the gate outright**, regardless of every other criterion.
It is undetectable downstream and contaminates the PRD, the flows, and the pitch.

---

# Universal Gates

U1–U7 apply. Most often missed here:

| | |
| --- | --- |
| **U1** | Persona prose invites untagged assertion more than any other module's output |
| **U3** | The prioritized segment must sit inside `market_definition` — check it explicitly |
| **U5** | Every inferred persona attribute is an assumption and needs a validation method |

---

# Evaluation Procedure

1. Run the four passes of `engine/review-loop.md`.
2. Verify every quote resolves to a source.
3. Verify the segment sits inside the market boundary.
4. Evaluate universal gates U1–U7.
5. Evaluate criteria 1–4 and the evidence honesty checks.
6. Record the verdict.

```yaml
gate:
  module: 03-user
  attempt: 1
  research_mode: proxy
  criteria:
    two_segments_with_priority: pass
    jobs_not_features: fail
    workflow_with_named_tools: pass
    switching_cost_named: pass
  evidence_honesty:
    mode_declared: pass
    no_invented_quotes: pass
    persona_rows_traceable: pass
    confidence_matches_mode: pass
  verdict: fail
  reason: "J2 reads 'wants automated reminders' — names a solution, not a job."
  action: "Rewrite J2 in When/I want/So I can form."
```

---

# On Failure

`module.yaml` sets `on_fail: return to 02-market`.

| Kind | Example | Action |
| --- | --- | --- |
| **Local** | A job names a feature | Revise here |
| **Upstream** | No coherent segment exists inside the boundary | Return to `02-market` |

A market so broadly bounded that every segment behaves identically is an upstream defect.
Fixing it here by narrowing informally leaves `market_definition` wrong for modules 05
and 06.

| Attempt | Action |
| --- | --- |
| 1–2 | Revise or regress |
| 3 | Halt. Escalate with the specific question |

---

# What a Passing Module 03 Looks Like

- The two segments would clearly behave differently, and it is obvious why one was chosen.
- The persona could not describe anyone else in the market.
- Every persona row can be traced, or is openly marked as inference.
- The workflow names real products, including paper and spreadsheets where true.
- Switching cost is assessed honestly, including the parts that make adoption hard.
- Every job would survive the product being built a completely different way.
- A reader knows immediately whether a real user was consulted.

---

> **Gate Principle**
>
> This is the last point at which an invented user is still visible.
>
> After this gate, the fiction becomes the specification.
