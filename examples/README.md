# Examples

Completed reference runs. Each is a real end-to-end pass through the framework —
the same fifteen artifacts a run produces for you, with the evidence tags,
open assumptions and gate verdicts left intact.

```
examples/<slug>/
  state.yaml        the run's memory — evidence log, assumptions, decisions
  deliverables/     the artifact set, exactly as delivered
  NOTES.md          what the run exposed about the framework itself
```

---

## Status: none yet

This directory is empty on purpose rather than by oversight, and the honest
position is worth stating plainly: **the framework has not yet been run end to
end.** Everything in this repository has been verified structurally — 21 checks
in `framework/engine/validate.py`, all passing — and nothing has been verified
by use.

A reference run is the next piece of work. When it lands here it will include
its failures: gates that were hard to pass, templates that were awkward to fill,
and any point where the method needed changing. A reference run that shows only
success would be the least useful artifact this project could publish.

---

## What an example is for

**To see the output before committing hours to a run.** Fifteen artifacts is a
large promise. Reading one real set answers "is this worth my time" faster than
any description.

**To calibrate.** The artifacts show what "enough evidence" looks like in
practice, how much an honest `[assumption]` density is, and what a run reporting
low confidence reads like.

**To prove the framework can say no.** The most valuable example is one where
the run recommends *do not build* — or where a cost check fails and the run
regresses. Those are the outcomes that distinguish this from a document
generator, and they are the ones worth publishing first.

---

## Contributing a run

If you complete a run and are willing to share it, it is welcome — especially in
a domain unlike the ones already here.

Before opening a pull request:

- Remove anything confidential. Real market research often is
- Keep the evidence tags, the open assumptions and the gate verdicts intact.
  A cleaned-up run teaches nothing
- Add `NOTES.md` saying what the framework got wrong, where you had to work
  around it, and which module cost the most effort
- Run `python3 framework/engine/validate-run.py examples/<slug>`

See [CONTRIBUTING.md](../CONTRIBUTING.md).
