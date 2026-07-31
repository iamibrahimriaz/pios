---
Title: Learning Objectives
Module: 14-ai-systems
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define what a learner should know and be able to do after the AI Systems module.
Audience:
  - Product Managers
  - Founders
  - Engineers
Prerequisites:
  - 14-ai-systems/learn/01-Why-It-Matters.md
Outputs:
  - AI capability assessment competencies
Related Modules:
  - 08-product
  - 09-technology
Tags:
  - AI
  - Objectives
  - Learn
---

# Learning Objectives

---

# Overview

> After this module you should be able to argue honestly for the alternative to your own
> proposal, say whether a user could detect a wrong output, and set a bar that can fail.

---

# Knowledge Objectives

You should understand:

- The **advocate check**, and why a straw man alternative proves nothing
- The **wrongness cost**: what it costs, who bears it, and whether it is detectable
- Why **detectability governs autonomy** rather than accuracy
- Why data availability is a blocker rather than a risk
- What a golden set is, why it is stratified, and why it is never tuned against
- Why data rights are a legal question, not a technical one
- What **capability theater** looks like

---

# Thinking Objectives

The shift is from *where can we use AI* to *what would have to be true for this to beat
the simpler thing*.

Instead of asking:

> "Where can AI improve this product?"

ask:

- Which ranked problem does this capability address?
- What is the simplest thing that would also address it, and what is its best argument?
- If this is wrong, who pays, and would they know?
- Does the data exist today — confirmed, not projected?
- What is the bar, and what happens if we miss it?

---

# Skill Objectives

You should be able to:

- Propose capabilities generously and eliminate them rigorously
- State an alternative's case as its advocate would
- Compute the wrongness cost and answer the detectability question honestly
- Confirm data availability, quality and rights separately
- Build a stratified golden set that includes the hard cases
- Write failure modes with specific detection and guardrails
- Compute the cost ratio and forward it to modules 09 and 13
- Record a rejection as a rejection so it stops being re-proposed

---

# Analytical Objectives

You should develop the ability to:

- Notice an alternative described in terms its advocate would not use
- Recognize a benchmark score presented as evidence about your task
- Tell projected data from confirmed data
- Spot an evaluation designed on demonstrable cases rather than hard ones

---

# Judgment Objectives

**Where the autonomy ceiling sits.** Determined by detectability and by who bears the
cost, not by the accuracy you expect to reach. Getting this backwards is the most
consequential error available in this module.

**When to keep something as a triggered candidate.** A capability that loses today because
data does not exist may win later. That is a different disposition from a rejection, and
conflating the two either loses a good idea or resurrects a dead one every quarter.

---

# You Have Learned This When

| Signal | What it indicates |
| --- | --- |
| You can argue the alternative better than its opponents | The advocate check is genuine |
| Your first question is who bears a wrong output | The wrongness cost is habitual |
| You set an autonomy ceiling for a reason other than accuracy | Detectability is understood |
| "Zero data exists" reads as a blocker | The distinction is live |
| You are comfortable proposing three and shipping none | The module's purpose is understood |

---

# What This Module Does Not Teach You

It does not teach model training or prompt engineering. It does not choose the
architecture; module 09 did. It does not specify the product; module 08 did, and a
capability with no requirement is an orphan by that module's definition.

---

> **Objectives Principle**
>
> The skill is arguing sincerely for the thing you did not propose.
>
> Everything else here — the data checks, the bar, the failure modes — follows from
> taking that argument seriously enough to lose it.
