---
Title: API Authentication
Module: 09-technology
Section: knowledge/api
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Specify how a caller proves identity at the interface, and what the token carries.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 09-technology/knowledge/api/Endpoints.md
Outputs:
  - Authentication at the interface within api_contract
Related Modules:
  - 08-product
Tags:
  - Technology
  - API
  - Concept
---

# API Authentication

---

# What It Is

How a caller establishes **who it is** at the interface — the transport-level half of identity.

The security model of identity itself — factors, credential storage, session lifetime, account recovery — is
`security/Authentication.md`. This file covers the contract:

| Decision | What it settles |
| --- | --- |
| Credential form | Session cookie, bearer token, API key, signed request |
| Where it travels | Header, cookie — and the consequences for browsers and CSRF |
| What it carries | An opaque reference, or claims the server trusts without a lookup |
| Lifetime and refresh | How long it is valid and how a new one is obtained |
| Failure response | 401, distinguished from 403 — `Authorization.md` |

The claims question matters most. A token carrying permissions avoids a lookup per request and becomes **stale the moment
access changes** — which for revoked access is a security property, not an optimization detail.

---

# When It Applies

In Move 3 (Expose), as a cross-cutting property of every operation.

---

# How to Apply It Here

**Distinguish 401 from 403 consistently.** Not authenticated and not permitted are different answers, and mixing them
confuses clients and leaks information.

**State what happens when access is revoked mid-session.** If the token carries claims, revocation takes effect at expiry
unless something checks. For a clinical or financial product that delay is a real exposure.

**Separate machine callers from human ones.** An API key for an integration and a session for a person have different
lifetimes, different revocation needs and different audit entries.

**Set the lifetime from the environment.** `03-user`'s findings decide it: a shared clinical workstation needs a short session;
a personal device does not. This is a product constraint, not a default.

**Never accept credentials in a URL.** They land in logs, in browser history and in referrer headers — three places Move 4
never accounted for.

---

# Where It Misleads

**Long-lived tokens with embedded claims are adopted for convenience.** Revocation then does not work, and nobody discovers
this until someone needs to remove access urgently.

**Refresh is treated as a client concern.** It determines whether a user is signed out mid-task — which `08-product` should
have specified as behavior, and which is an edge case in the failure category.

**Authentication is implemented per endpoint.** Like authorization, it needs a single point that cannot be bypassed.
`Backend.md` treats that as a criterion for the backend choice.

**API keys are issued with no scope and no rotation.** A permanent all-access credential in a customer's integration is the
one that turns up in a public repository.

**Session behavior on shared devices is ignored.** The next person at the workstation inherits the session, and in a clinical
setting that is an access-control failure with an audit consequence.

---

# Related

| | |
| --- | --- |
| `Authorization.md` | What the identity is permitted to do |
| `security/Authentication.md` | Factors, credentials and recovery |
| `security/Secrets.md` | Where keys and signing material live |
| `03-user` | Device and environment constraints |

---

> **Concept Note**
>
> A token that carries permissions is a token that cannot be
> revoked.
>
> That is a security decision, not a caching one — and it is usually
> made as if it were caching.
