# -*- coding: utf-8 -*-
"""Unit tests for Khasi Folklore and Traditional Songs Preservation Modules."""

import unittest
import khasi
import khasi.folklore as kf
import khasi.songs as ks


class TestKhasiFolkloreAndSongs(unittest.TestCase):
    def test_folklore_total_and_listing(self):
        stories = kf.list_stories()
        self.assertGreaterEqual(len(stories), 12)
        self.assertEqual(kf.total_stories(), len(stories))
        self.assertEqual(len(kf.folklore), len(stories))

    def test_get_story_by_id_and_title(self):
        story = kf.get_story("ka_jingkieng_ksier")
        self.assertIsNotNone(story)
        self.assertEqual(story.id, "ka_jingkieng_ksier")
        self.assertIn("Golden Ladder", story.title)
        self.assertGreater(len(story.khasi_text), 100)
        self.assertGreater(len(story.english_translation), 100)
        self.assertIn("Sohpetbneng", story.geographic_origin)
        self.assertGreaterEqual(len(story.sections), 3)
        self.assertTrue("jingkieng_ksier" in story.vocabulary or "hynniewtrep" in story.vocabulary)

        # Retrieval via approximate title
        story_approx = kf.get_story("diengiei")
        self.assertIsNotNone(story_approx)
        self.assertEqual(story_approx.id, "u_diengiei")

        # Object index access
        story_idx = kf.folklore["u_manik_raitong"]
        self.assertIsNotNone(story_idx)
        self.assertIn("purity", story_idx.cultural_moral.lower())

    def test_search_folklore(self):
        results = kf.search_folklore("thlen")
        self.assertGreaterEqual(len(results), 1)
        first = results[0]
        self.assertIn("story_id", first)
        self.assertIn("matches", first)
        self.assertGreaterEqual(len(first["matches"]), 1)

    def test_stories_by_category_and_summary(self):
        myths = kf.stories_by_category("Creation Myth")
        self.assertGreaterEqual(len(myths), 1)

        summary = kf.folklore.summary()
        self.assertEqual(summary["total_stories"], 12)
        self.assertGreater(summary["total_words"], 5000)

    def test_songs_total_and_listing(self):
        songs_list = ks.list_songs()
        self.assertGreaterEqual(len(songs_list), 10)
        self.assertEqual(ks.total_songs(), len(songs_list))
        self.assertEqual(len(ks.songs), len(songs_list))

    def test_get_song_and_stanzas(self):
        lapalang = ks.get_song("ka_sur_u_sier_lapalang")
        self.assertIsNotNone(lapalang)
        self.assertIn("Lapalang", lapalang.khasi_title)
        self.assertGreater(len(lapalang.lyrics_khasi), 50)
        self.assertGreater(len(lapalang.lyrics_english), 50)
        self.assertTrue(any("Maryngod" in inst for inst in lapalang.instruments))
        self.assertGreaterEqual(len(lapalang.stanzas), 4)

        # H.W. Sten's Duitara collection
        sten = ks.get_song("ki_sur_duitara_ksiar")
        self.assertIsNotNone(sten)
        self.assertEqual(sten.composer, "H.W. Sten")
        self.assertIn("Duitara", sten.instruments)

    def test_search_songs(self):
        results = ks.search_songs("khnam")
        self.assertGreaterEqual(len(results), 1)
        found_archery = any("iasiat" in r["song_id"] or "lapalang" in r["song_id"] for r in results)
        self.assertTrue(found_archery)

    def test_songs_by_category_and_summary(self):
        summary = ks.songs.summary()
        self.assertEqual(summary["total_songs"], 10)
        self.assertGreater(summary["total_words"], 500)

    def test_cultural_lexicon_enrichment(self):
        # Verify newly added words from folklore and songs are searchable in dictionary
        words_to_check = [
            "duitara",
            "sharati",
            "sier lapalang",
            "aitnar",
            "behdeinkhlam",
            "sohpetbneng",
            "diengiei",
            "jamlu",
            "symphiah",
            "ryntieh"
        ]
        for w in words_to_check:
            res = khasi.lookup(w)
            self.assertIsNotNone(res, f"Word '{w}' should be in dictionary")
            self.assertIn("english", res)


if __name__ == "__main__":
    unittest.main()
