# -*- coding: utf-8 -*-
"""Khasi Syntax Engine, SVO Word Order, and Sentence Construction."""

from typing import Optional, Dict, Any, List
from .verbs import conjugate
from .nouns import CORE_KHASI_NOUNS
from .pronouns import INTERROGATIVES

class SyntaxEngine:
    """Builds grammatically authentic Khasi sentences."""

    @staticmethod
    def build_sentence(
        subject: str,
        verb: str,
        obj: Optional[str] = None,
        tense: str = "present",
        aspect: str = "simple",
        negative: bool = False
    ) -> str:
        """
        Construct a valid Khasi SVO sentence.
        Example:
            subject='U briew', verb='bam', obj='u ja' -> 'U briew u bam ïa u ja'
        """
        subj_clean = subject.strip()
        tokens = subj_clean.split()
        first_tok_low = tokens[0].lower() if tokens else ""

        if len(tokens) > 1 and first_tok_low in ("u", "ka", "i", "ki"):
            agreement_pr = first_tok_low
            verb_clause = conjugate(verb=verb, tense=tense, pronoun=agreement_pr, aspect=aspect, negative=negative)
            sentence_core = f"{subj_clean} {verb_clause}"
        else:
            verb_clause = conjugate(verb=verb, tense=tense, pronoun=subj_clean, aspect=aspect, negative=negative)
            sentence_core = verb_clause

        if obj:
            clean_obj = obj.strip()
            # If object is not already marked with 'ïa', add it for objects
            if not clean_obj.startswith("ïa ") and not clean_obj.startswith("ha ") and not clean_obj.startswith("sha "):
                return f"{sentence_core} ïa {clean_obj}."
            return f"{sentence_core} {clean_obj}."
        return f"{sentence_core}."

    @staticmethod
    def interrogative_sentence(
        interrogative: str = "shano",
        subject: str = "phi",
        verb: str = "leit"
    ) -> str:
        """
        Construct a Khasi question.
        Example:
            interrogative='shano', subject='phi', verb='leit' -> 'Shano phi leit?'
        """
        q = interrogative.strip()
        pr = subject.strip()
        v = verb.strip()
        return f"{q.capitalize()} {pr} {v}?"

def build_sentence(
    subject: str,
    verb: str,
    obj: Optional[str] = None,
    tense: str = "present",
    aspect: str = "simple",
    negative: bool = False
) -> str:
    return SyntaxEngine.build_sentence(subject, verb, obj, tense, aspect, negative)

def interrogative_sentence(
    interrogative: str = "shano",
    subject: str = "phi",
    verb: str = "leit"
) -> str:
    return SyntaxEngine.interrogative_sentence(interrogative, subject, verb)
