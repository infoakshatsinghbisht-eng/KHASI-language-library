# -*- coding: utf-8 -*-
"""
Khasi Traditional Songs, Phawar & Ballads Preservation Module (Ka Thiar Jingrwai Khasi).
========================================================================================

Provides structured access to 10 foundational Khasi folk songs, chants, phawar,
epic ballads, and literary song cycles (including H.W. Sten's celebrated
*Ki Sur Na Ka Duitara Ksiar*), complete with full Khasi lyrics, English
translations, musical instrumentation, cultural context, and indigenous glossaries.

Key Features:
- Complete Khasi lyrics and stanza-by-stanza translations
- Multi-field and cross-song lyrics search (`song.search(...)` / `search_songs(...)`)
- Musical instrumentation catalog (Duitara, Tangmuri, Ksing, Maryngod, Sharati, etc.)
- Rich cultural metadata, themes, and linguistic vocabulary
- High-level object model (`songs["ka_sur_u_sier_lapalang"]` or `get_song("lapalang")`)
"""

import json
import re
from pathlib import Path
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any

_SONGS_DATA_DIR = Path(__file__).resolve().parent / "data" / "songs"
_INDEX_PATH = _SONGS_DATA_DIR / "songs_index.json"

_SONGS_INDEX_CACHE: Optional[List[Dict[str, Any]]] = None
_SONG_CACHE: Dict[str, "Song"] = {}


@dataclass
class Song:
    """Represents a complete Khasi folk song, phawar chant, or bardic ballad."""
    id: str
    title: str
    khasi_title: str
    category: str
    composer: str
    year: Any
    cultural_context: str
    instruments: List[str]
    themes: List[str]
    lyrics_khasi: str = field(repr=False)
    lyrics_english: str = field(repr=False)
    stanzas: List[Dict[str, Any]]
    vocabulary: Dict[str, str]
    word_count: int

    def __getitem__(self, item: str) -> Any:
        if hasattr(self, item):
            return getattr(self, item)
        raise KeyError(item)

    def __contains__(self, item: str) -> bool:
        return hasattr(self, item)

    def get(self, item: str, default: Any = None) -> Any:
        return getattr(self, item, default)

    def search(self, query: str, case_sensitive: bool = False) -> List[Dict[str, Any]]:
        """Search for a word or phrase within this song's lyrics.
        
        Returns:
            List of match dictionaries containing language, match count, and snippet.
        """
        results = []
        q_target = query if case_sensitive else query.lower()

        # Search Khasi lyrics
        t_kha = self.lyrics_khasi if case_sensitive else self.lyrics_khasi.lower()
        if q_target in t_kha:
            matches = list(re.finditer(re.escape(q_target), t_kha))
            first_m = matches[0]
            start = max(0, first_m.start() - 50)
            end = min(len(self.lyrics_khasi), first_m.end() + 50)
            snippet = self.lyrics_khasi[start:end].strip()
            if start > 0:
                snippet = "..." + snippet
            if end < len(self.lyrics_khasi):
                snippet = snippet + "..."
            results.append({
                "language": "khasi",
                "match_count": len(matches),
                "snippet": snippet
            })

        # Search English translation
        t_en = self.lyrics_english if case_sensitive else self.lyrics_english.lower()
        if q_target in t_en:
            matches = list(re.finditer(re.escape(q_target), t_en))
            first_m = matches[0]
            start = max(0, first_m.start() - 50)
            end = min(len(self.lyrics_english), first_m.end() + 50)
            snippet = self.lyrics_english[start:end].strip()
            if start > 0:
                snippet = "..." + snippet
            if end < len(self.lyrics_english):
                snippet = snippet + "..."
            results.append({
                "language": "english",
                "match_count": len(matches),
                "snippet": snippet
            })

        return results

    def read(self) -> str:
        """Return the complete Khasi lyrics."""
        return self.lyrics_khasi


def _load_index() -> List[Dict[str, Any]]:
    global _SONGS_INDEX_CACHE
    if _SONGS_INDEX_CACHE is not None:
        return _SONGS_INDEX_CACHE

    if not _INDEX_PATH.exists():
        return []

    try:
        with open(_INDEX_PATH, "r", encoding="utf-8") as f:
            _SONGS_INDEX_CACHE = json.load(f)
    except Exception:
        _SONGS_INDEX_CACHE = []

    return _SONGS_INDEX_CACHE


def list_songs() -> List[Dict[str, Any]]:
    """Return index metadata for all available Khasi songs and phawar chants."""
    return _load_index()


def total_songs() -> int:
    """Return total number of structured songs available in the library."""
    return len(_load_index())


def get_song(id_or_title: str) -> Optional[Song]:
    """Retrieve a complete Song instance by its ID or approximate title."""
    if not id_or_title:
        return None

    norm = id_or_title.strip().lower()

    if norm in _SONG_CACHE:
        return _SONG_CACHE[norm]

    index = _load_index()
    matched_entry = None

    # Exact ID match
    for entry in index:
        if entry["id"].lower() == norm:
            matched_entry = entry
            break

    # Substring / title match
    if not matched_entry:
        for entry in index:
            if (norm in entry["id"].lower() or
                norm in entry["title"].lower() or
                norm in entry["khasi_title"].lower()):
                matched_entry = entry
                break

    if not matched_entry:
        return None

    # Load song JSON
    song_file = _SONGS_DATA_DIR / matched_entry["file"]
    if not song_file.exists():
        return None

    try:
        with open(song_file, "r", encoding="utf-8") as f:
            raw = json.load(f)

        song_obj = Song(
            id=raw["id"],
            title=raw["title"],
            khasi_title=raw["khasi_title"],
            category=raw["category"],
            composer=raw.get("composer", "Oral Tradition"),
            year=raw.get("year", "Traditional"),
            cultural_context=raw.get("cultural_context", ""),
            instruments=raw.get("instruments", []),
            themes=raw.get("themes", []),
            lyrics_khasi=raw.get("lyrics_khasi", ""),
            lyrics_english=raw.get("lyrics_english", ""),
            stanzas=raw.get("stanzas", []),
            vocabulary=raw.get("vocabulary", {}),
            word_count=raw.get("word_count", 0)
        )

        _SONG_CACHE[norm] = song_obj
        _SONG_CACHE[song_obj.id] = song_obj
        return song_obj

    except Exception:
        return None


def search_songs(query: str, case_sensitive: bool = False) -> List[Dict[str, Any]]:
    """Search for a keyword across all Khasi songs and translations.
    
    Returns:
        List of results with song metadata and snippet matches.
    """
    results = []
    index = _load_index()

    for entry in index:
        song = get_song(entry["id"])
        if not song:
            continue
        matches = song.search(query, case_sensitive=case_sensitive)
        if matches:
            results.append({
                "song_id": song.id,
                "title": song.title,
                "khasi_title": song.khasi_title,
                "category": song.category,
                "matches": matches
            })

    return results


def songs_by_category(category: str) -> List[Song]:
    """Return all songs matching a given category (e.g. 'Phawar', 'Ballad', 'Lullaby')."""
    cat_norm = category.lower().strip()
    matched = []
    for entry in _load_index():
        if cat_norm in entry["category"].lower():
            s = get_song(entry["id"])
            if s:
                matched.append(s)
    return matched


class SongManager:
    """Convenience collection manager for Khasi songs."""

    def list(self) -> List[Dict[str, Any]]:
        """List metadata for all songs."""
        return list_songs()

    def all(self) -> List[Dict[str, Any]]:
        """List metadata for all songs (alias for list)."""
        return list_songs()

    def get(self, id_or_title: str) -> Optional[Song]:
        """Retrieve full Song object by ID or title."""
        return get_song(id_or_title)

    def search(self, query: str, case_sensitive: bool = False) -> List[Dict[str, Any]]:
        """Search across all songs."""
        return search_songs(query, case_sensitive=case_sensitive)

    def by_category(self, category: str) -> List[Song]:
        """Filter songs by category."""
        return songs_by_category(category)

    def summary(self) -> Dict[str, Any]:
        """Return statistical overview of the songs and phawar collection."""
        idx = _load_index()
        categories = {}
        for s in idx:
            c = s.get("category", "General")
            categories[c] = categories.get(c, 0) + 1

        return {
            "total_songs": len(idx),
            "categories_count": len(categories),
            "categories": categories,
            "total_words": sum(s.get("word_count", 0) for s in idx)
        }

    def __len__(self) -> int:
        return total_songs()

    def __iter__(self):
        for entry in list_songs():
            s = get_song(entry["id"])
            if s:
                yield s

    def __getitem__(self, item: str) -> Song:
        s = get_song(item)
        if s is None:
            raise KeyError(f"Song '{item}' not found in Khasi song library.")
        return s


# Global singleton instance
songs = SongManager()

