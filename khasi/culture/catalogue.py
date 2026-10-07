# -*- coding: utf-8 -*-
"""Khasi Master Bibliography Catalogue (200+ Books & Works across 8 Genres)."""

import json
from pathlib import Path
from typing import Dict, List, Any, Optional

_CATALOGUE_PATH = Path(__file__).parent / "data" / "khasi_bibliography_catalogue.json"
_CATALOGUE_CACHE: Optional[List[Dict[str, Any]]] = None

def _load_catalogue() -> List[Dict[str, Any]]:
    global _CATALOGUE_CACHE
    if _CATALOGUE_CACHE is None:
        if _CATALOGUE_PATH.exists():
            with open(_CATALOGUE_PATH, "r", encoding="utf-8") as f:
                _CATALOGUE_CACHE = json.load(f)
        else:
            _CATALOGUE_CACHE = []
    return _CATALOGUE_CACHE

def all_works() -> List[Dict[str, Any]]:
    """Return all 204 catalogued Khasi literary, historical, linguistic, and cultural works."""
    return list(_load_catalogue())

def by_genre(genre: str) -> List[Dict[str, Any]]:
    """Filter works by genre (e.g. 'Original Khasi literature', 'Khasi history/culture', 'Khasi grammar/linguistics', 'Khasi dictionaries', etc.)."""
    g_lower = genre.lower()
    return [w for w in _load_catalogue() if g_lower in w.get("genre", "").lower()]

def by_author(author: str) -> List[Dict[str, Any]]:
    """Filter works by author name (case-insensitive substring match)."""
    a_lower = author.lower()
    return [w for w in _load_catalogue() if a_lower in w.get("author", "").lower()]

def by_type(work_type: str) -> List[Dict[str, Any]]:
    """Filter works by format/type (e.g. 'Novel', 'Poetry', 'Drama', 'Dictionary', 'Grammar')."""
    t_lower = work_type.lower()
    return [w for w in _load_catalogue() if t_lower in w.get("type", "").lower()]

def search_works(query: str) -> List[Dict[str, Any]]:
    """Search works by title, author, genre, or notes."""
    q_lower = query.lower()
    results = []
    for w in _load_catalogue():
        if (q_lower in w.get("title", "").lower() or
            q_lower in w.get("author", "").lower() or
            q_lower in w.get("genre", "").lower() or
            q_lower in w.get("type", "").lower()):
            results.append(w)
    return results

def get_digitized_works() -> List[Dict[str, Any]]:
    """Return all works that are known to be digitized / scanned."""
    return [w for w in _load_catalogue() if w.get("digitized") is True]

def summary() -> Dict[str, Any]:
    """Return statistical summary of the catalogue."""
    cat = _load_catalogue()
    genres: Dict[str, int] = {}
    types: Dict[str, int] = {}
    authors_count: Dict[str, int] = {}
    digitized_count = 0
    for w in cat:
        g = w.get("genre", "Unknown")
        genres[g] = genres.get(g, 0) + 1
        t = w.get("type", "Unknown")
        types[t] = types.get(t, 0) + 1
        a = w.get("author", "Unknown")
        authors_count[a] = authors_count.get(a, 0) + 1
        if w.get("digitized"):
            digitized_count += 1
    return {
        "total_works": len(cat),
        "genres": genres,
        "types": types,
        "top_authors": sorted(authors_count.items(), key=lambda x: x[1], reverse=True)[:10],
        "digitized_works_count": digitized_count,
    }

class BibliographyCatalogue:
    """Object-oriented interface for the Khasi bibliography catalogue."""
    def __init__(self):
        self._items = _load_catalogue()

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def all(self) -> List[Dict[str, Any]]:
        return all_works()

    def by_genre(self, genre: str) -> List[Dict[str, Any]]:
        return by_genre(genre)

    def by_author(self, author: str) -> List[Dict[str, Any]]:
        return by_author(author)

    def by_type(self, work_type: str) -> List[Dict[str, Any]]:
        return by_type(work_type)

    def search(self, query: str) -> List[Dict[str, Any]]:
        return search_works(query)

    def digitized(self) -> List[Dict[str, Any]]:
        return get_digitized_works()

    def summary(self) -> Dict[str, Any]:
        return summary()
