# -*- coding: utf-8 -*-
"""Khasi Language Constants, Phoneme, Orthography, and Cultural Definitions."""

from enum import Enum
from typing import Dict, List, Any

# ISO & Linguistic Identifiers
ISO_639_3 = "kha"
ISO_639_NAME = "Khasi"
NATIVE_NAME = "Ka Ktien Khasi"
LANGUAGE_FAMILY = "Austroasiatic / Mon-Khmer"
SCRIPT = "Latin (Khasi Orthography formalized 1841)"

# Orthographic letter inventory
# Standard 23-letter alphabet
KHASI_ALPHABET = [
    "A", "B", "K", "D", "E", "G", "Ng", "H", "I", "Ï", "J", "L",
    "M", "N", "Ñ", "O", "P", "R", "S", "T", "U", "W", "Y"
]

KHASI_VOWELS = ["a", "e", "i", "ï", "o", "u"]
KHASI_VOWELS_UPPER = ["A", "E", "I", "Ï", "O", "U"]

KHASI_CONSONANTS = [
    "b", "k", "d", "g", "ng", "h", "j", "l", "m", "n", "ñ", "p", "r", "s", "t", "w", "y"
]
KHASI_CONSONANTS_UPPER = [
    "B", "K", "D", "G", "NG", "H", "J", "L", "M", "N", "Ñ", "P", "R", "S", "T", "W", "Y"
]

KHASI_SPECIAL_CHARS = {"ï", "Ï", "ñ", "Ñ"}
NON_INDIGENOUS_LETTERS = {"c", "f", "q", "v", "x", "z"}

# Dialects across Meghalaya
KHASI_DIALECTS = {
    "sohra": "Sohra (Standard Literary Khasi / Cherrapunji)",
    "shillong": "Shillong Colloquial (Urban East Khasi Hills)",
    "pnar": "Pnar / Jaiñtia (Jaiñtia Hills variant)",
    "war": "War Khasi (Southern slopes facing Bangladesh plains)",
    "bhoi": "Bhoi Khasi (Northern Ri-Bhoi district)",
    "maram": "Maram / Nongstoin (West Khasi Hills)"
}

class Dialect(str, Enum):
    SOHRA = "sohra"
    SHILLONG = "shillong"
    PNAR = "pnar"
    WAR = "war"
    BHOI = "bhoi"
    MARAM = "maram"

class Script(str, Enum):
    LATIN = "latin"
    ASCII_COLLOQUIAL = "ascii_colloquial"
    DEVANAGARI_TRANSLIT = "devanagari_translit"

class PartOfSpeech(str, Enum):
    NOUN = "noun"
    PRONOUN = "pronoun"
    VERB = "verb"
    ADJECTIVE = "adjective"
    ADVERB = "adverb"
    PREPOSITION = "preposition"
    ARTICLE = "article"
    CONJUNCTION = "conjunction"
    INTERJECTION = "interjection"
    PARTICLE = "particle"
    NUMERAL = "numeral"

class Tense(str, Enum):
    PAST = "past"
    PRESENT = "present"
    PROGRESSIVE = "progressive"
    FUTURE = "future"
    FUTURE_DEFINITE = "future_definite"
    HABITUAL = "habitual"

class Gender(str, Enum):
    MASCULINE = "u"       # Masculine singular article
    FEMININE = "ka"       # Feminine singular article
    DIMINUTIVE = "i"      # Diminutive/Affectionate article
    PLURAL = "ki"         # Plural article (all genders)

class GrammaticalNumber(str, Enum):
    SINGULAR = "singular"
    PLURAL = "plural"

# Four Khasi Seasons (Ki Aïom)
SEASONS = [
    {
        "khasi": "Aïom Pyrem",
        "english": "Spring",
        "months": "March - April",
        "description": "Season of blooming wild orchids, fresh green shoots, and the sacred Shad Suk Mynsiem festival."
    },
    {
        "khasi": "Aïom Lyiur",
        "english": "Monsoon / Summer",
        "months": "May - August",
        "description": "Heavy monsoon rains pouring over the Khasi and Jaintia hills, feeding roaring waterfalls like Nohkalikai."
    },
    {
        "khasi": "Aïom Synrai",
        "english": "Autumn",
        "months": "September - October",
        "description": "Golden skies, ripening paddy fields, harvest thanksgiving, and Ka Pomblang Nongkrem festival at Smit."
    },
    {
        "khasi": "Aïom Tlang",
        "english": "Winter",
        "months": "November - February",
        "description": "Crisp frosty mornings, morning mist over pine hills, fireside storytelling, and Seng Kut Snem celebrations."
    }
]

# 12 Traditional Khasi Lunar / Solar Months (Ki Bnai)
KHASI_MONTHS = [
    {"name": "Kyllalyngkot", "english": "January", "meaning": "Cold fireside month; time spent around the hearth"},
    {"name": "Rymphang", "english": "February", "meaning": "Windy month; strong mountain winds sweeping the ridges"},
    {"name": "Lber", "english": "March", "meaning": "Spring awakening; sprouting of vegetation"},
    {"name": "Ïaïong", "english": "April", "meaning": "Month of thunder clouds and sudden spring storms"},
    {"name": "Jymmang", "english": "May", "meaning": "Flowering month; blooming of wild rhododendrons and shrubs"},
    {"name": "Jylliew", "english": "June", "meaning": "Deep rain month; rivers swelling and deep waters"},
    {"name": "Naitung", "english": "July", "meaning": "Continuous rains causing dampness and vegetation rot"},
    {"name": "Nailar", "english": "August", "meaning": "Clearing skies; bright intervals between monsoon showers"},
    {"name": "Nailur", "english": "September", "meaning": "Weeding of paddy terraces and early harvest preparations"},
    {"name": "Risaw", "english": "October", "meaning": "Golden harvest season; mature paddy fields"},
    {"name": "Naiwieng", "english": "November", "meaning": "Season of the hearth stove; early cold setting in"},
    {"name": "Nohprah", "english": "December", "meaning": "Dropping of leaves; dry cold winter"}
]

# 7 Days of the Week
DAYS_OF_WEEK = [
    {"name": "Sngi U Blei", "english": "Sunday", "literal": "Day of God"},
    {"name": "Sngi Ba-ar", "english": "Monday", "literal": "Second Day"},
    {"name": "Sngi Ba-lai", "english": "Tuesday", "literal": "Third Day"},
    {"name": "Sngi Ba-saw", "english": "Wednesday", "literal": "Fourth Day"},
    {"name": "Sngi Ba-san", "english": "Thursday", "literal": "Fifth Day"},
    {"name": "Sngi Thohdieng", "english": "Friday", "literal": "Wood-gathering Day"},
    {"name": "Sngi Saitjaiñ", "english": "Saturday", "literal": "Cloth-washing Day"}
]

# Traditional 8-day Khasi Market Cycle (Sngi Iew)
MARKET_DAYS = [
    {"day": 1, "name": "Sngi Iewduh", "location": "Shillong (Great central Barabazar market)"},
    {"day": 2, "name": "Sngi Lyngka", "location": "Smaller regional village trading post"},
    {"day": 3, "name": "Sngi Nongkrem", "location": "Historic capital of Khyrim Syiemship"},
    {"day": 4, "name": "Sngi Mawlong", "location": "Cherrapunji / Southern slopes market"},
    {"day": 5, "name": "Sngi Rynghep", "location": "Highlands border market"},
    {"day": 6, "name": "Sngi Pomtiah", "location": "Jaintia / Ri-Bhoi border interchange"},
    {"day": 7, "name": "Sngi Umni", "location": "Riverside exchange market"},
    {"day": 8, "name": "Sngi Yeit", "location": "Final trading day before the cycle resets to Iewduh"}
]

# Matrilineal Kinship Terms (Kur and Kha)
KINSHIP = {
    "Mei": "Mother (central head of family lineage)",
    "Pa": "Father (protector and provider)",
    "Khadduh": "Youngest daughter (inheritor of ancestral home 'ïing-sad' and custodian of family religion)",
    "Kñi": "Maternal uncle (authoritative counselor and spiritual guide in family councils)",
    "Kur": "Maternal clan (relatives tracing back to common ancestral mother 'Ka Ïawbei')",
    "Kha": "Paternal clan (relatives from father's clan line)",
    "Kong": "Elder sister / polite respectful address for women",
    "Bah": "Elder brother / polite respectful address for men",
    "Hep": "Younger sibling / affectionate term for younger person",
    "Mei-rad": "Grandmother",
    "Kpa-tymmen": "Grandfather",
    "Khun": "Child / offspring",
    "Kmie-san": "Mother's elder sister (senior maternal aunt)",
    "Kmie-nah": "Mother's younger sister (junior maternal aunt)",
    "Kpa-san": "Father's elder brother (senior paternal uncle)",
    "Kpa-nah": "Father's younger brother (junior paternal uncle)",
    "Kñi-rangbah": "Senior maternal uncle (clan elder)",
    "Khun-kha": "Children of one's father's sister / paternal cousins",
    "Khun-ruit": "Sisters' children / maternal nephews and nieces",
    "Shi-kur": "Kin belonging to the exact same maternal clan",
    "Shi-kpoh": "Relatives descending from the same immediate maternal womb",
    "Kynsi": "Brother-in-law",
    "Konghei": "Sister-in-law",
    "Kthaw": "Father-in-law",
    "Kiaw": "Mother-in-law"
}

# Three Supreme Moral Pillars of Khasi Philosophy
MORAL_PILLARS = [
    {
        "principle": "Kamai ïa ka hok",
        "translation": "Earn righteousness by honest living",
        "description": "The foundation of Khasi morality — that life must be lived and wealth acquired solely through truth, justice, and honest effort."
    },
    {
        "principle": "Tip kur, tip kha",
        "translation": "Know your maternal kin, know your paternal kin",
        "description": "The ethical cornerstone governing kinship, lineage respect, exogamy rules, and social duties in matrilineal Khasi society."
    },
    {
        "principle": "Tip briew, tip Blei",
        "translation": "Know man to know God",
        "description": "To honor and treat human beings with compassion and dignity is the true path to knowing and serving God."
    }
]
