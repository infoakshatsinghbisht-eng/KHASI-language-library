# -*- coding: utf-8 -*-
"""Khasi Lexicon & Morphology Package."""

from .dictionary import KhasiDictionary
from .morphology import (
    KhasiMorphologyEngine,
    MorphAnalysis,
    get_morphology_engine,
)

__all__ = [
    "KhasiDictionary",
    "KhasiMorphologyEngine",
    "MorphAnalysis",
    "get_morphology_engine",
]
