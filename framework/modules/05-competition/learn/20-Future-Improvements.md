---
Title: Future Improvements
Module: 05-competition
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: State what the Competition module does not yet do well.
Audience:
  - Product Managers
  - Founders
  - Researchers
Prerequisites:
  - 05-competition/learn/19-Related-Modules.md
Outputs:
  - A candid list of the module's limitations
Related Modules:
  - 02-market
  - 07-strategy
Tags:
  - Competition
  - Improvements
  - Learn
---

# Future Improvements

---

# Known Limitations

**Nothing constrains where the comparison rows come from.** The framework says the
dimensions should derive from module 04's ranked problems. No gate checks it, and the
default behavior — rows from your own roadmap — passes cleanly.

**The gap classification is required in prose, not in structure.** A gap must carry
reasoning. It does not have to carry which of the three explanations applies, so the
reasoning can be a sentence of encouragement.

**Competitive intelligence decays and nothing marks it.** Pricing, features and
positioning change quarterly. A captured price is correct on the day and is carried
forward indefinitely with no staleness signal — the same defect module 02 has with
regulatory citations, and for the same reason.

**Moat and lead are not structurally distinguished.** The output has a field for the
advantage. It has none for how long the advantage survives a determined response, which
is the part module 07 actually needs.

**Indirect competitors are underspecified.** The gate asks for direct and indirect
competitors without defining the boundary between them, so in practice "indirect" holds
whatever did not fit elsewhere.

**No write-back to module 02.** When this module dismisses a gap that module 02
identified, the two documents disagree and the earlier one is not corrected. A reader
consulting only the market section gets a finding this module already killed.

---

# Candidate Improvements

| Candidate | What it would fix | Cost |
| --- | --- | --- |
| Require comparison rows to cite a ranked problem | The self-flattering matrix becomes hard to produce | Small, and it is probably the highest-value change here |
| A structured `gap_reason` field with three values | Classification stops being optional prose | Small |
| A `durability` estimate on each advantage | Module 07 learns how long the opening stays open | Moderate; the estimate is a judgment and will be optimistic |
| A capture date on every competitor fact | Stale intelligence becomes visible | Small, and needs a consumer to matter |
| A definition of indirect competition | The category stops being a residual bin | Small |
| Write-back to module 02's gaps | The two documents stop contradicting each other | Moderate; the engine does not currently support write-back |

---

# What Should Not Change

**The status quo stays in the gate.** It is the module's single most valuable
requirement and the one most likely to be dropped for being unglamorous. In most
markets it is the largest competitor and it never appears in anybody's analysis unless
a rule requires it.

**Pricing stays capture-or-mark-unavailable.** Allowing estimates would let module 06
justify a price against invented figures, and the error would be undetectable.

**Gaps stay unproven until reasoned.** Every version of this module that treats an
empty cell as an opening produces confident strategy aimed at things nobody wants.

**No entry verdict.** The gap analysis is the most persuasive artifact in the research
half of the framework. Letting it also carry a recommendation would collapse three
later modules into its conclusion.

---

> **Improvements Principle**
>
> This module's structural weakness is that it lets you choose the dimensions of your
> own comparison.
>
> One gate criterion — every comparison row traces to a ranked problem — would remove
> most of the flattery this module is prone to.
