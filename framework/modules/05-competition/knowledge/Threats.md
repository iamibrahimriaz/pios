---
Title: Threats
Module: 05-competition
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Anticipate how the field responds if this works, and what would make it irrelevant.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 05-competition/knowledge/Gap-Analysis.md
Outputs:
  - Threat assessment within gap_analysis
Related Modules:
  - 07-strategy
  - 14-ai-systems
Tags:
  - Competition
  - Threats
  - Concept
---

# Threats

---

# What It Is

What happens **if this succeeds** — the response, and the developments that would make the product unnecessary.

Competitive analysis usually stops at the current field. This asks about the field two years out, under the
assumption that the idea worked, because success is what provokes a response.

| Threat | Likelihood driver |
| --- | --- |
| **An incumbent ships it** | How much it conflicts with their model — `Gap-Analysis.md` answered this |
| **A platform absorbs it** | Whether the capability is a natural feature of a system users already have |
| **The enabling technology becomes free** | Whether the value is the mechanism or the workflow around it |
| **A well-funded entrant with distribution** | How visible and attractive the segment becomes |
| **Regulation closes the mechanism** | `02-market` Frame 2's direction of travel |
| **The problem disappears** | Whether a process change or a payment change would remove it |

---

# When It Applies

Alongside Move 5 (Locate). The output belongs in the risk register, and `07-strategy` weighs it when sequencing.

---

# How to Apply It Here

**Assume success, then reason.** The useful question is not whether someone will notice, but what the most likely
response is and how much time exists before it. A named response with a rough timeline is actionable; a general
worry is not.

**Take the platform threat seriously for AI features.** If the capability is a plausible built-in feature of a system
the user already pays for, the product is competing with something that will be free and pre-installed.
`14-ai-systems` costs the mechanism; this assesses whether owning it is a business.

**Ask whether the value survives the mechanism becoming free.** If a model that costs money today is commodity
tomorrow, what remains? Workflow, data, integration and trust survive. A wrapper around a capability does not.

**Include the benign threat.** A process reform, a change in how the work is paid for, or a regulator mandating a
different approach can remove the problem entirely. That is the honest tail risk in institutional markets.

**Say what the response would cost this product.** A threat that forces a price cut, a repositioning, or a segment
change is different from one that ends it. `07-strategy` needs the consequence, not just the event.

---

# Where It Misleads

**Threats get listed and never weighted**, which is the same defect `02-market`'s SWOT file identifies: an
existential threat and a minor competitive response occupy equal space. Attach likelihood and consequence or the
list changes nothing.

**The most likely response is under-imagined.** It is rarely a competitor building a better version; it is a
competitor shipping an adequate version to customers they already have. Adequate plus installed beats better plus
unknown.

**"They're too big to move fast" is a comfortable and unreliable assumption.** Large suppliers ship adequate copies
routinely, and adequate is sufficient when the distribution is already theirs.

**Commoditization of the mechanism is treated as a distant concern.** For AI-based products it is the central one,
and it has repeatedly arrived faster than planned for.

**Threat analysis becomes a reason to build more.** Anticipating a response can justify any amount of scope. The
correct output is a risk with a timeline, handed to `07-strategy` — not a wider MVP.

---

# Related

| | |
| --- | --- |
| `Gap-Analysis.md` | Whether the incumbent can respond |
| `Weaknesses.md` | Where neglect could reverse |
| `AI-Comparison.md` | Whether the mechanism is the value |
| `02-market` | Trends, including the one that argues against |

---

> **Concept Note**
>
> Assume it worked, then ask what happens next.
>
> The likely response is not a better product — it is an adequate one,
> shipped to customers a competitor already has.
