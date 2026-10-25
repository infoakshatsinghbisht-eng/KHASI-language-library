# -*- coding: utf-8 -*-
"""
Khasi Classical & Digitized Books Preservation Module (Ka Thiar Kot Khasi).
=============================================================================

Provides full digitized whole-book access (all pages, chapters, and metadata)
for 714 foundational Khasi literary, theological, dramatic, historical, and
linguistic masterpieces (84,370+ pages, 18,890,000+ words).

Key Features:
- Page-by-page text navigation (`book.get_page(page_number)`)
- Full concatenated book text access (`book.full_text`)
- In-book search across pages with text snippets (`book.search("...")`)
- Universal full-text search across all 714 books (`search_books("...")`)
- Rich metadata: Title, native title, author, year, genre, chapters, total words
"""

import json
import re
import urllib.request
import urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any, Union

_BOOKS_DATA_DIR = Path(__file__).resolve().parent / "data" / "books"
_INDEX_PATH = _BOOKS_DATA_DIR / "books_index.json"
_GITHUB_RAW_BOOKS_BASE = "https://raw.githubusercontent.com/infoakshatsinghbisht-eng/KHASI-language-library/main/khasi/culture/data/books"

_BOOKS_INDEX_CACHE: Optional[List[Dict[str, Any]]] = None
_BOOK_CACHE: Dict[str, "KhasiBook"] = {}


def _get_cache_dir() -> Path:
    """Return user cache directory for downloaded Khasi book JSON files."""
    cache = Path.home() / ".cache" / "pykhasi" / "books"
    try:
        cache.mkdir(parents=True, exist_ok=True)
    except Exception:
        pass
    return cache


def _resolve_book_path(book_id: str, auto_download: bool = True) -> Optional[Path]:
    """Resolve book file path from local package data, user cache, or online GitHub repository."""
    # 1. Check local package data directory
    p_local = _BOOKS_DATA_DIR / f"{book_id}.json"
    if p_local.exists():
        return p_local

    # 2. Check user cache directory
    cache_dir = _get_cache_dir()
    p_cache = cache_dir / f"{book_id}.json"
    if p_cache.exists():
        return p_cache

    if not auto_download:
        return None

    # 3. Auto-download from official GitHub repository
    url = f"{_GITHUB_RAW_BOOKS_BASE}/{book_id}.json"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "pykhasi-client/1.16.0"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            content = resp.read()

        # Try saving to local package dir if writable
        try:
            p_local.write_bytes(content)
            return p_local
        except (PermissionError, OSError):
            p_cache.write_bytes(content)
            return p_cache
    except Exception:
        return None



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


Book = KhasiBook


def _load_index() -> List[Dict[str, Any]]:
    global _BOOKS_INDEX_CACHE
    if _BOOKS_INDEX_CACHE is None:
        if _INDEX_PATH.exists():
            with open(_INDEX_PATH, "r", encoding="utf-8") as f:
                raw = json.load(f)
                if isinstance(raw, dict) and "books" in raw:
                    _BOOKS_INDEX_CACHE = raw["books"]
                elif isinstance(raw, list):
                    _BOOKS_INDEX_CACHE = raw
                else:
                    _BOOKS_INDEX_CACHE = []
        else:
            _BOOKS_INDEX_CACHE = []
    return _BOOKS_INDEX_CACHE


def list_books() -> List[Dict[str, Any]]:
    """Return summary metadata for all 714 digitized books in the library."""
    return list(_load_index())


def get_book(id_or_title: str, auto_download: bool = True) -> Optional[KhasiBook]:
    """Retrieve a Khasi book by slug ID or matching title.
    
    Loads and caches the full book content including all individual pages.
    If the book is not yet present locally, it is automatically fetched
    from the official GitHub repository and cached for offline use.
    """
    key = id_or_title.strip().lower()
    key_slug = key.replace(" ", "_").replace("-", "_")

    # Check cache (prefer canonical slug ID match)
    if key_slug in _BOOK_CACHE:
        return _BOOK_CACHE[key_slug]
    if key in _BOOK_CACHE:
        return _BOOK_CACHE[key]

    # Resolve filename
    idx = _load_index()
    matched_id: Optional[str] = None

    # Priority 1: Exact id match
    key_slug = key.replace(" ", "_").replace("-", "_")
    for item in idx:
        if item["id"].lower() in (key, key_slug):
            matched_id = item["id"]
            break

    # Priority 2: Exact title or native_title match
    if not matched_id:
        for item in idx:
            if item["title"].lower() == key or item.get("native_title", "").lower() == key:
                matched_id = item["id"]
                break

    # Priority 3: Substring title or native_title match
    if not matched_id:
        for item in idx:
            if key in item["title"].lower() or key in item.get("native_title", "").lower():
                matched_id = item["id"]
                break

    if not matched_id:
        # Check direct filename
        cand = _BOOKS_DATA_DIR / f"{key}.json"
        if cand.exists():
            matched_id = key

    if not matched_id:
        return None

    # Load book file from local package data, user cache, or GitHub
    book_file = _resolve_book_path(matched_id, auto_download=auto_download)
    if not book_file or not book_file.exists():
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
    _BOOK_CACHE[key] = book
    title_key = book.title.lower()
    if title_key not in _BOOK_CACHE:
        _BOOK_CACHE[title_key] = book
    return book


def download_book(id_or_title: str) -> Optional[KhasiBook]:
    """Download and cache a Khasi book from the official GitHub repository for offline access."""
    return get_book(id_or_title, auto_download=True)


def download_all_books(max_workers: int = 5, verbose: bool = True) -> int:
    """Download and cache all 2,598 digitized books from GitHub repository for full offline access.
    
    Args:
        max_workers: Number of concurrent download threads
        verbose: Print download progress
        
    Returns:
        Total count of successfully cached books.
    """
    idx = _load_index()
    total = len(idx)
    succeeded = 0

    def _fetch(item):
        bid = item["id"]
        res = _resolve_book_path(bid, auto_download=True)
        return bid, res is not None

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(_fetch, item): item for item in idx}
        for i, fut in enumerate(as_completed(futures), 1):
            bid, ok = fut.result()
            if ok:
                succeeded += 1
            if verbose and (i % 100 == 0 or i == total):
                print(f"[khasi] Downloaded and cached {succeeded}/{i} books ({i*100//total}%)...")

    return succeeded


def search_books(query: str, max_results_per_book: int = 5) -> List[Dict[str, Any]]:
    """Perform full-text search across locally available books and catalog metadata.
    
    Args:
        query: Search string (e.g. 'u hynniewtrep', 'ka hok', 'sohpetbneng')
        max_results_per_book: Max page hits to return per matching book
        
    Returns:
        List of matching page hits with snippet, book title, author, and page number.
    """
    results = []
    idx = _load_index()
    q_lower = query.lower()

    for item in idx:
        bid = item["id"]
        book_path = _resolve_book_path(bid, auto_download=False)
        if book_path and book_path.exists():
            b = get_book(bid, auto_download=False)
            if b:
                book_hits = b.search(query)
                if book_hits:
                    results.extend(book_hits[:max_results_per_book])
        else:
            if (q_lower in item.get("title", "").lower() or 
                q_lower in item.get("native_title", "").lower() or
                q_lower in item.get("author", "").lower() or
                q_lower in item.get("description", "").lower()):
                results.append({
                    "book_id": bid,
                    "title": item.get("title", ""),
                    "author": item.get("author", ""),
                    "page_number": 1,
                    "match_count": 1,
                    "snippet": item.get("description", f"Catalog match: {item.get('title')}")[:120]
                })
    return results


def get_book_full_text(id_or_title: str) -> Optional[str]:
    """Return the entire concatenated text of a book across all pages without page navigation."""
    b = get_book(id_or_title)
    if b:
        return b.full_text
    return None


def get_master_compendium_path() -> Path:
    """Return Path to the single consolidated plain-text compendium containing all digitized books."""
    workspace_root = Path(__file__).resolve().parent.parent.parent
    return workspace_root / "data" / "all_khasi_books_master_text.txt"


def get_master_jsonl_path() -> Path:
    """Return Path to the single consolidated JSONL dataset containing all books with full text."""
    workspace_root = Path(__file__).resolve().parent.parent.parent
    return workspace_root / "data" / "all_khasi_books_full_text.jsonl"


def get_pure_khasi_master_text_path() -> Path:
    """Return Path to single document with ALL books strictly in Khasi language (no English/Garo/translations)."""
    workspace_root = Path(__file__).resolve().parent.parent.parent
    return workspace_root / "data" / "pure_khasi_books_master_text.txt"


def get_pure_khasi_master_jsonl_path() -> Path:
    """Return Path to JSONL dataset of ALL books strictly in Khasi language with full text."""
    workspace_root = Path(__file__).resolve().parent.parent.parent
    return workspace_root / "data" / "pure_khasi_books_full_text.jsonl"


def total_books() -> int:
    """Return the total number of whole digitized books available (1,233)."""
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

    def get(self, id_or_title: str, auto_download: bool = True) -> Optional[KhasiBook]:
        """Get full book instance by ID or title (auto-downloads if needed)."""
        return get_book(id_or_title, auto_download=auto_download)

    def download(self, id_or_title: str) -> Optional[KhasiBook]:
        """Explicitly download and cache a book from GitHub."""
        return download_book(id_or_title)

    def download_all(self, max_workers: int = 5, verbose: bool = True) -> int:
        """Download and cache all 2,598 digitized books from GitHub."""
        return download_all_books(max_workers=max_workers, verbose=verbose)

    def read(self, id_or_title: str, page_number: int = 1) -> Optional[str]:
        """Read specific page text from a book."""
        b = get_book(id_or_title)
        if b:
            return b.get_page(page_number)
        return None

    def read_full(self, id_or_title: str) -> Optional[str]:
        """Read the entire unpaginated continuous text of a book."""
        return get_book_full_text(id_or_title)

    @property
    def master_text_file(self) -> Path:
        """Path to single document containing all books with complete content."""
        return get_master_compendium_path()

    @property
    def master_jsonl_file(self) -> Path:
        """Path to line-delimited JSON with each book's full content."""
        return get_master_jsonl_path()

    @property
    def pure_khasi_text_file(self) -> Path:
        """Path to single document containing only books in Khasi language (no English/translations)."""
        return get_pure_khasi_master_text_path()

    @property
    def pure_khasi_jsonl_file(self) -> Path:
        """Path to JSONL containing only books in Khasi language (no English/translations)."""
        return get_pure_khasi_master_jsonl_path()


    def search(self, query: str, max_results_per_book: int = 5) -> List[Dict[str, Any]]:
        """Search query across all books and all pages."""
        return search_books(query, max_results_per_book)

    def summary(self) -> Dict[str, Any]:
        """Return statistical overview of the digitized book preservation library."""
        idx = _load_index()
        authors = {}
        genres = {}
        for b in idx:
            raw_a = b.get("author", "Unknown")
            a = ", ".join(raw_a) if isinstance(raw_a, list) else str(raw_a)
            authors[a] = authors.get(a, 0) + 1
            raw_g = b.get("genre", "General")
            g = ", ".join(raw_g) if isinstance(raw_g, list) else str(raw_g)
            genres[g] = genres.get(g, 0) + 1

        return {
            "total_books": len(idx),
            "total_pages": sum(b.get("total_pages", 0) for b in idx),
            "total_words": sum(b.get("total_words", 0) for b in idx),
            "authors_count": len(authors),
            "genres_count": len(genres),
            "genres": genres,
            "top_authors": sorted(authors.items(), key=lambda x: x[1], reverse=True)[:5]
        }


# Global instance for top-level usage
books = BooksManager()

