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
    get_author,
    get_epic,
    search_literature,
    list_kinship_terms,
    get_kinship_info,
    search_kinship,
    describe_matrilineal_system,
    catalogue,
    all_works,
    by_genre,
    by_author,
    by_type,
    search_works,
    get_digitized_works,
    catalogue_summary,
    list_instruments,
    get_instrument,
    list_songs,
    get_song,
    list_musicians,
    list_plants,
    get_plant,
    by_plant_type,
    medicinal_plants,
    list_wildlife,
    get_animal,
    by_wildlife_class,
    list_dishes,
    get_dish,
    by_cuisine_category,
    list_places,
    get_place,
    by_geography_type,
    list_clans,
    get_clan,
    search_clans,
    list_idioms,
    get_idiom,
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

    def test_expanded_music_and_instruments(self):
        insts = list_instruments()
        self.assertGreaterEqual(len(insts), 10)
        duitara = get_instrument("duitara")
        self.assertIsNotNone(duitara)
        self.assertIn("Lute", duitara["category"])

        tangmuri = get_instrument("tangmuri")
        self.assertIsNotNone(tangmuri)

        songs = list_songs()
        self.assertGreaterEqual(len(songs), 5)
        self.assertTrue(any("Lapalang" in s["title"] for s in songs))

        musicians = list_musicians()
        self.assertGreaterEqual(len(musicians), 5)
        self.assertTrue(any("Wahlang" in m["name"] for m in musicians))

    def test_botany(self):
        plants = list_plants()
        self.assertGreaterEqual(len(plants), 25)
        sohiong = get_plant("sohiong")
        self.assertIsNotNone(sohiong)
        self.assertIn("Prunus nepalensis", sohiong["scientific_name"])

        trees = by_plant_type("tree")
        self.assertGreaterEqual(len(trees), 5)

        meds = medicinal_plants()
        self.assertGreaterEqual(len(meds), 10)

    def test_wildlife(self):
        wildlife = list_wildlife()
        self.assertGreaterEqual(len(wildlife), 15)
        tiger = get_animal("khla")
        self.assertIsNotNone(tiger)
        self.assertEqual(tiger["class_type"], "Mammal")

        birds = by_wildlife_class("bird")
        self.assertGreaterEqual(len(birds), 4)

    def test_cuisine(self):
        dishes = list_dishes()
        self.assertGreaterEqual(len(dishes), 15)
        jadoh = get_dish("jadoh")
        self.assertIsNotNone(jadoh)
        self.assertIn("pork", jadoh["ingredients"].lower())

        rice_dishes = by_cuisine_category("rice")
        self.assertGreaterEqual(len(rice_dishes), 3)

    def test_geography(self):
        places = list_places()
        self.assertGreaterEqual(len(places), 20)
        umngot = get_place("umngot")
        self.assertIsNotNone(umngot)
        self.assertIn("Dawki", umngot["location"])

        waterfalls = by_geography_type("waterfall")
        self.assertGreaterEqual(len(waterfalls), 4)

        caves = by_geography_type("cave")
        self.assertGreaterEqual(len(caves), 3)

    def test_clans(self):
        clans = list_clans()
        self.assertGreaterEqual(len(clans), 25)
        lyngdoh = get_clan("lyngdoh")
        self.assertIsNotNone(lyngdoh)
        self.assertIn("Priestly", lyngdoh["category"])

        res = search_clans("sohra")
        self.assertTrue(len(res) > 0)

    def test_idioms(self):
        idioms = list_idioms()
        self.assertGreaterEqual(len(idioms), 20)
        horkit = get_idiom("horkit")
        self.assertIsNotNone(horkit)
        self.assertIn("resolutely", horkit["meaning"].lower())

    def test_expanded_literature_and_authors(self):
        auth = authors()
        self.assertGreaterEqual(len(auth), 20)
        bareh = get_author("Victor Bareh")
        self.assertIsNotNone(bareh)

        ep = epics()
        self.assertGreaterEqual(len(ep), 12)
        lapalang = get_epic("Lapalang")
        self.assertIsNotNone(lapalang)

        search_res = search_literature("Tirot Sing")
        self.assertTrue(len(search_res["authors"]) > 0 or len(search_res["epics"]) > 0 or len(search_res["poems"]) > 0)

if __name__ == "__main__":
    unittest.main()
