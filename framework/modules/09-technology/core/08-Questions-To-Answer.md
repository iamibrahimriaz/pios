---
Title: Questions To Answer
Module: 09-technology
Section: core
Category: Inquiry
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: The complete question set this module must answer before its gate can pass.
Audience:
  - AI Agents
  - Engineers
Prerequisites:
  - 09-technology/core/06-Framework.md
Outputs:
  - Answered question set
Related Modules:
  - 10-execution
  - 13-operations
Tags:
  - Technology
  - Questions
---

# Questions To Answer

---

# Overview

This is the longest question set in the framework, because it is the last one before code.

Every question here is one a builder would otherwise answer alone, with none of the research
behind it. The test of whether a question belongs is simple: if two competent engineers could
answer it differently and both proceed, it belongs here.

Questions marked **OPERATOR** or **NEEDS LOOKUP** cannot be answered by inference. They go to
`state.open_questions`.

---

# 1. Inherited Constraints

| # | Question | If unanswered |
| --- | --- | --- |
| 1.1 | What are the MUST requirements? | The design has no scope |
| 1.2 | What edge cases did module 08 specify? | Failure responses will be invented |
| 1.3 | Which regulatory regimes apply? | Obligations discovered after the design is fixed |
| 1.4 | What is the cost-to-serve ceiling? | The design may break the business model |
| 1.5 | What are the launch and target user figures? | Sizing has no basis |
| 1.6 | What is the user's real operating environment? | Built for conditions that do not exist |
| 1.7 | What is the first shippable slice? | The design may not have a buildable first piece |
| 1.8 | Is any requirement unmeetable inside these constraints? | A regress goes unrecorded |

---

# 2. Deriving

| # | Question | If unanswered |
| --- | --- | --- |
| 2.1 | What things does the product act on? | No entity inventory |
| 2.2 | What is done to each of them? | No operation inventory |
| 2.3 | Which of them have a lifecycle? | State machines missing |
| 2.4 | **Does any entity match no requirement?** | Speculative modeling |
| 2.5 | **Does any requirement's data appear nowhere?** | The model has a hole, or module 08 was vague |
| 2.6 | For each such requirement, is its data genuinely implicit? | Invention gets mistaken for derivation |
| 2.7 | What is the central entity everything hangs off? | The model has no shape |

---

# 3. Data Model

| # | Question | If unanswered |
| --- | --- | --- |
| 3.1 | For every column: type, nullability, default? | Not schema-generatable |
| 3.2 | For every relationship: cardinality? | 1:N versus N:M is a different product |
| 3.3 | For every foreign key: on-delete behavior? | A business rule left to a default |
| 3.4 | Which business rules can be expressed as constraints? | Rules enforced only by memory |
| 3.5 | For every index: which query does it serve? | Indexes guessed |
| 3.6 | Which columns contain PII? | Privacy controls cannot be targeted |
| 3.7 | Which entities hold regulated data, and under what regime? | Compliance scope unknown |
| 3.8 | What is the retention period per entity, and on what basis? | Retention invented — a legal exposure |
| 3.9 | Which entities require an audit trail? | Audit added later, incompletely |
| 3.10 | Is deletion hard or soft, and what happens to related records? | Deletion behavior improvised |
| 3.11 | How are timestamps and timezones handled? | The most common source of silent data defects |
| 3.12 | Where does history need to be preserved rather than overwritten? | Past state lost irrecoverably |

---

# 4. State Machines

| # | Question | If unanswered |
| --- | --- | --- |
| 4.1 | What are the legal states? | Status is a free-text field |
| 4.2 | What are the legal transitions, and what triggers each? | Any state reaches any other |
| 4.3 | **What transitions are forbidden?** | Where the bugs live |
| 4.4 | What happens if a forbidden transition is attempted? | Undefined behavior |
| 4.5 | Who may cause each transition? | Authorization gap |
| 4.6 | What else changes as a side effect of each transition? | Side effects discovered in production |
| 4.7 | What is editable in each state? | A product rule, not an implementation detail |

---

# 5. Interface

| # | Question | If unanswered |
| --- | --- | --- |
| 5.1 | What is the interface style, and why? | Chosen by whoever starts first |
| 5.2 | For each operation: request and response shape, concretely? | Descriptions are not contracts |
| 5.3 | For each writable field: validation rule, traced to a requirement? | Validation invented |
| 5.4 | **Is every MUST requirement reachable?** | Gaps surface mid-build |
| 5.5 | **Does every operation serve a requirement?** | Speculative surface area |
| 5.6 | Does every edge case from module 08 map to a failure response? | Specified then dropped |
| 5.7 | Is each write operation idempotent — and if not, why is that safe? | Retries produce duplicates |
| 5.8 | Is the error shape consistent across the whole interface? | Clients handle errors ad hoc |
| 5.9 | 404 or 403 for records the caller may not see? | Existence disclosure |
| 5.10 | How is the interface versioned? | Breaking changes with no path |
| 5.11 | Pagination, filtering and sorting conventions? | Three conventions in one API |
| 5.12 | Rate limits, and the response when exceeded? | No protection, no client guidance |

---

# 6. Security

| # | Question | If unanswered |
| --- | --- | --- |
| 6.1 | How are users authenticated? | Undefined |
| 6.2 | Is authorization role-level, record-level, or both? | The most common serious gap |
| 6.3 | **Where is authorization enforced?** | Described but not located, which is the same as absent |
| 6.4 | **For each regulatory obligation: which mechanism meets it, and where?** | Compliance is an intention |
| 6.5 | Is any obligation unmet by any mechanism? | A blocker recorded as prose |
| 6.6 | What is encrypted at rest, at what granularity, with keys held where? | Encryption claimed, not designed |
| 6.7 | Where are secrets stored, and how are they rotated? | Credentials in configuration files |
| 6.8 | What is written to the audit log, retained how long, and can it be altered? | Audit trail that cannot be trusted |
| 6.9 | How could one user reach another user's data? | The threat that matters most, unexamined |
| 6.10 | How is a deletion request honored, end to end including backups? | An obligation half met |
| 6.11 | What is the backup frequency and retention — and has restore been tested? | Backups that do not restore |
| 6.12 | What is logged that should not be? | PII in logs, retained indefinitely |

---

# 7. Architecture and Stack

| # | Question | If unanswered |
| --- | --- | --- |
| 7.1 | What architectural shape, and why at this scale? | Shape by default |
| 7.2 | What are the components and their responsibilities? | Boundaries undefined |
| 7.3 | What is external to the system? | Integration surface unclear |
| 7.4 | For each technology choice: what was rejected? | Assertion, not a decision — fails the gate |
| 7.5 | For each: what is it worse at? | Trade-off unstated, so unexamined |
| 7.6 | For each: what would it cost to change later? | Reversibility unknown |
| 7.7 | Which choices are **one-way doors**? | The evidence bar is spread evenly across decisions of unequal weight |
| 7.8 | **Can the team that will run this actually run it?** | A design nobody can operate |
| 7.9 | Where would a more common technology have served? | Novelty chosen without a reason |
| 7.10 | What architectural capability are we deliberately not adding? | Inflation looks like prudence |
| 7.11 | What happens if a critical third-party service disappears? | Vendor risk unregistered |

---

# 8. Scale, Cost and Reliability

| # | Question | If unanswered |
| --- | --- | --- |
| 8.1 | What load at launch, and at target — from what basis? | Sizing without evidence |
| 8.2 | What breaks first, and at roughly what load? | No capacity plan |
| 8.3 | What is the specific response when it does? | "Scale horizontally" |
| 8.4 | **What are we deliberately not building for?** | Every limit reads as an oversight |
| 8.5 | What does it cost to run at launch? | Unknown burn |
| 8.6 | **Is cost per user inside the ceiling from module 06?** | The business model is broken and nobody knows |
| 8.7 | What availability target, and what justifies it? | Over- or under-engineered reliability |
| 8.8 | What still works when a dependency is down? | Total failure from a partial one |
| 8.9 | What are the RPO and RTO? | Recovery expectations undefined |

---

# 9. Provenance

| # | Question | Category |
| --- | --- | --- |
| 9.1 | Is any version-specific capability or limit claim written from memory? | **NEEDS LOOKUP** |
| 9.2 | Is any regulated field, retention period or code invented? | **NEEDS LOOKUP** |
| 9.3 | Is any cost figure a guess rather than a published price? | **NEEDS LOOKUP** |
| 9.4 | Are there infrastructure or vendor constraints we have not been told? | **OPERATOR** |
| 9.5 | Is there an existing system this must fit into? | **OPERATOR** |
| 9.6 | Are there technologies the team will not adopt? | **OPERATOR** |
| 9.7 | Who will operate this after launch? | **OPERATOR** |

> 9.5 and 9.7 change designs completely and are almost never asked. An operator with an
> existing datastore, or with nobody to run infrastructure, needs a different design — not a
> better one.

---

# Question Coverage

| Section | Feeds |
| --- | --- |
| 1 | §2 Inherited Inputs |
| 2 | §3 Data Model derivation |
| 3 | §3 Data Model |
| 4 | §5 State Machines |
| 5 | §6, §7 Interface and coverage |
| 6 | §10 Security Model |
| 7 | §8, §9, §13 Architecture, stack, decisions |
| 8 | §11, §12 Scale and cost |
| 9 | §15 Open Questions |

---

# Self Assessment

- Did I answer 2.4 and 2.5 in both directions?
- Could a builder answer 3.1 for every column without asking me?
- Did I write the forbidden transitions, or only the legal ones?
- Did I answer 5.4 and 5.5 in both directions?
- Is 6.3 answered with a location, not a description?
- Does every obligation in 6.4 name a mechanism?
- Did 7.4 and 7.5 get real answers, or restatements of the choice?
- Is 8.6 answered with arithmetic?
- Did I look up everything in section 9, or recall it?

---

> **Question Principle**
>
> A question left open here is not left open.
>
> It is answered by whoever builds it, in the dark, and permanently.
