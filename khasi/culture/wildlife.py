# -*- coding: utf-8 -*-
"""
Khasi Wildlife, Zoology, and Highland Fauna.
Comprehensive documentation of native mammals, birds, fish, reptiles, and insects
with binomial scientific names, habitats, and cultural/folklore significance.
"""

from typing import Dict, List, Any, Optional

WILDLIFE: List[Dict[str, Any]] = [
    {
        "khasi_name": "U Khla-lyngngoh",
        "common_name": "Clouded Leopard",
        "scientific_name": "Neofelis nebulosa",
        "class_type": "Mammal",
        "status": "Vulnerable / State Animal of Meghalaya",
        "habitat": "Dense evergreen rainforests and sacred groves",
        "cultural_significance": "State animal of Meghalaya; revered as an agile master of the tree canopies and guardian of the deep mountain ravines."
    },
    {
        "khasi_name": "U Khla",
        "common_name": "Royal Bengal Tiger",
        "scientific_name": "Panthera tigris",
        "class_type": "Mammal",
        "status": "Endangered",
        "habitat": "Historically roamed deep gorges; remembered in oral lore",
        "cultural_significance": "King of the wild beasts in folklore. Surrounded by deep taboos; killing a tiger required sacred appeasement ceremonies ('Ka Shad Rongkhli')."
    },
    {
        "khasi_name": "U Sier",
        "common_name": "Sambar Deer / Highland Stag",
        "scientific_name": "Rusa unicolor",
        "class_type": "Mammal",
        "status": "Vulnerable",
        "habitat": "Highland pine hills and mixed broadleaf forests",
        "cultural_significance": "Protagonist of the tragic epic 'U Sier Lapalang'; symbol of filial affection and maternal sorrow."
    },
    {
        "khasi_name": "U Dngiem",
        "common_name": "Asiatic Black Bear / Moon Bear",
        "scientific_name": "Ursus thibetanus",
        "class_type": "Mammal",
        "status": "Vulnerable",
        "habitat": "Temperate mountain forests and rhododendron thickets",
        "cultural_significance": "Feature of humorous and cautionary fireside folktales depicting his strength, love of mountain honey, and clumsy wit."
    },
    {
        "khasi_name": "U Hati",
        "common_name": "Asian Elephant",
        "scientific_name": "Elephas maximus",
        "class_type": "Mammal",
        "status": "Endangered",
        "habitat": "Subtropical bamboo forests in Ri-Bhoi and Garo boundary",
        "cultural_significance": "Symbol of majestic royal power; migration paths respected as ancient nature corridors."
    },
    {
        "khasi_name": "U Shrieh",
        "common_name": "Hoolock Gibbon",
        "scientific_name": "Hoolock hoolock",
        "class_type": "Mammal",
        "status": "Endangered (Only ape in India)",
        "habitat": "Dense upper canopy of tropical evergreen forests",
        "cultural_significance": "Vocal canopy acrobat whose morning calls echo across river valleys; depicted in folklore as an agile trickster."
    },
    {
        "khasi_name": "U Khnai-kba",
        "common_name": "Bamboo Rat",
        "scientific_name": "Cannomys badius",
        "class_type": "Mammal",
        "status": "Least Concern",
        "habitat": "Highland bamboo groves and burrows",
        "cultural_significance": "Associated with cyclical bamboo flowering (Mautam); indicator of forest ecological cycles."
    },
    {
        "khasi_name": "U Kohkarang",
        "common_name": "Great Indian Hornbill",
        "scientific_name": "Buceros bicornis",
        "class_type": "Bird",
        "status": "Vulnerable",
        "habitat": "Tall emergent rainforest trees in river canyons",
        "cultural_significance": "Sacred forest bird, admired for loyalty and lifelong fidelity; its wings and feathers historically adorned warrior headgear."
    },
    {
        "khasi_name": "U Klew",
        "common_name": "Indian Peafowl / Peacock",
        "scientific_name": "Pavo cristatus",
        "class_type": "Bird",
        "status": "Least Concern",
        "habitat": "Forest fringes and foothill valleys",
        "cultural_significance": "Hero of the celestial romance 'U Klew bad ka Sngi'; its shimmering iridescent plumage earned by staring toward the Sun maiden."
    },
    {
        "khasi_name": "Ka Sim-pyllieng",
        "common_name": "Oriental Magpie-Robin",
        "scientific_name": "Copsychus saularis",
        "class_type": "Bird",
        "status": "Least Concern",
        "habitat": "Highland gardens, village orchards, and open woods",
        "cultural_significance": "Beloved songbird of the dawn; its sweet morning trills historically awakened farmers to their honest daily labor."
    },
    {
        "khasi_name": "U Syiar",
        "common_name": "Indigenous Rooster / Cock",
        "scientific_name": "Gallus gallus domesticus",
        "class_type": "Bird",
        "status": "Domesticated / Cultural Sacred Emblem",
        "habitat": "Khasi households throughout the hills",
        "cultural_significance": "Sacred mediator in ancient mythology ('U Syiar uba bsa ia ka Pyrthei'); coaxed the Sun out of Krem Lamet Latang; vital in divination ('Shat Syiar')."
    },
    {
        "khasi_name": "U Tyngab",
        "common_name": "House Crow / Large-billed Crow",
        "scientific_name": "Corvus macrorhynchos",
        "class_type": "Bird",
        "status": "Least Concern",
        "habitat": "Settlements and open hill clearings",
        "cultural_significance": "Featured in Khasi creation fables; messenger bird whose calls were interpreted as weather and guest omens."
    },
    {
        "khasi_name": "Ka Sim-phreit",
        "common_name": "White-rumped Munia / Little Wren",
        "scientific_name": "Lonchura striata",
        "class_type": "Bird",
        "status": "Least Concern",
        "habitat": "Grasslands, terraced paddy fields, and scrub",
        "cultural_significance": "The humble mountain bird in the epic of Mount Diengiei that revealed the secret to felling the giant Tree of Darkness."
    },
    {
        "khasi_name": "U Kha-saw",
        "common_name": "Golden Mahseer",
        "scientific_name": "Tor putitora",
        "class_type": "Fish",
        "status": "Endangered",
        "habitat": "Crystal-clear rapid highland rivers (Wah Umngot, Wah Kynshi)",
        "cultural_significance": "Prized king of river fish, revered for swiftness and strength in fighting roaring white-water currents."
    },
    {
        "khasi_name": "Ka Dohkha-shalang",
        "common_name": "Zebrafish / Mountain Danio",
        "scientific_name": "Danio dangila / Danio rerio",
        "class_type": "Fish",
        "status": "Least Concern",
        "habitat": "Pebbled hill streams and clean waterfall pools",
        "cultural_significance": "Abundant small river fish caught using traditional conical wicker traps ('Khur') for fresh and smoked delicacies."
    },
    {
        "khasi_name": "U Bsein-thlen",
        "common_name": "Burmese Rock Python",
        "scientific_name": "Python bivittatus",
        "class_type": "Reptile",
        "status": "Vulnerable",
        "habitat": "Limestone karst caves and moist evergreen forests",
        "cultural_significance": "Zoological basis for the mythical monster 'U Thlen'; allegory of avarice, evil, and righteous human solidarity."
    },
    {
        "khasi_name": "U Bsein-khla",
        "common_name": "King Cobra",
        "scientific_name": "Ophiophagus hannah",
        "class_type": "Reptile",
        "status": "Vulnerable",
        "habitat": "Southern rainforest gorges and dense bamboo stands",
        "cultural_significance": "Revered with solemn fear as the king of serpents; traditionally avoided and treated with prayerful distance."
    },
    {
        "khasi_name": "U Bsein-iap-ngan",
        "common_name": "Monocled Cobra",
        "scientific_name": "Naja kaouthia",
        "class_type": "Reptile",
        "status": "Least Concern",
        "habitat": "Agricultural margins, lowland terraces, and stone piles",
        "cultural_significance": "Venomous snake featured in warnings of traditional medicine men and hunters."
    },
    {
        "khasi_name": "Ka Jakoid",
        "common_name": "Khasi Hills Rock Toad",
        "scientific_name": "Bufoides meghalayanus",
        "class_type": "Amphibian",
        "status": "Endangered (Endemic)",
        "habitat": "Mossy rocks, mountain torrents, and plateau caves",
        "cultural_significance": "Endemic rock toad found nowhere else on earth; indicator of pristine highland water health."
    },
    {
        "khasi_name": "Ka Ngap",
        "common_name": "Himalayan Honeybee",
        "scientific_name": "Apis cerana himalaya",
        "class_type": "Insect",
        "status": "Beneficial Pollinator",
        "habitat": "Hollow trees, cliffs, and traditional log hives",
        "cultural_significance": "Producer of prized rock honey ('Ngab-maw') and wild blossom honey, vital for Khasi mountain remedies and sweetening."
    },
    {
        "khasi_name": "U Niang-ryndia",
        "common_name": "Eri Silkworm",
        "scientific_name": "Samia cynthia ricini",
        "class_type": "Insect",
        "status": "Beneficial Sericulture Species",
        "habitat": "Fed on castor leaves across Ri-Bhoi district",
        "cultural_significance": "Producer of indigenous peace silk (Ryndia); worms are not boiled alive; hand-spun into heirloom warm shawls."
    },
    {
        "khasi_name": "U Niang-muga",
        "common_name": "Muga Golden Silkworm",
        "scientific_name": "Antheraea assamensis",
        "class_type": "Insect",
        "status": "Geographical Indication Species",
        "habitat": "Fed on wild aromatic laurel trees in warm valleys",
        "cultural_significance": "Produces the golden thread woven into the regal Dhara costumes worn in Shad Suk Mynsiem."
    }
]

def list_wildlife() -> List[Dict[str, Any]]:
    """Return all documented Khasi wildlife species."""
    return WILDLIFE

def get_animal(query: str) -> Optional[Dict[str, Any]]:
    """Find wildlife species by Khasi name, scientific name, or common name."""
    q = query.lower().strip()
    for a in WILDLIFE:
        if (q in a["khasi_name"].lower() or 
            q in a["scientific_name"].lower() or 
            q in a["common_name"].lower() or
            q in a["class_type"].lower()):
            return a
    return None

def by_class(class_type: str) -> List[Dict[str, Any]]:
    """Filter wildlife by class (e.g. 'Mammal', 'Bird', 'Fish', 'Reptile', 'Amphibian', 'Insect')."""
    ct = class_type.lower().strip()
    return [a for a in WILDLIFE if ct in a["class_type"].lower()]
