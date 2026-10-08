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

__version__ = "1.3.0"
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

# Culture, Calendar, Literature, Music, Botany, Wildlife, Cuisine, Geography & Kinship
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
    get_author,
    get_epic,
    search_literature,
    list_kinship_terms,
    get_kinship_info,
    search_kinship,
    describe_matrilineal_system,
    catalogue,
    BibliographyCatalogue,
    all_works,
    by_genre,
    by_author,
    by_type,
    search_works,
    get_digitized_works,
    catalogue_summary,
    INSTRUMENTS,
    FOLK_SONGS,
    MUSICIANS,
    list_instruments,
    get_instrument,
    list_songs,
    get_song,
    list_musicians,
    PLANTS,
    list_plants,
    get_plant,
    by_plant_type,
    medicinal_plants,
    WILDLIFE,
    list_wildlife,
    get_animal,
    by_wildlife_class,
    DISHES,
    list_dishes,
    get_dish,
    by_cuisine_category,
    GEOGRAPHY,
    list_places,
    get_place,
    by_geography_type,
    CLANS,
    list_clans,
    get_clan,
    search_clans,
    IDIOMS,
    list_idioms,
    get_idiom,
    RITUALS,
    list_rituals,
    get_ritual,
    rituals_by_category,
    DEITIES,
    list_deities,
    get_deity,
    deities_by_realm,
    SACRED_SITES,
    list_sacred_sites,
    get_sacred_site,
    sites_by_type,
)

# Voice & Speech Synthesis
from .voice import KhasiVoiceSynthesizer, KhasiAudioDataset

# Dialectology & Dedicated Sub-Lexicons
from .lexicon.dialects import (
    list_dialects,
    get_dialect_info,
    load_dialect_lexicon,
    lookup_dialect,
    translate_dialect,
    find_cognates,
    get_dialect_statistics,
)

# Aligned Parallel Corpora & MT Benchmarks
from .corpus import ParallelCorpus

# Digital Preservation & Archival
from .preservation import PreservationRecord, CorpusManager

# Global instances for simple top-level facade access
_DICT = KhasiDictionary()
phrases = type("Phrases", (), {"all": staticmethod(_DICT.all_phrases), "random": staticmethod(_DICT.random_phrase)})()
proverbs = type("Proverbs", (), {"all": staticmethod(_DICT.all_proverbs), "random": staticmethod(_DICT.random_proverb)})()
riddles = type("Riddles", (), {"all": staticmethod(_DICT.all_riddles), "random": staticmethod(_DICT.random_riddle)})()
instruments = type("Instruments", (), {"all": staticmethod(list_instruments), "get": staticmethod(get_instrument)})()
songs = type("Songs", (), {"all": staticmethod(list_songs), "get": staticmethod(get_song)})()
plants = type("Plants", (), {"all": staticmethod(list_plants), "get": staticmethod(get_plant), "medicinal": staticmethod(medicinal_plants)})()
wildlife = type("Wildlife", (), {"all": staticmethod(list_wildlife), "get": staticmethod(get_animal)})()
dishes = type("Dishes", (), {"all": staticmethod(list_dishes), "get": staticmethod(get_dish)})()
places = type("Places", (), {"all": staticmethod(list_places), "get": staticmethod(get_place)})()
clans = type("Clans", (), {"all": staticmethod(list_clans), "get": staticmethod(get_clan), "search": staticmethod(search_clans)})()
idioms = type("Idioms", (), {"all": staticmethod(list_idioms), "get": staticmethod(get_idiom)})()
rituals = type("Rituals", (), {"all": staticmethod(list_rituals), "get": staticmethod(get_ritual), "by_category": staticmethod(rituals_by_category)})()
deities = type("Deities", (), {"all": staticmethod(list_deities), "get": staticmethod(get_deity), "by_realm": staticmethod(deities_by_realm)})()
sacred_sites = type("SacredSites", (), {"all": staticmethod(list_sacred_sites), "get": staticmethod(get_sacred_site), "by_type": staticmethod(sites_by_type)})()

# Dialects, Audio & Corpus top-level facades
dialects = type("Dialects", (), {
    "list": staticmethod(list_dialects),
    "info": staticmethod(get_dialect_info),
    "lookup": staticmethod(lookup_dialect),
    "translate": staticmethod(translate_dialect),
    "cognates": staticmethod(find_cognates),
    "stats": staticmethod(get_dialect_statistics)
})()
audio_dataset = KhasiAudioDataset()
parallel_corpus = ParallelCorpus()

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
    "get_author", "get_epic", "search_literature",
    "phrases", "proverbs", "riddles",
    "instruments", "songs", "plants", "wildlife", "dishes", "places", "clans", "idioms",
    "rituals", "deities", "sacred_sites",
    "list_instruments", "get_instrument", "list_songs", "get_song", "list_musicians",
    "list_plants", "get_plant", "medicinal_plants",
    "list_wildlife", "get_animal", "by_wildlife_class",
    "list_dishes", "get_dish", "by_cuisine_category",
    "list_places", "get_place", "by_geography_type",
    "list_clans", "get_clan", "search_clans",
    "list_idioms", "get_idiom",
    "list_rituals", "get_ritual", "rituals_by_category", "RITUALS",
    "list_deities", "get_deity", "deities_by_realm", "DEITIES",
    "list_sacred_sites", "get_sacred_site", "sites_by_type", "SACRED_SITES",
    "list_kinship_terms", "get_kinship_info", "search_kinship", "describe_matrilineal_system",
    "catalogue", "BibliographyCatalogue", "all_works", "by_genre", "by_author", "by_type",
    "search_works", "get_digitized_works", "catalogue_summary",
    "dialects", "list_dialects", "get_dialect_info", "load_dialect_lexicon", "lookup_dialect", "translate_dialect", "find_cognates", "get_dialect_statistics",
    "audio_dataset", "KhasiAudioDataset", "KhasiVoiceSynthesizer",
    "parallel_corpus", "ParallelCorpus",
    "PreservationRecord", "CorpusManager",
    # Constants
    "ISO_639_3", "ISO_639_NAME", "NATIVE_NAME", "LANGUAGE_FAMILY", "SCRIPT",
    "KHASI_ALPHABET", "KHASI_VOWELS", "KHASI_CONSONANTS", "KHASI_SPECIAL_CHARS",
    "KHASI_DIALECTS", "Dialect", "Script", "PartOfSpeech", "Tense", "Gender", "GrammaticalNumber",
    "SEASONS", "KHASI_MONTHS", "DAYS_OF_WEEK", "MARKET_DAYS", "MARKET_CYCLE", "KINSHIP", "MORAL_PILLARS",
    "INSTRUMENTS", "FOLK_SONGS", "MUSICIANS", "PLANTS", "WILDLIFE", "DISHES", "GEOGRAPHY", "CLANS", "IDIOMS"
]
