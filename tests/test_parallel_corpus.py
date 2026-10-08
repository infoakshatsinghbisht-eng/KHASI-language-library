# -*- coding: utf-8 -*-
"""Unit tests for Sentence-Aligned Parallel Corpora and MT Benchmarks."""

import unittest
import os
import tempfile
from khasi import parallel_corpus, ParallelCorpus

class TestParallelCorpus(unittest.TestCase):

    def setUp(self):
        self.corpus = parallel_corpus

    def test_corpus_size_and_sources(self):
        self.assertGreaterEqual(len(self.corpus), 100)
        stats = self.corpus.get_stats()
        self.assertIn("Ka Niam Jong Ki Khasi", stats["sources"])
        self.assertIn("Ka Jingiaid U Pilgrim", stats["sources"])
        self.assertIn("Ki Dienjat Jong Ki Longshwa & Kot Pule", stats["sources"])
        self.assertGreaterEqual(stats["sources"]["Ka Niam Jong Ki Khasi"], 40)
        self.assertGreaterEqual(stats["sources"]["Ka Jingiaid U Pilgrim"], 40)

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
        self.assertGreaterEqual(len(pilgrim_pairs), 40)

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
        # Perfect match
        ref = ["U briew u leit sha ïing"]
        hyp = ["U briew u leit sha ïing"]
        bleu = ParallelCorpus.compute_bleu(hyp, ref)
        self.assertEqual(bleu["bleu"], 100.0)

        # Partial match
        hyp_partial = ["U briew u leit sha shnong"]
        bleu_part = ParallelCorpus.compute_bleu(hyp_partial, ref)
        self.assertGreater(bleu_part["p1"], 50.0)

if __name__ == "__main__":
    unittest.main()
