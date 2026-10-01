# -*- coding: utf-8 -*-
"""Unit tests for Khasi phonetics and orthography."""

import unittest
from khasi.phonetics import (
    normalize,
    tokenize,
    syllables,
    detect_script,
    latin_to_devanagari,
    devanagari_to_latin,
    is_khasi_word,
    has_khasi_diacritics,
    expand_contractions,
)

class TestKhasiPhonetics(unittest.TestCase):
    def test_normalize_apostrophe_and_diacritics(self):
        raw = "ngam tip ba phi leit sha iing"
        norm = normalize(raw)
        self.assertIn("ïing", norm)

    def test_expand_contractions(self):
        text = "ngam wan"
        expanded = expand_contractions(text)
        self.assertEqual(expanded, "nga ym wan")

    def test_detect_script(self):
        self.assertEqual(detect_script("Khublei"), "latin")
        self.assertEqual(detect_script("खुब्लेई"), "devanagari_translit")

    def test_tokenize(self):
        tokens = tokenize("Khublei shibun! Nga ieit ïa phi.")
        self.assertIn("Khublei", tokens)
        self.assertIn("!", tokens)
        self.assertIn("ïa", tokens)

    def test_syllables(self):
        syl = syllables("khublei")
        self.assertTrue(len(syl) >= 2)

    def test_is_khasi_word(self):
        self.assertTrue(is_khasi_word("khublei"))
        self.assertTrue(is_khasi_word("ïing"))
        self.assertFalse(is_khasi_word("zoo"))

    def test_has_khasi_diacritics(self):
        self.assertTrue(has_khasi_diacritics("ïing"))
        self.assertTrue(has_khasi_diacritics("shñiuh"))
        self.assertFalse(has_khasi_diacritics("lum"))

    def test_devanagari_translit(self):
        dev = latin_to_devanagari("khublei")
        self.assertTrue(len(dev) > 0)
        back = devanagari_to_latin(dev)
        self.assertTrue(len(back) > 0)

if __name__ == "__main__":
    unittest.main()
