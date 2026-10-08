# -*- coding: utf-8 -*-
"""Khasi Matrilineal Kinship System (Kur and Kha)."""

from typing import Dict, List, Any, Optional
from ..constants import KINSHIP, MORAL_PILLARS

def list_kinship_terms() -> Dict[str, str]:
    """Return dictionary of matrilineal kinship titles and roles."""
    return KINSHIP

def get_kinship_info(term: str) -> Optional[str]:
    """Lookup explanation of a Khasi kinship term."""
    clean = term.strip().capitalize()
    if clean in KINSHIP:
        return KINSHIP[clean]
    # Check case-insensitive match
    lower = term.strip().lower()
    for k, v in KINSHIP.items():
        if k.lower() == lower:
            return v
    return None

def search_kinship(query: str) -> Dict[str, str]:
    """Search kinship terms matching query in Khasi title or English description."""
    q = query.lower().strip()
    return {k: v for k, v in KINSHIP.items() if q in k.lower() or q in v.lower()}

def describe_matrilineal_system() -> Dict[str, Any]:
    """Overview of Khasi matrilineal social structure and principles."""
    return {
        "system": "Matrilineal & Matrilocal Clan Organization",
        "pillars": MORAL_PILLARS,
        "ancestral_roots": {
            "Ka_Iawbei": "The primal ancestral mother from whom the Kur (clan) traces descent.",
            "U_Thawlang": "The first paternal ancestor who married Ka Iawbei.",
            "U_Suidnia": "The first maternal uncle who acted as high priest and counselor."
        },
        "inheritance_rule": "Ultimogeniture — Ancestral property ('ïing-sad') is inherited by the youngest daughter ('Ka Khadduh').",
        "clan_exogamy": "Strict prohibition against marrying within one's maternal clan (Kur), considered the gravest moral taboo ('Sang').",
        "lineage_divisions": {
            "Kur": "The entire maternal clan tracing descent from Ka Ïawbei.",
            "Kpoh": "Sub-clan branch descending from a common grandmother.",
            "Shi-ïing": "Nuclear / extended family sharing one household hearth.",
            "Kha": "Paternal relations from the father's clan line."
        },
        "key_customs": {
            "Naming ('Kur-kjat')": "Traditional ceremony where clan elders bless and name a newborn infant.",
            "Marriage ('Poikha')": "Matrilocal union; the groom resides in the bride's ancestral house.",
            "Bone Interment ('Thep Mawbah')": "Solemn ritual depositing ancestral bones in the clan megalithic ossuary."
        }
    }
