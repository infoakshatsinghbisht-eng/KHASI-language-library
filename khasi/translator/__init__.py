# -*- coding: utf-8 -*-
"""Khasi Translation Engine Package."""

from .engine import translate, TranslationResult
from .rule_based import apply_dialect
from .pivot import pivot_translate
from .llm_adapter import get_khasi_prompt

__all__ = [
    "translate",
    "TranslationResult",
    "apply_dialect",
    "pivot_translate",
    "get_khasi_prompt",
]
