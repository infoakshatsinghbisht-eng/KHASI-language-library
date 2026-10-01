# -*- coding: utf-8 -*-
"""Khasi Festivals, Dances, and Cultural Celebrations."""

from typing import Dict, List, Any, Optional

KHASI_FESTIVALS: List[Dict[str, Any]] = [
    {
        "name": "Shad Suk Mynsiem (Dance of Peaceful Hearts)",
        "month": "Ïaïong (April)",
        "location": "Weiking Ground, Jaiaw, Shillong",
        "description": "Annual spring thanksgiving dance honoring God the Creator ('U Blei'), mother nature, and the matrilineal family line.",
        "tradition": "Unmarried maidens dance in traditional gold/silver crowns ('Pansngiat') and silk attire ('Dhara'), surrounded by men wielding whisks ('Symphiah') symbolizing protection."
    },
    {
        "name": "Ka Pomblang Nongkrem (Nongkrem Dance)",
        "month": "Naiwieng (November)",
        "location": "Smit (Historic capital of Khyrim Syiemship)",
        "description": "Five-day harvest thanksgiving festival and prayer for national peace and prosperity led by the Syiem of Khyrim and the High Priestess ('Ka Syiem Sad').",
        "tradition": "Sacred goat sacrifice ('Pomblang') followed by majestic Royal dances to the rhythm of 'Ksing' drums and 'Tangmuri' flutes."
    },
    {
        "name": "Behdeinkhlam (Chasing Away the Plague)",
        "month": "Naitung (July)",
        "location": "Jowai, Jaiñtia Hills",
        "description": "The most significant traditional festival of the Pnar people in Jaintia Hills to drive away evil spirits, plagues, and pestilence.",
        "tradition": "Young men carry tall decorated wooden towers ('Raths' / 'Rot') and beat the mud pond ('Aitnar') with sacred timber beams ('Deinkhlam')."
    },
    {
        "name": "Seng Kut Snem",
        "month": "Naiwieng 23 (November 23)",
        "location": "Across Khasi Hills & Shillong",
        "description": "Celebration commemorating the founding of the Seng Khasi socio-cultural movement (1899) dedicated to preserving indigenous faith, culture, and ethics.",
        "tradition": "Colorful street processions ('Iaid Pyni Riti'), display of traditional costumes, music, and chanting of sacred Phawar."
    },
    {
        "name": "Shad Wangala (Hundred Drums Festival)",
        "month": "Naiwieng (November)",
        "location": "Garo Hills & Meghalaya State Festival",
        "description": "Celebrated in Meghalaya as a post-harvest thanksgiving to the Sun God of Fertility ('Misi Saljong').",
        "tradition": "Synchronized beats of 100 long oval nagara drums played simultaneously by energetic youth."
    }
]

def list_festivals() -> List[Dict[str, Any]]:
    """Return all documented traditional festivals of Khasi and Meghalaya heritage."""
    return KHASI_FESTIVALS

def get_festival(query: str) -> Optional[Dict[str, Any]]:
    """Find festival by name or keyword."""
    q = query.lower().strip()
    for f in KHASI_FESTIVALS:
        if q in f["name"].lower() or q in f["description"].lower() or q in f["month"].lower():
            return f
    return None
