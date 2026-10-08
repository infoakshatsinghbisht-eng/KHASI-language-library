# -*- coding: utf-8 -*-
"""
Khasi Matrilineal Clans (Ki Kur & Ki Jaid), Lineage Systems & Surnames.
Comprehensive registry of recognized Khasi and Pnar clans, ancestral maternal roots (Ka Ïawbei),
and exogamous kinship rules of Meghalaya.
"""

from typing import Dict, List, Any, Optional

CLANS: List[Dict[str, Any]] = [
    {
        "clan_name": "Syiem (Jaid Syiem)",
        "branches": ["Syiemlieh", "Syiemiong", "Khriem", "Nongkhlaw", "Sohra", "Maharam"],
        "category": "Royal / Ruling Clan",
        "historical_role": "Hereditary constitutional chiefs and rulers of Khasi states (Ki Hima); trace descent from the mythological ancestress Ka Pahsyntiew or Ka Lieng Makaw."
    },
    {
        "clan_name": "Lyngdoh",
        "branches": ["Lyngdoh Nonglait", "Lyngdoh Mawphlang", "Lyngdoh Marshillong", "Lyngdoh Nongbri"],
        "category": "Priestly / Administrative Clan",
        "historical_role": "Traditional high priests and prime ministerial ministers; custodians of sacred groves, state sacrifices, and customary religious ceremonies."
    },
    {
        "clan_name": "Nongrum",
        "branches": ["Nongrum", "Roy Nongrum"],
        "category": "Foundational Highland Clan",
        "historical_role": "Prominent highland clan; produced illustrious authors, novelists (K.W. Nongrum), and traditional civic leaders."
    },
    {
        "clan_name": "Wahlang",
        "branches": ["Wahlang", "Kerios Wahlang"],
        "category": "Highland Clan",
        "historical_role": "Ancient clan rooted in the valleys and central ridges; produced revered musicians, folk balladeers, and community elders."
    },
    {
        "clan_name": "Kharbangar",
        "branches": ["Kharbangar", "Tipriti Kharbangar"],
        "category": "Traditional Clan",
        "historical_role": "Prominent clan bearing the traditional 'Khar-' prefix (historically denoting trade and settlement connections); celebrated in culture and the arts."
    },
    {
        "clan_name": "Dkhar (Jaid Dkhar)",
        "branches": ["Dkhar", "Streamlet Dkhar"],
        "category": "Assimilated Matrilineal Lineage",
        "historical_role": "Lineages founded by ancestral mothers of diverse origins who were ceremonially adopted and fully integrated into the matrilineal Khasi Kur system."
    },
    {
        "clan_name": "Rymbai",
        "branches": ["Rymbai"],
        "category": "Pnar / Jaiñtia Clan",
        "historical_role": "Distinguished Pnar clan holding hereditary administrative and judicial offices in the historic Jaintia Kingdom."
    },
    {
        "clan_name": "Khongwir",
        "branches": ["Khongwir"],
        "category": "Shella / Southern Escarpment Clan",
        "historical_role": "Ancient clan from the southern War Khasi region, famed for horticulture, orange groves, and village confederacies."
    },
    {
        "clan_name": "Kharlukhi",
        "branches": ["Kharlukhi", "K.K. Kharlukhi"],
        "category": "Traditional Clan",
        "historical_role": "Prominent clan that contributed pioneering novelists, playwrights, and public educators."
    },
    {
        "clan_name": "Laloo",
        "branches": ["Laloo", "Donbok T. Laloo", "Minimon Laloo"],
        "category": "Pnar & Khasi Clan",
        "historical_role": "Distinguished clan spanning Jowai and Shillong; produced legendary folklorists, ethnographers, and writers."
    },
    {
        "clan_name": "Tham",
        "branches": ["Tham", "Soso Tham"],
        "category": "Highland Clan",
        "historical_role": "Venerated clan of Sohra that gave birth to U Soso Tham, the revered national poet and literary architect of the Khasi language."
    },
    {
        "clan_name": "Shullai",
        "branches": ["Shullai", "L.G. Shullai"],
        "category": "Pnar & Khasi Clan",
        "historical_role": "Eminent family of scholars, political chroniclers, and constitutional archivists of Meghalaya."
    },
    {
        "clan_name": "Pariat",
        "branches": ["Pariat"],
        "category": "Jaiñtia Clan",
        "historical_role": "Historic Jaintia clan associated with governance, regional trade, and village councils."
    },
    {
        "clan_name": "Sutnga",
        "branches": ["Sutnga"],
        "category": "Ancient Royal Lineage of Jaintia",
        "historical_role": "The ancestral royal house of the Jaintia Kings (Syiem Sutnga); associated with the legend of Ka Matsieng."
    },
    {
        "clan_name": "Marbaniang",
        "branches": ["Marbaniang"],
        "category": "Central Khasi Clan",
        "historical_role": "Highland clan known for statecraft, civil service, and leadership in the Dorbar councils."
    },
    {
        "clan_name": "Khongdup",
        "branches": ["Khongdup", "D.S. Khongdup"],
        "category": "War Khasi Clan",
        "historical_role": "Southern slope clan; produced notable poets, educational writers, and linguists."
    },
    {
        "clan_name": "Nongkynrih",
        "branches": ["Nongkynrih", "K.S. Nongkynrih"],
        "category": "Highland Clan",
        "historical_role": "Distinguished lineage that produced internationally recognized novelists, poets, and academic anthologists."
    },
    {
        "clan_name": "Warjri",
        "branches": ["Warjri", "Hughlet Warjri"],
        "category": "Central Khasi Clan",
        "historical_role": "Influential clan active in journalism, civic policy, and educational institutions."
    },
    {
        "clan_name": "Mawlong",
        "branches": ["Mawlong"],
        "category": "Sohra & Southern Clan",
        "historical_role": "Ancient clan connected to market stewardship, lime trading, and regional councils."
    },
    {
        "clan_name": "Basaiawmoit",
        "branches": ["Basaiawmoit"],
        "category": "Highland Clan",
        "historical_role": "Respected clan active in community leadership, educational foundations, and church scholarship."
    },
    {
        "clan_name": "Diengdoh",
        "branches": ["Diengdoh"],
        "category": "Highland Clan",
        "historical_role": "Historic clan associated with Cherrapunji; produced early scholars, teachers, and civic leaders."
    },
    {
        "clan_name": "Bareh",
        "branches": ["Bareh", "Mondon Bareh", "Victor Bareh", "Hamlet Bareh"],
        "category": "Scholar & Literary Dynasty",
        "historical_role": "Monumental family that shaped 20th-century Khasi drama, lexicography, grammar textbooks, and modern historical scholarship."
    },
    {
        "clan_name": "Swer",
        "branches": ["Swer"],
        "category": "Highland Clan",
        "historical_role": "Ancient clan tracing back to central plateau settlements; prominent in civil administration."
    },
    {
        "clan_name": "Majaw",
        "branches": ["Majaw", "Lou Majaw"],
        "category": "Highland Clan",
        "historical_role": "Creative and artistic clan celebrated in folk and modern musical performance."
    },
    {
        "clan_name": "Kharpuri",
        "branches": ["Kharpuri"],
        "category": "Traditional Clan",
        "historical_role": "Prominent clan active in business, regional trade, and community councils."
    },
    {
        "clan_name": "Nongtdu",
        "branches": ["Nongtdu"],
        "category": "Pnar Clan",
        "historical_role": "Traditional Jaintia clan prominent in local village governance and cultural festivals."
    },
    {
        "clan_name": "Passah",
        "branches": ["Passah"],
        "category": "Pnar Clan",
        "historical_role": "Esteemed family in West Jaintia Hills that produced master musicians, educators, and community leaders."
    },
    {
        "clan_name": "Lamare",
        "branches": ["Lamare"],
        "category": "Pnar & Khasi Clan",
        "historical_role": "Widespread clan celebrated for agricultural stewardship, trade, and public service."
    },
    {
        "clan_name": "Mukhim",
        "branches": ["Mukhim", "Patricia Mukhim"],
        "category": "Highland Clan",
        "historical_role": "Prominent clan that produced pioneering journalists, Padma Shri recipients, and social commentators."
    }
]

def list_clans() -> List[Dict[str, Any]]:
    """Return all catalogued Khasi and Pnar clans."""
    return CLANS

def get_clan(name: str) -> Optional[Dict[str, Any]]:
    """Lookup clan by name or branch."""
    q = name.lower().strip()
    for c in CLANS:
        if q in c["clan_name"].lower() or any(q in b.lower() for b in c["branches"]):
            return c
    return None

def search_clans(query: str) -> List[Dict[str, Any]]:
    """Search clans by keyword in name, branches, category, or historical role."""
    q = query.lower().strip()
    return [c for c in CLANS if (
        q in c["clan_name"].lower() or
        any(q in b.lower() for b in c["branches"]) or
        q in c["category"].lower() or
        q in c["historical_role"].lower()
    )]
