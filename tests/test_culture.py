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
    catalogue,
    all_works,
    by_genre,
    by_author,
    search_works,
    get_digitized_works,
    catalogue_summary,
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
        self.assertGreaterEqual(len(auth), 12)
        self.assertTrue(any("Soso Tham" in a["name"] for a in auth))
        self.assertTrue(any("Streamlet Dkhar" in a["name"] for a in auth))
        self.assertTrue(any("Radhon Singh" in a["name"] for a in auth))
        ep = epics()
        self.assertGreaterEqual(len(ep), 6)
        self.assertTrue(any("Sohpetbneng" in e["title"] for e in ep))
        self.assertTrue(any("Meiramew" in e["title"] for e in ep))
        po = poems()
        self.assertGreaterEqual(len(po), 4)

    def test_kinship(self):
        terms = list_kinship_terms()
        self.assertIn("Khadduh", terms)
        self.assertIn("Kñi", terms)
        desc = describe_matrilineal_system()
        self.assertIn("Ultimogeniture", desc["inheritance_rule"])

    def test_bibliography_catalogue(self):
        # Total works check
        works = all_works()
        self.assertGreaterEqual(len(works), 200)
        self.assertEqual(len(catalogue), len(works))

        # Check filtering by genre
        novels = by_genre("literature")
        self.assertGreater(len(novels), 20)
        
        # Check filtering by author
        nongrum_works = by_author("Nongrum")
        self.assertGreaterEqual(len(nongrum_works), 20)
        self.assertTrue(any("Ka Pung Ka Jingieit" in w["title"] for w in nongrum_works))

        # Check search functionality
        search_res = search_works("Pilgrim")
        self.assertTrue(any("Ka Jingiaid U Pilgrim" in w["title"] for w in search_res))

        # Check digitized works filter
        digitized = get_digitized_works()
        self.assertGreater(len(digitized), 10)
        self.assertTrue(any("Jeebon Roy" in w["author"] for w in digitized))

        # Check catalogue summary
        summary = catalogue_summary()
        self.assertIn("total_works", summary)
        self.assertGreaterEqual(summary["total_works"], 300)
        self.assertIn("genres", summary)

if __name__ == "__main__":
    unittest.main()
