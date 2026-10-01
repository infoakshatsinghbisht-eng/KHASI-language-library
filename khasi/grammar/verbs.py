# -*- coding: utf-8 -*-
"""Khasi Verbs, Tense-Aspect-Mood (TAM) Conjugation, Causatives & Derivations."""

from typing import Dict, List, Any, Optional, Tuple

# Core verbs with meanings
CORE_KHASI_VERBS: List[Dict[str, str]] = [
    {"lemma": "wan", "english": "come", "hindi": "आना"},
    {"lemma": "leit", "english": "go", "hindi": "जाना"},
    {"lemma": "bam", "english": "eat", "hindi": "खाना"},
    {"lemma": "dih", "english": "drink", "hindi": "पीना"},
    {"lemma": "thoh", "english": "write", "hindi": "लिखना"},
    {"lemma": "pule", "english": "read / study", "hindi": "पढ़ना"},
    {"lemma": "trei", "english": "work", "hindi": "काम करना"},
    {"lemma": "thiah", "english": "sleep", "hindi": "सोना"},
    {"lemma": "ïaid", "english": "walk", "hindi": "चलना"},
    {"lemma": "kren", "english": "speak / talk", "hindi": "बोलना"},
    {"lemma": "ïoh", "english": "receive / get", "hindi": "पाना"},
    {"lemma": "ïohi", "english": "see", "hindi": "देखना"},
    {"lemma": "sngap", "english": "listen", "hindi": "सुनना"},
    {"lemma": "ieit", "english": "love", "hindi": "प्यार करना"},
    {"lemma": "long", "english": "be / exist", "hindi": "होना"},
    {"lemma": "shem", "english": "find / discover", "hindi": "पाना / खोजना"},
    {"lemma": "hikai", "english": "teach / learn", "hindi": "सिखाना / सीखना"},
    {"lemma": "ïap", "english": "die", "hindi": "मरना"},
    {"lemma": "im", "english": "live", "hindi": "जीना"},
    {"lemma": "bha", "english": "be good / heal", "hindi": "अच्छा होना"},
]

# Derivational prefixes in Khasi
PREFIX_SPECS = {
    "jing": {"type": "nominalizer", "meaning": "abstract noun / concept"},
    "pyn": {"type": "causative", "meaning": "cause to perform / become"},
    "nong": {"type": "agentive", "meaning": "doer / performer of action"},
    "sngew": {"type": "experiential", "meaning": "sensory / perception / feeling"},
    "mar": {"type": "reciprocal", "meaning": "reciprocal / distributive"},
    "shi": {"type": "unit", "meaning": "one / singular quantity"}
}

def extract_root(word: str) -> str:
    """Extract root morpheme by peeling productive Khasi prefixes."""
    w = word.lower().strip(".,!?;:'\"-")
    for pref in ["jing", "pyn", "nong", "sngew", "mar", "shi"]:
        if w.startswith(pref) and len(w) > len(pref) + 2:
            return w[len(pref):]
    return w

def causative(verb: str) -> str:
    """Derive causative verb form using prefix 'pyn-'."""
    root = extract_root(verb)
    return f"pyn{root}"

def nominalize(word: str) -> str:
    """Derive abstract noun from verb/adjective using prefix 'jing-'."""
    root = extract_root(word)
    return f"jing{root}"

def agent_noun(verb: str) -> str:
    """Derive agent / doer noun using prefix 'nong-'."""
    root = extract_root(verb)
    return f"nong{root}"

def experiential(verb: str) -> str:
    """Derive sensory/feeling word using prefix 'sngew-'."""
    root = extract_root(verb)
    return f"sngew{root}"

def conjugate(
    verb: str,
    tense: str = "present",
    pronoun: str = "nga",
    aspect: str = "simple",
    negative: bool = False
) -> str:
    """
    Synthesize authentic Khasi verbal clauses across tense, aspect, and mood.
    
    Args:
        verb: Root verb (e.g. 'wan', 'leit', 'bam')
        tense: 'present', 'past', 'future', 'future_definite', 'habitual'
        pronoun: Subject pronoun ('nga', 'ngi', 'phi', 'u', 'ka', 'ki', etc.)
        aspect: 'simple', 'progressive' ('dang'), 'potential' ('lah'), 'obligation' ('dei')
        negative: Whether the sentence is negated ('ym' / 'khlem')
    """
    v = verb.strip()
    pr = pronoun.strip().lower()

    # Contraction table for pronoun + negation
    neg_pronouns = {
        "nga": "ngam", "ngi": "ngim", "phi": "phim", "me": "mem",
        "pha": "pham", "u": "um", "ka": "kam", "i": "im", "ki": "kim"
    }

    # Contraction table for pronoun + future yn
    fut_pronouns = {
        "nga": "ngan", "ngi": "ngin", "phi": "phin", "me": "men",
        "pha": "phan", "u": "un", "ka": "kan", "i": "in", "ki": "kin"
    }

    # 1. Negative constructions
    if negative:
        neg_subj = neg_pronouns.get(pr, f"{pr} ym")
        if tense == "past":
            return f"{pr} khlem {v}"
        elif tense == "future":
            return f"{neg_subj} wan" if v == "wan" else f"{neg_subj} {v}"
        elif aspect == "progressive":
            return f"{neg_subj} dang {v}"
        elif aspect == "potential":
            return f"{neg_subj} lah ban {v}"
        elif aspect == "obligation":
            return f"{neg_subj} dei ban {v}"
        elif tense == "habitual":
            return f"{neg_subj} ju {v}"
        else:
            return f"{neg_subj} {v}"

    # 2. Affirmative constructions
    if aspect == "potential":
        return f"{pr} lah ban {v}"
    if aspect == "obligation":
        return f"{pr} dei ban {v}"

    if tense == "past":
        return f"{pr} la {v}"
    elif tense == "future":
        fut_subj = fut_pronouns.get(pr, f"{pr} yn")
        return f"{fut_subj} {v}"
    elif tense == "future_definite":
        return f"{pr} daw {v}"
    elif tense == "habitual":
        return f"{pr} ju {v}"
    elif aspect == "progressive" or tense == "progressive":
        return f"{pr} dang {v}"
    else:  # simple present
        return f"{pr} {v}"
