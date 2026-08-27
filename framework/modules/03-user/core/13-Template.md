---
Title: Template
Module: 03-user
Section: core
Category: Output
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: The working template for the User Analysis — this module's primary output.
Audience:
  - AI Agents
Prerequisites:
  - 03-user/core/06-Framework.md
Outputs:
  - projects/<slug>/research/03-user.md
Related Modules:
  - 04-problem
  - 10-execution
Tags:
  - User
  - Template
  - Output
---

# Template — User Analysis

---

# Usage

Copy everything below the line into `projects/<slug>/research/03-user.md` and fill it.

This is a **working document**, not a customer deliverable. It feeds
`deliverables/templates/01-Research-Dossier.md` §2, the PRD, and the UX Flows.

| Marker | Meaning |
| --- | --- |
| `«placeholder»` | Replace with real content |
| `<!-- guidance -->` | Instructions for you. Remove before completing |
| `[tag]` | Evidence tag per `engine/evidence-policy.md` |

A section that cannot be filled is a finding. Write what is missing and why.

---
---

# User Analysis — «Project Name»

| | |
| --- | --- |
| Module | 03-user |
| Date | «ISO date» |
| Market | «from market_definition» |
| Status | draft / complete |
| Confidence | «high / medium / low» |
| Primary research conducted | «yes / no — if no, everything here is inferred» |

<!-- The last row is the most important metadata in this document. An agent without
     access to real users has inferred these findings from proxy evidence. Say so
     plainly at the top, so no reader mistakes inference for observation. -->

---

## 1. Segments

<!-- Move 1. Divide the market into groups that behave differently. A segment is only
     a segment if its members would buy, use, or reject the product for different
     reasons. Demographic splits that do not change behavior are not segments. -->

| # | Segment | Size | Pain intensity | Ability to pay | Reachable via | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| S1 | «who» | «n» [tag] | high / med / low | high / med / low | «channel» | [tag] |
| S2 | «who» | «n» [tag] | high / med / low | high / med / low | «channel» | [tag] |

**What makes these different segments:** «the behavioral difference, not the demographic one»

---

## 2. Prioritization

<!-- Move 2. Choose one segment to serve first. The reasoning must reference the table
     above — not preference, not interest, not what is easiest to research. -->

**Serving first: S«n» — «name»**

| Criterion | S1 | S2 | Winner |
| --- | --- | --- | --- |
| Pain intensity | «rating» | «rating» | «which» |
| Ability to pay | «rating» | «rating» | «which» |
| Reachability | «rating» | «rating» | «which» |
| Speed to first customer | «rating» | «rating» | «which» |

**Reasoning:** «one paragraph, referencing the table»

**Why not the larger segment:** «if a bigger segment was passed over, defend that here»

**What we give up by choosing this one:** «honest cost of the choice»

---

## 3. Primary Persona

<!-- Move 3. Grounded in evidence, not invented. A persona that could describe anyone
     describes no one.

     THE EVIDENCE COLUMN TAKES THREE VALUES, not a tag or a blank:
       [verified: <source>]        — observed or reported by a real person
       [inferred: <basis>]         — reconstructed; NAME what it was reconstructed from
       [assumption: needs validation]

     A blank reads as an oversight and an invented citation is worse. Where a row has no
     source, mark it and say what it was built from. A persona whose rows are honestly all
     inferred is a finding about the run's evidence base — carry it into the limit output
     in engine/remote-validation.md rather than dressing it up.

     SEPARATELY FROM THE TAG, every user finding carries a MODE in evidence_log. The gate
     requires it and the two vocabularies are not interchangeable — a tag says how well the
     claim is supported, a mode says where it came from. Use these three words exactly:

       observed       — someone watched the work happen
       reported       — a person described it, in an interview, a review or a post
       reconstructed  — worked out from the shape of the work and from adjacent facts;
                        watched by nobody and described by nobody

     `reconstructed` is the normal case in a desk run and it is not a lesser answer. Marking
     a reconstruction as `reported` passes the gate while destroying the only distinction the
     gate exists to protect. Do not substitute a synonym — two runs that say `reconstructed`
     and `inferred` for the same thing cannot be compared to each other. -->

<!-- ACCEPTANCE: every persona row carries an evidence tag, and every user finding in
     state.evidence_log carries mode: observed | reported | reconstructed. -->

### «Name» — «role», «segment»

| | | Evidence |
| --- | --- | --- |
| Context | «where and how they work» | [tag] |
| Typical day | «the shape of it, relevant parts only» | [tag] |
| Goal | «what success looks like to them» | [tag] |
| Frustration | «what makes the current situation bad» | [tag] |
| Constraints | «time, budget, skill, regulation, physical setting» | [tag] |
| Technical comfort | «assessment» | [tag] |
| Buyer or user | «buyer / user / both» | — |
| Decision trigger | «what would make them change» | [tag] |
| Decision blocker | «what would stop them» | [tag] |

**In their words:** «a real quote from a review, forum, or study — attributed» [tag]

<!-- If no real quote can be found, write "no primary voice located" rather than
     inventing one. A fabricated quote is the single most damaging thing this
     module can produce. -->

**What we do NOT know about this person:** «the honest gaps»

---

## 4. Secondary Personas

<!-- Only those who affect the decision: the buyer if different from the user,
     the blocker, the influencer. Keep brief. -->

| Persona | Role in the decision | What they need to see | Evidence |
| --- | --- | --- | --- |
| «name» | buyer / blocker / influencer | «their criterion» | [tag] |

---

## 5. Current Workflow

<!-- Move 4. What actually happens today, step by step, with the tools named.
     This is where the real opportunity is usually found — in the friction between
     steps, not in the steps themselves. -->

```
«step 1» → «step 2» → «step 3» → «step 4» → «step 5»
```

| Step | What they do | Tool used | Time | Friction |
| --- | --- | --- | --- | --- |
| 1 | «action» | «named product or "paper"» | «duration» | «what is annoying» [tag] |

**Total time for the whole workflow:** «duration» [tag]

**Where it breaks:** «the friction points, ranked» [tag]

**The step they would most want removed:** «which, and why» [tag]

**Tools that would be replaced:** «named products»

**Tools that must be kept:** «what the product must coexist with»

---

## 6. Switching Cost

<!-- Underestimating this kills products. A better tool that costs two weeks of
     disruption loses to a worse tool already installed. -->

| Cost type | Magnitude | Detail | Mitigation |
| --- | --- | --- | --- |
| Data migration | high / med / low | «what data, what volume» | «approach» |
| Retraining | high / med / low | «who, how long» | «approach» |
| Workflow disruption | high / med / low | «what stops working during the change» | «approach» |
| Contractual lock-in | high / med / low | «terms, notice periods» | «approach» |
| Risk of change | high / med / low | «what they fear going wrong» | «approach» |

**Total switching cost:** «assessment»

**What must be true for switching to be worth it:** «the bar the product must clear»

**Who inside the organization would resist, and why:** «if applicable»

---

## 7. Jobs To Be Done

<!-- Move 5. Jobs, not features. Format: When «situation», I want to «motivation»,
     so I can «outcome».
     THE TEST: if the sentence names a solution, it is not a job. -->

| # | Job | Frequency | Currently satisfied by | How well | Evidence |
| --- | --- | --- | --- | --- | --- |
| J1 | When «situation», I want to «motivation», so I can «outcome» | «daily» | «today's method» | poorly / adequately | [tag] |
| J2 | ... | | | | |

**Primary job:** J«n» — «why this one carries the product»

**Jobs the product will NOT serve:** «explicit, so scope stays bounded»

---

## 8. What They Would Not Change

<!-- Under-asked and highly predictive. Habits, tools, or rituals that are effectively
     immovable define the shape any successful product must take. -->

| Immovable | Why | Implication for the product |
| --- | --- | --- |
| «habit, tool, or constraint» | «reason» | «what the product must accommodate» |

---

## 9. Contradicting Evidence

<!-- From the adversarial review pass. What did you find suggesting these users do NOT
     want this, or would not adopt it? Must not be empty. -->

| Finding | Source | Implication | Resolved? |
| --- | --- | --- | --- |
| «what argues against» | [tag] | «what it would mean» | «how addressed» |

---

## 10. Handoff

| Field | Value | Consumed by |
| --- | --- | --- |
| `segments` | «summary + priority» | 04-problem, 05-competition, 06-business |
| `personas` | «primary + secondary» | 04-problem, 08-product, 10-execution |
| `jobs_to_be_done` | «list» | 04-problem, 08-product, 14-ai-systems |
| `current_workflow` | «summary» | 04-problem, 10-execution |
| `switching_cost` | «assessment» | 06-business, 11-growth |

---

## 11. Sources

| # | Source | Type | Accessed | Used for |
| --- | --- | --- | --- | --- |
| S1 | «citation» | review / forum / study / interview / job posting | «date» | «claims» |

---

## 12. Evidence Standing

| | Count |
| --- | --- |
| Claims from primary research | «n» |
| Claims from proxy evidence | «n» |
| Claims inferred | «n» |
| Open assumptions | «n» |

**Was any real user consulted?** «yes / no»

**Largest gap:** «what is least established about these users»

**Confidence:** «high / medium / low»

<!-- If no real user was consulted, confidence cannot be "high". State what would
     raise it: how many interviews, with whom. -->

---

<!-- COMPLETION CHECK — remove before marking complete
- [ ] >= 2 segments, differing by behavior not demographics
- [ ] One segment prioritized, defended against the criteria table
- [ ] Persona grounded in evidence — every row traceable
- [ ] No invented quotes; missing voice stated as missing
- [ ] Current workflow documented step by step, with tools named
- [ ] Switching cost assessed across all five types
- [ ] Jobs stated as jobs — none names a solution
- [ ] "What they would not change" completed
- [ ] Contradicting evidence non-empty
- [ ] Primary-research status stated honestly at the top
- [ ] Every claim carries exactly one evidence tag
- [ ] Every placeholder replaced, every guidance comment removed
-->
