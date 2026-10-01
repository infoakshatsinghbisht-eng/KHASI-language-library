# -*- coding: utf-8 -*-
"""Universal Multilingual Pivot Translation Engine for Khasi."""

from .engine import translate, TranslationResult

def pivot_translate(
    text: str,
    source_lang: str = "en",
    target_lang: str = "khasi",
    dialect: str = "sohra"
) -> TranslationResult:
    """Translate through pivot language representations into Khasi."""
    return translate(text, source=source_lang, target=target_lang, dialect=dialect)
