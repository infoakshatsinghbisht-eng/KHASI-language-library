# -*- coding: utf-8 -*-
"""Khasi Pronouns, Person/Number Paradigm, Demonstratives & Interrogatives."""

from typing import Dict, List, Any, Optional

PRONOUN_TABLE: Dict[str, Dict[str, Any]] = {
    "1sg": {
        "pronoun": "nga",
        "english": "I / me",
        "hindi": "मैं / मुझे",
        "possessive": "jong nga",
        "contracted_neg": "ngam",
        "contracted_fut": "ngan"
    },
    "1pl": {
        "pronoun": "ngi",
        "english": "we / us",
        "hindi": "हम / हमें",
        "possessive": "jong ngi",
        "contracted_neg": "ngim",
        "contracted_fut": "ngin"
    },
    "2sg_masc": {
        "pronoun": "me",
        "english": "you (familiar masculine)",
        "hindi": "तू (पुल्लिंग)",
        "possessive": "jong me",
        "contracted_neg": "mem",
        "contracted_fut": "men"
    },
    "2sg_fem": {
        "pronoun": "pha",
        "english": "you (familiar feminine)",
        "hindi": "तू (स्त्रीलिंग)",
        "possessive": "jong pha",
        "contracted_neg": "pham",
        "contracted_fut": "phan"
    },
    "2_polite": {
        "pronoun": "phi",
        "english": "you (respectful singular / plural)",
        "hindi": "आप / तुम",
        "possessive": "jong phi",
        "contracted_neg": "phim",
        "contracted_fut": "phin"
    },
    "3sg_masc": {
        "pronoun": "u",
        "english": "he / him / it (masculine)",
        "hindi": "वह / उसे (पुल्लिंग)",
        "possessive": "jong u",
        "contracted_neg": "um",
        "contracted_fut": "un"
    },
    "3sg_fem": {
        "pronoun": "ka",
        "english": "she / her / it (feminine)",
        "hindi": "वह / उसे (स्त्रीलिंग)",
        "possessive": "jong ka",
        "contracted_neg": "kam",
        "contracted_fut": "kan"
    },
    "3sg_dim": {
        "pronoun": "i",
        "english": "s/he (affectionate / child / diminutive)",
        "hindi": "वह (स्नेहपूर्ण / नन्हा)",
        "possessive": "jong i",
        "contracted_neg": "im",
        "contracted_fut": "in"
    },
    "3pl": {
        "pronoun": "ki",
        "english": "they / them",
        "hindi": "वे / उन्हें",
        "possessive": "jong ki",
        "contracted_neg": "kim",
        "contracted_fut": "kin"
    }
}

DEMONSTRATIVES: Dict[str, Dict[str, str]] = {
    "near_this": {
        "masc": "une",
        "fem": "kane",
        "dim": "ine",
        "pl": "kine",
        "english": "this / these"
    },
    "medial_that": {
        "masc": "uto",
        "fem": "kato",
        "dim": "ito",
        "pl": "kito",
        "english": "that / those (near or visible)"
    },
    "distal_that": {
        "masc": "utai",
        "fem": "katai",
        "dim": "itai",
        "pl": "kitai",
        "english": "that / those (distant)"
    }
}

INTERROGATIVES: Dict[str, Dict[str, str]] = {
    "who": {"khasi": "mano", "hindi": "कौन", "english": "who"},
    "what": {"khasi": "kaei", "hindi": "क्या", "english": "what"},
    "where": {"khasi": "shano", "hindi": "कहाँ (किस तरफ)", "english": "where to"},
    "where_at": {"khasi": "haei", "hindi": "कहाँ (स्थान पर)", "english": "where at"},
    "where_from": {"khasi": "nangno", "hindi": "कहाँ से", "english": "where from"},
    "why": {"khasi": "balei", "hindi": "क्यों", "english": "why"},
    "how": {"khasi": "kumno", "hindi": "कैसे", "english": "how"},
    "how_much": {"khasi": "katno", "hindi": "कितना / कितने", "english": "how much / how many"},
    "when": {"khasi": "lano", "hindi": "कब (भविष्य)", "english": "when (future)"},
    "when_past": {"khasi": "mynno", "hindi": "कब (भूतकाल)", "english": "when (past)"}
}

def get_pronoun(key: str) -> Optional[str]:
    """Retrieve pronoun by paradigm key (e.g., '1sg', '2_polite', '3sg_masc')."""
    if key in PRONOUN_TABLE:
        return PRONOUN_TABLE[key]["pronoun"]
    return None
