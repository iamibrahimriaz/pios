---
Title: Empty States
Module: 10-execution
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Design the first experience, and distinguish the four kinds of emptiness.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 10-execution/knowledge/Wireframes.md
Outputs:
  - Empty states within ux_flows
Related Modules:
  - 08-product
  - 11-growth
Tags:
  - Execution
  - UX
  - Concept
---

# Empty States

---

# What It Is

What a screen shows when there is nothing to show — and the framework treats it as the **most important state**, because it is the
first one every user sees.

Four kinds, and they need different answers:

| Kind | What the user needs |
| --- | --- |
| **First use** — nothing exists yet | What this screen is for, and one action to create the first thing |
| **Cleared** — everything is done or archived | Confirmation that this is success, not a fault |
| **No results** — a filter or search matched nothing | Which filter caused it, and how to clear it |
| **Not permitted** — content exists but not for them | Per `09-technology`'s disclosure policy, possibly indistinguishable from the first |

The distinction that matters most: **an empty inbox and a broken inbox look identical** unless the empty state says which it is.

---

# When It Applies

In Move 1 (Flow), as a required state per screen. `08-product` specified the empty category per requirement; this is where it becomes
something a person sees.

---

# How to Apply It Here

**Make the first-use state teach and offer.** One sentence saying what this is for, and the single action that creates the first
record. It is the highest-leverage screen in the product and usually the least designed.

**Count it in time to first value.** `User-Flows.md`'s number runs from arrival. Every empty state between arrival and value is part
of that count.

**Distinguish cleared from broken, explicitly.** "Nothing outstanding" reads as success. A blank area reads as a failure, and users
report it as one.

**Name the filter on a no-results state.** Users forget filters are applied. Showing which one excluded everything, with a way to
remove it, resolves the most common false bug report in any list interface.

**Respect the disclosure policy on the permission case.** `09-technology/knowledge/api/Authorization.md` decided whether absence and
prohibition look the same. The interface must not contradict it.

---

# Where It Misleads

**Empty states are treated as an edge case.** They are the majority experience for a new user and a frequent one thereafter. Calling
them edge cases is how they end up unspecified.

**Sample or seeded data hides them during development.** Every screen looks populated, and the state ships as whatever the framework
renders by default.

**They are used for marketing.** An empty state is not the place for a product tour. It has one job: say what this is and offer the
next step.

**All four kinds get one design.** "No results" advising the user to create their first record, when they have two hundred and a
filter applied, is actively confusing.

**Onboarding is built instead.** A well-designed empty state frequently removes the need for a tour, and `11-growth` cares because
time to first value is an activation number.

---

# Related

| | |
| --- | --- |
| `Loading-States.md` | The state that precedes it |
| `Error-States.md` | The state it must be distinguishable from |
| `Wireframes.md` | Where it is drawn first |
| `08-product`, `11-growth` | The edge category, and activation |

---

> **Concept Note**
>
> An empty inbox and a broken inbox look the same. Say which it is.
>
> First use is the most-seen screen in your product and usually the
> least designed one.
