#!/usr/bin/env python3
"""Arm 2 (mechanical): TextRank-style extractive selector. No model, no network, no vendor.

Fixed rule, applied identically to every document. Zero per-document overrides.
Standard library only. Deterministic: same input, same output, no seed.

Usage:  python3 scripts/mechanical_selector.py   (requires corpus/body/ — see rebuild_corpus.py)
"""
import json, math, os, re, glob

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # instrument root
STOP = set("""a an the and or but if while of to in on at by for with about against between into
through during before after above below from up down out off over under again further then once
here there when where why how all any both each few more most other some such no nor not only own
same so than too very can will just should now is are was were be been being have has had do does
did this that these those it its as we our they their he she his her i you your which who whom what
also may might must could would shall thus therefore however moreover furthermore""".split())


def sentences(text):
    out = []
    for para in text.split("\n\n"):
        para = para.strip()
        if not para:
            continue
        # protect common abbreviations and decimals before splitting
        p = re.sub(r"\b([A-Z][a-z]{0,3})\.\s", r"\1<DOT> ", para)
        p = re.sub(r"(\d)\.(\d)", r"\1<DEC>\2", p)
        p = re.sub(r"\b(e\.g|i\.e|et al|vs|Fig|Eq|approx|ca)\.", r"\1<DOT>", p)
        for s in re.split(r"(?<=[.!?])\s+(?=[A-Z(])", p):
            s = s.replace("<DOT>", ".").replace("<DEC>", ".").strip()
            if s:
                out.append(s)
    return out


def content(s):
    return {w for w in re.findall(r"[a-z][a-z\-]{2,}", s.lower()) if w not in STOP}


def textrank(sents, d=0.85, iters=60):
    toks = [content(s) for s in sents]
    n = len(sents)
    sim = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            a, b = toks[i], toks[j]
            if not a or not b:
                continue
            inter = len(a & b)
            if inter == 0:
                continue
            v = inter / (math.log(len(a) + 1) + math.log(len(b) + 1))
            sim[i][j] = sim[j][i] = v
    score = [1.0] * n
    for _ in range(iters):
        new = []
        for i in range(n):
            acc = 0.0
            for j in range(n):
                if j == i or sim[j][i] == 0:
                    continue
                rowsum = sum(sim[j])
                if rowsum > 0:
                    acc += sim[j][i] / rowsum * score[j]
            new.append((1 - d) + d * acc)
        score = new
    return score


results = {}
for path in sorted(glob.glob(f"{OUT}/corpus/body/*.txt")):
    n = os.path.basename(path)[:2]
    text = open(path).read()
    sents = sentences(text)
    elig = [(i, s) for i, s in enumerate(sents) if 15 <= len(s.split()) <= 60]
    if len(elig) < 5:
        elig = [(i, s) for i, s in enumerate(sents) if 8 <= len(s.split()) <= 90]
    idxs = [i for i, _ in elig]
    scores = textrank([s for _, s in elig])
    ranked = sorted(zip(idxs, scores), key=lambda t: -t[1])[:5]
    chosen = sorted(i for i, _ in ranked)
    picked = [sents[i] for i in chosen]
    ok = all(s in text for s in picked)
    results[n] = {"sentences": picked, "verbatim_ok": ok,
                  "n_sentences_total": len(sents), "n_eligible": len(elig)}

json.dump(results, open(f"{OUT}/selections/arm2-mechanical.json", "w"), indent=1, ensure_ascii=False)
bad = [k for k, v in results.items() if not v["verbatim_ok"]]
print(f"docs={len(results)}  verbatim_failures={len(bad)} {bad}")
for k, v in results.items():
    print(f"\n--- {k}  ({v['n_eligible']}/{v['n_sentences_total']} eligible) ---")
    for s in v["sentences"]:
        print("  *", s[:220])
