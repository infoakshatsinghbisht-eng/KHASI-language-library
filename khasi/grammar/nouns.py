# -*- coding: utf-8 -*-
"""Khasi Nouns, Gender Articles, Declensions, and Classifiers."""

from typing import Dict, List, Any, Optional

class KhasiNoun:
    def __init__(self, lemma: str, gender: str, english: str, hindi: str):
        self.lemma = lemma
        self.gender = gender  # "u" (masc), "ka" (fem), "i" (diminutive)
        self.english = english
        self.hindi = hindi

    @property
    def full_singular(self) -> str:
        return f"{self.gender} {self.lemma}"

    @property
    def full_plural(self) -> str:
        return f"ki {self.lemma}"

    @property
    def full_diminutive(self) -> str:
        return f"i {self.lemma}"

    def declensions(self) -> Dict[str, str]:
        """Generate case forms with prepositions."""
        return {
            "nominative_sg": f"{self.gender} {self.lemma}",
            "nominative_pl": f"ki {self.lemma}",
            "accusative_sg": f"ïa {self.gender} {self.lemma}",
            "accusative_pl": f"ïa ki {self.lemma}",
            "genitive_sg": f"jong {self.gender} {self.lemma}",
            "genitive_pl": f"jong ki {self.lemma}",
            "locative_sg": f"ha {self.gender} {self.lemma}",
            "locative_pl": f"ha ki {self.lemma}",
            "allative_sg": f"sha {self.gender} {self.lemma}",
            "allative_pl": f"sha ki {self.lemma}",
            "ablative_sg": f"na {self.gender} {self.lemma}",
            "ablative_pl": f"na ki {self.lemma}",
            "instrumental_sg": f"da {self.gender} {self.lemma}",
            "instrumental_pl": f"da ki {self.lemma}",
            "comitative_sg": f"bad {self.gender} {self.lemma}",
            "comitative_pl": f"bad ki {self.lemma}",
        }

CORE_KHASI_NOUNS: List[KhasiNoun] = [
    KhasiNoun("briew", "u", "man / person", "आदमी / मनुष्य"),
    KhasiNoun("kynthei", "ka", "woman", "महिला / औरत"),
    KhasiNoun("khynnah", "u", "boy / child", "लड़का / बच्चा"),
    KhasiNoun("khunlung", "i", "baby / infant", "शिशु / नन्हा बच्चा"),
    KhasiNoun("ïing", "ka", "house / home", "घर / मकान"),
    KhasiNoun("lum", "u", "mountain / hill", "पहाड़"),
    KhasiNoun("wah", "ka", "river", "नदी"),
    KhasiNoun("um", "ka", "water", "पानी / जल"),
    KhasiNoun("ding", "ka", "fire", "आग"),
    KhasiNoun("sngi", "ka", "sun / day", "सूर्य / दिन"),
    KhasiNoun("bnai", "u", "moon / month", "चाँद / महीना"),
    KhasiNoun("khlur", "u", "star", "तारा"),
    KhasiNoun("dieng", "u", "tree / wood", "पेड़ / लकड़ी"),
    KhasiNoun("tiew", "u", "flower", "फूल"),
    KhasiNoun("sim", "ka", "bird", "पक्षी / चिड़िया"),
    KhasiNoun("ksew", "u", "dog", "कुत्ता"),
    KhasiNoun("miaw", "ka", "cat", "बिल्ली"),
    KhasiNoun("masi", "ka", "cow", "गाय"),
    KhasiNoun("kulai", "u", "horse", "घोड़ा"),
    KhasiNoun("kot", "ka", "book", "किताब / पुस्तक"),
    KhasiNoun("shnong", "ka", "village / town", "गाँव / नगर"),
    KhasiNoun("ktien", "ka", "language / word", "भाषा / शब्द"),
    KhasiNoun("jingim", "ka", "life", "जीवन"),
    KhasiNoun("jingieit", "ka", "love", "प्रेम / प्यार"),
    KhasiNoun("hok", "ka", "righteousness / truth / justice", "सत्य / धर्म / न्याय"),
    KhasiNoun("blei", "u", "God / deity", "ईश्वर / भगवान"),
]

def pluralize(word: str, gender: str = "ka") -> str:
    """Return the pluralized form of a Khasi noun using article 'ki'."""
    clean = word.strip()
    # Strip existing singular article if present
    for art in ["u ", "ka ", "i "]:
        if clean.startswith(art):
            clean = clean[len(art):].strip()
            break
    return f"ki {clean}"

def decline_noun(noun: str, gender: str = "ka") -> Dict[str, str]:
    """Generate all prepositional declension forms for a given noun."""
    clean = noun.strip()
    for art in ["u ", "ka ", "i ", "ki "]:
        if clean.startswith(art):
            gender = art.strip()
            clean = clean[len(art):].strip()
            break
    kn = KhasiNoun(clean, gender, clean, clean)
    return kn.declensions()

def make_diminutive(noun: str) -> str:
    """Attach the affectionate diminutive article 'i' to a noun."""
    clean = noun.strip()
    for art in ["u ", "ka ", "ki "]:
        if clean.startswith(art):
            clean = clean[len(art):].strip()
            break
    return f"i {clean}"

def make_augmentative(noun: str) -> str:
    """Make noun augmentative using Khasi modifiers."""
    clean = noun.strip()
    return f"{clean} heh"
