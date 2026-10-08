# -*- coding: utf-8 -*-
"""
Khasi Botanical Knowledge & Ethnomedicinal Flora of Meghalaya.
Comprehensive database of indigenous trees, wild fruits, medicinal herbs, and sacred plants
with binomial scientific names, botanical families, and cultural applications.
"""

from typing import Dict, List, Any, Optional

PLANTS: List[Dict[str, Any]] = [
    {
        "khasi_name": "Tiew-rakot / Kynbat-khlieng",
        "common_name": "Khasi Pitcher Plant",
        "scientific_name": "Nepenthes khasiana",
        "family": "Nepenthaceae",
        "type": "Insectivorous Climber / Herb",
        "cultural_use": "Medicinal (fluid inside unopened pitcher used for eye ailments, skin infections, diabetes; taboo to destroy)",
        "habitat": "Endemic to Meghalaya; South Khasi Hills and Jaintia sandstone ridges",
        "conservation": "Endangered / Schedule I Protected"
    },
    {
        "khasi_name": "Sohiong",
        "common_name": "Khasi Black Cherry",
        "scientific_name": "Prunus nepalensis",
        "family": "Rosaceae",
        "type": "Deciduous Mountain Tree",
        "cultural_use": "Culinary (edible dark purple-black fruit eaten fresh, made into famous Khasi wine, jams, and medicinal astringent syrups)",
        "habitat": "Highland forests across East & West Khasi Hills (1,500m - 2,000m)",
        "conservation": "Indigenous fruit crop"
    },
    {
        "khasi_name": "Sohphie",
        "common_name": "Wild Box Myrtle",
        "scientific_name": "Myrica esculenta",
        "family": "Myricaceae",
        "type": "Sub-tropical Evergreen Tree",
        "cultural_use": "Culinary & Medicinal (tart sweet-sour wild fruit loved by children and sold in markets; bark decoction used for stomach disorders and fevers)",
        "habitat": "Khasi pine forests and ridge margins",
        "conservation": "Common wild fruit"
    },
    {
        "khasi_name": "Sohshang",
        "common_name": "Bastard Oleaster / Wild Olive",
        "scientific_name": "Elaeagnus latifolia",
        "family": "Elaeagnaceae",
        "type": "Woody Climbing Shrub",
        "cultural_use": "Culinary (bright pinkish-red tart fruit eaten raw with rock salt and chili; high in Vitamin C and antioxidants)",
        "habitat": "Scrub forests and village margins across Khasi Hills",
        "conservation": "Cultivated and wild"
    },
    {
        "khasi_name": "Ja-myrdoh",
        "common_name": "Fish Mint / Chameleon Plant",
        "scientific_name": "Houttuynia cordata",
        "family": "Saururaceae",
        "type": "Perennial Rhizomatous Herb",
        "cultural_use": "Culinary & Medicinal (staple salad herb eaten raw with fermented fish and onions; potent antiviral, antibacterial, and digestive aid)",
        "habitat": "Damp moist valleys, riverbanks, and kitchen garden borders",
        "conservation": "Cultivated & wild"
    },
    {
        "khasi_name": "Bat-khliang-syiar",
        "common_name": "Indian Pennywort / Gotu Kola",
        "scientific_name": "Centella asiatica",
        "family": "Apiaceae",
        "type": "Creeping Perennial Herb",
        "cultural_use": "Medicinal (leaf juice taken as brain memory tonic, wound healing poultice, liver protector, and cure for infant fevers)",
        "habitat": "Moist soil, grassy stream banks, and meadows",
        "conservation": "Common wild herb"
    },
    {
        "khasi_name": "Jarem",
        "common_name": "Clerodendrum Shrub",
        "scientific_name": "Clerodendrum colebrookianum",
        "family": "Lamiaceae",
        "type": "Evergreen Shrub",
        "cultural_use": "Medicinal (tender leaves boiled and eaten as soup; highly valued throughout Khasi society for lowering high blood pressure)",
        "habitat": "Sub-tropical forest undergrowth and moist valleys",
        "conservation": "Wild and domestic gardens"
    },
    {
        "khasi_name": "Jarain",
        "common_name": "Wild Buckwheat Greens",
        "scientific_name": "Fagopyrum esculentum",
        "family": "Polygonaceae",
        "type": "Annual Herb",
        "cultural_use": "Culinary & Medicinal (sour leaves cooked as nutritious broth; traditionally consumed for hypertension and kidney cleansing)",
        "habitat": "Terraced fields and high altitude clearings",
        "conservation": "Semi-cultivated"
    },
    {
        "khasi_name": "U Bet",
        "common_name": "Sweet Flag / Calamus",
        "scientific_name": "Acorus calamus",
        "family": "Acoraceae",
        "type": "Aromatic Wetland Herb",
        "cultural_use": "Medicinal (aromatic root chewed for coughs, voice clarity, influenza, and bone fracture healing pastes)",
        "habitat": "Marshy wetlands and highland stream edges",
        "conservation": "Ethnomedicinal herb"
    },
    {
        "khasi_name": "Ïing-shmoh",
        "common_name": "Aromatic Ginger / Peacock Ginger",
        "scientific_name": "Kaempferia rotunda",
        "family": "Zingiberaceae",
        "type": "Rhizomatous Herb",
        "cultural_use": "Medicinal (pounded rhizomes used in traditional bone-setting pastes and poultices for swollen sprains and respiratory fever)",
        "habitat": "Moist humus-rich slopes",
        "conservation": "Wild herb"
    },
    {
        "khasi_name": "Bat-bsein",
        "common_name": "Paris Rhizome / Love Apple",
        "scientific_name": "Paris polyphylla",
        "family": "Melanthiaceae",
        "type": "Perennial Woodland Herb",
        "cultural_use": "Medicinal (rhizome applied for venomous snakebites, severe burns, and internal anti-inflammatory detoxification)",
        "habitat": "Shady temperate forests and sacred groves",
        "conservation": "Vulnerable due to overharvesting"
    },
    {
        "khasi_name": "Rhoi",
        "common_name": "Indian Madder",
        "scientific_name": "Rubia cordifolia",
        "family": "Rubiaceae",
        "type": "Climbing Perennial Herb",
        "cultural_use": "Textile Dye & Medicinal (red roots boiled to produce rich natural scarlet dye for traditional Ryndia silk; treated for skin ulcers)",
        "habitat": "Hilly terrain and secondary forest clearings",
        "conservation": "Wild dye plant"
    },
    {
        "khasi_name": "Bat sma-iwtung",
        "common_name": "Crofton Weed / Ageratina",
        "scientific_name": "Eupatorium adenophorum",
        "family": "Asteraceae",
        "type": "Perennial Shrub",
        "cultural_use": "First Aid (fresh crushed leaves applied directly to fresh cuts to instantly stop heavy bleeding and prevent infection)",
        "habitat": "Roadside slopes, waste ground, and fallow hills",
        "conservation": "Abundant"
    },
    {
        "khasi_name": "Kynbat samthiah",
        "common_name": "Sensitive Plant / Touch-Me-Not",
        "scientific_name": "Mimosa pudica",
        "family": "Fabaceae",
        "type": "Creeping Thorny Herb",
        "cultural_use": "Medicinal (root decoction given for jaundice, urinary tract disorders, and skin rashes)",
        "habitat": "Open sunny meadows and low hills",
        "conservation": "Common"
    },
    {
        "khasi_name": "Dieng-titkongling",
        "common_name": "Midnight Horror / Indian Trumpet Flower",
        "scientific_name": "Oroxylum indicum",
        "family": "Bignoniaceae",
        "type": "Deciduous Small Tree",
        "cultural_use": "Medicinal (bitter root bark brewed for severe diarrhea, dysentery, and rheumatic joint pain)",
        "habitat": "Lower hill slopes and subtropical ravines",
        "conservation": "Wild medicinal tree"
    },
    {
        "khasi_name": "Dieng-ksew",
        "common_name": "Khasi Pine",
        "scientific_name": "Pinus kesiya",
        "family": "Pinaceae",
        "type": "Tall Evergreen Conifer",
        "cultural_use": "Ecological & Material (dominant pine shaping the landscape of Shillong plateau; high quality timber, resin, firewood, and pine needle mulch)",
        "habitat": "Extensive natural and managed forests (1,000m - 1,800m)",
        "conservation": "Keystone species"
    },
    {
        "khasi_name": "Dieng-jri",
        "common_name": "Indian Rubber Fig",
        "scientific_name": "Ficus elastica",
        "family": "Moraceae",
        "type": "Monumental Epiphytic / Terrestrial Fig",
        "cultural_use": "Living Architecture (aerial roots trained through hollowed betel trunks across rivers to engineer living root bridges, Jingkieng Jri)",
        "habitat": "Southern rainforest gorges and steep valleys of Sohra, Mawlynnong, and Pynursla",
        "conservation": "Sacred community heritage"
    },
    {
        "khasi_name": "Dieng-blei",
        "common_name": "Sacred Himalayan Yew",
        "scientific_name": "Taxus wallichiana",
        "family": "Taxaceae",
        "type": "Slow-growing Evergreen Tree",
        "cultural_use": "Sacred & Medicinal (revered in sacred groves as an ancestral tree; source of anti-cancer compound paclitaxel)",
        "habitat": "Preserved exclusively in virgin Law Kyntang sacred groves",
        "conservation": "Endangered"
    },
    {
        "khasi_name": "Dieng-sohot",
        "common_name": "Khasi Chestnut",
        "scientific_name": "Castanopsis indica",
        "family": "Fagaceae",
        "type": "Hardwood Canopy Tree",
        "cultural_use": "Culinary & Material (edible wild sweet chestnuts gathered and roasted in winter; durable timber for house frames)",
        "habitat": "Subtropical mixed broadleaf forests",
        "conservation": "Indigenous forest species"
    },
    {
        "khasi_name": "U Siej / U Shken",
        "common_name": "Giant Hill Bamboo",
        "scientific_name": "Dendrocalamus hamiltonii",
        "family": "Poaceae",
        "type": "Arborescent Giant Bamboo",
        "cultural_use": "Material & Culinary (backbone of Khasi material culture: water conduits, house walls, Khoh backpacks, and edible fermented shoots, Lung-siej)",
        "habitat": "Highland slopes and ravines",
        "conservation": "Staple resource"
    },
    {
        "khasi_name": "Shynrai Lakadong",
        "common_name": "Lakadong Turmeric",
        "scientific_name": "Curcuma longa var. Lakadong",
        "family": "Zingiberaceae",
        "type": "Perennial Rhizomatous Herb",
        "cultural_use": "Culinary & Medicinal (world-renowned heirloom turmeric with unprecedented 7-12% curcumin; gives Ja Stem rice its brilliant golden hue)",
        "habitat": "Lakadong plateau, Jaintia Hills",
        "conservation": "Geographical Indication (GI) protected"
    },
    {
        "khasi_name": "Kwai",
        "common_name": "Areca Nut / Betel Nut Palm",
        "scientific_name": "Areca catechu",
        "family": "Arecaceae",
        "type": "Slender Feather Palm",
        "cultural_use": "Social & Ritual (central emblem of Khasi hospitality; offered to every guest alongside betel leaf; vital in all formal greetings)",
        "habitat": "Cultivated extensively on southern slopes (Ri War)",
        "conservation": "Primary cash crop"
    },
    {
        "khasi_name": "Tympew",
        "common_name": "Betel Vine Leaf",
        "scientific_name": "Piper betle",
        "family": "Piperaceae",
        "type": "Aromatic Evergreen Climber",
        "cultural_use": "Social & Ritual (paired with Kwai nut and lime in everyday Khasi social communion and marriage rites)",
        "habitat": "Warm southern slopes trained around betel and jackfruit trunks",
        "conservation": "Primary crop"
    },
    {
        "khasi_name": "Tiew-japang",
        "common_name": "Lady's Slipper Orchid",
        "scientific_name": "Paphiopedilum insigne",
        "family": "Orchidaceae",
        "type": "Terrestrial & Lithophytic Orchid",
        "cultural_use": "Aesthetic & Ecological (prized endemic jewel of the limestone crevices of Sohra; cultural symbol of pristine highland beauty)",
        "habitat": "Shady limestone and sandstone crags",
        "conservation": "CITES Appendix I Protected"
    },
    {
        "khasi_name": "Tiew-saw",
        "common_name": "Tree Rhododendron",
        "scientific_name": "Rhododendron arboreum",
        "family": "Ericaceae",
        "type": "Small Flowering Tree",
        "cultural_use": "Ornamental & Cultural (crimson spring blossoms herald the arrival of spring, Aïom Pyrem, and the Shad Suk Mynsiem season)",
        "habitat": "High mountain crests and ridges (1,500m - 2,000m)",
        "conservation": "Wild mountain flora"
    },
    {
        "khasi_name": "Sohkynphor",
        "common_name": "Khasi Mandarin Orange",
        "scientific_name": "Citrus reticulata / Citrus latipes",
        "family": "Rutaceae",
        "type": "Evergreen Citrus Tree",
        "cultural_use": "Culinary (legendary sweet-sour Cherrapunji/Sohra mandarin orange celebrated throughout Northeast India; GI registered)",
        "habitat": "Southern sun-drenched hill slopes",
        "conservation": "GI Tagged heritage fruit"
    },
    {
        "khasi_name": "Sohshur",
        "common_name": "Wild Himalayan Pear",
        "scientific_name": "Pyrus pashia",
        "family": "Rosaceae",
        "type": "Medium Deciduous Tree",
        "cultural_use": "Culinary (small sweet bletted fruit gathered in late autumn; rootstock for mountain grafting)",
        "habitat": "Temperate woodland borders",
        "conservation": "Wild fruit"
    },
    {
        "khasi_name": "Sohkhawïong",
        "common_name": "Golden Himalayan Raspberry",
        "scientific_name": "Rubus ellipticus",
        "family": "Rosaceae",
        "type": "Prickly Shrub",
        "cultural_use": "Culinary & Medicinal (succulent golden-yellow wild berries gathered in spring; root bark chewed for colic)",
        "habitat": "Sunny slopes and forest edges",
        "conservation": "Abundant wild fruit"
    },
    {
        "khasi_name": "Dieng-sohkymphor",
        "common_name": "Khasi Papeda Wild Citrus",
        "scientific_name": "Citrus latipes",
        "family": "Rutaceae",
        "type": "Wild Spiny Tree",
        "cultural_use": "Medicinal & Folk (fragrant wild citrus species native exclusively to Khasi hills; utilized in traditional fever tonics)",
        "habitat": "Highland evergreen rainforests",
        "conservation": "Rare endemic citrus"
    },
    {
        "khasi_name": "Sohlang ksew",
        "common_name": "Wild Red Berry Shrub",
        "scientific_name": "Viburnum foetidum",
        "family": "Adoxaceae",
        "type": "Evergreen Shrub",
        "cultural_use": "Medicinal (leaves and berries possess potent antioxidant and anti-hypertensive properties; uterine sedative)",
        "habitat": "Hill forests of East Khasi Hills",
        "conservation": "Ethnomedicinal shrub"
    }
]

def list_plants() -> List[Dict[str, Any]]:
    """Return all documented Khasi botanical species."""
    return PLANTS

def get_plant(query: str) -> Optional[Dict[str, Any]]:
    """Find plant by Khasi name, scientific name, or common name."""
    q = query.lower().strip()
    for p in PLANTS:
        if (q in p["khasi_name"].lower() or 
            q in p["scientific_name"].lower() or 
            q in p["common_name"].lower() or
            q in p["family"].lower()):
            return p
    return None

def by_plant_type(ptype: str) -> List[Dict[str, Any]]:
    """Filter plants by type (e.g. 'Tree', 'Herb', 'Shrub', 'Fruit', 'Insectivorous')."""
    pt = ptype.lower().strip()
    return [p for p in PLANTS if pt in p["type"].lower()]

def medicinal_plants() -> List[Dict[str, Any]]:
    """Return all plants with documented traditional medicinal uses."""
    return [p for p in PLANTS if "medicinal" in p["cultural_use"].lower() or "poultice" in p["cultural_use"].lower()]
