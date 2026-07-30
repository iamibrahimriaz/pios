---
Title: Mission
Module: 08-product
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Use the mission as a present-tense scope check against what the release actually does.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 01-idea/knowledge/Mission.md
Outputs:
  - One-line reference in prd_body
Related Modules:
  - 01-idea
  - 07-strategy
Tags:
  - Product
  - Mission
  - Concept
---

# Mission

---

# What It Is

What the product does now, for whom, and to what end — inherited from `01-idea`, and useful here in a way the vision is
not.

Because it is **present tense**, it can be checked against the requirement list:

| Check | What it detects |
| --- | --- |
| Does the MUST list deliver what the mission claims? | A mission broader than the release — an implicit promise |
| Does the MUST list do more than the mission describes? | Scope that has grown past the stated purpose |
| Would the mission need rewriting to accommodate this requirement? | A strategy decision arriving as a specification |

The third row is the working test. `01-idea` put it this way: when a capability is proposed, ask whether the mission
would need rewriting to accommodate it. If it would, that is `07-strategy`'s decision — not an addition here.

---

# When It Applies

As a check during Move 2 (Specify), and once as a line in the PRD's inherited section.

---

# How to Apply It Here

**Read the mission against the MUST list, in both directions.** Under-delivery is an implicit promise users will read as
a commitment. Over-delivery is scope laundering with a paper trail.

**Use the rewriting test on borderline requirements.** It is a sharper instrument than asking whether something is in
scope, because it makes the answer checkable against a sentence written before the argument started.

**Do not update the mission to fit the spec.** If the release has outgrown the mission, that is the finding. Editing the
mission to match makes the check circular and removes the only present-tense boundary available.

**Keep it out of the parent column.** Like the vision, it is context. Requirements trace to ranked problems.

**Flag a mission that is now false.** If `07-strategy`'s cut removed a capability the mission describes, the mission has
stopped being true and someone should decide which of the two changes.

---

# Where It Misleads

**Mission and vision get merged, and the merged version is always the vision** — which loses the present tense and with
it the only usable scope check of the two.

**A mission broader than the product is read as a promise.** Users, buyers and builders all take it literally. An
overstated mission generates expectations `13-operations` has to field as support.

**It gets widened one requirement at a time.** Each widening is small and defensible; the sum is a product with no
boundary. Rewriting the mission should be a noticed event.

**Company missions get used in place of product missions.** "We are building the future of clinical software" describes an
organization's ambition and cannot check any requirement against anything.

**The check is skipped because the mission feels like marketing copy.** It is the one inherited sentence that can be
falsified by the requirement list, which makes it the most functional piece of framing this module receives.

---

# Related

| | |
| --- | --- |
| `Vision.md` | The future-tense counterpart, with no role in requirements |
| `Product-Strategy.md` | The binding cut and non-goals |
| `Requirements.md` | The MUST list this is checked against |
| `01-idea` | Where the mission and the rewriting test are defined |

---

> **Concept Note**
>
> Ask whether the mission would need rewriting to fit the
> requirement.
>
> If yes, it is module 07's decision — and editing the mission to
> agree makes the test worthless.
