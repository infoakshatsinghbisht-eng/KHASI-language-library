# -*- coding: utf-8 -*-
"""Khasi Main Translation Engine."""

import re
from typing import Dict, List, Any, Optional, NamedTuple
from .rule_based import (
    CONVERSATIONAL_HINGLISH_KHASI_MAP,
    CONVERSATIONAL_EN_KHASI_MAP,
    CONVERSATIONAL_HI_KHASI_MAP,
    CONVERSATIONAL_KHASI_EN_MAP,
    CONVERSATIONAL_KHASI_HI_MAP,
    apply_dialect,
)
from ..lexicon.dictionary import KhasiDictionary

class TranslationResult(NamedTuple):
    text: str
    source_lang: str
    target_lang: str
    confidence: float
    dialect: str

    def __repr__(self) -> str:
        return f"<TranslationResult text='{self.text}' dialect='{self.dialect}' conf={self.confidence:.2f}>"

_DICT: Optional[KhasiDictionary] = None

def _get_dict() -> KhasiDictionary:
    global _DICT
    if _DICT is None:
        _DICT = KhasiDictionary()
    return _DICT

def translate(
    text: str,
    source: str = "auto",
    target: str = "khasi",
    dialect: str = "sohra"
) -> TranslationResult:
    """
    Translate English, Hindi, Hinglish, or Khasi text bidirectionally.
    
    Args:
        text: Input sentence or phrase
        source: 'auto', 'en', 'hi', 'hinglish', or 'khasi'
        target: 'khasi' (default), 'en', or 'hi'
        dialect: 'sohra' (standard), 'shillong', 'pnar', 'war', 'bhoi'
    """
    clean = text.strip()
    if not clean:
        return TranslationResult("", source, target, 1.0, dialect)

    clean_low = clean.lower()
    clean_no_punct = re.sub(r"[^\w\s]", "", clean_low)

    # A. Target is English (Khasi -> English)
    if target.lower() in ("en", "english"):
        for pattern, en_target in CONVERSATIONAL_KHASI_EN_MAP:
            if re.search(pattern, clean_low) or re.search(pattern, clean_no_punct):
                matched = re.sub(pattern, en_target, clean_low) if r"\1" in en_target else en_target
                return TranslationResult(matched, "khasi", "en", 0.98, dialect)

        # Word-by-word lookup
        d = _get_dict()
        tokens = clean.split()
        translated_tokens = []
        found_count = 0
        for tok in tokens:
            clean_tok = tok.strip(".,!?;:\"'")
            entry = d.lookup(clean_tok)
            if entry and entry.get("english"):
                translated_tokens.append(entry["english"].split("/")[0].strip())
                found_count += 1
            else:
                translated_tokens.append(tok)
        if found_count > 0:
            return TranslationResult(" ".join(translated_tokens), "khasi", "en", max(round(found_count / len(tokens), 2), 0.60), dialect)
        return TranslationResult(clean, "khasi", "en", 0.40, dialect)

    # B. Target is Hindi (Khasi -> Hindi)
    if target.lower() in ("hi", "hindi"):
        for pattern, hi_target in CONVERSATIONAL_KHASI_HI_MAP:
            if re.search(pattern, clean_low) or re.search(pattern, clean_no_punct):
                matched = re.sub(pattern, hi_target, clean_low) if r"\1" in hi_target else hi_target
                return TranslationResult(matched, "khasi", "hi", 0.98, dialect)

        # Word-by-word lookup
        d = _get_dict()
        tokens = clean.split()
        translated_tokens = []
        found_count = 0
        for tok in tokens:
            clean_tok = tok.strip(".,!?;:\"'")
            entry = d.lookup(clean_tok)
            if entry and entry.get("hindi"):
                translated_tokens.append(entry["hindi"].split("/")[0].strip())
                found_count += 1
            else:
                translated_tokens.append(tok)
        if found_count > 0:
            return TranslationResult(" ".join(translated_tokens), "khasi", "hi", max(round(found_count / len(tokens), 2), 0.60), dialect)
        return TranslationResult(clean, "khasi", "hi", 0.40, dialect)

    # 1. Match Hinglish expressions
    for pattern, kh_target in CONVERSATIONAL_HINGLISH_KHASI_MAP:
        if re.search(pattern, clean_low) or re.search(pattern, clean_no_punct):
            matched = re.sub(pattern, kh_target, clean_low) if r"\1" in kh_target else kh_target
            return TranslationResult(apply_dialect(matched, dialect), "hinglish", target, 0.98, dialect)

    # 2. Match English expressions
    for pattern, kh_target in CONVERSATIONAL_EN_KHASI_MAP:
        if re.search(pattern, clean_low) or re.search(pattern, clean_no_punct):
            matched = re.sub(pattern, kh_target, clean_low) if r"\1" in kh_target else kh_target
            return TranslationResult(apply_dialect(matched, dialect), "en", target, 0.98, dialect)

    # 3. Match Hindi expressions
    for pattern, kh_target in CONVERSATIONAL_HI_KHASI_MAP:
        if re.search(pattern, clean) or re.search(pattern, clean_no_punct):
            matched = re.sub(pattern, kh_target, clean) if r"\1" in kh_target else kh_target
            return TranslationResult(apply_dialect(matched, dialect), "hi", target, 0.98, dialect)

    # 4. Word-by-word lexical fallback
    d = _get_dict()
    tokens = clean.split()
    translated_tokens = []
    found_count = 0

    for tok in tokens:
        clean_tok = tok.strip(".,!?;:\"'")
        res = d.search(clean_tok)
        if res:
            translated_tokens.append(res[0]["khasi"])
            found_count += 1
        else:
            translated_tokens.append(tok)

    if found_count > 0:
        composed = " ".join(translated_tokens)
        conf = round(found_count / len(tokens), 2)
        return TranslationResult(apply_dialect(composed, dialect), source, target, max(conf, 0.60), dialect)

    # 5. Direct return if already Khasi or untranslatable
    return TranslationResult(apply_dialect(clean, dialect), source, target, 0.50, dialect)
