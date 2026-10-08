# -*- coding: utf-8 -*-
"""Unit tests for Khasi Dialectology & Dedicated Sub-Lexicons."""

import unittest
from khasi import dialects
from khasi.lexicon.dialects import (
    list_dialects,
    load_dialect_lexicon,
    lookup_dialect,
    translate_dialect,
    find_cognates,
    get_dialect_statistics,
)

class TestDialectology(unittest.TestCase):

    def test_list_dialects(self):
        d_list = list_dialects()
        self.assertIn("pnar", d_list)
        self.assertIn("war", d_list)
        self.assertIn("bhoi", d_list)
        self.assertIn("maram", d_list)
        self.assertIn("sohra", d_list)

    def test_pnar_lexicon_size(self):
        pnar_words = load_dialect_lexicon("pnar")
        self.assertGreaterEqual(len(pnar_words), 5000, "Pnar lexicon should have 5,000+ words")

    def test_war_lexicon_size(self):
        war_words = load_dialect_lexicon("war")
        self.assertGreaterEqual(len(war_words), 5000, "War lexicon should have 5,000+ words")

    def test_bhoi_and_maram_lexicons(self):
        bhoi_words = load_dialect_lexicon("bhoi")
        maram_words = load_dialect_lexicon("maram")
        self.assertGreaterEqual(len(bhoi_words), 1000)
        self.assertGreaterEqual(len(maram_words), 1000)

    def test_dialect_lookup(self):
        res_pnar = lookup_dialect("mei", "pnar")
        self.assertIsNotNone(res_pnar)
        self.assertEqual(res_pnar["dialect_word"], "bei")

        res_war = lookup_dialect("kpa", "war")
        self.assertIsNotNone(res_war)
        self.assertEqual(res_war["dialect_word"], "po")

    def test_cognates_search(self):
        cogs = find_cognates("briew")
        self.assertEqual(cogs["sohra"], "briew")
        self.assertEqual(cogs["pnar"], "bru")
        self.assertEqual(cogs["war"], "brou")

    def test_translate_dialect(self):
        # Sohra to Pnar translation
        sohra_txt = "U briew u ieit ia ka mei bad u kpa ha ïing."
        pnar_txt = translate_dialect(sohra_txt, from_dialect="sohra", to_dialect="pnar")
        self.assertIn("bru", pnar_txt)
        self.assertIn("maya", pnar_txt)
        self.assertIn("bei", pnar_txt)
        self.assertIn("pa", pnar_txt)
        self.assertIn("ïung", pnar_txt)

        # Sohra to War translation
        sohra_txt2 = "U briew u leit sha ïing ban bam ja bad dih um."
        war_txt = translate_dialect(sohra_txt2, from_dialect="sohra", to_dialect="war")
        self.assertIn("brou", war_txt)
        self.assertIn("hie", war_txt)
        self.assertIn("ba", war_txt)
        self.assertIn("am", war_txt)

    def test_dialect_statistics(self):
        stats = get_dialect_statistics()
        self.assertIn("pnar", stats)
        self.assertIn("war", stats)
        self.assertGreaterEqual(stats["pnar"]["word_count"], 5000)
        self.assertGreaterEqual(stats["war"]["word_count"], 5000)

    def test_facade_access(self):
        self.assertIn("pnar", dialects.list())
        self.assertEqual(dialects.cognates("briew")["pnar"], "bru")

if __name__ == "__main__":
    unittest.main()
