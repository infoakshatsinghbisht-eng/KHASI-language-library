# -*- coding: utf-8 -*-
"""Unit tests verifying the 100 Whole Books, 150 Traditional Songs, 500 Audio Recordings,
100+ Clans, 50+ Names, 85+ Flora, and 65+ Fauna library expansion."""

import unittest
import khasi

class TestMegaExpansion(unittest.TestCase):

    def test_books_expansion_to_300(self):
        """Verify digitized whole books have reached at least 370."""
        self.assertGreaterEqual(khasi.total_books(), 370)
        self.assertEqual(len(khasi.books), khasi.total_books())
        self.assertGreater(khasi.total_pages(), 25000)
        self.assertGreater(khasi.total_words(), 7000000)

    def test_songs_expansion_to_300(self):
        """Verify songs collection has reached at least 300."""
        self.assertGreaterEqual(khasi.total_songs(), 300)
        from khasi.culture.songs import songs as song_mgr
        self.assertEqual(len(song_mgr), khasi.total_songs())
        summary = song_mgr.summary()
        self.assertGreaterEqual(summary["total_songs"], 300)
        self.assertGreaterEqual(summary["categories_count"], 40)

    def test_speech_audio_expansion_to_500(self):
        """Verify audio dataset has reached exactly 500 recordings and all are valid."""
        ds = khasi.audio_dataset
        self.assertEqual(len(ds), 500)
        integrity = ds.verify_integrity()
        self.assertTrue(integrity["all_healthy"])
        self.assertEqual(integrity["verified_valid"], 500)
        self.assertEqual(len(integrity["missing_files"]), 0)

    def test_clans_and_surnames_expansion(self):
        """Verify clans registry contains over 100 clans and surnames."""
        clans = khasi.list_clans()
        self.assertGreaterEqual(len(clans), 100)
        self.assertEqual(khasi.total_clans(), len(clans))
        
        # Test lookup of historical and branch clans
        syiem = khasi.get_clan("syiem")
        self.assertIsNotNone(syiem)
        self.assertIn("Royal", syiem["category"])

        nongkhlaw = khasi.get_clan("nongkhlaw")
        self.assertIsNotNone(nongkhlaw)

        warjri = khasi.get_clan("warjri")
        self.assertIsNotNone(warjri)

    def test_traditional_names_registry(self):
        """Verify traditional given names contain over 50 entries."""
        names = khasi.list_names()
        self.assertGreaterEqual(len(names), 50)
        self.assertEqual(khasi.total_names(), len(names))

        # Check male, female and unisex lookups
        kynpham = khasi.get_name("kynpham")
        self.assertIsNotNone(kynpham)
        self.assertEqual(kynpham["gender"], "male")

        phyrnai = khasi.get_name("phyrnai")
        self.assertIsNotNone(phyrnai)
        self.assertEqual(phyrnai["gender"], "female")

        sngewbha = khasi.get_name("sngewbha")
        self.assertIsNotNone(sngewbha)
        self.assertEqual(sngewbha["gender"], "unisex")

        # Test filtering by gender
        females = khasi.list_names(gender="female")
        self.assertGreaterEqual(len(females), 15)

    def test_botany_flora_expansion(self):
        """Verify botanical database contains 105 species."""
        plants = khasi.list_plants()
        self.assertGreaterEqual(len(plants), 105)
        self.assertEqual(khasi.total_plants(), len(plants))

        pitcher = khasi.get_plant("Nepenthes khasiana")
        self.assertIsNotNone(pitcher)

        oak = khasi.get_plant("sning")
        self.assertIsNotNone(oak)

        meds = khasi.medicinal_plants()
        self.assertGreaterEqual(len(meds), 15)

    def test_wildlife_fauna_expansion(self):
        """Verify wildlife zoological database contains 80 species."""
        wildlife = khasi.list_wildlife()
        self.assertGreaterEqual(len(wildlife), 80)
        self.assertEqual(khasi.total_wildlife(), len(wildlife))

        clouded = khasi.get_animal("khla-lyngngoh")
        self.assertIsNotNone(clouded)
        self.assertEqual(clouded["class_type"], "Mammal")

        hornbill = khasi.get_animal("kohkarang")
        self.assertIsNotNone(hornbill)
        self.assertEqual(hornbill["class_type"], "Bird")

        mahseer = khasi.get_animal("kha-saw")
        self.assertIsNotNone(mahseer)
        self.assertEqual(mahseer["class_type"], "Fish")

    def test_deities_and_culture(self):
        """Verify traditional deities count reaches 29 and idioms reach 37."""
        self.assertGreaterEqual(len(khasi.culture.deities.DEITIES), 29)
        self.assertGreaterEqual(len(khasi.culture.idioms.IDIOMS), 37)

    def test_lexicon_mega_wordbase(self):
        """Verify massive headword dictionary reaches over 384,000 entries."""
        kd = khasi.KhasiDictionary()
        self.assertGreaterEqual(len(kd.all_words()), 384000)
        self.assertGreaterEqual(len(kd.all_phrases()), 205)
        self.assertGreaterEqual(len(kd.all_riddles()), 50)

if __name__ == "__main__":
    unittest.main()
