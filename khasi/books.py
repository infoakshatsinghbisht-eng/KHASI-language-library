# -*- coding: utf-8 -*-
"""
Khasi Digitized Books & Literature Library Module
=================================================

Exposes the full digitized book library across `khasi.books`.
Provides page-by-page text navigation, cover-to-cover text reading,
and cross-book keyword search for all public domain Khasi literature.
"""

from .culture.books import (
    BookPage,
    KhasiBook,
    Book,
    BooksManager,
    list_books,
    get_book,
    get_book_full_text,
    get_master_compendium_path,
    get_master_jsonl_path,
    get_pure_khasi_master_text_path,
    get_pure_khasi_master_jsonl_path,
    search_books,
    total_books,
    total_pages,
    total_words,
    books,
)

__all__ = [
    "BookPage",
    "KhasiBook",
    "Book",
    "BooksManager",
    "list_books",
    "get_book",
    "get_book_full_text",
    "get_master_compendium_path",
    "get_master_jsonl_path",
    "get_pure_khasi_master_text_path",
    "get_pure_khasi_master_jsonl_path",
    "search_books",
    "total_books",
    "total_pages",
    "total_words",
    "books",
]


