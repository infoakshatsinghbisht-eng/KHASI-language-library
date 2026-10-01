# -*- coding: utf-8 -*-
"""LLM Adapter for Neural Khasi Translation."""

from typing import Dict, Any, Optional

def get_khasi_prompt(text: str, source_lang: str = "en", dialect: str = "sohra") -> str:
    """Generate structured system prompt for generative LLM Khasi translation."""
    return f"""You are an expert native Khasi (Ka Ktien Khasi) linguist from Meghalaya.
Translate the following {source_lang} text into authentic, natural, colloquial Khasi ({dialect} dialect):

Source Text: "{text}"
Khasi Translation:"""
