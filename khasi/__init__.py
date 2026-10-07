# -*- coding: utf-8 -*-
"""
Khasi (Ka Ktien Khasi) Language Library for Python
=================================================

A standard-library-style Python package for the Khasi language (Meghalaya, Northeast India),
providing linguistic primitives, orthography normalization, grammar parsing, 
verb conjugation, 300,000+ morphological inflections, dictionary lookups, 
matrilineal kinship analysis, and universal translation into Khasi across dialects.

Quick Start:
------------
>>> import khasi
>>> khasi.translate("How are you?")
<TranslationResult text='Kumno phi long?' dialect='sohra' conf=0.98>
>>> khasi.conjugate("wan", tense="past", pronoun="u")
'u la wan'
>>> khasi.num_to_words(42)
'sawphew ar'
>>> khasi.lookup("khublei")
{'khasi': 'khublei', 'hindi': 'नमस्ते / धन्यवाद / प्रणाम', 'english': 'hello / thank you / greetings', 'pos': 'interjection'}
"""

__version__ = "1.1.0"
__author__ = "Akshat Singh Bisht"
__email__ = "infoakshatsinghbisht@gmail.com"
__maintainer__ = "Akshat Singh Bisht"
__website__ = "https://akshatsinghbisht.com/"
__copyright__ = "Copyright (c) 2026 Akshat Singh Bisht"
__license__ = "MIT"

# Constants
from .constants import (
    ISO_639_3,
    ISO_639_NAME,
    NATIVE_NAME,
    LANGUAGE_FAMILY,
    SCRIPT,
    KHASI_ALPHABET,
    KHASI_VOWELS,
    KHASI_CONSONANTS,
    KHASI_SPECIAL_CHARS,
    KHASI_DIALECTS,
    Dialect,
    Script,
    PartOfSpeech,
    Tense,
    Gender,
    GrammaticalNumber,
    SEASONS,
    KHASI_MONTHS,
    DAYS_OF_WEEK,
    MARKET_DAYS,
    KINSHIP,
    MORAL_PILLARS,
)

# Phonetics, Orthography & Transliteration
from .phonetics import (
    normalize,
    tokenize,
    syllables,
    detect_script,
    latin_to_devanagari,
    devanagari_to_latin,
    is_khasi_word,
    has_khasi_diacritics,
    expand_contractions,
)

# Numbers & Numerals
from .numbers import (
    num_to_words,
    words_to_num,
    ordinal,
    fraction,
)

# Grammar & Morphology
from .grammar import (
    KhasiNoun,
    CORE_KHASI_NOUNS,
    pluralize,
    decline_noun,
    make_diminutive,
    make_augmentative,
    KHASI_PREPOSITIONS,
    get_marker,
    attach_case,
    PRONOUN_TABLE,
    DEMONSTRATIVES,
    INTERROGATIVES,
    get_pronoun,
    CORE_KHASI_VERBS,
    conjugate,
    extract_root,
    causative,
    nominalize,
    agent_noun,
    experiential,
    SyntaxEngine,
    build_sentence,
    interrogative_sentence,
    make_attributive,
    make_comparative,
    make_superlative,
    qualify_noun,
    reduplicate_adverb,
    classify_adverb,
    list_echo_words,
    find_echo_word,
)

# Lexicon, Dictionary & 300,000+ Morphological Universe
from .lexicon import (
    KhasiDictionary,
    KhasiMorphologyEngine,
    MorphAnalysis,
    get_morphology_engine,
)

# Translation Engine
from .translator import (
    translate,
    TranslationResult,
    apply_dialect,
    pivot_translate,
    get_khasi_prompt,
)

# Culture, Calendar, Literature & Kinship
from .culture import (
    KHASI_SEASONS,
    KHASI_DAYS,
    MARKET_CYCLE,
    get_current_season,
    get_current_khasi_month,
    get_market_day,
    KHASI_FESTIVALS,
    list_festivals,
    get_festival,
    AUTHORS,
    EPICS,
    POEMS,
    authors,
    epics,
    poems,
    list_kinship_terms,
    get_kinship_info,
    describe_matrilineal_system,
    catalogue,
    BibliographyCatalogue,
)

# Voice & Speech Synthesis
from .voice import KhasiVoiceSynthesizer

# Digital Preservation & Archival
from .preservation import PreservationRecord, CorpusManager

# Global instances for simple top-level facade access
_DICT = KhasiDictionary()
phrases = type("Phrases", (), {"all": _DICT.all_phrases, "random": _DICT.random_phrase})()
proverbs = type("Proverbs", (), {"all": _DICT.all_proverbs, "random": _DICT.random_proverb})()
riddles = type("Riddles", (), {"all": _DICT.all_riddles, "random": _DICT.random_riddle})()

def lookup(word: str):
    """Look up a Khasi word in dictionary with morphological fallback."""
    return _DICT.lookup(word)

def search(query: str):
    """Search words matching across Khasi, English, or Hindi."""
    return _DICT.search(query)

def analyze(word: str):
    """Perform morphological decomposition on a Khasi word."""
    return get_morphology_engine().analyze(word)

def total_word_forms() -> int:
    """Return count of represented morphological forms (300,000+)."""
    return get_morphology_engine().total_forms_count()

def get_months():
    """Return traditional 12 Khasi months."""
    return KHASI_MONTHS

def get_seasons():
    """Return traditional 4 Khasi seasons."""
    return SEASONS

__all__ = [
    # Top-level functions
    "translate", "TranslationResult",
    "lookup", "search", "analyze", "total_word_forms",
    "normalize", "tokenize", "syllables", "detect_script",
    "latin_to_devanagari", "devanagari_to_latin", "is_khasi_word",
    "num_to_words", "words_to_num", "ordinal", "fraction",
    "conjugate", "causative", "nominalize", "agent_noun", "experiential",
    "pluralize", "decline_noun", "build_sentence", "interrogative_sentence",
    "make_attributive", "make_comparative", "make_superlative", "qualify_noun",
    "reduplicate_adverb", "classify_adverb", "list_echo_words", "find_echo_word",
    "get_months", "get_seasons", "get_current_season", "get_current_khasi_month", "get_market_day",
    "list_festivals", "get_festival", "authors", "epics", "poems",
    "phrases", "proverbs", "riddles",
    "list_kinship_terms", "get_kinship_info", "describe_matrilineal_system",
    "catalogue", "BibliographyCatalogue",
    "KhasiVoiceSynthesizer",
    "PreservationRecord", "CorpusManager",
    # Constants
    "ISO_639_3", "ISO_639_NAME", "NATIVE_NAME", "LANGUAGE_FAMILY", "SCRIPT",
    "KHASI_ALPHABET", "KHASI_VOWELS", "KHASI_CONSONANTS", "KHASI_SPECIAL_CHARS",
    "KHASI_DIALECTS", "Dialect", "Script", "PartOfSpeech", "Tense", "Gender", "GrammaticalNumber",
    "SEASONS", "KHASI_MONTHS", "DAYS_OF_WEEK", "MARKET_DAYS", "MARKET_CYCLE", "KINSHIP", "MORAL_PILLARS"
]
