# -*- coding: utf-8 -*-
"""
Khasi Traditional Attire, Handloom Textiles, Jewellery, and Dance Regalia.
Documented from authentic Khasi ethnographical, textile, and cultural authorities:
- Ka Riti Jong Ka Ri Khasi (U Radhon Singh Berry)
- Ka Niam Khasi Tynrai & Traditional Regalia Records (Seng Khasi & Seinraij)
- Meghalaya Handloom & Sericulture Monographs (Ryndia / Eri Silk Traditions of Ri Bhoi)
- Pnar and Khasi Traditional Ornaments and Dance Attire (Bareh, Gurdon, Roy)
"""

from typing import Dict, List, Any, Optional

TRADITIONAL_GARMENTS: List[Dict[str, Any]] = [
    {
        "id": "jainsem",
        "name": "Ka Jaiñsem",
        "english_name": "Two-Piece Draped Silk Tunic",
        "gender": "female",
        "category": "garment",
        "type": "outerwear",
        "materials": ["Mulberry silk", "Eri silk (Ryndia)", "Muga silk", "Fine cotton"],
        "region": ["Khasi Hills", "Ri Bhoi", "Jaintia Hills"],
        "description": "The quintessential traditional garment worn by Khasi women. Consists of two unstitched lengths of silk or cotton, each pinned over opposite shoulders with ornate brooches (kad-kpieng) and draped gracefully to cross over the chest and back, hanging gracefully down to the ankles.",
        "cultural_significance": "Represents feminine grace, modesty, and matrilineal pride. In Khasi philosophy, the harmonious crossover of the two cloths signifies balance, protection of the heart, and dignity in public life.",
        "occasions": ["Formal gatherings", "Church / Chapel services", "Festivals", "Daily wear (cotton)", "Weddings"]
    },
    {
        "id": "dhara",
        "name": "Ka Dhara (Jaiñsem Dhara)",
        "english_name": "Heavy Ceremonial Brocade Silk Garment",
        "gender": "female",
        "category": "garment",
        "type": "ceremonial",
        "materials": ["Heavy raw mulberry silk", "Gold thread brocade"],
        "region": ["All Khasi and Pnar regions"],
        "description": "The heaviest and most prestigious version of the Jainsem, woven from thick, lustrous raw silk with embroidered or plain borders. Worn during Shad Suk Mynsiem, Shad Nongkrem, and royal weddings.",
        "cultural_significance": "A prized heirloom passed down across generations from mother to youngest daughter (Ka Khadduh). Its weight and stiffness give the dancer a regal, gliding posture.",
        "occasions": ["Shad Suk Mynsiem", "Ka Shad Nongkrem", "Traditional Weddings", "State receptions"]
    },
    {
        "id": "jainkup",
        "name": "Ka Jaiñkup",
        "english_name": "Mantle / Shawl Wrap",
        "gender": "female",
        "category": "garment",
        "type": "mantle",
        "materials": ["Woven wool", "Cashmere", "Thick silk", "Velvet"],
        "region": ["Sohra", "Shillong Plateau", "Upper Khasi Highlands"],
        "description": "A dignified, heavy woolen or silk cape-shawl draped around the shoulders and neck, held together at the throat or pinned with a golden clasp. Often richly bordered or fringed.",
        "cultural_significance": "Worn by respected matriarchs and elders, providing thermal protection against misty highland rains while embodying maternal authority and quiet grandeur.",
        "occasions": ["Winter gatherings", "Funeral wakes", "Dorbar convocations", "Elderly ceremonial wear"]
    },
    {
        "id": "kyrshah",
        "name": "Ka Kyrshah",
        "english_name": "Checkered Working Apron / Wrap",
        "gender": "female",
        "category": "garment",
        "type": "daily_wrap",
        "materials": ["Gingham cotton", "Handspun checkered cotton", "Linen"],
        "region": ["All Khasi, Bhoi, and War villages"],
        "description": "A practical checkered cloth fastened across one shoulder with a diagonal knot or safety pin, draping across the torso to shield inner garments during hearth work, harvesting, and domestic hospitality.",
        "cultural_significance": "The symbol of industrious Khasi homemaking, agricultural diligence, and warm hearthside hospitality. Worn while brewing tea, peeling kwai, or tending fields.",
        "occasions": ["Everyday village life", "Agricultural harvesting", "Cooking", "Local markets"]
    },
    {
        "id": "tapmohkhlieh",
        "name": "Ka Tapmohkhlieh",
        "english_name": "Traditional Headscarf & Cowl",
        "gender": "female",
        "category": "garment",
        "type": "headwear",
        "materials": ["Knitted wool", "Woven silk-cotton", "Embroidered cashmere"],
        "region": ["Highland Sohra", "Mawphlang", "Mylliem"],
        "description": "A warm rectangular scarf wrapped snugly under the chin and over the crown of the head, framing the face and tied behind the neck or crossed across the chest.",
        "cultural_significance": "Provides shield against the biting plateau frost and winds of Sohra while maintaining dignified, modest presentation.",
        "occasions": ["Misty winters", "Sunday walks", "Market mornings (Iewduh)"]
    },
    {
        "id": "jainpien",
        "name": "Ka Jaiñpien",
        "english_name": "Inner Wraparound Skirt",
        "gender": "female",
        "category": "garment",
        "type": "undergarment",
        "materials": ["Cotton", "Linen", "Soft silk"],
        "region": ["All Khasi Hills"],
        "description": "An inner unstitched cotton or silk skirt wrapped securely around the waist beneath the Jainsem, falling down to the shins.",
        "cultural_significance": "Forms the structural base layer upon which the outer silk Jainsem is anchored and styled.",
        "occasions": ["Underneath all traditional female attire"]
    },
    {
        "id": "tor_khyrwang",
        "name": "Ka Tor Khyrwang (Thoh Khyrwang Garment)",
        "english_name": "Pnar Checkered Striped Wrap",
        "gender": "female",
        "category": "garment",
        "type": "cultural_heritage",
        "materials": ["Handloom cotton", "Wild eri silk"],
        "region": ["Jaintia Hills (Pnar)", "War Jaintia"],
        "description": "A distinctive Pnar/Jaintia handwoven cloth patterned with bold black and crimson/white longitudinal geometric checks, worn by Pnar maidens during festivals like Behdeinkhlam and Shad Laho.",
        "cultural_significance": "Signature visual motif of Jaintia tribal identity, woven with generational hand-loom techniques.",
        "occasions": ["Behdeinkhlam", "Shad Laho", "Pnar communal festivals"]
    },
    {
        "id": "jymphong",
        "name": "U Jymphong",
        "english_name": "Sleeveless Long Tunic / Waistcoat",
        "gender": "male",
        "category": "garment",
        "type": "tunic",
        "materials": ["Velvet", "Ryndia silk", "Heavy cotton", "Embroidered wool"],
        "region": ["All Khasi states (Hima)"],
        "description": "A sleeveless, long-bodied male tunic reaching below the hips, open down the front, secured across the chest with frogs or silver chains (kynjri rupa). Often richly embroidered with golden piping along collar and edges.",
        "cultural_significance": "The primary garment of the Khasi male warrior, elder, and dancer. Leaves the arms free for archery (siat khnam), swordplay (mastieh), or playing the drum (ksing).",
        "occasions": ["Shad Suk Mynsiem", "Ka Shad Nongkrem", "Dorbar Hima meetings", "Traditional weddings"]
    },
    {
        "id": "spong",
        "name": "U Spong (Jaiñspong)",
        "english_name": "Ceremonial Silk Turban",
        "gender": "male",
        "category": "garment",
        "type": "headwear",
        "materials": ["Ryndia (Eri silk)", "Muga silk", "Fine muslin"],
        "region": ["All Khasi and Pnar regions"],
        "description": "A stately turban wrapped meticulously with multiple spiral folds around the crown, culminating in a ceremonial fan crest or trailing end.",
        "cultural_significance": "Symbolizes male wisdom, chivalry, and clan honor. Worn by kings (Syiem), priests (Lyngdoh), ministers (Myntri), and male ceremonial dancers.",
        "occasions": ["Shad Nongkrem", "Shad Suk Mynsiem", "Coronation of Syiem", "Dorbar"]
    },
    {
        "id": "dhoti_khasi",
        "name": "Ka Jaiñboit / Ka Dhoti Khasi",
        "english_name": "Traditional Pleated Lower Silk Wrapper",
        "gender": "male",
        "category": "garment",
        "type": "lower_body",
        "materials": ["White or yellow silk", "Ryndia silk", "Fine cotton"],
        "region": ["All Khasi Hills"],
        "description": "An unstitched silk or fine cloth tied firmly around the waist with pleated folds tucked securely in front and between the legs, allowing freedom of martial footwork.",
        "cultural_significance": "Enables agility during energetic ritual dances like Ka Shad Mastieh and archery ceremonies.",
        "occasions": ["Ritual dances", "Archery tournaments", "Festivals"]
    }
]

TEXTILES_AND_FABRICS: List[Dict[str, Any]] = [
    {
        "id": "ryndia",
        "name": "Ka Ryndia (Eri Silk)",
        "english_name": "Sacred Organic Khasi Peace-Silk",
        "category": "textile",
        "origin_region": "Ri Bhoi (Umden, Nongpoh, Saiden)",
        "silkworm": "Samia ricini (Castor-feeding moth)",
        "dyeing": "100% Natural dyes (Turmeric/stem, Lac insects, Madder, Iron-rich mud, Walnut bark)",
        "properties": [
            "Thermal insulation (cool in summer, warm in highland winter)",
            "Heirloom durability (grows softer with each wash over decades)",
            "Ahimsa / Non-violent peace silk (moths exit naturally before spinning)",
            "Hypoallergenic and breathable"
        ],
        "cultural_significance": "The sacred indigenous textile of the Khasi people. Used for mourning wraps, dance shawls, and royal investiture. Received Geographical Indication (GI) recognition.",
        "traditional_uses": ["Spong (turbans)", "Jainkup (shawls)", "Megalithic bone wrappers (Thep Mawbah)", "Jymphong tunics"]
    },
    {
        "id": "thoh_khyrwang_fabric",
        "name": "Ka Jaiñ Thoh Khyrwang",
        "english_name": "Traditional Jaintia Checkered Handloom Fabric",
        "category": "textile",
        "origin_region": "Jaintia Hills / Ri War",
        "weaving_loom": "Traditional reed floor loom / Frame loom",
        "patterns": "Contrasting geometric checks in bold black, crimson, and ivory white",
        "cultural_significance": "Unique weaving heritage of Pnar weavers, handed down matrilineally from mother to daughters in Jowai and surrounding hamlets.",
        "traditional_uses": ["Pnar dance wrappers", "Shoulder slings for infants", "Ceremonial waistbands"]
    },
    {
        "id": "jainsem_muga",
        "name": "Ka Jaiñsem Muga",
        "english_name": "Golden Muga Silk Textile",
        "category": "textile",
        "origin_region": "Brahmaputra-Meghalaya borderlands & Khasi hills",
        "properties": ["Natural lustrous golden sheen", "Resistant to moisture and friction"],
        "cultural_significance": "Worn by high-clan brides and the queen-mothers (Ka Syiem Sad) of Hima Khyrim during autumn sacrifices.",
        "traditional_uses": ["Royal garments", "Bridal dhara", "Festival wear"]
    },
    {
        "id": "sulan",
        "name": "Ka Jaiñ Sulan",
        "english_name": "Coarse Handspun Cotton Blanket",
        "category": "textile",
        "origin_region": "War Khasi & Bhoi borderlands",
        "properties": ["Thick, rugged, weather-resistant heavy cotton weave"],
        "cultural_significance": "Traditional field blanket and porter's shield against torrential monsoon rains in the southern gorges.",
        "traditional_uses": ["Everyday warmth", "Travel across mountain passes", "Sleeping blanket"]
    }
]

JEWELLERY_AND_ORNAMENTS: List[Dict[str, Any]] = [
    {
        "id": "pansngiat",
        "name": "Ka Pansngiat",
        "english_name": "Golden Maiden Crown / Tiara with Plume",
        "gender": "female",
        "category": "jewellery",
        "body_location": "Head / Crown",
        "materials": ["Solid gold", "Embossed sterling silver"],
        "design": "A semi-circular coronet of chased gold adorned with filigree floral engravings, featuring a vertical plume or spear-like spire (tiew lasubon) ascending from the back.",
        "cultural_significance": "The crowning symbol of unmarried Khasi maidenhood (Ki Thei Sotti) during sacred dances (Shad Suk Mynsiem and Shad Nongkrem). Signifies royal lineage, spiritual innocence, and the reverence accorded to women as custodians of clan life.",
        "occasions": ["Shad Suk Mynsiem", "Ka Shad Nongkrem"]
    },
    {
        "id": "paila",
        "name": "Ka Paila (Paila Mukmor)",
        "english_name": "Red Coral & Hollow Gold Bead Necklace",
        "gender": "both",
        "category": "jewellery",
        "body_location": "Neck / Chest",
        "materials": ["Polished cylindrical red coral beads (Muga/Mukmor)", "Hollow chased 24k gold spheres (Kba Ksiar)"],
        "design": "Alternate large red coral barrels and gleaming globular gold beads strung along thick silk cords, worn in heavy, multi-layered tiers hanging down to the waist.",
        "cultural_significance": "The most celebrated and treasured heirloom (Kynshew) of the Khasi family. Passed down strictly along the matrilineal line to Ka Khadduh (youngest daughter). Worn by both maidens and male dancers in festivals.",
        "occasions": ["All festivals", "Traditional weddings", "Clan ceremonies"]
    },
    {
        "id": "kynjri_ksiar",
        "name": "U Kynjri Ksiar",
        "english_name": "Tiered Gold Chain Necklace",
        "gender": "female",
        "category": "jewellery",
        "body_location": "Neck & Chest",
        "materials": ["22k / 24k gold"],
        "design": "Multi-strand braided gold loops with interlocking florets or mesh plates that lie flat across the upper chest.",
        "cultural_significance": "Displays family heritage, artistic metallurgy, and maternal wealth.",
        "occasions": ["Shad Suk Mynsiem", "Weddings"]
    },
    {
        "id": "kynjri_rupa",
        "name": "U Kynjri Rupa",
        "english_name": "Silver Waist Chain and Pectoral Chords",
        "gender": "both",
        "category": "jewellery",
        "body_location": "Waist / Chest",
        "materials": ["Pure silver (Rupa)"],
        "design": "Heavy hand-forged silver chains linked with decorative medallions and bells, worn by men crisscrossed over the Jymphong and around the waist.",
        "cultural_significance": "Denotes warrior dignity, protective vigor, and aristocratic pedigree in male participants.",
        "occasions": ["Shad Mastieh (Warrior dance)", "Nongkrem festival"]
    },
    {
        "id": "shanryndang",
        "name": "U Shanryndang",
        "english_name": "Filigree Gold Choker",
        "gender": "female",
        "category": "jewellery",
        "body_location": "Throat / Neck",
        "materials": ["Gold filigree", "Precious enamel inlay"],
        "design": "A rigid, hinged gold collar encircling the throat, etched with local flora such as the Tiew-ja-ngew or ginger blossom motifs.",
        "cultural_significance": "Adorns the neck of the maiden, symbolising melodic speech and grace.",
        "occasions": ["Festival dances", "Weddings"]
    },
    {
        "id": "siar_kynthei",
        "name": "Ki Siar Kynthei / Ki Khadu",
        "english_name": "Heavy Gold or Silver Forearm Cuffs",
        "gender": "female",
        "category": "jewellery",
        "body_location": "Wrists & Forearms",
        "materials": ["Solid gold", "Chased silver"],
        "design": "Heavy, broad bracelets clasping the forearms, decorated with repoussé reliefs of traditional Khasi symbols.",
        "cultural_significance": "Worn in pairs on both wrists. The metallic clinking during subtle hand movements adds rhythmic cadence to the dancer's steps.",
        "occasions": ["Ceremonial dance", "Festivals"]
    },
    {
        "id": "mahu",
        "name": "Ki Mahu (Khadu Mahu)",
        "english_name": "Warrior Armlets / Bicep Bands",
        "gender": "male",
        "category": "jewellery",
        "body_location": "Upper Arms / Biceps",
        "materials": ["Solid silver", "Gilded brass"],
        "design": "Thick circular silver armbands worn tightly around the biceps above the elbows.",
        "cultural_significance": "Ancient insignia of heroic warriors (Ki Rangbah Shynrang) ready for combat or state representation.",
        "occasions": ["Shad Mastieh", "State convocations"]
    },
    {
        "id": "ta_kora",
        "name": "Ka Ta-kora",
        "english_name": "Pectoral Silver Disc Ornament",
        "gender": "female",
        "category": "jewellery",
        "body_location": "Chest",
        "materials": ["Embossed silver", "Coral insets"],
        "design": "A large central silver disc or medallion suspended across the chest from dual silver ropes.",
        "cultural_significance": "Worn by maidens as an emblem of truth and purity.",
        "occasions": ["Shad Suk Mynsiem"]
    },
    {
        "id": "sa_shiah",
        "name": "Ki Sa-shiah / Thiah-shiah",
        "english_name": "Ornamental Gold Cloak Pins & Hairpins",
        "gender": "female",
        "category": "jewellery",
        "body_location": "Hair / Shoulders",
        "materials": ["Solid gold", "Gilded silver with gemstones"],
        "design": "Long, sharp ornamental pins crowned with three-dimensional gold blossoms, betel leaves, or peacocks, used to pin the Jainsem at the shoulders and ornament hair chignons.",
        "cultural_significance": "Combines practical garment pinning with high jewelry aesthetics.",
        "occasions": ["Everyday formal wear", "Dance festivals"]
    },
    {
        "id": "siatsngi",
        "name": "Ki Siatsngi (Ki Kpieng Shkor)",
        "english_name": "Sunburst Gold Chandelier Earrings",
        "gender": "female",
        "category": "jewellery",
        "body_location": "Ears",
        "materials": ["24k yellow gold"],
        "design": "Elaborate earrings depicting radiant sunbursts (Ka Sngi) with hanging fringe drops and tiny filigree bells.",
        "cultural_significance": "Honors Ka Sngi (the Sun Goddess, feminine in Khasi cosmology), acknowledging her as the mother of light and life.",
        "occasions": ["Festivals", "Weddings"]
    },
    {
        "id": "kynjri_tabah",
        "name": "U Kynjri Tabah",
        "english_name": "Ornamental Silver Waistband",
        "gender": "both",
        "category": "jewellery",
        "body_location": "Waist",
        "materials": ["Interlinked sterling silver loops"],
        "design": "A flexible mesh sash wrapped around the waist to anchor draped garments and swords.",
        "cultural_significance": "Secures male dhotis and swords during martial maneuvers.",
        "occasions": ["Festivals", "Ceremonies"]
    }
]

REGALIA_AND_WEAPONS: List[Dict[str, Any]] = [
    {
        "id": "waitlam",
        "name": "Ka Waitlam",
        "english_name": "Two-Handed Ceremonial Broadsword",
        "category": "regalia_weapon",
        "wielder": "Male dancers, warriors, and chieftains",
        "materials": ["Tempered carbon steel", "Silver-wound hilt", "Brass guard"],
        "description": "A long, straight indigenous Khasi steel sword held in the right hand during the warrior dance (Shad Mastieh). Wielded aloft with fluid circular sweeps that slice through the air in time with the war drums.",
        "cultural_significance": "Symbolizes the duty of the Khasi male to defend women, clan hearths, land borders, and ancestral honor.",
        "occasions": ["Shad Mastieh", "Shad Suk Mynsiem", "Funeral of royal chieftains"]
    },
    {
        "id": "stieh",
        "name": "Ka Stieh",
        "english_name": "Embossed Silver or Brass Shield",
        "category": "regalia_weapon",
        "wielder": "Male dancers and warriors",
        "materials": ["Embossed brass", "Sterling silver plate", "Wood core"],
        "description": "A circular shield held in the left hand, adorned with sunburst or concentric repoussé rings. Clashed rhythmically against swords during combat demonstrations.",
        "cultural_significance": "Represents spiritual and physical defense, warding off malevolent unseen forces and mortal adversaries.",
        "occasions": ["Shad Mastieh", "Nongkrem dance"]
    },
    {
        "id": "symphiah",
        "name": "U Symphiah",
        "english_name": "Ceremonial Yak-Tail / Goat-Hair Whisk",
        "category": "regalia_accessory",
        "wielder": "Male ceremonial dancers",
        "materials": ["White or black yak tail / long goat hair", "Silver-chased wooden handle"],
        "description": "A sacred whisk held in the left or right hand by male dancers, rhythmically waved in sweeping arcs over the dancing maidens.",
        "cultural_significance": "Carried to sweep away evil spirits, uncleanness, and misfortune from the sacred dancing ring (Lympung), blessing the maidens dancing peacefully at the center.",
        "occasions": ["Shad Suk Mynsiem", "Ka Shad Nongkrem"]
    },
    {
        "id": "ryntieh_bad_khnam",
        "name": "Ka Ryntieh bad Ki Khnam",
        "english_name": "Bamboo Recurve Bow & Iron-Tipped Arrows",
        "category": "regalia_weapon",
        "wielder": "Khasi archers, hunters, and elders",
        "materials": ["Cured mountain bamboo (Shken / Siej)", "Feather fletching", "Hand-forged iron arrowheads (Sop-khnam)"],
        "description": "The quintessential weapon of the Khasi. Three consecrated arrows are placed beside every newborn baby boy at birth, denoting defense of homeland, defense of maternal clan, and sovereignty under God.",
        "cultural_significance": "Archery is the national sport and sacred martial art of the Khasi people. Used in divination, border defense, and festive competitions (Ka Siat Khnam).",
        "occasions": ["Ka Jer Ka Thoh (Naming rite)", "Ka Siat Khnam", "Coronation rites"]
    },
    {
        "id": "wait_bnoh",
        "name": "Ka Wait-bnoh",
        "english_name": "Hooked Billhook Knife",
        "category": "regalia_tool",
        "wielder": "Khasi elders, hunters, and woodsmen",
        "materials": ["Forged steel blade with curved beak", "Wood / bamboo handle"],
        "description": "A heavy, multi-purpose curved chopper featuring a recurved beak. Used for cutting trails through rainforests, harvesting bamboo, and defensive close-quarter combat.",
        "cultural_significance": "An indispensable everyday companion of the highland woodsman and an ancient symbol of pragmatic resilience.",
        "occasions": ["Highland travel", "Forest clearing", "Sacred grove maintenance"]
    },
    {
        "id": "pah_wait",
        "name": "Ka Pah-wait",
        "english_name": "Ornamental Sword Scabbard & Baldric",
        "category": "regalia_accessory",
        "wielder": "Male warriors and dignitaries",
        "materials": ["Chased silver sheath", "Embossed leather strap", "Gilt rings"],
        "description": "An elaborately decorated scabbard housing the Waitlam sword, slung across the right shoulder over the Jymphong.",
        "cultural_significance": "Completes the formal ceremonial battle regalia of a Khasi nobleman.",
        "occasions": ["State convocations", "Processions"]
    }
]

# Master aggregate list
ALL_ATTIRE: List[Dict[str, Any]] = (
    TRADITIONAL_GARMENTS +
    TEXTILES_AND_FABRICS +
    JEWELLERY_AND_ORNAMENTS +
    REGALIA_AND_WEAPONS
)

def list_garments(gender: Optional[str] = None) -> List[Dict[str, Any]]:
    """Return traditional garments, optionally filtered by gender ('female', 'male')."""
    if not gender:
        return TRADITIONAL_GARMENTS
    g = gender.lower().strip()
    return [item for item in TRADITIONAL_GARMENTS if item.get("gender") in (g, "both")]

def get_garment(query: str) -> Optional[Dict[str, Any]]:
    """Find a traditional garment by Khasi or English name or identifier."""
    q = query.lower().strip()
    for item in TRADITIONAL_GARMENTS:
        if (q == item["id"] or
            q in item["name"].lower() or
            q in item["english_name"].lower()):
            return item
    return None

def list_jewellery(gender: Optional[str] = None) -> List[Dict[str, Any]]:
    """Return traditional jewellery and ornaments, optionally filtered by gender."""
    if not gender:
        return JEWELLERY_AND_ORNAMENTS
    g = gender.lower().strip()
    return [item for item in JEWELLERY_AND_ORNAMENTS if item.get("gender") in (g, "both")]

def get_jewellery(query: str) -> Optional[Dict[str, Any]]:
    """Find jewellery by Khasi or English name or identifier."""
    q = query.lower().strip()
    for item in JEWELLERY_AND_ORNAMENTS:
        if (q == item["id"] or
            q in item["name"].lower() or
            q in item["english_name"].lower()):
            return item
    return None

def list_fabrics() -> List[Dict[str, Any]]:
    """Return traditional Khasi handloom textiles and fabrics."""
    return TEXTILES_AND_FABRICS

def get_fabric(query: str) -> Optional[Dict[str, Any]]:
    """Find a textile or fabric by name or identifier."""
    q = query.lower().strip()
    for item in TEXTILES_AND_FABRICS:
        if (q == item["id"] or
            q in item["name"].lower() or
            q in item["english_name"].lower()):
            return item
    return None

def list_regalia() -> List[Dict[str, Any]]:
    """Return traditional martial dance regalia, accessories, and weapons."""
    return REGALIA_AND_WEAPONS

def get_regalia(query: str) -> Optional[Dict[str, Any]]:
    """Find regalia or weapon by name or identifier."""
    q = query.lower().strip()
    for item in REGALIA_AND_WEAPONS:
        if (q == item["id"] or
            q in item["name"].lower() or
            q in item["english_name"].lower()):
            return item
    return None

def search_attire(query: str) -> List[Dict[str, Any]]:
    """Search across all garments, fabrics, jewellery, and regalia."""
    q = query.lower().strip()
    matches = []
    for item in ALL_ATTIRE:
        searchable_text = " ".join([
            item.get("id", ""),
            item.get("name", ""),
            item.get("english_name", ""),
            item.get("description", ""),
            item.get("cultural_significance", ""),
            " ".join(item.get("occasions", [])),
            " ".join(item.get("materials", []))
        ]).lower()
        if q in searchable_text:
            matches.append(item)
    return matches

def list_all_attire() -> List[Dict[str, Any]]:
    """Return complete list of all traditional attire, jewellery, fabrics, and regalia."""
    return ALL_ATTIRE

class AttireManager:
    """Convenience class for managing Khasi attire, jewellery, textiles, and regalia."""

    @property
    def garments(self) -> List[Dict[str, Any]]:
        return TRADITIONAL_GARMENTS

    @property
    def jewellery(self) -> List[Dict[str, Any]]:
        return JEWELLERY_AND_ORNAMENTS

    @property
    def fabrics(self) -> List[Dict[str, Any]]:
        return TEXTILES_AND_FABRICS

    @property
    def regalia(self) -> List[Dict[str, Any]]:
        return REGALIA_AND_WEAPONS

    @property
    def all_items(self) -> List[Dict[str, Any]]:
        return ALL_ATTIRE

    def get(self, query: str) -> Optional[Dict[str, Any]]:
        for item in ALL_ATTIRE:
            if (query.lower().strip() == item["id"] or
                query.lower().strip() in item["name"].lower() or
                query.lower().strip() in item["english_name"].lower()):
                return item
        return None

    def search(self, query: str) -> List[Dict[str, Any]]:
        return search_attire(query)

    def by_gender(self, gender: str) -> List[Dict[str, Any]]:
        g = gender.lower().strip()
        return [item for item in ALL_ATTIRE if item.get("gender") in (g, "both")]

attire = AttireManager()
