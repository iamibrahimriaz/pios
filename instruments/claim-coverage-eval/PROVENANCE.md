# Provenance

**Where this instrument came from, what the originating run concluded, and where the boundary
between the two is drawn.**

**Read this as history. Nothing here is an assumption the instrument carries.**

---

## Origin

This evaluation was built on **2026-08-13** inside a PIOS product research run
(`projects/briefly-chrome-extension`), as a substitute for a validation test the operator could not
personally perform. It was extracted afterwards because **the corpus and method outlived the
decision they were built to inform**.

The originating run's own artifacts remain in that project directory:
`validation/M0.5-substitute-design.md` (the pre-registration) and `validation/M0.5-RESULT.md` (the
result as it bore on that product).

---

## What the originating run concluded

**Recorded for honesty about where the thresholds came from. It is not a claim about your project.**

The run assessed a browser-extension concept and reached **STOP — do not build**, on five grounds
established before this evaluation existed: the core capability was free and shipped natively by the
browser; the most prominent independent competitor charged nothing; **zero of 90 coded evidence items
stated a consequence of the problem**; no defensible differentiation was found; and the modelled
economics ran **−$31/month to +$84/month against ~250 hours of build**, with payback never reached
in the low and middle cases.

**This evaluation then removed the run's last surviving cheap option.** That option's entire appeal
was that it contained no model — which took running cost from ~$40–94/month to about $2/month. **Its
selector is arm 2, and arm 2 recovered 28% of the authors' claims.** The 68% figure requires the
model whose cost the option existed to eliminate.

> **The finding that transferred is not "that product should not be built." It is: a mechanical
> extractive selector may be far weaker than it looks, and the cheap-option-versus-capable-option
> trade must be measured rather than assumed.**

---

## The separation boundary

### Travels with the instrument

The measure `C_a` · the two-arm model-vs-mechanical design · externally-authored ground truth as the
contamination fix · the blind-selection directory layout · the strict binary grading rule ·
verbatim-containment and normalization testing · the self-graded-arm cap · pre-registration
discipline (floors and thresholds before collection) · the 12-document corpus and its 50 claims ·
the finding that TextRank selects methods boilerplate on technical prose.

### Left behind — deliberately

Any product definition, target audience, pricing, channel, or market hypothesis. The originating
run's verdict. Its cost model, its competitor set, its jurisdiction, and its business case.

**None of these appear anywhere in `corpus/`, `selections/`, `results/` or `scripts/`.**

### Inherited but **must be re-derived**

> **The ≥70% / 50–69% / <50% bands.**

They encode one product's tolerance — *if three claims in ten are missing, the reader must open the
document anyway.* **They are reported by `verify_and_score.py` with an explicit warning, and they
are the most likely way this asset gets misused.** Set your own, in advance, and write them down
before you look at a result.

---

## Status of the originating run

**Closed. Product decision: STOP. Commercial validation: not established. Development authorized:
false.**

**This instrument does not reopen it**, does not propose a product direction, and does not
constitute a specification, plan, or authorization to build anything.
