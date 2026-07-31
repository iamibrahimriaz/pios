---
Title: Future Improvements
Module: 09-technology
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: State what the Technology module does not yet do well.
Audience:
  - Product Managers
  - Founders
  - Engineers
Prerequisites:
  - 09-technology/learn/19-Related-Modules.md
Outputs:
  - A candid list of the module's limitations
Related Modules:
  - 02-market
  - 13-operations
Tags:
  - Technology
  - Improvements
  - Learn
---

# Future Improvements

---

# Known Limitations

**Nothing checks that every obligation has a mechanism.** The gate says regulatory
requirements are "reflected in the security model." Reflected is not mechanized, and a
document can reflect an obligation in a sentence.

**The regulated column list is a convention.** Three modules check against it and no
field holds it. In practice it lives in prose, which means the downstream checks are
performed against whatever the reader interprets.

**Architecture inflation has no test.** The date-and-number question is guidance. A gate
criterion cannot easily distinguish a justified component from a well-argued one.

**Cost scale is unspecified.** "Infrastructure cost" without a required scale permits the
flattering computation, and the check that consumes it in module 13 has no way to know
which scale was used.

**Technology claims decay.** The module requires version-and-date citation, as module 14
does for model claims. Nothing revisits them, so a run reused a year later carries stale
pricing and deprecated versions.

**Blocker and risk are distinguished in prose only.** The distinction is load-bearing —
it decides whether something stops a launch — and it is carried by a word.

**Build-versus-buy has no structure.** Most cost and most operational surface is decided
by what you choose not to build, and the module has no place to record those decisions or
their reasoning.

**No treatment of data migration.** The data model is the most durable artifact in the
product and the module does not ask how it will change. The first schema change on live
data is where most of the pain is.

---

# Candidate Improvements

| Candidate | What it would fix | Cost |
| --- | --- | --- |
| An obligation-to-mechanism table as a required output | The chain's middle link stops depending on prose | Small, and the highest-value change here |
| A structured `regulated_columns` list | Three downstream checks become real | Small |
| Required scale and date on the cost figure | The third arithmetic check becomes trustworthy | Small |
| A `blocker` type distinct from `risk` | Launch-stopping issues stop being softened | Small |
| A build-versus-buy record | The largest cost decisions become inspectable | Moderate |
| A migration section | The durable artifact gets a change plan | Moderate |
| Staleness dates on technology claims | Reused runs stop carrying dead versions | Small, and needs a consumer |

The first two rows together would convert this module's two most important
contributions — the mechanism and the list — from conventions into structure. Everything
else on the page is secondary to that.

---

# What Should Not Change

**The schema test stays the bar.** It is demanding, it is objective, and it catches the
decisions that otherwise get made quickly by one person during build.

**Stack justification stays required to name a downside.** It is the only defense against
a choice nobody compared.

**The cost check stays in this module.** Moving it later would mean discovering an
unaffordable architecture after it exists.

**Failure modes stay enumerated.** They are the sole source of module 13's runbooks, and
a description of error handling produces nothing operable.

**The module stays downstream of specification.** Technical design that starts deciding
what the product does is module 08 happening again, without the trace requirement.

---

> **Improvements Principle**
>
> This module's two most important outputs — the mechanism and the regulated column
> list — are both carried by convention.
>
> Three other modules check against them. Making them structural is the difference
> between four real checks and four that read well.
