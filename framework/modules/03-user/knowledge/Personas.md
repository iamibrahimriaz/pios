---
Title: Personas
Module: 03-user
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define a persona as compressed evidence, and state the prohibition on invention.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 03-user/knowledge/User-Segments.md
Outputs:
  - personas
Related Modules:
  - 08-product
  - 10-execution
Tags:
  - User
  - Personas
  - Concept
---

# Personas

---

# What It Is

A compression of research about one segment into one described person — built so that later modules
can ask "would this person do that?" and get a constraining answer.

A persona is **evidence, compressed.** It is not a character sketch. Every row must be traceable to
a source, and rows that cannot be are recorded as gaps rather than filled in.

> **The test:** could this persona describe anyone in the market?
>
> If yes, it describes no one, and it will not constrain a single product decision.

---

# When It Applies

In Move 3 (Embody), after a segment has been chosen and defended. It is consumed by `08-product` for
requirements and by `10-execution` for flows.

---

# How to Apply It Here

**Tag every row.** `[verified: source]`, `[inferred: basis]`, `[assumption: needs validation]`. A
persona of twelve rows where eight are assumptions is honest and usable. One where all twelve read as
fact is fiction with a photograph.

**Include a gaps section.** What is not known is the most actionable part of the artifact — it tells
`04-problem` exactly what to validate. A persona that appears complete gives the next module nothing
to do and no reason to doubt it.

**Never invent a quote.** This is the most damaging output the module can produce. A fabricated user
voice reads as primary evidence, propagates verbatim into the PRD, and **nobody downstream can tell
it was invented.** If no real voice can be found, write that no primary voice was located — that
sentence is a finding, and a useful one.

**Build a second persona where the buyer differs from the user.** Every later module then carries two
sets of criteria. Discovering this at `06-business` means re-running this module.

**Keep it to what changes decisions.** Name, role, context, tools, constraints, what they are
measured on, what they fear. Hobbies and a stock photo are the parts that make personas mocked, and
deservedly.

---

# Where It Misleads

**A persona is the framework's most convincing vehicle for fabrication.** The format invites
completeness, plausible detail is easy to generate, and the result is indistinguishable from research
after one hand-off. Every other guard in this file exists because of that single property.

**Plausibility is mistaken for evidence.** "Time-poor, skeptical of new software, works late" is true
of almost every professional — which means it constrains nothing. The rows that earn their place are
the surprising ones, and surprising rows are exactly the ones that need a source.

**One persona gets treated as the user.** It represents a segment, and segments contain variation. If
a decision hinges on a row, that row deserves validation rather than deference.

**Personas outlive their evidence.** Written once and quoted for months, they harden while the market
moves. The version and the date of the underlying research belong on the artifact.

---

# Related

| | |
| --- | --- |
| `User-Segments.md` | The group a persona represents |
| `Empathy-Map.md` | A structuring device, with its own limits |
| `Environment.md` | The context a persona operates in |
| `08-product` | Where persona rows become requirements |

---

> **Concept Note**
>
> Tag every row, record the gaps, and invent no quote.
>
> A fabricated user voice is the only error in this framework that
> nobody downstream can detect.
