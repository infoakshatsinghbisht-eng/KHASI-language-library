# -*- coding: utf-8 -*-
"""
Khasi Sacred Sites, Sacred Groves (Law Kyntang), Megalithic Clusters & Traditional Shrines.
Documented from:
- Archaeological Survey of India (ASI) Meghalaya Circle
- Seng Khasi Heritage Documentation
- District Gazettes & Customary Hima Records
"""

from typing import Dict, List, Any, Optional

SACRED_SITES: List[Dict[str, Any]] = [
    {
        "id": "law_kyntang_mawphlang",
        "name": "Law Kyntang Mawphlang (Mawphlang Sacred Forest)",
        "site_type": "sacred_grove",
        "location": "Mawphlang, East Khasi Hills (25 km from Shillong)",
        "elevation": "1,850 m",
        "presiding_deity": "U Ryngkew U Basa (Labasa), manifested as a protective leopard or snake",
        "historical_age": "800+ years of unbroken customary preservation",
        "significance": "The most celebrated sacred grove in Meghalaya, spanning 192 acres of ancient subtropical broadleaf cloud forest. Preserved under strict customary taboo (Adong): not a single twig, dead leaf, flower, or pebble may be taken out. Houses prehistoric megalithic sacrifice altars (Duwan) where state treaties and clan reconciliations were sealed.",
        "cultural_practices": ["Annual animal thanksgiving sacrifice by the Lyngdoh of Mawphlang", "Coronation ceremonies for traditional council elders"]
    },
    {
        "id": "nartiang_monoliths",
        "name": "Ki Mawbynna Nartiang (Nartiang Megalithic Complex)",
        "site_type": "megalithic_monolith",
        "location": "Nartiang, West Jaiñtia Hills",
        "elevation": "1,380 m",
        "presiding_deity": "U Mar Phalyngki (Legendary Pnar giant and general of the Jaintia King)",
        "historical_age": "Circa 1500–1835 CE (Pre-colonial Jaintia Kingdom era)",
        "significance": "The largest concentration of megaliths in any single site in the world. The towering central menhir (Maw-shynrang) stands over 8.3 meters (27 feet) in height and is almost 1 meter thick. Surrounding female dolmens (Maw-kynthei) measure up to 5 meters in diameter. Commemorates the great royal summer capital of the Jaintia Syiems.",
        "cultural_practices": ["Clan bone commemoration", "National monument protected under the Archaeological Survey of India"]
    },
    {
        "id": "lum_shillong_shrine",
        "name": "Lum Shillong (Throne of U Lei Shyllong)",
        "site_type": "mountain_sanctuary",
        "location": "Shillong Peak, East Khasi Hills",
        "elevation": "1,965 m (highest peak of Khasi Hills)",
        "presiding_deity": "U Lei Shyllong",
        "historical_age": "Ancient indigenous mythological epoch",
        "significance": "The sacred mountain sanctuary where the royal state house of Khyrim and Mylliem communes with U Lei Shyllong. The summit commands views over the entire Khasi plateau down to the plains of Surma in Bangladesh.",
        "cultural_practices": ["State sacrifices (Pomblang) invoking peace, harvest, and realm security"]
    },
    {
        "id": "lum_sohpetbneng",
        "name": "Lum Sohpetbneng (The Navel of Heaven)",
        "site_type": "mythological_sanctuary",
        "location": "Ri-Bhoi District, near Umiam Lake",
        "elevation": "1,343 m",
        "presiding_deity": "U Blei Nongthaw / Ki Hynñiew Trep",
        "historical_age": "Primordial Austroasiatic creation myth",
        "significance": "The holy mountain regarded as the cradle of Khasi civilization. According to sacred oral lore, this peak was the terrestrial anchor of the golden celestial ladder (Jingkieng Ksiar) that allowed humanity to traverse freely between heaven (Khat-hynriew Trep) and earth (Hynñiew Trep).",
        "cultural_practices": ["Annual Seng Khasi spiritual pilgrimage on the first Sunday of February"]
    },
    {
        "id": "aitnar_pool",
        "name": "Ka Aitnar (Sacred Behdeiñkhlam Pool)",
        "site_type": "sacred_water_shrine",
        "location": "Jowai town, West Jaiñtia Hills",
        "elevation": "1,380 m",
        "presiding_deity": "U Blai Synteng / Territorial spirits of Jowai",
        "historical_age": "Pre-colonial Pnar socio-religious tradition",
        "significance": "A consecrated natural mud pool where the climax of the four-day Behdeiñkhlam festival takes place. Hundreds of thousands of Pnar dancers descend into the pool to carry and immerse the monumental wooden tower structures (Rot) and defeat symbolic pestilence.",
        "cultural_practices": ["Ritual mud dancing, immersion of the Khnong and Rot, driving away of plague"]
    },
    {
        "id": "krem_mawmluh_shrine",
        "name": "Krem Mawmluh & Ka Syiem Mawmluh",
        "site_type": "cave_sanctuary",
        "location": "Mawmluh village, Sohra plateau",
        "elevation": "1,290 m",
        "presiding_deity": "Ka Syiem Mawmluh (Goddess of subterranean springs)",
        "historical_age": "Global geological type-locality for the Meghalayan Age (4,200 years BP)",
        "significance": "Sacred labyrinthine cavern revered by Sohra villagers for its crystal pools and calcite formations. Ancient Khasi elders entered its chambers to seek visions and divine underground water flow during extreme droughts.",
        "cultural_practices": ["Customary spring protection rites"]
    },
    {
        "id": "lum_kyllang_monolith",
        "name": "Lum Kyllang (Kyllang Rock Granite Dome)",
        "site_type": "geological_shrine",
        "location": "West Khasi Hills, near Mairang",
        "elevation": "1,774 m",
        "presiding_deity": "U Kyllang (Deity of Stone and Wind)",
        "historical_age": "Pre-colonial mountain tradition",
        "significance": "A colossal single granite dome rising over 300 meters from the surrounding pine forest. Associated with epic folklore battles against U Leisymper and traditional meteorological predictions.",
        "cultural_practices": ["Local pastoral blessings and clan gatherings"]
    }
]

def list_sacred_sites() -> List[Dict[str, Any]]:
    """Return all documented traditional Khasi sacred sites and shrines."""
    return SACRED_SITES

def get_sacred_site(query: str) -> Optional[Dict[str, Any]]:
    """Find sacred site by name, location, or identifier."""
    q = query.lower().strip()
    for s in SACRED_SITES:
        if (q == s["id"] or
            q in s["name"].lower() or
            q in s["location"].lower()):
            return s
    return None

def sites_by_type(site_type: str) -> List[Dict[str, Any]]:
    """Filter sacred sites by type ('sacred_grove', 'megalithic_monolith', 'mountain_sanctuary', etc.)."""
    st = site_type.lower().strip()
    return [s for s in SACRED_SITES if s.get("site_type") == st]
