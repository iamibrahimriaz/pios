---
Title: AI Comparison
Module: 05-competition
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Compare AI capabilities on what survives commoditization, not on the model used.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 05-competition/knowledge/Technology-Comparison.md
Outputs:
  - AI capability comparison within competitor_matrix
Related Modules:
  - 14-ai-systems
Tags:
  - Competition
  - AI
  - Concept
---

# AI Comparison

---

# What It Is

An assessment of what competitors' AI features actually do for the user — scoped by a single question:

> **If the underlying model became free and available to everyone tomorrow, what would still distinguish them?**

| Survives commoditization | Does not survive |
| --- | --- |
| Proprietary data nobody else can obtain | Which model they call |
| Integration into the system of record | Prompt quality |
| Trust, certification and audit evidence | Being first to ship a wrapper |
| The workflow the output lands in | A better interface for the same output |
| Feedback loops that improve with use | Model size or benchmark scores |
| Autonomy the market has accepted | Marketing that says "AI-powered" |

The left column is the competitive analysis. The right column is what almost every AI comparison table contains.

---

# When It Applies

Alongside Move 3 (Test), where an AI capability affects whether a ranked problem is solved, and in Move 5 where its
durability is tested. It hands directly to `14-ai-systems`.

---

# How to Apply It Here

**Compare outputs, not mechanisms.** What does the user receive, how much correction does it need, and do they act on
it? A competitor using a weaker model with better grounding produces better output, and only the output is visible to
the buyer.

**Record the autonomy level each competitor has shipped.** Suggests, drafts, acts with confirmation, acts
independently. Where competitors have all stopped at "suggests", the market or the regulator may be the reason —
`14-ai-systems` treats detectability as governing autonomy, and this is the market evidence for it.

**Note who has data nobody else can get.** Proprietary data is the one genuinely durable AI advantage, and it is
usually visible: exclusive partnerships, an installed base generating labeled examples, access to a regulated
dataset.

**Check whether the AI is the product or a feature of the workflow.** A capability wrapped in nothing is copied in
weeks. The same capability inside an integrated workflow is protected by the integration, not by the model.

**Look for what they shipped and withdrew.** An AI feature quietly removed is a strong finding — usually about trust,
cost, or accuracy in the real distribution of cases.

---

# Where It Misleads

**Model choice is presented as differentiation and is the least durable property in the table.** Everyone has access
to comparable models, including the incumbent with the distribution. This is `Gap-Analysis.md`'s "nothing stops them"
row in its most common contemporary form.

**Demos are compared instead of behavior at the tail.** AI features perform well on curated cases and degrade on the
messy distribution real work produces. Reviews and support forums describe the tail; marketing never does.

**Absence of an AI feature is read as a gap.** A competitor may have tried it and withdrawn, or concluded the
liability was not worth the benefit. In regulated fields that judgment is a finding, and copying the feature inherits
the reason they stopped.

**"AI-powered" gets recorded as a capability.** It describes nothing. What the user receives, and whether they trust
it enough to act, is the only comparable content.

**First-mover advantage is assumed for AI features.** It is among the weakest advantages available here, because the
capability arrives simultaneously for everyone and the incumbent already has the customers.

---

# Related

| | |
| --- | --- |
| `Threats.md` | Commoditization and platform absorption |
| `Gap-Analysis.md` | Whether an AI advantage can be held |
| `Technology-Comparison.md` | Why the stack is not a position |
| `14-ai-systems` | Where the mechanism is justified or dropped |

---

> **Concept Note**
>
> Ask what would remain if the model were free tomorrow.
>
> Whatever survives that question is the competitive analysis.
> Everything else is a wrapper with a launch date.
