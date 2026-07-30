---
Title: Automation
Module: 07-strategy
Section: knowledge/solutions
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Decide what to automate by the cost of a wrong result, not by what is automatable.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 07-strategy/knowledge/solutions/AI-Opportunities.md
Outputs:
  - Automation scope within chosen_approach
Related Modules:
  - 03-user
  - 14-ai-systems
Tags:
  - Strategy
  - Automation
  - Concept
---

# Automation

---

# What It Is

The decision about which steps the product performs on the user's behalf — governed by what a wrong result costs and
whether anyone would notice.

Most automation in professional products is not AI. Removing re-typing between two systems, pre-filling a form from
data already held, or scheduling something that was manual are deterministic, cheap, auditable, and frequently the
larger win. `03-user`'s journey usually shows the friction sitting in transitions rather than in judgment.

| Step type | Automate to |
| --- | --- |
| Mechanical, verifiable, low consequence | Fully — no confirmation needed |
| Mechanical, high consequence | Automate the work, require confirmation of the result |
| Judgment, detectable if wrong | Suggest, and make the suggestion easy to reject |
| Judgment, undetectable if wrong | Do not automate above suggestion without a visibility mechanism |

The last row is `14-ai-systems`' rule: **detectability governs autonomy, not accuracy.**

---

# When It Applies

In Move 1 (Diverge) and Move 3 (Choose) — automation scope is part of what distinguishes options, since it changes the
first build.

---

# How to Apply It Here

**Automate the transitions first.** `03-user`'s journey names the copying, re-typing and waiting between steps. These
are the cheapest wins in the framework and they require no model.

**Ask what a wrong result costs, and who finds out.** Those two answers set the autonomy ceiling for that step. A
cheap and visible error tolerates full automation; an expensive invisible one does not, at any accuracy.

**Leave the human where the accountability sits.** In regulated work, someone signs. Automation that removes the
review without removing the accountability creates exposure — for the user, which means for the product.

**Check the immovables.** `03-user` recorded what will not change. Automation requiring an immovable to move does not
get adopted, however good it is.

**Keep the manual path.** Users need a way to do it themselves when the automation is wrong or the case is unusual.
`08-product`'s edge categories will require it anyway.

---

# Where It Misleads

**Automatable is confused with worth automating.** The question is not what can be done without the user, but which
steps cost them something and can be removed safely. `04-problem`'s ranking answers the first half.

**Time saved is treated as the only benefit and review time is not subtracted.** Automation producing output that must
be carefully checked has moved the work rather than removed it. `06-business`'s capture share and `12-metrics`'
counter-metrics both exist for this.

**Full automation is treated as the goal state.** For judgment work with undetectable errors it is not a later phase —
it is the wrong destination. Autonomy is bounded by consequence, not by maturity.

**Automation removes the step where the user was thinking.** A clinician re-reading notes while typing them is
reviewing the consultation. Removing the typing removes the review, and nobody asked for that.

**Trust is assumed to arrive with accuracy.** Professional users grant autonomy gradually and withdraw it instantly
after one bad outcome. `11-growth` and `13-operations` both live with the consequence.

---

# Related

| | |
| --- | --- |
| `AI-Opportunities.md` | Where a model may be needed |
| `03-user` | The journey, the transitions and the immovables |
| `08-product` | Where the manual path becomes a requirement |
| `14-ai-systems` | Where detectability bounds autonomy |

---

> **Concept Note**
>
> Ask what a wrong result costs and whether anyone would notice.
>
> Those two answers set the ceiling — and no amount of accuracy raises
> it when the error is invisible.
