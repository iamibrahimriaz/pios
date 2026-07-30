---
Title: Voice
Module: 14-ai-systems
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Check the environment before proposing speech, and treat consent as a requirement.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 14-ai-systems/knowledge/AI-Use-Cases.md
Outputs:
  - Voice capabilities within model_strategy
Related Modules:
  - 03-user
  - 09-technology
Tags:
  - AI
  - Voice
  - Concept
---

# Voice

---

# What It Is

Speech as input — transcription, dictation, or voice control.

It is the capability most constrained by the **environment**, and `03-user` already recorded the deciding facts:

| Environmental fact | Consequence |
| --- | --- |
| Who else can hear | Speaking clinical or financial detail aloud may be unacceptable regardless of quality |
| Background noise | Accuracy degrades sharply, and wards and offices are not quiet |
| Whether a phone is permitted | Some settings prohibit the device entirely |
| Whether the user's speech is typical | Accent, speech differences and non-native speakers all affect accuracy — an `Accessibility` question |
| Whether a third party is present | Their voice may be captured, which is a consent question |

The last row is the one that turns this from a quality question into a legal one: **recording a consultation captures another person's
voice and words.** Consent, retention and residency all apply, and `02-market` Frame 2 decides how.

---

# When It Applies

In Move 2 (Compare) as a candidate, and in Move 3 where data rights make consent a requirement rather than a courtesy.

---

# How to Apply It Here

**Check `03-user`'s environment first.** For a shared clinical space, speaking aloud may be ruled out before accuracy is even discussed — an
immovable rather than a preference.

**Treat third-party consent as a requirement in `08-product`.** How consent is obtained, recorded and revoked, and what happens if it is
refused. That is a product surface, not a policy note.

**Decide whether audio is retained, and for how long.** Audio is a richer and more sensitive record than the transcript. Discarding it after
transcription is frequently the correct design and it needs to be a stated one.

**Specify the accuracy failure path.** Transcription errors in clinical or financial detail are consequential and — crucially — the user may
not notice them if they did not re-read. That is `Automation.md`'s undetectable-error case.

**Include speech variation in evaluation.** A golden set of clear, native, quiet-room speech measures a population the product does not
serve.

---

# Where It Misleads

**Accuracy figures from quiet conditions are assumed to transfer.** The clinic, the ward and the car are the real environments, and
performance there is substantially worse.

**Domain vocabulary is assumed to be handled.** Drug names, procedure codes and proper nouns are exactly the high-consequence terms most
likely to be mis-transcribed.

**Consent is treated as an operational detail.** In a two-party setting it is a legal precondition, and it is a requirement with an interface.

**Voice is proposed as an accessibility feature without checking.** It helps some users and excludes others — those with speech differences,
those in shared spaces, those who cannot use a phone. `10-execution/knowledge/Accessibility.md` requires input methods that work for the
recorded population.

**Audio is retained by default.** It is the most sensitive artifact the product will hold, and default retention by a provider is a residency
and obligation question `09-technology` must answer.

---

# Related

| | |
| --- | --- |
| `LLM.md` | What happens to the transcript afterwards |
| `Automation.md` | Undetectable transcription errors |
| `03-user`, `10-execution` | Environment, immovables and accessibility |
| `09-technology` | Consent, retention and residency for audio |

---

> **Concept Note**
>
> Check whether they can speak at all before asking how accurately you
> can hear them.
>
> And a two-party recording captures someone who is not your user —
> which makes consent a requirement, not a setting.
