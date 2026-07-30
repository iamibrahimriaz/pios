---
Title: LLM
Module: 14-ai-systems
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Match language-model capabilities to the tasks they suit, and know their characteristic failures.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 14-ai-systems/knowledge/AI-Use-Cases.md
Outputs:
  - LLM capabilities within model_strategy
Related Modules:
  - 06-business
  - 09-technology
Tags:
  - AI
  - LLM
  - Concept
---

# LLM

---

# What It Is

A large language model — the capability class most often proposed and the one whose failures are hardest to detect.

| Suits | Does not suit |
| --- | --- |
| Unstructured text becoming structured | Arithmetic and calculation |
| Long text becoming shorter, with judgment about salience | Anything requiring a guaranteed answer |
| Rewriting between registers or formats | Retrieval of fact from its own memory |
| Classification where categories resist enumeration | Deterministic rules that could be coded |
| Drafting where a human edits | Actions with undetectable, costly errors |

The characteristic failures, all of which `AI-Risks.md` requires stated specifically:

| Failure | Why it matters here |
| --- | --- |
| Fluent invention | The error reads exactly like the correct answer |
| Silent partial output | Missing content looks like absent input |
| Instruction drift on long inputs | Constraints stated once get lost |
| Sensitivity to phrasing | Two equivalent inputs produce different structure |
| Variability across versions | A provider update changes behavior with no change of yours |

---

# When It Applies

In Move 2 (Compare) as a candidate mechanism, and in Move 6 as part of `model_strategy`.

---

# How to Apply It Here

**Ground it rather than relying on recall.** Retrieved context with citations is more accurate and — more importantly — **checkable**, which
is what `Automation.md` says governs autonomy.

**Never use it for arithmetic.** Compute the number in code and let the model describe it. This is the single most common misapplication and
the easiest to avoid.

**Validate the output structurally.** Parse it, check the fields, reject what fails. `Prompt-Engineering.md`'s point: an instruction to produce
a shape is not a schema.

**Price it per operation and compute the share of revenue.** The cost ratio — cost per operation × operations per user ÷ revenue per user —
goes to `09-technology` and `13-operations` as a line in the cost to serve.

**Check the inputs against `09-technology` §3's regulated columns.** Sending a regulated field to a model provider is the same class of
exposure as putting one in an analytics event property.

---

# Where It Misleads

**It is proposed for tasks a rule would solve.** Deterministic, enumerable logic is cheaper, faster, auditable and always right. `AI-Use-Cases.md`'s
comparison exists to catch this.

**Confidence is read from fluency.** The model's tone is identical whether it is right or wrong, which is the plausibility problem and the reason
detectability outranks accuracy.

**Latency is discovered after the interaction is designed.** `09-technology/knowledge/Performance.md` sets the budget from the user's available
time, and inference frequently exceeds it — which is a mechanism decision, not something to tune.

**Cost is assumed to fall faster than usage rises.** It has fallen, and engagement rises too. `06-business/knowledge/pricing/Freemium.md` notes
this makes free tiers structurally hard for AI products.

**Provider terms are assumed acceptable.** Retention, training use and sub-processing all matter to a regulated buyer, and they are contractual
rather than technical questions.

---

# Related

| | |
| --- | --- |
| `Prompt-Engineering.md` | The instruction, and its limits |
| `AI-Risks.md` | Fluent invention and silent partial output |
| `Evaluation.md` | The golden set and per-instance guarantees |
| `09-technology`, `06-business` | Regulated inputs, latency and cost |

---

> **Concept Note**
>
> Ground it, validate the shape, and never let it do arithmetic.
>
> Its wrong answers sound exactly like its right ones — which is the
> whole reason autonomy is bounded by detectability.
