# Framework defects surfaced by one completed run

**Date:** 2026-09-09
**Source:** `state.friction_log` from Run 1 — nine entries, all read — plus one defect found by an operator-requested audit that the friction log did not contain
**Produced by:** Claude Opus 5 (1M context), Claude Code. **Grounded in a completed run, not reasoned from documentation.**

> **No project content appears in this document.** The run is referred to as Run 1. No product, market, sector, customer, competitor, vendor, figure or recognizable idea is named anywhere, and every defect is stated so that it stands without the run in front of you.

---

## Decision summary

| # | Defect | Owner | Blast radius | Recommendation | Status |
| --- | --- | --- | --- | --- | --- |
| **D1** | The delivery surface is asked at `01-idea` and consumed by nothing | `08-product`, manifest | **Cross-module** | **Adopt** | ✅ Implemented |
| **D2** | A `07-strategy` re-entry silently stales every module after it | `run-order`, engine | **Cross-module** | **Adopt** | ✅ Implemented |
| **D3** | `state-schema` version default drifted from the manifest | engine | One file | **Adopt** | ✅ Implemented |
| **D4** | `02-market` may record "the category is unnamed" and search it once | `02-market` gate | One module | **Adopt** | ✅ Implemented |
| **D5** | No pass asks whether a cited source contradicts a conclusion drawn from it | `review-loop` | **Every module** | **Adopt** | ✅ Implemented |
| **D6** | `01-idea`'s Context table has no row for a data subject who is neither user nor buyer | `01-idea` template | One module, wide effect | **Adopt** | ✅ Implemented |
| **D7** | A load-bearing external figure needs only one read | engine, evidence policy | **Every module** | **Adopt as a note** | ✅ Implemented |
| **D8** | The equivalence argument's ordering is unverifiable after the fact | engine | Validation tests | **Adopt** | ✅ Implemented |
| **D9** | `state.yaml` is one growing file with no integrity check | engine, `AGENTS.md` | **Whole run** | **Adopt guidance; structural fix needs design** | ◐ Partial |
| **D10** | `01-idea` records `verdict: fail` on every correct first attempt | `01-idea`, gate vocabulary | **Gate vocabulary** | ### **Maintainer decision — not implemented** | ⬜ Proposed |

**Nine of ten adopted. One left for the maintainer because it touches a load-bearing vocabulary.**

**Manifest `version: 4 → 5`.** One new artifact carries `since: 5`; one new check is gated on it. **No completed run is affected by any change here.**

---

## D1 — The delivery surface is asked and consumed by nothing

**What changes.** `delivery_surface` becomes a named output of `01-idea`; `08-product` depends on and consumes it; a new gate criterion requires the interface and non-functional requirements the surface implies, **or one sentence recording that it implies none.** A new conditional artifact, `interface-requirements`, carries them.

**Why.** `01-idea`'s gate makes the operator name the surface. Nothing downstream read it:

| Checked | Result |
| --- | --- |
| Modules declaring it in `consumes` | **0 of 14** |
| Gate criteria mentioning accessibility, layout, browser support, performance budgets or design | ### **0** |
| Deliverable acceptance criteria covering any of them | **1 of 21** |

**A run can name a visual surface at the first gate and hand a builder a specification containing no interaction states beyond the happy path, no layout behavior at any width, no accessibility target, no performance budget and no supported-client policy — passing all fourteen gates and every structural check.**

**Two things hid it.** `AGENTS.md` asserts that six later modules *"read it as settled context"* — **no module definition implemented that.** And `08-product/learn/20-Future-Improvements.md` already recorded the cause: *"Non-functional requirements have no home… they land in module 09 as architecture concerns, which is too late for several of them."* **A limitation recorded in `learn/` is skipped by every executing agent.** It described the defect indefinitely without preventing it.

**Blast radius.** Cross-module: `01-idea`, `03-user`, `08-product`, the manifest, a template, a knowledge file, `AGENTS.md`.

**The boundary this had to respect.** `constitution/core/00-Purpose.md` ends the framework at the pre-development package, and the authoring skill forbids QA methods. Interface quality is where specification and process blur most easily, so the line is drawn explicitly in the criterion, the template and the knowledge file: **a conformance target is in scope; a pipeline scan is not. A budget with a measurement condition is in scope; a test suite is not.** An acceptance criterion states it: *"every entry is a requirement rather than a verification method."*

**The judgement call.** The artifact is owed **unless** the surface is unambiguously view-less — `api`, `cli`, `library`, `sdk`, `batch`, `daemon`, `service`, `headless`, `protocol`. **`other` and blank trigger it.** The errors are not symmetric: a false positive costs one sentence; a false negative is the defect. **Testing against a real run found the surface recorded as `other` for a product that plainly had one.**

**What it cannot do.** It cannot detect a lazy *"not applicable"*. **It prevents the silent omission, which was the actual failure** — and a false "not applicable" is a sentence somebody wrote and can be challenged.

---

## D2 — A strategy re-entry silently stales every module after it

**What changes.** `state.run.module_completions` (module → date) and `state.outputs.chosen_approach.decided_at`. `validate-run.py` fails when any module downstream of `07-strategy` in `run-order.yaml` carries a completion date earlier than `decided_at`.

**Why.** `07-strategy` can be re-entered and return a different chosen option. **`run-order.yaml` has no concept of downstream invalidation.** No field recorded when the direction was decided, none recorded when each module ran, and nothing compared them.

> **Stale outputs do not look wrong.** They are complete, internally consistent, and pass every gate — they describe a product the run has abandoned. **A run can carry a full specification of a discarded option into the build handoff, the one artifact somebody builds from without re-reading the research.**

**This is worse than ordinary staleness** because a re-entry is triggered by a *failed validation* — the run is already in the state where its author is looking elsewhere.

**Blast radius.** Cross-module; every module after `07-strategy`.

**Backwards compatible by construction.** A run recording neither field gets a **note**, and only when `superseded_option` is set — so it appears exactly where the risk is real. **Negative-tested:** with two downstream modules dated before the decision and one after, the check names the two.

---

## D3 — The schema's version default drifted from the manifest

**What changes.** The default is corrected, and a structural check in `validate.py` requires it to equal the manifest's version.

**Why.** The field is documented as being set *"from that file's `version` when the run is created"* — that file being the manifest. **It was a hardcoded literal and it drifted.** `validate-run.py` derives the artifact folder layout from it, so a run that wrote the correct layout was reported as **missing every artifact**, with remediation text telling the operator to move them the wrong way. **Nothing compared the two numbers.**

**Blast radius.** One file; the failure it produced was total and misdirected.

---

## D4 — A module may record "this category is unnamed" and then search it once

**What changes.** A sixth gate criterion on `02-market`: **search vocabulary recorded, and where the category has no established name, at least two independent vocabularies were searched.**

**Why.** A module can state *"this category has no established name"* as a finding and, sections later, present a competitive field and a price anchor derived from a single vocabulary. **Both facts sit in the same document and no criterion connects them.** Every individual claim is sourced and dated, the gate passes, and the market analysis is wrong about who the competitors are — for a reason the document already contained.

**What makes a second vocabulary independent** is specified in the criterion: not a synonym, but **a different mental model taken from a different party** — what a buyer would type, what a vendor calls itself, what an adjacent discipline calls it, what the thing substitutes for. **Two vocabularies returning the same set is itself a finding.**

**Blast radius.** One module — with everything downstream of a market definition behind it.

---

## D5 — No pass asks whether a cited source contradicts a conclusion drawn from it

**What changes.** A question added to the adversarial pass of `engine/review-loop.md`, with the method for running it.

**Why.** A source can be cited for one narrow fact — a count, a price, a date — while a conclusion is drawn about the same subject **that the source's own description of itself falsifies.** The citation is real, the figure is correct, and the conclusion is wrong. **Pass 2 checks that a claim was sourced; it does not read the source back against the conclusion.**

**In Run 1 this cost a withdrawn wedge, a changed central problem, and a full re-derivation one module later. It was caught because an unrelated module happened to re-read the same source.**

**Blast radius.** Every module. **Mechanical cost: one question in a pass that already runs.**

---

## D6 — No row for a data subject who is neither user nor buyer

**What changes.** A row in `01-idea`'s Context table, a note explaining why it is not a user row, and a checklist line.

**Why.** Some products process data about a person who **never sees the product, never pays for it, and is not a user in any sense** — the party measured by a monitoring tool, the patient in a clinical system, the applicant in a hiring tool. **Their consent is frequently the entire supply of the thing being sold, and their interests are the ones nobody in the purchase conversation represents.**

**Before this, they were written into a spare User row and explained in prose, where no gate reads it.** A different run would have put them elsewhere or omitted them, **and nothing would notice either way.**

**Blast radius.** One template row, with wide effect: it reaches `03-user`, the privacy posture, and any consent design.

---

## D7 — A load-bearing external figure needs only one read

**What changes.** A `corroborated_by` field on evidence entries, and a `validate-run.py` **note** listing load-bearing verified claims sourced to an external page that carry no second read.

**Why.** `evidence-policy.md` requires a source and a date. **It does not require a load-bearing figure to be read twice**, and a single automated read of a pricing or marketing page satisfies every check the framework performs. **A misread is indistinguishable from a correct read.** In Run 1 one such figure was wrong by an order of magnitude and was caught **only because the misread values contradicted each other**; a coherent-looking misread would have propagated.

**Recommended as a note, not a failure.** Whether a claim is a *figure* is a judgement no validator can make from a string, and failing every long-form external claim would train operators to ignore the check.

**Blast radius.** Every module that cites an external page.

---

## D8 — The equivalence argument's ordering is unverifiable after the fact

**What changes.** `recorded_before: execution` is required on a substituted instrument, mirroring the field validation tests already carry. `validate-run.py` fails a substitution without it, **gated on manifest v5.**

**Why.** `engine/instrument-substitution.md` requires the equivalence argument to be written **before** the substitute runs. **Nothing enforced or detected the ordering.** An agent that collects first and argues equivalence afterwards produces a document indistinguishable from one that did it correctly — **and the argument is then silently shaped by what was found, which is the one thing the ordering exists to prevent.** The checklist item existed and was unverifiable.

**Requiring the field forces the argument to be a separate, earlier state write rather than prose inside the write-up.**

**Blast radius.** Every substituted validation test — which `instrument-substitution.md` itself calls *"the common case, not the exception."*

---

## D9 — `state.yaml` is one growing file with no integrity check

**Adopted, in part.** `AGENTS.md` gains the editing discipline: **anchor on something provably unique, and re-parse and re-count after every write.**

**Why.** The file is the only copy of the audit trail, it passes four thousand lines on a full run, and there is no history behind it. **A bad anchor produces valid YAML that is missing half the run** — nothing downstream notices until a gate reads something no longer there.

**What is not proposed, and why.** The structural fix — splitting state, or a checksum, or a write-through journal — **is a design question with real trade-offs the maintainer should own.** Every option costs something the single-file design currently gives for free: one place to read, one file to diff, one file to hand to a validator.

**Blast radius.** Whole run. **Recommendation: adopt the guidance now; treat the structural fix as a separate proposal.**

---

## D10 — `01-idea` records `verdict: fail` on every correct first attempt

### **Not implemented. Maintainer decision.**

**The defect.** Four of `01-idea`'s criteria can only be satisfied by operator answers, and **the gate is evaluated before the frame checkpoint where those answers are requested.** A correctly run module 01 therefore records `verdict: fail` on its first attempt unless the operator's opening message happened to contain a jurisdiction, a payer, a surface and a differentiation stance.

**The consequence is small but real: the first entry in every run's audit trail is a failure that is the expected and correct state.** `decision_dependent_failure` already prevents it consuming an attempt, so nothing is broken — **the word simply reads as a defect to anyone scanning `state.yaml`.**

**Why it is not implemented.** The obvious fix is a fourth gate verdict — `pending_operator` alongside `pass | fail | conditional_pass`. **The authoring skill flags controlled vocabularies as load-bearing, and adding a verdict that means "not really failed" is exactly the shape of change that erodes one.** Once a gate can resolve to something that is neither pass nor fail, the pressure to use it elsewhere is immediate.

**Recommendation.** Either accept the cosmetic cost and document it where someone reading `state.yaml` will see it, **or** change the evaluation order so module 01's gate runs after the frame checkpoint. **The second is the smaller change to the vocabulary and the larger one to `run-order.yaml`.** Both are yours.

---

## Not proposed

**Nothing in the friction log was rejected.** All nine entries qualified under the contribution table — each was a gate, template, check or engine behavior that would affect any operator, not a preference about one run.

**One item in this document did not come from the friction log at all.** **D1 was found by an operator-requested audit**, not recorded as friction during the run — **because the agent did not notice the absence.** That is the friction log's own limitation working exactly as the contribution guidance describes it: **the log records where the framework blocked the agent, and cannot record where the framework failed to ask.**

---

## Verification

```
python3 framework/engine/validate.py            # all structural checks pass
python3 framework/engine/validate-run.py <run>  # unaffected: notes, not failures
```

**Every new check was negative-tested** — deliberately made to fail on a mutated copy, then confirmed to pass on the unmutated one. **A gate that never fails is not a gate.**

**A mechanism was added along the way.** Adding an artifact retroactively failed a completed run, which is the property `state.framework_version` exists to protect. **Artifacts may now declare `since: <manifest version>`**, generalizing the single hardcoded `PHASES_ERA = 4` constant. It also exposed a latent bug: `required = [a for a in artifacts if a.get("required")]` treated the string `"conditional"` as truthy, **so any conditional artifact would have been demanded of every run.** It had never surfaced because none existed in `artifacts` before. **Conditions are now evaluated in both places.**

---

## Note on how this was produced

**This work was carried out under `/pios:author`, not `/pios:learn`.** The two conflict on one point: `/pios:learn` forbids modifying `framework/` *"not even temporarily to test it"* and produces a proposal only, while `/pios:author` exists to modify the framework deliberately.

**The framework files were changed on this machine.** That is `author`'s remit and the operator is the maintainer, **but a reader of this document should know it is a record of changes already made, not a request to make them.**
