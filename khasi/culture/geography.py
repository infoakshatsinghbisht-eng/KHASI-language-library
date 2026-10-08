# -*- coding: utf-8 -*-
"""
Khasi Geography, Topography, Sacred Sites & Natural Wonders.
Comprehensive inventory of rivers (Wah), waterfalls (Kshaid), mountain peaks (Lum),
limestone caverns (Krem), sacred virgin forests (Law Kyntang), living root bridges (Jingkieng Jri),
and traditional Syiemship states (Ki Hima) of Meghalaya.
"""

from typing import Dict, List, Any, Optional

GEOGRAPHY: List[Dict[str, Any]] = [
    # --- Rivers (Ki Wah) ---
    {
        "name": "Wah Umngot",
        "type": "River (Wah)",
        "location": "Dawki, Indo-Bangladesh border",
        "significance": "Famed worldwide as the cleanest and clearest river in India; boats appear to float on glass above green pebble riverbeds; flows into the plains of Sylhet."
    },
    {
        "name": "Wah Umiam",
        "type": "River & Reservoir (Wah)",
        "location": "Ri-Bhoi & East Khasi Hills",
        "significance": "Scenic mountain river dammed in the 1960s to form Barapani Lake (Umiam Lake); named 'Lake of Tears' in ancient oral lore."
    },
    {
        "name": "Wah Kynshi",
        "type": "River (Wah)",
        "location": "West Khasi Hills & South West Khasi Hills",
        "significance": "Mighty river fed by numerous highland tributaries, cutting dramatic deep sandstone gorges and feeding vast hydroelectric potential."
    },
    {
        "name": "Wah Myntdu",
        "type": "River (Wah)",
        "location": "Jowai, West Jaintia Hills",
        "significance": "Revered by the Pnar people as their sacred guardian river ('Ka Tawiar Ka Takan'), encircling Jowai town on three sides."
    },
    {
        "name": "Wah Umngi",
        "type": "River (Wah)",
        "location": "South West Khasi Hills",
        "significance": "Torrential mountain river celebrated for golden mahseer fishing and dramatic sandstone canyon valleys."
    },

    # --- Waterfalls (Ki Kshaid) ---
    {
        "name": "Kshaid Nohkalikai",
        "type": "Waterfall (Kshaid)",
        "location": "Cherrapunji / Sohra (340 meters plunge)",
        "significance": "Tallest plunge waterfall in India (1,115 ft); immortalized by the poignant tragic legend of Ka Likai."
    },
    {
        "name": "Kshaid Dainthlen",
        "type": "Waterfall (Kshaid)",
        "location": "Near Sohra",
        "significance": "Site of the legendary mythological battle where hero U Suidnoh and community warriors slew the demon serpent U Thlen; stone natural chisel marks visible on bedrock."
    },
    {
        "name": "Kshaid Nohsngithiang (Seven Sisters Falls)",
        "type": "Waterfall (Kshaid)",
        "location": "Mawsmai village, Sohra (315 meters)",
        "significance": "Spectacular seven-segmented cascade plummeting off towering limestone cliffs into Bangladesh plains; illuminated by afternoon sun rays."
    },
    {
        "name": "Kshaid Kynrem",
        "type": "Waterfall (Kshaid)",
        "location": "Thangkharang Park, Sohra (305 meters)",
        "significance": "Majestic three-tiered cascade roaring through dense southern rainforest slopes."
    },
    {
        "name": "Kshaid Krang Suri",
        "type": "Waterfall (Kshaid)",
        "location": "Amlarem, West Jaintia Hills",
        "significance": "Unearthly natural plunge pool of turquoise-blue crystalline waters surrounded by lush green foliage and stone bridges."
    },
    {
        "name": "Kshaid Elephant (Ka Kshaid Lai Pateng Khohsiew)",
        "type": "Waterfall (Kshaid)",
        "location": "Upper Shillong",
        "significance": "Historic three-tier cascade named after an elephant-shaped rock; traditional rest stop for travellers scaling the high plateau."
    },

    # --- Mountains & Peaks (Ki Lum) ---
    {
        "name": "Lum Shillong (Shillong Peak)",
        "type": "Mountain Peak (Lum)",
        "elevation": "1,965 meters (Highest point in Khasi Hills)",
        "significance": "Sacred summit venerated as the sanctum of 'U Lei Shillong' (the presiding deity of the land); panoramic view across entire Khasi plateau."
    },
    {
        "name": "Lum Sohpetbneng",
        "type": "Sacred Mountain Peak (Lum)",
        "elevation": "1,344 meters (Ri-Bhoi)",
        "significance": "The 'Navel of Heaven'; holiest mountain of Khasi faith where the Golden Ladder connected the 16 celestial families to earth, and where Ki Hynniewtrep descended."
    },
    {
        "name": "Lum Diengiei",
        "type": "Mountain Peak (Lum)",
        "elevation": "1,823 meters (West of Shillong)",
        "significance": "Site of the ancient cosmic legend where the colossal Tree of Darkness blotted out the sun until felled by community courage."
    },
    {
        "name": "Lum Kyllang (Kyllang Rock)",
        "type": "Mammoth Granite Dome Rock (Lum)",
        "elevation": "1,774 meters (Near Mairang, West Khasi Hills)",
        "significance": "Monolithic red granite dome rising sheer out of the surrounding pine forest; mythological rival of Lum Symper."
    },
    {
        "name": "Lum Mawlongbna",
        "type": "Natural Heritage Site (Lum)",
        "location": "Mawsynram plateau",
        "significance": "Unique fossil site with prehistoric marine fossils, animal footprints embedded in stone, and natural cold freshwater springs."
    },

    # --- Sacred Groves (Ki Law Kyntang) ---
    {
        "name": "Law Kyntang Mawphlang",
        "type": "Sacred Virgin Grove (Law Kyntang)",
        "location": "Mawphlang, East Khasi Hills (76 hectares)",
        "significance": "Ancient virgin forest protected for over 800 years under customary law; abode of the forest deity Labasa; strict taboo prohibits removing even a single leaf or stone."
    },
    {
        "name": "Law Kyntang Sohra",
        "type": "Sacred Grove (Law Kyntang)",
        "location": "Sohra",
        "significance": "Highland rainforest preserve protecting endemic flora, orchids, and rare medicinal shrubs from rainfall erosion."
    },

    # --- Caves (Ki Krem) ---
    {
        "name": "Krem Liat Prah",
        "type": "Limestone Cave System (Krem)",
        "length": "Over 34 kilometers (Longest cave in South Asia)",
        "location": "Shnongrim Ridge, East Jaintia Hills",
        "significance": "Vast subterranean labyrinth of giant halls ('The Aircraft Hangar') and subterranean river systems."
    },
    {
        "name": "Krem Puri",
        "type": "Sandstone Cave System (Krem)",
        "length": "Over 24.5 kilometers (Longest sandstone cave in the world)",
        "location": "Mawsynram",
        "significance": "Houses dinosaur bones, shark teeth fossils, and unique blind subterranean fauna."
    },
    {
        "name": "Krem Mawmluh",
        "type": "Geological Type-Locality Cave (Krem)",
        "location": "Near Sohra (over 7 km long)",
        "significance": "Global geological type-locality for the 'Meghalayan Age' (the current geological age of Earth beginning 4,200 years ago), formalized by the IUGS in 2018."
    },

    # --- Living Root Bridges (Ki Jingkieng Jri) ---
    {
        "name": "Jingkieng Jri Nongriat (Double Decker Living Root Bridge)",
        "type": "Living Root Architecture (Jingkieng Jri)",
        "location": "Nongriat village (reached by 3,500 stone steps down Sohra cliffs)",
        "significance": "Bio-engineered wonder created by guiding aerial roots of Ficus elastica across roaring gorge waters; two parallel stacked root bridges carrying village transit for over 250 years."
    },
    {
        "name": "Jingkieng Jri Riwai",
        "type": "Living Root Bridge (Jingkieng Jri)",
        "location": "Riwai / Mawlynnong ('Cleanest Village in Asia')",
        "significance": "Massive single-span living root bridge stretching across the Thyllong river, thriving and growing stronger with each monsoon."
    },

    # --- Traditional Native States (Ki Hima Syiemship) ---
    {
        "name": "Hima Khyrim",
        "type": "Traditional Native Syiemship (Hima)",
        "capital": "Smit",
        "significance": "Major traditional Khasi state governed by the Syiem of Khyrim and Ka Syiem Sad; host of the annual Ka Pomblang Nongkrem festival."
    },
    {
        "name": "Hima Mylliem",
        "type": "Traditional Native Syiemship (Hima)",
        "capital": "Shillong / Nongkseh",
        "significance": "One of the largest Syiemships encompassing central Shillong, historic Iewduh market, and sacred Lum Shillong."
    },
    {
        "name": "Hima Sohra",
        "type": "Traditional Native Syiemship (Hima)",
        "capital": "Sohra (Cherrapunji)",
        "significance": "The cradle of standard literary Khasi orthography, historic British treaties, and high rainfall plateau."
    },
    {
        "name": "Hima Nongkhlaw",
        "type": "Traditional Native Syiemship (Hima)",
        "capital": "Nongkhlaw",
        "significance": "Realm of the heroic patriot U Tirot Sing Syiem who waged the historic Anglo-Khasi War (1829–1833) to preserve tribal freedom."
    },
    {
        "name": "Hima Nongstoin",
        "type": "Traditional Native Syiemship (Hima)",
        "capital": "Nongstoin, West Khasi Hills",
        "significance": "Vast western forested Syiemship renowned for ancient iron-smelting, monolithic stone quarries, and timber trade."
    }
]

def list_places() -> List[Dict[str, Any]]:
    """Return all documented Khasi geographical and historical places."""
    return GEOGRAPHY

def get_place(name: str) -> Optional[Dict[str, Any]]:
    """Find place by name, type, or location."""
    q = name.lower().strip()
    for p in GEOGRAPHY:
        if q in p["name"].lower() or q in p["type"].lower() or q in p.get("location", "").lower():
            return p
    return None

def by_type(geo_type: str) -> List[Dict[str, Any]]:
    """Filter places by geographical category (e.g. 'River', 'Waterfall', 'Peak', 'Cave', 'Sacred', 'Root Bridge', 'Hima')."""
    gt = geo_type.lower().strip()
    return [p for p in GEOGRAPHY if gt in p["type"].lower()]
