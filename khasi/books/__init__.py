# -*- coding: utf-8 -*-
"""
Khasi Books & Classical Literature Preservation Module (khasi.books).
======================================================================

Provides direct whole-book reading, page navigation, and full-text search
for 714 digitized Khasi books (84,370+ pages, 18,890,000+ words).

Usage:
------
>>> import khasi.books as kb
>>> len(kb.list_books())
714
>>> book = kb.get_book("u_sier_lapalang")
>>> book.total_pages
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
