# -*- coding: utf-8 -*-
"""Unit tests for Khasi Indigenous Roots (Ki Ktien Tynrai) and Phonaesthetic Expressives."""

import unittest
import khasi

class TestTynraiRoots(unittest.TestCase):

    def test_roots_presence(self):
        root_list = khasi.roots.all()
        self.assertGreaterEqual(len(root_list), 25)

        # Test Eye (Khmat)
        khmat = khasi.roots.get("khmat")
        self.assertIsNotNone(khmat)
        self.assertEqual(khmat["category"], "anatomy")
        self.assertIn("Mon-Khmer", khmat["austroasiatic_family"])

        # Test Womb / Matrilineal branch (Kpoh)
        kpoh = khasi.roots.get("kpoh")
        self.assertIsNotNone(kpoh)
        self.assertEqual(kpoh["gender"], "ka")
        self.assertIn("womb", kpoh["english"].lower())

        # Test Righteousness (Hok)
        hok = khasi.roots.get("hok")
        self.assertIsNotNone(hok)
        self.assertEqual(hok["category"], "philosophy")
        self.assertIn("righteousness", hok["english"].lower())

        # Test category filtering
        anatomy_roots = khasi.roots.by_category("anatomy")
        self.assertGreaterEqual(len(anatomy_roots), 8)

    def test_expressives_presence(self):
        exp_list = khasi.expressives.all()
        self.assertGreaterEqual(len(exp_list), 20)

        # Test dazzling white
        white = khasi.expressives.get("lieh phyrnai")
        self.assertIsNotNone(white)
        self.assertEqual(white["domain"], "light_and_color")
        self.assertIn("white", white["english"])

        # Test pitch black
        black = khasi.expressives.get("iong thiej")
        self.assertIsNotNone(black)
        self.assertIn("black", black["english"])

        # Test soothing warmth
        warmth = khasi.expressives.get("syaid lumbor")
        self.assertIsNotNone(warmth)
        self.assertEqual(warmth["domain"], "temperature_sensation")

        # Test rock hard
        hard = khasi.expressives.get("eh tian")
        self.assertIsNotNone(hard)
        self.assertEqual(hard["domain"], "texture_sensation")

        # Test graceful gait
        gait = khasi.expressives.get("iaid wiar-wiar")
        self.assertIsNotNone(gait)
        self.assertEqual(gait["domain"], "movement_gait")

    def test_lexicon_tynrai_integration(self):
        # Verify that original roots are in words.json lookup
        r_shkor = khasi.lookup("shkor")
        self.assertIsNotNone(r_shkor)
        self.assertIn("कान", r_shkor["hindi"])
        self.assertIn("tynrai", r_shkor["tags"])

        r_rngiew = khasi.lookup("rngiew")
        self.assertIsNotNone(r_rngiew)
        self.assertIn("aura", r_rngiew["english"].lower())

        r_white = khasi.lookup("lieh phyrnai")
        self.assertIsNotNone(r_white)
        self.assertEqual(r_white["pos"], "adverb")

        r_dorbar = khasi.lookup("ka dorbar")
        self.assertIsNotNone(r_dorbar)
        self.assertIn("council", r_dorbar["english"].lower())

if __name__ == "__main__":
    unittest.main()
