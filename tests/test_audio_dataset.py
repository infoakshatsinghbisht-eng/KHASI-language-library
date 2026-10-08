# -*- coding: utf-8 -*-
"""Unit tests for Khasi Audio Waveform Dataset & Manifests."""

import unittest
import os
import tempfile
from khasi import audio_dataset, KhasiAudioDataset

class TestAudioDataset(unittest.TestCase):

    def setUp(self):
        self.ds = audio_dataset

    def test_dataset_size(self):
        # Must have exactly 252 recordings (187 phrases + 65 proverbs)
        self.assertEqual(len(self.ds), 252)

    def test_phrases_and_proverbs_breakdown(self):
        stats = self.ds.get_stats()
        self.assertEqual(stats["total_phrases"], 187)
        self.assertEqual(stats["total_proverbs"], 65)
        self.assertEqual(stats["sample_rate_hz"], 16000)
        self.assertGreater(stats["total_duration_seconds"], 500)

    def test_splits(self):
        train = self.ds.get_records(split="train")
        val = self.ds.get_records(split="validation")
        test = self.ds.get_records(split="test")
        self.assertGreater(len(train), 180)
        self.assertGreater(len(val), 20)
        self.assertGreater(len(test), 20)
        self.assertEqual(len(train) + len(val) + len(test), 252)

    def test_all_audio_files_integrity(self):
        # Critical test: verify that all 252 files physically exist on disk and are valid 16kHz mono WAV
        res = self.ds.verify_integrity()
        self.assertTrue(res["all_healthy"], f"Integrity check failed: {res}")
        self.assertEqual(res["verified_valid"], 252)
        self.assertEqual(len(res["missing_files"]), 0)
        self.assertEqual(len(res["corrupted_files"]), 0)

    def test_get_item_and_audio_bytes(self):
        item = self.ds.get_item("phrase_001")
        self.assertIsNotNone(item)
        self.assertEqual(item["khasi_text"], "Khublei!")

        wav_bytes = self.ds.get_audio_bytes("phrase_001")
        self.assertIsNotNone(wav_bytes)
        self.assertGreater(len(wav_bytes), 1000)
        # Check standard RIFF header signature
        self.assertTrue(wav_bytes.startswith(b"RIFF"))

    def test_search_audio(self):
        results = self.ds.search_audio("khublei")
        self.assertGreaterEqual(len(results), 1)

    def test_export_formats(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            hf_path = os.path.join(tmpdir, "dataset.jsonl")
            cv_path = os.path.join(tmpdir, "common_voice.tsv")
            n_hf = self.ds.export_huggingface_format(hf_path)
            n_cv = self.ds.export_common_voice_tsv(cv_path)
            self.assertEqual(n_hf, 252)
            self.assertEqual(n_cv, 252)
            self.assertTrue(os.path.exists(hf_path))
            self.assertTrue(os.path.exists(cv_path))

if __name__ == "__main__":
    unittest.main()
