# -*- coding: utf-8 -*-
"""Khasi Dialects Package Facade."""

from ..lexicon.dialects import (
    list_dialects,
    get_dialect_info,
    load_dialect_lexicon,
    lookup_dialect,
    translate_dialect,
    find_cognates,
    get_dialect_statistics,
    DIALECT_INFO,
)

__all__ = [
    "list_dialects",
    "get_dialect_info",
    "load_dialect_lexicon",
    "lookup_dialect",
    "translate_dialect",
    "find_cognates",
    "get_dialect_statistics",
    "DIALECT_INFO",
]
