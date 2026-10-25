# -*- coding: utf-8 -*-
"""Unit tests for Khasi classical grammar rules and extended syntax builders."""

import unittest
import khasi
from khasi.grammar import (
    grammar_rules,
    GrammarRule,
    CLASSICAL_GRAMMAR_RULES,
    build_complex_sentence,
    build_conditional_sentence,
    build_relative_clause,
    build_comparative_sentence,
    build_passive_sentence,
)


class TestClassicalGrammarRules(unittest.TestCase):
    def test_total_rules_count(self):
        """Verify at least 100 classical grammar rules are catalogued."""
        rules = grammar_rules.all()
        self.assertGreaterEqual(len(rules), 100)
        self.assertEqual(len(rules), len(CLASSICAL_GRAMMAR_RULES))

    def test_get_rule_by_id(self):
        """Verify retrieval of specific rules by ID."""
        r1 = grammar_rules.get("AGR-01")
        self.assertIsNotNone(r1)
        self.assertEqual(r1.name, "Mandatory Article Prefixation")
        self.assertIn("u / ka / i / ki", r1.formula)
        self.assertTrue(len(r1.khasi_examples) > 0)
        self.assertTrue(len(r1.english_translations) > 0)

        r2 = grammar_rules.get("tam-02")  # case-insensitive check
        self.assertIsNotNone(r2)
        self.assertIn("Past Particle", r2.name)

        r_synteng = grammar_rules.get("CAS-09")
        self.assertIsNotNone(r_synteng)
        self.assertIn("Synteng", r_synteng.name)
        self.assertIn("che", r_synteng.formula)

        r_optative = grammar_rules.get("TAM-15")
        self.assertIsNotNone(r_optative)
        self.assertIn("Cohortative", r_optative.name)

        r_glottal = grammar_rules.get("PHO-02")
        self.assertIsNotNone(r_glottal)
        self.assertIn("Glottal", r_glottal.name)

        r_dir = grammar_rules.get("DER-11")
        self.assertIsNotNone(r_dir)
        self.assertIn("Directional", r_dir.name)

        r_concessive = grammar_rules.get("CLA-10")
        self.assertIsNotNone(r_concessive)
        self.assertIn("Concessive", r_concessive.name)

        r_recip = grammar_rules.get("TAM-18")
        self.assertIsNotNone(r_recip)
        self.assertIn("Reciprocal", r_recip.name)

        r_tree_num = grammar_rules.get("NUM-05")
        self.assertIsNotNone(r_tree_num)
        self.assertIn("Arboreal", r_tree_num.name)

        r_tag = grammar_rules.get("DIS-04")
        self.assertIsNotNone(r_tag)
        self.assertIn("Tag Enclitic", r_tag.name)

        r_sesqui = grammar_rules.get("PHO-01")
        self.assertIsNotNone(r_sesqui)
        self.assertIn("Sesquisyllabic", r_sesqui.name)

        # Batch 1 rules verification
        r_agr08 = grammar_rules.get("AGR-08")
        self.assertIsNotNone(r_agr08)
        self.assertIn("Epicene Feminine Agreement", r_agr08.name)

        r_tam22 = grammar_rules.get("TAM-22")
        self.assertIsNotNone(r_tam22)
        self.assertIn("Definite Assured Prospective", r_tam22.name)

        r_cas10 = grammar_rules.get("CAS-10")
        self.assertIsNotNone(r_cas10)
        self.assertIn("Sociative / Comitative", r_cas10.name)

        r_der12 = grammar_rules.get("DER-12")
        self.assertIsNotNone(r_der12)
        self.assertIn("Antonymic and Pejorative", r_der12.name)

        r_cla11 = grammar_rules.get("CLA-11")
        self.assertIsNotNone(r_cla11)
        self.assertIn("Comparative and Superlative", r_cla11.name)

        r_exp11 = grammar_rules.get("EXP-11")
        self.assertIsNotNone(r_exp11)
        self.assertIn("Ideophonic Sensory Expressives", r_exp11.name)

        r_num07 = grammar_rules.get("NUM-07")
        self.assertIsNotNone(r_num07)
        self.assertIn("Marketplace Measure Classifiers", r_num07.name)

        r_dis05 = grammar_rules.get("DIS-05")
        self.assertIsNotNone(r_dis05)
        self.assertIn("Topicalizing and Contrastive Focus", r_dis05.name)

        r_pho05 = grammar_rules.get("PHO-05")
        self.assertIsNotNone(r_pho05)
        self.assertIn("Morpho-Phonological Glide Epenthesis", r_pho05.name)

        r_tam23 = grammar_rules.get("TAM-23")
        self.assertIsNotNone(r_tam23)
        self.assertIn("Intensive Deliberative Aspect Marker", r_tam23.name)

        # Rules 91-100 verification
        r_tam24 = grammar_rules.get("TAM-24")
        self.assertIsNotNone(r_tam24)
        self.assertIn("Historical Optative-Precative", r_tam24.name)

        r_tam25 = grammar_rules.get("TAM-25")
        self.assertIsNotNone(r_tam25)
        self.assertIn("Sequential Concomitant Aspect", r_tam25.name)

        r_agr09 = grammar_rules.get("AGR-09")
        self.assertIsNotNone(r_agr09)
        self.assertIn("Honorific Diminutive Agreement", r_agr09.name)

        r_cas11 = grammar_rules.get("CAS-11")
        self.assertIsNotNone(r_cas11)
        self.assertIn("Synteng / Pnar Locative Postpositional", r_cas11.name)

        r_der13 = grammar_rules.get("DER-13")
        self.assertIsNotNone(r_der13)
        self.assertIn("Reciprocal Collectivity Compound Prefix", r_der13.name)

        r_cla12 = grammar_rules.get("CLA-12")
        self.assertIsNotNone(r_cla12)
        self.assertIn("Temporal Subordinating Clause Inversion", r_cla12.name)

        r_exp12 = grammar_rules.get("EXP-12")
        self.assertIsNotNone(r_exp12)
        self.assertIn("Phonaesthetic Reduplicative Attenuative", r_exp12.name)

        r_num08 = grammar_rules.get("NUM-08")
        self.assertIsNotNone(r_num08)
        self.assertIn("Botanical Cluster and Sheaf Classifiers", r_num08.name)

        r_dis06 = grammar_rules.get("DIS-06")
        self.assertIsNotNone(r_dis06)
        self.assertIn("Assertive Emphatic Enclitic", r_dis06.name)

        r_pho06 = grammar_rules.get("PHO-06")
        self.assertIsNotNone(r_pho06)
        self.assertIn("Consonant Gemination and Coda Lenition", r_pho06.name)

        r_invalid = grammar_rules.get("NONEXISTENT-99")
        self.assertIsNone(r_invalid)

    def test_filter_by_category(self):
        """Verify category filtering across nominal, verbal, case, morphology, clause, expressive."""
        agr_rules = grammar_rules.by_category("Nominal Agreement")
        self.assertGreaterEqual(len(agr_rules), 8)

        tam_rules = grammar_rules.by_category("Tense-Aspect-Mood")
        self.assertGreaterEqual(len(tam_rules), 23)

        cas_rules = grammar_rules.by_category("Case Marking")
        self.assertGreaterEqual(len(cas_rules), 10)

        der_rules = grammar_rules.by_category("Derivational Morphology")
        self.assertGreaterEqual(len(der_rules), 12)

        cla_rules = grammar_rules.by_category("Complex Syntax")
        self.assertGreaterEqual(len(cla_rules), 11)

        exp_rules = grammar_rules.by_category("Enclitics & Expressives")
        self.assertGreaterEqual(len(exp_rules), 11)

        cls_rules = grammar_rules.by_category("Numeral Classifiers")
        self.assertGreaterEqual(len(cls_rules), 7)

        dis_rules = grammar_rules.by_category("Discourse Particles")
        self.assertGreaterEqual(len(dis_rules), 5)

        pho_rules = grammar_rules.by_category("Phonotactics & Morpho-Phonology")
        self.assertGreaterEqual(len(pho_rules), 3)

    def test_search_rules(self):
        """Verify searching rules by keyword."""
        res_cond = grammar_rules.search("conditional")
        self.assertTrue(any(r.id == "CLA-01" for r in res_cond))

        res_noh = grammar_rules.search("noh")
        self.assertTrue(any(r.id == "EXP-01" for r in res_noh))

        res_pyn = grammar_rules.search("pyn-")
        self.assertTrue(any(r.id == "DER-02" for r in res_pyn))

        res_ngut = grammar_rules.search("ngut")
        self.assertTrue(any(r.id == "CLS-01" for r in res_ngut))

    def test_summary(self):
        """Verify statistical summary reporting."""
        summary = grammar_rules.summary()
        self.assertGreaterEqual(summary["total_rules"], 90)
        self.assertGreaterEqual(summary["categories_count"], 9)
        self.assertIn("sources", summary)
        self.assertTrue(len(summary["sources"]) >= 4)


class TestExtendedSyntaxBuilders(unittest.TestCase):
    def test_build_complex_sentence(self):
        """Test complex sentence clause linking with conjunctions."""
        sent = build_complex_sentence("u la leit", "ka la slap", conjunction="namar ba")
        self.assertEqual(sent, "u la leit namar ba ka la slap.")

        sent2 = build_complex_sentence("nga la ïohi", "u la don hangta", conjunction="ba")
        self.assertEqual(sent2, "nga la ïohi ba u la don hangta.")

    def test_build_conditional_sentence(self):
        """Test conditional sentence builder (standard and concessive)."""
        # Standard: Lada phi wan, ngan leit.
        sent1 = build_conditional_sentence("phi wan", "ngan leit", concessive=False)
        self.assertEqual(sent1, "Lada phi wan, ngan leit.")

        # Concessive: Wat la u la pyrshang, pynban u la rem.
        sent2 = build_conditional_sentence("u la pyrshang", "u la rem", concessive=True)
        self.assertEqual(sent2, "Wat la u la pyrshang, pynban u la rem.")

    def test_build_relative_clause(self):
        """Test relative clause builder with gender markers."""
        # Masculine: u briew uba la wan
        rel_m = build_relative_clause("u briew", "la wan", gender="u")
        self.assertEqual(rel_m, "u briew uba la wan")

        # Feminine: ka samla kaba trei shitom
        rel_f = build_relative_clause("ka samla", "trei shitom", gender="ka")
        self.assertEqual(rel_f, "ka samla kaba trei shitom")

        # Plural: ki khynnah kiba rwai
        rel_pl = build_relative_clause("ki khynnah", "rwai", gender="ki")
        self.assertEqual(rel_pl, "ki khynnah kiba rwai")

        # Diminutive: i khunlung iba ïam
        rel_dim = build_relative_clause("i khunlung", "ïam", gender="i")
        self.assertEqual(rel_dim, "i khunlung iba ïam")

    def test_build_comparative_sentence(self):
        """Test comparative sentence construction."""
        comp = build_comparative_sentence("u ksew", "ka miaw", "heh")
        self.assertEqual(comp, "u ksew u kham heh ban ïa ka miaw.")

    def test_build_passive_sentence(self):
        """Test passive sentence construction (adversative vs neutral)."""
        # Adversative passive with shah
        pass_adv = build_passive_sentence("u nongtuh", "kem", agent="ki pulit", adversative=True)
        self.assertEqual(pass_adv, "u nongtuh u la shah kem ha ki pulit.")

        # Neutral passive with da
        pass_ben = build_passive_sentence("u khynnah", "hikai", agent="ka nonghikai", adversative=False)
        self.assertEqual(pass_ben, "u khynnah u la hikai da ka nonghikai.")

    def test_top_level_package_exports(self):
        """Verify new grammar features are exported directly from khasi namespace."""
        self.assertTrue(hasattr(khasi, "grammar_rules"))
        self.assertTrue(hasattr(khasi, "GrammarRule"))
        self.assertTrue(hasattr(khasi, "build_complex_sentence"))
        self.assertTrue(hasattr(khasi, "build_conditional_sentence"))
        self.assertTrue(hasattr(khasi, "build_relative_clause"))
        self.assertTrue(hasattr(khasi, "build_comparative_sentence"))
        self.assertTrue(hasattr(khasi, "build_passive_sentence"))
        self.assertGreaterEqual(len(khasi.grammar_rules.all()), 90)


if __name__ == "__main__":
    unittest.main()
