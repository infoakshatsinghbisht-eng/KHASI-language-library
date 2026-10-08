# -*- coding: utf-8 -*-
"""
Khasi Folklore, Myths & Oral Legends Preservation Module (khasi.folklore).
===========================================================================

Provides direct access to 12 foundational Khasi oral myths, legends, fables,
and allegories (over 6,950+ words of authentic Khasi prose and poetry) with
section-by-section narratives, English translations, character registries,
cultural morals, and linguistic glossaries.

Usage:
------
>>> import khasi.folklore as kf
>>> kf.folklore.summary()
>>> story = kf.get_story("ka_jingkieng_ksier")
>>> print(story.khasi_text)
>>> print(story.english_translation)
>>> results = kf.search_folklore("u thlen")
"""

from ..culture.folklore import (
    folklore,
    FolkloreStory,
    list_stories,
    get_story,
    search_folklore,
    stories_by_category,
    total_stories,
    FolkloreManager,
)

all = list_stories
get = get_story
search = search_folklore
by_category = stories_by_category
summary = folklore.summary

__all__ = [
    "folklore",
    "FolkloreStory",
    "list_stories",
    "get_story",
    "all",
    "get",
    "search",
    "by_category",
    "summary",
    "search_folklore",
    "stories_by_category",
    "total_stories",
    "FolkloreManager",
]
