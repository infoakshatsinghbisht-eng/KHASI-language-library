# -*- coding: utf-8 -*-
"""
Khasi Pantheon, Territorial Guardian Deities & Indigenous Spiritual Beings.
Documented from:
- Shaphang U Wai U Blai (Babu Jeebon Roy)
- Ki Bor Phylla U Hynniewtrep (Donbok T. Laloo)
- Ka Niam Jong Ki Khasi (U Sib Charan Roy)
- Ka Niam Khasi Tynrai (S. Synrang Khonglah)
"""

from typing import Dict, List, Any, Optional

DEITIES: List[Dict[str, Any]] = [
    {
        "id": "nongbuh_nongthaw",
        "name": "U Blei Nongbuh Nongthaw",
        "realm": "celestial_supreme",
        "title": "The Supreme Sovereign Creator and Ordainer",
        "gender": "Universal Transcendent (addressed with honorific U)",
        "description": "The omnipotent, formless, uncreated Supreme God in Khasi monotheism. Does not inhabit man-made idols or stone carvings. Created the cosmos, the heavens, and human beings with the sole mandate to 'Kamai ïa ka Hok' (Earn Righteousness).",
        "manifestation": "Pure divine light, moral truth, supreme cosmic order (Ka Jutang).",
        "worship_form": "Pure prayer (Duwai Phirat) without idols, accompanied by libations."
    },
    {
        "id": "meiramew",
        "name": "Ka Meiramew",
        "realm": "terrestrial_nature",
        "title": "Mother Earth / Primal Nurturing Goddess",
        "gender": "Feminine (Ka)",
        "description": "The sacred Earth goddess who brings forth vegetation, mineral wealth, agriculture, and water springs to sustain humankind. Revered as the physical mother of all mortal existence.",
        "manifestation": "Fertile soil, forests, crops, living water.",
        "worship_form": "Thanksgiving ceremonies before sowing and after harvest."
    },
    {
        "id": "lei_shyllong",
        "name": "U Lei Shyllong",
        "realm": "mountain_sovereign",
        "title": "Patron Mountain Deity of Shillong Peak",
        "gender": "Masculine (U)",
        "description": "The paramount territorial guardian spirit presiding over the sacred summit of Lum Shillong (1,965 m). Revered as the state patron deity of both Hima Mylliem and Hima Khyrim, from whom the royal Syiem line of Khyrim and Mylliem claims political covenant.",
        "manifestation": "High mountain peaks, thunderclouds over the central plateau.",
        "worship_form": "Annual Pomblang state festival at Smit and state sacrifices on Shillong Peak."
    },
    {
        "id": "suidnia",
        "name": "U Suidnia",
        "realm": "ancestral_matrilineal",
        "title": "Primal Maternal Uncle & Divine Intercessor",
        "gender": "Masculine (U)",
        "description": "The deified spiritual representation of the first maternal uncle (Kñi) of the clan who crossed into the spiritual realm. In Khasi belief, U Suidnia stands before God as the chief advocate and mediator pleading for the welfare and purification of his living matrilineal kin.",
        "manifestation": "Central tall upright megalithic stone (U Maw-shynrang) in clan alignments.",
        "worship_form": "Tangsnoing lineage chants and the highest sacrificial offerings during bone internment."
    },
    {
        "id": "ka_iawbei",
        "name": "Ka Iawbei (Ka Iawbei Tynrai)",
        "realm": "ancestral_matrilineal",
        "title": "The Primal Ancestral Mother of the Clan",
        "gender": "Feminine (Ka)",
        "description": "The revered founding matriarch from whose womb the entire matrilineal clan (Kur) sprang. Remembered with profound reverence in every domestic prayer as the mother of the clan's life.",
        "manifestation": "Horizontal flat dolmen stone (Ka Maw-kynthei) resting upon stone pedestals.",
        "worship_form": "Consecration of the central stone table during Thep Mawbah."
    },
    {
        "id": "u_thawlang",
        "name": "U Thawlang",
        "realm": "ancestral_paternal",
        "title": "The Primal Father of the Matrilineal Clan",
        "gender": "Masculine (U)",
        "description": "The first husband of Ka Iawbei and primal father of the lineage. Though descent is matrilineal, U Thawlang is honored as the bringer of seed and physical protection.",
        "manifestation": "Head stone in the male megalithic tri-pillar grouping.",
        "worship_form": "Dual libations offered during family remembrance rites."
    },
    {
        "id": "ryngkew_basa",
        "name": "U Ryngkew U Basa (Labasa)",
        "realm": "territorial_forest",
        "title": "Territorial Guardian Spirits of Soil & Sacred Groves",
        "gender": "Masculine (U)",
        "description": "The vigilant spirit guardians residing in sacred groves (Law Kyntang) and village borders. Manifests as a protective leopard, tiger, or serpent. Punishes violators who desecrate sacred forests by taking dead wood, leaves, or stones.",
        "manifestation": "Sacred virgin cloud forests (e.g. Mawphlang), massive living trees, stone altars.",
        "worship_form": "Annual Kñia Ryngkew sacrifice at the forest altar (Duwan)."
    },
    {
        "id": "leisymper",
        "name": "U Leisymper",
        "realm": "mountain_sovereign",
        "title": "Guardian God of Symper Rock",
        "gender": "Masculine (U)",
        "description": "The mountain deity dwelling upon the dramatic domed monolith of Symper Rock in Maharam. Legend recounts an epic duel of stones between U Leisymper and U Kyllang (Kyllang Rock).",
        "manifestation": "The granite dome of Symper Rock, fierce mountain winds.",
        "worship_form": "Local pastoral sacrifices by surrounding villages."
    },
    {
        "id": "ka_kupli",
        "name": "Ka Kupli",
        "realm": "river_water",
        "title": "Goddess of the Kopili River",
        "gender": "Feminine (Ka)",
        "description": "The fierce, sovereign river deity of the Kopili border river between the Jaintia Hills and Assam. In pre-colonial times, travellers and the royal court of Jaintiapur offered solemn sacrifices at the Kupli falls before crossing the torrent.",
        "manifestation": "Roaring rapids, river falls, river mists.",
        "worship_form": "Historical state sacrifices along the border crossing."
    },
    {
        "id": "lei_longspah",
        "name": "U Lei Longspah",
        "realm": "wealth_providence",
        "title": "Deity of Righteous Prosperity and Abundance",
        "gender": "Masculine (U)",
        "description": "The divinity who dispenses legitimate commercial wealth, fertile livestock, and grain to families who earn through honest, virtuous labor (Kamai ïa ka Hok). Strictly distinguished from ill-gotten wealth associated with the evil Thlen.",
        "manifestation": "Rich granaries, thriving domestic trade, peaceful harvests.",
        "worship_form": "Home thanksgiving prayers accompanied by betel nut offerings."
    },
    {
        "id": "blai_synteng",
        "name": "U Blai Synteng",
        "realm": "regional_supreme",
        "title": "Supreme Divine Presence of Jaintia / Pnar Realm",
        "gender": "Universal / Masculine",
        "description": "The divine sovereign entity revered by the Pnar (Jaintia) people, celebrated during the Behdeiñkhlam festival at Jowai in the sacred pool Aitnar.",
        "manifestation": "The sacred Aitnar pool, the Symbud Khnong and Deinkhlam sacred logs.",
        "worship_form": "Behdeiñkhlam ritual dance and immersion of sacred Rot towers."
    }
]

def list_deities() -> List[Dict[str, Any]]:
    """Return all documented traditional Khasi deities and guardian spirits."""
    return DEITIES

def get_deity(query: str) -> Optional[Dict[str, Any]]:
    """Find deity by Khasi name, English title, or identifier."""
    q = query.lower().strip()
    for d in DEITIES:
        if (q == d["id"] or
            q in d["name"].lower() or
            q in d["title"].lower()):
            return d
    return None

def deities_by_realm(realm: str) -> List[Dict[str, Any]]:
    """Filter deities by realm ('celestial_supreme', 'mountain_sovereign', 'ancestral_matrilineal', 'territorial_forest', etc.)."""
    r = realm.lower().strip()
    return [d for d in DEITIES if d.get("realm") == r]
