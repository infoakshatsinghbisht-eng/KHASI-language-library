# -*- coding: utf-8 -*-
"""
Khasi Wildlife, Zoology, and Highland Fauna of Meghalaya.
Comprehensive documentation of native mammals, birds, fish, reptiles, amphibians, and insects
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
        "cultural_significance": "State animal of Meghalaya; revered as an agile master of the tree canopies and guardian of deep mountain ravines."
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
        "status": "Endangered / Sole ape of India",
        "habitat": "Dense tropical evergreen canopies of Nokrek and South Khasi",
        "cultural_significance": "Famous for haunting territorial songs echoing through river valleys; strictly taboo to harm."
    },
    {
        "khasi_name": "Ka Risang",
        "common_name": "Malayan Giant Squirrel",
        "scientific_name": "Ratufa bicolor",
        "class_type": "Mammal",
        "status": "Near Threatened",
        "habitat": "High canopy of undisturbed broadleaf forests",
        "cultural_significance": "Acrobatic forest dweller whose presence indicates a healthy, ancient forest ecosystem."
    },
    {
        "khasi_name": "Ka Bsei / Ka Ksaw",
        "common_name": "Binturong / Bearcat",
        "scientific_name": "Arctictis binturong",
        "class_type": "Mammal",
        "status": "Vulnerable",
        "habitat": "Dense evergreen rainforest canopies",
        "cultural_significance": "Nocturnal arboreal creature known for its buttered-popcorn scent and prehensile tail."
    },
    {
        "khasi_name": "U Ksew-ngi",
        "common_name": "Dhole / Asiatic Wild Dog",
        "scientific_name": "Cuon alpinus",
        "class_type": "Mammal",
        "status": "Endangered",
        "habitat": "Highland plateau forests and hunting commons",
        "cultural_significance": "Revered for exceptional cooperative hunting packs and intelligence in tribal hunting lore."
    },
    {
        "khasi_name": "U Sniang-khlaw",
        "common_name": "Wild Boar",
        "scientific_name": "Sus scrofa",
        "class_type": "Mammal",
        "status": "Least Concern",
        "habitat": "Bamboo thickets and secondary scrub across hills",
        "cultural_significance": "Prized game animal in traditional autumn communal hunts; tusks worn as hunter's trophies."
    },
    {
        "khasi_name": "U Bthuh",
        "common_name": "Barking Deer / Northern Red Muntjac",
        "scientific_name": "Muntiacus vaginalis",
        "class_type": "Mammal",
        "status": "Least Concern",
        "habitat": "Deep forest undergrowth and valley margins",
        "cultural_significance": "Its sharp dog-like bark warns villagers and forest creatures of approaching predators."
    },
    {
        "khasi_name": "Ka Masi-prut",
        "common_name": "Gaur / Indian Bison",
        "scientific_name": "Bos gaurus",
        "class_type": "Mammal",
        "status": "Vulnerable",
        "habitat": "Foothill grasslands and bamboo tracts of Ri-Bhoi",
        "cultural_significance": "Embodiment of massive raw strength and pasture nobility in highland folklore."
    },
    {
        "khasi_name": "Ka Mynthi",
        "common_name": "Mainland Serow / Goat-Antelope",
        "scientific_name": "Capricornis sumatraensis",
        "class_type": "Mammal",
        "status": "Vulnerable",
        "habitat": "Precipitous rocky crags and inaccessible limestone ravines",
        "cultural_significance": "Elusive cliff-dweller celebrated in hunting poetry for traversing vertical stone walls."
    },
    {
        "khasi_name": "Ka Tngaw",
        "common_name": "Capped Langur",
        "scientific_name": "Trachypithecus pileatus",
        "class_type": "Mammal",
        "status": "Vulnerable",
        "habitat": "Subtropical broadleaf and mixed evergreen forests",
        "cultural_significance": "Golden-bellied arboreal primate; troop calls announce change in mountain weather."
    },
    {
        "khasi_name": "Ka Shrieh-snam",
        "common_name": "Stump-tailed Macaque",
        "scientific_name": "Macaca arctoides",
        "class_type": "Mammal",
        "status": "Vulnerable",
        "habitat": "Evergreen and semi-evergreen hill forests",
        "cultural_significance": "Red-faced forest monkey noted for communal grooming and foraging on wild figs."
    },
    {
        "khasi_name": "U Ksing",
        "common_name": "Leopard Cat",
        "scientific_name": "Prionailurus bengalensis",
        "class_type": "Mammal",
        "status": "Least Concern",
        "habitat": "Highland agricultural borders and forest streams",
        "cultural_significance": "Small spotted wild feline; legendary for stealth and mouse-hunting around grain stores."
    },
    {
        "khasi_name": "U Khla-nam",
        "common_name": "Asiatic Golden Cat",
        "scientific_name": "Catopuma temminckii",
        "class_type": "Mammal",
        "status": "Near Threatened",
        "habitat": "Dense tropical and montane cloud forests",
        "cultural_significance": "Mysterious polymorphic feline appearing in red, melanistic, and ocelot-patterned coats."
    },
    {
        "khasi_name": "U Tngaw-stem",
        "common_name": "Assamese Macaque",
        "scientific_name": "Macaca assamensis",
        "class_type": "Mammal",
        "status": "Near Threatened",
        "habitat": "Riverine hill forests and cliff terraces",
        "cultural_significance": "Clever social troops frequently seen foraging along the gorges of Cherrapunjee."
    },
    {
        "khasi_name": "Ka Khnap",
        "common_name": "Bengal Slow Loris",
        "scientific_name": "Nycticebus bengalensis",
        "class_type": "Mammal",
        "status": "Endangered",
        "habitat": "Tropical wet evergreen and bamboo forests",
        "cultural_significance": "Gentle nocturnal primate with huge round eyes; protected under deep taboo against mistreatment."
    },
    {
        "khasi_name": "U Brap / U Dkhiew",
        "common_name": "Chinese Pangolin / Scaly Anteater",
        "scientific_name": "Manis pentadactyla",
        "class_type": "Mammal",
        "status": "Critically Endangered",
        "habitat": "Burrows in subtropical deciduous hill forests",
        "cultural_significance": "Ancient scaly creature; rolled into defensive sphere; strictly protected under traditional customary taboo."
    },
    {
        "khasi_name": "Ka Bsein-ding",
        "common_name": "Marbled Cat",
        "scientific_name": "Pardofelis marmorata",
        "class_type": "Mammal",
        "status": "Near Threatened",
        "habitat": "Moist tropical evergreen forest canopies",
        "cultural_significance": "Tiny arboreal predator with cloud-like rosette markings and a remarkably bushy long tail."
    },
    {
        "khasi_name": "Ka Risang-stem",
        "common_name": "Orange-bellied Himalayan Squirrel",
        "scientific_name": "Dremomys lokriah",
        "class_type": "Mammal",
        "status": "Least Concern",
        "habitat": "Oak and pine forests between 1,200m - 2,200m",
        "cultural_significance": "Chattering squirrel seen caching acorns and wild hazelnuts in sacred grove leaf litter."
    },
    {
        "khasi_name": "U Khnai-khlaw",
        "common_name": "Malayan Crestless Porcupine",
        "scientific_name": "Hystrix brachyura",
        "class_type": "Mammal",
        "status": "Least Concern",
        "habitat": "Rocky crevices and forest burrows",
        "cultural_significance": "Spines collected by village elders to weave protective talismans and decorative quills."
    },
    {
        "khasi_name": "Ka Ksew-um",
        "common_name": "Eurasian Otter / River Otter",
        "scientific_name": "Lutra lutra",
        "class_type": "Mammal",
        "status": "Near Threatened",
        "habitat": "Pristine clear highland mountain torrents (Umngot, Myntdu)",
        "cultural_significance": "Agile playful swimmer; symbolizes unpolluted crystal rivers."
    },
    {
        "khasi_name": "Ka Dngiem-rit",
        "common_name": "Malayan Sun Bear",
        "scientific_name": "Helarctos malayanus",
        "class_type": "Mammal",
        "status": "Vulnerable",
        "habitat": "Dense lowland tropical rainforests",
        "cultural_significance": "Smallest bear in the world; skilled tree climber with an exceptionally long tongue for wild bee hives."
    },
    {
        "khasi_name": "U Kohkarang",
        "common_name": "Great Pied Hornbill",
        "scientific_name": "Buceros bicornis",
        "class_type": "Bird",
        "status": "Vulnerable / Emblem of Highland Majesty",
        "habitat": "Tall canopy trees of sacred groves and old-growth rainforests",
        "cultural_significance": "Its deep whooshing wingbeats and majestic casque feathers represent regal tribal dignity and forest guardianship."
    },
    {
        "khasi_name": "Ka Syiem-sim / U Sim-pyllieng",
        "common_name": "Green Peafowl / Indian Peacock",
        "scientific_name": "Pavo muticus / Pavo cristatus",
        "class_type": "Bird",
        "status": "Endangered / Sacred Bird",
        "habitat": "Dense scrub and riverine forests",
        "cultural_significance": "Queen of the birds; spectacular tail dance mimics the golden rainclouds of Meghalaya."
    },
    {
        "khasi_name": "Ka Sim-khaleng",
        "common_name": "Black Kite / Mountain Eagle",
        "scientific_name": "Milvus migrans",
        "class_type": "Bird",
        "status": "Least Concern",
        "habitat": "Thermal updrafts above highland cliffs and open valleys",
        "cultural_significance": "Symbol of soaring freedom; featured in philosophical Khasi proverbs on perspective and vision."
    },
    {
        "khasi_name": "Ka Sim-tyngwieng",
        "common_name": "Mountain Bulbul",
        "scientific_name": "Ixos mcclellandii",
        "class_type": "Bird",
        "status": "Least Concern",
        "habitat": "Broadleaved evergreen hill forests",
        "cultural_significance": "Melodious songster whose lively notes accompany travelers along misty pine trails."
    },
    {
        "khasi_name": "Ka Sim-puh-dieng",
        "common_name": "Great Slaty Woodpecker",
        "scientific_name": "Mulleripicus pulverulentus",
        "class_type": "Bird",
        "status": "Vulnerable",
        "habitat": "Mature dipterocarp and oak forests",
        "cultural_significance": "Largest woodpecker in Asia; rhythmic tapping on hollow trunks regarded as the drumbeat of the forest."
    },
    {
        "khasi_name": "Ka Sim-lyngdoh",
        "common_name": "White-throated Fantail",
        "scientific_name": "Rhipidura albicollis",
        "class_type": "Bird",
        "status": "Least Concern",
        "habitat": "Undergrowth of moist mountain ravines",
        "cultural_significance": "Graceful fan-tail aerial dances resemble the flowing silk scarves of Shad Suk Mynsiem dancers."
    },
    {
        "khasi_name": "Ka Dkhait",
        "common_name": "Spotted Dove",
        "scientific_name": "Spilopelia chinensis",
        "family": "Columbidae",
        "class_type": "Bird",
        "status": "Least Concern",
        "habitat": "Homesteads, grain threshing floors, and open woodlands",
        "cultural_significance": "Gentle cooing represents peace, domestic tranquility, and matrimonial fidelity in Khasi songs."
    },
    {
        "khasi_name": "Ka Phreit",
        "common_name": "White-rumped Munia",
        "scientific_name": "Lonchura striata",
        "class_type": "Bird",
        "status": "Least Concern",
        "habitat": "Terrace paddies, grassy fallows, and bamboo brakes",
        "cultural_significance": "Tiny communal grain-eaters featured in harvest songs teaching children to share village bounty."
    },
    {
        "khasi_name": "Ka Sim-pyllieng",
        "common_name": "Blue Whistling Thrush",
        "scientific_name": "Myophonus caeruleus",
        "class_type": "Bird",
        "status": "Least Concern",
        "habitat": "Bouldered mountain torrents and misty waterfall gorges",
        "cultural_significance": "Dark violet-blue plumage; dawn whistling notes heard above the roar of mountain cataracts."
    },
    {
        "khasi_name": "Ka Muka-sim",
        "common_name": "Common Cuckoo",
        "scientific_name": "Cuculus canorus",
        "class_type": "Bird",
        "status": "Least Concern",
        "habitat": "Highland pine groves and open woods",
        "cultural_significance": "Seasonal arrival in April signals the exact moment to sow maize and mountain rice."
    },
    {
        "khasi_name": "Ka Sim-soh-khlur",
        "common_name": "Scarlet Minivet",
        "scientific_name": "Pericrocotus speciosus",
        "class_type": "Bird",
        "status": "Least Concern",
        "habitat": "High tree canopies across hill ranges",
        "cultural_significance": "Flocks of dazzling flame-red males and yellow females described as flying sparks of forest fire."
    },
    {
        "khasi_name": "Ka Khlieng",
        "common_name": "Crested Serpent Eagle",
        "scientific_name": "Spilornis cheela",
        "class_type": "Bird",
        "status": "Least Concern",
        "habitat": "Forested hills and riverine valleys",
        "cultural_significance": "Mighty raptor known for hunting venomous snakes; respected as a protector against reptile peril."
    },
    {
        "khasi_name": "Ka Sim-iap-ngi",
        "common_name": "Eastern Grass Owl / Barn Owl",
        "scientific_name": "Tyto longimembris",
        "class_type": "Bird",
        "status": "Least Concern",
        "habitat": "Tall highland grasslands and abandoned stone granaries",
        "cultural_significance": "Nocturnal silence and heart-shaped face; revered as a messenger of nocturnal secrets."
    },
    {
        "khasi_name": "Ka Sim-lieh",
        "common_name": "Little Egret",
        "scientific_name": "Egretta garzetta",
        "class_type": "Bird",
        "status": "Least Concern",
        "habitat": "Valley wetlands, river shallows, and wet rice fields",
        "cultural_significance": "Dazzling white plumage; symbol of moral innocence and purity of spirit."
    },
    {
        "khasi_name": "Ka Sim-kordor",
        "common_name": "Fire-tailed Sunbird",
        "scientific_name": "Aethopyga ignicauda",
        "class_type": "Bird",
        "status": "Least Concern",
        "habitat": "Rhododendron scrub and high elevation mossy forests",
        "cultural_significance": "Miniature avian gem sipping nectar from mountain orchids and rhododendron blooms."
    },
    {
        "khasi_name": "Ka Sim-jri",
        "common_name": "Asian Koel",
        "scientific_name": "Eudynamys scolopaceus",
        "class_type": "Bird",
        "status": "Least Concern",
        "habitat": "Subtropical garden groves and sacred banyans",
        "cultural_significance": "Celebrated in poetry for its melodic crescendo calls during warm summer rains."
    },
    {
        "khasi_name": "Ka Kbeit",
        "common_name": "Peregrine Falcon",
        "scientific_name": "Falco peregrinus",
        "class_type": "Bird",
        "status": "Least Concern",
        "habitat": "Precipitous sandstone cliffs of Cherrapunjee",
        "cultural_significance": "Fastest creature on earth; emblem of lightning speed and piercing precision."
    },
    {
        "khasi_name": "Ka Sim-blang",
        "common_name": "Pied Kingfisher",
        "scientific_name": "Ceryle rudis",
        "class_type": "Bird",
        "status": "Least Concern",
        "habitat": "River estuaries and highland clear pools",
        "cultural_significance": "Hovering above calm waters before vertical dives; archetype of patient concentration."
    },
    {
        "khasi_name": "Ka Sim-kba",
        "common_name": "Red Junglefowl",
        "scientific_name": "Gallus gallus",
        "class_type": "Bird",
        "status": "Least Concern",
        "habitat": "Bamboo brakes and dense scrub borders",
        "cultural_significance": "Wild ancestor of domestic rooster (U 'Iar Krad-Lyngkha), the sacred mediator in Khasi cosmology."
    },
    {
        "khasi_name": "Ka Radhad",
        "common_name": "Asian Emerald Dove",
        "scientific_name": "Chalcophaps indica",
        "class_type": "Bird",
        "status": "Least Concern",
        "habitat": "Undergrowth of wet evergreen forests",
        "cultural_significance": "Iridescent emerald-green back; quiet ground forager evoking forest seclusion."
    },
    {
        "khasi_name": "U Bsein-thlen",
        "common_name": "Indian Rock Python / Mythological Dragon Serpent",
        "scientific_name": "Python molurus",
        "class_type": "Reptile",
        "status": "Vulnerable / Central to Khasi Folk Demonology",
        "habitat": "Deep subterranean caves and limestone ravines",
        "cultural_significance": "In Khasi folklore, U Thlen is the demonic insatiable serpent slain by U Suidnoh at Dainthlen Falls."
    },
    {
        "khasi_name": "U Bsein-kynbat",
        "common_name": "White-lipped Green Pit Viper",
        "scientific_name": "Trimeresurus albolabris",
        "class_type": "Reptile",
        "status": "Least Concern",
        "habitat": "Low bushes, tea plantations, and bamboo clumps",
        "cultural_significance": "Vivid green venomous snake; respected by hill foragers who carry bamboo walking sticks."
    },
    {
        "khasi_name": "U Bsein-saw",
        "common_name": "Banded Krait",
        "scientific_name": "Bungarus fasciatus",
        "class_type": "Reptile",
        "status": "Least Concern",
        "habitat": "Moist lowlands, river valleys, and paddy dykes",
        "cultural_significance": "Strap-striped black and gold nocturnal serpent; revered for its lethally potent venom."
    },
    {
        "khasi_name": "U Bsein-eit-masi",
        "common_name": "King Cobra",
        "scientific_name": "Ophiophagus hannah",
        "class_type": "Reptile",
        "status": "Vulnerable",
        "habitat": "Deep wet rainforests of southern Meghalaya gorges",
        "cultural_significance": "Longest venomous snake in the world; respected with deep superstitious dread and reverence."
    },
    {
        "khasi_name": "Ka Niang-bshiah",
        "common_name": "Tokay Gecko",
        "scientific_name": "Gekko gecko",
        "class_type": "Reptile",
        "status": "Least Concern",
        "habitat": "Rocky limestone cliffs and wooden cottage walls",
        "cultural_significance": "Loud staccato mating cry ('To-kay!') believed to bring good fortune and rain to households."
    },
    {
        "khasi_name": "Ka Niang-thylliej",
        "common_name": "Oriental Garden Lizard / Bloodsucker",
        "scientific_name": "Calotes versicolor",
        "class_type": "Reptile",
        "status": "Least Concern",
        "habitat": "Sunny garden hedges, stone walls, and tree trunks",
        "cultural_significance": "Male turns crimson-headed during breeding display; subject of children's rhyming games."
    },
    {
        "khasi_name": "Ka Dkar",
        "common_name": "Assam Roofed Turtle",
        "scientific_name": "Pangshura sylhetensis",
        "class_type": "Reptile",
        "status": "Critically Endangered",
        "habitat": "Clear, fast-flowing hill rivers with sandy banks",
        "cultural_significance": "Spiky-shelled aquatic turtle endemic to the streams of Meghalaya and Barak Valley."
    },
    {
        "khasi_name": "Ka Jakoid-khlaw",
        "common_name": "Torrent Cascades Frog",
        "scientific_name": "Amolops kohimaensis",
        "class_type": "Amphibian",
        "status": "Least Concern",
        "habitat": "Raging mountain torrents and vertical wet rocks",
        "cultural_significance": "Possesses specialized abdominal suckers to cling to rocks amidst roaring waterfalls."
    },
    {
        "khasi_name": "Ka Jakoid-maw",
        "common_name": "Mawphlang Cascade Rock Frog",
        "scientific_name": "Odorrana mawphlangensis",
        "class_type": "Amphibian",
        "status": "Endemic to Meghalaya",
        "habitat": "Sacred grove streams of Mawphlang",
        "cultural_significance": "Named after the historic Khasi village and sacred forest of Mawphlang."
    },
    {
        "khasi_name": "Ka Jakoid-dieng",
        "common_name": "Highland Flying Tree Frog",
        "scientific_name": "Rhacophorus smaragdinus",
        "class_type": "Amphibian",
        "status": "Near Threatened",
        "habitat": "Canopy foliage above mountain ponds",
        "cultural_significance": "Extensive webbing on toes allows it to glide between high forest branches; builds foam nests."
    },
    {
        "khasi_name": "Ka Kha-saw",
        "common_name": "Golden Mahseer / Red Mahseer",
        "scientific_name": "Tor putitora",
        "class_type": "Fish",
        "status": "Endangered / King of River Fish",
        "habitat": "Deep crystal pools and rapid torrents (Umngot, Wahkaba)",
        "cultural_significance": "Legendary sport fish of pristine Meghalaya rivers; protected in sacred river sanctuaries (Fish Sanctuaries)."
    },
    {
        "khasi_name": "Ka Kha-ko",
        "common_name": "Chocolate Mahseer / Copper Mahseer",
        "scientific_name": "Neolissochilus hexagonolepis",
        "class_type": "Fish",
        "status": "Near Threatened",
        "habitat": "Clear, cold gravelly mountain streams",
        "cultural_significance": "Prized river catch celebrated in traditional smoked fish feasts."
    },
    {
        "khasi_name": "Ka Kha-bah",
        "common_name": "Goonch Giant Catfish",
        "scientific_name": "Bagarius yarrelli",
        "class_type": "Fish",
        "status": "Vulnerable",
        "habitat": "Deep turbulent river gorges and boulder undercuts",
        "cultural_significance": "Giant prehistoric-looking predatory catfish spoken of in river crossing folktales."
    },
    {
        "khasi_name": "Ka Kha-spah",
        "common_name": "Meghalaya Blind Cave Fish",
        "scientific_name": "Neolissochilus pnar",
        "class_type": "Fish",
        "status": "Critically Endangered / Subterranean Wonder",
        "habitat": "Deep subterranean limestone water caves in Jaintia Hills",
        "cultural_significance": "World's largest subterranean cave-adapted fish, scientifically named 'pnar' in honour of the indigenous people."
    },
    {
        "khasi_name": "Ka Kha-tngan",
        "common_name": "Assamese Snakehead",
        "scientific_name": "Channa stewartii",
        "class_type": "Fish",
        "status": "Least Concern",
        "habitat": "Mountain streams, swampy ditches, and rice canals",
        "cultural_significance": "Hardy air-breathing fish capable of traveling across wet grass; traditional delicacy."
    },
    {
        "khasi_name": "Ka Thapbalieh",
        "common_name": "Kaiser-i-Hind Butterfly",
        "scientific_name": "Teinopalpus imperialis",
        "class_type": "Insect",
        "status": "Near Threatened / Schedule II Protected",
        "habitat": "High montane cloud forest canopies (1,800m - 2,500m)",
        "cultural_significance": "Spectacular iridescent emerald swallowtail with golden trailing tails; jewel of the Khasi mountain peaks."
    },
    {
        "khasi_name": "Ka Niang-tari",
        "common_name": "Highland Singing Cicada",
        "scientific_name": "Chremistica mixta",
        "class_type": "Insect",
        "status": "Least Concern",
        "habitat": "Oak and pine tree trunks",
        "cultural_significance": "Its electric crescendo chorus marks the hottest hours of pre-monsoon summer."
    },
    {
        "khasi_name": "Ka Ngap-khlaw",
        "common_name": "Giant Rock Honeybee",
        "scientific_name": "Apis dorsata",
        "class_type": "Insect",
        "status": "Wild Keystone Pollinator",
        "habitat": "Vertical limestone cliff overhangs",
        "cultural_significance": "Hangs enormous semicircular honey combs under cliffs; wild honey traditionally harvested using rope ladders."
    },
    {
        "khasi_name": "Ka Niang-lartham",
        "common_name": "Giant Forest Scorpion",
        "scientific_name": "Heterometrus swammerdami",
        "class_type": "Invertebrate",
        "status": "Least Concern",
        "habitat": "Under moist rotten logs and stone crevices",
        "cultural_significance": "Ancient arachnid; cautionary symbol in folklore against sudden malice or spite."
    },
    {
        "khasi_name": "Ka Niang-bshiat",
        "common_name": "Praying Mantis",
        "scientific_name": "Mantis religiosa",
        "class_type": "Insect",
        "status": "Least Concern",
        "habitat": "Shrubs, garden crops, and tall grasslands",
        "cultural_significance": "Folded forelimbs look like prayer (Tip-Blei); admired for supreme stillness before striking."
    },
    {
        "khasi_name": "U Dkhiew-khlaw",
        "common_name": "Asian Weaver Ant",
        "scientific_name": "Oecophylla smaragdina",
        "class_type": "Insect",
        "status": "Abundant",
        "habitat": "Broadleaved forest tree canopies",
        "cultural_significance": "Weaves living leaf nests with larval silk; nests harvested in foothills for sour chutney rich in formic acid."
    },
    {
        "khasi_name": "U Shrieh-hoolock",
        "common_name": "Western Hoolock Gibbon",
        "scientific_name": "Hoolock hoolock",
        "class_type": "Mammal",
        "status": "Endangered / Schedule I Protected",
        "habitat": "Contiguous canopy of dense subtropical evergreen forests",
        "cultural_significance": "India's only ape; its resonant morning duet echoes across sacred groves and valleys; taboo to harm in Khasi tradition."
    },
    {
        "khasi_name": "U 'Kyndad / U 'Miaw-khlaw",
        "common_name": "Binturong / Asian Bearcat",
        "scientific_name": "Arctictis binturong",
        "class_type": "Mammal",
        "status": "Vulnerable",
        "habitat": "High canopy of old-growth rainforests",
        "cultural_significance": "Nocturnal arboreal civet with a prehensile tail and popcorn-like musk scent; mysterious figure in folktales."
    },
    {
        "khasi_name": "U 'Masi-prut",
        "common_name": "Gaur / Indian Wild Bison",
        "scientific_name": "Bos gaurus",
        "class_type": "Mammal",
        "status": "Vulnerable / Schedule I",
        "habitat": "Foothills and bamboo forests of Ri-Bhoi",
        "cultural_significance": "Colossal bovine admired for supreme muscular power and peaceful majesty; horn used in traditional signal horns."
    },
    {
        "khasi_name": "U 'Dkhoh",
        "common_name": "Brown Fish Owl",
        "scientific_name": "Ketupa zeylonensis",
        "family": "Strigidae",
        "class_type": "Bird",
        "status": "Least Concern",
        "habitat": "Riverside trees in rocky limestone valleys",
        "cultural_significance": "Deep resonant hoot heard along gorges; respected as a nocturnal guardian watcher of forest streams."
    },
    {
        "khasi_name": "U 'Sier-stem",
        "common_name": "Indian Muntjac / Barking Deer",
        "scientific_name": "Muntiacus muntjak",
        "class_type": "Mammal",
        "status": "Least Concern",
        "habitat": "Dense scrub and deep river ravines",
        "cultural_significance": "Its sharp dog-like alarm bark warns all forest animals of approaching leopards or tigers."
    },
    {
        "khasi_name": "U 'Rngai",
        "common_name": "Leopard Cat",
        "scientific_name": "Prionailurus bengalensis",
        "class_type": "Mammal",
        "status": "Least Concern / Schedule I",
        "habitat": "Oak forests, sacred groves, and village scrub",
        "cultural_significance": "Agile nocturnal hunter with golden rosettes; frequent trickster hero in village fable traditions."
    },
    {
        "khasi_name": "Ka Dohkha-saw",
        "common_name": "Golden Himalayan Mahseer",
        "scientific_name": "Tor putitora",
        "class_type": "Fish",
        "status": "Endangered",
        "habitat": "Fast-flowing, cold boulder-strewn rivers (Umngot, Myntdu)",
        "cultural_significance": "The king of mountain rivers; revered in village community fish sanctuaries (e.g. Nongbareh) where feeding is a sacred custom."
    },
    {
        "khasi_name": "U 'Gnor",
        "common_name": "Indian Pangolin / Scaly Anteater",
        "scientific_name": "Manis crassicaudata",
        "class_type": "Mammal",
        "status": "Critically Endangered",
        "habitat": "Burrows in lateritic hill soils and scrub forests",
        "cultural_significance": "Armored mammal capable of rolling into an impenetrable sphere; protected under strict customary taboos."
    },
    {
        "khasi_name": "U 'Jakoid-maw",
        "common_name": "Cascade Torrent Frog",
        "scientific_name": "Amolops formosus",
        "class_type": "Amphibian",
        "status": "Least Concern",
        "habitat": "Mossy boulders in the spray zones of waterfalls",
        "cultural_significance": "Equipped with powerful toe-discs to cling to vertical wet rock amidst roaring torrents."
    },
    {
        "khasi_name": "Ka Sim-pyllieng",
        "common_name": "Himalayan Cuckoo",
        "scientific_name": "Cuculus saturatus",
        "class_type": "Bird",
        "status": "Migratory Resident",
        "habitat": "Conifer and mixed oak-pine canopies",
        "cultural_significance": "Its fluting hollow call in April signals the arrival of spring rains and the time for clearing hill farms."
    },
    {
        "khasi_name": "U Jalyeit",
        "common_name": "Khasi Land Snail / Mollusk",
        "scientific_name": "Macrochlamys sp.",
        "class_type": "Mollusk",
        "status": "Common",
        "habitat": "Moist temperate oak-pine forest litter",
        "cultural_significance": "Contrasted humorously with edible wild greens in folk anecdotes (Minimon Laloo) as a living soil dweller."
    },
    {
        "khasi_name": "Ka Sim-pyllieng",
        "common_name": "Spotted Dove",
        "scientific_name": "Spilopelia chinensis",
        "class_type": "Bird",
        "status": "Least Concern",
        "habitat": "Open woods, village farmland, sacred groves",
        "cultural_significance": "Its gentle rhythmic cooing heralds peaceful autumn days and harvest season across the Khasi plateau."
    },
    {
        "khasi_name": "U Kyllap",
        "common_name": "Mountain Bamboo Partridge",
        "scientific_name": "Bambusicola fytchii",
        "class_type": "Bird",
        "status": "Least Concern",
        "habitat": "Dense hill bamboo brakes and steep valley slopes",
        "cultural_significance": "Reclusive ground bird celebrated in mountain hunters' phawar and forest lore."
    },
    {
        "khasi_name": "U Kha-koit",
        "common_name": "Torrent Hill Stream Loach",
        "scientific_name": "Schistura sikmaiensis",
        "class_type": "Fish",
        "status": "Native Stream Species",
        "habitat": "Clear fast-flowing boulder streams of the Khasi & Jaintia Hills",
        "cultural_significance": "Indicator species of clean river ecosystems, gathered in traditional stone fish weirs."
    }
]

def list_wildlife() -> List[Dict[str, Any]]:
    """Return all catalogued indigenous Khasi wildlife, mammals, birds, reptiles, fish, and insects."""
    return WILDLIFE

def get_animal(name: str) -> Optional[Dict[str, Any]]:
    """Lookup an animal by Khasi name, common name, or scientific binomial name."""
    q = name.lower().strip()
    for a in WILDLIFE:
        if (q in a["khasi_name"].lower() or
            q in a["common_name"].lower() or
            q in a["scientific_name"].lower()):
            return a
    return None

def by_class(class_type: str) -> List[Dict[str, Any]]:
    """Filter wildlife by class type (e.g., 'Mammal', 'Bird', 'Reptile', 'Amphibian', 'Fish', 'Insect')."""
    ct = class_type.lower().strip()
    return [a for a in WILDLIFE if ct in a["class_type"].lower()]

def search_wildlife(query: str) -> List[Dict[str, Any]]:
    """Search wildlife by keyword across all zoological fields."""
    q = query.lower().strip()
    return [a for a in WILDLIFE if (
        q in a["khasi_name"].lower() or
        q in a["common_name"].lower() or
        q in a["scientific_name"].lower() or
        q in a["class_type"].lower() or
        q in a["cultural_significance"].lower() or
        q in a["habitat"].lower()
    )]

def total_wildlife() -> int:
    """Return total count of catalogued fauna species."""
    return len(WILDLIFE)
