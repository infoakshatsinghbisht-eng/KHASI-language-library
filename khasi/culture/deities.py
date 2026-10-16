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
    },
    {
        "id": "lei_kyllang",
        "name": "U Lei Kyllang",
        "realm": "mountain_sovereign",
        "title": "Deity of the Kyllang Granite Monolith & Gales",
        "gender": "Masculine (U)",
        "description": "The mighty mountain god presiding over Kyllang Rock (1,650 m) near Mairang. According to oral lore, he engaged in an epic stone-hurling duel against U Leisymper and commands ferocious gale winds across the plateau.",
        "manifestation": "Massive red granite dome of Kyllang Rock, vortex winds, thunder.",
        "worship_form": "Traditional offerings by the Khadsawphra / Nongkhlaw clan confederations."
    },
    {
        "id": "lei_synshar",
        "name": "Ka Lei Synshar",
        "realm": "celestial_justice",
        "title": "Goddess of Constitutional Justice, Law & Good Governance",
        "gender": "Feminine (Ka)",
        "description": "The divine patroness of statecraft, the people's assembly (Ka Dorbar), constitutional wisdom, and legal balance. Invoked by chieftains (Syiem) and elders (Lyngdoh) before enacting communal judgments.",
        "manifestation": "The sacred stone council circle (Ki Maw-dorbar), moral jurisprudence.",
        "worship_form": "Opening prayers before village and state Dorbars."
    },
    {
        "id": "ka_sngi_blei",
        "name": "Ka Sngi (Ka Lei Sngi)",
        "realm": "celestial_supreme",
        "title": "The Radiant Sun Goddess / Primal Mother of Light",
        "gender": "Feminine (Ka)",
        "description": "In Khasi cosmology, the Sun is feminine (Ka Sngi) and the Moon is masculine (U Bnai). She is the supreme dispenser of daylight, plant photosynthesis, warmth, and vitality across the earth.",
        "manifestation": "Sunlight, daybreak, solar warmth, morning mist dispersal.",
        "worship_form": "Dawn salutations and solar thanksgiving chants."
    },
    {
        "id": "u_bnai_blei",
        "name": "U Bnai (U Lei Bnai)",
        "realm": "celestial_supreme",
        "title": "The Gentle Moon God / Lord of Night and Market Cycles",
        "gender": "Masculine (U)",
        "description": "The elder brother of Ka Sngi who accepted soot upon his face out of profound shame in the ancient myth. Regulates the 8-day traditional market cycle and night tides.",
        "manifestation": "Moonlight, evening skies, lunar phases, nocturnal cooling.",
        "worship_form": "Nocturnal prayers during full moon and new moon ceremonies."
    },
    {
        "id": "lei_myntdu",
        "name": "Ka Lei Myntdu (Ka Tawiar Takan)",
        "realm": "river_water",
        "title": "Guardian River Goddess of Jowai & Jaintia Realm",
        "gender": "Feminine (Ka)",
        "description": "The sacred river deity encircling the ancient city of Jowai on three sides like a guardian necklace (Tawiar Takan). Protects the people of Jowai from plague, drought, and invading enemies.",
        "manifestation": "Meandering crystal waters of River Myntdu, riparian meadows.",
        "worship_form": "Pre-Behdeiñkhlam riverbank libations and Pnar civic rituals."
    },
    {
        "id": "lei_umngot",
        "name": "Ka Lei Umngot",
        "realm": "river_water",
        "title": "The Mirror-Clear River Goddess of the Southern Gorges",
        "gender": "Feminine (Ka)",
        "description": "The sister river to Ka Umïam, famous for her transparent emerald depths at Dawki and Shnongpdeng where wooden boats appear to float on air. Sisterly rival in the famous footrace to the plains.",
        "manifestation": "Glass-clear waters, limestone river canyons, border cascades.",
        "worship_form": "Fishermen's phawar and river thanksgiving ceremonies."
    },
    {
        "id": "u_bsein_thlen",
        "name": "U Bsein Thlen",
        "realm": "underworld_serpent",
        "title": "The Evil Serpent Demon of Greed and Blood Curse",
        "gender": "Masculine (U)",
        "description": "The malevolent primordial serpent who demanded human blood sacrifices (Nongshohnoh) in exchange for fleeting earthly gold. Slain by heroic U Suidnoh at Dainthlen waterfall, but remnants of his curse remain as a moral warning against avarice.",
        "manifestation": "Hidden underground caverns, Dainthlen basalt potholes, destructive greed.",
        "worship_form": "Strictly renounced; rituals exist to sever and purge Thlen curses (Kñia Thlen)."
    },
    {
        "id": "ka_ksaw_ka_jiri",
        "name": "Ka Ksaw Ka Jiri",
        "realm": "territorial_forest",
        "title": "Spirit Maiden of the Sacred Canopy & Ancient Epiphytes",
        "gender": "Feminine (Ka)",
        "description": "The elusive woodland nymph residing in centuries-old strangler figs (Jiri) and living root bridges. Protects woodland flowers, ferns, and nesting mountain birds.",
        "manifestation": "Living root bridges (Jingkieng Jri), aerial banyan roots, forest mist.",
        "worship_form": "Quiet forest blessings and offerings of betel leaf at river crossings."
    },
    {
        "id": "suid_tynrai",
        "name": "U Suid Tynrai",
        "realm": "ancestral_matrilineal",
        "title": "Primal Guardian Spirit of the Ancestral Clan Estate",
        "gender": "Masculine (U)",
        "description": "The deified spiritual presence of all departed maternal ancestors watching over the collective ancestral land (Ri Kur) and clan ossuary (Mawbah).",
        "manifestation": "Ancestral land boundary stones, clan stone cists.",
        "worship_form": "Thep Mawbah clan funeral ceremonies and annual libations."
    },
    {
        "id": "mawlong_syiem",
        "name": "U Mawlong Syiem",
        "realm": "mountain_sovereign",
        "title": "Patron Monolith Spirit of the Shella Gorges",
        "gender": "Masculine (U)",
        "description": "The guardian rock spirit defending the southern limestone canyons facing the Bengal plains. Revered by the War-Khasi people for shielding citrus and betel plantations.",
        "manifestation": "Limestone pillars, subtropical river gorges of Shella.",
        "worship_form": "Local War-Khasi seasonal agrarian offerings."
    },
    {
        "id": "lei_khyrwi",
        "name": "Ka Lei Khyrwi",
        "realm": "terrestrial_nature",
        "title": "Goddess of Sprouting Seeds & Germination",
        "gender": "Feminine (Ka)",
        "description": "The gentle agricultural divinity who causes dormant grains of paddy, millet, and maize to burst into life within the dark soil.",
        "manifestation": "Green seedlings, springtime terrace shoots.",
        "worship_form": "Pre-monsoon sowing chants and blessed seed ceremonies."
    },
    {
        "id": "lei_diengiei",
        "name": "U Lei Diengiei",
        "realm": "mountain_sovereign",
        "title": "Deity of Mount Diengiei & Cosmic Light Restoration",
        "gender": "Masculine (U)",
        "description": "The divine spirit inhabiting Lum Diengiei (west of Shillong), where the legendary cosmic tree Diengiei once blocked the sun until felled through the united wisdom of all creatures led by the Phreit bird.",
        "manifestation": "Crest of Mount Diengiei, ancient crater lake, mountain breezes.",
        "worship_form": "Commemorative origin prayers honoring unity and ecological balance."
    },
    {
        "id": "phan_kyrpad",
        "name": "U Phan U Kyrpad",
        "realm": "wealth_providence",
        "title": "Household Deity of Domestic Sustenance & Root Crops",
        "gender": "Masculine (U)",
        "description": "The benevolent domestic spirit who watches over the kitchen garden, yam storage, sweet potato pits, and domestic fowl.",
        "manifestation": "Family granary, dry food racks above the hearth.",
        "worship_form": "First-fruit offerings of freshly dug tubers during harvest."
    },
    {
        "id": "rngiew_tymmen",
        "name": "U Rngiew (Ka Rngiew)",
        "realm": "spiritual_aura",
        "title": "The Divine Spirit of Inner Radiance, Moral Stature & Aura",
        "gender": "Universal / Transcendent",
        "description": "The intrinsic spiritual aura and personal power granted by God to every human being. When a person lives righteously (Hok), their Rngiew shines brilliantly (Ksan Rngiew); when they commit sin or deceit, their Rngiew diminishes (Rem Rngiew).",
        "manifestation": "Moral courage, personal dignity, spiritual presence, charismatic leadership.",
        "worship_form": "Chants of Phawar Ksan Rngiew and ceremonial blessings by maternal uncles."
    },
    {
        "id": "ka_lei_umiam",
        "name": "Ka Lei Umïam",
        "realm": "aquatic_sacred",
        "title": "Goddess of the Umiam Waters & Weeping Lake",
        "gender": "Feminine (Ka)",
        "description": "The river deity born of the tears of the sorrowful sister who wept upon reaching the plains of Ri Bhoi, sanctified in foundational folk myth.",
        "manifestation": "Umiam river gorge, emerald waters, river mist.",
        "worship_form": "Traditional river libations and harvest prayers."
    },
    {
        "id": "u_lei_shillong",
        "name": "U Lei Shillong",
        "realm": "mountain_sovereign",
        "title": "Sovereign Mountain Protector of Shillong Peak",
        "gender": "Masculine (U)",
        "description": "The revered territorial deity guarding Lum Shillong, invoked by the royal Syiemships of Mylliem and Khyrim.",
        "manifestation": "Shillong peak crest, sacred stone altar, pine groves.",
        "worship_form": "State Pomblang goat sacrifice and royal blessings."
    },
    {
        "id": "u_lei_biskorom",
        "name": "U Lei Biskorom",
        "realm": "terrestrial_nature",
        "title": "Patron Spirit of Metallurgy, Blacksmiths & Craft",
        "gender": "Masculine (U)",
        "description": "Indigenous spirit of smithcraft, smelting, and toolmaking revered by Khasi artisans across ancient iron-smelting centers.",
        "manifestation": "Forge fires, anvils, sharpened blades (Waitlam).",
        "worship_form": "Traditional forge invocations and tool consecration."
    },
    {
        "id": "ka_lei_longspah",
        "name": "Ka Lei Longspah",
        "realm": "wealth_providence",
        "title": "Goddess of Abundance & Righteous Wealth",
        "gender": "Feminine (Ka)",
        "description": "The divine custodian of honest wealth and hearth prosperity granted only to those who live by righteous labor (Kamai ia ka hok).",
        "manifestation": "Golden paddy ears, abundance in the family granary.",
        "worship_form": "Kamai Ia Ka Hok prayers and honest hearth blessings."
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
