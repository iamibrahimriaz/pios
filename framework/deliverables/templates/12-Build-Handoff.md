---
Artifact: build-handoff
Project: «project name»
Version: 1.0
Date: «ISO date»
Modules: [08-product, 09-technology, 10-execution, 12-metrics]
Critical: true
---

<!-- fill: THIS IS THE MOST IMPORTANT ARTIFACT IN THE RUN.

     THE STANDALONE TEST: could an agent or engineer open this file, with NO access to
     the research conversation and no other document, and start writing correct code today?

     That means:
       - Do not write "as discussed" or "per the research" — the reader was not there.
       - Do not assume the reader will open the other artifacts. Reference them for depth,
         but carry the essentials inline.
       - No unresolved [assumption] may sit in a build-blocking position. If something is
         genuinely undecided, it goes in Blocked Work with a named owner — not into the
         build instructions where someone will guess.

     Write this LAST. Remove every <!-- fill --> comment before delivery. -->

# Build Handoff — «Product Name»

> **Read this first.** This document is self-contained. It tells you what to build, in what
> order, and what "correct" means. Supporting detail lives in the sibling artifacts, but you
> can begin from this file alone.

---

## 1. What You Are Building

<!-- fill: 150 words maximum. Someone who has never heard of this project should finish
     this section able to describe the product to a colleague. -->

«Description»

**For:** «primary persona, one line»
**Solving:** «the sharpest problem, one line»
**Success:** «the activation event — what a user doing it right looks like»

---

## 2. Build This First

<!-- fill: The single most important instruction in the document. Name the first
     milestone, the first feature, and the first thing to put on screen or in the API. -->

**First milestone:** M«n» — «name»

**Why this first:** «one sentence»

**The first thing to make work end to end:**

«A specific, concrete slice. Not "set up the project" — the first slice that a real user
could actually complete. For example: "a doctor can open a patient, dictate a note, and
see it saved to that patient's history."»

**Done when:** «the observable condition»

---

## 3. Stack

| Layer | Technology | Version | Notes |
| --- | --- | --- | --- |
| Language / runtime | «tech» | «version» | |
| Framework | «tech» | «version» | |
| Database | «tech» | «version» | |
| Cache | «tech» | «version» | |
| Queue | «tech» | «version» | |
| Hosting | «tech» | — | |
| Auth | «tech» | — | |

**Decisions you should not revisit without cause:** «the ones with high switching cost —
see `07-Architecture.md` §12 for the reasoning behind each»

---

## 4. Repository Layout

<!-- fill: Concrete. A reader should be able to create these directories immediately. -->

```
«repo-name»/
  src/
    «...»
  tests/
  migrations/
  docs/
```

| Path | Contains | Convention |
| --- | --- | --- |
| `«path»` | «what» | «rule» |

---

## 5. Data Model — Start Here

<!-- fill: The entities needed for milestone 1 ONLY, inline. Do not make the reader
     open another document to start. Full model in 05-Data-Model.md. -->

Build these tables first:

| Entity | Purpose | Key columns |
| --- | --- | --- |
| «name» | «what it holds» | «the ones that matter» |

```sql
-- «entity» — minimal shape for milestone 1
CREATE TABLE «name» (
  id          uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  «column»    «type» NOT NULL,
  created_at  timestamptz NOT NULL DEFAULT now(),
  updated_at  timestamptz NOT NULL DEFAULT now()
);
```

**Full model:** `05-Data-Model.md`
**Non-negotiable constraints:** «the ones encoding business rules that must not be relaxed»

---

## 6. API — Start Here

<!-- fill: The endpoints needed for milestone 1 only. Full contract in 06-API-Contract.md. -->

| Method | Path | Purpose | Auth |
| --- | --- | --- | --- |
| POST | `/v1/«resource»` | «what» | required |
| GET | `/v1/«resource»` | «what» | required |

**Auth scheme:** «summary — full detail in 06-API-Contract.md §2»
**Error shape:** «the standard envelope, inline»

---

## 7. The Critical User Flow

<!-- fill: One flow, in build terms. This is what milestone 1 must make work. -->

```
«step» → «step» → «step» → «done»
```

| Step | Frontend | Backend | Data written |
| --- | --- | --- | --- |
| 1 | «what renders» | «what is called» | «what changes» |

**Must complete in:** «n steps, n seconds»
**Must survive:** «interruption, refresh, connection loss — whichever apply»

---

## 8. Acceptance Criteria for Milestone 1

<!-- fill: Testable. A QA engineer or a test suite could verify each line without
     asking what it means. -->

- [ ] «condition»
- [ ] «condition»
- [ ] «condition»
- [ ] «condition»

**Definition of done:** all boxes checked, «plus any additional bar — tests passing,
deployed to staging, reviewed».

---

## 9. Instrumentation to Build Now

<!-- fill: From 11-Success-Metrics.md §6. If these are not built with the feature, they
     will not be retrofitted, and the product ships blind. -->

| Event | Fires when | Properties |
| --- | --- | --- |
| `«event»` | «trigger» | `«prop»: «type»` |

**Do not instrument:** «what is excluded for privacy or regulatory reasons»

---

## 10. Non-Negotiables

<!-- fill: The rules that must hold regardless of implementation choices. Usually
     security, compliance, and data-integrity constraints carried from the research.
     Anything here that gets violated is a defect, not a trade-off. -->

| # | Rule | Why | Consequence if broken |
| --- | --- | --- | --- |
| 1 | «rule» | «regime or reasoning» | «impact» |

---

## 11. Explicitly Out of Scope

<!-- fill: What NOT to build. Prevents helpful over-delivery that expands the surface
     area before the core is proven. -->

| Not now | Why | Where it lives |
| --- | --- | --- |
| «capability» | «reason» | `09-Roadmap.md` |

---

## 12. Blocked Work

<!-- fill: Anything that cannot be built until a question is answered. This is where
     unresolved assumptions go — NOT into the build instructions.
     If this section is empty, say "None". If it is not empty, the owner must be a
     named human, not "the team". -->

| # | Blocked | Waiting on | Owner | Needed by |
| --- | --- | --- | --- | --- |
| B1 | «what cannot start» | «question or decision» | «named person» | «milestone» |

---

## 13. Known Assumptions in This Build

<!-- fill: Assumptions the reader is inheriting. They are not blocking, but the builder
     should know what ground they are standing on. Full register in
     10-Risks-and-Assumptions.md. -->

| # | We assumed | If it turns out false | What would need to change |
| --- | --- | --- | --- |
| A«n» | «statement» | «consequence» | «which component» |

---

## 14. Next Milestones

| Milestone | Delivers | Start after |
| --- | --- | --- |
| M«n» | «capability» | «M«n» done» |

---

## 15. Where to Look

| Question | Document |
| --- | --- |
| Why are we building this? | `00-Executive-Summary.md` |
| Who is it for, and what do they need? | `01-Research-Dossier.md` |
| Which problem is real? | `02-Problem-Validation.md` |
| What exactly should it do? | `03-PRD.md` |
| What is in the MVP? | `04-Feature-Spec.md` |
| Full schema | `05-Data-Model.md` |
| Full API | `06-API-Contract.md` |
| How is it structured? | `07-Architecture.md` |
| How should it feel to use? | `08-UX-Flows.md` |
| What comes next? | `09-Roadmap.md` |
| What could go wrong? | `10-Risks-and-Assumptions.md` |
| How do we know it worked? | `11-Success-Metrics.md` |

---

## 16. Specification Coverage

<!-- fill: ONE ROW PER SUBJECT IN manifest.yaml's `build_coverage`. Do not delete a row.

     This table is not a summary — it is the standalone test above, made checkable.
     Every other acceptance criterion in this run asks whether one artifact is good.
     This one asks whether the set is enough to build from, which is a different
     question and the only one nothing else was asking.

     Each row is answered EXACTLY ONE of two ways:
       - the artifact and section that specifies it, e.g. `03-PRD.md` §5.1
       - "Not applicable" AND the reason, in the same cell

     "Not applicable" with no reason is the failure this table exists to catch: it is
     indistinguishable from having forgotten.

     THESE SUBJECTS TRACE TO NO RANKED PROBLEM. That is why they are listed here and
     why they are easy to miss — nobody complains about needing to log in, and
     §1's requirement that features trace to problems quietly excludes them. -->

| Subject | The question | Specified in |
| --- | --- | --- |
| **Account and identity** | How is an account created, signed in to, recovered, and deleted? | «artifact §section, or Not applicable — reason» |
| **Authorization** | Who may act on what, and where is that decided? | «...» |
| **Money** | Prices, plans, entitlements, and what happens when someone stops paying | «...» |
| **Non-functional targets** | Latency, availability, durability, capacity, recovery — as numbers | «...» |
| **Data lifecycle** | Retention, deletion, export, and who can trigger each | «...» |
| **Failure behavior** | Errors, limits, and how the system degrades rather than stops | «...» |
| **Environments and configuration** | Every value the system reads, and where it comes from | «...» |
| **Test, QA and release** | What must be true before a change ships, every time | «...» |

> **A row pointing at an artifact that does not cover the subject is worse than a blank
> one.** The blank gets noticed; the pointer gets believed.

---

<!-- ACCEPTANCE — remove before delivery
- [ ] STANDALONE TEST: an agent with no other context could start writing code from this file
- [ ] §16 has a row for every `build_coverage` subject, each naming a section or a reason
- [ ] States what to build first, and why, as a concrete end-to-end slice
- [ ] Data model and API for milestone 1 carried INLINE, not only by reference
- [ ] Stack, versions and repo layout named
- [ ] Acceptance criteria testable
- [ ] Instrumentation specified alongside the feature
- [ ] Non-negotiables carried from the research
- [ ] NO unresolved [assumption] in a build-blocking position — those are in §12 with a named owner
- [ ] Every fill comment removed
-->
