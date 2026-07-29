---
Artifact: problem-validation
Project: «project name»
Version: 1.0
Date: «ISO date»
Confidence: «high | medium | low»
Modules: [04-problem]
---

<!-- fill: This document separates what is KNOWN from what is BELIEVED about the problem.
     It is the honesty checkpoint of the entire run. Everything downstream — the PRD,
     the features, the build — rests on it being truthful.
     Keep validated and assumed problems VISUALLY separate. Do not blend them in prose.
     Remove every <!-- fill --> comment before delivery. -->

# Problem Validation — «Product Name»

## Verdict

<!-- fill: One of:
     VALIDATED        — the core problem is real and evidenced
     PARTIALLY VALIDATED — some problems evidenced, the central one is not
     UNVALIDATED      — the problem is plausible but entirely assumed
     INVALIDATED      — research contradicts the premise
     If UNVALIDATED, say so clearly. Building on an unvalidated problem is the most
     expensive mistake in product development, and the framework exists to prevent it. -->

**«VALIDATED | PARTIALLY VALIDATED | UNVALIDATED | INVALIDATED»**

«Two sentences on what that means for the decision to proceed.»

---

# 1. Problem Inventory

<!-- fill: Every problem surfaced during research. Score each honestly.
     Frequency  — how often it occurs (per day / week / month)
     Severity   — what it costs when it does (time, money, risk, reputation)
     Workaround — what they do today, and how well it works
     Evidence   — the tag. This column determines which table it lands in below. -->

| # | Problem | Who | Frequency | Severity | Current workaround | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| P1 | «problem» | «persona» | «daily» | «high» | «what they do» | [tag] |
| P2 | «problem» | «persona» | «weekly» | «med» | «what they do» | [tag] |
| P3 | «problem» | «persona» | «monthly» | «low» | «what they do» | [tag] |

---

# 2. Validated Problems

<!-- fill: ONLY problems with [verified] evidence. If this section is empty, say so
     explicitly — do not promote assumed problems here to make the document look stronger.
     An empty validated section is a finding, not a failure. -->

> These problems are supported by retrievable evidence.

### P«n» — «problem statement»

| | |
| --- | --- |
| Who | «persona / segment» |
| Frequency | «how often» [tag] |
| Cost when it occurs | «quantified» [tag] |
| Today's workaround | «what they do» |
| Why the workaround is inadequate | «reason» [tag] |
| Evidence | «source» |

---

# 3. Assumed Problems

<!-- fill: Problems that are plausible but not evidenced. These are NOT lesser problems —
     they may be the most important ones. They are simply unproven, and must be labelled
     as such so nobody builds on them by accident. -->

> ⚠️ These problems are believed but **not established**. Do not build on them without validation.

| # | Assumed problem | Why we believe it | What would prove it | Cost to test |
| --- | --- | --- | --- | --- |
| P«n» | «problem» | «reasoning» | «evidence needed» | «effort» |

---

# 4. The Sharpest Problem

<!-- fill: One problem. The one the product should be built around.
     Defend the choice against the scoring table — not against preference or interest.
     If the sharpest problem is an ASSUMED one, say so directly. That is a critical
     finding and changes what should happen next. -->

## «P«n» — problem statement»

**Why this one:**

«Defend against the inventory. Reference frequency, severity, and the inadequacy of the
current workaround. Explain why the other high-scoring problems were not chosen.»

**Evidence standing:** «verified | assumed» — «implication»

**What the product must do about it:** «one sentence — this becomes the product's core job»

---

# 5. Problems We Are Not Solving

<!-- fill: Explicit. Problems that are real but out of scope, and why.
     This prevents scope creep later and shows the reader the choice was deliberate. -->

| Problem | Real? | Why not now |
| --- | --- | --- |
| «problem» | yes | «reason — adjacency, cost, segment mismatch, timing» |

---

# 6. Contradicting Evidence

<!-- fill: From the adversarial review pass. What did you find that argues AGAINST
     the problem being worth solving? If this section is empty, the adversarial pass
     was not performed honestly — every real problem has a case against it. -->

| Finding | Source | Implication | Resolved? |
| --- | --- | --- | --- |
| «what argues against» | [tag] | «what it would mean» | «how it was addressed» |

---

# 7. Validation Plan

<!-- fill: For every assumed problem and every open assumption. Ordered by
     what should be tested FIRST — cheapest test of the most load-bearing belief.
     Be concrete: "interview 10 solo GPs about charting time" not "conduct user research". -->

| Order | Assumption to test | Method | Sample | Effort | Would invalidate |
| --- | --- | --- | --- | --- | --- |
| 1 | «statement» | «interviews / survey / prototype / data pull» | «n and who» | «days» | «what breaks if false» |
| 2 | ... | | | | |

**Test this first:** «the single cheapest test of the most load-bearing assumption»

**Stop-and-rethink trigger:** «what result would mean the product should not be built»

---

# 8. Evidence Standing

| | Count |
| --- | --- |
| Problems identified | «n» |
| Verified with evidence | «n» |
| Assumed | «n» |
| Contradicting findings | «n» |

«One sentence: how much weight the problem foundation can bear.»

---

<!-- ACCEPTANCE — remove before delivery
- [ ] Verdict stated up front
- [ ] Problems ranked by frequency, severity and current workaround
- [ ] Validated and assumed problems visually separate, never blended
- [ ] The sharpest problem identified and defended against the scoring table
- [ ] Contradicting evidence section is non-empty
- [ ] Validation plan is concrete and ordered by cheapest-test-of-biggest-belief
- [ ] Every assumption appears in state.assumptions
- [ ] Every fill comment removed
-->
