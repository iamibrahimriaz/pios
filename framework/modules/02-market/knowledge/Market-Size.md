---
Title: Market Size
Module: 02-market
Section: knowledge
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Explain how a market figure is derived, tagged, and kept honest.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 02-market/knowledge/Market-Definition.md
Outputs:
  - tam_sam_som
Related Modules:
  - 06-business
  - 07-strategy
Tags:
  - Market
  - Sizing
  - Method
---

# Market Size

---

# What It Is

An estimate of how much demand exists inside the bounded market, expressed at three
scopes — TAM, SAM, SOM — each with its **derivation shown**.

The framework treats sizing as a decision input, not a headline. Its purpose is to tell
`07-strategy` and `06-business` whether the market can support the operator's goal. A figure that
cannot be traced to its inputs cannot support that decision, however impressive it looks.

| | Contains |
| --- | --- |
| **A figure** | A number |
| **A size** | A number, its arithmetic, its inputs, and a tag on each input |

---

# When It Applies

In Frame 3 (Size) — **after** Frame 2 (Regulate). The order is deliberate: regulation determines
who may participate at all, and sizing a market before checking who may legally sell in it
produces figures wrong by an order of magnitude.

---

# How to Apply It Here

**Prefer bottom-up.**

```
unit count × realistic price × reachable share = figure
```

Each input is separately checkable, which makes the result correctable. A top-down figure is a
single opaque number and can only be accepted or rejected whole.

**Tag every input.** `[verified: source]`, `[inferred: basis]`, `[assumption: needs validation]`.
One untagged or assumed input makes the whole figure an assumption — precise arithmetic on an
invented input is still an invented result.

**Run both methods where both are available.** If they disagree materially, **the disagreement is
the finding.** Record both, say which is more trustworthy here and why. Do not quietly adopt the
more attractive number.

**Show the arithmetic in the artifact.** A reader must be able to recompute it. This is what makes
a size auditable rather than assertable.

**Use realistic prices, not aspirational ones.** The price used in sizing and the price used in
`06-business` should be the same number, and if it changes there, the size changes with it.

---

# Where It Misleads

**Precision is read as accuracy.** "£412.6m" is more persuasive and no more true than "roughly
£400m". Round to the precision the weakest input supports; a figure derived from one assumed
percentage deserves one significant figure.

**Market reports measure the boundary they chose, not yours.** Lifting their number imports their
definition silently — the borrowed-sizing failure. If a report is used, state its boundary next to
its figure and say how it differs from Frame 1's.

**Big markets reassure, and reassurance stops the questioning early.** A large TAM says nothing
about whether this product can reach anyone. SOM and `11-growth`'s channels carry that answer, and
they are the parts most often left thin.

**Sizing can be run to justify a decision already made.** The signal is inputs that move: if a
share or price assumption rises during the arithmetic, the arithmetic has become advocacy.

---

# Related

| | |
| --- | --- |
| `TAM.md`, `SAM.md`, `SOM.md` | The three scopes in detail |
| `Growth.md` | Whether the figure is moving |
| `06-business` | Where price and margin are set properly |
| `07-strategy` | Where the figure changes a decision |

---

> **Concept Note**
>
> Show the arithmetic, tag the inputs, and round to the precision
> the weakest input supports.
>
> A market size is an argument, not a number.
