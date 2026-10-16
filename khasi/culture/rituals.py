# -*- coding: utf-8 -*-
"""
Khasi Rituals, Divination & Traditional Ceremonial Practices.
Documented from authentic ethnographical records:
- Ka Niam Jong Ki Khasi (U Sib Charan Roy, 1919)
- Ka Niam Khasi Tynrai (S. Synrang Khonglah)
- U Khasi Hyndai (Rash Mohon Roy Nongrum, 1959)
- Notes on Khasi Divination and Sacrifice (Gurdon, Bareh, Lyngdoh)
"""

from typing import Dict, List, Any, Optional

RITUALS: List[Dict[str, Any]] = [
    {
        "id": "shat_pylleng",
        "name": "Ka Shat Pylleng",
        "english_name": "Egg Divination Rite",
        "category": "divination",
        "significance": "The primary method of divination in Khasi religion. The diviner strikes an unboiled egg upon the consecrated wooden board (Dieng Shat Pylleng) with red earth. By the pattern in which eggshell fragments fall (concave or convex, right or left), divine will, sources of affliction, or moral taboos are interpreted.",
        "materials": ["Pylleng (Egg)", "Dieng shat pylleng (Divining board)", "Dewstem (Yellowish-red clay)", "Kiad (Rice beer libation)"],
        "officiant": "U Nongkhan / U Nongshat (Diviner elder)",
        "occasions": ["Illness", "Before laying foundation of home", "Selecting syiem or village elder", "Unexplained misfortune"]
    },
    {
        "id": "khan_pyrthat",
        "name": "Ka Khan Pyrthat",
        "english_name": "Thunder & Celestial Omen Divination",
        "category": "divination",
        "significance": "Interpreting lightning strikes, dry thunder, and unusual celestial occurrences as direct warnings from U Blei regarding moral breaches in the realm.",
        "materials": ["Dieng-ngan (Hardwood branch)", "Kwai bad tympew (Betel nut and leaf)"],
        "officiant": "Ki Tymmen Shnong (Council elders)",
        "occasions": ["Unseasonal storms", "Community calamity"]
    },
    {
        "id": "syiar_ryngkew",
        "name": "U Syiar Ryngkew",
        "english_name": "Sacrifice of the Cock Mediator",
        "category": "sacrifice",
        "significance": "In Khasi theology, the unblemished cock volunteered to sacrifice its life to bring back the sun when humanity was plunged into darkness at Lum Diengiei. The cock is offered as a sacred mediator that bears humanity's spiritual burden before Almighty God.",
        "materials": ["Syiar shynrang (Unblemished young rooster)", "Kba (Rice grains)", "Um khuid (Pure spring water)"],
        "officiant": "U Lyngdoh / U Kñi (Priest or maternal uncle)",
        "occasions": ["Annual state rituals", "Hearth purification", "Grave illness"]
    },
    {
        "id": "pomblang_nongkrem",
        "name": "Ka Pomblang Nongkrem",
        "english_name": "Royal Goat Decapitation Sacrifice",
        "category": "sacrifice",
        "significance": "The crowning liturgical ceremony of Hima Khyrim during the Nongkrem Festival at Smit. Sacrificial he-goats (Blang) offered by the Syiem, Lyngskor, and hereditary noble clans are solemnly decapitated in single strokes before the altar of U Lei Shyllong to ensure rain, harvest, and commonwealth peace.",
        "materials": ["Ki blang (He-goats)", "Waitlam (Traditional sacrificial sword)", "Kiad hiar (Sacred libation)"],
        "officiant": "U Syiem bad u Soh-Blei (King and Chief Priest of Khyrim)",
        "occasions": ["Autumn state festival at Smit"]
    },
    {
        "id": "thep_mawbah",
        "name": "Ka Thep Mawbah",
        "english_name": "Clan Megalithic Bone Internment Ceremony",
        "category": "funerary",
        "significance": "The most elaborate and costly life-cycle rite of the Khasi. The cremated bone relics (Ki Shyieng) of all departed clan members are gathered from temporary cairns (Mawshyngiar) and ceremonially transferred with royal pomp, chanting, and feast to the great ancestral clan megalith (U Mawbah). This final unification seals clan solidarity beyond mortality.",
        "materials": ["Khyndew / Maw (Granite megaliths)", "Jaiñ-kup (Embroidered funerary silks)", "Ksing bad Sharati (Flutes and mourning drums)"],
        "officiant": "U Kñi Rangbah bad Ka Khadduh (Elder maternal uncle and youngest heiress daughter)",
        "occasions": ["Once every few decades per matrilineal clan"]
    },
    {
        "id": "jer_thoh",
        "name": "Ka Jer Ka Thoh",
        "english_name": "Traditional Naming & Dedication Ceremony",
        "category": "rite_of_passage",
        "significance": "Performed on the morning after birth. The infant is formally dedicated. If male, a miniature bow and three arrows (Ryntieh bad khnam) are placed, symbolising hunting, defence, and sovereignty. If female, a woven basket and headstrap (Khoh bad star) are placed, symbolising hearth management, matrilineal lineage preservation, and trade.",
        "materials": ["Ryntieh bad khnam (Bow and 3 arrows)", "Khoh bad star (Basket and strap)", "Kiad um (Rice wine)", "Pylleng (Egg)"],
        "officiant": "U Kñi (Maternal uncle) or grandmother",
        "occasions": ["Infant birth"]
    },
    {
        "id": "shongkurim_niam",
        "name": "Ka Shongkurim Katkum Ka Niam Tynrai",
        "english_name": "Customary Matrimonial Matrilocal Covenant",
        "category": "marriage",
        "significance": "Solemn marriage treaty between two exogamous matrilineal clans (Kur). Strict observance of clan exogamy (no Kur or Kha incestuous overlap). The groom's maternal uncle leads the procession to the bride's hearth, where prayers, libations, and the eating of rice from a single platter solemnize the lifelong bond.",
        "materials": ["Pliang rupa (Silver platter)", "Ja bad doh (Consecrated rice and meat)", "Kiad (Sacred libation)"],
        "officiant": "Ki Kñi jong baroh arliang (Maternal uncles of bride and groom)",
        "occasions": ["Matrimony"]
    },
    {
        "id": "knia_shnong",
        "name": "Ka Kñia Shnong",
        "english_name": "Village Communal Sanctification Sacrifice",
        "category": "agricultural_communal",
        "significance": "Conducted at the village boundary altars to propitiate U Ryngkew U Basa (guardian spirits of the territory), seeking protection against landslides, cattle plagues, blight, and hostile incursions.",
        "materials": ["Syiar (Sacrificial fowl)", "Kwai (Betel nuts)", "Sla lakait (Plantain leaves)"],
        "officiant": "U Lyngdoh Shnong (Village priest)",
        "occasions": ["Spring sowing season", "Post-harvest thanksgiving"]
    },
    {
        "id": "tangsnoing",
        "name": "Ka Tangsnoing",
        "english_name": "Ancestral Lineage Recitation & Covenant",
        "category": "genealogy",
        "significance": "The sacred oral recitation of the maternal clan's genealogy, ancestral roots, founding matriarch (Ka Iawbei), and primal uncle (U Suidnia) chanted solemnly before major sacrifices to establish unbroken continuity.",
        "materials": ["Sla dula (Sacred leaves)", "Kiad"],
        "officiant": "U Tymmen Kur / U Kñi Rangbah (Clan patriarch)",
        "occasions": ["Before Thep Mawbah", "Clan reconciliation"]
    },
    {
        "id": "pyllait_thlen",
        "name": "Ka Pyllait Thlen",
        "english_name": "Ritual Cleansing & Severing of the Thlen Curse",
        "category": "purification",
        "significance": "A rare, solemn ritual performed when a family discovers ancestral association with the demonic serpent Thlen. All accumulated gold, coins, clothing, and domestic goods are destroyed or thrown into deep roaring rivers, and solemn oaths are sworn before God never to harbor the spirit again.",
        "materials": ["Nar ba sait shit (Red-hot iron)", "Klong um (Gourd filled with holy water)"],
        "officiant": "U Lyngdoh / Assembly of village elders",
        "occasions": ["Casting off spiritual affliction"]
    },
    {
        "id": "behdeinkhlam_tapmohkhlieh",
        "name": "Ka Tap-Mohkhlieh bad Ka Shad Behdeinkhlam",
        "english_name": "Pnar Sanctification & Pestilence-Chasing Rite",
        "category": "agricultural_communal",
        "significance": "The sacred Jaintia ritual where young men beat the roofs of every house with polished wooden poles (Khlam) to chase away pestilence, plague, and malevolent spirits, followed by dancing in the sacred muddy pool Aitnar and immersing towering colourful 'Raths' (Rots) to invoke bountiful harvest.",
        "materials": ["Deinkhlam (Sacred poles)", "Rots (Towering paper bamboo towers)", "Kiad (Sacred rice libation)", "Ka Aitnar (Holy pool)"],
        "officiant": "U Daloi bad u Langdoh (Pnar Chieftain and Chief Priest)",
        "occasions": ["Mid-summer monsoons in Jowai (July)"]
    },
    {
        "id": "knia_mawbynna",
        "name": "Ka Kñia Mawbynna",
        "english_name": "Megalith Erection & Consecration Rite",
        "category": "memorial",
        "significance": "Solemn ritual performed when erecting memorial monoliths (Mawbynna / Maw-shynrang) and dolmens (Mawkynthai / Maw-kynthei). Prayers and libations are offered to immortalize renowned maternal uncles, ancestral chiefs, and mothers, bridging the realm of the living with the spirit world.",
        "materials": ["Maw-bynna (Granite monolith)", "Maw-kynthei (Flat dolmen stone)", "Syiar (Rooster)", "Kiad hiar (Distilled rice libation)"],
        "officiant": "U Kñi Rangbah bad Ki Tymmen Shnong (Senior maternal uncle and elders)",
        "occasions": ["After clan funerary rites", "Commemorating heroic ancestors"]
    },
    {
        "id": "knia_pyrda_kmie",
        "name": "Ka Kñia Pyrda / Ka Kñia Kmie",
        "english_name": "Maternal Hearth Ancestral Sacrifice to Ka Iawbei",
        "category": "ancestral",
        "significance": "Sacred domestic sacrifice conducted at the family hearth (Ka Dpei) to propitiate Ka Iawbei (the founding primal mother of the clan) and ancestral spirits. Fowl or animal offerings and sacred rice are consecrated to ensure maternal fertility, familial harmony, and continuous blessing upon the lineage.",
        "materials": ["Ka Dpei (Sacred hearth fire)", "Syiar kynthei (Consecrated hen)", "Ja khuid (Pure consecrated rice)", "Klong kiad (Gourd of rice beer)"],
        "officiant": "Ka Khadduh (Youngest daughter/priestess) bad U Kñi (Maternal uncle)",
        "occasions": ["Ancestral memorial days", "Before building a home", "Resolving family discord"]
    },
    {
        "id": "pyniasoh_kpoh",
        "name": "Ka Pyniasoh Kpoh",
        "english_name": "Clan Adoption & Lineage Grafting Covenant",
        "category": "kinship",
        "significance": "A rare customary legal and religious rite wherein a family without female heirs (Ka Iap-duh) formally adopts and grafts a daughter from an allied related clan into their matrilineal womb (Kpoh), preserving the lineage, hearth rites, and clan inheritance from extinction.",
        "materials": ["Kwai bad tympew (Betel nut and leaf covenants)", "Klong kiad", "Sla lakait (Plantain leaves)"],
        "officiant": "Ki Kñi jong baroh arliang bad Ki Myntri (Maternal uncles and state magistrates)",
        "occasions": ["Imminent clan extinction (Iapduh)", "Lineage preservation"]
    },
    {
        "id": "khan_pylleng_jingpang",
        "name": "Ka Khan-Pylleng ha Ka Jingpang",
        "english_name": "Diagnostic Healing Divination & Spiritual Appeasement",
        "category": "healing_divination",
        "significance": "Performed when medicine fails to alleviate illness. An egg is broken upon the board to discover whether the sickness is caused by an offended territorial spirit (U Ryngkew U Basa), broken moral vow (Ka Sngewbha / Ka Sngewlem), or ancestral displeasure, determining the precise atonement sacrifice needed.",
        "materials": ["Pylleng (Egg)", "Dieng shat pylleng (Divination board)", "Dewstem (Sacred red-yellow earth)"],
        "officiant": "U Nongkhan / U Nongshat (Master diviner)",
        "occasions": ["Chronic illness", "Sudden mysterious affliction"]
    }
]

def list_rituals() -> List[Dict[str, Any]]:
    """Return all documented traditional Khasi rituals."""
    return RITUALS

def get_ritual(query: str) -> Optional[Dict[str, Any]]:
    """Find ritual by Khasi name, English name, or identifier."""
    q = query.lower().strip()
    for r in RITUALS:
        if (q == r["id"] or
            q in r["name"].lower() or
            q in r["english_name"].lower()):
            return r
    return None

def rituals_by_category(category: str) -> List[Dict[str, Any]]:
    """Filter rituals by category ('divination', 'sacrifice', 'funerary', 'rite_of_passage', etc.)."""
    c = category.lower().strip()
    return [r for r in RITUALS if r.get("category") == c]
