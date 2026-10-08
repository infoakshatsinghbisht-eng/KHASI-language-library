# -*- coding: utf-8 -*-
"""
Khasi Aligned Parallel Corpus Manager & MT Evaluation Toolkit.
Manages sentence-aligned bitext corpora from:
- Ka Niam Jong Ki Khasi (U Sib Charan Roy, 1919)
- Ka Jingiaid U Pilgrim (The Pilgrim's Progress in Khasi)
- Traditional Folklore Readers (Lum Diengiei, Sohpetbneng, Manik Raitong, U Thlen)
Supports bitext export, Hugging Face JSONL, TMX (Translation Memory), and BLEU calculation.
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
    """Sentence-aligned Khasi-English parallel corpus for Machine Translation benchmarking."""

    def __init__(self, corpus_path: Optional[str] = None):
        self.corpus_path = corpus_path or MASTER_CORPUS_FILE
        self.records: List[Dict[str, Any]] = self._load()

    def _load(self) -> List[Dict[str, Any]]:
        if not os.path.exists(self.corpus_path):
            return []
        with open(self.corpus_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def __len__(self) -> int:
        return len(self.records)

    def get_records(
        self,
        source: Optional[str] = None,
        split: Optional[str] = None,
        domain: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """Filter records by source book, train/test split, or thematic domain."""
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
        return res

    def get_pairs(
        self,
        source: Optional[str] = None,
        split: Optional[str] = None
    ) -> List[Tuple[str, str]]:
        """Return raw (khasi_sentence, english_sentence) tuples."""
        records = self.get_records(source=source, split=split)
        return [(r["khasi"], r["english"]) for r in records]

    def search(self, query: str) -> List[Dict[str, Any]]:
        """Search parallel corpus across Khasi or English text."""
        q = query.lower().strip()
        return [
            r for r in self.records
            if q in r.get("khasi", "").lower() or q in r.get("english", "").lower()
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
            "sources": dict(sources),
            "splits": dict(splits),
            "domains": dict(domains),
            "total_khasi_words": total_khasi_words,
            "total_english_words": total_english_words,
            "avg_khasi_sentence_len": round(total_khasi_words / max(1, len(self.records)), 2),
            "avg_english_sentence_len": round(total_english_words / max(1, len(self.records)), 2),
        }

    def export_bitext(self, khasi_path: str, english_path: str, split: Optional[str] = None) -> int:
        """Export aligned bitext sentences to parallel plain text files (.kha and .en)."""
        pairs = self.get_pairs(split=split)
        os.makedirs(os.path.dirname(khasi_path), exist_ok=True)
        os.makedirs(os.path.dirname(english_path), exist_ok=True)

        with open(khasi_path, "w", encoding="utf-8") as fk, open(english_path, "w", encoding="utf-8") as fe:
            for kh, en in pairs:
                fk.write(kh.strip() + "\n")
                fe.write(en.strip() + "\n")
        return len(pairs)

    def export_tmx(self, output_path: str) -> int:
        """Export parallel corpus to Translation Memory eXchange (TMX 1.4b) format."""
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        lines = [
            '<?xml version="1.0" encoding="UTF-8"?>',
            '<!DOCTYPE tmx SYSTEM "tmx14.dtd">',
            '<tmx version="1.4">',
            '  <header creationtool="pykhasi" creationtoolversion="1.2.0" segtype="sentence" o-tmf="UTF-8" adminlang="en" srclang="kha" datatype="PlainText"/>',
            '  <body>'
        ]
        for r in self.records:
            lines.append('    <tu>')
            lines.append('      <tuv xml:lang="kha">')
            lines.append(f'        <seg>{r["khasi"]}</seg>')
            lines.append('      </tuv>')
            lines.append('      <tuv xml:lang="en">')
            lines.append(f'        <seg>{r["english"]}</seg>')
            lines.append('      </tuv>')
            lines.append('    </tu>')
        lines.append('  </body>')
        lines.append('</tmx>')

        with open(output_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")
        return len(self.records)

    def export_huggingface_format(self, output_path: str) -> int:
        """Export parallel corpus in Hugging Face translation dataset format ({'translation': {'kha': ..., 'en': ...}})."""
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            for r in self.records:
                item = {
                    "id": r["id"],
                    "translation": {
                        "kha": r["khasi"],
                        "en": r["english"]
                    },
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
