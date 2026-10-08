# -*- coding: utf-8 -*-
"""Comprehensive tests for Khasi Language Library top-level API."""

import unittest
import khasi

class TestKhasiTopLevel(unittest.TestCase):
    def test_metadata(self):
        self.assertEqual(khasi.__version__, "1.4.0")
        self.assertEqual(khasi.__author__, "Akshat Singh Bisht")
        self.assertEqual(khasi.ISO_639_3, "kha")
        self.assertEqual(khasi.NATIVE_NAME, "Ka Ktien Khasi")
        self.assertIsNotNone(khasi.dialects)
        self.assertIsNotNone(khasi.audio_dataset)
        self.assertIsNotNone(khasi.parallel_corpus)

    def test_translation(self):
        res = khasi.translate("How are you?")
        self.assertEqual(res.text, "Kumno phi long?")
        self.assertEqual(res.target_lang, "khasi")

        res_hi = khasi.translate("आप कैसे हैं?")
        self.assertEqual(res_hi.text, "Kumno phi long?")

        res_pnar = khasi.translate("I love you", dialect="pnar")
        self.assertIn("maya", res_pnar.text)

    def test_numbers(self):
        self.assertEqual(khasi.num_to_words(0), "nod")
        self.assertEqual(khasi.num_to_words(1), "wei")
        self.assertEqual(khasi.num_to_words(42), "sawphew ar")
        self.assertEqual(khasi.words_to_num("sawphew ar"), 42)
        self.assertEqual(khasi.ordinal(1), "ba-nyngkong")
        self.assertEqual(khasi.ordinal(2), "ba-ar")

    def test_dictionary_lookup(self):
        res = khasi.lookup("khublei")
        self.assertIsNotNone(res)
        self.assertTrue("hello" in res["english"].lower() or "thank you" in res["english"].lower())

        search_res = khasi.search("water")
        self.assertTrue(len(search_res) > 0)
        self.assertTrue(any(w["khasi"] == "um" for w in search_res))

    def test_grammar_conjugation(self):
        past = khasi.conjugate("wan", tense="past", pronoun="u")
        self.assertEqual(past, "u la wan")

        fut = khasi.conjugate("wan", tense="future", pronoun="u")
        self.assertEqual(fut, "un wan")

        caus = khasi.causative("ïap")
        self.assertEqual(caus, "pynïap")

        nom = khasi.nominalize("stad")
        self.assertEqual(nom, "jingstad")

        ag = khasi.agent_noun("hikai")
        self.assertEqual(ag, "nonghikai")

    def test_morphology_universe(self):
        total = khasi.total_word_forms()
        self.assertGreaterEqual(total, 300000)

        analysis = khasi.analyze("jingstad")
        self.assertIsNotNone(analysis)
        self.assertEqual(analysis.lemma, "stad")

    def test_culture_calendar(self):
        season = khasi.get_current_season()
        self.assertIn("name_khasi", season)
        self.assertEqual(len(khasi.get_months()), 12)

        festivals = khasi.list_festivals()
        self.assertGreaterEqual(len(festivals), 4)
        self.assertTrue(any("Nongkrem" in f["name"] for f in festivals))

    def test_proverbs_and_phrases(self):
        p = khasi.proverbs.random()
        self.assertIsNotNone(p)
        self.assertIn("khasi", p)

        ph = khasi.phrases.random()
        self.assertIsNotNone(ph)
        self.assertIn("khasi", ph)

    def test_voice(self):
        ssml = khasi.KhasiVoiceSynthesizer.get_speech_ssml("Khublei shibun")
        self.assertIn("<speak>", ssml)
        self.assertIn("Khublei shibun", ssml)

        wav = khasi.KhasiVoiceSynthesizer.generate_pcm_wav(0.1)
        self.assertTrue(wav.startswith(b"RIFF"))

    def test_expanded_knowledge_facades(self):
        # Instruments
        insts = khasi.instruments.all()
        self.assertGreaterEqual(len(insts), 10)
        duitara = khasi.instruments.get("duitara")
        self.assertIsNotNone(duitara)
        self.assertIn("Lute", duitara["category"])

        # Songs
        sngs = khasi.songs.all()
        self.assertGreaterEqual(len(sngs), 5)
        self.assertTrue(any("Lapalang" in s["title"] for s in sngs))

        # Plants
        plnts = khasi.plants.all()
        self.assertGreaterEqual(len(plnts), 25)
        pitcher = khasi.plants.get("Nepenthes")
        self.assertIsNotNone(pitcher)
        self.assertIn("Nepenthes khasiana", pitcher["scientific_name"])
        meds = khasi.plants.medicinal()
        self.assertGreaterEqual(len(meds), 10)

        # Wildlife
        fauna = khasi.wildlife.all()
        self.assertGreaterEqual(len(fauna), 15)
        leopard = khasi.wildlife.get("Neofelis")
        self.assertIsNotNone(leopard)

        # Cuisine
        dsh = khasi.dishes.all()
        self.assertGreaterEqual(len(dsh), 15)
        jadoh = khasi.dishes.get("jadoh")
        self.assertIsNotNone(jadoh)

        # Places / Geography
        plcs = khasi.places.all()
        self.assertGreaterEqual(len(plcs), 20)
        nohkalikai = khasi.places.get("nohkalikai")
        self.assertIsNotNone(nohkalikai)

        # Clans
        cln_list = khasi.clans.all()
        self.assertGreaterEqual(len(cln_list), 25)
        syiem_clan = khasi.clans.get("syiem")
        self.assertIsNotNone(syiem_clan)

        # Idioms
        idms = khasi.idioms.all()
        self.assertGreaterEqual(len(idms), 20)
        horkit = khasi.idioms.get("horkit")
        self.assertIsNotNone(horkit)

if __name__ == "__main__":
    unittest.main()
