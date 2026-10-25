# -*- coding: utf-8 -*-
"""Unit tests for Sentence-Aligned Parallel Corpora and MT Benchmarks."""

import unittest
import os
import json
import tempfile
from khasi import parallel_corpus, ParallelCorpus

SAMPLE_RECORDS = [
    {
        "id": f"SMP_{i:03d}",
        "source_book": "Ka Niam Jong Ki Khasi" if i < 50 else ("Ka Jingiaid U Pilgrim" if i < 80 else "Ki Dienjat Jong Ki Longshwa & Kot Pule"),
        "author": "U Sib Charan Roy",
        "year": 1919,
        "section": "Chapter 1",
        "paragraph_id": i,
        "khasi": f"U briew u wan sha kane ka pyrthei ban kamai ïa ka Hok num {i}." if i < 50 else f"U Pilgrim u ïaid lynti sha ka shnong kaba khraw num {i}.",
        "english": f"Man came into this world to earn righteousness num {i}." if i < 50 else f"Pilgrim journeyed towards the celestial city num {i}.",
        "domain": "culture_philosophy",
        "split": "train" if i < 80 else "test",
        "book_id": "ka_niam" if i < 50 else "pilgrim"
    }
    for i in range(1, 105)
]

class TestParallelCorpus(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.temp_dir = tempfile.TemporaryDirectory()
        cls.sample_path = os.path.join(cls.temp_dir.name, "sample_parallel.json")
        with open(cls.sample_path, "w", encoding="utf-8") as f:
            json.dump(SAMPLE_RECORDS, f)

    @classmethod
    def tearDownClass(cls):
        cls.temp_dir.cleanup()

    def setUp(self):
        if len(parallel_corpus) >= 100:
            self.corpus = parallel_corpus
        else:
            self.corpus = ParallelCorpus(self.sample_path, include_books=False)

    def test_corpus_size_and_sources(self):
        self.assertGreaterEqual(len(self.corpus), 100)
        stats = self.corpus.get_stats()
        self.assertIn("Ka Niam Jong Ki Khasi", stats["sources"])
        self.assertIn("Ka Jingiaid U Pilgrim", stats["sources"])
        self.assertIn("Ki Dienjat Jong Ki Longshwa & Kot Pule", stats["sources"])
        self.assertGreaterEqual(stats["sources"]["Ka Niam Jong Ki Khasi"], 40)
        self.assertGreaterEqual(stats["sources"]["Ka Jingiaid U Pilgrim"], 30)

    def test_sentence_pairs_alignment(self):
        pairs = self.corpus.get_pairs()
        self.assertGreaterEqual(len(pairs), 100)
        for kh, en in pairs[:10]:
            self.assertTrue(len(kh) > 5)
            self.assertTrue(len(en) > 5)

    def test_filtering_and_splits(self):
        niam_pairs = self.corpus.get_records(source="Niam")
        self.assertGreaterEqual(len(niam_pairs), 40)

        pilgrim_pairs = self.corpus.get_records(source="Pilgrim")
        self.assertGreaterEqual(len(pilgrim_pairs), 30)

        train = self.corpus.get_records(split="train")
        test = self.corpus.get_records(split="test")
        self.assertGreater(len(train), 70)
        self.assertGreater(len(test), 20)

    def test_search_parallel(self):
        res = self.corpus.search("Hok")
        self.assertGreaterEqual(len(res), 5)
        res_pilgrim = self.corpus.search("Pilgrim")
        self.assertGreaterEqual(len(res_pilgrim), 5)

    def test_export_bitext_and_tmx(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            kha_file = os.path.join(tmpdir, "train.kha")
            en_file = os.path.join(tmpdir, "train.en")
            tmx_file = os.path.join(tmpdir, "memory.tmx")
            hf_file = os.path.join(tmpdir, "hf_parallel.jsonl")

            n_bitext = self.corpus.export_bitext(kha_file, en_file)
            n_tmx = self.corpus.export_tmx(tmx_file)
            n_hf = self.corpus.export_huggingface_format(hf_file)

            self.assertGreaterEqual(n_bitext, 100)
            self.assertGreaterEqual(n_tmx, 100)
            self.assertGreaterEqual(n_hf, 100)

            self.assertTrue(os.path.exists(kha_file))
            self.assertTrue(os.path.exists(en_file))
            self.assertTrue(os.path.exists(tmx_file))
            self.assertTrue(os.path.exists(hf_file))

    def test_bleu_computation(self):
        ref = ["U briew u leit sha ïing"]
        hyp = ["U briew u leit sha ïing"]
        bleu = ParallelCorpus.compute_bleu(hyp, ref)
        self.assertEqual(bleu["bleu"], 100.0)

        hyp_partial = ["U briew u leit sha shnong"]
        bleu_part = ParallelCorpus.compute_bleu(hyp_partial, ref)
        self.assertGreater(bleu_part["p1"], 50.0)

if __name__ == "__main__":
    unittest.main()
