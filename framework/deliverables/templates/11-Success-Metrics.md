---
Artifact: success-metrics
Project: «project name»
Version: 1.0
Date: «ISO date»
Modules: [12-metrics]
---

<!-- fill: Every metric needs a DEFINITION, a SOURCE and a TARGET. A metric without a
     target is a number nobody acts on. Event-level instrumentation is specified here
     because the build handoff depends on it — if it is not defined now, it will not
     be built, and the product will ship blind.
     Remove every <!-- fill --> comment before delivery. -->

# Success Metrics — «Product Name»

## 1. North Star

<!-- fill: Exactly one. It must represent delivered user value, not company convenience.
     Revenue is usually not a north star — it is a consequence of one.
     Defend the choice: why this metric and not the obvious alternative? -->

## «Metric name»

| | |
| --- | --- |
| Definition | «precise, unambiguous — a reader could compute it» |
| Why this one | «what it captures that alternatives do not» |
| Rejected alternative | «metric» — «why it would mislead» |
| Source | «where the number comes from» |
| Baseline | «current value, or "new product — none"» |
| Target | «figure by date» |
| Review cadence | «weekly / monthly» |

**What it would look like if we were gaming it:** «the degenerate behavior this metric
could incentivize, and what guards against it»

---

## 2. Goal Metrics

<!-- fill: One per goal in the PRD. Every PRD goal must appear here. -->

| Goal | Metric | Definition | Baseline | Target | By |
| --- | --- | --- | --- | --- | --- |
| G1 | «metric» | «how computed» | «value» | «value» | «date» |
| G2 | «metric» | «how computed» | «value» | «value» | «date» |

---

## 3. Leading vs Lagging

<!-- fill: Leading indicators move first and are actionable. Lagging indicators confirm
     but arrive too late to steer by. Teams that track only lagging metrics discover
     problems a quarter after they could have fixed them. -->

### Leading Indicators

| Metric | Predicts | Definition | Target | Warning threshold |
| --- | --- | --- | --- | --- |
| «metric» | «which lagging metric» | «how computed» | «value» | «when to worry» |

### Lagging Indicators

| Metric | Confirms | Definition | Target |
| --- | --- | --- | --- |
| «metric» | «what» | «how computed» | «value» |

---

## 4. Activation

<!-- fill: The single most important early metric for a new product. Define the moment
     a user has genuinely received value — tied to the time-to-first-value in the UX flows. -->

| | |
| --- | --- |
| Activation event | «the specific action that means "they got it"» |
| Why this event | «reasoning» |
| Target time to activate | «minutes, from UX flows» |
| Target activation rate | «percentage of signups» |

---

## 5. Counter-Metrics

<!-- fill: What must NOT get worse while the primary metrics improve.
     Without these, a team optimizes the north star into a worse product. -->

| Metric | Must not exceed / fall below | Why it matters |
| --- | --- | --- |
| «e.g. error rate» | «threshold» | «what it protects» |
| «e.g. time per task» | «threshold» | «what it protects» |

---

## 6. Instrumentation Plan

<!-- fill: Event-level. This section is consumed directly by the build handoff.
     If an event is not specified here, it will not exist, and the metric above
     cannot be computed. Name every property. -->

| Event | Fires when | Properties | Feeds metric |
| --- | --- | --- | --- |
| `«event_name»` | «trigger» | `«prop»: «type»`, `«prop»: «type»` | «metric» |

**Identity:** «how a user is identified across sessions and devices»

**Privacy constraints:** «what must NOT be captured, per the regulatory landscape»

<!-- fill: For regulated domains this is critical — analytics on regulated data is a
     compliance exposure. State explicitly what is excluded from instrumentation. -->

---

## 7. Measurement Infrastructure

| Concern | Approach |
| --- | --- |
| Analytics tool | «tool» |
| Event pipeline | «how events reach it» |
| Dashboard | «where the team sees this» |
| Data retention | «period, per regulation» |
| Who reviews, how often | «person / cadence» |

---

## 8. Reporting

| Report | Audience | Cadence | Contains |
| --- | --- | --- | --- |
| «name» | «who» | «weekly» | «which metrics» |

---

## 9. Metric Review Triggers

<!-- fill: When should the metrics themselves be reconsidered? Metrics that made sense
     at launch often stop making sense at scale. -->

| Trigger | Reconsider |
| --- | --- |
| «e.g. after 100 active accounts» | «whether the north star still reflects value» |

---

<!-- ACCEPTANCE — remove before delivery
- [ ] Exactly one north star, with the reasoning and a rejected alternative
- [ ] Every PRD goal appears as a goal metric
- [ ] Every metric has definition, source and target
- [ ] Leading and lagging indicators distinguished
- [ ] Activation event defined and tied to time-to-first-value
- [ ] Counter-metrics defined
- [ ] Event-level instrumentation specified with properties
- [ ] Privacy constraints on instrumentation stated
- [ ] Every fill comment removed
-->
