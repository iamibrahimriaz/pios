---
Title: Reflection
Module: 08-product
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Prompt a learner to examine what they left in their own head.
Audience:
  - Product Managers
  - Founders
  - Researchers
Prerequisites:
  - 08-product/learn/16-Evaluation.md
Outputs:
  - Examined assumptions about your own specification habits
Related Modules:
  - 07-strategy
  - 10-execution
Tags:
  - Product
  - Reflection
  - Learn
---

# Reflection

---

# Overview

Specification failures are failures of imagination about other readers. These questions
are about the gap between what you meant and what you wrote.

---

# On the Document

**What did you assume the reader knows?** List it. Some of it is fair — a builder knows
their craft — and some of it is context that exists only in your conversations.

**Which section did you write fastest?** That one is usually the least specified. Speed
comes from familiarity, and familiarity is what makes you skip the parts you already
know.

**What would you have to explain if you handed this over and left?** Everything on that
list belongs in the document.

---

# On the Requirements

**Which one traces to nothing?** There is almost always one. Naming it is not an
argument for removing it — it is an argument for saying out loud that it is an
exception.

**Which one did you argue hardest for?** Check whether the argument was compensating for
an absent trace.

**Which one is a design preference?** Everyone smuggles at least one interface decision
into a requirement. Finding yours tells you where you stop trusting the next module.

---

# On the Edges

**Which edge category did you skip?** Concurrent and hostile, usually. Both feel like
someone else's job — engineering's, or security's — and both change requirements.

**What is on screen the very first time?** Empty states are the most-used screen in a
new product and the least specified.

**What happens if the user does the thing you told them not to?** Not what should
happen. What does.

---

# On the Cut

**Did specifying it reveal that the MVP was bigger than module 07 thought?** This
happens frequently and it is a legitimate finding.

**What did you do about it?** Reporting back is correct. Quietly writing a larger MVP is
how scope laundering finishes.

**What did you drop without writing it down?** Go and check. There is usually something,
and it is usually the thing that comes back.

---

# On Your Own Pattern

| Look for | What it suggests |
| --- | --- |
| Your specs are strong on the happy path | You specify what you can picture |
| Your criteria contain adjectives | You are writing intent rather than tests |
| You never report a cut back to strategy | Scope pressure resolves through you silently |
| Your requirements include layouts | You do not yet trust module 10 |
| Builders always come back with questions | The document is a summary of a conversation, not a substitute for one |

The last row is the diagnostic one. If the same questions recur across projects, they
identify precisely which decisions you habitually keep in your head.

---

# The Question Worth Returning To

> If you were unavailable for a month, what would get built wrong?

Answer specifically. Each item is a decision you are currently holding rather than
documenting, and the list is usually short, concrete, and fixable in an afternoon.

---

> **Reflection Principle**
>
> You are the worst possible reader of your own specification, because you cannot
> unknow what you meant.
>
> The corrective is not more care. It is another reader.
