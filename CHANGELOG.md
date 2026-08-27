# Changelog

All notable changes to Product Intelligence OS are recorded here.

This project uses [semantic versioning](https://semver.org). For a framework rather than a
program, the versions mean:

| Bump | Means |
| --- | --- |
| **major** | A completed run written against the previous version would no longer validate |
| **minor** | New modules, gates, artifacts or checks. Existing runs stay valid |
| **patch** | Corrections, clarifications, documentation |

**`state.version` records the schema era a run was written against.** Checks introduced after
a run was produced are reported as out of scope for it rather than failing it. A run is a
historical record; a validator that grew later must not be able to fail one retroactively.

---

## [0.1.0] — Unreleased

First public release. The framework is complete and structurally validated; **no claim about
outcomes has been tested by a published run.**

### Added

- **14 lifecycle modules**, four layers each — `core/` (how to think), `knowledge/` (what to
  know), `resources/` (templates and anti-examples), `learn/` (human curriculum).
- **17 deliverable templates**, 15 required, grouped into `00-decision/` · `01-research/` ·
  `02-product/` · `03-technical/` · `04-delivery/`.
- **Five completion artifacts**, one per audience — decision report, HTML proposal,
  engineering kickoff deck, phase board, AI entry file. Produced on every completed run,
  including one that concludes *do not build*.
- **The evidence policy** — every factual claim carries exactly one tag: `verified`,
  `inferred`, or `assumption`. An untagged claim is a defect.
- **Seven universal gates (U1–U7)** applied to every module on top of its own criteria.
- **Six failure classes**, so a shortfall reports what it actually is rather than a single
  undifferentiated "did not pass".
- **Six validation outcomes**, keeping `inconclusive` and `blocked` distinct from `fail`.
- `validate.py` — 40 structural checks on the framework.
- `validate-run.py` — lints a finished run for deliverability.
- `/pios` and `/pios-author` skills.
- **Installable as a Claude Code plugin.** `.claude-plugin/plugin.json` and
  `marketplace.json`; the framework resolves from `$CLAUDE_PLUGIN_ROOT` and runs land in
  `./pios/<slug>/` in the operator's own project.
- `gemini-extension.json` and `package.json` for Gemini CLI and npm distribution.

### Framework portability

- Framework detection now checks **plugin mode first**, then in-repo, then `PIOS_HOME`.
- **Every framework path is written repo-relative and resolved against `<FRAMEWORK>`.** Two
  new structural checks enforce it: one rejects any non-canonical form (`./framework/`,
  `../framework/`, absolute), the other requires the resolution rule to be taught in both
  places an agent starts reading.

  Without this, an installed plugin reads gate criteria pointing at method documents that do
  not resolve from the operator's working directory — and the run continues without the
  method, reaching delivery having silently skipped the document that would have failed it.

### Known limitations

- **No reference run is published.** Runs are private and stay that way; a synthetic example
  run is the next milestone.
- `framework/packs/` — vertical knowledge packs are declared and not built.
- A full run is slow. Roughly 410k tokens of framework reading before any research begins.
