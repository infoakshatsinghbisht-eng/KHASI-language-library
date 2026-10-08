# -*- coding: utf-8 -*-
"""
Khasi Folklore, Myths & Oral Legends Preservation Module (Ka Thiar Parom Khasi).
=================================================================================

Provides direct structured access to 12 foundational Khasi oral myths,
legends, fables, and cultural allegories with full Khasi texts, English
translations, characters, moral tenets, and indigenous glossaries.

Stories Included:
- Ka Jingkieng Ksier (The Golden Ladder & Genesis of the Seven Huts)
- U Diengiei (The Tree of Eclipsing Darkness & Council of Lum Diengiei)
- U Sier Lapalang (The Stately Stag & The Mother's Heartbreaking Lament)
- U Manik Raitong (The Melodies of the Sharati & Tragic Love)
- Ka Nohkalikai (The Leap of Likai & Waterfall of Tears)
- U Bsein Thlen (The Monster Serpent & Slaying at Dainthlen)
- Ka Sngi bad U Bnai (The Sun, the Moon & the Ash of Shame)
- U Klew bad Ka Sngi (The Peacock's Love for the Sun)
- Ka Wah Umïam bad Ka Wah Umngot (The Twin Sister Rivers)
- Ka Krem Lamet Latang (The Primal Council Cave of Animals)
- Ki Mawbynna bad Ki Mawlynti (The Megalithic Monoliths & Ancestors)
- Ka Pansngiat Ksiar Ka Meiramew (The Golden Crown of Mother Earth & Seasons)
"""

import json
import re
from pathlib import Path
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any

_FOLKLORE_DATA_DIR = Path(__file__).resolve().parent / "data" / "folklore"
_INDEX_PATH = _FOLKLORE_DATA_DIR / "folklore_index.json"

_FOLKLORE_INDEX_CACHE: Optional[List[Dict[str, Any]]] = None
_STORY_CACHE: Dict[str, "FolkloreStory"] = {}


@dataclass
class FolkloreStory:
    """Represents a complete Khasi oral legend or mythological narrative."""
    id: str
    title: str
    khasi_title: str
    category: str
    geographic_origin: str
    characters: List[str]
    cultural_moral: str
    khasi_text: str = field(repr=False)
    english_translation: str = field(repr=False)
    sections: List[Dict[str, Any]]
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
        """Search for a keyword or phrase across Khasi text and English translation.
        
        Returns:
            List of matching occurrences with contextual snippets.
        """
        results = []
        q_target = query if case_sensitive else query.lower()

        # Search Khasi text
        t_kha = self.khasi_text if case_sensitive else self.khasi_text.lower()
        if q_target in t_kha:
            matches = list(re.finditer(re.escape(q_target), t_kha))
            first_m = matches[0]
            start = max(0, first_m.start() - 60)
            end = min(len(self.khasi_text), first_m.end() + 60)
            snippet = self.khasi_text[start:end].strip()
            if start > 0:
                snippet = "..." + snippet
            if end < len(self.khasi_text):
                snippet = snippet + "..."
            results.append({
                "language": "khasi",
                "match_count": len(matches),
                "snippet": snippet
            })

        # Search English translation
        t_en = self.english_translation if case_sensitive else self.english_translation.lower()
        if q_target in t_en:
            matches = list(re.finditer(re.escape(q_target), t_en))
            first_m = matches[0]
            start = max(0, first_m.start() - 60)
            end = min(len(self.english_translation), first_m.end() + 60)
            snippet = self.english_translation[start:end].strip()
            if start > 0:
                snippet = "..." + snippet
            if end < len(self.english_translation):
                snippet = snippet + "..."
            results.append({
                "language": "english",
                "match_count": len(matches),
                "snippet": snippet
            })

        return results

    def to_dict(self) -> Dict[str, Any]:
        """Convert story to dictionary representation."""
        return {
            "id": self.id,
            "title": self.title,
            "khasi_title": self.khasi_title,
            "category": self.category,
            "geographic_origin": self.geographic_origin,
            "characters": self.characters,
            "cultural_moral": self.cultural_moral,
            "khasi_text": self.khasi_text,
            "english_translation": self.english_translation,
            "sections": self.sections,
            "vocabulary": self.vocabulary,
            "word_count": self.word_count
        }


def _load_index() -> List[Dict[str, Any]]:
    global _FOLKLORE_INDEX_CACHE
    if _FOLKLORE_INDEX_CACHE is None:
        if _INDEX_PATH.exists():
            with open(_INDEX_PATH, "r", encoding="utf-8") as f:
                _FOLKLORE_INDEX_CACHE = json.load(f)
        else:
            _FOLKLORE_INDEX_CACHE = []
    return _FOLKLORE_INDEX_CACHE


def list_stories() -> List[Dict[str, Any]]:
    """Return summary metadata for all 12 preserved Khasi folktales and myths."""
    return list(_load_index())


def get_story(id_or_title: str) -> Optional[FolkloreStory]:
    """Retrieve a Khasi folklore narrative by slug ID or matching title."""
    key = id_or_title.strip().lower()

    if key in _STORY_CACHE:
        return _STORY_CACHE[key]

    idx = _load_index()
    matched_id: Optional[str] = None

    for item in idx:
        if (item["id"].lower() == key or
            item["title"].lower() == key or
            key in item["title"].lower() or
            key in item.get("khasi_title", "").lower()):
            matched_id = item["id"]
            break

    if not matched_id:
        cand = _FOLKLORE_DATA_DIR / f"{key}.json"
        if cand.exists():
            matched_id = key

    if not matched_id:
        return None

    story_file = _FOLKLORE_DATA_DIR / f"{matched_id}.json"
    if not story_file.exists():
        return None

    with open(story_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    story = FolkloreStory(
        id=data["id"],
        title=data["title"],
        khasi_title=data.get("khasi_title", data["title"]),
        category=data.get("category", "Folktale"),
        geographic_origin=data.get("geographic_origin", "Meghalaya"),
        characters=data.get("characters", []),
        cultural_moral=data.get("cultural_moral", ""),
        khasi_text=data.get("khasi_text", ""),
        english_translation=data.get("english_translation", ""),
        sections=data.get("sections", []),
        vocabulary=data.get("vocabulary", {}),
        word_count=data.get("word_count", 0)
    )

    _STORY_CACHE[matched_id] = story
    _STORY_CACHE[story.title.lower()] = story
    return story


def search_folklore(query: str) -> List[Dict[str, Any]]:
    """Search for keywords across all Khasi folklore stories and translations."""
    results = []
    idx = _load_index()
    for item in idx:
        s = get_story(item["id"])
        if not s:
            continue
        hits = s.search(query)
        if hits:
            results.append({
                "story_id": s.id,
                "title": s.title,
                "category": s.category,
                "matches": hits
            })
    return results


def stories_by_category(category: str) -> List[Dict[str, Any]]:
    """Filter folklore stories by category (e.g. 'Creation Myth', 'Tragic Epic', 'Romance')."""
    c_lower = category.lower()
    return [s for s in _load_index() if c_lower in s.get("category", "").lower()]


def total_stories() -> int:
    """Return the total number of preserved folklore stories (12)."""
    return len(_load_index())


class FolkloreManager:
    """Object-oriented facade for reading, searching, and exploring Khasi folklore."""

    def __len__(self) -> int:
        return total_stories()

    def __iter__(self):
        for s in list_stories():
            yield get_story(s["id"])

    def __getitem__(self, item: str) -> Optional[FolkloreStory]:
        return get_story(item)

    def all(self) -> List[Dict[str, Any]]:
        """List metadata of all stories."""
        return list_stories()

    def get(self, id_or_title: str) -> Optional[FolkloreStory]:
        """Get full FolkloreStory instance by ID or title."""
        return get_story(id_or_title)

    def search(self, query: str) -> List[Dict[str, Any]]:
        """Universal search across all folklore stories and translations."""
        return search_folklore(query)

    def by_category(self, category: str) -> List[Dict[str, Any]]:
        """Filter stories by category."""
        return stories_by_category(category)

    def summary(self) -> Dict[str, Any]:
        """Return statistical overview of the folklore preservation collection."""
        idx = _load_index()
        categories = {}
        for s in idx:
            c = s.get("category", "General")
            categories[c] = categories.get(c, 0) + 1

        return {
            "total_stories": len(idx),
            "categories_count": len(categories),
            "categories": categories,
            "total_words": sum(s.get("word_count", 0) for s in idx)
        }


# Global facade instance
folklore = FolkloreManager()
