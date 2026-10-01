# -*- coding: utf-8 -*-
"""Unit tests for Khasi grammar, nouns, prepositions, verbs, and syntax."""

import unittest
from khasi.grammar import (
    pluralize,
    decline_noun,
    make_diminutive,
    make_augmentative,
    get_marker,
    attach_case,
    conjugate,
    causative,
    nominalize,
    agent_noun,
    experiential,
    build_sentence,
    interrogative_sentence,
    PRONOUN_TABLE,
    make_attributive,
    make_comparative,
    make_superlative,
    qualify_noun,
    reduplicate_adverb,
    classify_adverb,
    list_echo_words,
    find_echo_word,
)

class TestKhasiGrammar(unittest.TestCase):
    def test_pluralize(self):
        self.assertEqual(pluralize("u briew"), "ki briew")
        self.assertEqual(pluralize("ka ïing"), "ki ïing")

    def test_diminutive(self):
        self.assertEqual(make_diminutive("u khunlung"), "i khunlung")

    def test_decline_noun(self):
        decls = decline_noun("ïing", "ka")
        self.assertEqual(decls["genitive_sg"], "jong ka ïing")
        self.assertEqual(decls["locative_sg"], "ha ka ïing")
        self.assertEqual(decls["allative_sg"], "sha ka ïing")

    def test_prepositions(self):
        self.assertEqual(get_marker("genitive"), "jong")
        self.assertEqual(get_marker("locative"), "ha")
        self.assertEqual(attach_case("ka ïing", "genitive"), "jong ka ïing")

    def test_pronouns(self):
        self.assertIn("1sg", PRONOUN_TABLE)
        self.assertEqual(PRONOUN_TABLE["1sg"]["pronoun"], "nga")

    def test_conjugate_tenses(self):
        # Past
        self.assertEqual(conjugate("wan", tense="past", pronoun="u"), "u la wan")
        # Future
        self.assertEqual(conjugate("wan", tense="future", pronoun="u"), "un wan")
        # Definite Future
        self.assertEqual(conjugate("wan", tense="future_definite", pronoun="u"), "u daw wan")
        # Habitual
        self.assertEqual(conjugate("wan", tense="habitual", pronoun="u"), "u ju wan")
        # Progressive
        self.assertEqual(conjugate("wan", aspect="progressive", pronoun="nga"), "nga dang wan")
        # Negation
        self.assertEqual(conjugate("wan", tense="past", pronoun="nga", negative=True), "nga khlem wan")

    def test_derivational_prefixes(self):
        self.assertEqual(causative("ïap"), "pynïap")
        self.assertEqual(nominalize("im"), "jingim")
        self.assertEqual(agent_noun("thoh"), "nongthoh")
        self.assertEqual(experiential("bha"), "sngewbha")

    def test_syntax(self):
        s = build_sentence("U briew", "bam", "u ja")
        self.assertEqual(s, "U briew u bam ïa u ja.")
        q = interrogative_sentence("shano", "phi", "leit")
        self.assertEqual(q, "Shano phi leit?")

    def test_adjectives(self):
        self.assertEqual(make_attributive("bha"), "ba-bha")
        self.assertEqual(make_comparative("heh"), "kham heh")
        self.assertEqual(make_comparative("heh", "kata"), "kham heh ban ïa kata")
        self.assertEqual(make_superlative("stad"), "ba-stad tam")
        self.assertEqual(qualify_noun("ka ïing", "heh", attributive=False), "ka ïing heh")
        self.assertEqual(qualify_noun("u briew", "bha", attributive=True), "u briew ba-bha")

    def test_adverbs(self):
        self.assertEqual(reduplicate_adverb("suki"), "suki-suki")
        self.assertEqual(reduplicate_adverb("kloi"), "kloi-kloi")
        cls = classify_adverb("suki")
        self.assertIsNotNone(cls)
        self.assertEqual(cls["type"], "manner")

    def test_echo_words(self):
        echos = list_echo_words()
        self.assertGreater(len(echos), 10)
        found = find_echo_word("ja")
        self.assertIsNotNone(found)
        self.assertIn("ka ja - ka doh", found["compound"])


if __name__ == "__main__":
    unittest.main()
