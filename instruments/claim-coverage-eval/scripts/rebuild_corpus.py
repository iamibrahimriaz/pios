#!/usr/bin/env python3
"""Deterministically rebuild the evaluation corpus from pinned PMC identifiers.

The original corpus was discovered with a relevance-ranked PMC search, which is NOT
reproducible — the same query returns different articles over time. This script pins the
twelve identifiers instead, so any later run reconstructs byte-identical body text and can
verify it against the recorded SHA-256 digests.

Writes:
  corpus/body/NN.txt   article body prose (abstract, highlights, methods, declarations removed)
  corpus/manifest.json per-article metadata + digest

Ground truth (corpus/truth/NN.txt) is committed to the repository and is NEVER regenerated
here — regenerating it would let a later change to this script silently rewrite the answers.

Usage:  python3 scripts/rebuild_corpus.py [--verify]
"""
import hashlib, json, os, re, sys, time, urllib.request

EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Pinned corpus. Discovery provenance is in corpus/screening-log.txt (77 articles screened).
PINNED = [
    ("01", "13448589"), ("02", "13448187"), ("03", "13446196"), ("04", "13446199"),
    ("05", "11909433"), ("06", "11908583"), ("07", "11908581"), ("08", "11908580"),
    ("09", "13415681"), ("10", "13415678"), ("11", "13400140"), ("12", "13400184"),
]


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "claim-coverage-eval/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8", "replace")


def strip_tags(s):
    s = re.sub(r"<(xref|italic|bold|sup|sub|sc|underline|monospace)[^>]*>", "", s)
    s = re.sub(r"</(xref|italic|bold|sup|sub|sc|underline|monospace)>", "", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = s.replace("&#x02019;", "’").replace("&#x02018;", "‘")
    s = s.replace("&#x0201c;", "“").replace("&#x0201d;", "”")
    s = s.replace("&#x02013;", "–").replace("&#x02014;", "—")
    s = s.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
    s = re.sub(r"&#x0([0-9a-fA-F]{4});", lambda m: chr(int(m.group(1), 16)), s)
    s = re.sub(r"&[a-zA-Z]+;", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def highlights(xml):
    m = re.search(r'<abstract abstract-type="author-highlights".*?</abstract>', xml, re.S)
    if not m:
        return []
    return [strip_tags(t) for t in re.findall(r"<list-item[^>]*>(.*?)</list-item>", m.group(0), re.S)]


def body_text(xml):
    """Body prose only. Abstract, author highlights, figures, tables, methods and
    declarations are removed so the task cannot be solved by locating a summary."""
    m = re.search(r"<body[^>]*>(.*?)</body>", xml, re.S)
    if not m:
        return ""
    b = m.group(1)
    for tag in ("fig", "table-wrap", "disp-formula", "inline-formula", "supplementary-material",
                "graphic", "media", "table", "list", "ack", "fn-group", "boxed-text"):
        b = re.sub(rf"<{tag}[^>]*>.*?</{tag}>", " ", b, flags=re.S)
        b = re.sub(rf"<{tag}[^>]*/>", " ", b)
    paras = []
    for sec in re.findall(r"<sec\b.*?</sec>", b, re.S) or [b]:
        t = re.search(r"<title>(.*?)</title>", sec, re.S)
        title = strip_tags(t.group(1)) if t else ""
        if re.search(r"method|declaration|acknowledg|data and code|resource availability|supplemental",
                     title, re.I):
            continue
        for p in re.findall(r"<p\b[^>]*>(.*?)</p>", sec, re.S):
            x = strip_tags(p)
            if len(x) > 120:
                paras.append(x)
    if not paras:
        for p in re.findall(r"<p\b[^>]*>(.*?)</p>", b, re.S):
            x = strip_tags(p)
            if len(x) > 120:
                paras.append(x)
    return "\n\n".join(paras)


def meta(xml):
    def one(pat, default=""):
        m = re.search(pat, xml, re.S)
        return strip_tags(m.group(1)) if m else default
    lic = re.search(r'<license[^>]*license-type="([^"]+)"', xml)
    lic_link = re.search(r'<license[^>]*xlink:href="([^"]+)"', xml)
    return {
        "journal": one(r"<journal-title>(.*?)</journal-title>"),
        "title": one(r"<article-title>(.*?)</article-title>"),
        "doi": one(r'<article-id pub-id-type="doi">(.*?)</article-id>'),
        "year": one(r"<pub-date[^>]*>.*?<year>(\d{4})</year>"),
        "license_type": lic.group(1) if lic else "see PMC record",
        "license_url": lic_link.group(1) if lic_link else "see PMC record",
    }


def main():
    verify = "--verify" in sys.argv
    os.makedirs(f"{ROOT}/corpus/body", exist_ok=True)
    manifest_path = f"{ROOT}/corpus/manifest.json"
    old = json.load(open(manifest_path)) if (verify and os.path.exists(manifest_path)) else None
    out, mismatches = [], []

    for n, pmcid in PINNED:
        xml = get(f"{EUTILS}/efetch.fcgi?db=pmc&id={pmcid}&retmode=xml")
        time.sleep(0.4)
        bt, hl, md = body_text(xml), highlights(xml), meta(xml)
        digest = hashlib.sha256(bt.encode("utf-8")).hexdigest()
        open(f"{ROOT}/corpus/body/{n}.txt", "w", encoding="utf-8").write(bt)
        rec = {"n": n, "pmcid": f"PMC{pmcid}", "claims": len(hl),
               "body_words": len(bt.split()), "body_sha256": digest, **md}
        out.append(rec)
        if old:
            prev = next((r for r in old["articles"] if r["n"] == n), None)
            if prev and prev["body_sha256"] != digest:
                mismatches.append(n)
        print(f"{n}  PMC{pmcid}  {md['journal'][:24]:<24} {rec['body_words']:>6}w  {len(hl)} claims")

    json.dump({"instrument": "claim-coverage-eval",
               "corpus_pinned_on": "2026-08-13",
               "source": "NCBI PubMed Central Open Access subset, via E-utilities",
               "licence_note": "Per-article licence recorded below. Verify before redistributing full text.",
               "articles": out,
               "totals": {"documents": len(out), "claims": sum(r["claims"] for r in out)}},
              open(manifest_path, "w"), indent=1)

    if verify:
        print("\nVERIFY:", "ALL BODIES MATCH" if not mismatches else f"MISMATCH in {mismatches}")
        sys.exit(1 if mismatches else 0)
    print(f"\n{len(out)} documents, {sum(r['claims'] for r in out)} author-written claims")


main()
