# -*- coding: utf-8 -*-
"""
Khasi Adjectives, Agreement with Relative Particle 'ba-', Comparatives & Superlatives.
Based on H. Roberts (1891) and native Khasi syntactical rules:
- Adjectives follow the noun: 'ka ïing heh' (the big house)
- Attributive agreement with 'ba-': 'u briew ba-bha' (the good man)
- Comparative with 'kham ... ban ïa': 'kham heh ban ïa' (bigger than)
- Superlative with 'ba ... tam': 'ba heh tam' (the biggest)
"""

from typing import Dict, List, Any, Optional

CORE_KHASI_ADJECTIVES: List[Dict[str, str]] = [
    {"lemma": "bha", "english": "good / well", "hindi": "अच्छा"},
    {"lemma": "sniew", "english": "bad / evil", "hindi": "बुरा / खराब"},
    {"lemma": "heh", "english": "big / large", "hindi": "बड़ा"},
    {"lemma": "rit", "english": "small / little", "hindi": "छोटा"},
    {"lemma": "jngai", "english": "far / distant", "hindi": "दूर"},
    {"lemma": "jan", "english": "near / close", "hindi": "पास / निकट"},
    {"lemma": "stad", "english": "wise / clever / intelligent", "hindi": "बुद्धिमान"},
    {"lemma": "bieit", "english": "foolish / ignorant", "hindi": "मूर्ख / अज्ञानी"},
    {"lemma": "khlain", "english": "strong / healthy", "hindi": "बलवान / स्वस्थ"},
    {"lemma": "tlot", "english": "weak / feeble", "hindi": "कमजोर"},
    {"lemma": "shlur", "english": "brave / courageous", "hindi": "बहादुर / साहसी"},
    {"lemma": "bhabriew", "english": "beautiful / handsome", "hindi": "सुंदर / खूबसूरत"},
    {"lemma": "suk", "english": "peaceful / happy / easy", "hindi": "शांत / सुखी / सरल"},
    {"lemma": "shitom", "english": "difficult / painful / suffering", "hindi": "कठिन / कष्टकारी"},
    {"lemma": "khriat", "english": "cold / chilly", "hindi": "ठंडा"},
    {"lemma": "khluit", "english": "hot / boiling", "hindi": "गर्म"},
    {"lemma": "lieh", "english": "white", "hindi": "सफेद"},
    {"lemma": "ïong", "english": "black / dark", "hindi": "काला"},
    {"lemma": "saw", "english": "red", "hindi": "लाल"},
    {"lemma": "jyrngam", "english": "green", "hindi": "हरा"},
    {"lemma": "stem", "english": "yellow", "hindi": "पीला"},
    {"lemma": "thymmai", "english": "new / fresh", "hindi": "नया"},
    {"lemma": "rim", "english": "old (objects/time)", "hindi": "पुराना"},
    {"lemma": "tymmen", "english": "old / elderly (people)", "hindi": "वृद्ध / बुजुर्ग"},
    {"lemma": "lung", "english": "young / tender", "hindi": "कोमल / नन्हा"},
]

def make_attributive(adjective: str) -> str:
    """Attach the relative marker 'ba-' to make adjective attributive (e.g. 'bha' -> 'ba-bha')."""
    clean = adjective.strip().lower()
    if clean.startswith("ba-") or clean.startswith("ba "):
        return clean
    return f"ba-{clean}"

def make_comparative(adjective: str, comparison_target: Optional[str] = None) -> str:
    """
    Form comparative degree:
    'kham <adj>' (e.g. 'kham heh' = bigger)
    'kham <adj> ban ïa <target>' (e.g. 'kham heh ban ïa kata' = bigger than that)
    """
    clean = adjective.strip().lower()
    comp = f"kham {clean}"
    if comparison_target:
        clean_target = comparison_target.strip()
        if not clean_target.startswith("ïa "):
            clean_target = f"ïa {clean_target}"
        return f"{comp} ban {clean_target}"
    return comp

def make_superlative(adjective: str) -> str:
    """Form superlative degree: 'ba-<adj> tam' (e.g. 'ba-heh tam' = biggest)."""
    attr = make_attributive(adjective)
    return f"{attr} tam"

def make_intensified(adjective: str, degree: str = "very") -> str:
    """Attach Khasi post-adjectival intensifiers: 'eh' (very), 'shibun' (much)."""
    clean = adjective.strip().lower()
    if degree == "extreme":
        return f"{clean} eh eh"
    elif degree == "much":
        return f"{clean} shibun"
    else:  # standard very
        return f"{clean} eh"

def qualify_noun(noun_phrase: str, adjective: str, attributive: bool = True) -> str:
    """
    Combine noun phrase and adjective according to Khasi post-nominal syntax.
    Example:
        qualify_noun("ka ïing", "heh", attributive=False) -> "ka ïing heh"
        qualify_noun("u briew", "bha", attributive=True)  -> "u briew ba-bha"
    """
    n = noun_phrase.strip()
    if attributive:
        adj_str = make_attributive(adjective)
    else:
        adj_str = adjective.strip()
    return f"{n} {adj_str}"
