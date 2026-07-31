---
Title: Quality Gate
Module: 02-market
Section: core
Category: Gate
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define how the Market module's gate is evaluated, criterion by criterion.
Audience:
  - AI Agents
Prerequisites:
  - 02-market/module.yaml
  - engine/gates.yaml
Outputs:
  - Gate verdict recorded in state.run
Related Modules:
  - 01-idea
  - 05-competition
Tags:
  - Market
  - Quality
  - Gate
---

# Quality Gate

---

# Overview

`module.yaml` states the gate criteria. This document explains how to evaluate each one.

Four modules consume this module's output. A defect that passes here is inherited by all
four, and none of them will re-examine it.

---

# Governing Rule

> A gate is failed by default when its status cannot be determined.
>
> Uncertainty is a fail, not a pass.

---

# Criterion 1 — Market defined by boundary, not by adjective

**Passes when:** the definition names *who*, *what need*, and *where*, lists explicit
exclusions, and rules on at least one borderline case.

**Test:** take a company that is arguably in this market. Can the definition alone decide
whether it is in or out? If it requires a judgment call not covered by the definition,
the boundary is not drawn.

| Fails | Passes |
| --- | --- |
| "The healthcare software market" | "Clinical documentation tools sold to solo and two-doctor general practices in «jurisdiction». Excludes hospital EMRs (different buyer, procurement-led) and consumer health apps (not clinician-facing)." |

---

# Criterion 2 — TAM / SAM / SOM each sourced or explicitly marked [assumption]

**Passes when:** all three figures exist, each shows its derivation, and every input in
that derivation carries a tag.

**Fails when:** a figure appears without arithmetic, or when the arithmetic contains an
untagged input.

Partial credit is not available. One unsourced, untagged input makes the whole figure an
assumption — and if it is not labeled as one, the criterion fails.

| Fails | Passes |
| --- | --- |
| "SAM: $180M [verified: «report»]" | "SAM: $180M = 12,400 practices [verified: registry, 2025] × $1,450/yr [inferred: competitor pricing] × 100% serviceable [verified: no licensing barrier]" |

**Additional check:** if an external figure was adopted, was its boundary compared to the
boundary in Criterion 1? An unchecked external figure is measuring a different market.

---

# Criterion 3 — >= 3 trends with direction and evidence

**Passes when:** three or more trends exist, each states a direction (growing / declining),
each carries evidence, each states an implication — **and at least one works against the
idea.**

**The unfavorable-trend requirement is part of this criterion.** An analysis where every
trend is favorable did not research the market; it researched the idea.

| Does not count | Counts |
| --- | --- |
| "AI is important in healthcare" | "Ambient documentation tools moved from pilot to procurement in large systems during 2024–25 [verified: «source»] — growing; implies the window for a solo-practice wedge may be 18–24 months" |

---

# Criterion 4 — Regulatory constraints for the named jurisdiction identified

**Passes when:** the jurisdiction came from `idea_brief` (never inferred), applicable
regimes are named with their triggers, and each states **concrete obligations** rather
than a regime name.

**The downstream test:** could an engineer reading only the regulatory section design a
compliant data model? If it says "HIPAA applies" and nothing more, no.

**Also required:** an explicit answer to *does regulation exclude a segment named in the
idea brief?* Silence fails the criterion — that question can end the run early and must
be answered rather than skipped.

---

# Criterion 5 — Every regulatory and pricing claim carries the date it was checked

**Passes when:** each citation carries the date it was verified.

**Fails when:** a regulation or price appears without one, including when it is correct —
an undated fact cannot be revalidated, and this module's findings are consumed by four
later modules.

**Why it matters here.** A run reused in a year carries regulatory findings forward with no
signal that they are stale.

---

# Universal Gates

`engine/gates.yaml` U1–U6 apply. Most often missed in this module:

| | |
| --- | --- |
| **U1** | Every claim tagged. Market prose is where untagged assertions hide most easily |
| **U3** | No contradiction with `idea_brief` — check that the market did not quietly widen beyond the brief's segment |
| **U6** | The regulatory section is read by module 09 seven steps later. Write for a stranger |

---

# Evaluation Procedure

1. Run the four passes of `engine/review-loop.md`.
2. Verify every `[verified]` tag resolves to a row in the Sources table.
3. Evaluate universal gates U1–U6.
4. Evaluate criteria 1–4.
5. Record the verdict in `state.run`.

```yaml
gate:
  module: 02-market
  attempt: 1
  criteria:
    boundary_not_adjective: pass
    sizing_sourced: fail
    three_trends_with_direction: pass
    regulatory_identified: pass
  universal: [U1 pass, U2 pass, U3 pass, U4 pass, U5 pass, U6 pass]
  verdict: fail
  reason: "SAM adopted from an analyst report; its boundary was never compared to §1."
  action: "Rebuild SAM bottom-up from practice count and price."
```

---

# On Failure

`module.yaml` sets `on_fail: return to 01-idea`.

Distinguish two kinds of failure:

| Kind | Example | Action |
| --- | --- | --- |
| **Local defect** | Sizing lacks derivation | Revise within this module |
| **Upstream defect** | The brief's segment is too vague to bound a market | Return to `01-idea` |

Do not return upstream for a defect this module can fix. Do not patch locally a defect
that originates in the brief — it will resurface at module 05.

| Attempt | Action |
| --- | --- |
| 1–2 | Revise or regress as appropriate |
| 3 | Halt. Escalate with the specific unresolvable question |

---

# What a Passing Module 02 Looks Like

- A practitioner in the domain would recognize the category name.
- The boundary decides borderline cases without further judgment.
- Every figure can be argued with, because the arithmetic is visible.
- The regulatory section is a specification, not a list of acronyms.
- At least one trend makes the idea look harder than it did before.
- Each gap explains why nobody has closed it.
- A reader can tell exactly which parts are established and which are believed.

---

> **Gate Principle**
>
> Four modules read this module's output and none of them will re-check it.
>
> This gate is the last point at which a wrong boundary is cheap to fix.
