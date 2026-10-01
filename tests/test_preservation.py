# -*- coding: utf-8 -*-
"""Unit tests for Khasi digital preservation and corpus archiving."""

import unittest
from khasi.preservation import CorpusManager, PreservationRecord

class TestKhasiPreservation(unittest.TestCase):
    def test_record_creation(self):
        rec = PreservationRecord(
            id="test-001",
            title_khasi="Ka Nohkalikai",
            title_english="Legend of Likai",
            khasi_text="Ka la don ka samla kaba kyrteng ka Likai ha Sohra.",
            english_translation="There lived a young woman named Likai in Sohra."
        )
        self.assertEqual(rec.id, "test-001")
        d = rec.to_dict()
        self.assertIn("title_khasi", d)

    def test_text_validation(self):
        manager = CorpusManager()
        valid_res = manager.validate_text("Khublei shibun, nga ieit ïa phi.")
        self.assertTrue(valid_res["valid"])
        self.assertTrue(valid_res["has_khasi_diacritics"])

        invalid_res = manager.validate_text("zoo zebra")
        self.assertFalse(invalid_res["valid"])

if __name__ == "__main__":
    unittest.main()
