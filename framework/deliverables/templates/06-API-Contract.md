---
Artifact: api-contract
Project: «project name»
Version: 1.0
Date: «ISO date»
Modules: [09-technology]
---

<!-- fill: Every product capability in the feature spec must have a supporting endpoint
     here. Run that check explicitly — an unsupported capability is a gap that surfaces
     mid-build. Request and response shapes must be concrete, not described.
     Remove every <!-- fill --> comment before delivery. -->

# API Contract — «Product Name»

## 1. Overview

| | |
| --- | --- |
| Style | «REST / GraphQL / RPC» |
| Base URL | `«https://api.example.com/v1»` |
| Format | JSON |
| Versioning | «URL path / header» |
| Auth | «scheme» |

---

## 2. Authentication

<!-- fill: Concrete. Which scheme, how a token is obtained, how long it lives,
     how it is refreshed, and what happens when it expires. -->

**Scheme:** «e.g. Bearer JWT»

**Obtaining a token**

```http
POST /v1/auth/token
Content-Type: application/json

{
  "email": "«string»",
  "password": "«string»"
}
```

```json
{
  "access_token": "«jwt»",
  "expires_in": 3600,
  "refresh_token": "«token»"
}
```

**Token lifetime:** «duration»
**Refresh:** «mechanism»
**On expiry:** «401 with what body; client behaviour expected»

---

## 3. Authorisation Model

<!-- fill: Who can do what. This is where IDOR and privilege-escalation bugs are
     prevented or created. Be explicit about record-level access, not just roles. -->

| Role | Can | Cannot |
| --- | --- | --- |
| «role» | «permissions» | «explicit denials» |

**Record-level rule:** «e.g. a user may only read records belonging to their own clinic»

**Enforcement point:** «where this is checked — middleware, query scope, both»

---

## 4. Endpoints

<!-- fill: One block per endpoint. Include: method, path, auth requirement, params,
     request body, success response, and every error response.
     "Returns the user object" is not a response shape. Show the JSON. -->

### «Resource»

#### `GET /v1/«resource»`

«One sentence: what this returns and who calls it.»

| | |
| --- | --- |
| Auth | required — «role» |
| Serves | F«n» |
| Idempotent | yes |

**Query parameters**

| Param | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `page` | int | no | 1 | |
| `limit` | int | no | 25 | max 100 |
| `«filter»` | «type» | no | — | «meaning» |

**Response — 200**

```json
{
  "data": [
    {
      "id": "«uuid»",
      "«field»": "«value»"
    }
  ],
  "meta": { "page": 1, "limit": 25, "total": 0 }
}
```

**Errors**

| Status | Code | When |
| --- | --- | --- |
| 401 | `unauthenticated` | Missing or invalid token |
| 403 | `forbidden` | Authenticated but not permitted |
| 422 | `validation_failed` | Invalid query parameters |

---

#### `POST /v1/«resource»`

**Request**

```json
{
  "«field»": "«value»"
}
```

**Validation**

| Field | Rule |
| --- | --- |
| `«field»` | required, «constraint» |

**Response — 201**

```json
{ "data": { "id": "«uuid»" } }
```

**Errors**

| Status | Code | When |
| --- | --- | --- |
| 409 | `conflict` | «condition» |
| 422 | `validation_failed` | «condition» |

---

<!-- fill: Repeat for each endpoint. -->

---

## 5. Error Taxonomy

<!-- fill: One consistent error shape across the whole API. Clients depend on this. -->

```json
{
  "error": {
    "code": "«machine_readable_code»",
    "message": "«human readable»",
    "details": [
      { "field": "«name»", "issue": "«what is wrong»" }
    ]
  }
}
```

| Status | Code | Meaning |
| --- | --- | --- |
| 400 | `bad_request` | Malformed request |
| 401 | `unauthenticated` | No valid credentials |
| 403 | `forbidden` | Authenticated, not permitted |
| 404 | `not_found` | Resource does not exist, or caller may not see it |
| 409 | `conflict` | State conflict |
| 422 | `validation_failed` | Semantically invalid |
| 429 | `rate_limited` | Too many requests |
| 500 | `internal_error` | Unhandled |

<!-- fill: Note the 404 wording — returning 404 rather than 403 for records the caller
     may not see prevents existence disclosure. State the chosen behaviour explicitly. -->

---

## 6. Pagination, Filtering, Sorting

| Concern | Convention |
| --- | --- |
| Pagination | «offset / cursor» — «parameters» |
| Filtering | «convention» |
| Sorting | «convention, default order» |

---

## 7. Rate Limiting

| Scope | Limit | Window | Response |
| --- | --- | --- | --- |
| «per token» | «n» | «period» | 429 + `Retry-After` |

---

## 8. Webhooks / Events

<!-- fill: Only if the product emits them. Include the payload shape, delivery
     guarantees, retry policy and signature verification. -->

| Event | Fired when | Payload |
| --- | --- | --- |
| `«event.name»` | «trigger» | «shape» |

**Delivery:** «at-least-once / at-most-once»
**Retry:** «policy»
**Signature:** «how the receiver verifies authenticity»

---

## 9. Capability Coverage Check

<!-- fill: MANDATORY. Every MVP feature must map to at least one endpoint.
     A row with no endpoint is a gap that will surface mid-build. Resolve it here. -->

| Feature | Endpoint(s) | Covered |
| --- | --- | --- |
| F1 | `POST /v1/«x»`, `GET /v1/«x»` | ✓ |
| F2 | «...» | ✓ |

**Uncovered capabilities:** «none, or list them and say why»

---

<!-- ACCEPTANCE — remove before delivery
- [ ] Endpoints, methods, request and response shapes are concrete JSON, not descriptions
- [ ] Auth and authorisation model specified including record-level rules
- [ ] Consistent error taxonomy defined
- [ ] Every MVP feature maps to an endpoint in the coverage check
- [ ] Validation rules stated per writable field
- [ ] Every fill comment removed
-->
