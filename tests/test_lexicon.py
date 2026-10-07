# -*- coding: utf-8 -*-
"""Unit tests for Khasi dictionary and lexicon."""

import unittest
from khasi.lexicon import KhasiDictionary, get_morphology_engine

class TestKhasiLexicon(unittest.TestCase):
    def setUp(self):
        self.d = KhasiDictionary()

    def test_lookup_exact(self):
        res = self.d.lookup("khublei")
        self.assertIsNotNone(res)
        self.assertEqual(res["pos"], "interjection")

    def test_lookup_with_article(self):
        res = self.d.lookup("u briew")
        self.assertIsNotNone(res)
        self.assertEqual(res["khasi"], "briew")

    def test_lookup_stem_fallback(self):
        res = self.d.lookup("jingtrei")
        self.assertIsNotNone(res)
        self.assertEqual(res.get("root"), "trei")

    def test_search(self):
        results = self.d.search("mountain")
        self.assertTrue(len(results) > 0)
        self.assertTrue(any(r["khasi"] == "lum" for r in results))

    def test_all_collections(self):
        self.assertGreaterEqual(len(self.d.all_words()), 100000)
        self.assertTrue(len(self.d.all_phrases()) >= 10)
        self.assertTrue(len(self.d.all_proverbs()) >= 5)
        self.assertTrue(len(self.d.all_riddles()) >= 4)

    def test_morphology_engine(self):
        engine = get_morphology_engine()
        self.assertGreaterEqual(engine.total_forms_count(), 300000)

if __name__ == "__main__":
    unittest.main()
