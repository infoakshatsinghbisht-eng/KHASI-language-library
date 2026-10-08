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
