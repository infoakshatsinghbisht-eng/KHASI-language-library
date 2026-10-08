# -*- coding: utf-8 -*-
"""
Khasi Dialectology Engine & Dedicated Sub-Lexicons.
Supports:
- Pnar / Synteng (Jaiñtia Hills, 5,500+ words)
- War Khasi (Southern Slopes & Shella, 5,300+ words)
- Bhoi Khasi (Ri-Bhoi District, 1,250+ words)
- Maram Khasi (West Khasi Hills, 1,250+ words)
- Sohra (Standard Literary Khasi)
- Shillong Colloquial
"""

import json
import os
from typing import Dict, List, Any, Optional

DIALECTS_DIR = os.path.join(os.path.dirname(__file__), "data", "dialects")

_DIALECT_CACHE: Dict[str, List[Dict[str, Any]]] = {}
_LOOKUP_CACHE: Dict[str, Dict[str, Dict[str, Any]]] = {}

DIALECT_INFO = {
    "pnar": {
        "name": "Pnar / Synteng",
        "region": "Jaiñtia Hills (East & West Jaiñtia Hills: Jowai, Khliehriat, Shangpung)",
        "speakers_est": "350,000+",
        "features": "Mon-Khmer palatal fricative shift (sh -> ch), vowel shift (ie -> u/e), front nasal (sng -> sñ), rich independent oral tradition (Ka Behdeiñkhlam).",
        "file": "pnar_lexicon.json"
    },
    "war": {
        "name": "War Khasi",
        "region": "Southern Slopes facing Bangladesh (Shella, Sohbar, Nongjri, Mawlong, Tyrna)",
        "speakers_est": "60,000+",
        "features": "Archaic Austroasiatic vowel preservation, depalatalization (sh -> s), vowel lowering (u -> o), living root bridge builders.",
        "file": "war_lexicon.json"
    },
    "bhoi": {
        "name": "Bhoi Khasi",
        "region": "Ri-Bhoi District (Nongpoh, Umsning, Byrnihat)",
        "speakers_est": "150,000+",
        "features": "Northern border dialect, distinctive vocabulary, close contact with Karbi and Assamese borderlands.",
        "file": "bhoi_lexicon.json"
    },
    "maram": {
        "name": "Maram / Nongstoin",
        "region": "West Khasi Hills & South West Khasi Hills (Nongstoin, Mairang, Mawkyrwat)",
        "speakers_est": "180,000+",
        "features": "Vowel raising, distinct intonation patterns, central upland forest culture.",
        "file": "maram_lexicon.json"
    },
    "sohra": {
        "name": "Sohra (Standard Literary Khasi)",
        "region": "Cherrapunji & East Khasi Hills (State-wide literary standard)",
        "speakers_est": "1,100,000+",
        "features": "Formal orthography established 1841 by Thomas Jones, standard medium of Khasi literature, education and governance.",
        "file": None
    },
    "shillong": {
        "name": "Shillong Colloquial",
        "region": "Greater Shillong Urban Area",
        "speakers_est": "500,000+",
        "features": "Urban vernacular with simplified kinship terms (mei-rad, pa-rad) and modern cosmopolitan loanwords.",
        "file": None
    }
}

def list_dialects() -> List[str]:
    """Return list of supported Khasi dialects."""
    return list(DIALECT_INFO.keys())

def get_dialect_info(dialect: str) -> Optional[Dict[str, Any]]:
    """Return ethnographic and linguistic metadata for a dialect."""
    return DIALECT_INFO.get(dialect.lower().strip())

def load_dialect_lexicon(dialect: str) -> List[Dict[str, Any]]:
    """Load the dedicated sub-lexicon for a given dialect."""
    d = dialect.lower().strip()
    if d in _DIALECT_CACHE:
        return _DIALECT_CACHE[d]

    info = DIALECT_INFO.get(d)
    if not info or not info.get("file"):
        return []

    filepath = os.path.join(DIALECTS_DIR, info["file"])
    if not os.path.exists(filepath):
        return []

    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    _DIALECT_CACHE[d] = data
    return data

def _ensure_lookup(dialect: str) -> Dict[str, Dict[str, Any]]:
    d = dialect.lower().strip()
    if d not in _LOOKUP_CACHE:
        lex = load_dialect_lexicon(d)
        mapping = {}
        for item in lex:
            # Map both dialect word and standard word for bi-directional lookup
            dw = item["dialect_word"].lower().strip()
            sw = item["standard_khasi"].lower().strip()
            mapping[dw] = item
            if sw not in mapping:
                mapping[sw] = item
        _LOOKUP_CACHE[d] = mapping
    return _LOOKUP_CACHE[d]

def lookup_dialect(word: str, dialect: str) -> Optional[Dict[str, Any]]:
    """
    Search for a word in a specific dialect lexicon.
    Matches either dialect form or standard Sohra form.
    """
    lookup = _ensure_lookup(dialect)
    return lookup.get(word.lower().strip())

def find_cognates(word: str) -> Dict[str, str]:
    """
    Find cognate forms across all supported dialects (Sohra, Pnar, War, Bhoi, Maram).
    """
    w = word.lower().strip()
    cognates = {"sohra": w}
    for d in ["pnar", "war", "bhoi", "maram"]:
        res = lookup_dialect(w, d)
        if res:
            cognates[d] = res["dialect_word"]
        else:
            cognates[d] = w
    return cognates

def translate_dialect(text: str, from_dialect: str = "sohra", to_dialect: str = "pnar") -> str:
    """
    Translate text across Khasi dialects using dedicated sub-lexicon mappings.
    """
    from_d = from_dialect.lower().strip()
    to_d = to_dialect.lower().strip()

    if from_d == to_d or not text.strip():
        return text

    words = text.split()
    translated_words = []

    for token in words:
        punct_prefix = ""
        punct_suffix = ""
        w = token
        while w and w[0] in "([{\"'`«":
            punct_prefix += w[0]
            w = w[1:]
        while w and w[-1] in ".,?!;:\"'»)}]":
            punct_suffix = w[-1] + punct_suffix
            w = w[:-1]

        if not w:
            translated_words.append(token)
            continue

        low = w.lower()
        # 1. Resolve from source dialect to Standard Sohra
        sohra_form = low
        if from_d != "sohra":
            source_entry = lookup_dialect(low, from_d)
            if source_entry:
                sohra_form = source_entry["standard_khasi"].lower()

        # 2. Resolve from Sohra to target dialect
        if to_d == "sohra":
            target_form = sohra_form
        else:
            target_entry = lookup_dialect(sohra_form, to_d)
            if target_entry:
                target_form = target_entry["dialect_word"]
            else:
                target_form = sohra_form

        # Preserve capitalization
        if w.isupper():
            target_form = target_form.upper()
        elif w[0].isupper():
            target_form = target_form.capitalize()

        translated_words.append(punct_prefix + target_form + punct_suffix)

    return " ".join(translated_words)

def get_dialect_statistics() -> Dict[str, Any]:
    """Return statistical summary of all dialect sub-lexicons."""
    stats = {}
    for d, info in DIALECT_INFO.items():
        if info.get("file"):
            lex = load_dialect_lexicon(d)
            stats[d] = {
                "name": info["name"],
                "region": info["region"],
                "word_count": len(lex),
                "documented_shifts": len(set(x.get("phonetic_shift", "") for x in lex))
            }
        else:
            stats[d] = {
                "name": info["name"],
                "region": info["region"],
                "word_count": "State Standard / Colloquial"
            }
    return stats
