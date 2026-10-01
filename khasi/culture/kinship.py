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
    return KINSHIP.get(clean)

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
        "clan_exogamy": "Strict prohibition against marrying within one's maternal clan (Kur), considered the gravest moral taboo ('Sang')."
    }
