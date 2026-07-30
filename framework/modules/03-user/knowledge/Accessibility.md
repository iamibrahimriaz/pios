---
Title: Accessibility
Module: 03-user
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Treat accessibility as a user fact with legal force, established here rather than retrofitted.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 03-user/knowledge/Environment.md
Outputs:
  - Accessibility constraints within personas
Related Modules:
  - 08-product
  - 09-technology
  - 10-execution
Tags:
  - User
  - Accessibility
  - Concept
---

# Accessibility

---

# What It Is

The requirement that the product be usable by people whose abilities, conditions of use, or equipment
differ from the assumed default.

Two things make it this module's business rather than a later refinement:

| | |
| --- | --- |
| **It is a fact about the users** | Permanent, temporary and situational limitations are attributes of the segment, and this is the module that establishes attributes of the segment |
| **It is frequently a legal obligation** | In public-sector and many regulated markets, a named standard applies and procurement checks it. `02-market` Frame 2 may already have found it |

| Kind | Example |
| --- | --- |
| **Permanent** | Low vision, no hearing, one hand |
| **Temporary** | An injury, an eye infection, medication effects |
| **Situational** | Gloves on, patient present, noisy ward, bright sunlight, one hand holding a phone |

The situational row is the one that applies to nearly every user of a professional tool, and it is the
one most often omitted.

---

# When It Applies

In Move 3 (Embody) as persona attributes, and in Move 4 (Observe) wherever conditions of use constrain
a step. It becomes requirements in `08-product` and flow constraints in `10-execution`.

---

# How to Apply It Here

**Check whether a standard is legally binding for this segment.** If `02-market` found one, name it
here with the obligation attached — a standard named in `08-product` without a specific requirement
becomes a line nobody implements.

**Record situational constraints as first-class.** Gloves, sunlight, one free hand, a screen visible to
a patient. These come straight out of `Environment.md` and they change interaction design more than any
compliance checklist.

**State the input methods that must work.** Keyboard only, voice, screen reader, touch with imprecise
targets. This is what `10-execution` can actually design against.

**Say what is unknown.** If no accessibility need has been researched for this segment, record that as
a gap rather than as an absence. They are different findings and only one of them is honest.

**Note where accessibility and the AI mechanism interact.** Voice input assumes clear speech and a quiet
room; both are assumptions about ability and environment, and `14-ai-systems` must be told.

---

# Where It Misleads

**It is treated as a late-stage audit.** Retrofitting accessibility into a built interface is expensive
and partial; establishing it as a user fact here makes it a requirement rather than a remediation. The
cost difference is the whole argument.

**Conformance to a standard is mistaken for usability.** A product can satisfy every checkpoint and
still be unusable one-handed in a noisy room. The standard is a floor, and the situational constraints
are the actual test.

**The default user is assumed and never stated.** Every product implicitly assumes an ability profile.
Writing it down is what makes the exclusions visible — and some of them may be a large share of the
segment.

**It gets scoped out of the MVP quietly.** That is a `07-strategy` decision with a legal dimension in
regulated markets, and it belongs in the deferral ledger with the obligation named, not omitted from
the requirements list.

---

# Related

| | |
| --- | --- |
| `Environment.md` | Where situational constraints originate |
| `Personas.md` | Where ability profiles are recorded |
| `02-market` | Where a binding standard may already be identified |
| `08-product`, `10-execution` | Where this becomes requirements and flows |

---

> **Concept Note**
>
> Every product assumes an ability profile. Write yours down.
>
> The exclusions only become visible once the assumed default is on
> the page.
