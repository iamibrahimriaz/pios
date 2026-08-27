#!/usr/bin/env python3
"""Verify verbatim containment and score claim coverage for both selector arms.

Reports four things:
  1. Verbatim containment, raw byte comparison        (the strict test)
  2. Verbatim containment, Unicode NFC + punctuation-folded  (the diagnostic test)
  3. Coverage C_a per arm, against the recorded grading table
  4. The structural check that no arm can be scored above the count of claims

Run 2, not 1, is what tells you whether an "anchoring failure" was semantic or typographic.

Usage:  python3 scripts/verify_and_score.py
"""
import csv, json, os, sys, unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Characters that render identically enough to fool a human author but not a byte comparison.
FOLD = {"’": "'", "‘": "'", "“": '"', "”": '"',
        "–": "-", "—": "-", "−": "-", " ": " ",
        " ": " ", " ": " ", " ": " ", "﻿": ""}


def fold(s):
    """Normalize to NFC, then fold the punctuation classes that break naive anchoring."""
    s = unicodedata.normalize("NFC", s)
    for a, b in FOLD.items():
        s = s.replace(a, b)
    return " ".join(s.split())


def check(arm_file, label):
    sel = json.load(open(f"{ROOT}/selections/{arm_file}", encoding="utf-8"))
    raw_fail, fold_fail, total = [], [], 0
    for doc in sorted(sel):
        body = open(f"{ROOT}/corpus/body/{doc}.txt", encoding="utf-8").read()
        sents = sel[doc]["sentences"] if isinstance(sel[doc], dict) else sel[doc]
        fbody = fold(body)
        for i, s in enumerate(sents, 1):
            total += 1
            if s not in body:
                raw_fail.append((doc, i))
                if fold(s) not in fbody:
                    fold_fail.append((doc, i))
    print(f"\n{label}")
    print(f"  sentences checked            : {total}")
    print(f"  raw byte containment failures: {len(raw_fail)} {raw_fail if raw_fail else ''}")
    print(f"  after NFC + punctuation fold : {len(fold_fail)} {fold_fail if fold_fail else ''}")
    if raw_fail and not fold_fail:
        print("  -> every failure was TYPOGRAPHIC, not semantic. Normalize before comparing.")
    return len(raw_fail), len(fold_fail)


def score():
    rows = list(csv.DictReader(open(f"{ROOT}/results/grading.csv", encoding="utf-8")))
    n = len(rows)
    a1 = sum(r["arm1_model_guided"] == "Y" for r in rows)
    a2 = sum(r["arm2_mechanical"] == "Y" for r in rows)
    assert a1 <= n and a2 <= n, "structural check failed: recovered exceeds claim count"
    band = lambda x: "PASS (>=70%)" if x >= .70 else ("REVISE (50-69%)" if x >= .50 else "STOP (<50%)")
    print(f"\nCOVERAGE  (claims = {n})")
    print(f"  arm 1  model-guided selector : {a1}/{n} = {a1/n:6.1%}   {band(a1/n)}")
    print(f"  arm 2  mechanical selector   : {a2}/{n} = {a2/n:6.1%}   {band(a2/n)}")
    print("\n  Bands above are the DEFAULTS INHERITED FROM THE ORIGINATING PROJECT.")
    print("  A new user must re-derive them from their own product bar before use.")
    return a1, a2, n


if __name__ == "__main__":
    if not os.path.isdir(f"{ROOT}/corpus/body"):
        sys.exit("corpus/body missing — run scripts/rebuild_corpus.py first")
    r1, f1 = check("arm1-model-guided.json", "ARM 1  model-guided selector")
    r2, f2 = check("arm2-mechanical.json", "ARM 2  mechanical selector (no model)")
    score()
    print(f"\nverbatim containment, raw : arm1 {60-r1}/60   arm2 {60-r2}/60")
    print(f"verbatim containment, fold: arm1 {60-f1}/60   arm2 {60-f2}/60")
