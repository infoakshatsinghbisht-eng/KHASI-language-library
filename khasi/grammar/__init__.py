# -*- coding: utf-8 -*-
"""Khasi Grammar, Morphology, Syntax & Expressives Package."""

from .nouns import (
    KhasiNoun,
    CORE_KHASI_NOUNS,
    pluralize,
    decline_noun,
    make_diminutive,
    make_augmentative,
)
from .adjectives import (
    CORE_KHASI_ADJECTIVES,
    make_attributive,
    make_comparative,
    make_superlative,
    make_intensified,
    qualify_noun,
)
from .adverbs import (
    KHASI_ADVERBS,
    reduplicate_adverb,
    get_adverbs_by_type,
    classify_adverb,
)
from .prepositions import (
    KHASI_PREPOSITIONS,
    get_marker,
    attach_case,
)
from .pronouns import (
    PRONOUN_TABLE,
    DEMONSTRATIVES,
    INTERROGATIVES,
    get_pronoun,
)
from .verbs import (
    CORE_KHASI_VERBS,
    conjugate,
    extract_root,
    causative,
    nominalize,
    agent_noun,
    experiential,
)
from .syntax import (
    SyntaxEngine,
    build_sentence,
    interrogative_sentence,
)
from .echo_words import (
    ECHO_WORDS,
    list_echo_words,
    find_echo_word,
)

__all__ = [
    # Nouns & Gender
    "KhasiNoun",
    "CORE_KHASI_NOUNS",
    "pluralize",
    "decline_noun",
    "make_diminutive",
    "make_augmentative",
    # Adjectives
    "CORE_KHASI_ADJECTIVES",
    "make_attributive",
    "make_comparative",
    "make_superlative",
    "make_intensified",
    "qualify_noun",
    # Adverbs & Expressives
    "KHASI_ADVERBS",
    "reduplicate_adverb",
    "get_adverbs_by_type",
    "classify_adverb",
    # Prepositions & Cases
    "KHASI_PREPOSITIONS",
    "get_marker",
    "attach_case",
    # Pronouns
    "PRONOUN_TABLE",
    "DEMONSTRATIVES",
    "INTERROGATIVES",
    "get_pronoun",
    # Verbs & Derivations
    "CORE_KHASI_VERBS",
    "conjugate",
    "extract_root",
    "causative",
    "nominalize",
    "agent_noun",
    "experiential",
    # Syntax
    "SyntaxEngine",
    "build_sentence",
    "interrogative_sentence",
    # Echo Words
    "ECHO_WORDS",
    "list_echo_words",
    "find_echo_word",
]
