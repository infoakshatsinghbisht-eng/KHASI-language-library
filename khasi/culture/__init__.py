# -*- coding: utf-8 -*-
"""Khasi Culture, Heritage, Calendar, Literature, Music, Botany, Wildlife, Cuisine, Geography & Festivals Package."""

from .calendar import (
    KHASI_MONTHS,
    KHASI_SEASONS,
    KHASI_DAYS,
    MARKET_CYCLE,
    get_current_season,
    get_current_khasi_month,
    get_market_day,
)
from .festivals import (
    KHASI_FESTIVALS,
    list_festivals,
    get_festival,
)
from .literature import (
    AUTHORS,
    EPICS,
    POEMS,
    authors,
    epics,
    poems,
    get_author,
    get_epic,
    search_literature,
)
from .kinship import (
    list_kinship_terms,
    get_kinship_info,
    search_kinship,
    describe_matrilineal_system,
)
from .catalogue import (
    BibliographyCatalogue,
    all_works,
    by_genre,
    by_author,
    by_type,
    search_works,
    get_digitized_works,
    summary as catalogue_summary,
)
from .music import (
    INSTRUMENTS,
    FOLK_SONGS,
    MUSICIANS,
    list_instruments,
    get_instrument,
    list_songs,
    get_song,
    list_musicians,
)
from .botany import (
    PLANTS,
    list_plants,
    get_plant,
    by_plant_type,
    medicinal_plants,
)
from .wildlife import (
    WILDLIFE,
    list_wildlife,
    get_animal,
    by_class as by_wildlife_class,
)
from .cuisine import (
    DISHES,
    list_dishes,
    get_dish,
    by_category as by_cuisine_category,
)
from .geography import (
    GEOGRAPHY,
    list_places,
    get_place,
    by_type as by_geography_type,
)
from .clans import (
    CLANS,
    list_clans,
    get_clan,
    search_clans,
)
from .idioms import (
    IDIOMS,
    list_idioms,
    get_idiom,
)
from .rituals import (
    RITUALS,
    list_rituals,
    get_ritual,
    rituals_by_category,
)
from .deities import (
    DEITIES,
    list_deities,
    get_deity,
    deities_by_realm,
)
from .sacred_sites import (
    SACRED_SITES,
    list_sacred_sites,
    get_sacred_site,
    sites_by_type,
)
from .books import (
    books,
    KhasiBook,
    BookPage,
    list_books,
    get_book,
    search_books,
    total_books,
    total_pages,
    total_words,
)

catalogue = BibliographyCatalogue()

__all__ = [
    # Calendar & Astronomy
    "KHASI_MONTHS",
    "KHASI_SEASONS",
    "KHASI_DAYS",
    "MARKET_CYCLE",
    "get_current_season",
    "get_current_khasi_month",
    "get_market_day",
    # Festivals
    "KHASI_FESTIVALS",
    "list_festivals",
    "get_festival",
    # Literature, Poetry & Folklore
    "AUTHORS",
    "EPICS",
    "POEMS",
    "authors",
    "epics",
    "poems",
    "get_author",
    "get_epic",
    "search_literature",
    # Kinship & Social Order
    "list_kinship_terms",
    "get_kinship_info",
    "search_kinship",
    "describe_matrilineal_system",
    # Master Bibliography Catalogue
    "BibliographyCatalogue",
    "catalogue",
    "all_works",
    "by_genre",
    "by_author",
    "by_type",
    "search_works",
    "get_digitized_works",
    "catalogue_summary",
    # Music & Instruments (NEW)
    "INSTRUMENTS",
    "FOLK_SONGS",
    "MUSICIANS",
    "list_instruments",
    "get_instrument",
    "list_songs",
    "get_song",
    "list_musicians",
    # Botany & Ethnomedicine (NEW)
    "PLANTS",
    "list_plants",
    "get_plant",
    "by_plant_type",
    "medicinal_plants",
    # Wildlife & Zoology (NEW)
    "WILDLIFE",
    "list_wildlife",
    "get_animal",
    "by_wildlife_class",
    # Cuisine & Food Heritage (NEW)
    "DISHES",
    "list_dishes",
    "get_dish",
    "by_cuisine_category",
    # Geography & Sacred Sites (NEW)
    "GEOGRAPHY",
    "list_places",
    "get_place",
    "by_geography_type",
    # Clans & Surnames (NEW)
    "CLANS",
    "list_clans",
    "get_clan",
    "search_clans",
    # Idioms & Ktien Kynnoh (NEW)
    "IDIOMS",
    "list_idioms",
    "get_idiom",
    # Rituals & Ceremonies (NEW)
    "RITUALS",
    "list_rituals",
    "get_ritual",
    "rituals_by_category",
    # Deities & Pantheon (NEW)
    "DEITIES",
    "list_deities",
    "get_deity",
    "deities_by_realm",
    # Sacred Sites & Megaliths (NEW)
    "SACRED_SITES",
    "list_sacred_sites",
    "get_sacred_site",
    "sites_by_type",
    # Digitized Whole Books & Preservation (NEW)
    "books",
    "KhasiBook",
    "BookPage",
    "list_books",
    "get_book",
    "search_books",
    "total_books",
    "total_pages",
    "total_words",
]
