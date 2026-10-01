# -*- coding: utf-8 -*-
"""Khasi Prepositional & Case-Marker System."""

from typing import Dict, List, Any, Optional

KHASI_PREPOSITIONS: Dict[str, Dict[str, str]] = {
    "jong": {
        "case": "genitive",
        "english": "of / belonging to",
        "hindi": "का / की / के",
        "example": "ka ïing jong nga (my house)"
    },
    "ha": {
        "case": "locative",
        "english": "in / at / on",
        "hindi": "में / पर",
        "example": "ha shnong (in the village)"
    },
    "sha": {
        "case": "allative",
        "english": "to / towards",
        "hindi": "की तरफ / को",
        "example": "sha ïing (towards home)"
    },
    "na": {
        "case": "ablative",
        "english": "from / out of",
        "hindi": "से",
        "example": "na Shillong (from Shillong)"
    },
    "da": {
        "case": "instrumental",
        "english": "by / with (instrument / means)",
        "hindi": "के द्वारा / से",
        "example": "da ka kti (with the hand)"
    },
    "bad": {
        "case": "comitative",
        "english": "with / and",
        "hindi": "और / के साथ",
        "example": "bad u lok (with the friend)"
    },
    "ïa": {
        "case": "accusative_dative",
        "english": "to / marker of direct object",
        "hindi": "को (कर्म कारक)",
        "example": "nga ieit ïa phi (I love you)"
    },
    "ban": {
        "case": "purposive_infinitive",
        "english": "to / in order to",
        "hindi": "के लिए / करने हेतु",
        "example": "ban bam (to eat)"
    },
    "namar": {
        "case": "causal",
        "english": "because of / for the sake of",
        "hindi": "क्योंकि / के कारण",
        "example": "namar jong phi (because of you)"
    }
}

def get_marker(case: str) -> Optional[str]:
    """Retrieve the preposition for a given grammatical case."""
    for prep, data in KHASI_PREPOSITIONS.items():
        if data["case"].lower() == case.lower():
            return prep
    return None

def attach_case(noun_phrase: str, case: str) -> str:
    """Attach the corresponding Khasi case preposition to a noun phrase."""
    prep = get_marker(case)
    if prep:
        return f"{prep} {noun_phrase.strip()}"
    return noun_phrase.strip()
