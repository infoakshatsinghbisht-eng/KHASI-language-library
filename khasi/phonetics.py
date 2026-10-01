# -*- coding: utf-8 -*-
"""Khasi Phonetics, Orthography, Normalization & Script Utilities."""

import re
import unicodedata
from typing import List, Dict, Set, Optional

from .constants import (
    KHASI_VOWELS,
    KHASI_CONSONANTS,
    KHASI_SPECIAL_CHARS,
    KHASI_ALPHABET,
    NON_INDIGENOUS_LETTERS
)

APOSTROPHE_PATTERN = re.compile(r"[`’´‘ʻʼ]")

# Common ASCII approximations to formal Khasi diacritic orthography
ASCII_TO_KHASI_DIACRITICS: Dict[str, str] = {
    "iing": "ïing",
    "iap": "ïap",
    "ia": "ïa",
    "ieit": "ïeit",
    "id": "ïd",
    "it": "ït",
    "itkhmih": "ïtkhmih",
    "iangi": "ïangi",
    "iapngan": "ïapngan",
    "iohi": "ïohi",
    "iong": "ïong",
    "iarap": "ïarap",
    "iad": "ïad",
    "iaprem": "ïaprem",
    "shniuh": "shñiuh",
    "shnong": "shnong",
}

# Spoken/informal contractions to full grammatical particles
CONTRACTIONS_MAP: Dict[str, str] = {
    "nga'm": "nga ym",
    "ngam": "nga ym",
    "u'm": "u ym",
    "um": "u ym",
    "ka'm": "ka ym",
    "kam": "ka ym",
    "ki'm": "ki ym",
    "kim": "ki ym",
    "phi'm": "phi ym",
    "phim": "phi ym",
    "me'm": "me ym",
    "pha'm": "pha ym",
    "nga'n": "nga yn",
    "ngan": "nga yn",
    "u'n": "u yn",
    "un": "u yn",
    "ka'n": "ka yn",
    "kan": "ka yn",
    "ki'n": "ki yn",
    "kin": "ki yn",
    "phi'n": "phi yn",
    "phin": "phi yn",
    "ngi'n": "ngi yn",
    "ngin": "ngi yn",
    "ngi'm": "ngi ym",
    "ngim": "ngi ym",
}

# Transliteration mappings between Khasi Latin and Devanagari
KHASI_LATIN_TO_DEV_MAP = {
    "a": "अ", "e": "ए", "i": "इ", "ï": "ई", "o": "ओ", "u": "उ",
    "b": "ब", "k": "क", "d": "द", "g": "ग", "ng": "ङ", "h": "ह",
    "j": "ज", "l": "ल", "m": "म", "n": "न", "ñ": "ञ", "p": "प",
    "r": "र", "s": "स", "t": "त", "w": "व", "y": "य",
    "sh": "श", "kh": "ख", "ph": "फ", "th": "थ"
}

DEV_TO_KHASI_LATIN_MAP = {v: k for k, v in KHASI_LATIN_TO_DEV_MAP.items()}

def normalize(text: str) -> str:
    """
    Standardize Khasi text:
    - Normalizes Unicode to NFC
    - Unifies curly/typographical apostrophes
    - Restores diacritics ('ï', 'ñ') for common mis-transcribed words
    - Cleans extra whitespace
    """
    if not text:
        return ""

    # Unicode NFC normalization
    result = unicodedata.normalize("NFC", text)
    # Standardize apostrophes
    result = APOSTROPHE_PATTERN.sub("'", result)

    # Word-level diacritic restoration
    def replace_word(m: re.Match) -> str:
        w = m.group(0)
        low = w.lower()
        if low in ASCII_TO_KHASI_DIACRITICS:
            rep = ASCII_TO_KHASI_DIACRITICS[low]
            if w.isupper():
                return rep.upper()
            elif w[0].isupper():
                return rep.capitalize()
            return rep
        return w

    result = re.sub(r"\b[a-zA-ZïÏñÑ']+\b", replace_word, result)
    result = re.sub(r"[ \t]+", " ", result).strip()
    return result

def expand_contractions(text: str) -> str:
    """Expand Khasi colloquial contractions into full grammatical words."""
    if not text:
        return ""
    words = text.split()
    expanded = []
    for w in words:
        low = w.lower().strip(".,!?;:\"'")
        if low in CONTRACTIONS_MAP:
            rep = CONTRACTIONS_MAP[low]
            expanded.append(rep)
        else:
            expanded.append(w)
    return " ".join(expanded)

def detect_script(text: str) -> str:
    """Detect whether input is in Latin (standard Khasi) or Devanagari transliteration."""
    if not text:
        return "latin"
    if re.search(r"[\u0900-\u097F]", text):
        return "devanagari_translit"
    return "latin"

def tokenize(text: str, lower: bool = False, keep_punct: bool = True) -> List[str]:
    """Tokenize Khasi text preserving contractions, hyphens, and diacritics."""
    if not text:
        return []
    if keep_punct:
        pattern = re.compile(r"[a-zA-ZïÏñÑ]+(?:'[a-zA-ZïÏñÑ]+)?(?:-[a-zA-ZïÏñÑ]+)*|[0-9]+|[^\w\s]")
    else:
        pattern = re.compile(r"[a-zA-ZïÏñÑ]+(?:'[a-zA-ZïÏñÑ]+)?(?:-[a-zA-ZïÏñÑ]+)*")
    tokens = pattern.findall(text)
    if lower:
        return [t.lower() for t in tokens]
    return tokens

def syllables(word: str) -> List[str]:
    """Break a Khasi word into phonotactic syllable clusters."""
    clean = word.lower().strip(".,!?;:'\"-")
    if not clean:
        return []
    if len(clean) <= 3:
        return [clean]

    # Khasi vowels including ï
    vowel_regex = r"[aeiïou]+"
    parts = []
    last_idx = 0
    matches = list(re.finditer(vowel_regex, clean))
    if not matches:
        return [clean]

    for i, match in enumerate(matches):
        start, end = match.span()
        if i == 0:
            syl_start = 0
        else:
            prev_end = matches[i - 1].end()
            inter_consonants = clean[prev_end:start]
            if len(inter_consonants) <= 1:
                syl_start = prev_end
            else:
                syl_start = prev_end + (len(inter_consonants) // 2)
            parts.append(clean[last_idx:syl_start])
            last_idx = syl_start

    parts.append(clean[last_idx:])
    return [p for p in parts if p]

def latin_to_devanagari(text: str) -> str:
    """Transliterate Khasi Latin script into approximate Devanagari."""
    norm = normalize(text)
    out = norm
    # Multi-letter digraphs first
    digraphs = {"ng": "ङ", "kh": "ख", "ph": "फ", "th": "थ", "sh": "श", "ñ": "ञ", "ï": "ई"}
    for k, v in digraphs.items():
        out = re.sub(k, v, out, flags=re.IGNORECASE)
    # Single letters
    for k, v in KHASI_LATIN_TO_DEV_MAP.items():
        if k not in digraphs:
            out = re.sub(k, v, out, flags=re.IGNORECASE)
    return out

def devanagari_to_latin(text: str) -> str:
    """Transliterate Devanagari representation of Khasi back to Latin."""
    out = text
    for dev, lat in DEV_TO_KHASI_LATIN_MAP.items():
        out = out.replace(dev, lat)
    return out

def is_khasi_word(word: str) -> bool:
    """Validate if a word adheres to Khasi orthography."""
    w = word.lower().strip(".,!?;:'\"-")
    if not w:
        return False
    for ch in w:
        if ch in NON_INDIGENOUS_LETTERS:
            return False
    return True

def has_khasi_diacritics(text: str) -> bool:
    """Check if text contains authentic Khasi diacritics (ï, ñ)."""
    return any(ch in KHASI_SPECIAL_CHARS for ch in text)
