# -*- coding: utf-8 -*-
"""
Khasi Traditional Songs, Phawar & Ballads Preservation Module (khasi.songs).
============================================================================

Provides direct access to 10 foundational Khasi folk songs, chants, archery
phawar, epic ballads, and H.W. Sten's celebrated *Ki Sur Na Ka Duitara Ksiar*
with full Khasi lyrics, English translations, musical instrumentation, and
indigenous glossaries.

Usage:
------
>>> import khasi.songs as ks
>>> song = ks.get_song("ka_sur_u_sier_lapalang")
>>> print(song.lyrics_khasi)
>>> print(song.lyrics_english)
>>> results = ks.search_songs("duitara")
"""

from ..culture.songs import (
    songs,
    Song,
    list_songs,
    get_song,
    search_songs,
    songs_by_category,
    total_songs,
    SongManager,
)

all = list_songs
get = get_song
search = search_songs
by_category = songs_by_category
summary = songs.summary

__all__ = [
    "songs",
    "Song",
    "list_songs",
    "get_song",
    "all",
    "get",
    "search",
    "by_category",
    "summary",
    "search_songs",
    "songs_by_category",
    "total_songs",
    "SongManager",
]
