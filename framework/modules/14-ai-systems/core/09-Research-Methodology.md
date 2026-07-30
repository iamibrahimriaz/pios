---
Title: Research Methodology
Module: 14-ai-systems
Section: core
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define how claims about model capability, data and quality are sourced and bounded.
Audience:
  - AI Agents
Prerequisites:
  - engine/evidence-policy.md
  - 14-ai-systems/core/06-Framework.md
Outputs:
  - Honestly bounded AI plan
Related Modules:
  - 12-metrics
  - 13-operations
Tags:
  - AI Systems
  - Methodology
  - Evidence
---

# Research Methodology

---

# The Hardest Evidence Problem in the Framework

This module makes claims about how well something will work on inputs it has never seen. There is no
honest way to know that in advance, and three habits make it worse:

| Habit | Why it misleads |
| --- | --- |
| Citing a benchmark | Measured on a public dataset that is not this product's inputs |
| Citing a demo | One curated example, chosen because it worked |
| Citing general capability | "Models are good at summarization" is not a claim about this data |

> Nothing establishes how a model performs on this product's inputs except running it on this
> product's inputs.

So every quality expectation is `[assumption: needs validation]` until measured on real cases, and
the module's job is not to predict quality but to **define the bar and the method that will settle
it**.

---

# Four Kinds of Statement

| Kind | Example | Label |
| --- | --- | --- |
| **Derived** | "This capability serves R4, which requires filtering by clinician" | `derived: R4` |
| **Documented** | "«Model» supports «context length» as of «version», «date»" | `[verified: source, date]` |
| **Judgment** | "Suggests, not acts — the user cannot detect a wrong code" | `judgment`, with the reasoning |
| **Expectation** | "≈90% accuracy on extraction" | `[assumption: needs validation]` |

The dangerous class is an expectation written as documented. "The model handles this well" reads as a
capability claim, is actually a recollection about other people's data, and is acted on immediately.

---

# Version-Scoped Claims, Again

`09-technology` established that version-specific claims are the most reliably wrong statements in
technical writing. Model claims are the same category with a faster clock:

| Claim | Must cite |
| --- | --- |
| Context length, modality support, tool support | The provider's docs, with the model version and a date |
| Price per operation | The published price page, with the date |
| Rate limits and quotas | The provider's limits, with the tier |
| Deprecation timeline | The provider's announcement |

**Pin the version.** A capability designed against an unpinned model is a capability whose behavior
changes without a deployment, and whose evaluation results expire silently.

---

# The Comparison Must Be Honest, Not Balanced

Move 2's non-AI alternative is a claim about what would happen if you built something simpler. It
cannot be verified, but it can be made in good faith — and the test for good faith is mechanical:

> **The advocate check.** Can a competent person argue for the alternative in one honest sentence?

| Straw man | Honest alternative |
| --- | --- |
| "The user could memorize all 70,000 codes" | "A search box ordered by this clinician's own 40 most-used codes" |
| "Someone could read every document manually" | "Require the sender to submit structured data, which most already have" |
| "We could hard-code every rule" | "The eight rules that cover 90% of cases, and a manual path for the rest" |

A straw man does not merely weaken the analysis. It **invalidates** it, because the module's single
gate criterion is that the comparison happened.

---

# Data Availability Is Confirmed, Not Projected

| Claim | Acceptable form |
| --- | --- |
| "We have historical consultations to ground on" | `[verified: «n» records exist in «source», sampled «date»]` |
| "The operator has this data" | `[verified: operator]`, having actually asked |
| "This data will exist after launch" | Not availability. This is a cold-start problem |
| "Public data covers this domain" | `[verified: source]`, with the license checked |

**An unconfirmed data need is a blocker, not a risk.** A capability resting on data nobody has looked
for cannot be estimated, scheduled or built — and it will be discovered in the first week of
implementation, which is the most expensive place to discover it.

---

# Data Rights Are Legal Claims

The framework has been consistent about this class of statement since `09-technology`: a regulatory
claim cites the regulation, and no document here may assert compliance.

| Never | Instead |
| --- | --- |
| "We can use patient data for this" | The regime, the basis, and the citation |
| "Consent covers it" | Which consent, obtained how, covering which use |
| "The provider is compliant, so we are" | A compliant provider is a precondition, never a conclusion |
| "The data is anonymized" | The method, and whether it survives the regime's definition |

**The mechanical check.** Take the regulated and PII column list from `09-technology` §3 and check it
against every model input. This is the fourth place the framework runs that check:

| Module | Checks the same list against |
| --- | --- |
| `09-technology` | Obligations, mechanisms, enforcement points |
| `12-metrics` | Event properties |
| `13-operations` | The review schedule |
| **`14-ai-systems`** | **Model inputs** |

---

# Evaluation Must Be Designed Before It Is Convenient

A bar set after seeing outputs is not a bar; it is a description of what happened.

| Requirement | Why |
| --- | --- |
| The bar precedes the build | Otherwise the result defines the standard |
| The golden set is built from real cases | Synthetic cases measure fluency, not correctness |
| The golden set is never used for tuning | Otherwise it measures fit to itself |
| The sample size is stated | Three examples is an anecdote |
| The judge is qualified | The build team cannot assess domain correctness |
| The ship gate is explicit | Otherwise it ships |

**On who judges.** This is the same principle `03-user` applies when it forbids inventing user
quotes: confidence in an output is not evidence about it. A developer who finds a generated clinical
summary convincing has established that it is convincing, which is precisely the property that makes
a wrong one dangerous.

---

# The Plausibility Problem Is an Evidence Problem

> A model's errors are fluent. They arrive in the same register as its correct answers.

This is the framework's own central prohibition, occurring inside the product rather than inside the
document:

| Framework rule | Model behavior |
| --- | --- |
| "An assumption must never be smoothed into a fact" | A model does this by default, in every sentence |

Which is why this module weights **detectability** above accuracy, and why per-instance guarantees —
always labeled, always dismissible, always bounded, always cited — carry more real safety than any
accuracy figure. Those hold on every output. An accuracy figure holds on average, and users
experience instances.

---

# The Prohibitions

| Never | Why |
| --- | --- |
| Cite a benchmark as evidence for this product's quality | Different data, different task, different definitions |
| Cite a demo | One curated example, selected for success |
| State a quality expectation as documented | It is an expectation about unseen inputs |
| Make a version claim without a version and a date | The most reliably wrong class of statement |
| Design against an unpinned model | Behavior changes without a deployment |
| Write a straw-man alternative | It invalidates the gate criterion |
| Report projected data as available | The failure arrives in implementation week one |
| Assert a data right | Cite the regime and the basis |
| Send a regulated field to a provider | The same exposure as an analytics event property |
| Let the build team judge domain quality | Convincing is not correct |
| Tune against the golden set | It measures fit to itself |
| Set the bar after seeing results | The result becomes the standard |
| Offer a better prompt as a guardrail | A prompt is not a control |
| Treat the non-AI fallback as a contingency | It is scope, and it belongs in `08-product` |

---

# Cross-Checks Before the Gate

| Check | Against | Fails when |
| --- | --- | --- |
| Requirement trace | `08-product` §7 | A capability serves no requirement |
| Regulated inputs | `09-technology` §3 | A protected field is a model input |
| Placement | `09-technology` §8 | The capability implies architecture that does not exist |
| Cost | `06-business`, `09-technology` §12 | The share of revenue is unacceptable, or the line is missing |
| Latency | `10-execution` §4 | The capability is slower than its step allows |
| Autonomy | `03-user` | The level exceeds the persona's real error tolerance |
| Disclosure | `02-market` | A disclosure obligation is unmet |
| Fallback | `08-product` | The non-AI path is not a requirement |

---

# Self Assessment

- Is every quality expectation tagged as an assumption?
- Did I cite a benchmark or a demo as evidence?
- Is every model claim version-pinned and dated?
- Could someone argue for each of my non-AI alternatives?
- Is any data need projected rather than confirmed?
- Does every data-rights claim cite a regime?
- Does any model input carry a protected field?
- Is the judge qualified to judge?
- Was the bar set before the build?
- Did I offer a prompt as a guardrail?

---

> **Methodology Principle**
>
> This module cannot know how well the model will work.
>
> Its integrity lies in saying so, and in defining exactly what
> would settle the question before anyone depends on the answer.
