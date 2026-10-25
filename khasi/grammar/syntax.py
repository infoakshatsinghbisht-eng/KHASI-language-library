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

    @staticmethod
    def build_complex_sentence(
        main_clause: str,
        sub_clause: str,
        conjunction: str = "namar ba"
    ) -> str:
        """Link two clauses using a conjunction (e.g. 'namar ba', 'lada', 'wat la', 'katba')."""
        c = conjunction.strip()
        m = main_clause.rstrip(". ")
        s = sub_clause.rstrip(". ")
        if c.lower() in ("lada", "wat la", "katba", "ynda"):
            if c.lower() == "wat la":
                return f"{c.capitalize()} {s}, pynban {m}."
            elif c.lower() == "ynda":
                return f"{c.capitalize()} {s}, sa {m}."
            return f"{c.capitalize()} {s}, {m}."
        return f"{m} {c} {s}."

    @staticmethod
    def build_conditional_sentence(
        condition: str,
        consequence: str,
        concessive: bool = False
    ) -> str:
        """Construct conditional ('lada') or concessive ('wat la') sentence."""
        conj = "wat la" if concessive else "lada"
        return SyntaxEngine.build_complex_sentence(main_clause=consequence, sub_clause=condition, conjunction=conj)

    @staticmethod
    def build_relative_clause(
        antecedent: str,
        verb_clause: str,
        gender: str = "u"
    ) -> str:
        """Construct relative clause with agreement marker ('uba', 'kaba', 'iba', 'kiba')."""
        rel_map = {
            "u": "uba", "m": "uba", "masculine": "uba",
            "ka": "kaba", "f": "kaba", "feminine": "kaba",
            "i": "iba", "dim": "iba", "diminutive": "iba",
            "ki": "kiba", "pl": "kiba", "plural": "kiba"
        }
        rel_pr = rel_map.get(gender.lower(), "uba")
        head = antecedent.strip()
        vc = verb_clause.strip()
        return f"{head} {rel_pr} {vc}"

    @staticmethod
    def build_comparative_sentence(
        item1: str,
        item2: str,
        adjective: str,
        degree: str = "kham"
    ) -> str:
        """Construct comparison of superiority ('kham [adj] ban ïa')."""
        i1 = item1.strip()
        i2 = item2.strip()
        adj = adjective.strip()
        toks = i1.split()
        cp = toks[0].lower() if toks and toks[0].lower() in ("u", "ka", "i", "ki") else ""
        cp_str = f" {cp}" if cp else ""
        return f"{i1}{cp_str} {degree} {adj} ban ïa {i2}."

    @staticmethod
    def build_passive_sentence(
        patient: str,
        verb: str,
        agent: Optional[str] = None,
        adversative: bool = True
    ) -> str:
        """Construct passive voice sentence using 'shah' (adversative) or 'da'."""
        pat = patient.strip()
        toks = pat.split()
        cp = toks[0].lower() if toks and toks[0].lower() in ("u", "ka", "i", "ki") else ""
        cp_str = f" {cp}" if cp else ""
        v = verb.strip()
        if adversative:
            ag_str = f" ha {agent.strip()}" if agent else ""
            return f"{pat}{cp_str} la shah {v}{ag_str}."
        else:
            ag_str = f" da {agent.strip()}" if agent else ""
            return f"{pat}{cp_str} la {v}{ag_str}."


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

def build_complex_sentence(main_clause: str, sub_clause: str, conjunction: str = "namar ba") -> str:
    return SyntaxEngine.build_complex_sentence(main_clause, sub_clause, conjunction)

def build_conditional_sentence(condition: str, consequence: str, concessive: bool = False) -> str:
    return SyntaxEngine.build_conditional_sentence(condition, consequence, concessive)

def build_relative_clause(antecedent: str, verb_clause: str, gender: str = "u") -> str:
    return SyntaxEngine.build_relative_clause(antecedent, verb_clause, gender)

def build_comparative_sentence(item1: str, item2: str, adjective: str, degree: str = "kham") -> str:
    return SyntaxEngine.build_comparative_sentence(item1, item2, adjective, degree)

def build_passive_sentence(patient: str, verb: str, agent: Optional[str] = None, adversative: bool = True) -> str:
    return SyntaxEngine.build_passive_sentence(patient, verb, agent, adversative)
