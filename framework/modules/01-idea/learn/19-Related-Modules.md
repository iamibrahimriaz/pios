---
Title: Related Modules
Module: 01-idea
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Show a learner how the Idea module connects to the rest of the framework, and what each downstream module inherits from it.
Audience:
  - Product Managers
  - Founders
  - Researchers
Prerequisites:
  - 01-idea/README.md
Outputs:
  - Understanding of the idea stage's position in the chain
Related Modules:
  - 02-market
  - 03-user
  - 06-business
Tags:
  - Idea
  - Relationships
  - Learn
---

# Related Modules

---

# Overview

The Idea module depends on nothing. It is the only module in the framework with an
empty `depends_on`, which means every error it makes is original — none of them were
inherited.

It is also the module whose outputs travel furthest. Four of its products are still
being consulted at module 13.

---

# What It Sends Forward

| Output | Who consumes it | What they do with it |
| --- | --- | --- |
| `idea_brief` | `02-market`, `03-user` | The premise everything else is checked against |
| `scope_boundaries` | `02-market`, `07-strategy` | Where the market stops; where the MVP cut can fall |
| `initial_assumptions` | `04-problem` | The starting inventory for the validation plan |
| `clarifying_questions` | The operator | The record of what was asked and what was deferred |

The second row is the one learners underestimate. A scope boundary set casually at the
idea stage is still constraining the roadmap six modules later, usually without anyone
remembering it was set here.

---

# The Immediate Neighbors

**`02-market`** takes the boundary and tries to size it. Its gate — "market defined by
boundary, not by adjective" — is written against this module's most common failure,
and when it fails, the engine returns here. That return path is the framework's
statement that a market cannot be sized around an idea that was never bounded.

**`03-user`** takes the brief and asks who is actually served. This is where the
buyer/user distinction made here first does real work: module 03 produces segments,
and a brief that conflated the two produces segments describing the wrong person.

---

# Where the Idea Stage Reappears Later

| Module | How it reappears |
| --- | --- |
| `04-problem` | Every untagged assumption from here arrives as an unexamined premise; every tagged one arrives as validation work |
| `06-business` | The payer question. If it was not asked here, it is answered by default here |
| `07-strategy` | The chosen approach is checked against the ranked problems — but the non-goals it starts from are this module's scope boundaries, matured |
| `12-metrics` | The north star metric has to express the premise. A vague premise produces a metric that measures activity |

Module 12 is the most surprising of these. A north star metric is downstream of
almost everything, and yet the most common reason one is unusable is that the original
premise never said what success would look like in the user's life.

---

# What It Deliberately Does Not Do

| It does not | Because |
| --- | --- |
| Judge the idea | No evidence exists yet; a verdict here would be preference |
| Size anything | That is `02-market`, and it needs a boundary this module supplies |
| Identify problems | That is `04-problem`, and it needs users this module has not met |
| Propose solutions | That is `07-strategy`, after three modules of evidence |

The discipline of *not* doing these is the module's main contribution. A run that
arrives at module 07 with a solution already chosen at module 01 has performed six
modules of research to justify a decision that was made before any of it began.

---

# The Chain, in One Line

```
idea → market → users → problems → competition → business
     → strategy → product → technology → execution
     → growth → metrics → operations → ai
```

Each arrow is a dependency, and each has a return path when the gate fails. The Idea
module has no return path — its `on_fail` is to halt and ask the operator, because
there is nowhere upstream to go.

That is worth sitting with. It is the only place in the framework where the correct
response to insufficient information is to stop and ask a human.

---

> **Relationships Principle**
>
> This module inherits nothing and is inherited by everything.
>
> Its errors do not get corrected downstream — they get built on, because every module
> after it assumes the premise was stated accurately.
