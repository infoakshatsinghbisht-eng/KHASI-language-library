# -*- coding: utf-8 -*-
"""Khasi Lexicon & Morphology Package."""

from .dictionary import KhasiDictionary
from .morphology import (
    KhasiMorphologyEngine,
    MorphAnalysis,
    get_morphology_engine,
)

from .dialects import (
    list_dialects,
    get_dialect_info,
    load_dialect_lexicon,
    lookup_dialect,
    translate_dialect,
    find_cognates,
    get_dialect_statistics,
)

__all__ = [
    "KhasiDictionary",
    "KhasiMorphologyEngine",
    "MorphAnalysis",
    "get_morphology_engine",
    "list_dialects",
    "get_dialect_info",
    "load_dialect_lexicon",
    "lookup_dialect",
    "translate_dialect",
    "find_cognates",
    "get_dialect_statistics",
]
