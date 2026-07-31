---
Title: Future Improvements
Module: 02-market
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: State what the Market module does not yet do well.
Audience:
  - Product Managers
  - Founders
  - Researchers
Prerequisites:
  - 02-market/learn/19-Related-Modules.md
Outputs:
  - A candid list of the module's limitations
Related Modules:
  - 05-competition
  - 13-operations
Tags:
  - Market
  - Improvements
  - Learn
---

# Future Improvements

---

# Known Limitations

**The sizing gate checks labeling, not derivation.** TAM, SAM and SOM must each be
sourced or marked `[assumption]`. Nothing checks that the three are consistent with
each other, or that SOM was derived from SAM rather than chosen. A run can pass with
three independently invented numbers, each honestly tagged.

**Regulatory coverage depends on knowing what to look for.** The module asks for the
jurisdiction and the applicable regime, and an unknown regime is not found by asking a
better question. Sector-specific obligations — clinical, financial, children's data —
are the ones most often missed, and the framework has no checklist that would surface
them.

**Citations decay and nothing tracks it.** A regulation cited with a date is correct
practice, and the date is never revisited. A run reused eighteen months later carries
its original regulatory findings forward with no signal that they are stale.

**The timing verdict has no evidence requirement.** Trends need direction and evidence.
Timing needs neither. A verdict of RIGHT can be asserted, and modules 07 and 11 will
consume it as though it were established.

**Market gaps are produced here and tested in module 05.** In between, they read like
findings. A gap that module 05 later dismisses is rarely propagated back into this
module's output, so the two documents disagree and nobody notices.

**No mechanism for a market that spans jurisdictions.** The gate names *the*
jurisdiction. Products operating across several get a single answer where they need a
matrix, and the framework currently handles that by convention rather than by
structure.

---

# Candidate Improvements

| Candidate | What it would fix | Cost |
| --- | --- | --- |
| Require SOM to be derived from SAM explicitly | Three unconnected numbers stop passing the gate | Small |
| A sector trigger list for regulatory search | The most expensive misses become less likely | Moderate; the list needs maintaining and will always be incomplete |
| A staleness date on every citation | Reused runs stop carrying dead regulation | Small, and it needs a consumer — a date nobody checks is decoration |
| Evidence requirement on the timing verdict | RIGHT stops being free | Small; one criterion |
| A multi-jurisdiction structure | Cross-border products stop being a special case | Large, and it affects modules 09 and 13 |
| Feed module 05's gap verdict back here | The two documents stop disagreeing | Moderate; requires a write-back the engine does not currently do |

The staleness row is worth reading carefully. Adding a date is trivial; making it
matter requires a module that reads it and acts, and adding the field without that is
the kind of improvement that makes a framework look more rigorous without being so.

---

# What Should Not Change

**Boundary before size.** Every proposal to relax this arrives as a request to allow a
market to be described first and bounded later. The order is the module.

**No entry recommendation.** A module that produces a large number and a verdict in the
same document will have the verdict read off the number. Keeping them separate is what
makes modules 05 through 07 able to disagree with it.

**The regulatory output stays mandatory even when it is empty.** "No sector-specific
obligations identified for this jurisdiction" is a finding with a name attached.
Omitting the section entirely is indistinguishable from not having looked.

---

> **Improvements Principle**
>
> This module's weakest point is that its outputs look finished.
>
> A number, a verdict and a citation all present as conclusions. Three of the six
> limitations above exist because nothing in the framework asks how any of them were
> reached.
