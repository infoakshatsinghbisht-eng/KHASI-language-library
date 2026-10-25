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

KHASI_GRAMMAR_EN: Dict[str, str] = {
    "u": "the", "ka": "the", "i": "the", "ki": "the",
    "bad": "and", "hynrei": "but", "la": "", "yn": "will",
    "da": "by", "ha": "in", "sha": "to", "na": "from",
    "jong": "of", "ïa": "", "ia": "", "ba": "that",
    "kaba": "which", "uba": "who", "kiba": "who", "kiba": "which",
    "dei": "must", "ban": "to", "nga": "I", "ngi": "we",
    "phi": "you", "me": "you", "pha": "you", "shisha": "truly",
    "shibun": "very", "ym": "not", "don": "has", "em": "no", "hooid": "yes",
    "mynta": "now", "lashai": "tomorrow", "mynnor": "yesterday", "shnong": "village"
}

KHASI_GRAMMAR_HI: Dict[str, str] = {
    "u": "वह", "ka": "वह", "i": "छोटा", "ki": "वे",
    "bad": "और", "hynrei": "किंतु", "la": "", "yn": "गा",
    "da": "से", "ha": "में", "sha": "की ओर", "na": "से",
    "jong": "का", "ïa": "को", "ia": "को", "ba": "कि",
    "kaba": "जो", "uba": "जो", "kiba": "जो",
    "dei": "चाहिए", "ban": "के लिए", "nga": "मैं", "ngi": "हम",
    "phi": "आप", "me": "तू", "pha": "तू", "shisha": "सचमुच",
    "shibun": "बहुत", "ym": "नहीं", "don": "है", "em": "नहीं", "hooid": "हाँ",
    "mynta": "अब", "lashai": "कल", "shnong": "गाँव"
}

def _clean_gloss(text: str, is_hindi: bool = False) -> str:
    if not text:
        return ""
    clean = re.sub(r"\[.*?\]", "", text)
    clean = re.sub(r"\(.*?\)", "", clean)
    clean = re.sub(r"\b(v\.t\.|v\.i\.|v\.|n\.|adj\.|adv\.|prep\.|conj\.|interj\.|pron\.)\b", "", clean, flags=re.I)
    clean = re.sub(r"\b(v\.|to)\s+", "", clean, flags=re.I)
    parts = re.split(r"[/;,]", clean)
    chosen = parts[0].strip()
    chosen = re.sub(r"^\d+\.\s*", "", chosen)
    for noise in ["(खासी शब्द)", "(खासी साहित्यिक शब्द)", "का खासी अनुवाद", "का अनुवाद"]:
        chosen = chosen.replace(noise, "")
    chosen = chosen.strip(".,!?:\"' —-_\\")
    return chosen

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
            clean_tok = tok.strip(".,!?;:\"'()[]{}«»")
            low_tok = clean_tok.lower()
            if low_tok in KHASI_GRAMMAR_EN:
                gram = KHASI_GRAMMAR_EN[low_tok]
                if gram:
                    translated_tokens.append(gram)
                found_count += 1
                continue
            entry = d.lookup(clean_tok)
            if entry and entry.get("english"):
                gloss = _clean_gloss(entry["english"])
                if gloss:
                    translated_tokens.append(gloss)
                    found_count += 1
                else:
                    translated_tokens.append(tok)
            else:
                translated_tokens.append(tok)
        if found_count > 0:
            res_str = " ".join(translated_tokens)
            res_str = re.sub(r"\s+", " ", res_str).strip()
            return TranslationResult(res_str, "khasi", "en", max(round(found_count / len(tokens), 2), 0.60), dialect)
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
            clean_tok = tok.strip(".,!?;:\"'()[]{}«»")
            low_tok = clean_tok.lower()
            if low_tok in KHASI_GRAMMAR_HI:
                gram = KHASI_GRAMMAR_HI[low_tok]
                if gram:
                    translated_tokens.append(gram)
                found_count += 1
                continue
            entry = d.lookup(clean_tok)
            if entry and entry.get("hindi"):
                gloss = _clean_gloss(entry["hindi"], is_hindi=True)
                if gloss:
                    translated_tokens.append(gloss)
                    found_count += 1
                else:
                    translated_tokens.append(tok)
            else:
                translated_tokens.append(tok)
        if found_count > 0:
            res_str = " ".join(translated_tokens)
            res_str = re.sub(r"\s+", " ", res_str).strip()
            return TranslationResult(res_str, "khasi", "hi", max(round(found_count / len(tokens), 2), 0.60), dialect)
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
