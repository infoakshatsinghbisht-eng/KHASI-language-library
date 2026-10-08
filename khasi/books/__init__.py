# -*- coding: utf-8 -*-
"""
Khasi Books & Classical Literature Preservation Module (khasi.books).
======================================================================

Provides direct whole-book reading, page navigation, and full-text search
for 24 foundational Khasi books (1,980+ pages, 470,000+ words).

Usage:
------
>>> import khasi.books as kb
>>> kb.books.summary()
>>> book = kb.get_book("ka_niam_ki_khasi")
>>> book.total_pages
64
>>> print(book.get_page(1))
>>> results = kb.search_books("hynniewtrep")
"""

from ..culture.books import (
    books,
    KhasiBook,
    BookPage,
    list_books,
    get_book,
    search_books,
    total_books,
    total_pages,
    total_words,
    BooksManager,
)

__all__ = [
    "books",
    "KhasiBook",
    "BookPage",
    "list_books",
    "get_book",
    "search_books",
    "total_books",
    "total_pages",
    "total_words",
    "BooksManager",
]
