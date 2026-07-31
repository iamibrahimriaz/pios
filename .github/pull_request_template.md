## What this changes

«One or two sentences. What is different after this is merged?»

## The defect it fixes

«Which limitation of the framework does this address? State it so it stands on
its own — a reviewer should be able to judge it without knowing which project
revealed it.»

## What it could break

«Every gate, criterion and template is load-bearing for something downstream.
Say what you considered. "Nothing" is an acceptable answer if you looked.»

---

## Checks

- [ ] `python3 framework/engine/validate.py` exits 0
- [ ] **No run content attached or committed.** Nothing from `projects/` or
      `examples/`, no client name, real price, named customer or market figure,
      and no text lifted from a deliverable
- [ ] Content is in the right layer — an operating instruction is in `core/`,
      not `learn/`
- [ ] Gate criteria match between `module.yaml` and `core/11-Quality-Gate.md`
- [ ] Anti-examples were written from scratch, not harvested from a real run
- [ ] American spelling

See [CONTRIBUTING.md](../CONTRIBUTING.md).
