# -*- coding: utf-8 -*-
"""Unit tests for Khasi number system."""

import unittest
from khasi.numbers import (
    num_to_words,
    words_to_num,
    ordinal,
    fraction,
)

class TestKhasiNumbers(unittest.TestCase):
    def test_basic_units(self):
        self.assertEqual(num_to_words(0), "nod")
        self.assertEqual(num_to_words(1), "wei")
        self.assertEqual(num_to_words(5), "san")
        self.assertEqual(num_to_words(9), "khyndai")

    def test_teens_and_tens(self):
        self.assertEqual(num_to_words(10), "shiphew")
        self.assertEqual(num_to_words(11), "khatwei")
        self.assertEqual(num_to_words(20), "arphew")
        self.assertEqual(num_to_words(42), "sawphew ar")

    def test_hundreds_and_thousands(self):
        self.assertEqual(num_to_words(100), "shispah")
        self.assertEqual(num_to_words(200), "arspah")
        self.assertEqual(num_to_words(1000), "shihajar")

    def test_words_to_num(self):
        self.assertEqual(words_to_num("sawphew ar"), 42)
        self.assertEqual(words_to_num("shispah"), 100)

    def test_ordinal_and_fraction(self):
        self.assertEqual(ordinal(1), "ba-nyngkong")
        self.assertEqual(ordinal(2), "ba-ar")
        self.assertEqual(fraction(1, 2), "shiteng")
        self.assertEqual(fraction(1, 4), "shikhana")

if __name__ == "__main__":
    unittest.main()
