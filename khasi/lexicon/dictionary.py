# -*- coding: utf-8 -*-
"""Khasi Dictionary and Lexical Lookup Engine."""

import json
import random
from pathlib import Path
from typing import Dict, List, Any, Optional

from ..phonetics import normalize
from ..grammar.verbs import extract_root

DATA_DIR = Path(__file__).resolve().parent / "data"

class KhasiDictionary:
    """Manages bilingual & trilingual Khasi-English-Hindi lexical datasets."""

    def __init__(self):
        self._words: Dict[str, Dict[str, Any]] = {}
        self._phrases: List[Dict[str, Any]] = []
        self._proverbs: List[Dict[str, Any]] = []
        self._riddles: List[Dict[str, Any]] = []
        self._load_data()

    def _load_data(self):
        w_file = DATA_DIR / "words.json"
        if w_file.exists():
            with open(w_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                for item in data:
                    self._words[item["khasi"].lower()] = item

        p_file = DATA_DIR / "phrases.json"
        if p_file.exists():
            with open(p_file, "r", encoding="utf-8") as f:
                self._phrases = json.load(f)

        pr_file = DATA_DIR / "proverbs.json"
        if pr_file.exists():
            with open(pr_file, "r", encoding="utf-8") as f:
                self._proverbs = json.load(f)

        r_file = DATA_DIR / "riddles.json"
        if r_file.exists():
            with open(r_file, "r", encoding="utf-8") as f:
                self._riddles = json.load(f)

        # Merge core grammatical vocabulary so essential roots are always resolved
        try:
            from ..grammar.nouns import CORE_KHASI_NOUNS
            for n in CORE_KHASI_NOUNS:
                w = n.lemma.lower()
                if w not in self._words:
                    self._words[w] = {
                        "khasi": n.lemma,
                        "english": n.english,
                        "hindi": n.hindi,
                        "pos": "noun",
                        "gender": n.gender,
                    }
        except Exception:
            pass

        try:
            from ..grammar.verbs import CORE_KHASI_VERBS
            for v in CORE_KHASI_VERBS:
                w = v["lemma"].lower()
                if w not in self._words:
                    self._words[w] = {
                        "khasi": v["lemma"],
                        "english": v["english"],
                        "hindi": v["hindi"],
                        "pos": "verb",
                    }
        except Exception:
            pass

        try:
            from ..grammar.adjectives import CORE_KHASI_ADJECTIVES
            for a in CORE_KHASI_ADJECTIVES:
                w = a["lemma"].lower()
                if w not in self._words:
                    self._words[w] = {
                        "khasi": a["lemma"],
                        "english": a["english"],
                        "hindi": a["hindi"],
                        "pos": "adjective",
                    }
        except Exception:
            pass

    def lookup(self, word: str) -> Optional[Dict[str, Any]]:
        """Look up a Khasi word with exact, diacritic, or morphological root matching."""
        clean = normalize(word).lower().strip(".,!?;:'\"-")
        if not clean:
            return None

        # 1. Exact match
        if clean in self._words:
            return self._words[clean]

        # 2. Check without gender article if user passed "u briew" or "ka ïing"
        for art in ["u ", "ka ", "i ", "ki "]:
            if clean.startswith(art):
                sub = clean[len(art):].strip()
                if sub in self._words:
                    return self._words[sub]

        # 3. Morphological root fallback (jing-, pyn-, nong-, sngew-)
        root = extract_root(clean)
        if root != clean and root in self._words:
            base = self._words[root].copy()
            base["note"] = f"Derived form of root '{root}'"
            base["root"] = root
            return base

        return None

    def search(self, query: str) -> List[Dict[str, Any]]:
        """Search vocabulary matching across Khasi, English, or Hindi."""
        q = query.lower().strip()
        results = []
        for w, item in self._words.items():
            if (
                q in w or
                q in item.get("english", "").lower() or
                q in item.get("hindi", "").lower()
            ):
                results.append(item)
        return results

    def all_words(self) -> List[Dict[str, Any]]:
        return list(self._words.values())

    def all_phrases(self) -> List[Dict[str, Any]]:
        return self._phrases

    def all_proverbs(self) -> List[Dict[str, Any]]:
        return self._proverbs

    def all_riddles(self) -> List[Dict[str, Any]]:
        return self._riddles

    def random_word(self) -> Optional[Dict[str, Any]]:
        words = list(self._words.values())
        return random.choice(words) if words else None

    def random_phrase(self) -> Optional[Dict[str, Any]]:
        return random.choice(self._phrases) if self._phrases else None

    def random_proverb(self) -> Optional[Dict[str, Any]]:
        return random.choice(self._proverbs) if self._proverbs else None

    def random_riddle(self) -> Optional[Dict[str, Any]]:
        return random.choice(self._riddles) if self._riddles else None
