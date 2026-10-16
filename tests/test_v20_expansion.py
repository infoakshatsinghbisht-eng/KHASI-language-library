import unittest
import khasi
from khasi.culture.deities import DEITIES, get_deity
from khasi.culture.botany import PLANTS, get_plant
from khasi.culture.wildlife import WILDLIFE, get_animal
from khasi.culture.idioms import IDIOMS, get_idiom
from khasi.culture.books import list_books, get_book

class TestV20Expansion(unittest.TestCase):
    def test_book_count_and_batch_15(self):
        books = list_books()
        self.assertGreaterEqual(len(books), 421)
        self.assertGreaterEqual(khasi.total_pages(), 32000)
        self.assertGreaterEqual(khasi.total_words(), 8300000)
        
        # Verify Batch 15 specific books
        b_phuit = get_book("phuit_ka_sabuit_bad_kiwei_kiwei_de_khana_464512")
        self.assertIsNotNone(b_phuit)
        self.assertGreater(b_phuit.total_words, 70000)
        
        b_pnar = get_book("nait_o_ka_kot_parom_ion_pnar_467592")
        self.assertIsNotNone(b_pnar)
        self.assertGreater(b_pnar.total_words, 40000)

    def test_total_lexicon_over_415k(self):
        all_words = khasi._DICT.all_words()
        self.assertGreaterEqual(len(all_words), 415000)
        
        # Verify lookups from new corpus
        r1 = khasi.lookup("shkor")
        self.assertIsNotNone(r1)
        r2 = khasi.lookup("pynshai")
        self.assertIsNotNone(r2)
        r3 = khasi.lookup("nongrwai")
        self.assertIsNotNone(r3)

    def test_deities_expansion(self):
        self.assertGreaterEqual(len(DEITIES), 39)
        d_khyrdop = get_deity("lei_khyrdop")
        self.assertIsNotNone(d_khyrdop)
        d_symper = get_deity("lei_symper")
        self.assertIsNotNone(d_symper)

    def test_flora_expansion(self):
        self.assertGreaterEqual(len(PLANTS), 112)
        p_jatira = get_plant("jatira")
        self.assertIsNotNone(p_jatira)
        self.assertIn("Oenanthe", p_jatira["scientific_name"])
        p_tit = get_plant("tit-tung")
        self.assertIsNotNone(p_tit)

    def test_fauna_expansion(self):
        self.assertGreaterEqual(len(WILDLIFE), 89)
        a_sier = get_animal("sier-lapalang")
        self.assertIsNotNone(a_sier)
        self.assertEqual(a_sier["class_type"], "Mammal")

    def test_idioms_and_riddles_expansion(self):
        self.assertGreaterEqual(len(IDIOMS), 45)
        i_hok = get_idiom("Kamai-ïa-ka-hok")
        self.assertIsNotNone(i_hok)
        
        riddles = khasi.riddles.all()
        self.assertGreaterEqual(len(riddles), 66)
        
        phrases = khasi.phrases.all()
        self.assertGreaterEqual(len(phrases), 223)

if __name__ == "__main__":
    unittest.main()
