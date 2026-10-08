# -*- coding: utf-8 -*-
"""Unit tests for khasi.culture.books and top-level whole-book reader APIs."""

import unittest
import khasi
from khasi.culture.books import (
    books,
    list_books,
    get_book,
    search_books,
    total_books,
    total_pages,
    total_words,
    KhasiBook,
    BookPage
)


class TestKhasiBooks(unittest.TestCase):
    """Test suite for digitized Khasi whole books preservation."""

    def test_total_books_count(self):
        """Verify at least 24 digitized books are available."""
        self.assertGreaterEqual(total_books(), 24)
        self.assertEqual(len(books), total_books())

    def test_total_pages_and_words(self):
        """Verify digitized library contains over 1,900 pages and 400,000+ words."""
        self.assertGreater(total_pages(), 1800)
        self.assertGreater(total_words(), 400000)

    def test_list_books(self):
        """Verify list_books returns comprehensive metadata for all titles."""
        all_b = list_books()
        self.assertGreaterEqual(len(all_b), 24)
        first = all_b[0]
        self.assertIn("id", first)
        self.assertIn("title", first)
        self.assertIn("author", first)
        self.assertIn("total_pages", first)
        self.assertIn("total_words", first)

    def test_get_book_by_id(self):
        """Verify retrieving a classical book by id returns all its pages."""
        book = get_book("ka_niam_ki_khasi")
        self.assertIsNotNone(book)
        self.assertIsInstance(book, KhasiBook)
        self.assertEqual(book.id, "ka_niam_ki_khasi")
        self.assertEqual(book.author, "U Sib Charan Roy")
        self.assertGreater(book.total_pages, 50)
        self.assertGreater(book.total_words, 15000)
        self.assertEqual(len(book.pages), book.total_pages)

    def test_get_book_by_title_lookup(self):
        """Verify case-insensitive title lookup works."""
        book = get_book("u khasi hyndai")
        self.assertIsNotNone(book)
        self.assertEqual(book.author, "Dr. H. Lyngdoh")
        self.assertGreater(book.total_pages, 50)

    def test_book_page_navigation(self):
        """Verify page-by-page reading and out-of-range bounds checking."""
        book = get_book("ka_jingsneng_tymmen_part_1")
        self.assertIsNotNone(book)
        p1 = book.get_page(1)
        self.assertIsNotNone(p1)
        self.assertIsInstance(p1, str)
        self.assertIn("JINGSNENG", p1.upper())

        # Test BookPage object
        p_obj = book.get_page_obj(1)
        self.assertIsInstance(p_obj, BookPage)
        self.assertEqual(p_obj.page_number, 1)

        # Test invalid bounds
        self.assertIsNone(book.get_page(0))
        self.assertIsNone(book.get_page(9999))

    def test_book_full_text(self):
        """Verify full_text property aggregates all pages."""
        book = get_book("ka_myntoi")
        self.assertIsNotNone(book)
        full = book.full_text
        self.assertIsInstance(full, str)
        self.assertGreater(len(full), 10000)

    def test_in_book_search(self):
        """Verify searching within a book returns page numbers and snippets."""
        book = get_book("ka_niam_ki_khasi")
        self.assertIsNotNone(book)
        hits = book.search("blei")
        self.assertGreater(len(hits), 0)
        first = hits[0]
        self.assertIn("page_number", first)
        self.assertIn("snippet", first)
        self.assertIn("match_count", first)

    def test_cross_book_universal_search(self):
        """Verify searching across all 24 books returns multi-book hits."""
        hits = search_books("hynniewtrep", max_results_per_book=2)
        self.assertGreater(len(hits), 0)
        book_ids = {h["book_id"] for h in hits}
        self.assertGreaterEqual(len(book_ids), 2)

    def test_books_manager_facade(self):
        """Verify BooksManager facade methods."""
        summary = books.summary()
        self.assertIn("total_books", summary)
        self.assertIn("total_pages", summary)
        self.assertIn("total_words", summary)
        self.assertIn("genres", summary)

        # Dict-like access
        b = books["ka_drama_u_mihsngi"]
        self.assertIsNotNone(b)
        self.assertEqual(b.author, "U Mondon Bareh")

        # Read helper
        txt = books.read("ka_drama_u_mihsngi", 1)
        self.assertIsNotNone(txt)

    def test_top_level_khasi_exports(self):
        """Verify top-level module exposes books reader APIs."""
        self.assertTrue(hasattr(khasi, "books"))
        self.assertTrue(hasattr(khasi, "list_books"))
        self.assertTrue(hasattr(khasi, "get_book"))
        self.assertTrue(hasattr(khasi, "search_books"))
        self.assertTrue(hasattr(khasi, "total_books"))
        self.assertTrue(hasattr(khasi, "total_pages"))
        self.assertTrue(hasattr(khasi, "total_words"))
        self.assertGreaterEqual(khasi.total_books(), 24)


if __name__ == "__main__":
    unittest.main()
