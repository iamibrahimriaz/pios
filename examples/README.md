# Examples

**This directory is local. Nothing in it is ever committed or published.**

`.gitignore` excludes everything here except this file. That is deliberate and it
is not going to change.

---

## Why runs stay private

A completed run is not a demo. It carries the market research someone paid for,
the customers they named, the price they intend to charge, and the strategy they
have not announced yet. It is the most sensitive document the framework produces,
which is exactly why it is the one people are most tempted to publish.

The framework is open. **What people put through it is theirs.**

This holds for your own runs too. A private project of yours is still a private
project, and the moment one run gets published "just as an example", the boundary
stops meaning anything.

---

## What this directory is for

```
examples/<slug>/
  state.yaml        the run's memory — evidence log, assumptions, decisions
  deliverables/     the artifact set, exactly as delivered
  NOTES.md          what the run exposed about the framework itself
```

Keep finished runs here to learn from, compare against each other, and calibrate.
Reading three of your own runs side by side is what surfaces the patterns a single
run cannot show — that your market sizing is always optimistic, or that module 09
is where every run stalls.

`NOTES.md` is the part that matters most. Write it while the run is fresh: which
gate was hard to pass honestly, which template was awkward to fill, where you
worked around the method instead of following it.

---

## How a run improves the framework

Runs teach; runs do not ship. The lesson crosses the boundary, the run never does.

**Extract the defect, discard the project.** A framework change must stand on its
own for someone in an unrelated domain. If the reasoning only makes sense with the
run in front of you, it is not a framework change yet.

| Do not write | Write |
| --- | --- |
| "In the Acme run, the pricing gate failed" | "The pricing gate cannot be passed when the buyer and the user are different people" |
| "Module 05 missed Shopify" | "05-competition's gate does not force the incumbent platform to be named" |

**Never carry across:** a client or company name, a real price, a named customer,
a market size figure, a screenshot, or a sentence lifted from a deliverable.
Anti-examples in `resources/` are written from scratch, not harvested from someone
else's run.

Then make the change deliberately with `/pios:author`, and let the commit message
explain the defect — not the project that revealed it.

> **Learn from every run. Publish none of them.**
