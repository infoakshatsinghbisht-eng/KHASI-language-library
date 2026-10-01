# -*- coding: utf-8 -*-
"""Unit tests for Khasi culture, festivals, calendar, and matrilineal kinship."""

import unittest
from khasi.culture import (
    get_current_season,
    get_current_khasi_month,
    get_market_day,
    list_festivals,
    get_festival,
    authors,
    epics,
    poems,
    list_kinship_terms,
    get_kinship_info,
    describe_matrilineal_system,
    KHASI_MONTHS,
    MARKET_CYCLE,
)

class TestKhasiCulture(unittest.TestCase):
    def test_calendar_and_months(self):
        self.assertEqual(len(KHASI_MONTHS), 12)
        m = get_current_khasi_month()
        self.assertIn("name", m)
        s = get_current_season()
        self.assertIn("name_khasi", s)

    def test_market_cycle(self):
        self.assertEqual(len(MARKET_CYCLE), 8)
        d1 = get_market_day(1)
        self.assertEqual(d1["name"], "Sngi Iewduh")

    def test_festivals(self):
        f_list = list_festivals()
        self.assertGreaterEqual(len(f_list), 4)
        nongkrem = get_festival("Nongkrem")
        self.assertIsNotNone(nongkrem)
        self.assertIn("Smit", nongkrem["location"])

    def test_literature(self):
        auth = authors()
        self.assertTrue(any("Soso Tham" in a["name"] for a in auth))
        ep = epics()
        self.assertTrue(any("Sohpetbneng" in e["title"] for e in ep))
        po = poems()
        self.assertTrue(len(po) >= 2)

    def test_kinship(self):
        terms = list_kinship_terms()
        self.assertIn("Khadduh", terms)
        self.assertIn("Kñi", terms)
        desc = describe_matrilineal_system()
        self.assertIn("Ultimogeniture", desc["inheritance_rule"])

if __name__ == "__main__":
    unittest.main()
