# -*- coding: utf-8 -*-
"""Khasi Calendar, Traditional Months (Ki Bnai), Seasons (Ki Aïom), and Market Days."""

import datetime
from typing import Dict, List, Any

KHASI_MONTHS = {
    1: {"name": "Kyllalyngkot", "english": "January", "meaning": "Cold fireside month; time spent around the hearth"},
    2: {"name": "Rymphang", "english": "February", "meaning": "Windy month; strong mountain winds sweeping the ridges"},
    3: {"name": "Lber", "english": "March", "meaning": "Spring awakening; sprouting of vegetation"},
    4: {"name": "Ïaïong", "english": "April", "meaning": "Month of thunder clouds and sudden spring storms"},
    5: {"name": "Jymmang", "english": "May", "meaning": "Flowering month; blooming of wild rhododendrons and orchids"},
    6: {"name": "Jylliew", "english": "June", "meaning": "Deep rain month; rivers swelling and deep waters"},
    7: {"name": "Naitung", "english": "July", "meaning": "Continuous rains causing dampness and vegetation decay"},
    8: {"name": "Nailar", "english": "August", "meaning": "Clearing skies; bright intervals between monsoon showers"},
    9: {"name": "Nailur", "english": "September", "meaning": "Weeding of paddy terraces and early harvest preparations"},
    10: {"name": "Risaw", "english": "October", "meaning": "Golden harvest season; mature paddy fields"},
    11: {"name": "Naiwieng", "english": "November", "meaning": "Season of the hearth stove; early cold setting in"},
    12: {"name": "Nohprah", "english": "December", "meaning": "Dropping of leaves; dry cold winter"}
}

KHASI_SEASONS = {
    "Aïom Pyrem": {
        "english": "Spring",
        "hindi": "वसंत",
        "months": ["Lber", "Ïaïong"],
        "description": "Season of blossoms, fresh pine scent, and the sacred thanksgiving dance Shad Suk Mynsiem."
    },
    "Aïom Lyiur": {
        "english": "Monsoon / Summer",
        "hindi": "वर्षा / ग्रीष्म",
        "months": ["Jymmang", "Jylliew", "Naitung", "Nailar"],
        "description": "Continuous torrential rains over the southern escarpment (Cherrapunji/Mawsynram), feeding roaring waterfalls."
    },
    "Aïom Synrai": {
        "english": "Autumn",
        "hindi": "शरद",
        "months": ["Nailur", "Risaw"],
        "description": "Clear mountain skies, golden ripening paddy, and Ka Pomblang Nongkrem harvest festival at Smit."
    },
    "Aïom Tlang": {
        "english": "Winter",
        "hindi": "शीत",
        "months": ["Naiwieng", "Nohprah", "Kyllalyngkot", "Rymphang"],
        "description": "Crisp morning frost over highland plateaus, cozy hearth gatherings, and Seng Kut Snem celebrations."
    }
}

KHASI_DAYS = {
    "Sunday": {"khasi": "Sngi U Blei", "meaning": "Day of God"},
    "Monday": {"khasi": "Sngi Ba-ar", "meaning": "Second Day"},
    "Tuesday": {"khasi": "Sngi Ba-lai", "meaning": "Third Day"},
    "Wednesday": {"khasi": "Sngi Ba-saw", "meaning": "Fourth Day"},
    "Thursday": {"khasi": "Sngi Ba-san", "meaning": "Fifth Day"},
    "Friday": {"khasi": "Sngi Thohdieng", "meaning": "Wood-gathering Day"},
    "Saturday": {"khasi": "Sngi Saitjaiñ", "meaning": "Cloth-washing Day"}
}

# The unique 8-day Khasi traditional market rotation cycle
MARKET_CYCLE = [
    {"day": 1, "name": "Sngi Iewduh", "location": "Shillong (Great central Barabazar market)"},
    {"day": 2, "name": "Sngi Lyngka", "location": "Smaller regional village trading post"},
    {"day": 3, "name": "Sngi Nongkrem", "location": "Historic capital of Khyrim Syiemship"},
    {"day": 4, "name": "Sngi Mawlong", "location": "Cherrapunji / Southern slopes market"},
    {"day": 5, "name": "Sngi Rynghep", "location": "Highlands border market"},
    {"day": 6, "name": "Sngi Pomtiah", "location": "Jaintia / Ri-Bhoi border interchange"},
    {"day": 7, "name": "Sngi Umni", "location": "Riverside exchange market"},
    {"day": 8, "name": "Sngi Yeit", "location": "Final trading day before the cycle resets to Iewduh"}
]

def get_current_season() -> Dict[str, str]:
    """Return current Khasi season based on Gregorian month."""
    m = datetime.datetime.now().month
    if m in (3, 4):
        return {"name_khasi": "Aïom Pyrem", "name_hindi": "वसंत", "english_season": "Spring"}
    elif m in (5, 6, 7, 8):
        return {"name_khasi": "Aïom Lyiur", "name_hindi": "वर्षा / ग्रीष्म", "english_season": "Monsoon / Summer"}
    elif m in (9, 10):
        return {"name_khasi": "Aïom Synrai", "name_hindi": "शरद", "english_season": "Autumn"}
    else:
        return {"name_khasi": "Aïom Tlang", "name_hindi": "शीत", "english_season": "Winter"}

def get_current_khasi_month() -> Dict[str, Any]:
    """Return the current Khasi lunar/solar month."""
    m = datetime.datetime.now().month
    return KHASI_MONTHS[m]

def get_market_day(day_index: int = 1) -> Dict[str, Any]:
    """Get market day information from 8-day cycle (1 to 8)."""
    idx = (day_index - 1) % 8
    return MARKET_CYCLE[idx]
