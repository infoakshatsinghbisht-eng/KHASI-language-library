# -*- coding: utf-8 -*-
"""
Khasi Botanical Knowledge & Ethnomedicinal Flora of Meghalaya.
Comprehensive database of indigenous trees, wild fruits, medicinal herbs, sacred grove plants,
orchids, bamboos, canes, and edible mushrooms with binomial scientific names, botanical families,
and cultural applications.
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
        "khasi_name": "Sohphlang",
        "common_name": "Khasi Root Tuber",
        "scientific_name": "Flemingia vestita",
        "family": "Fabaceae",
        "type": "Leguminous Herbaceous Tuber",
        "cultural_use": "Culinary & Anthelmintic (sweet crunchy root peeled and eaten raw with toasted perilla seeds 'Nei-lieh'; scientifically proven vermifuge against flatworms)",
        "habitat": "Highland slopes of East and West Khasi Hills",
        "conservation": "Locally domesticated"
    },
    {
        "khasi_name": "Dieng-kseh",
        "common_name": "Khasi Pine",
        "scientific_name": "Pinus kesiya",
        "family": "Pinaceae",
        "type": "Coniferous Evergreen Tree",
        "cultural_use": "Timber, resin, and cultural landscape marker; resinous heartwood ('kseh') used as traditional torchlight and hearth starter",
        "habitat": "Dominant canopy tree of the Khasi and Jaintia uplands (800m - 2,000m)",
        "conservation": "Abundant indigenous conifer"
    },
    {
        "khasi_name": "Dieng-sning",
        "common_name": "Khasi Highland Oak",
        "scientific_name": "Quercus serrata",
        "family": "Fagaceae",
        "type": "Hardwood Canopy Tree",
        "cultural_use": "Keystone species in sacred groves (Law Kyntang); provides sacred firewood for sacrificial rites and acorn forage",
        "habitat": "Sacred groves, climax cloud forests",
        "conservation": "Culturally protected"
    },
    {
        "khasi_name": "Dieng-soh-manir / Sla-tyrkang",
        "common_name": "Indian Bay Leaf / Malabathrum",
        "scientific_name": "Cinnamomum tamala",
        "family": "Lauraceae",
        "type": "Sub-tropical Tree",
        "cultural_use": "Aromatic spice and cash crop; leaves dried for culinary seasoning and bark used for traditional tonics",
        "habitat": "Southern slopes of Khasi and Jaintia Hills",
        "conservation": "Major agroforestry crop"
    },
    {
        "khasi_name": "Dieng-raishan",
        "common_name": "Tree Rhododendron",
        "scientific_name": "Rhododendron arboreum",
        "family": "Ericaceae",
        "type": "Montane Flowering Tree",
        "cultural_use": "Ornamental & Traditional (spectacular scarlet blossoms herald the Khasi spring; petals eaten in chutneys and sour curries)",
        "habitat": "High mountain ridges and peaks (Shillong Peak, Mawphlang)",
        "conservation": "Highland native"
    },
    {
        "khasi_name": "Tiew-ri-saw",
        "common_name": "Blue Vanda Orchid",
        "scientific_name": "Vanda coerulea",
        "family": "Orchidaceae",
        "type": "Epiphytic Orchid",
        "cultural_use": "Ornamental & Ethnobotanical (prized royal blue blossoms; emblem of highland floral heritage; eyedrop extract in folk remedies)",
        "habitat": "Oak and pine canopies in Khasi Hills",
        "conservation": "Endangered / CITES Appendix II"
    },
    {
        "khasi_name": "Tiew-doh-maw",
        "common_name": "Lady's Slipper Orchid",
        "scientific_name": "Paphiopedilum insigne",
        "family": "Orchidaceae",
        "type": "Lithophytic / Terrestrial Orchid",
        "cultural_use": "Traditional aesthetic admiration in folk poetry; blooms on mossy limestone cliffs",
        "habitat": "Shaded limestone gorges around Sohra and Mawlong",
        "conservation": "Threatened / Protected"
    },
    {
        "khasi_name": "Soh-mylleng",
        "common_name": "Indian Gooseberry / Amla",
        "scientific_name": "Phyllanthus emblica",
        "family": "Phyllanthaceae",
        "type": "Deciduous Tree",
        "cultural_use": "Medicinal & Culinary (eaten raw for sore throat, digestive tonic, hair wash, and liver health)",
        "habitat": "Deciduous scrub and foothills of Ri-Bhoi",
        "conservation": "Common wild & cultivated"
    },
    {
        "khasi_name": "Soh-ot",
        "common_name": "Wild Khasi Chestnut",
        "scientific_name": "Castanopsis indica",
        "family": "Fagaceae",
        "type": "Evergreen Hardwood Tree",
        "cultural_use": "Edible spiny nuts gathered in autumn, roasted on hearth embers; timber prized for tool handles",
        "habitat": "Subtropical mixed forests and sacred groves",
        "conservation": "Locally common"
    },
    {
        "khasi_name": "Soh-lyngdkhur",
        "common_name": "Himalayan Mulberry",
        "scientific_name": "Morus macroura",
        "family": "Moraceae",
        "type": "Deciduous Fruit Tree",
        "cultural_use": "Long succulent sweet berries eaten raw; foliage traditionally harvested to feed indigenous silkworms",
        "habitat": "Forest fringes and homestead orchards",
        "conservation": "Traditional fruit tree"
    },
    {
        "khasi_name": "Dieng-jri",
        "common_name": "Indian Rubber Fig (Living Root Bridge Tree)",
        "scientific_name": "Ficus elastica",
        "family": "Moraceae",
        "type": "Evergreen Epiphytic Banyan",
        "cultural_use": "Bio-engineering: Aerial roots trained across turbulent rivers by War Khasi villagers to form world-famous Living Root Bridges (Jingkieng Jri)",
        "habitat": "Steep humid subtropical valleys of southern Meghalaya",
        "conservation": "Sacred keystone species"
    },
    {
        "khasi_name": "Soh-mrit",
        "common_name": "Wild Black Pepper",
        "scientific_name": "Piper nigrum",
        "family": "Piperaceae",
        "type": "Woody Perennial Climber",
        "cultural_use": "Pungent condiment; wild berries dried as whole black peppercorns; warm infusion taken for chest coughs",
        "habitat": "Evergreen forest canopies in southern slopes",
        "conservation": "Cultivated & wild"
    },
    {
        "khasi_name": "Soh-ramdieng",
        "common_name": "Cowa Mangosteen",
        "scientific_name": "Garcinia cowa",
        "family": "Clusiaceae",
        "type": "Evergreen Forest Tree",
        "cultural_use": "Culinary & Dysentery cure: Slices of yellow sour fruit dried as souring agent for fish curries; bark decoction stops dysentery",
        "habitat": "Evergreen forests of Khasi and Jaintia foothills",
        "conservation": "Wild forest fruit"
    },
    {
        "khasi_name": "Soh-brap",
        "common_name": "Highland Passionfruit",
        "scientific_name": "Passiflora edulis",
        "family": "Passifloraceae",
        "type": "Perennial Tendril Climber",
        "cultural_use": "Culinary: Aromatic tart pulp consumed fresh or pressed into refreshing mountain juices; leaves brewed for mild sedation",
        "habitat": "Hedgerows and garden fences across highland villages",
        "conservation": "Naturalized fruit crop"
    },
    {
        "khasi_name": "Soh-mon",
        "common_name": "Mountain Sumac / Nutgall Tree",
        "scientific_name": "Rhus semialata",
        "family": "Anacardiaceae",
        "type": "Small Deciduous Tree",
        "cultural_use": "Medicinal: Sour fruit eaten as digestive; rich in tannins; used against diarrhoea, colic, and vomiting",
        "habitat": "Open secondary forests, hillsides, and river banks",
        "conservation": "Locally abundant"
    },
    {
        "khasi_name": "Soh-kymphor",
        "common_name": "Wild Mountain Papaya",
        "scientific_name": "Carica papaya",
        "family": "Caricaceae",
        "type": "Herbaceous Tree",
        "cultural_use": "Culinary & Digestive: Unripe fruit boiled as vegetable; milky latex applied topically on ringworm and wasp stings",
        "habitat": "Homesteads and valley slopes",
        "conservation": "Cultivated"
    },
    {
        "khasi_name": "Soh-shen",
        "common_name": "Siberian / Khasi Crabapple",
        "scientific_name": "Malus baccata",
        "family": "Rosaceae",
        "type": "Deciduous Small Tree",
        "cultural_use": "Small crimson tart apples eaten by village children, pickled in brine, or brewed into cider vinegar",
        "habitat": "High elevation temperate valleys (1,600m - 2,200m)",
        "conservation": "Montane wild fruit"
    },
    {
        "khasi_name": "Soh-pieng",
        "common_name": "Wild Mountain Mango",
        "scientific_name": "Mangifera sylvatica",
        "family": "Anacardiaceae",
        "type": "Large Evergreen Canopy Tree",
        "cultural_use": "Ancestral wild mango with intensely fragrant tart pulp; pickled by southern War communities",
        "habitat": "Lowland rainforest valleys of Ri-Bhoi and War borders",
        "conservation": "Wild relative of mango"
    },
    {
        "khasi_name": "Soh-trun",
        "common_name": "Mountain Pineapple",
        "scientific_name": "Ananas comosus",
        "family": "Bromeliaceae",
        "type": "Perennial Herb",
        "cultural_use": "Celebrated sweet Kew pineapples grown along the slopes of Ri-Bhoi; renowned for exceptionally low acidity",
        "habitat": "Sunlit red laterite slopes of northern Meghalaya",
        "conservation": "Major state cash crop"
    },
    {
        "khasi_name": "Dieng-lieng",
        "common_name": "Rasomala / Sacred Cloud Tree",
        "scientific_name": "Altingia excelsa",
        "family": "Altingiaceae",
        "type": "Gigantic Evergreen Canopy Tree",
        "cultural_use": "Sacred tree of Mawphlang sacred grove; aromatic balsam extracted from bark for incense",
        "habitat": "Climax sacred cloud forests (Law Kyntang)",
        "conservation": "Protected in sacred groves"
    },
    {
        "khasi_name": "Dieng-doh",
        "common_name": "Pipli Tree",
        "scientific_name": "Exbucklandia populnea",
        "family": "Hamamelidaceae",
        "type": "Large Evergreen Hardwood Tree",
        "cultural_use": "Traditional building timber for Khasi thatched cottages; leaves used as cattle fodder and soil binder",
        "habitat": "Moist montane forests of East Khasi Hills",
        "conservation": "Native forest tree"
    },
    {
        "khasi_name": "Dieng-pari",
        "common_name": "Indian Birch",
        "scientific_name": "Betula alnoides",
        "family": "Betulaceae",
        "type": "Deciduous Tree",
        "cultural_use": "Silvery bark peeling in thin sheets; historically used for wrapping food and sacred amulets; timber for pestles",
        "habitat": "Ravines and temperate slopes (1,500m - 2,000m)",
        "conservation": "Indigenous"
    },
    {
        "khasi_name": "Dieng-kynbat / Dieng-blei",
        "common_name": "Himalayan Yew",
        "scientific_name": "Taxus wallichiana",
        "family": "Taxaceae",
        "type": "Coniferous Evergreen Tree",
        "cultural_use": "Medicinal: Bark historically infused for calming remedies; source of taxol; revered as sacred long-lived tree",
        "habitat": "Shaded moist ravines of high plateaus",
        "conservation": "Endangered / Threatened"
    },
    {
        "khasi_name": "Dieng-soh-phan",
        "common_name": "Wild Jackfruit",
        "scientific_name": "Artocarpus heterophyllus",
        "family": "Moraceae",
        "type": "Evergreen Tree",
        "cultural_use": "Culinary & Musical: Seeds roasted or boiled in pork curries; wood prized for crafting traditional Duitara lutes and Ksing drums",
        "habitat": "Subtropical slopes of War and Ri-Bhoi",
        "conservation": "Cultivated and wild"
    },
    {
        "khasi_name": "Dieng-lang",
        "common_name": "Hairy Chestnut Oak",
        "scientific_name": "Castanopsis hystrix",
        "family": "Fagaceae",
        "type": "Evergreen Hardwood Tree",
        "cultural_use": "Durable timber used in building community bridges and council halls; nuts eaten by wildlife",
        "habitat": "Mid-elevation subtropical broadleaved forests",
        "conservation": "Native forest keystone"
    },
    {
        "khasi_name": "Tyngkhier",
        "common_name": "Indian Pennywort / Gotu Kola",
        "scientific_name": "Centella asiatica",
        "family": "Apiaceae",
        "type": "Creeping Herb",
        "cultural_use": "Medicinal & Culinary: Raw leaves pounded for brain memory tonic, stomach ulcer remedy, and revitalizing fresh salad",
        "habitat": "Wet marshy grassy meadows, ditch banks",
        "conservation": "Wild and common"
    },
    {
        "khasi_name": "Kynbat-ksew",
        "common_name": "Greater Plantain",
        "scientific_name": "Plantago major",
        "family": "Plantaginaceae",
        "type": "Perennial Rosette Herb",
        "cultural_use": "Medicinal: Fresh crushed leaves applied to stop bleeding wounds, insect bites, and skin burns",
        "habitat": "Footpaths, pastures, and garden edges",
        "conservation": "Common wild herb"
    },
    {
        "khasi_name": "Kynbat-iong",
        "common_name": "Billy Goat Weed",
        "scientific_name": "Ageratum conyzoides",
        "family": "Asteraceae",
        "type": "Annual Aromatic Herb",
        "cultural_use": "Medicinal: Leaf juice squeezed directly onto fresh cuts for antiseptic haemostatic clotting",
        "habitat": "Widespread along forest trails and fallows",
        "conservation": "Abundant wild weed"
    },
    {
        "khasi_name": "Bat-pyngngad",
        "common_name": "Cooling Mountain Mint",
        "scientific_name": "Mentha arvensis",
        "family": "Lamiaceae",
        "type": "Perennial Aromatic Herb",
        "cultural_use": "Medicinal: Leaves infused into hot water for fever relief, indigestion, and cooling chest compresses",
        "habitat": "Moist stream banks and household herbal plots",
        "conservation": "Cultivated & wild"
    },
    {
        "khasi_name": "Jamyrdoh-lieh",
        "common_name": "Water Celery / Sweet Dropwort",
        "scientific_name": "Oenanthe javanica",
        "family": "Apiaceae",
        "type": "Stoloniferous Wetland Herb",
        "cultural_use": "Culinary: Aromatic tender shoots eaten raw in chutneys with roasted fish; relieves liver inflammation",
        "habitat": "Rice field paddies and slow muddy brooks",
        "conservation": "Common wild green"
    },
    {
        "khasi_name": "Kynbat-thnem",
        "common_name": "Poison Antidote Herb",
        "scientific_name": "Clerodendrum colebrookianum",
        "family": "Lamiaceae",
        "type": "Perennial Shrub",
        "cultural_use": "Medicinal: Bitter young leaves boiled to lower blood pressure, hypertension, and rheumatic pain",
        "habitat": "Roadside scrub and secondary hillside growth",
        "conservation": "Traditional medicine"
    },
    {
        "khasi_name": "Tyrkhang",
        "common_name": "Edible Bracken Fern / Fiddlehead",
        "scientific_name": "Pteridium aquilinum / Diplazium esculentum",
        "family": "Dennstaedtiaceae / Athyriaceae",
        "type": "Terrestrial Perennial Fern",
        "cultural_use": "Culinary: Tender coiled spring fiddlehead crosiers ('tyrkhang') stir-fried with pork or potatoes",
        "habitat": "Forest understory, shady mountain damp slopes",
        "conservation": "Common wild vegetable"
    },
    {
        "khasi_name": "Kchu",
        "common_name": "Highland Taro / Cocoyam",
        "scientific_name": "Colocasia esculenta",
        "family": "Araceae",
        "type": "Tuberous Perennial Herb",
        "cultural_use": "Culinary: Corms and stalks boiled in savoury pork stews; large water-repellent leaves used to wrap provisions",
        "habitat": "Moist stream borders and terrace gardens",
        "conservation": "Staple indigenous tuber"
    },
    {
        "khasi_name": "Jalyniar",
        "common_name": "Wild Water Cress",
        "scientific_name": "Nasturtium officinale",
        "family": "Brassicaceae",
        "type": "Aquatic Perennial Herb",
        "cultural_use": "Culinary: Crisp peppery leaves eaten raw in village salads or boiled with smoked beef",
        "habitat": "Cold clear spring-fed highland streams",
        "conservation": "Abundant wild vegetable"
    },
    {
        "khasi_name": "Sla-met",
        "common_name": "Phrynium Leaf / Wrapping Leaf",
        "scientific_name": "Phrynium pubinerve",
        "family": "Marantaceae",
        "type": "Broadleaf Forest Herb",
        "cultural_use": "Domestic: Enormous tough waterproof leaves used to wrap rice cakes (Pukhlein, Putharo) and butcher meat",
        "habitat": "Moist tropical valleys and shady ravines",
        "conservation": "Common forest understory"
    },
    {
        "khasi_name": "Tiew-kulab",
        "common_name": "Wild Khasi Mountain Rose",
        "scientific_name": "Rosa clinophylla",
        "family": "Rosaceae",
        "type": "Evergreen Prickly Shrub",
        "cultural_use": "Poetic & Floral: Celebrated in romantic Khasi songs as the emblem of pure maternal and romantic beauty",
        "habitat": "Stream banks and marshy valleys",
        "conservation": "Native wild rose"
    },
    {
        "khasi_name": "Tiew-lyngksiar",
        "common_name": "Golden Pineapple Orchid",
        "scientific_name": "Dendrobium densiflorum",
        "family": "Orchidaceae",
        "type": "Epiphytic Orchid",
        "cultural_use": "Aesthetic: Dense pendent golden yellow flower clusters worn by maidens in their hair during Shad Suk Mynsiem",
        "habitat": "Mossy tree trunks in sub-montane forests",
        "conservation": "Ornamental native"
    },
    {
        "khasi_name": "Tiew-saw",
        "common_name": "Scarlet Fox-Brush Orchid",
        "scientific_name": "Aerides multiflora",
        "family": "Orchidaceae",
        "type": "Epiphytic Orchid",
        "cultural_use": "Traditional adornment during springtime thanksgiving festivals",
        "habitat": "Broadleaf trees in southern foothills",
        "conservation": "Wild orchid"
    },
    {
        "khasi_name": "Tiew-stem",
        "common_name": "Golden Dendrobium",
        "scientific_name": "Dendrobium chrysanthum",
        "family": "Orchidaceae",
        "type": "Epiphytic Orchid",
        "cultural_use": "Ornamental and symbolic in folklore of youthful renewal and spring blossoms",
        "habitat": "Epiphyte on highland oaks and pines",
        "conservation": "Protected"
    },
    {
        "khasi_name": "Siej-lieh",
        "common_name": "White Hill Bamboo",
        "scientific_name": "Bambusa tulda",
        "family": "Poaceae",
        "type": "Large Clumping Bamboo",
        "cultural_use": "Craft & Architecture: Primary material for wall paneling, ceiling mats, split bamboo flooring, and fishing baskets",
        "habitat": "Foothills and river valleys up to 1,200m",
        "conservation": "Cultivated & wild"
    },
    {
        "khasi_name": "Siej-shken",
        "common_name": "Berry Bamboo",
        "scientific_name": "Melocanna baccifera",
        "family": "Poaceae",
        "type": "Rhizomatous Diffuse Bamboo",
        "cultural_use": "Produces edible pear-sized fleshy bamboo fruit; thin culms split for fine weaving of rain-shields (Knup)",
        "habitat": "Abundant across mid-hills and southern slopes",
        "conservation": "Dominant wild bamboo"
    },
    {
        "khasi_name": "Siej-namlang",
        "common_name": "Highland Arrow Bamboo",
        "scientific_name": "Thamnocalamus aristatus",
        "family": "Poaceae",
        "type": "Montane Bamboo",
        "cultural_use": "Straight tough culms harvested exclusively to craft traditional hunting arrows for Khasi archery (Thoh Tim)",
        "habitat": "Upper montane ridges above 1,800m",
        "conservation": "Culturally significant"
    },
    {
        "khasi_name": "Siej-rit",
        "common_name": "Slender Pipe Bamboo",
        "scientific_name": "Arundinaria suberecta",
        "family": "Poaceae",
        "type": "Dwarf Montane Bamboo",
        "cultural_use": "Musical instruments: Cut to craft traditional flutes (Sharati, Shyngwiang) and smoking pipes",
        "habitat": "Rocky ravines and limestone cliff edges",
        "conservation": "Indigenous"
    },
    {
        "khasi_name": "Tynriew",
        "common_name": "Wild Rattan Cane",
        "scientific_name": "Calamus tenuis",
        "family": "Arecaceae",
        "type": "Climbing Spiny Palm",
        "cultural_use": "Master craft: Stems split into tough lashings to bind house poles, bamboo bridges, and exquisite canes",
        "habitat": "Wet lowland rainforests and canyon bottoms",
        "conservation": "Agro-forestry resource"
    },
    {
        "khasi_name": "Sla-tyr-a",
        "common_name": "Broom Grass / Hill Broom",
        "scientific_name": "Thysanolaena latifolia",
        "family": "Poaceae",
        "type": "Tall Perennial Grass",
        "cultural_use": "Major export commodity: Inflorescences harvested and dried into famous Meghalaya hill broomsticks",
        "habitat": "Steep rocky hillsides and fallow terraces",
        "conservation": "Major commercial cash crop"
    },
    {
        "khasi_name": "Tit-tung",
        "common_name": "Khasi Black Meadow Mushroom",
        "scientific_name": "Agaricus bisporus (wild variety)",
        "family": "Agaricaceae",
        "type": "Edible Basidiomycete Fungi",
        "cultural_use": "Culinary: Foraged from mountain grassy meadows after monsoon thunderstorms; cooked with ginger and onions",
        "habitat": "Grassy highland commons and pine margins",
        "conservation": "Seasonal wild food"
    },
    {
        "khasi_name": "Tit-saw",
        "common_name": "Red Pine Mushroom",
        "scientific_name": "Lactarius deliciosus",
        "family": "Russulaceae",
        "type": "Mycorrhizal Edible Fungus",
        "cultural_use": "Culinary: Prized edible mushroom with carrot-orange milk; foraged in Khasi pine groves in autumn",
        "habitat": "Symbiotic with Pinus kesiya root systems",
        "conservation": "Foraged wild mushroom"
    },
    {
        "khasi_name": "Tit-stem",
        "common_name": "Highland Chanterelle",
        "scientific_name": "Cantharellus cibarius",
        "family": "Cantharellaceae",
        "type": "Mycorrhizal Edible Fungus",
        "cultural_use": "Culinary: Golden-yellow trumpet mushroom with apricot aroma; considered a seasonal delicacy",
        "habitat": "Highland oak and broadleaf sacred forests",
        "conservation": "Wild seasonal delicacy"
    },
    {
        "khasi_name": "Tit-khoh",
        "common_name": "Termite Mound Mushroom",
        "scientific_name": "Termitomyces eurhizus",
        "family": "Lyophyllaceae",
        "type": "Symbiotic Macrofungus",
        "cultural_use": "Culinary: Large meaty umbrella mushroom emerging from underground subterranean combs; highly valued in local markets",
        "habitat": "Subtropical foothills and forest margins",
        "conservation": "Wild delicacy"
    },
    {
        "khasi_name": "Tit-thylliej-blang",
        "common_name": "Goat's Tongue Mushroom / Coral Fungus",
        "scientific_name": "Ramaria flava",
        "family": "Gomphaceae",
        "type": "Edible Coral Mushroom",
        "cultural_use": "Culinary: Bright yellow branching fungus resemblance to goat tongue; boiled and eaten in traditional stews",
        "habitat": "Forest floor litter under deciduous trees",
        "conservation": "Wild edible"
    },
    {
        "khasi_name": "Soh-lyngkait",
        "common_name": "Wild Mountain Raspberry",
        "scientific_name": "Rubus ellipticus",
        "family": "Rosaceae",
        "type": "Prickly Evergreen Shrub",
        "cultural_use": "Culinary & Medicinal: Golden juicy berries eaten fresh along roadsides; roots chewed for mouth ulcers and coughs",
        "habitat": "Sunny forest edges, roadsides, and wasteland",
        "conservation": "Common wild fruit"
    },
    {
        "khasi_name": "Soh-khaw-iong",
        "common_name": "Wild Blackberry / Hill Bramble",
        "scientific_name": "Rubus niveus",
        "family": "Rosaceae",
        "type": "Prickly Shrub",
        "cultural_use": "Culinary: Sweet-tart purple-black berries foraged in winter; high antioxidant content",
        "habitat": "High altitude shrubberies (1,400m - 2,000m)",
        "conservation": "Common wild fruit"
    },
    {
        "khasi_name": "Soh-lang",
        "common_name": "Wild Mountain Silverberry",
        "scientific_name": "Elaeagnus umbellata",
        "family": "Elaeagnaceae",
        "type": "Deciduous Shrub",
        "cultural_use": "Culinary: Small red berries dotted with silver scales; tart and vitamin-rich",
        "habitat": "Open rocky hillsides and river gravels",
        "conservation": "Wild fruit"
    },
    {
        "khasi_name": "Soh-pyrkhi",
        "common_name": "Highland Gooseberry",
        "scientific_name": "Ribes glaciale",
        "family": "Grossulariaceae",
        "type": "Montane Shrub",
        "cultural_use": "Culinary: Tart berries eaten raw with salt; boiled into wild preserves",
        "habitat": "High cold valleys of Shillong ridge",
        "conservation": "Montane native"
    },
    {
        "khasi_name": "Soh-khlur",
        "common_name": "Star Fruit / Mountain Carambola",
        "scientific_name": "Averrhoa carambola",
        "family": "Oxalidaceae",
        "type": "Small Tropical Tree",
        "cultural_use": "Culinary: Star-shaped crunchy fruit eaten raw with chili powder; juice cleanses brass ornaments",
        "habitat": "Southern War valleys and Ri-Bhoi orchards",
        "conservation": "Cultivated"
    },
    {
        "khasi_name": "Soh-pang",
        "common_name": "Wild Hog Plum",
        "scientific_name": "Spondias pinnata",
        "family": "Anacardiaceae",
        "type": "Deciduous Tree",
        "cultural_use": "Culinary & Astringent: Sour green fruit stewed with dry fish; juice calms bilious fevers",
        "habitat": "Lowland deciduous forests",
        "conservation": "Wild fruit tree"
    },
    {
        "khasi_name": "Soh-khyllam",
        "common_name": "Wild Mountain Pear",
        "scientific_name": "Pyrus pashia",
        "family": "Rosaceae",
        "type": "Deciduous Tree",
        "cultural_use": "Culinary: Russet brown speckled wild pears softened after frost; leaves yield brown textile dye",
        "habitat": "Hedge margins and secondary pine forests",
        "conservation": "Native mountain fruit"
    },
    {
        "khasi_name": "Dieng-soh-risang",
        "common_name": "Khasi Alder",
        "scientific_name": "Alnus nepalensis",
        "family": "Betulaceae",
        "type": "Fast-growing Deciduous Tree",
        "cultural_use": "Agro-forestry: Nitrogen-fixing tree planted on steep jhum slopes to restore exhausted mountain soil",
        "habitat": "Landslide scars, stream gorges, fallow lands",
        "conservation": "Ecological restoration keystone"
    },
    {
        "khasi_name": "Dieng-sait-khmat",
        "common_name": "Eye-Wash Tree",
        "scientific_name": "Symplocos cochinchinensis",
        "family": "Symplocaceae",
        "type": "Subtropical Tree",
        "cultural_use": "Medicinal & Dyeing: Bark infusion used as traditional soothing eyewash; leaves mordant for red natural dyes",
        "habitat": "Moist broadleaf forests and sacred groves",
        "conservation": "Indigenous"
    },
    {
        "khasi_name": "Dieng-byrtha",
        "common_name": "Wild Cinnamon",
        "scientific_name": "Cinnamomum verum (wild form)",
        "family": "Lauraceae",
        "type": "Evergreen Tree",
        "cultural_use": "Culinary & Aromatic: Bark stripped and dried as sweet cinnamon quills; oil distilled for toothache relief",
        "habitat": "Southern subtropical slopes",
        "conservation": "Agro-forestry"
    },
    {
        "khasi_name": "Latyrdop",
        "common_name": "Climbing Mountain Fern",
        "scientific_name": "Stenochlaena palustris",
        "family": "Blechnaceae",
        "type": "Epiphytic / Scandent Fern",
        "cultural_use": "Culinary: Young tender reddish fronds cooked with pork; rhizome infusion taken for stomach spasms",
        "habitat": "Dense wet swamp forests and river gorges",
        "conservation": "Wild vegetable"
    },
    {
        "khasi_name": "Bat-shira",
        "common_name": "Sweet Mountain Stevia / Herb",
        "scientific_name": "Scoparia dulcis",
        "family": "Plantaginaceae",
        "type": "Erect Perennial Herb",
        "cultural_use": "Medicinal: Sweet-tasting herb brewed for childhood coughs, kidney stones, and digestive ailments",
        "habitat": "Roadside verges and sandy stream gravels",
        "conservation": "Common herb"
    },
    {
        "khasi_name": "Kynbat-moina",
        "common_name": "Hill Burnet Saxifrage",
        "scientific_name": "Pimpinella candolleana",
        "family": "Apiaceae",
        "type": "Montane Aromatic Herb",
        "cultural_use": "Medicinal: Pounded aromatic root used in traditional tonics for gastric discomfort and colic",
        "habitat": "Grassy hill ridges around Mawphlang",
        "conservation": "Montane indigenous"
    },
    {
        "khasi_name": "Soh-jhalia",
        "common_name": "Wild Mountain Turmeric",
        "scientific_name": "Curcuma aromatica",
        "family": "Zingiberaceae",
        "type": "Rhizomatous Perennial Herb",
        "cultural_use": "Cosmetic & Antiseptic: Fragrant golden rhizome pasted on the face for skin beauty; antiseptic for bruises",
        "habitat": "Undergrowth of deciduous hill forests",
        "conservation": "Wild relative of turmeric"
    },
    {
        "khasi_name": "Bat-kba",
        "common_name": "Wild Paddy Field Herb",
        "scientific_name": "Limnophila aromatica",
        "family": "Plantaginaceae",
        "type": "Marsh Herb",
        "cultural_use": "Culinary: Aromatic citrus-scented herb used to flavour fish curries in Pnar and Bhoi villages",
        "habitat": "Wet rice paddies and swamp canals",
        "conservation": "Wild culinary green"
    },
    {
        "khasi_name": "Kdait",
        "common_name": "Khasi Reed / River Cane",
        "scientific_name": "Neyraudia reynaudiana",
        "family": "Poaceae",
        "type": "Tall Silky Reed Grass",
        "cultural_use": "Craft: Fluffy silky flower plumes collected for mattress stuffing; reeds woven into light temporary partitions",
        "habitat": "Riverbanks, cliffs, and mountain roadsides",
        "conservation": "Abundant wild grass"
    },
    {
        "khasi_name": "Phlang-pinar",
        "common_name": "Sacred Thatch Grass",
        "scientific_name": "Imperata cylindrica",
        "family": "Poaceae",
        "type": "Perennial Rhizomatous Grass",
        "cultural_use": "Traditional roofing: Harvested in late autumn for traditional water-resistant thatched roofs of Khasi huts",
        "habitat": "Highland grasslands and ridge tops",
        "conservation": "Common native grass"
    },
    {
        "khasi_name": "Nei-lieh",
        "common_name": "White Perilla Seed",
        "scientific_name": "Perilla frutescens",
        "family": "Lamiaceae",
        "type": "Annual Bushy Herb",
        "cultural_use": "Culinary cornerstone: Fragrant nutty seeds toasted, pounded in wooden mortar, and mixed into famous 'Dohneiiong' pork curry and salad chutneys",
        "habitat": "Cultivated in highland village gardens and jhum fields",
        "conservation": "Traditional indigenous spice"
    },
    {
        "khasi_name": "Nei-iong",
        "common_name": "Black Sesame / Black Perilla",
        "scientific_name": "Sesamum indicum (black seeded)",
        "family": "Pedaliaceae",
        "type": "Annual Herb",
        "cultural_use": "Culinary & Ritual: Roasted black seeds pounded into thick savory paste for classic Khasi black sesame pork ('Doh-snam' / 'Doh-nei-iong')",
        "habitat": "Highland terraces and kitchen gardens",
        "conservation": "Core culinary crop"
    },
    {
        "khasi_name": "Synsar",
        "common_name": "Wild Cardamom / Greater Cardamom",
        "scientific_name": "Amomum subulatum",
        "family": "Zingiberaceae",
        "type": "Perennial Understory Herb",
        "cultural_use": "High-value spice: Dark ribbed seed capsules harvested in shady valleys; aromatic condiment and breath freshener",
        "habitat": "Moist shaded stream gullies in southern hills",
        "conservation": "Agro-forestry spice"
    },
    {
        "khasi_name": "Soh-kwai",
        "common_name": "Areca Nut / Betel Nut Palm",
        "scientific_name": "Areca catechu",
        "family": "Arecaceae",
        "type": "Slender Solitary Palm",
        "cultural_use": "Cultural foundation: The core of the universal Khasi hospitality rite 'Kwai'; sliced raw and offered with betel leaf (Tympew) and lime to every guest",
        "habitat": "Subtropical southern slopes (War Shella, Sohra, Dawki)",
        "conservation": "Universal cultural crop"
    },
    {
        "khasi_name": "Tympew",
        "common_name": "Betel Vine Leaf",
        "scientific_name": "Piper betle",
        "family": "Piperaceae",
        "type": "Dioecious Evergreen Climber",
        "cultural_use": "Cultural rite: Fresh heart-shaped pungent leaves paired with Kwai nut as the highest token of peace, friendship, and greeting",
        "habitat": "Climbing on Areca palms and forest trees in southern valleys",
        "conservation": "Sacred cultural vine"
    },
    {
        "khasi_name": "Soh-manir",
        "common_name": "Calamus Fruit / Wild Sweet Palm",
        "scientific_name": "Zalacca secunda / Calamus erectus",
        "family": "Arecaceae",
        "type": "Tufted Sub-tropical Palm",
        "cultural_use": "Culinary: Scaly brownish fruit with tangy crisp pulp enjoyed by hill walkers; fronds used for rain thatch",
        "habitat": "Deep gorges and river valleys",
        "conservation": "Wild forest palm"
    },
    {
        "khasi_name": "Soh-kymphor-pyrthei",
        "common_name": "Wild Fig / Cluster Fig",
        "scientific_name": "Ficus racemosa",
        "family": "Moraceae",
        "type": "Large Evergreen Tree",
        "cultural_use": "Culinary & Folk: Clusters of wild figs eaten by birds and villagers; sacred tree guarding water aquifers",
        "habitat": "Stream margins and sacred groves",
        "conservation": "Keystone ecological tree"
    },
    {
        "khasi_name": "Dieng-soh-khyllung",
        "common_name": "Tree Bean",
        "scientific_name": "Parkia timoriana",
        "family": "Fabaceae",
        "type": "Large Deciduous Tree",
        "cultural_use": "Culinary Delicacy: Long flat green pods eaten raw in chutneys with fermented fish or cooked with beef; pods fetch premium prices in markets",
        "habitat": "Warm humid slopes of Ri-Bhoi and War borders",
        "conservation": "High-value indigenous tree"
    },
    {
        "khasi_name": "Dieng-soh-pdok",
        "common_name": "Wild Plum / Indian Cherry",
        "scientific_name": "Flacourtia jangomas",
        "family": "Salicaceae",
        "type": "Dioecious Spiny Tree",
        "cultural_use": "Culinary: Purple-red astringent fruits rolled between palms before eating to sweeten pulp; bark used for bilious fevers",
        "habitat": "Foothill forests and abandoned settlements",
        "conservation": "Wild fruit tree"
    },
    {
        "khasi_name": "Soh-lyngwait",
        "common_name": "Wild Mountain Strawberry",
        "scientific_name": "Fragaria vesca (montane form)",
        "family": "Rosaceae",
        "type": "Creeping Herb",
        "cultural_use": "Culinary: Delicate sweet miniature red strawberries foraged on high grassy hillocks",
        "habitat": "Montane meadows and pine woodland fringes",
        "conservation": "Wild fruit"
    },
    {
        "khasi_name": "Dieng-tyrnem",
        "common_name": "Hammer Hardwood Tree",
        "scientific_name": "Mesua ferrea",
        "family": "Calophyllaceae",
        "type": "Evergreen Hardwood Tree",
        "cultural_use": "Craft: Extremely heavy iron-like wood used to fashion traditional tool handles, pestles, and war clubs; fragrant white flowers",
        "habitat": "Subtropical evergreen forests",
        "conservation": "Culturally valued hardwood"
    },
    {
        "khasi_name": "Dieng-ngan",
        "common_name": "Indian Alder Birch",
        "scientific_name": "Schima wallichii",
        "family": "Theaceae",
        "type": "Evergreen Canopy Tree",
        "cultural_use": "Timber & Tannin: Durable building timber; white camellia-like blossoms; bark contains irritant crystalline saponins",
        "habitat": "Dominant associate in Khasi pine and broadleaf mixed forests",
        "conservation": "Widespread forest tree"
    },
    {
        "khasi_name": "Dieng-soh-kyrpho",
        "common_name": "Wild Chinese Olive",
        "scientific_name": "Canarium resiniferum",
        "family": "Burseraceae",
        "type": "Large Forest Tree",
        "cultural_use": "Resin & Fruit: Oily fruit kernels eaten roasted; trunk yields fragrant clear black dammar resin burned in sacred rituals",
        "habitat": "Moist subtropical river gorges",
        "conservation": "Indigenous"
    },
    {
        "khasi_name": "Tiew-dohmaw",
        "common_name": "Khasi Lady's Slipper Orchid",
        "scientific_name": "Paphiopedilum insigne",
        "family": "Orchidaceae",
        "type": "Terrestrial & Lithophytic Orchid",
        "cultural_use": "Ornamental & Cultural: Rare sacred orchid blooming on mossy limestone crags; celebrated in classical poetry",
        "habitat": "Moist, shady limestone cliffs around Sohra and Mawsynram (1,200m - 1,800m)",
        "conservation": "Threatened / CITES Appendix I"
    },
    {
        "khasi_name": "Soh-phlang",
        "common_name": "Khasi Edible Tuber / Flemingia",
        "scientific_name": "Flemingia vestita",
        "family": "Fabaceae",
        "type": "Perennial Nitrogen-Fixing Tuberous Legume",
        "cultural_use": "Culinary & Medicinal: Crunchy sweet white tubers eaten raw with roasted perilla seeds (Nei Lieh); anthelmintic and deworming properties",
        "habitat": "Highland terrace fields across East Khasi Hills",
        "conservation": "Traditional indigenous crop"
    },
    {
        "khasi_name": "Kynbat-dawai / Chirayita",
        "common_name": "Khasi Chiretta",
        "scientific_name": "Swertia chirayita",
        "family": "Gentianaceae",
        "type": "Erect Medicinal Herb",
        "cultural_use": "Medicinal: Renowned bitter tonic decoction used to treat persistent fevers, malaria, liver sluggishness, and blood purification",
        "habitat": "Subalpine grassy slopes (1,500m - 2,200m)",
        "conservation": "Medicinal heritage herb"
    },
    {
        "khasi_name": "Dieng-jri",
        "common_name": "Indian Rubber Fig / Root Bridge Fig",
        "scientific_name": "Ficus elastica",
        "family": "Moraceae",
        "type": "Massive Strangler Fig / Canopy Tree",
        "cultural_use": "Cultural Engineering: Aerial prop roots are guided through hollow betel trunks to weave world-famous living root bridges (Jingkieng Jri)",
        "habitat": "Subtropical southern slopes and river gorges of War-Khasi",
        "conservation": "Sacred keystone species"
    },
    {
        "khasi_name": "Sla-met",
        "common_name": "Khasi Wrapping Leaf",
        "scientific_name": "Phrynium pubinerve",
        "family": "Marantaceae",
        "type": "Broad-leaved Forest Herb",
        "cultural_use": "Culinary & Ritual: Broad, flexible waterproof leaves used to wrap steaming rice cakes (Pukhlein, Kpu), dry fish, and market produce",
        "habitat": "Damp evergreen forest understory",
        "conservation": "Abundant wild resource"
    },
    {
        "khasi_name": "Sla-tyrpad",
        "common_name": "Khasi Bay Leaf / Indian Cassia",
        "scientific_name": "Cinnamomum tamala",
        "family": "Lauraceae",
        "type": "Evergreen Aromatic Tree",
        "cultural_use": "Culinary & Trade: Highly aromatic dried leaves exported across India as Tejpat; bark used as cinnamon substitute; digestive carminative",
        "habitat": "Southern gorges of Ri-War, Shella, and Cherrapunjee",
        "conservation": "Major organic cash crop"
    },
    {
        "khasi_name": "Siej-namlang",
        "common_name": "Giant Hill Bamboo",
        "scientific_name": "Dendrocalamus hamiltonii",
        "family": "Poaceae",
        "type": "Giant Clumping Bamboo",
        "cultural_use": "Craft & Architecture: Thick-walled bamboo culms used for house water pipes, structural poles, and water-carrying vessels (Ktang-um)",
        "habitat": "River valleys and subtropical hill slopes",
        "conservation": "Abundant indigenous bamboo"
    },
    {
        "khasi_name": "Soh-shiah",
        "common_name": "Golden Himalayan Raspberry",
        "scientific_name": "Rubus ellipticus",
        "family": "Rosaceae",
        "type": "Thorny Evergreen Shrub",
        "cultural_use": "Culinary & Medicinal: Sweet golden-yellow wild berries gathered in spring; root decoction taken for diarrhea and abdominal cramps",
        "habitat": "Forest edges, roadsides, and pine scrub",
        "conservation": "Common wild fruit"
    },
    {
        "khasi_name": "Soh-khyllam",
        "common_name": "Assam Wild Crabapple",
        "scientific_name": "Docynia indica",
        "family": "Rosaceae",
        "type": "Medium Deciduous Mountain Tree",
        "cultural_use": "Culinary: Acidic tart fruits eaten fresh with salt or pickled; high pectin content used in traditional jellies",
        "habitat": "Khasi highlands (1,400m - 1,900m)",
        "conservation": "Wild and domestic"
    },
    {
        "khasi_name": "Tiew-jalyngngap",
        "common_name": "White Hill Rhododendron",
        "scientific_name": "Rhododendron formosum",
        "family": "Ericaceae",
        "type": "Epiphytic or Lithophytic Shrub",
        "cultural_use": "Ornamental & Cultural: Fragrant pure white-pink trumpet flowers blooming in April; symbol of highland spring in Khasi songs",
        "habitat": "Exposed rocky crags and mossy trees in high-rainfall zones",
        "conservation": "Subalpine native"
    },
    {
        "khasi_name": "Kynbat-khlieng",
        "common_name": "Indian Pennywort / Gotu Kola",
        "scientific_name": "Centella asiatica",
        "family": "Apiaceae",
        "type": "Creeping Perennial Herb",
        "cultural_use": "Medicinal & Culinary: Fan-shaped leaves eaten fresh in herbal salads; revered memory-enhancer, wound healer, and cooling blood purifier",
        "habitat": "Damp meadows, spring margins, and stream edges",
        "conservation": "Common indigenous herb"
    },
    {
        "khasi_name": "Soh-mylleng",
        "common_name": "Wild Amla / Indian Gooseberry",
        "scientific_name": "Phyllanthus emblica",
        "family": "Phyllanthaceae",
        "type": "Deciduous Mountain Tree",
        "cultural_use": "Medicinal & Culinary: Highly astringent sour fruit that leaves a sweet lingering aftertaste in cold spring water; potent Vitamin C tonic",
        "habitat": "Dry open slopes and mixed deciduous ridges",
        "conservation": "Indigenous wild tree"
    },
    {
        "khasi_name": "Tit-stem",
        "common_name": "Golden Pine Chanterelle",
        "scientific_name": "Cantharellus cibarius",
        "family": "Cantharellaceae",
        "type": "Wild Ectomycorrhizal Edible Mushroom",
        "cultural_use": "Culinary: Prized apricot-scented golden mushroom foraged from pine duff in July-August; cooked with pork, ginger, and mustard oil",
        "habitat": "Khasi pine (Pinus kesiya) forest floor",
        "conservation": "Seasonal wild delicacy"
    },
    {
        "khasi_name": "Dieng-sning",
        "common_name": "Griffith's Khasi Oak",
        "scientific_name": "Quercus griffithii",
        "family": "Fagaceae",
        "type": "Large Mountain Oak",
        "cultural_use": "Ecological & Timber: Heavy, durable timber used for house frames and agricultural tool handles; sacred grove keystone species",
        "habitat": "Sacred groves (Lawkyntang) and primary broadleaf forests",
        "conservation": "Old-growth native"
    },
    {
        "khasi_name": "Sla-tympew",
        "common_name": "Khasi Betel Vine",
        "scientific_name": "Piper betle",
        "family": "Piperaceae",
        "type": "Evergreen Climber",
        "cultural_use": "Sacred Ritual & Hospitality: Essential leaf chewed with kwai (areca nut) and lime; indispensable token of greeting and ancestral covenants",
        "habitat": "Warm subtropical southern slopes of Shella and Pynursla",
        "conservation": "Major cash crop"
    }
]

def list_plants() -> List[Dict[str, Any]]:
    """Return all catalogued indigenous Khasi flora, wild fruits, trees, and ethnomedicinal plants."""
    return PLANTS

def get_plant(name: str) -> Optional[Dict[str, Any]]:
    """Lookup a plant by Khasi name, common name, or scientific binomial name."""
    q = name.lower().strip()
    for p in PLANTS:
        if (q in p["khasi_name"].lower() or
            q in p["common_name"].lower() or
            q in p["scientific_name"].lower()):
            return p
    return None

def by_plant_type(plant_type: str) -> List[Dict[str, Any]]:
    """Filter plants by type (e.g., 'Tree', 'Herb', 'Fruit', 'Orchid', 'Bamboo', 'Fungi')."""
    pt = plant_type.lower().strip()
    return [p for p in PLANTS if pt in p["type"].lower() or pt in p["cultural_use"].lower()]

def medicinal_plants() -> List[Dict[str, Any]]:
    """Return all plants with documented medicinal or therapeutic uses."""
    return [p for p in PLANTS if "medicinal" in p["cultural_use"].lower() or "antiseptic" in p["cultural_use"].lower() or "tonic" in p["cultural_use"].lower()]

def search_plants(query: str) -> List[Dict[str, Any]]:
    """Search plants by keyword across all botanical fields."""
    q = query.lower().strip()
    return [p for p in PLANTS if (
        q in p["khasi_name"].lower() or
        q in p["common_name"].lower() or
        q in p["scientific_name"].lower() or
        q in p["family"].lower() or
        q in p["cultural_use"].lower() or
        q in p["habitat"].lower()
    )]

def total_plants() -> int:
    """Return total count of catalogued botanical species."""
    return len(PLANTS)
