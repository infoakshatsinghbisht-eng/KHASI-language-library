# -*- coding: utf-8 -*-
"""Unit tests for Khasi Attire, Textiles, Jewellery, Regalia, and Expanded Rituals."""

import unittest
import khasi

class TestAttireAndRituals(unittest.TestCase):

    def test_garments_presence(self):
        garments = khasi.clothing.all()
        self.assertGreaterEqual(len(garments), 8)

        # Test Jainsem
        jainsem = khasi.clothing.get("jainsem")
        self.assertIsNotNone(jainsem)
        self.assertEqual(jainsem["gender"], "female")
        self.assertIn("Two-Piece", jainsem["english_name"])

        # Test Dhara
        dhara = khasi.clothing.get("dhara")
        self.assertIsNotNone(dhara)
        self.assertIn("Shad Suk Mynsiem", dhara["occasions"])

        # Test Jymphong
        jymphong = khasi.clothing.get("jymphong")
        self.assertIsNotNone(jymphong)
        self.assertEqual(jymphong["gender"], "male")

        # Test Spong
        spong = khasi.clothing.get("spong")
        self.assertIsNotNone(spong)
        self.assertEqual(spong["type"], "headwear")

        # Test filter by gender
        female_wear = khasi.clothing.by_gender("female")
        self.assertTrue(any(g["id"] == "jainsem" for g in female_wear))

    def test_textiles_and_fabrics(self):
        fabric_list = khasi.fabrics.all()
        self.assertGreaterEqual(len(fabric_list), 4)

        # Test Ryndia (Eri silk)
        ryndia = khasi.fabrics.get("ryndia")
        self.assertIsNotNone(ryndia)
        self.assertIn("Ri Bhoi", ryndia["origin_region"])
        self.assertIn("Peace-Silk", ryndia["english_name"])

        # Test Thoh Khyrwang
        thoh = khasi.fabrics.get("thoh_khyrwang_fabric")
        self.assertIsNotNone(thoh)
        self.assertIn("Jaintia", thoh["origin_region"])

    def test_jewellery_presence(self):
        jewels = khasi.jewellery.all()
        self.assertGreaterEqual(len(jewels), 10)

        # Test Pansngiat
        pansngiat = khasi.jewellery.get("pansngiat")
        self.assertIsNotNone(pansngiat)
        self.assertIn("Crown", pansngiat["english_name"])
        self.assertEqual(pansngiat["gender"], "female")

        # Test Paila (coral and gold)
        paila = khasi.jewellery.get("paila")
        self.assertIsNotNone(paila)
        self.assertIn("Coral", paila["english_name"])

        # Test Shanryndang choker
        choker = khasi.jewellery.get("shanryndang")
        self.assertIsNotNone(choker)
        self.assertEqual(choker["body_location"], "Throat / Neck")

        # Test Mahu armlets
        mahu = khasi.jewellery.get("mahu")
        self.assertIsNotNone(mahu)
        self.assertEqual(mahu["gender"], "male")

    def test_regalia_and_weapons(self):
        regalia_items = khasi.regalia.all()
        self.assertGreaterEqual(len(regalia_items), 6)

        # Test Waitlam broadsword
        waitlam = khasi.regalia.get("waitlam")
        self.assertIsNotNone(waitlam)
        self.assertIn("Broadsword", waitlam["english_name"])

        # Test Stieh shield
        stieh = khasi.regalia.get("stieh")
        self.assertIsNotNone(stieh)
        self.assertIn("Shield", stieh["english_name"])

        # Test Symphiah whisk
        whisk = khasi.regalia.get("symphiah")
        self.assertIsNotNone(whisk)
        self.assertIn("Whisk", whisk["english_name"])

    def test_expanded_rituals(self):
        rituals_list = khasi.rituals.all()
        self.assertGreaterEqual(len(rituals_list), 15)

        # Test Behdeinkhlam
        behdein = khasi.rituals.get("behdeinkhlam_tapmohkhlieh")
        self.assertIsNotNone(behdein)
        self.assertIn("Behdeinkhlam", behdein["name"])

        # Test Mawbynna erection
        mawbynna = khasi.rituals.get("knia_mawbynna")
        self.assertIsNotNone(mawbynna)
        self.assertEqual(mawbynna["category"], "memorial")

        # Test Knia Pyrda
        pyrda = khasi.rituals.get("knia_pyrda_kmie")
        self.assertIsNotNone(pyrda)
        self.assertIn("Iawbei", pyrda["significance"])

        # Test Pyniasoh Kpoh
        kpoh = khasi.rituals.get("pyniasoh_kpoh")
        self.assertIsNotNone(kpoh)
        self.assertEqual(kpoh["category"], "kinship")

    def test_new_songs_with_stanzas(self):
        all_songs = khasi.songs.all()
        self.assertGreaterEqual(len(all_songs), 28)

        # Test Ballad of U Thlen
        thlen_song = khasi.songs.get("ka_rwai_u_thlen")
        self.assertIsNotNone(thlen_song)
        self.assertIn("Dainthlen", thlen_song["title"])
        self.assertIn("lyrics_khasi", thlen_song)
        self.assertIn("Suidnoh", thlen_song["lyrics_khasi"])
        self.assertEqual(len(thlen_song["stanzas"]), 4)

        # Test Sun and Moon song
        sun_song = khasi.songs.get("ka_rwai_ka_sngi_bad_u_bnai")
        self.assertIsNotNone(sun_song)
        self.assertIn("dpei", sun_song["lyrics_khasi"])

        # Test Phawar song
        phawar_song = khasi.songs.get("phawar_kynjoh_khaskhain")
        self.assertIsNotNone(phawar_song)
        self.assertIn("Hoiw-kiw", phawar_song["lyrics_khasi"])

    def test_lexicon_attire_lookup(self):
        res = khasi.lookup("jainsem")
        self.assertIsNotNone(res)
        self.assertEqual(res["pos"], "noun")
        self.assertEqual(res["gender"], "feminine")
        self.assertIn("पोशाक", res["hindi"])

        res2 = khasi.lookup("ryndia")
        self.assertIsNotNone(res2)
        self.assertIn("silk", res2["tags"])

        res3 = khasi.lookup("pansngiat")
        self.assertIsNotNone(res3)
        self.assertIn("gold", res3["tags"])

if __name__ == "__main__":
    unittest.main()
