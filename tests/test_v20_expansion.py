import unittest
import khasi
from khasi.culture.deities import DEITIES, get_deity
from khasi.culture.botany import PLANTS, get_plant
from khasi.culture.wildlife import WILDLIFE, get_animal
from khasi.culture.idioms import IDIOMS, get_idiom
from khasi.culture.books import list_books, get_book

class TestV20Expansion(unittest.TestCase):
    def test_book_count_and_batch_14(self):
        books = list_books()
        self.assertGreaterEqual(len(books), 397)
        self.assertGreaterEqual(khasi.total_pages(), 28000)
        self.assertGreaterEqual(khasi.total_words(), 7500000)
        
        # Verify Batch 14 specific books
        b_niam = get_book("rwai_niam_464955")
        self.assertIsNotNone(b_niam)
        self.assertEqual(b_niam.author, "Pariat, A.")
        self.assertGreater(b_niam.total_words, 30000)
        
        b_phawar = get_book("ka_jingsneng_tymmen_shaphang_ka_akor_kha_464867")
        self.assertIsNotNone(b_phawar)
        self.assertEqual(b_phawar.author, "Berry, Radhon Singh")
        
        b_kiang = get_book("u_kiang_nangbah_464458")
        self.assertIsNotNone(b_kiang)
        self.assertEqual(b_kiang.author, "Sumer, S. Quotient")

    def test_total_lexicon_over_400k(self):
        all_words = khasi._DICT.all_words()
        self.assertGreaterEqual(len(all_words), 400000)
        
        # Verify lookups from new corpus
        r1 = khasi.lookup("shkor")
        self.assertIsNotNone(r1)
        r2 = khasi.lookup("pynshai")
        self.assertIsNotNone(r2)
        r3 = khasi.lookup("nongrwai")
        self.assertIsNotNone(r3)

    def test_deities_expansion(self):
        self.assertGreaterEqual(len(DEITIES), 35)
        d_khyrdop = get_deity("lei_khyrdop")
        self.assertIsNotNone(d_khyrdop)
        d_dingiei = get_deity("lei_dingiei")
        self.assertIsNotNone(d_dingiei)
        d_syntiew = get_deity("blei_syntiew")
        self.assertIsNotNone(d_syntiew)

    def test_flora_expansion(self):
        self.assertGreaterEqual(len(PLANTS), 110)
        p_jatira = get_plant("jatira")
        self.assertIsNotNone(p_jatira)
        self.assertIn("Oenanthe", p_jatira["scientific_name"])
        p_sohlyng = get_plant("sohlyngdkhur")
        self.assertIsNotNone(p_sohlyng)
        self.assertEqual(p_sohlyng["scientific_name"], "Morus indica")
        p_soh_ot = get_plant("dieng-soh-ot")
        self.assertIsNotNone(p_soh_ot)

    def test_fauna_expansion(self):
        self.assertGreaterEqual(len(WILDLIFE), 85)
        a_shiriang = get_animal("shiriang")
        self.assertIsNotNone(a_shiriang)
        self.assertEqual(a_shiriang["class_type"], "Mammal")
        a_dkhoh = get_animal("dkhoh")
        self.assertIsNotNone(a_dkhoh)
        self.assertEqual(a_dkhoh["class_type"], "Bird")

    def test_idioms_and_riddles_expansion(self):
        self.assertGreaterEqual(len(IDIOMS), 40)
        i_hok = get_idiom("Kamai-ïa-ka-hok")
        self.assertIsNotNone(i_hok)
        
        riddles = khasi.riddles.all()
        self.assertGreaterEqual(len(riddles), 60)
        
        phrases = khasi.phrases.all()
        self.assertGreaterEqual(len(phrases), 215)

if __name__ == "__main__":
    unittest.main()
