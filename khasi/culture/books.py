# -*- coding: utf-8 -*-
"""
Khasi Classical & Digitized Books Preservation Module (Ka Thiar Kot Khasi).
=============================================================================

Provides full digitized whole-book access (all pages, chapters, and metadata)
for 24 foundational Khasi literary, theological, dramatic, historical, and
linguistic masterpieces.

Key Features:
- Page-by-page text navigation (`book.get_page(page_number)`)
- Full concatenated book text access (`book.full_text`)
- In-book search across pages with text snippets (`book.search("...")`)
- Universal full-text search across all 24 books (`search_books("...")`)
- Rich metadata: Title, native title, author, year, genre, chapters, total words
"""

import json
import re
from pathlib import Path
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any, Union

_BOOKS_DATA_DIR = Path(__file__).resolve().parent / "data" / "books"
_INDEX_PATH = _BOOKS_DATA_DIR / "books_index.json"

_BOOKS_INDEX_CACHE: Optional[List[Dict[str, Any]]] = None
_BOOK_CACHE: Dict[str, "KhasiBook"] = {}


@dataclass
class BookPage:
    """Represents a single page in a Khasi book."""
    page_number: int
    text: str
    word_count: int

    def contains(self, query: str, case_sensitive: bool = False) -> bool:
        """Check if query is in this page's text."""
        if case_sensitive:
            return query in self.text
        return query.lower() in self.text.lower()


@dataclass
class KhasiBook:
    """Represents a complete Khasi book with all its pages, chapters, and metadata."""
    id: str
    title: str
    native_title: str
    author: str
    year: int
    genre: str
    description: str
    total_pages: int
    total_words: int
    chapters: List[str]
    source_type: str
    pages: List[BookPage] = field(repr=False)

    @property
    def full_text(self) -> str:
        """Return the entire concatenated text of the book across all pages."""
        return "\n\n".join(p.text for p in self.pages if p.text)

    def get_page(self, page_number: int) -> Optional[str]:
        """Return the text of a specific 1-indexed page."""
        if 1 <= page_number <= len(self.pages):
            return self.pages[page_number - 1].text
        return None

    def get_page_obj(self, page_number: int) -> Optional[BookPage]:
        """Return the BookPage object for a specific 1-indexed page."""
        if 1 <= page_number <= len(self.pages):
            return self.pages[page_number - 1]
        return None

    def read(self, page_number: int = 1) -> Optional[str]:
        """Convenience alias for get_page."""
        return self.get_page(page_number)

    def search(self, query: str, case_sensitive: bool = False) -> List[Dict[str, Any]]:
        """Search for a keyword or phrase across all pages of this book.
        
        Returns:
            List of dicts: [
                {
                    "page_number": int,
                    "match_count": int,
                    "snippet": str
                }
            ]
        """
        results = []
        q_target = query if case_sensitive else query.lower()

        for page in self.pages:
            t = page.text if case_sensitive else page.text.lower()
            if q_target in t:
                matches = list(re.finditer(re.escape(q_target), t))
                # Create context snippet around first match
                first_m = matches[0]
                start = max(0, first_m.start() - 60)
                end = min(len(page.text), first_m.end() + 60)
                snippet = page.text[start:end].strip()
                if start > 0:
                    snippet = "..." + snippet
                if end < len(page.text):
                    snippet = snippet + "..."

                results.append({
                    "book_id": self.id,
                    "title": self.title,
                    "author": self.author,
                    "page_number": page.page_number,
                    "match_count": len(matches),
                    "snippet": snippet
                })

        return results

    def to_dict(self, include_pages: bool = False) -> Dict[str, Any]:
        """Convert book to dictionary representation."""
        data = {
            "id": self.id,
            "title": self.title,
            "native_title": self.native_title,
            "author": self.author,
            "year": self.year,
            "genre": self.genre,
            "description": self.description,
            "total_pages": self.total_pages,
            "total_words": self.total_words,
            "chapter_count": len(self.chapters),
            "chapters": self.chapters,
            "source_type": self.source_type
        }
        if include_pages:
            data["pages"] = [
                {"page_number": p.page_number, "text": p.text, "word_count": p.word_count}
                for p in self.pages
            ]
        return data


def _load_index() -> List[Dict[str, Any]]:
    global _BOOKS_INDEX_CACHE
    if _BOOKS_INDEX_CACHE is None:
        if _INDEX_PATH.exists():
            with open(_INDEX_PATH, "r", encoding="utf-8") as f:
                _BOOKS_INDEX_CACHE = json.load(f)
        else:
            _BOOKS_INDEX_CACHE = []
    return _BOOKS_INDEX_CACHE


def list_books() -> List[Dict[str, Any]]:
    """Return summary metadata for all 24 digitized books in the library."""
    return list(_load_index())


def get_book(id_or_title: str) -> Optional[KhasiBook]:
    """Retrieve a Khasi book by slug ID or matching title.
    
    Loads and caches the full book content including all individual pages.
    """
    key = id_or_title.strip().lower()

    # Check cache
    if key in _BOOK_CACHE:
        return _BOOK_CACHE[key]

    # Resolve filename
    idx = _load_index()
    matched_id: Optional[str] = None

    for item in idx:
        if (item["id"].lower() == key or 
            item["title"].lower() == key or 
            key in item["title"].lower() or
            key in item.get("native_title", "").lower()):
            matched_id = item["id"]
            break

    if not matched_id:
        # Check direct filename
        cand = _BOOKS_DATA_DIR / f"{key}.json"
        if cand.exists():
            matched_id = key

    if not matched_id:
        return None

    # Load book file
    book_file = _BOOKS_DATA_DIR / f"{matched_id}.json"
    if not book_file.exists():
        return None

    with open(book_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    pages = [
        BookPage(
            page_number=p["page_number"],
            text=p["text"],
            word_count=p.get("word_count", len(p["text"].split()))
        )
        for p in data.get("pages", [])
    ]

    book = KhasiBook(
        id=data["id"],
        title=data["title"],
        native_title=data.get("native_title", data["title"]),
        author=data["author"],
        year=data.get("year", 0),
        genre=data.get("genre", "Literature"),
        description=data.get("description", ""),
        total_pages=data.get("total_pages", len(pages)),
        total_words=data.get("total_words", sum(p.word_count for p in pages)),
        chapters=data.get("chapters", []),
        source_type=data.get("source_type", "digital_edition"),
        pages=pages
    )

    _BOOK_CACHE[matched_id] = book
    _BOOK_CACHE[book.title.lower()] = book
    return book


def search_books(query: str, max_results_per_book: int = 5) -> List[Dict[str, Any]]:
    """Perform full-text search across ALL 24 books and all pages.
    
    Args:
        query: Search string (e.g. 'u hynniewtrep', 'ka hok', 'sohpetbneng')
        max_results_per_book: Max page hits to return per matching book
        
    Returns:
        List of matching page hits with snippet, book title, author, and page number.
    """
    results = []
    idx = _load_index()
    for item in idx:
        b = get_book(item["id"])
        if not b:
            continue
        book_hits = b.search(query)
        if book_hits:
            results.extend(book_hits[:max_results_per_book])
    return results


def total_books() -> int:
    """Return the total number of whole digitized books available (24)."""
    return len(_load_index())


def total_pages() -> int:
    """Return the total number of digitized pages across all books."""
    return sum(b.get("total_pages", 0) for b in _load_index())


def total_words() -> int:
    """Return the total number of words across all digitized book pages."""
    return sum(b.get("total_words", 0) for b in _load_index())


class BooksManager:
    """Object-oriented facade for reading, searching, and inspecting Khasi books."""

    def __len__(self) -> int:
        return total_books()

    def __iter__(self):
        for b in list_books():
            yield get_book(b["id"])

    def __getitem__(self, item: str) -> Optional[KhasiBook]:
        return get_book(item)

    def all(self) -> List[Dict[str, Any]]:
        """List summary metadata of all books."""
        return list_books()

    def get(self, id_or_title: str) -> Optional[KhasiBook]:
        """Get full book instance by ID or title."""
        return get_book(id_or_title)

    def read(self, id_or_title: str, page_number: int = 1) -> Optional[str]:
        """Read specific page text from a book."""
        b = get_book(id_or_title)
        if b:
            return b.get_page(page_number)
        return None

    def search(self, query: str, max_results_per_book: int = 5) -> List[Dict[str, Any]]:
        """Search query across all books and all pages."""
        return search_books(query, max_results_per_book)

    def summary(self) -> Dict[str, Any]:
        """Return statistical overview of the digitized book preservation library."""
        idx = _load_index()
        authors = {}
        genres = {}
        for b in idx:
            a = b["author"]
            authors[a] = authors.get(a, 0) + 1
            g = b["genre"]
            genres[g] = genres.get(g, 0) + 1

        return {
            "total_books": len(idx),
            "total_pages": sum(b["total_pages"] for b in idx),
            "total_words": sum(b["total_words"] for b in idx),
            "authors_count": len(authors),
            "genres_count": len(genres),
            "genres": genres,
            "top_authors": sorted(authors.items(), key=lambda x: x[1], reverse=True)[:5]
        }


# Global instance for top-level usage
books = BooksManager()
