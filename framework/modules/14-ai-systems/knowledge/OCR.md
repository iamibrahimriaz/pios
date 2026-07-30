---
Title: OCR
Module: 14-ai-systems
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Handle document extraction, whose characteristic failure is silent partial output.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 14-ai-systems/knowledge/AI-Use-Cases.md
Outputs:
  - Extraction capabilities within model_strategy
Related Modules:
  - 08-product
  - 09-technology
Tags:
  - AI
  - OCR
  - Concept
---

# OCR

---

# What It Is

Extracting text and structured data from documents and images.

Accuracy varies enormously by input, and the variation is predictable:

| Input | Typical reliability |
| --- | --- |
| Digitally generated PDF with a text layer | Near perfect — and no model is needed; extract the text layer |
| Clean scan of a printed form | High |
| Photograph of a printed document | Moderate — lighting, angle and focus dominate |
| Handwriting | Low and highly variable |
| Tables and multi-column layouts | Poor structure recovery even where the characters are right |

**The characteristic failure is silent partial extraction:** fields that were missed look identical to fields the sender left blank. The
user cannot distinguish the two, which puts this squarely in `Automation.md`'s undetectable-error category.

And the alternative `AI-Use-Cases.md` requires considering: **a better upload format, or asking the sender for structured data.** For a
recurring correspondent, that frequently wins outright.

---

# When It Applies

In Move 2 (Compare) as a candidate, and in Move 4 where its undetectability constrains autonomy.

---

# How to Apply It Here

**Check for a text layer first.** A digitally generated PDF needs no model, and a large share of documents in professional workflows are
digitally generated.

**Pursue the structured-source alternative seriously.** Asking a regular sender to provide data rather than a document removes the capability
entirely — which `AI-Use-Cases.md` counts as success.

**Distinguish "not found" from "empty" in the output.** This is the guardrail for the silent-partial failure, and it is a per-instance
requirement rather than an accuracy improvement.

**Require review of extracted values before they are relied on.** Given the detectability problem, autonomy above "drafts" needs a visibility
mechanism — showing the source region alongside each extracted value is the usual one.

**Specify the unreadable-input path.** `08-product`'s failure category applies: what the user sees and does when extraction fails or is
partial.

---

# Where It Misleads

**Benchmark accuracy is assumed to transfer.** Published figures come from clean datasets. Real inputs are photographed at an angle, in poor
light, of a document that was already a photocopy.

**Handwriting is treated as a solved problem.** It is not, and in clinical and legal contexts the consequences of a misread value are
significant.

**Structure is assumed to survive.** Characters can be correct while the table layout is wrong, which produces values assigned to the wrong
fields — a worse outcome than a failed extraction.

**Confidence scores are trusted as calibrated.** They are a signal and not a probability. Treating a high score as verification reintroduces
the undetectability problem.

**Regulated content is sent to a third-party service without assessment.** Documents in professional workflows are frequently the most
sensitive data in the product, and `09-technology`'s obligations apply to the extraction path.

---

# Related

| | |
| --- | --- |
| `Automation.md` | Why undetectable errors cap autonomy |
| `AI-Risks.md` | Silent partial output as a named failure |
| `08-product` | The unreadable-input edge case |
| `09-technology` | Regulated documents and residency |

---

> **Concept Note**
>
> A missed field looks exactly like an empty one — that is the whole
> risk.
>
> Check for a text layer, and ask whether the sender could just send you
> the data.
