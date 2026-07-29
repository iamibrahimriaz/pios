# Product Intelligence OS

> **An AI-first Product Research & Discovery Framework that transforms ideas into implementation-ready product blueprints.**

---

# What is Product Intelligence OS?

Product Intelligence OS (PIOS) is an open, structured framework that trains AI agents to perform professional product research.

Instead of giving AI dozens of custom prompts for every new idea, Product Intelligence OS teaches AI **how to think**, **how to research**, **how to evaluate**, and **how to deliver**.

The goal is simple:

> Give AI an idea.

> Receive a complete product blueprint.

---

# Why This Project Exists

Modern AI can generate documents.

Great product managers generate decisions.

Most AI assistants can write.

Few AI assistants know **how to discover products**.

Product Intelligence OS bridges that gap.

It provides a repeatable methodology that teaches AI to work like an experienced:

- Product Manager
- Product Researcher
- Business Analyst
- UX Strategist
- Solution Architect
- Technical Consultant

Every research project follows the same principles, standards, and quality gates.

---

# Vision

Build the world's best open framework for AI-driven product discovery.

Every idea should become:

- Validated
- Well researched
- User focused
- Technically feasible
- Business viable
- AI ready
- Implementation ready

without requiring dozens of custom prompts.

---

# Mission

Create a reusable knowledge framework that enables AI to independently perform professional product research using standardized methodologies, structured reasoning, quality evaluation, and continuous learning.

---

# Philosophy

Product Intelligence OS is not a prompt library.

It is not a documentation repository.

It is not a collection of templates.

It is a learning system.

Every module teaches AI:

- Why something matters
- How experts think
- Which questions to ask
- Which mistakes to avoid
- How to evaluate itself
- How to improve continuously

The objective is not better documents.

The objective is better decisions.

---

# What Can It Do?

Starting from only a product idea:

```
Idea

↓

Understand

↓

Research

↓

Analyze

↓

Challenge Assumptions

↓

Discover Opportunities

↓

Validate

↓

Design

↓

Review

↓

Deliver
```

Product Intelligence OS enables AI to generate:

- Product Vision
- Market Research
- Competitor Analysis
- User Research
- Problem Analysis
- Solution Exploration
- Business Strategy
- Product Requirements
- Feature Specifications
- UX Strategy
- AI Opportunities
- Technical Research
- Architecture
- Database Design
- API Design
- Security Analysis
- Scalability Planning
- Pricing Strategy
- Product Roadmap
- Risk Analysis
- Validation Plan
- Executive Summary

Everything required before development begins.

---

# Repository Structure

```
product-intelligence-os/

AGENTS.md                 how an agent executes a run — start here

framework/                ships to users; read-only during a run

  constitution/           governing principles — how to think

  engine/                 how a run executes
    run-order.yaml          module sequence and stages
    gates.yaml              how a module passes or fails
    evidence-policy.md      verified / inferred / assumption
    state-schema.yaml       the carry-forward project state
    review-loop.md          the four-pass self review

  deliverables/           THE OUTPUT SPECIFICATION
    manifest.yaml           15 artifacts with acceptance criteria

  modules/                the 14 lifecycle domains
    01-idea/  02-market/  03-user/  04-problem/  05-competition/
    06-business/  07-strategy/  08-product/  09-technology/
    10-execution/  11-growth/  12-metrics/  13-operations/
    14-ai-systems/

  packs/                  optional vertical knowledge (healthcare, fintech, ...)

projects/<slug>/          one run — state.yaml, research/, deliverables/

examples/                 completed reference runs
```

Each module contains four layers:

| Layer | Teaches | Read by |
| --- | --- | --- |
| `core/` | How to think — frameworks, workflow, questions, quality gates | the agent |
| `knowledge/` | What to know — concepts, terminology, methods | the agent |
| `resources/` | Templates, examples, anti-examples | the agent |
| `learn/` | Curriculum — why it matters, objectives, reflection | humans |

Every module also carries a `module.yaml` — its machine-readable contract:
what it depends on, what it consumes, what it produces, and the gate it must
pass before the run continues.

---

# Running It

An agent is pointed at this repository and given one idea. It reads
`AGENTS.md`, works through the modules in the order defined by
`framework/engine/run-order.yaml`, and emits the artifact set specified in
`framework/deliverables/manifest.yaml`.

```
Input:   one idea, loosely described
Process: 14 modules, gated, evidence-bound
Output:  a build-ready blueprint in projects/<slug>/deliverables/
```

The run produces, among others: a Research Dossier, Problem Validation, a full
PRD, Feature Spec, Data Model, API Contract, Architecture, UX Flows, Roadmap,
Risks and Assumptions, Success Metrics, and a **Build Handoff** — a standalone
file an engineering team or coding agent can start building from with no other
context.

---

# The Evidence Rule

Every factual claim in every output carries exactly one tag:

- `[verified: <source>]` — checked against a named, retrievable source
- `[inferred: <basis>]` — reasoned from something verified
- `[assumption: needs validation]` — believed, not established

**An assumption is never smoothed into a fact.** A blueprint that openly states
what it assumed is useful. One that silently asserts it is a liability. See
`framework/engine/evidence-policy.md`.

---

# Research Lifecycle

Every project follows the same lifecycle.

```
Receive Idea

↓

Clarify Requirements

↓

Research Market

↓

Research Competitors

↓

Research Users

↓

Discover Problems

↓

Generate Solutions

↓

Validate Business

↓

Design Product

↓

Research Technology

↓

Design Architecture

↓

Design Database

↓

Design APIs

↓

Evaluate Security

↓

Plan Scalability

↓

Validate Findings

↓

Generate Documentation

↓

Review Quality

↓

Deliver Final Blueprint
```

No steps are skipped.

---

# Design Principles

Every research project should be:

- Evidence based
- User centered
- Business driven
- Technology aware
- AI first
- Practical
- Maintainable
- Reusable
- Explainable
- Reviewable

---

# Quality Standards

Every output should answer:

- Is the problem real?
- Is the research complete?
- Are assumptions clearly identified?
- Are sources trustworthy?
- Is the recommendation justified?
- Are alternatives explored?
- Is the solution technically feasible?
- Is it commercially viable?
- Can another AI reproduce the work?

If not,

the research is incomplete.

---

# Who Is This For?

This framework is designed for:

- AI Agents
- Founders
- Product Managers
- Startup Teams
- Software Engineers
- Researchers
- Consultants
- UX Designers
- Business Analysts

Anyone responsible for turning ideas into successful products.

---

# Continuous Learning

Every completed project should improve Product Intelligence OS.

Every lesson learned becomes documentation.

Every mistake becomes a best practice.

Every successful product strengthens the framework.

The framework should continuously evolve as more products are researched.

---

# Long-Term Vision

Imagine an AI that receives only this:

> "Build an AI-powered Pharmacy Management System."

Without additional prompts, it should be able to:

- Ask intelligent questions
- Discover unknown requirements
- Research the market
- Compare competitors
- Analyze users
- Validate opportunities
- Design the product
- Recommend technologies
- Create implementation-ready documentation
- Review its own work
- Suggest future improvements

That is the purpose of Product Intelligence OS.

---

# Contributing

Product Intelligence OS is designed as a living knowledge system.

Contributions should improve:

- Research quality
- Decision quality
- AI reasoning
- Documentation standards
- Templates
- Playbooks
- Examples
- Evaluation methods

Every contribution should make future research better.

---

# Guiding Principle

> **Don't teach AI what to write.**
>
> **Teach AI how to think.**

Everything in this repository exists to make AI a better product researcher, strategist, and decision-maker.

---

## Future Vision

Product Intelligence OS aims to become the open standard for AI-powered product discovery.

A framework where one well-described idea can become a complete, validated, implementation-ready product blueprint.

Not through prompts.

Through structured intelligence.
