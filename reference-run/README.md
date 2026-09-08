# Reference run

**One published PIOS run, so you can read the output before deciding to spend hours
producing your own.**

> **Status: not yet produced.** This directory is the home for it and the rules it has to
> meet. Until a run lands here, the only way to see PIOS output is to make some.

---

## Why this exists at all

Everything else in this repository describes the method. None of it shows the result. A
reader deciding whether PIOS is worth several sessions has to take the artifact set on
faith, and that is the wrong thing to ask of anyone.

The output is fifteen documents. Fifteen documents is a claim. One readable run is evidence.

---

## Why it does not breach the privacy rule

**Runs are private.** `projects/` and `examples/` are gitignored, a structural check fails
the build if run content is tracked there, and a separate CI step re-checks it. None of that
changes, and none of it is weakened by what lives here.

The rule protects **someone's research** — their market, their named customers, their pricing,
their unreleased strategy. A reference run has no such owner:

| | Real run | Reference run |
| --- | --- | --- |
| The operator | A real person or company | **Invented** |
| The market | Real | **Real** — otherwise the research is worthless |
| The strategy | Theirs, unreleased | Nobody's |
| Published | **Never** | **Deliberately** |

The market has to be real. A run against an invented market would have no retrievable sources,
every claim would tag `[assumption]`, and the artifact set would demonstrate nothing except the
templates.

---

## Rules a run in here has to meet

**The operator is invented, and the file says so.** Not anonymised, not a real company with
the name filed off. Invented. Anonymising a real run is how a real run gets published by
accident.

**The verdict is whatever the run reached.** Decided before the run starts, not after.
A reference run that reached *do not build* is published as it stands — it is the better
demonstration, because it proves the gates bite. Re-running until the answer flatters the
framework is the exact dishonesty the framework exists to prevent, and doing it here would
discredit every rule in `framework/`.

**It is dated, and read as a snapshot.** Market claims go stale. The run states when it was
produced and is not maintained against a moving market. It demonstrates the method, not the
state of an industry.

**It passes `validate-run.py`.** A reference run that would not pass the framework's own
run linter teaches the wrong thing. CI checks this whenever a run is present here.

**Defects it surfaces are fixed in the framework, not papered over in the run.** Producing
this is the first real use PIOS has had. Whatever breaks is a contribution — see
[CONTRIBUTING.md](../CONTRIBUTING.md).

---

## Layout

```
reference-run/
  README.md            this file
  <slug>/              the run, exactly as PIOS produced it
    DECISION.md
    CLAUDE.md
    state.yaml
    deliverables/
    phases/
    proposal/
    presentation/
```

> **Show the output, or the artifact set is a promise.**
