# -*- coding: utf-8 -*-
"""
Khasi Indigenous Roots (Ki Ktien Tynrai) & Phonaesthetic Expressives (Ki Ktien Pynshai Dur).
Documented from authentic Austroasiatic, Mon-Khmer, and Khasi ethnolinguistic authorities:
- Mon-Khmer Studies & Austroasiatic Comparative Lexica (Shorto, Diffloth, Nagaraja)
- Ka Ktien Khasi bad Ki Ktien Kynnoh (U Radhon Singh Berry, 1903)
- Ka Niam Jong Ki Khasi (Babu Jeebon Roy, 1897)
- Khasi Phonaesthetics and Expressives (Eugénie Henderson, Lili Rabel, K.S. Nagaraja)
"""

from typing import Dict, List, Any, Optional

INDIGENOUS_ROOTS: List[Dict[str, Any]] = [
    # --- Anatomy & Body ---
    {
        "root": "khmat",
        "english": "eye",
        "hindi": "आँख / नेत्र",
        "pos": "noun",
        "gender": "ka",
        "category": "anatomy",
        "austroasiatic_family": "Mon-Khmer core cognate (Mon 'mat', Khmer 'phnek/mat', Vietnamese 'mắt')",
        "derived_forms": ["peit khmat (to gaze)", "khmat-sngi (face of the sun)", "mar-khmat (face-to-face)"],
        "cultural_note": "Symbol of discernment, vigilance, and truth."
    },
    {
        "root": "shkor",
        "english": "ear",
        "hindi": "कान / कर्ण",
        "pos": "noun",
        "gender": "ka",
        "category": "anatomy",
        "austroasiatic_family": "Proto-Khasian root (Pnar 'shkor', War 'skor')",
        "derived_forms": ["shah-shkor (to heed/listen)", "kpieng-shkor (earrings)", "sngap-shkor (to listen attentively)"],
        "cultural_note": "Revered as the gateway to receiving oral wisdom and ancestral proverbs (Ki Ktien Tymmen)."
    },
    {
        "root": "khmut",
        "english": "nose",
        "hindi": "नाक / नासिका",
        "pos": "noun",
        "gender": "ka",
        "category": "anatomy",
        "austroasiatic_family": "Mon-Khmer (Mon 'muh', Khmer 'crmoh')",
        "derived_forms": ["iw-khmut (to smell)", "khmut-lum (ridge of a hill)"],
        "cultural_note": "Associated with pride and perception of character."
    },
    {
        "root": "ktien",
        "english": "mouth, word, language, speech",
        "hindi": "मुँह / शब्द / भाषा / बोली",
        "pos": "noun",
        "gender": "ka",
        "category": "anatomy_linguistics",
        "austroasiatic_family": "Proto-Khasian *ktien (Pnar 'ktien', War 'tien', Bhoi 'ktien')",
        "derived_forms": ["kren-ktien (to speak)", "ktien-tymmen (proverb/elder word)", "ka ktien khasi (the Khasi language)", "ktien-kynnoh (rhymed idiom)"],
        "cultural_note": "Central concept of Khasi identity: Ka Ktien is the soul of matrilineal transmission."
    },
    {
        "root": "bniat",
        "english": "tooth, teeth",
        "hindi": "दाँत / दंत",
        "pos": "noun",
        "gender": "ka",
        "category": "anatomy",
        "austroasiatic_family": "Mon-Khmer cognate (Mon 'bnéak')",
        "derived_forms": ["bniat-hati (ivory)", "dait-bniat (to gnash teeth)"],
        "cultural_note": "Blackened teeth from chewing kwai (areca and betel) were historically esteemed as a sign of adulthood."
    },
    {
        "root": "thylliej",
        "english": "tongue",
        "hindi": "जीभ / जिह्वा",
        "pos": "noun",
        "gender": "u",
        "category": "anatomy",
        "austroasiatic_family": "Mon-Khmer (Mon 'lateak', Khmer 'andaat')",
        "derived_forms": ["thylliej ding (tongue of fire / flame)", "kren da u thylliej (to articulate clearly)"],
        "cultural_note": "In cosmology, the tongue represents covenant veracity (Ka Jutang)."
    },
    {
        "root": "kti",
        "english": "hand, arm",
        "hindi": "हाथ / भुजा",
        "pos": "noun",
        "gender": "ka",
        "category": "anatomy",
        "austroasiatic_family": "Mon-Khmer core cognate (Mon 'tai', Khmer 'dai', Vietnamese 'tay')",
        "derived_forms": ["khun-kti (descendants/offspring)", "kynmaw-kti (signature/handmark)", "trei-kti (manual labor)"],
        "cultural_note": "Associated with industrious labor and hospitality."
    },
    {
        "root": "kjat",
        "english": "foot, leg",
        "hindi": "पैर / पाँव / चरण",
        "pos": "noun",
        "gender": "ka",
        "category": "anatomy",
        "austroasiatic_family": "Proto-Khasian (Pnar 'kjat', War 'kjet')",
        "derived_forms": ["kjat-sngi (sunbeams/sunrays)", "iaid-kjat (to travel on foot)", "kjat-lum (foothills)"],
        "cultural_note": "Footwork in dance (Ka Shad) connects human rhythm with Mother Earth (Ka Mei-Ramew)."
    },
    {
        "root": "doh",
        "english": "flesh, meat, skin",
        "hindi": "मांस / देह",
        "pos": "noun",
        "gender": "ka",
        "category": "anatomy_culinary",
        "austroasiatic_family": "Proto-Khasian (Pnar 'doh', War 'doh')",
        "derived_forms": ["dohkha (fish)", "dohsniang (pork)", "dohsyiar (chicken)", "kur-doh (consanguineous clan kin)"],
        "cultural_note": "Used both for physical flesh and maternal biological kinship."
    },
    {
        "root": "snam",
        "english": "blood",
        "hindi": "रक्त / खून",
        "pos": "noun",
        "gender": "ka",
        "category": "anatomy_kinship",
        "austroasiatic_family": "Mon-Khmer core root (Mon 'chim', Khmer 'chheam', Bahnaric 'maham')",
        "derived_forms": ["shi-snam (of one blood / maternal siblings)", "mih-snam (bleeding)"],
        "cultural_note": "The maternal bloodline (Ka Kpoh) is transmitted exclusively through the mother."
    },
    {
        "root": "shyieng",
        "english": "bone, seed kernel",
        "hindi": "हड्डी / अस्थि / बीज",
        "pos": "noun",
        "gender": "ka",
        "category": "anatomy_sacred",
        "austroasiatic_family": "Proto-Khasian *shyieng",
        "derived_forms": ["thep-shyieng (bone internment rite)", "shyieng-mawbah (ancestral megalith bones)", "shyieng-soh (fruit seed)"],
        "cultural_note": "Cremated bone relics are the central focus of the clan's highest funerary rite (Thep Mawbah)."
    },
    {
        "root": "klong-sngi",
        "english": "heart (anatomical and spiritual)",
        "hindi": "हृदय / दिल",
        "pos": "noun",
        "gender": "u",
        "category": "anatomy_spirituality",
        "austroasiatic_family": "Compound of klong (sacred gourd/vessel) + sngi (sun)",
        "derived_forms": ["klong-kjat (calf muscle)", "khih u klong-sngi (heart palpitation)"],
        "cultural_note": "Considered the inner sun and seat of conscience where God (U Blei) whispers truth."
    },
    {
        "root": "kpoh",
        "english": "womb, belly, matrilineal clan branch",
        "hindi": "गर्भ / कोख / उदर / मातृवंशीय शाखा",
        "pos": "noun",
        "gender": "ka",
        "category": "anatomy_kinship",
        "austroasiatic_family": "Proto-Khasian *kpoh (Pnar 'kpooh', War 'kpoh')",
        "derived_forms": ["shi-kpoh (of the same womb / uterine siblings)", "roi ka kpoh (prosperity of the clan line)", "pyniasoh-kpoh (clan adoption rite)"],
        "cultural_note": "The foundation of Khasi matriliny: all descendants trace origin to the womb of Ka Iawbei."
    },

    # --- Cosmos, Elements & Nature ---
    {
        "root": "sngi",
        "english": "sun, day, daytime",
        "hindi": "सूर्य / दिन",
        "pos": "noun",
        "gender": "ka",
        "category": "cosmos",
        "austroasiatic_family": "Mon-Khmer (Mon 'tŋi', Khmer 'tŋay', Stieng 'tŋey')",
        "derived_forms": ["ka sngi (the sun / female deity)", "shi-sngi (one full day)", "sngi-iew (market day)", "siatsngi (sunburst earrings)"],
        "cultural_note": "In Khasi cosmology, the sun is female (Ka Sngi)—the supreme maternal life-giver and mother of light."
    },
    {
        "root": "bnai",
        "english": "moon, month",
        "hindi": "चाँद / चंद्रमा / मास",
        "pos": "noun",
        "gender": "u",
        "category": "cosmos",
        "austroasiatic_family": "Mon-Khmer (Mon 'gnoa', Khmer 'khae', Bahnar 'khe')",
        "derived_forms": ["u bnai (the moon / younger brother)", "shi-bnai (one month)", "bnai-kdor (crescent moon)"],
        "cultural_note": "The moon is male (U Bnai), brother to the sun, ash-stained on his face for past transgression."
    },
    {
        "root": "khlur",
        "english": "star",
        "hindi": "तारा / नक्षत्र",
        "pos": "noun",
        "gender": "u",
        "category": "cosmos",
        "austroasiatic_family": "Proto-Khasian (Pnar 'khloor', War 'khlor')",
        "derived_forms": ["khlur-step (morning star / Venus)", "bun kum ki khlur (innumerable as the stars)"],
        "cultural_note": "Guides celestial travelers across the plateau."
    },
    {
        "root": "bneng",
        "english": "sky, heaven, firmament",
        "hindi": "आकाश / गगन / स्वर्ग",
        "pos": "noun",
        "gender": "ka",
        "category": "cosmos_theology",
        "austroasiatic_family": "Mon-Khmer root (Pnar 'bneeng', War 'bneng')",
        "derived_forms": ["lei-bneng (heavenly deity)", "suin-bneng (open sky / blue atmosphere)", "kiew sha bneng (to ascend to heaven)"],
        "cultural_note": "The celestial abode of U Blei (God Almighty) and ancestors who completed life in truth."
    },
    {
        "root": "khyndew",
        "english": "earth, soil, ground, land",
        "hindi": "भूमि / धरती / मिट्टी / ज़मीन",
        "pos": "noun",
        "gender": "ka",
        "category": "nature_law",
        "austroasiatic_family": "Compound of *khyn + *dew (earth/clay)",
        "derived_forms": ["mei-ramew (Mother Earth)", "ri-khyndew (ancestral homeland)", "dew-stem (sacred yellow clay)", "khyndew-kur (clan-held land)"],
        "cultural_note": "Sacred Mother Earth sustains all living beings; land cannot be permanently alienated from maternal clans."
    },
    {
        "root": "um",
        "english": "water, liquid, stream",
        "hindi": "जल / पानी / नीर",
        "pos": "noun",
        "gender": "ka",
        "category": "nature",
        "austroasiatic_family": "Mon-Khmer core root (Mon 'dàik', Khmer 'tœk', Vietnamese 'nước', Proto-Mon-Khmer *da:k / *?om)",
        "derived_forms": ["um-khuid (pure spring water)", "um-saw (flash flood / red river)", "dih-um (to drink water)", "kiad-um (rice wine libation)"],
        "cultural_note": "Water is the primal purifying agent in all Khasi sacrifices and life-cycle rituals."
    },
    {
        "root": "ding",
        "english": "fire, flame",
        "hindi": "अग्नि / आग",
        "pos": "noun",
        "gender": "ka",
        "category": "nature_sacred",
        "austroasiatic_family": "Proto-Khasian *ding (Pnar 'ding', War 'deng')",
        "derived_forms": ["dpei-ding (hearth fire)", "prei-ding (sparks)", "thang-ding (to burn with fire)"],
        "cultural_note": "The hearth fire (Ka Dpei) must never be entirely extinguished in a traditional Khasi household."
    },
    {
        "root": "lyer",
        "english": "wind, air, breeze",
        "hindi": "वायु / हवा / पवन",
        "pos": "noun",
        "gender": "ka",
        "category": "nature",
        "austroasiatic_family": "Mon-Khmer (Mon 'kya', Khmer 'khyol')",
        "derived_forms": ["lyer-khriat (cold highland wind)", "beh-lyer (wind blowing)", "pynhiar-mynsiem (breathing wind/spirit)"],
        "cultural_note": "Carries the voices of spirits and forest guardians (Ki Ryngkew Ki Basa)."
    },
    {
        "root": "lum",
        "english": "mountain, hill, highland",
        "hindi": "पहाड़ / पर्वत / चोटी",
        "pos": "noun",
        "gender": "u",
        "category": "geography",
        "austroasiatic_family": "Proto-Khasian *lum (Pnar 'loom', War 'lum')",
        "derived_forms": ["ri-lum (the Khasi Highlands)", "lum-shyllong (Shillong Peak)", "lum-diengiei (Diengiei Peak of the golden vine)"],
        "cultural_note": "High peaks are sovereign deities (Ki Lei Lum) who protect the territorial realms."
    },
    {
        "root": "wah",
        "english": "river, stream",
        "hindi": "नदी / सरिता / धारा",
        "pos": "noun",
        "gender": "ka",
        "category": "geography",
        "austroasiatic_family": "Proto-Khasian (Pnar 'waah', War 'wah')",
        "derived_forms": ["wah-umkhrah (Umkhrah river)", "wah-shella (Shella river)", "khap-wah (riverbank)"],
        "cultural_note": "Rivers form the sacred natural boundaries of indigenous Khasi kingdoms (Hima)."
    },
    {
        "root": "khlaw",
        "english": "forest, jungle, woods",
        "hindi": "जंगल / वन / अरण्य",
        "pos": "noun",
        "gender": "ka",
        "category": "nature",
        "austroasiatic_family": "Proto-Khasian (Pnar 'khloo', War 'khlaw')",
        "derived_forms": ["law-kyntang (sacred grove)", "law-adong (protected community forest)", "mrad-khlaw (wild beasts of the forest)"],
        "cultural_note": "Sacred groves (Law Kyntang) are inviolable sanctuaries where not even a twig may be plucked."
    },

    # --- Moral Philosophy & Customary Pillars ---
    {
        "root": "hok",
        "english": "righteousness, truth, justice, moral law",
        "hindi": "धर्म / सत्य / न्याय / नीति",
        "pos": "noun",
        "gender": "ka",
        "category": "philosophy",
        "austroasiatic_family": "Ancient Austroasiatic ethical base (Pnar 'hok', War 'hok')",
        "derived_forms": ["ba-hok (honest, just)", "kamai ia ka hok (earn righteousness - supreme ethical maxim)", "jinghok (divine justice)"],
        "cultural_note": "The first pillar of Khasi religion: human life is lived solely to earn righteousness before God."
    },
    {
        "root": "sot",
        "english": "integrity, uprightness, pure truth",
        "hindi": "सत्यनिष्ठा / निष्कपटता / शुचिता",
        "pos": "noun",
        "gender": "ka",
        "category": "philosophy",
        "austroasiatic_family": "Proto-Khasian ethical root",
        "derived_forms": ["ba-sot (chaste, pure, innocent)", "ki thei sotti (unmarried maidens of pure character)"],
        "cultural_note": "The prerequisite for entering the sacred dancing ring (Lympung) at Shad Suk Mynsiem."
    },
    {
        "root": "niam",
        "english": "religion, customary faith, liturgical order",
        "hindi": "धर्म / उपासना / रीति-रिवाज",
        "pos": "noun",
        "gender": "ka",
        "category": "religion",
        "austroasiatic_family": "Core Austroasiatic-Sanskritic religious loan blend (Pnar 'niam', War 'niam')",
        "derived_forms": ["ka niam tynrai (traditional indigenous Khasi religion)", "niam-khasi (Khasi faith)", "niam-iap (funerary rites)"],
        "cultural_note": "Encompasses faith, ceremonial rites, ethics, and social duties as an indivisible whole."
    },
    {
        "root": "riti",
        "english": "custom, constitutional law, unwritten code of ethics",
        "hindi": "प्रथा / रीति / परंपरा / विधान",
        "pos": "noun",
        "gender": "ka",
        "category": "customary_law",
        "austroasiatic_family": "Ancient indigenous legal tradition",
        "derived_forms": ["ka riti jong ka ri khasi (customary constitution of the Khasi people)", "katkum ka riti (according to traditional law)"],
        "cultural_note": "Governs clan elections of kings (Syiem), land tenures, and matrilineal inheritance."
    },
    {
        "root": "sang",
        "english": "cardinal taboo, incest, moral sacrilege",
        "hindi": "महापाप / वर्जना / गोत्र-व्यभिचार",
        "pos": "noun",
        "gender": "ka",
        "category": "ethics_taboo",
        "austroasiatic_family": "Proto-Khasian moral taboo root",
        "derived_forms": ["shong-sang (incestuous marriage within clan - cardinal sin)", "sang-kur (clan incest)", "sang-kha (paternal taboo violation)"],
        "cultural_note": "To commit Sang results in total excommunication from clan, loss of burial in Mawbah, and spiritual ruin."
    },
    {
        "root": "ma",
        "english": "peril, spiritual dread, ominous warning",
        "hindi": "भय / संकट / अपशकुन",
        "pos": "noun",
        "gender": "ka",
        "category": "ethics_taboo",
        "austroasiatic_family": "Proto-Khasian *ma",
        "derived_forms": ["ka sang ka ma (taboo and ominous consequence)", "sheptieng ka ma (fearing spiritual peril)"],
        "cultural_note": "Coupled with Sang as the dual warning system of traditional morality."
    },
    {
        "root": "rngiew",
        "english": "spiritual aura, personality, divine charisma, inner majesty",
        "hindi": "तेज / आत्मिक आभा / गरिमा / व्यक्तित्व",
        "pos": "noun",
        "gender": "ka",
        "category": "spiritual_psychology",
        "austroasiatic_family": "Unique Austroasiatic psychological concept",
        "derived_forms": ["khlain ka rngiew (strong protective spiritual aura)", "hiar ka rngiew (diminished spiritual power / vulnerable to evil)"],
        "cultural_note": "A person whose Rngiew is high cannot be harmed by black magic, sorcery, or U Thlen."
    },

    # --- Essential Verbs & Action Roots ---
    {
        "root": "im",
        "english": "to live, to be alive",
        "hindi": "जीना / जीवित रहना",
        "pos": "verb",
        "austroasiatic_family": "Mon-Khmer core verb root (Mon 'yim', Khmer 'rim')",
        "derived_forms": ["jingim (life)", "pynim (to save/revive)", "nongpynim (savior)", "ba-im (living/alive)"],
        "cultural_note": "The root of all vitality and creation."
    },
    {
        "root": "ïap",
        "english": "to die, perish, extinguish",
        "hindi": "मरना / मृत्यु पाना",
        "pos": "verb",
        "austroasiatic_family": "Mon-Khmer (Mon 'dap', Khmer 'slap')",
        "derived_forms": ["jingïap (death)", "iapduh (lineage extinction)", "shyieng-iap (mortal remains)"],
        "cultural_note": "In Khasi thought, physical death is merely the departure of the soul to eat betel nut in the courtyard of God (Bam Kwai ha Ïing U Blei)."
    },
    {
        "root": "tip",
        "english": "to know, perceive, understand, be conscious",
        "hindi": "जानना / समझना / बोध होना",
        "pos": "verb",
        "austroasiatic_family": "Proto-Khasian *tip (Pnar 'tip', War 'tep')",
        "derived_forms": ["jingtip (knowledge)", "tip-briew (knowing humanity / courtesy)", "tip-blei (knowing God / reverence)", "nongtip (sage/knower)"],
        "cultural_note": "Foundation of the second pillar: Tip-Briew Tip-Blei (To know man is to know God)."
    },
    {
        "root": "trei",
        "english": "to work, labor, accomplish, execute",
        "hindi": "कार्य करना / श्रम करना",
        "pos": "verb",
        "austroasiatic_family": "Proto-Khasian *trei (Pnar 'trei', War 'trei')",
        "derived_forms": ["jingtrei (work/job/task)", "nongtrei (worker/laborer)", "pyntrei-kam (to implement/execute)"],
        "cultural_note": "Work is viewed as active participation in the Creator's continuous cosmos."
    },
    {
        "root": "shong",
        "english": "to sit, dwell, reside, marry",
        "hindi": "बैठना / निवास करना / विवाह करना",
        "pos": "verb",
        "austroasiatic_family": "Mon-Khmer (Pnar 'shong', War 'shong')",
        "derived_forms": ["shnong (village/settlement)", "shongsah (to reside)", "shongkurim (to marry)", "jingshong-suk (peaceful dwelling)"],
        "cultural_note": "Notice 'shnong' (village) is morphologically derived via infix -n- from 'shong' (to sit/dwell)."
    },
    {
        "root": "kren",
        "english": "to speak, utter, converse",
        "hindi": "बोलना / बात करना / कहना",
        "pos": "verb",
        "austroasiatic_family": "Proto-Khasian (Pnar 'kren', War 'kren')",
        "derived_forms": ["jingkren (speech/discourse)", "nongkren (speaker/orator)", "kren-bha (to speak well of)"],
        "cultural_note": "Oratory (Ka Ktien Jingkren) in the Dorbar council is the highest masculine civic art."
    }
]

PHONAESTHETIC_EXPRESSIVES: List[Dict[str, Any]] = [
    # --- Light, Color & Visual Appearance ---
    {
        "expressive": "lieh phyrnai",
        "literal": "dazzling radiant white",
        "domain": "light_and_color",
        "english": "dazzling bright white, shimmering like fresh sunlight on limestone",
        "hindi": "चकाचौंध कर देने वाला चमकदार सफ़ेद",
        "usage_example": "Ka sopti ka ba lieh phyrnai (A dazzlingly radiant white shirt)",
        "nuance": "Denotes pristine luminescence and cleanliness."
    },
    {
        "expressive": "lieh pup",
        "literal": "chalky powdery white",
        "domain": "light_and_color",
        "english": "powdery chalk white, ashen or pale white",
        "hindi": "चाक जैसा सफ़ेद / अत्यधिक पीला-सफ़ेद",
        "usage_example": "U la kylla lieh pup na ka jingsheptieng (He turned ashen white from terror)",
        "nuance": "Used for shock, pallor, or dry powder."
    },
    {
        "expressive": "iong thiej",
        "literal": "pitch black, jet black",
        "domain": "light_and_color",
        "english": "deep pitch black, fathomless dark without reflection",
        "hindi": "घना गहरा काला / स्याह काला",
        "usage_example": "Ka miet kaba iong thiej (A pitch-black midnight)",
        "nuance": "Describes impenetrable obsidian darkness."
    },
    {
        "expressive": "iong tngit",
        "literal": "grimy sooty black",
        "domain": "light_and_color",
        "english": "dirty, sooty black like coal dust or chimney grime",
        "hindi": "मैला-कुचैला काला / कालिख जैसा",
        "usage_example": "Ki kti kiba iong tngit na ka rnga (Hands blackened with charcoal dust)",
        "nuance": "Implies uncleanness or soot."
    },
    {
        "expressive": "saw hynñiang",
        "literal": "vivid crimson blood-red",
        "domain": "light_and_color",
        "english": "deep intense blood-red or scarlet",
        "hindi": "गहरा रक्त जैसा लाल / सुर्ख लाल",
        "usage_example": "Ka snam kaba saw hynñiang (Deep crimson blood)",
        "nuance": "Denotes fresh blood, fiery sunrise, or ripe betel juice."
    },
    {
        "expressive": "stem mluh",
        "literal": "bright golden turmeric yellow",
        "domain": "light_and_color",
        "english": "vibrant, rich saffron or golden yellow",
        "hindi": "हल्दी जैसा चमकदार गहरा पीला",
        "usage_example": "Ka jaiñsem kaba stem mluh (A bright saffron-yellow silk jainsem)",
        "nuance": "Sacred festive color of purity in Khasi dances."
    },
    {
        "expressive": "jyrngam duk",
        "literal": "deep verdant forest green",
        "domain": "light_and_color",
        "english": "rich, lush, deep rainforest green",
        "hindi": "गहरा हरा / हरा-भरा सघन वन जैसा",
        "usage_example": "Ki lum kiba jyrngam duk ha lyiur (Hills lush with deep emerald green during monsoons)",
        "nuance": "Evokes fertile mountain vegetation."
    },
    {
        "expressive": "shai kdar",
        "literal": "crystal clear illumination",
        "domain": "light_and_color",
        "english": "crystal clear, brightly and transparently illuminated",
        "hindi": "बिल्कुल साफ़ / स्पष्ट रूप से प्रकाशित",
        "usage_example": "Ka sngi ka la shai kdar (The day has dawned crystal clear and bright)",
        "nuance": "Truth, intellectual clarity, and unclouded sky."
    },
    {
        "expressive": "dum kput",
        "literal": "pitch-dark blackness",
        "domain": "light_and_color",
        "english": "utterly dark, blindingly pitch dark with zero visibility",
        "hindi": "घोर अंधकार / घुप्प अंधेरा",
        "usage_example": "Ha krem ka dum kput (Inside the cave it is pitch black)",
        "nuance": "Total absence of light."
    },

    # --- Temperature & Physical Sensation ---
    {
        "expressive": "khluit thar",
        "literal": "scalding stinging hot",
        "domain": "temperature_sensation",
        "english": "scalding, boiling hot that stings on contact",
        "hindi": "खौलता हुआ / अत्यंत गर्म जिससे हाथ जल जाए",
        "usage_example": "Ka um-sha kaba khluit thar (Scalding piping-hot tea)",
        "nuance": "Instant searing heat."
    },
    {
        "expressive": "syaid lumbor",
        "literal": "comforting snug warmth",
        "domain": "temperature_sensation",
        "english": "pleasantly, soothingly warm and comfortable",
        "hindi": "सुखद गुनगुना / आरामदेह गर्माहट",
        "usage_example": "Ka dpei kaba syaid lumbor ha tlang (A hearth fire giving snug soothing warmth in winter)",
        "nuance": "Hearthside peace, security, and gentle temperature."
    },
    {
        "expressive": "khriat jur-jur",
        "literal": "biting shivering cold",
        "domain": "temperature_sensation",
        "english": "penetrating, shivering cold that makes one shudder",
        "hindi": "कंपकंपी छुड़ाने वाली कड़ाके की ठंड",
        "usage_example": "Ka lyer tlang kaba khriat jur-jur (Winter wind of shivering biting cold)",
        "nuance": "Sohra winter frost and mountain chill."
    },
    {
        "expressive": "pjah thait",
        "literal": "ice-cold clammy chill",
        "domain": "temperature_sensation",
        "english": "completely cold, icy, chilled to the marrow",
        "hindi": "बर्फ जैसा ठंडा / बिल्कुल ठंडा पड़ा हुआ",
        "usage_example": "Ka um-pukir kaba pjah thait (Spring water chilled like ice)",
        "nuance": "Mountain springs or lifeless chill."
    },
    {
        "expressive": "eh tian",
        "literal": "unyielding stone hard",
        "domain": "texture_sensation",
        "english": "solid, rock-hard, absolutely unyielding and rigid",
        "hindi": "पत्थर जैसा कठोर / अभेद्य कड़ा",
        "usage_example": "U mawleiphu uba eh tian (Granite rock solid and unyielding)",
        "nuance": "Unyielding firmness, determination, and megaliths."
    },
    {
        "expressive": "jem pudep",
        "literal": "pillow-soft and yielding",
        "domain": "texture_sensation",
        "english": "fluffy, pillow-soft, cushioned and yielding to touch",
        "hindi": "रुई जैसा कोमल / अत्यधिक मुलायम",
        "usage_example": "Ka syngkhlieh kaba jem pudep (A pillow delightfully soft and fluffy)",
        "nuance": "Gentle softness and comfort."
    },
    {
        "expressive": "stang rynghang",
        "literal": "whisper thin, gossamer translucent",
        "domain": "texture_sensation",
        "english": "paper-thin, gossamer and delicate",
        "hindi": "कागज़ जैसा पतला / झीना",
        "usage_example": "Ka kot-khubor kaba stang rynghang (Paper extremely thin)",
        "nuance": "Frail, fine, or delicate layer."
    },
    {
        "expressive": "rben khap-khap",
        "literal": "densely thick and heavy",
        "domain": "texture_sensation",
        "english": "substantially thick, dense, and closely woven",
        "hindi": "अत्यधिक मोटा और घना",
        "usage_example": "Ka jainkup kaba rben khap-khap (A mantle-shawl thick and dense against rain)",
        "nuance": "Thermal protection and quality handloom."
    },

    # --- Gait, Movement & Locomotion ---
    {
        "expressive": "iaid wiar-wiar",
        "literal": "walking with gliding maternal grace",
        "domain": "movement_gait",
        "english": "walking with slow, majestic, fluid, and dignified grace",
        "hindi": "धीमी, गरिमामयी और शालीन चाल से चलना",
        "usage_example": "Ka thei samla ka iaid wiar-wiar ha ka shad (The maiden walks with majestic graceful steps in dance)",
        "nuance": "Signature slow gliding step of Khasi female dancers in Shad Suk Mynsiem."
    },
    {
        "expressive": "iaid thwiat-thwiat",
        "literal": "walking briskly with purposeful stride",
        "domain": "movement_gait",
        "english": "walking briskly, energetically, and with urgent purpose",
        "hindi": "तेज़ कदमों से फुर्ती से चलना",
        "usage_example": "U leit sha iew da kaba iaid thwiat-thwiat (He heads to market walking with brisk energetic strides)",
        "nuance": "Highland hill-climbers and busy merchants."
    },
    {
        "expressive": "phet kyrthep",
        "literal": "running in panicked stampede",
        "domain": "movement_gait",
        "english": "fleeing helter-skelter in wild terrified stampede",
        "hindi": "घबराकर बदहवास भागना / भगदड़ मचना",
        "usage_example": "Ki sniang ki la phet kyrthep haba iohi ia ka khla (The pigs stampeded in panic when spotting the tiger)",
        "nuance": "Chaotic terrified flight."
    },
    {
        "expressive": "khih phet-phet",
        "literal": "quivering, trembling rapidly",
        "domain": "movement_gait",
        "english": "palpitating, trembling rapidly from fear or fever",
        "hindi": "थरथर कांपना / फड़कना",
        "usage_example": "Ki kti jong u ki la khih phet-phet na ka jingpang (His hands trembled rapidly from illness)",
        "nuance": "Rapid involuntary vibration."
    },
    {
        "expressive": "thiah lyng-ngai",
        "literal": "sleeping in serene, undisturbed tranquil bliss",
        "domain": "movement_gait",
        "english": "sleeping deeply, serenely, and peacefully without worry",
        "hindi": "बेफिक्र, शांत और गहरी नींद में सोना",
        "usage_example": "I khunlung i la thiah lyng-ngai ha ka thari (The infant sleeps in sweet tranquil peace in the cradle)",
        "nuance": "Complete contentment, spiritual rest, and safety."
    },

    # --- Acoustics, Voice & Emotion ---
    {
        "expressive": "sawa kdup-kdup",
        "literal": "deep rhythmic thumping sound",
        "domain": "acoustics_sound",
        "english": "dull, resonant, rhythmic thudding or pounding sound",
        "hindi": "धप-धप की गूंजती हुई आवाज़ / दिल की धड़कन जैसी थाप",
        "usage_example": "U ksing u sawa kdup-kdup ha lympung (The great drum echoes with heavy rhythmic thuds across the arena)",
        "nuance": "Drum beats or pounding of the heart in warrior dances."
    },
    {
        "expressive": "phuh mut-mut",
        "literal": "smiling with radiant, quiet joy",
        "domain": "emotion_expression",
        "english": "smiling serenely and gently, radiating subtle inner happiness",
        "hindi": "मंद-मंद मुस्कुराना / सौम्य प्रसन्नता से खिल उठना",
        "usage_example": "Ka kmie ka phuh mut-mut haba iohi ia la ki khun (The mother smiles with serene gentle joy beholding her children)",
        "nuance": "Warm, affectionate, unpretentious happiness."
    },
    {
        "expressive": "khmih pyrkhing",
        "literal": "scrutinizing with stern, grave solemnity",
        "domain": "emotion_expression",
        "english": "staring with severe, strict, and uncompromising gravity",
        "hindi": "गंभीरता और कड़ाई से घूरना / सख्त नज़र रखना",
        "usage_example": "U tymmen shnong u khmih pyrkhing ia ka kam (The village elder scrutinizes the matter with strict gravity)",
        "nuance": "Judicial authority and moral discipline."
    }
]

def list_indigenous_roots(category: Optional[str] = None) -> List[Dict[str, Any]]:
    """Return foundational Austroasiatic / Mon-Khmer Khasi root words (Ki Ktien Tynrai)."""
    if not category:
        return INDIGENOUS_ROOTS
    cat = category.lower().strip()
    return [r for r in INDIGENOUS_ROOTS if cat in r.get("category", "").lower()]

def get_indigenous_root(word: str) -> Optional[Dict[str, Any]]:
    """Find root word metadata by Khasi root or English name."""
    w = word.lower().strip()
    for r in INDIGENOUS_ROOTS:
        if (w == r["root"].lower() or
            w in r["english"].lower()):
            return r
    return None

def list_expressives(domain: Optional[str] = None) -> List[Dict[str, Any]]:
    """Return traditional Khasi phonaesthetic expressives and ideophones (Ki Ktien Pynshai Dur)."""
    if not domain:
        return PHONAESTHETIC_EXPRESSIVES
    d = domain.lower().strip()
    return [exp for exp in PHONAESTHETIC_EXPRESSIVES if d in exp.get("domain", "").lower()]

def get_expressive(query: str) -> Optional[Dict[str, Any]]:
    """Find a phonaesthetic expressive by Khasi phrase or English description."""
    q = query.lower().strip()
    for exp in PHONAESTHETIC_EXPRESSIVES:
        if (q == exp["expressive"].lower() or
            q in exp["expressive"].lower() or
            q in exp["english"].lower()):
            return exp
    return None

class TynraiManager:
    """Manager for indigenous Khasi roots and phonaesthetic expressives."""

    @property
    def roots(self) -> List[Dict[str, Any]]:
        return INDIGENOUS_ROOTS

    @property
    def expressives(self) -> List[Dict[str, Any]]:
        return PHONAESTHETIC_EXPRESSIVES

    def get_root(self, query: str) -> Optional[Dict[str, Any]]:
        return get_indigenous_root(query)

    def get_expressive(self, query: str) -> Optional[Dict[str, Any]]:
        return get_expressive(query)

    def search(self, query: str) -> List[Dict[str, Any]]:
        q = query.lower().strip()
        matches = []
        for r in INDIGENOUS_ROOTS:
            txt = f"{r.get('root', '')} {r.get('english', '')} {r.get('hindi', '')} {r.get('austroasiatic_family', '')}".lower()
            if q in txt:
                matches.append(r)
        for exp in PHONAESTHETIC_EXPRESSIVES:
            txt = f"{exp.get('expressive', '')} {exp.get('english', '')} {exp.get('hindi', '')} {exp.get('usage_example', '')}".lower()
            if q in txt:
                matches.append(exp)
        return matches

tynrai = TynraiManager()
