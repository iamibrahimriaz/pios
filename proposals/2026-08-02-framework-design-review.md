# Framework Design Review — Eight Proposed Changes

| | |
| --- | --- |
| Date | 2026-08-02 |
| Status | **PROPOSAL — nothing in `framework/` has been changed** |
| Source | The friction logs of two completed runs: 23 entries, 12 of them operator-visible |
| Decision needed | Accept / Modify / Reject, per item |

---

## How to read this

Each item carries the same twelve fields. **Read the Decision Summary first**, then only the
items you intend to change — they are independent except where "Depends on" says otherwise.

**The evidence sections name no project, market, figure or customer.** This file is tracked;
`projects/` is gitignored specifically so run content never reaches a public repository. Both runs
therefore appear as structural facts only — which is also the form in which a defect is actually
useful, since a defect that only makes sense with a particular run in front of you is not yet a
framework change.

**Runs are identified as Run 1 and Run 2** by completion order. Nothing else about them is stated.

---

## Decision Summary

| # | Change | Priority | Size | Blast radius | Recommendation |
| --- | --- | --- | --- | --- | --- |
| **H** | **Preserve uncertainty rather than reduce it** — as a named principle | **Governs A** | One section | Constitution | **Accept** |
| **A** | **Conditional continuation after a research-limited gate** | **1st** | Large | Gates · schema · validator · skill | **Accept, as specified** |
| **B** | **Remote Validation mode** | 2nd | Medium | New engine doc · evidence policy | **Accept** |
| **C** | **Reply contract — a typable closing line** | 3rd | Small | Skill only | **Accept** |
| **D** | **Explicit framework boundary** | 4th | One section | Constitution · both skills | **Accept** |
| **E** | **Four gate criteria that offer false binaries** | 5th | Medium | 4 module pairs | **Accept E1/E2/E4 · Modify E3** |
| **F** | **Record operator-confirmed value** | 6th | Small | Schema · authoring skill | **Accept** |
| **G** | **Template gaps, and the check that would have caught them** | 7th | Small–Medium | Templates · `validate.py` | **Accept** |

---

## The guarantees item A must preserve

Stated as binding constraints on the design, not as aspirations. **A design that violates any of
these should be rejected outright rather than amended.**

1. **A failed gate remains failed.** It is not reclassified, retired or absorbed.
2. **Conditional work is always explicitly marked**, in state and in every artifact.
3. **Validation status can never be upgraded implicitly.** Only new evidence raises it.
4. **Every downstream module inherits the uncertainty automatically** — not by the agent
   remembering to.
5. **Final outputs cannot claim validated conclusions** while a conditional gate is unresolved.
6. **The validator distinguishes three states**: Passed · Failed · Conditionally Continued.

> **The objective is to represent reality more accurately, not to make it easier to continue.**
> Every mechanism below is designed to make conditional continuation *more* work than passing
> honestly, never less.

---

## Recommended sequencing

Close to the stated priority, with one deliberate change.

| Order | Item | Why here |
| --- | --- | --- |
| 1 | **H** | **It governs A.** A conditional-continuation state designed without the principle stated is the change most likely to drift into an escape hatch. One section, and it constrains everything after it |
| 2 | **C**, **D** | Near-free, no artifact or gate impact, and they fix the defect the operator hit most often. Doing them early removes noise from the review of A |
| 3 | **A** | The architectural change. Reviewed on its own, against H |
| 4 | **B** | Structural, independent of A |
| 5 | **F**, **G** | Small; G's validator check is the real deliverable |
| 6 | **E** | Last, because E3 needs modelling against both runs before it is safe |

**The only departure from the stated priority is putting H before A**, on the grounds that A's design
should be answerable to a written principle rather than to a review conversation.

---
---

# H · Preserve uncertainty rather than reduce it

> Proposed by the operator. Placed first because it is the constraint the other seven are judged
> against.

### Problem statement

The framework enforces uncertainty-preservation through many local mechanisms — three evidence tags
with no partial credit, mechanically computed confidence, no-fabrication rules, the declared
shortfall, pre-registration of expected outcomes. **It never states the axiom those mechanisms
implement.** A principle that exists only as implementations is removed one implementation at a
time, each removal locally reasonable and none of them obviously the moment the property was lost.

### Why it occurred

The constitution states operating rules. This is the axiom *behind* several of them, and axioms are
the easiest thing to leave implicit because everyone currently working on the system already holds
it.

### Evidence from both runs

- **Both runs:** the outputs the operator identified as most trustworthy were refusals — an analysis
  reported as impossible rather than filled; a gate left failed rather than passed on a plausible
  estimate; a stated differentiator withdrawn when the law prohibited it; original figures retained
  beside corrected ones rather than overwritten.
- **Run 2:** the operator stated it directly and unprompted — *preserving uncertainty is preferable
  to creating false certainty* — and made it a standing instruction for the remainder of the run,
  which the framework had no way to record as a durable property rather than a one-off directive.
- **Both runs** reached `low` confidence for the same structural reason: verified market and
  regulatory material, unverified human behaviour. In both, the temptation available at that point
  was to average the two into something that sounded more solid.

### Current workaround

Implicit, and defended by whoever is paying attention. It required operator intervention twice.

### Proposed solution

Add a named principle to the constitution:

> **Accurate uncertainty outranks unsupported confidence.**

With its operational consequences stated, because a principle without consequences is decoration:

1. A finding that cannot be established is reported as unestablished. **It is never estimated into
   existence** to complete a section.
2. Confidence is computed from the evidence standing of load-bearing claims. **It is never
   asserted**, and never adjusted to match the tone of a conclusion.
3. **No downstream step may raise the standing of an upstream claim.** Restating an assumption in a
   later artifact does not make it a finding.
4. Where a required output cannot be produced honestly, the framework reports the impossibility and
   what would resolve it, rather than producing a lower-quality version of the output.

Then bind it in `pios-author`: **any change that would reduce recorded uncertainty must state what
evidence justifies the reduction.**

### Alternative designs considered

| Alternative | Why rejected |
| --- | --- |
| Leave it implicit — the mechanisms already enforce it | It has already required operator intervention twice in two runs. That is the failure mode, observed |
| Make it a gate criterion | It is an axiom, not something a module either satisfies or does not. As a criterion it would be unfalsifiable and would degrade into a box-tick |
| Put it in `learn/` as rationale | An executing agent skips `learn/` entirely. It would be invisible at exactly the moment it matters |

### Risks introduced

**A principle can be cited to block useful simplification** — "that would reduce uncertainty" is
available as an argument against almost any change. Mitigated by scoping it to *claims and their
standing*, not to prose, structure or length. Simplifying how something is written is untouched;
simplifying away the record of what is not known is not.

### Why the proposed solution is preferable

It converts a property currently held by attention into one held by the document. The alternative
is not that the property is enforced elsewhere — it is that it survives as long as the people
involved happen to value it.

### Backward compatibility impact

**None.** No artifact, key or gate changes.

### Files / modules affected

`framework/constitution/` (one new principle) · `.claude/skills/pios-author/SKILL.md` (the binding
rule).

### Migration strategy

None required.

### Recommendation

**Accept.** This is the item that protects the value of the other seven, and it is the cheapest
change in the set.

---
---

# A · Conditional continuation after a research-limited gate

**Depends on: H.**

### Problem statement

A gate has two verdicts: passed, failed. A gate can fail for a third reason neither models — **the
evidence the criterion requires does not exist in any source available to the run**, and no amount
of further work by the agent will produce it.

At that point the framework offers only two paths, and both are wrong. Abandon the run, discarding
completed and still-valid work. Or continue by improvisation, with no defined vocabulary for what
"continue" means — which is what happened, and which produces two runs that cannot be compared
because each invented its own.

### Why it occurred

`gates.yaml` was designed around two causes of failure:

- **Insufficient work** → retry, consuming a loop-protection attempt.
- **A missing decision** → `decision_dependent_failure`, which correctly does not consume an
  attempt.

A third cause — **the answer is unobtainable by any method available to this run** — was not
modelled. Two existing mechanisms look adjacent and are not:

- `declared_shortfall` is deliberately scoped to a single criterion in a single module, because a
  waiver available everywhere binds nowhere. Widening it is the wrong fix and is explicitly warned
  against in the authoring rules.
- `degraded_mode` covers an agent with **no retrieval capability**. Here retrieval works perfectly
  and the answer is not in the world. Conflating the two would let a run with a broken tool claim the
  same standing as a run that exhausted its sources.

### Evidence from both runs

**The same module failed in both runs. That is the signal, and it is why this item is first.**

- **Run 1:** the gate failed twice on one criterion. Both times the missing input was an operator
  *decision*, not a research finding, and loop protection consumed attempts for a wait the agent
  could not have shortened. **This produced `decision_dependent_failure`, which is now in the
  framework and working.**
- **Run 2:** the same module, failed twice, but the missing input was a measured quantity that eight
  named source types established does not exist in public form. The operator authorised the run to
  continue with the premise open. **The agent then invented four mechanisms** to carry that state: a
  conditional verdict value, a status key on every downstream output, a binding precondition on the
  first build milestone, and a three-way inline claim-marking convention. **None of the four exists
  in the framework.**
- **Run 2, at delivery:** the run validator reported the artifact set as *not deliverable* for one
  reason — the failed module was correctly absent from the completed list. The only way to make it
  pass was to record a module as complete that was not, which is precisely the laundering the
  evidence policy forbids. **The framework's own tooling could not express the honest state.**

### Current workaround

Improvisation, per run. Four mechanisms in Run 2; Run 1 did not need them because its blocker was a
decision rather than a research limit. **A third run would invent a fifth vocabulary.**

### Proposed solution

A `conditional_continuation` block in `framework/engine/gates.yaml`, designed so that entering it is
*harder* than passing.

**Preconditions — all must hold, and all are recorded:**

| # | Precondition | Purpose |
| --- | --- | --- |
| 1 | The gate has failed **at least twice** on the same criterion | Prevents first-attempt escape |
| 2 | The failure cause is recorded as `evidence_unobtainable`, **with an exhaustion record**: each source type attempted, named, with its result | Makes "unobtainable" auditable rather than asserted. **This is the load-bearing precondition** |
| 3 | The operator authorises it **explicitly**, recorded verbatim with a date | A human owns the decision, and the record shows who |
| 4 | **One gate attempt is reserved, not spent** — and it may not be spent on the method that already failed | The gate is postponed, not abandoned. Recorded as reserved |
| 5 | A validation milestone becomes the **first** milestone of the roadmap, and the first build milestone is blocked on the reserved attempt being evaluated | Makes the postponement operational rather than rhetorical |

**Consequences — automatic, not the agent's choice:**

| Guarantee | Mechanism |
| --- | --- |
| A failed gate remains failed | The module stays in `failed_gates` and **never enters `completed_modules`** |
| Downstream inherits automatically | Every module after it records `conditional_on: <module>`; the validator fails if the chain is incomplete |
| Conditional work is always marked | Every downstream deliverable carries a conditional banner and the three-way claim marking |
| Status cannot be upgraded implicitly | **`run.confidence` is capped at `low`** while any conditional gate is open |
| No validated claim | The executive summary must state the run is a conditional blueprint, not a validated case |
| Three validator states | Exit **0** deliverable · **2** deliverable, conditionally · **1** not deliverable |

**Exit code 2 is the point of the change.** It is the state both runs were actually in and neither
could express.

### Alternative designs considered

| Alternative | Why rejected |
| --- | --- |
| **Widen `declared_shortfall` to any gate** | The authoring rules already answer this: the moment any gate can be waived by declaration, no gate binds anywhere. It is scoped to one criterion in one module deliberately |
| **Treat it as `degraded_mode`** | Different condition — missing *capability* versus missing *evidence in the world*. Conflating them lets a broken toolchain claim the standing of an exhaustive search |
| **Halt the run; require fieldwork before continuing** | **The theoretically pure answer, and it deserves stating.** Rejected on two grounds: it discards completed work that remains valid, and the fieldwork is usually *better designed* once the downstream specification exists — you need the design to know what to ask. The cost is that the specification is provisional, which is exactly what the marking is for |
| **A boolean `conditional: true` on the run** | Too weak to hold any of the six guarantees. No preconditions, no reserved attempt, no inheritance, no validator distinction. It becomes a checkbox within one run |

### Risks introduced by the change

| Risk | Severity | Mitigation |
| --- | --- | --- |
| **It becomes the default escape hatch from any hard gate** | **High — this is the risk** | Requires two prior failures, a named-source exhaustion record, explicit operator authorisation, and it renders the run permanently un-validatable until resolved. **Strictly more work than passing honestly** |
| Modules are marked conditional that need not be | Medium | The validator checks the inheritance chain is complete *and* that nothing outside the downstream set is marked |
| Exit code 2 is read as success by automation | Medium | The word "conditionally" in the output; documented that 2 is not 0; the summary line states the unresolved gate by name |
| The reserved attempt is quietly spent on desk research again | Medium | Precondition 4 records the method that failed; spending the reserved attempt on it is a validator failure |

### Why the proposed solution is preferable

**The alternative to a defined conditional state is not rigor — it is improvisation, and that has
been observed twice.** A framework whose only options are "pass" and "abandon" will be worked around
by any competent agent facing eight modules of valid work and one unobtainable number. The question
is whether the workaround is designed and auditable, or invented fresh each time.

It also converts a recurring accident into evidence: a run that enters this state has *documented*
that a specific question is not answerable remotely, which is itself a finding about the market.

### Backward compatibility impact

**Additive.** No existing key changes meaning. A run with no conditional gate has an empty
precondition set and exits 0 exactly as before. Exit code 2 is new and previously unused.

### Files / modules affected

`framework/engine/gates.yaml` (new block) · `framework/engine/state-schema.yaml` (verdict value,
`conditional_on`, the exhaustion and authorisation records) · `framework/engine/validate-run.py`
(third exit state, inheritance-chain check, confidence cap) · `.claude/skills/pios/SKILL.md` (when to
propose it, and that only the operator may authorise it) · `framework/deliverables/manifest.yaml`
(executive-summary acceptance criterion).

### Migration strategy

**None required for completed runs.** They contain no conditional gates and are unaffected.

One completed run carries an improvised version of this state. **Recommend leaving it as written** —
it is a historical record of what the run believed, and rewriting it to match a mechanism that did
not exist at the time would falsify the audit trail. A short mapping note may be added to that run's
checkpoint instead.

### Recommendation

**Accept, as specified.** Reject any variant that drops preconditions 2 or 4, or the confidence cap
— those three are what make it a representation of reality rather than an escape hatch.

---
---

# B · Remote Validation mode

### Problem statement

The framework assumes primary research — interviews, observation, direct customer contact — is
available to whoever runs it. **For a solo operator at the idea stage it frequently is not**, at
least not before some desk work justifies the effort. There is no method for reaching the limit of
public evidence efficiently, and no defined output stating what remains unobtainable without
customer contact.

### Why it occurred

Modules specify **what evidence is needed**. The evidence policy specifies **how to grade a claim
once you have it**. Neither specifies **how to acquire it**, or what to do when the only source type
that could supply a claim is unavailable to this operator.

### Evidence from both runs

- **Run 2:** eight source types were attempted against a single question before concluding that the
  public corpus does not exist. **The exhaustion was discovered, not planned** — there was no ladder
  to walk, so the agent improvised an order and stopped when it ran out of ideas. The finding that
  emerged (buyers in that category are not reachable through any public channel) was **real market
  intelligence, surfaced as a byproduct of a failed search**, and a less stubborn run would have
  filed it as "insufficient research".
- **Run 1:** the same structural condition, less visibly — the run reached delivery with no primary
  voice, and with no explicit statement of what that cost or what would close it.
- **Both runs:** confidence `low` for the identical reason — market structure and regulation
  verified, human behaviour unverified. **That pattern is not a coincidence of two projects; it is
  the shape of every desk-only run**, and the framework does not name it.

### Current workaround

None. The agent improvises a search order, and reports a shortfall in prose.

### Proposed solution

A `remote_validation` mode in `framework/engine/`, invoked when primary research is unavailable for
a given question.

**1 — A source ladder, cheapest first**, each rung recording *attempted · found · not found*:

official and regulatory publications → competitor published material (pricing, documentation, FAQs,
demos, changelogs) → public discussion (forums, groups, review aggregators) → hiring signals (job
postings) → trade press.

**2 — A required output, `remote_validation_limit`:** the specific questions that cannot be closed
without customer contact, each with the cheapest method that would close it and its cost in days.
**This output feeds the validation milestone directly**, so the fieldwork plan is derived from what
the desk work could not reach rather than invented separately.

**3 — Exhaustion is a recorded finding, not an apology.** *"The internet cannot answer this"*
becomes a first-class verdict, and **the absence of a public corpus is itself evidence** — about
reachability, about channel, about how the market's buyers actually behave.

### Alternative designs considered

| Alternative | Why rejected |
| --- | --- |
| Fold into `degraded_mode` | Different condition: missing *capability* versus missing *access to people*. A run with full retrieval and no interviewees is not degraded, it is desk-only |
| Make it a module | It is cross-cutting. Any research module can hit the wall, and a separate module would either duplicate their methods or be skipped |
| Leave it to agent judgement | This is the status quo, and it produced an undirected eight-source crawl whose value was recovered only because the agent happened to record the negative result |

### Risks introduced by the change

A ladder invites mechanical box-ticking, and an agent that walks it shallowly can claim exhaustion
after five minutes per rung. **Mitigated by requiring each negative result to state what was actually
searched**, so "not found" is auditable rather than assertable — the same discipline the evidence
policy applies to positive claims.

### Why the proposed solution is preferable

It converts the most common condition of a real run from an improvisation into a method, and it
turns the most disappointing outcome — nothing found — into an output with downstream value.

### Backward compatibility impact

**Additive and opt-in per question.** Runs with primary research available are unaffected.

### Files / modules affected

New `framework/engine/remote-validation.md` · `framework/engine/evidence-policy.md` (reference) ·
`framework/engine/state-schema.yaml` (the limit output) · the research modules' `knowledge/` files.

### Migration strategy

None. Completed runs keep their existing evidence records.

### Recommendation

**Accept.**

---
---

# C · Reply contract — a typable closing line

### Problem statement

The reply contract requires every message to close by naming one of three situations. **Its third
branch — "nothing is needed from you" — has no required form, and offering the operator a set of
options is not prohibited.** The result satisfies the contract and still leaves the reader deciding
whether the ball is in their court before they can decide anything else.

### Why it occurred

The contract was written as guidance with example phrasings rather than as a constraint with a
prohibition. **Guidance degrades under the pressure to be helpful** — listing three things the
operator might want feels more accommodating than instructing them to type one word, and it is
worse.

### Evidence from both runs

- **Run 2:** reported by the operator about **every reply across fourteen modules**, not one of them.
  It is the single most repeated defect either run produced.
- **Run 2:** **none of the sixteen agent-recorded friction entries caught it.** An agent reads its
  own closing block as unambiguous because it knows what it meant. This is the blind spot the
  authoring rules already warn about — the log records where the framework blocked the *agent*, and
  cannot see where it was unclear to the *operator*.
- **Run 1:** not recorded, which given the above is consistent with the same defect being present
  and unnoticed rather than with its absence.

### Current workaround

None. It depends on agent discipline, which did not hold for fourteen consecutive modules.

### Proposed solution

Convert guidance into a constraint:

1. **Every reply ends with a line the operator can type verbatim.**
2. **The pattern "tell me if you want X, Y or Z" is banned by name.** It is a menu wearing an
   instruction's clothes.
3. **When options exist, one is marked the default**, and the block states what a bare `continue`
   does — so an operator who does not want to choose still has a path.
4. **Every blocking question carries the assumed default and its cost** if unanswered.
5. Make it a **checked criterion at each human checkpoint** rather than prose, so it is enforceable
   rather than aspirational.

### Alternative designs considered

| Alternative | Why rejected |
| --- | --- |
| Leave as guidance, state it more emphatically | It was already stated with a test attached. Emphasis is what failed |
| A fixed template string for the closing block | Too rigid — a question block, a confirmation block and a progress block have genuinely different shapes. Constrains the wrong thing |
| Enforce it only at checkpoints | Most replies in a run are not at checkpoints, and that is where it degraded |

### Risks introduced by the change

**Replies become formulaic.** Mitigated by scoping the rule to the final block only; everything
above it is unconstrained.

### Why the proposed solution is preferable

It is the cheapest change in this document by a wide margin and it addresses the defect the operator
personally encountered most often. A prohibition on a named pattern is enforceable in review; an
exhortation to be clear is not.

### Backward compatibility impact

**None.** Affects agent behaviour, not artifacts or state.

### Files / modules affected

`.claude/skills/pios/SKILL.md` · mirrored in `.claude/skills/pios-author/SKILL.md`.

### Migration strategy

None.

### Recommendation

**Accept.**

---
---

# D · Explicit framework boundary

### Problem statement

**The framework never states where it stops.** It describes fourteen modules, a delivery step, a
proposal step, and a handoff step whose stated purpose is to make the run directory the place work
starts — and then says nothing about whether that work is in scope.

### Why it occurred

The handoff step was added late, to close a real gap: a completed run had no defined way to reach a
developer. Its language solved that problem and introduced this one. *"Making the folder the place
the work starts"* reads as an on-ramp to building rather than as the framework's last act.

### Evidence from both runs

**The two runs failed in opposite directions, and together they locate the boundary precisely.**

- **Run 1:** friction recorded that the framework ended at "the validator exits 0" with no defined
  step for getting artifacts into a developer's hands. **This produced the handoff step, which now
  exists and works.**
- **Run 2:** the inverse. After delivery the agent was asked how build and test skills should be
  shaped, analysed *how to shape them* without first asking *whether they belonged*, wrote one,
  wired it into the run's entry file, and had begun deriving a scaffold plan before the operator
  stopped it. **Nothing in the framework would have flagged an agent that kept going.**

### Current workaround

Operator intervention, after the fact.

### Proposed solution

One paragraph, in the constitution and in the `pios` skill:

> **This framework produces the pre-development package — research, specification, proposal, handoff
> — and stops there. Development, testing and release belong to the project that receives the
> package, not to this framework.**

Plus a corollary rule in `pios-author`: **what must never be added.** "Now build it" is the natural
request after every completed run, so the boundary needs a defender in the place where changes are
made.

Also reword the on-ramp language in the handoff step, which is the specific sentence that invites the
drift.

### Alternative designs considered

| Alternative | Why rejected |
| --- | --- |
| Leave it implicit | It has already failed once, in the direction of doing more work than asked — the harder failure to notice, because it looks like helpfulness |
| Add build and test modules to the framework | A different product. It would roughly double the surface, and the two halves would have incompatible evidence standards — research grades claims, engineering grades tests |
| State it only in the skill | An operator reading the constitution to understand scope would not find it |

### Risks introduced by the change

An operator who wants build support may read the boundary as a refusal. **Mitigated by stating what
the handoff does provide** — a folder a developer or agent can open and start from — immediately
alongside what the framework does not do.

### Why the proposed solution is preferable

One paragraph prevents a class of drift that has already occurred and that no existing check would
catch. The cost is a paragraph; the cost of the alternative was a skill written and deleted.

### Backward compatibility impact

**None.**

### Files / modules affected

`framework/constitution/` · `.claude/skills/pios/SKILL.md` · `.claude/skills/pios-author/SKILL.md` ·
`framework/engine/handoff.md` (reword).

### Migration strategy

None.

### Recommendation

**Accept.**

---
---

# E · Four gate criteria that offer false binaries

### Problem statement

Four criteria present two-state choices, or evaluate at a point, that reality does not fit. In each
case a correct run must either misreport itself or record a deviation by hand.

| | Defect |
| --- | --- |
| **E1** | A user-evidence criterion offers **observed or reported**. A desk-stage finding reconstructed from regulation and statistics is **neither**, and forcing it into either is a misreport in one direction or the other |
| **E2** | A criterion counts clarifying questions as *asked and answered, or explicitly deferred* — but it is **evaluated at the checkpoint where the questions have just been asked**, so none can yet be answered |
| **E3** | A problem-ranking score multiplies frequency by severity by workaround difficulty. **As a pure product, a rare but existential problem ranks below a frequent but survivable one** — and rare-existential is exactly the class an externally imposed obligation falls into |
| **E4** | A criterion requires the build handoff to be *readable by an agent with no prior context*, but it is **evaluated at a module that runs before the handoff artifact is written** |

### Why it occurred

**E1, E3** — the criteria were written assuming the well-resourced case, where observation is
available and problems are encountered often enough for frequency to carry real signal.
**E2, E4** — the criteria are evaluated where the module ends rather than where the artifact they
describe comes into existence.

### Evidence from both runs

- **Run 2:** all four, one entry each. Each required a judgement call recorded by hand, and **a
  second run would judge each differently** — which is the definition of a criterion that is not
  doing its job.
- **Run 1:** none of the four surfaced. **That is informative rather than reassuring**: they appear
  when evidence is thin, which is the condition the framework most needs to handle correctly.

### Current workaround

Agent judgement, recorded as a deviation. Not reproducible across runs.

### Proposed solution

| | Fix |
| --- | --- |
| **E1** | Add a third state, `reconstructed`, **requiring a stated basis**. It is not a softening: it counts as `[inferred]`, never `[verified]`, and naming what it was reconstructed from is mandatory |
| **E2** | **Split the criterion.** *Asked* is evaluated at the checkpoint; *resolved or explicitly deferred* is evaluated at module close |
| **E3** | Change the aggregation so a maximal severity cannot be cancelled by low frequency — either a weighted sum, or a floor rule where any problem at maximum severity is ranked regardless of frequency. **Requires modelling before selection** |
| **E4** | Evaluate at delivery, where the artifact exists — or reword to the property that can genuinely be checked at the module |

### Alternative designs considered

- **E1:** allow `observed` with a caveat field. Rejected — it puts a reconstruction and a real
  observation in the same bucket, which is the misreport being fixed.
- **E3:** leave the formula and instruct agents to override consciously. Rejected — an override
  recorded in prose is exactly the non-reproducible judgement this item exists to remove.
- **All four:** leave as-is and document the deviations. Rejected — that is the current state, and it
  produced four hand-judged criteria in one run.

### Risks introduced by the change

**E3 is the delicate one and the reason this item is sequenced last. Changing a scoring formula
changes which problem a run selects as sharpest, and therefore what gets built.** It must be modelled
against the recorded scores of both completed runs before a formula is chosen — if the ranking
changes, the change needs a stronger argument than "the formula looked wrong".

E1 carries a smaller risk: a third state can become the default hiding place for weak evidence.
Mitigated by the mandatory basis field and by its fixed mapping to `[inferred]`.

### Why the proposed solution is preferable

Three of the four are unambiguous defects with cheap fixes. The fourth is a real design question that
deserves modelling rather than a guess — which is why it is proposed as **Modify** rather than
**Accept**.

### Backward compatibility impact

**E1, E2, E4 are additive.** **E3 changes rankings** — a completed run re-scored under a new formula
could select a different sharpest problem.

### Files / modules affected

Four `module.yaml` + `core/11-Quality-Gate.md` pairs — **gate parity is validator-enforced, so both
must change together** — plus the affected `core/13-Template.md` files.

### Migration strategy

**Do not re-score completed runs.** Their rankings were correct under the rules in force when they
ran, and re-scoring would rewrite conclusions that downstream artifacts already depend on. Note the
formula change and its effective date.

### Recommendation

**Accept E1, E2, E4. Modify E3** — adopt the intent, defer the formula until it has been modelled
against both runs' recorded scores.

---
---

# F · Record operator-confirmed value

### Problem statement

`friction_log` records where the framework **obstructed** a run. **Nothing records which of its
mechanisms an operator confirmed were worth their cost.** A future author reading the state file sees
a list of things that went wrong and no signal about which properties are load-bearing.

A second, smaller defect sits in the same place: `operator_visible` cannot distinguish friction the
operator **ran into** from feedback the operator **reported afterwards**. Both are marked true.

### Why it occurred

The log was designed to surface defects, on the correct assumption that defects are what a framework
needs to hear. Confirmation of value was not modelled, because it is not friction.

### Evidence from both runs

- **Run 2:** at delivery the operator named three mechanisms unprompted as the reason the output was
  trustworthy. **All three cost real effort in every module, and all three look exactly like
  simplification candidates to someone optimising the framework.** With nowhere to record them, they
  were written into `friction_log` — the wrong log — specifically so they would not be lost.
- **Run 1:** no equivalent record exists, so whether the same mechanisms carried their weight there
  is unknown.

### Current workaround

An entry in the wrong log, framed as friction so it has somewhere to live.

### Proposed solution

A `confirmed_value` top-level key in `state-schema.yaml`: the mechanism, who confirmed it, what it
cost, and what it bought. `pios-author` reads it as a **do-not-remove list**, alongside the existing
"changes that need a stronger argument than usual" section — which is the same idea already applied
to properties the framework's authors identified, extended to properties its users identify.

Separately: split `operator_visible` into *encountered by the operator* and *reported by the
operator*, or add a field. They are different signals and currently collapse into one.

### Alternative designs considered

| Alternative | Why rejected |
| --- | --- |
| Keep using `friction_log` with a convention | Content recorded under a key that does not mean it is invisible to anything reading the key properly — the same defect this framework already logged once |
| Maintain the list in `pios-author` only | It would record what authors believe is load-bearing, not what operators found to be. The whole value is that it comes from use |

### Risks introduced by the change

**A list of untouchables ossifies the framework.** Mitigated by scoping it as a *record of
confirmation*, not a prohibition: an author may still change a confirmed mechanism, but must state
what replaces the property it was providing.

### Why the proposed solution is preferable

The framework already accepts this principle — the "stronger argument than usual" list exists for
exactly these reasons. This extends it to evidence from use rather than from design intent.

### Backward compatibility impact

**Additive key.** Existing runs simply have none.

### Files / modules affected

`framework/engine/state-schema.yaml` · `.claude/skills/pios-author/SKILL.md` ·
`framework/engine/validate-run.py` if the key is to be schema-checked.

### Migration strategy

None. One completed run holds a confirmation in `friction_log`; it can be left where it is with a
pointer, or copied across. **Recommend copying rather than moving** — the friction entry also records
that the schema had nowhere to put it, which is itself the defect.

### Recommendation

**Accept.**

---
---

# G · Template gaps, and the check that would have caught them

### Problem statement

Three separate cases where a template had no home for content the framework itself requires:

| | Gap |
| --- | --- |
| **G1** | A gate criterion requires a pre-mortem recorded before research begins. **The template has no pre-mortem section.** An agent filling every section faithfully satisfies the template and still fails the gate |
| **G2** | No home for a **finding that invalidates an earlier module's framing** without failing the current module's own gate — a common and valuable outcome with nowhere to go |
| **G3** | A persona table with one evidence column per row, which works when every row rests on a source. **When half the rows honestly have none**, the table forces either a blank that reads as an oversight or a citation that does not exist |

**The individual gaps are symptoms. The defect is that nothing checks that every gate criterion has a
place in the template where it can be satisfied.**

### Why it occurred

Templates and gate criteria are authored in the same module but as separate files, and the validator
enforces parity between `module.yaml` and the quality-gate file — **but not between either and the
template.** A criterion can therefore be added without anywhere to record its output.

### Evidence from both runs

- **Run 2:** three entries, each requiring the agent to add an unnumbered section or improvise a
  column. **Two runs would produce two different artifact shapes**, which defeats the purpose of
  having a template.
- **Run 1:** one structurally identical entry — a required artifact had no section for a property the
  operator asked about, and the template offered nowhere to put it. **Same defect class, different
  template, different run.**

### Current workaround

The agent adds sections and columns as needed. Artifacts drift apart between runs.

### Proposed solution

1. **Add the three missing homes**: a pre-mortem section; a section for findings that invalidate an
   earlier module's framing, carrying what it invalidates and whether a re-derivation is required;
   and an evidence column that permits an explicit "none — reconstructed" value rather than a blank.
2. **Add a validator check — this is the real deliverable.** Every gate criterion that requires a
   *recorded artifact* must map to a template section. Criteria that describe a property rather than
   an output are exempt and marked as such.

### Alternative designs considered

| Alternative | Why rejected |
| --- | --- |
| Fix the three gaps only | Leaves the mechanism that produced them. A fourth appears the next time a criterion is added |
| Require the template to be a superset by convention | A convention with no check is what currently exists |
| Generate templates from gate criteria | Over-engineered, and templates carry structure that no criterion requires |

### Risks introduced by the change

**The mapping may be hard to automate precisely** — criterion wording and section headings will not
always correspond mechanically. Fallback if automation proves brittle: an authoring-checklist item
plus a warning-level check rather than a failing one.

### Why the proposed solution is preferable

It fixes the class rather than three instances, and the check is cheap relative to the cost of
artifacts drifting apart across runs.

### Backward compatibility impact

**Additive.** New sections; existing artifacts remain valid.

### Files / modules affected

Three `core/13-Template.md` files · `framework/engine/validate.py` (new check) ·
`framework/AUTHORING.md` (checklist item).

### Migration strategy

None for completed runs. If the new check is introduced as failing rather than warning, **every
existing module must be brought into compliance in the same change**, or the framework validator
breaks on first run.

### Recommendation

**Accept**, with the validator check as the primary deliverable and the three sections as its first
consumers.

---
---

## Cross-cutting notes

**Only one item changes existing behaviour: E3.** Everything else is additive, and every completed
run continues to validate exactly as it does today.

**Exit code 2 is the only new external contract.** Anything consuming the run validator's exit status
needs to know that 2 means *deliverable, conditionally* and is not a failure — and, critically, is
not a success either.

**H should land before A.** A conditional-continuation mechanism designed without the principle
written down is the change in this document most likely to drift into an escape hatch, and the
drift would be invisible because each individual relaxation would look reasonable.

**Nothing in `framework/` has been modified.** The only change made to the repository during this
review is this file.

---

## Decisions taken, 2026-08-02

| Item | Decision | Status |
| --- | --- | --- |
| **H** | Accept | **Implemented** — Principle 16 |
| **A** | **Modify** — add a Research Exhaustion Report as a validator-checked precondition | **Implemented** with the safeguard |
| **B** | Accept | **Implemented** — `engine/remote-validation.md` |
| **C** | Accept | **Implemented** |
| **D** | Accept | **Implemented** |
| **E1 · E2 · E4** | Accept | **Implemented** |
| **E3** | **Defer** — model against multiple completed runs before changing the formula | **NOT implemented, deliberately.** `04-problem` is untouched |
| **F** | Accept | **Implemented** — `state.confirmed_value` |
| **G** | Accept | **Implemented** — three sections plus a reporting check |

---

## Deferred to a future revision

### E3 — the problem-scoring formula

**Accepted in intent, deferred in implementation.** A rare-but-existential problem currently ranks
below a frequent-but-survivable one, because the score is a pure product of frequency, severity and
workaround difficulty.

**Why it is not implemented:** changing the formula changes which problem a run selects as sharpest,
and therefore what gets built. **It must first be modeled against the recorded scores of multiple
completed runs.** If the ranking changes, the change needs a stronger argument than "the formula
looked wrong."

**What would unblock it:** three or more completed runs with their stage-3 scores intact, re-scored
under each candidate aggregation — a weighted sum, and a floor rule where maximum severity ranks
regardless of frequency.

### Principle I — Evidence has diminishing returns

**Proposed by the operator. Not implemented; recorded so it is not lost.**

Not every unanswered question deserves more research. The framework should eventually distinguish
three states rather than two:

| State | Meaning |
| --- | --- |
| **Resolved** | The evidence exists and was obtained |
| **Resolvable with additional work** | The evidence exists and has not been obtained. **This is a gap** |
| **Currently unknowable** | No available method reaches it. **This is a finding** |

**The third category is the point.** Treating an unknowable question as a gap produces a run that
keeps searching, reports failure, and never says the useful thing — which is that the question is
not answerable by this method, and here is what would answer it.

**Partially addressed already.** `remote-validation.md` distinguishes the second from the third for
questions needing customer contact, and `conditional_continuation` handles the case where a gate
depends on one. **What is missing is the general rule**: every open question carrying one of the
three states, so a reader can tell at a glance which are waiting on work and which are waiting on
access.

**Where it would go:** `state.open_questions` gains the state field; `evidence-policy.md` defines
the three; the modules' question sections adopt it. Deferred because it touches every module's
question handling and should be designed once rather than accreted.

### Run versioning — validate a run against the framework it was run under

**Proposed by the operator when deciding the migration question. Not implemented; recorded so it is
not lost.**

**The decision that produced it:** the earlier of the two completed runs improvised a conditional
state before one existed, and marked the *downstream* modules `conditional_pass` rather than the
*failing gate*. Under the semantics defined by item A that is inverted, so the run now reports four
non-conformances where it previously reported one.

**The decision taken: leave it as written.** A completed run is an immutable historical record. It
shows what the framework looked like at the time, what its limitations were, what workaround was
necessary, and why the change was later made — and that history is worth more than a clean validator
run. **Previous research is never rewritten to satisfy a newer validator.**

**The consequence to solve:** an old run reporting non-conformances is acceptable only while someone
can tell that they result from framework evolution rather than project defects. Today nothing in the
run says which framework produced it, so that distinction lives in a person's memory.

**What was proposed:** metadata rather than migration — `framework_version` and `run_version`
recorded in `state.yaml` at run start, and a `validation_profile` letting `validate-run.py`
distinguish two questions it currently conflates:

| Question | Answer today |
| --- | --- |
| Was this run valid under the framework that produced it? | Cannot be asked |
| Would this run be valid under the framework as it now stands? | The only question asked |

**Why it is deferred:** it needs a version identifier that is meaningful. A commit hash is exact and
unreadable; a hand-maintained semantic version drifts from what is on disk within a few changes. The
identifier has to be decided before the fields are added, or the metadata records something nobody
can resolve later. **This is the design work that unblocks it.**

**Interim position, which costs nothing:** the non-conformance is explained in this document and the
run is untouched. Any reader who reaches a confusing validator result on an old run lands here.

---

> **Review Principle**
>
> A framework change proposed from a single run is an anecdote. Proposed from two runs that failed
> the same way for different reasons, it is a design defect.
>
> The items above are ordered by that distinction, not by how easy they are to implement.
