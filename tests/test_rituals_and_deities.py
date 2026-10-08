# -*- coding: utf-8 -*-
"""Unit tests for Khasi Rituals, Deities, Sacred Sites, and Songs with Lyrics."""

import unittest
import khasi

class TestRitualsAndDeities(unittest.TestCase):

    def test_rituals_presence(self):
        rituals_list = khasi.rituals.all()
        self.assertGreaterEqual(len(rituals_list), 10)
        
        # Test egg divination
        shat = khasi.rituals.get("shat_pylleng")
        self.assertIsNotNone(shat)
        self.assertEqual(shat["category"], "divination")
        self.assertIn("Egg Divination", shat["english_name"])

        # Test bone internment
        mawbah = khasi.rituals.get("thep_mawbah")
        self.assertIsNotNone(mawbah)
        self.assertEqual(mawbah["category"], "funerary")

        # Test category filter
        div_list = khasi.rituals.by_category("divination")
        self.assertGreaterEqual(len(div_list), 2)

    def test_deities_presence(self):
        deities_list = khasi.deities.all()
        self.assertGreaterEqual(len(deities_list), 10)

        # Test Supreme Creator
        creator = khasi.deities.get("nongbuh_nongthaw")
        self.assertIsNotNone(creator)
        self.assertEqual(creator["realm"], "celestial_supreme")

        # Test Lei Shyllong
        shyllong = khasi.deities.get("lei_shyllong")
        self.assertIsNotNone(shyllong)
        self.assertEqual(shyllong["realm"], "mountain_sovereign")

        # Test Mother Earth
        meiramew = khasi.deities.get("meiramew")
        self.assertIsNotNone(meiramew)
        self.assertIn("Mother Earth", meiramew["title"])

        # Test realm filter
        mountain_deities = khasi.deities.by_realm("mountain_sovereign")
        self.assertGreaterEqual(len(mountain_deities), 2)

    def test_sacred_sites_presence(self):
        sites_list = khasi.sacred_sites.all()
        self.assertGreaterEqual(len(sites_list), 7)

        # Test Mawphlang Sacred Forest
        mawphlang = khasi.sacred_sites.get("mawphlang")
        self.assertIsNotNone(mawphlang)
        self.assertEqual(mawphlang["site_type"], "sacred_grove")
        self.assertIn("Labasa", mawphlang["presiding_deity"])

        # Test Nartiang Monoliths
        nartiang = khasi.sacred_sites.get("nartiang")
        self.assertIsNotNone(nartiang)
        self.assertEqual(nartiang["site_type"], "megalithic_monolith")

    def test_folk_song_lyrics(self):
        song = khasi.songs.get("Shad Suk Mynsiem")
        self.assertIsNotNone(song)
        self.assertIn("lyrics_khasi", song)
        self.assertIn("lyrics_english", song)
        self.assertIn("Lympung", song["lyrics_khasi"])
        self.assertIn("thanksgiving", song["lyrics_english"].lower())

        # Test archery phawar
        archery = khasi.songs.get("Iasiat Khnam")
        self.assertIsNotNone(archery)
        self.assertIn("ryntieh", archery["lyrics_khasi"])
        self.assertIn("Hoi kiw", archery["lyrics_khasi"])

    def test_extracted_cultural_vocabulary_lookup(self):
        # Look up words extracted from raw books
        w_phawar = khasi.lookup("phawar")
        self.assertIsNotNone(w_phawar)
        self.assertEqual(w_phawar["category"], "music")

        w_shat = khasi.lookup("shat-pylleng")
        self.assertIsNotNone(w_shat)
        self.assertEqual(w_shat["category"], "rituals")

        w_lei = khasi.lookup("lei-shyllong")
        self.assertIsNotNone(w_lei)
        self.assertEqual(w_lei["category"], "deities")

        w_grove = khasi.lookup("law-kyntang")
        self.assertIsNotNone(w_grove)
        self.assertEqual(w_grove["category"], "sacred_sites")

if __name__ == "__main__":
    unittest.main()
