# -*- coding: utf-8 -*-
"""
Khasi Aligned Parallel Corpus Manager & MT Evaluation Toolkit.
Manages sentence-aligned bitext parallel corpora and Machine Translation evaluation.
Supports bitext export, Hugging Face JSONL, TMX (Translation Memory), BLEU calculation,
and aligned sentence querying.
"""

import os
import json
import re
import math
from typing import Dict, List, Any, Optional, Tuple
from collections import Counter

CORPUS_DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
MASTER_CORPUS_FILE = os.path.join(CORPUS_DATA_DIR, "parallel_khasi_english.json")


class ParallelCorpus:
    """
    Sentence-aligned Khasi parallel corpus manager for Machine Translation benchmarking,
    corpus linguistics, and bilingual dataset generation.
    """

    def __init__(self, corpus_path: Optional[str] = None, include_books: bool = True):
        self.corpus_path = corpus_path or MASTER_CORPUS_FILE
        self.include_books = include_books and (corpus_path is None)
        self.records: List[Dict[str, Any]] = self._load()

    def _load(self) -> List[Dict[str, Any]]:
        records: List[Dict[str, Any]] = []
        seen_ids = set()

        if os.path.exists(self.corpus_path):
            with open(self.corpus_path, "r", encoding="utf-8") as f:
                for r in json.load(f):
                    rid = r.get("id")
                    if rid not in seen_ids:
                        records.append(r)
                        if rid:
                            seen_ids.add(rid)

        # Merge verified book datasets from data/books/*.json
        books_dir = os.path.join(CORPUS_DATA_DIR, "books")
        if self.include_books and os.path.exists(books_dir):
            for bfile in sorted(os.listdir(books_dir)):
                if bfile.endswith(".json"):
                    bpath = os.path.join(books_dir, bfile)
                    with open(bpath, "r", encoding="utf-8") as f:
                        for r in json.load(f):
                            rid = r.get("id")
                            if rid in seen_ids:
                                for existing in records:
                                    if existing.get("id") == rid:
                                        existing.update(r)
                                        break
                            else:
                                records.append(r)
                                if rid:
                                    seen_ids.add(rid)

        return records

    def __len__(self) -> int:
        return len(self.records)

    def get_records(
        self,
        source: Optional[str] = None,
        split: Optional[str] = None,
        domain: Optional[str] = None,
        book_id: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """Filter records by source book, train/test split, domain, or book_id."""
        res = self.records
        if source:
            s_low = source.lower()
            res = [r for r in res if s_low in r.get("source_book", "").lower()]
        if split:
            sp_low = split.lower().strip()
            res = [r for r in res if r.get("split", "").lower() == sp_low]
        if domain:
            d_low = domain.lower()
            res = [r for r in res if d_low in r.get("domain", "").lower()]
        if book_id:
            b_low = book_id.lower().strip()
            res = [r for r in res if b_low in r.get("book_id", "").lower()]
        return res

    def get_pairs(
        self,
        source: Optional[str] = None,
        split: Optional[str] = None,
        target_lang: str = "en"
    ) -> List[Tuple[str, str]]:
        """Return raw (khasi_sentence, target_sentence) tuples (target_lang='en' or 'hi')."""
        records = self.get_records(source=source, split=split)
        lang_key = "hindi" if target_lang.lower().startswith("hi") else "english"
        return [(r["khasi"], r.get(lang_key, "")) for r in records if r.get(lang_key)]

    def get_english_pairs(
        self,
        source: Optional[str] = None,
        split: Optional[str] = None
    ) -> List[Tuple[str, str]]:
        """Convenience method for (khasi, english) sentence pairs."""
        return self.get_pairs(source=source, split=split, target_lang="en")

    def get_book_sentences(self, book_id: str) -> List[Dict[str, Any]]:
        """Return all sentences extracted from a specific digitized book ID."""
        b_low = book_id.lower().strip()
        return [r for r in self.records if r.get("book_id", "").lower() == b_low]

    def list_books_in_corpus(self) -> List[Dict[str, Any]]:
        """List all books represented in the corpus along with sentence counts."""
        book_counts = Counter(r.get("source_book", "Unknown") for r in self.records)
        book_ids = {}
        for r in self.records:
            title = r.get("source_book", "Unknown")
            if title not in book_ids and "book_id" in r:
                book_ids[title] = r["book_id"]

        result = []
        for title, count in sorted(book_counts.items(), key=lambda x: -x[1]):
            result.append({
                "source_book": title,
                "book_id": book_ids.get(title, ""),
                "sentence_count": count
            })
        return result

    def search(self, query: str, lang: Optional[str] = None) -> List[Dict[str, Any]]:
        """Search parallel corpus across Khasi or English text."""
        q = query.lower().strip()
        if lang == "kha" or lang == "khasi":
            return [r for r in self.records if q in r.get("khasi", "").lower()]
        elif lang == "en" or lang == "english":
            return [r for r in self.records if q in r.get("english", "").lower()]
        return [
            r for r in self.records
            if q in r.get("khasi", "").lower()
            or q in r.get("english", "").lower()
        ]

    def get_stats(self) -> Dict[str, Any]:
        """Return dataset statistics including source counts, vocabulary, and splits."""
        sources = Counter(r.get("source_book", "Unknown") for r in self.records)
        splits = Counter(r.get("split", "unassigned") for r in self.records)
        domains = Counter(r.get("domain", "general") for r in self.records)

        total_khasi_words = sum(len(r.get("khasi", "").split()) for r in self.records)
        total_english_words = sum(len(r.get("english", "").split()) for r in self.records)

        return {
            "total_sentence_pairs": len(self.records),
            "total_books_represented": len(sources),
            "sources": dict(sources),
            "splits": dict(splits),
            "domains": dict(domains),
            "total_khasi_words": total_khasi_words,
            "total_english_words": total_english_words,
            "avg_khasi_sentence_len": round(total_khasi_words / max(1, len(self.records)), 2),
            "avg_english_sentence_len": round(total_english_words / max(1, len(self.records)), 2),
        }

    def export_bitext(
        self,
        khasi_path: str,
        target_path: str,
        target_lang: str = "en",
        split: Optional[str] = None
    ) -> int:
        """Export aligned bitext sentences to parallel plain text files (.kha and .en)."""
        pairs = self.get_pairs(split=split, target_lang=target_lang)
        os.makedirs(os.path.dirname(os.path.abspath(khasi_path)), exist_ok=True)
        os.makedirs(os.path.dirname(os.path.abspath(target_path)), exist_ok=True)

        with open(khasi_path, "w", encoding="utf-8") as fk, open(target_path, "w", encoding="utf-8") as ft:
            for kh, trg in pairs:
                fk.write(kh.strip() + "\n")
                ft.write(trg.strip() + "\n")
        return len(pairs)

    def export_tmx(self, output_path: str, target_lang: str = "en") -> int:
        """Export parallel corpus to Translation Memory eXchange (TMX 1.4b) format."""
        os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
        target_key = "hindi" if target_lang.lower().startswith("hi") else "english"
        target_code = "hi" if target_lang.lower().startswith("hi") else "en"

        lines = [
            '<?xml version="1.0" encoding="UTF-8"?>',
            '<!DOCTYPE tmx SYSTEM "tmx14.dtd">',
            '<tmx version="1.4">',
            f'  <header creationtool="pykhasi" creationtoolversion="1.12.0" segtype="sentence" o-tmf="UTF-8" adminlang="en" srclang="kha" datatype="PlainText"/>',
            '  <body>'
        ]
        for r in self.records:
            if target_key in r and r[target_key]:
                lines.append('    <tu>')
                lines.append('      <tuv xml:lang="kha">')
                lines.append(f'        <seg>{r["khasi"]}</seg>')
                lines.append('      </tuv>')
                lines.append(f'      <tuv xml:lang="{target_code}">')
                lines.append(f'        <seg>{r[target_key]}</seg>')
                lines.append('      </tuv>')
                lines.append('    </tu>')
        lines.append('  </body>')
        lines.append('</tmx>')

        with open(output_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")
        return len(self.records)

    def export_huggingface_format(self, output_path: str, include_hindi: bool = True) -> int:
        """Export parallel corpus in Hugging Face translation dataset format ({'translation': {'kha': ..., 'en': ..., 'hi': ...}})."""
        os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            for r in self.records:
                trans = {
                    "kha": r["khasi"],
                    "en": r.get("english", "")
                }
                if include_hindi and "hindi" in r:
                    trans["hi"] = r["hindi"]

                item = {
                    "id": r["id"],
                    "translation": trans,
                    "source": r.get("source_book", ""),
                    "domain": r.get("domain", ""),
                    "split": r.get("split", "train")
                }
                f.write(json.dumps(item, ensure_ascii=False) + "\n")
        return len(self.records)

    @staticmethod
    def compute_bleu(
        hypotheses: List[str],
        references: List[str],
        max_order: int = 4
    ) -> Dict[str, float]:
        """
        Compute standard BLEU score (n-gram precision with brevity penalty)
        for machine translation evaluation without external dependencies.
        """
        if len(hypotheses) != len(references) or not hypotheses:
            return {"bleu": 0.0, "p1": 0.0, "p2": 0.0, "p3": 0.0, "p4": 0.0, "bp": 0.0}

        def tokenize_simple(text: str) -> List[str]:
            return [w for w in re.split(r"\W+", text.lower()) if w]

        precisions = []
        hyp_len_total = 0
        ref_len_total = 0

        for n in range(1, max_order + 1):
            clipped_matches = 0
            total_ngrams = 0

            for hyp, ref in zip(hypotheses, references):
                hyp_toks = tokenize_simple(hyp)
                ref_toks = tokenize_simple(ref)
                if n == 1:
                    hyp_len_total += len(hyp_toks)
                    ref_len_total += len(ref_toks)

                hyp_ngrams = Counter(
                    tuple(hyp_toks[i:i+n]) for i in range(len(hyp_toks) - n + 1)
                )
                ref_ngrams = Counter(
                    tuple(ref_toks[i:i+n]) for i in range(len(ref_toks) - n + 1)
                )

                for ng, count in hyp_ngrams.items():
                    clipped_matches += min(count, ref_ngrams.get(ng, 0))
                total_ngrams += max(0, len(hyp_toks) - n + 1)

            p_n = (clipped_matches / total_ngrams) if total_ngrams > 0 else 0.0
            precisions.append(p_n)

        # Brevity Penalty
        if hyp_len_total == 0:
            bp = 0.0
        elif hyp_len_total < ref_len_total:
            bp = math.exp(1.0 - (ref_len_total / hyp_len_total))
        else:
            bp = 1.0

        # Geometric mean of precisions
        smooth_eps = 1e-6
        log_prec_sum = 0.0
        for p in precisions:
            val = p if p > 0 else smooth_eps
            log_prec_sum += (1.0 / max_order) * math.log(val)

        bleu_score = bp * math.exp(log_prec_sum) * 100.0

        return {
            "bleu": round(bleu_score, 2),
            "p1": round(precisions[0] * 100, 2),
            "p2": round(precisions[1] * 100, 2),
            "p3": round(precisions[2] * 100, 2),
            "p4": round(precisions[3] * 100, 2),
            "brevity_penalty": round(bp, 4)
        }

