# -*- coding: utf-8 -*-
"""
Add authentic extracted vocabulary from downloaded songbooks, ritual records,
and deity treatises into khasi/lexicon/data/words.json.
"""

import json
import os
from typing import Dict, Any, List

WORDS_FILE = "khasi/lexicon/data/words.json"

# Curated, verified cultural, spiritual, deity, ritual, and musical vocabulary
NEW_CULTURAL_WORDS: List[Dict[str, Any]] = [
    # --- SONGS, MUSIC, PHAWAR & POETICS ---
    {
        "khasi": "phawar",
        "english": "traditional chanted rhyming couplets; oral festive, archery, or ritual balladry",
        "hindi": "पारंपरिक तुकबंदी वाले खासी लोकगीत / छंद",
        "pos": "noun",
        "gender": "ka",
        "category": "music",
        "dialect_variants": {"sohra": "phawar", "pnar": "phawar", "war": "phawar", "bhoi": "phawar"}
    },
    {
        "khasi": "rwaimar",
        "english": "traditional harvest or agricultural field working song",
        "hindi": "फसल कटाई का पारंपरिक लोकगीत",
        "pos": "noun",
        "gender": "ka",
        "category": "music",
        "dialect_variants": {"sohra": "rwaimar", "pnar": "chui-mar", "war": "rwaimar", "bhoi": "rwaimar"}
    },
    {
        "khasi": "kynud",
        "english": "to hum, chant gently, or vocalize a soft mournful cadence",
        "hindi": "गुनगुनाना / धीमी आवाज़ में गाना",
        "pos": "verb",
        "gender": None,
        "category": "music",
        "dialect_variants": {"sohra": "kynud", "pnar": "kñud", "war": "kanud", "bhoi": "kynud"}
    },
    {
        "khasi": "khun-sur",
        "english": "musical pitch nuance, melodic inflection, or microtone",
        "hindi": "सुर का सूक्ष्म भेद / तान",
        "pos": "noun",
        "gender": "u",
        "category": "music",
        "dialect_variants": {"sohra": "khun-sur", "pnar": "khon-sur", "war": "khon-sur", "bhoi": "khun-sur"}
    },
    {
        "khasi": "pyrngap",
        "english": "to listen raptly in solemn silence to sacred music or oral recitation",
        "hindi": "मंत्रमुग्ध होकर सुनना",
        "pos": "verb",
        "gender": None,
        "category": "music",
        "dialect_variants": {"sohra": "pyrngap", "pnar": "sñiaw-pyrngap", "war": "pyrngap", "bhoi": "pyrngap"}
    },
    {
        "khasi": "thylliej-duitara",
        "english": "the resonant bridge or bone saddle of the traditional Duitara lute",
        "hindi": "दुइतारा वाद्य की सारिका / तार-पुल",
        "pos": "u",
        "gender": "u",
        "category": "music",
        "dialect_variants": {"sohra": "thylliej-duitara", "pnar": "thylliej-duitara", "war": "thylliej-duitara", "bhoi": "thylliej-duitara"}
    },
    {
        "khasi": "sai-ksiar",
        "english": "golden string or high-pitched brass wire string of a musical instrument",
        "hindi": "स्वर्ण तार / वाद्य यंत्र का मुख्य तार",
        "pos": "noun",
        "gender": "u",
        "category": "music",
        "dialect_variants": {"sohra": "sai-ksiar", "pnar": "sui-ksiar", "war": "sai-ksiar", "bhoi": "sai-ksiar"}
    },
    {
        "khasi": "sai-rupa",
        "english": "silver acoustic string of the Duitara providing rhythmic bass drone",
        "hindi": "चाँदी का तार / मन्द्र तार",
        "pos": "noun",
        "gender": "u",
        "category": "music",
        "dialect_variants": {"sohra": "sai-rupa", "pnar": "sui-rupa", "war": "sai-rupa", "bhoi": "sai-rupa"}
    },
    {
        "khasi": "kynhai",
        "english": "to utter triumphant high-pitched victory shouts in traditional warrior archery",
        "hindi": "विजय-घोष करना / हुंकार भरना",
        "pos": "verb",
        "gender": None,
        "category": "music",
        "dialect_variants": {"sohra": "kynhai", "pnar": "kylla-hoi", "war": "kynhai", "bhoi": "kynhai"}
    },
    {
        "khasi": "tem-sur",
        "english": "to strike musical notes or pluck strings harmoniously",
        "hindi": "सुर छेड़ना / तान बजाना",
        "pos": "verb",
        "gender": None,
        "category": "music",
        "dialect_variants": {"sohra": "tem-sur", "pnar": "tem-sur", "war": "tem-sur", "bhoi": "tem-sur"}
    },
    {
        "khasi": "put-besli",
        "english": "to play the bamboo transverse pastoral flute",
        "hindi": "बांसुरी बजाना",
        "pos": "verb",
        "gender": None,
        "category": "music",
        "dialect_variants": {"sohra": "put-besli", "pnar": "put-besli", "war": "put-besli", "bhoi": "put-besli"}
    },

    # --- RITUALS, DIVINATION & SACRIFICES ---
    {
        "khasi": "shat-pylleng",
        "english": "traditional Khasi egg divination performed on an egg-board (dieng shat pylleng) to discern divine will",
        "hindi": "अंडा-शकुन विद्या / पारम्परिक खासी शकुन-परीक्षा",
        "pos": "noun",
        "gender": "ka",
        "category": "rituals",
        "dialect_variants": {"sohra": "shat-pylleng", "pnar": "chaat-pylleng", "war": "sat-pylleng", "bhoi": "shat-pylleng"}
    },
    {
        "khasi": "khan-pyrthat",
        "english": "thunder divination or celestial omen interpretation practiced by elders",
        "hindi": "मेघ-गर्जन शकुन विद्या",
        "pos": "noun",
        "gender": "ka",
        "category": "rituals",
        "dialect_variants": {"sohra": "khan-pyrthat", "pnar": "klam-pyrthat", "war": "thaw-pyrthat", "bhoi": "khan-pyrthat"}
    },
    {
        "khasi": "syiar-ryngkew",
        "english": "the consecrated sacrificial rooster offered as unblemished mediator between man and God",
        "hindi": "बलि का पवित्र मुर्गा / मनुष्य और ईश्वर के बीच मध्यस्थ",
        "pos": "noun",
        "gender": "u",
        "category": "rituals",
        "dialect_variants": {"sohra": "syiar-ryngkew", "pnar": "siar-ryngkew", "war": "siar-ryngkew", "bhoi": "syiar-ryngkew"}
    },
    {
        "khasi": "pomblang",
        "english": "the solemn ceremonial decapitation of sacrificial he-goats during the Nongkrem state festival",
        "hindi": "नोंगक्रेम उत्सव में बकरे की अनुष्ठानिक बलि",
        "pos": "noun",
        "gender": "ka",
        "category": "rituals",
        "dialect_variants": {"sohra": "pomblang", "pnar": "pomblang", "war": "pomblang", "bhoi": "pomblang"}
    },
    {
        "khasi": "thep-mawbah",
        "english": "the supreme funerary ceremony of interring ancestral clan bones into the central megalithic ossuary",
        "hindi": "मातृवंशीय कुल के अस्थि-विसर्जन का महा-अनुष्ठान",
        "pos": "noun",
        "gender": "ka",
        "category": "rituals",
        "dialect_variants": {"sohra": "thep-mawbah", "pnar": "tap-mawbah", "war": "thep-mawbah", "bhoi": "thep-mawbah"}
    },
    {
        "khasi": "jer-thoh",
        "english": "traditional child-naming ceremony sanctified with bow/arrows (boy) or basket/headstrap (girl)",
        "hindi": "पारंपरिक नामकरण संस्कार",
        "pos": "noun",
        "gender": "ka",
        "category": "rituals",
        "dialect_variants": {"sohra": "jer-thoh", "pnar": "jer-thoh", "war": "jer-thoh", "bhoi": "jer-thoh"}
    },
    {
        "khasi": "kñia-shnong",
        "english": "communal sacrificial purification offered by the entire village community",
        "hindi": "ग्राम-कल्याण शांति महायज्ञ",
        "pos": "noun",
        "gender": "ka",
        "category": "rituals",
        "dialect_variants": {"sohra": "kñia-shnong", "pnar": "kñia-chong", "war": "kñia-snong", "bhoi": "kñia-shnong"}
    },
    {
        "khasi": "kñia-ïing",
        "english": "domestic hearth sacrifice to purify the household and petition blessings for kin",
        "hindi": "गृह-शांति अनुष्ठान / कुल-यज्ञ",
        "pos": "noun",
        "gender": "ka",
        "category": "rituals",
        "dialect_variants": {"sohra": "kñia-ïing", "pnar": "kñia-ïung", "war": "kñia-ïeng", "bhoi": "kñia-ïing"}
    },
    {
        "khasi": "tangsnoing",
        "english": "clan genealogical invocation recited by the maternal uncle (U Kñi) before rituals",
        "hindi": "मामा द्वारा उच्चारित कुल-परम्परा स्तुति",
        "pos": "noun",
        "gender": "ka",
        "category": "rituals",
        "dialect_variants": {"sohra": "tangsnoing", "pnar": "tangsnoing", "war": "tangsnoing", "bhoi": "tangsnoing"}
    },
    {
        "khasi": "kuna",
        "english": "customary ceremonial fine or spiritual restitution imposed for moral transgressions",
        "hindi": "धार्मिक प्रायश्चित दंड / प्रथागत जुर्माना",
        "pos": "noun",
        "gender": "ka",
        "category": "rituals",
        "dialect_variants": {"sohra": "kuna", "pnar": "kuna", "war": "kuna", "bhoi": "kuna"}
    },
    {
        "khasi": "pynsuk-mynsiem",
        "english": "propitiatory ritual to pacify departed ancestral souls and bring spiritual calm",
        "hindi": "पितरों की आत्मा की शांति का अनुष्ठान",
        "pos": "noun",
        "gender": "ka",
        "category": "rituals",
        "dialect_variants": {"sohra": "pynsuk-mynsiem", "pnar": "pynsuk-mynsiem", "war": "pynsuk-mynsiem", "bhoi": "pynsuk-mynsiem"}
    },
    {
        "khasi": "kñia-khlam",
        "english": "ritual sacrifice to banish pestilence, plague, and catastrophic illness from the land",
        "hindi": "महामारी निवारण अनुष्ठान",
        "pos": "noun",
        "gender": "ka",
        "category": "rituals",
        "dialect_variants": {"sohra": "kñia-khlam", "pnar": "kñia-khlam", "war": "kñia-khlam", "bhoi": "kñia-khlam"}
    },

    # --- DEITIES & SPIRITUAL BEINGS ---
    {
        "khasi": "nongbuh-nongthaw",
        "english": "God the Supreme Architect, Ordainer and Creator of heaven, earth, and humankind",
        "hindi": "परमेश्वर / सृष्टि के रचयिता और विधाता",
        "pos": "noun",
        "gender": "u",
        "category": "deities",
        "dialect_variants": {"sohra": "nongbuh-nongthaw", "pnar": "nongbuh-nongthaw", "war": "nongbuh-nongthaw", "bhoi": "nongbuh-nongthaw"}
    },
    {
        "khasi": "meiramew",
        "english": "Mother Earth; the sacred divine feminine essence that nourishes all living beings",
        "hindi": "धरती माता / प्रकृति देवी",
        "pos": "noun",
        "gender": "ka",
        "category": "deities",
        "dialect_variants": {"sohra": "meiramew", "pnar": "beiramew", "war": "meiramew", "bhoi": "meiramew"}
    },
    {
        "khasi": "lei-shyllong",
        "english": "the sovereign patron mountain deity of Shillong Peak and the territorial realms of Mylliem and Khyrim",
        "hindi": "शिलांग शिखर के अधिष्ठाता देवता",
        "pos": "noun",
        "gender": "u",
        "category": "deities",
        "dialect_variants": {"sohra": "lei-shyllong", "pnar": "blai-shyllong", "war": "lei-shyllong", "bhoi": "lei-shyllong"}
    },
    {
        "khasi": "lei-longspah",
        "english": "the deity of righteous prosperity, abundance, and material wealth",
        "hindi": "धन, समृद्धि और ऐश्वर्य के देवता",
        "pos": "noun",
        "gender": "u",
        "category": "deities",
        "dialect_variants": {"sohra": "lei-longspah", "pnar": "blai-longspah", "war": "lei-longspah", "bhoi": "lei-longspah"}
    },
    {
        "khasi": "lei-hima",
        "english": "the guardian protector deity of the customary Khasi state and sovereign realm",
        "hindi": "राज्य और प्रजा के रक्षक देवता",
        "pos": "noun",
        "gender": "u",
        "category": "deities",
        "dialect_variants": {"sohra": "lei-hima", "pnar": "blai-hima", "war": "lei-hima", "bhoi": "lei-hima"}
    },
    {
        "khasi": "suidnia",
        "english": "the primal maternal uncle and ancestor of the matrilineal clan presiding as intercessor before God",
        "hindi": "कुल के आदि मामा / पितृ-मध्यस्थ देव",
        "pos": "noun",
        "gender": "u",
        "category": "deities",
        "dialect_variants": {"sohra": "suidnia", "pnar": "suidnia", "war": "suidnia", "bhoi": "suidnia"}
    },
    {
        "khasi": "ka-iawbei",
        "english": "the revered primal ancestral mother and foundress of the matrilineal clan",
        "hindi": "मातृवंश की आदि माता / मूल मातृका",
        "pos": "noun",
        "gender": "ka",
        "category": "deities",
        "dialect_variants": {"sohra": "ka-iawbei", "pnar": "ka-bei-tynrai", "war": "ka-me-tynrai", "bhoi": "ka-iawbei"}
    },
    {
        "khasi": "u-thawlang",
        "english": "the primal paternal progenitor of the clan, commemorated alongside the maternal ancestors",
        "hindi": "मातृवंश के आदि जनक / मूल पिता",
        "pos": "noun",
        "gender": "u",
        "category": "deities",
        "dialect_variants": {"sohra": "u-thawlang", "pnar": "u-palang", "war": "u-polang", "bhoi": "u-thawlang"}
    },
    {
        "khasi": "ryngkew-basa",
        "english": "the territorial guardian spirits of local soil, village boundaries, and sacred groves",
        "hindi": "ग्राम-भूमि और पवित्र वनों के रक्षक क्षेत्रपाल",
        "pos": "noun",
        "gender": "u",
        "category": "deities",
        "dialect_variants": {"sohra": "ryngkew-basa", "pnar": "ryngkaw-basa", "war": "ryngkew-basa", "bhoi": "ryngkew-basa"}
    },
    {
        "khasi": "leisymper",
        "english": "the mighty mountain guardian spirit residing upon Symper Rock in Maharam",
        "hindi": "सिमपर पर्वत के शक्तिशाली रक्षक देवता",
        "pos": "noun",
        "gender": "u",
        "category": "deities",
        "dialect_variants": {"sohra": "leisymper", "pnar": "blaisymper", "war": "leisymper", "bhoi": "leisymper"}
    },
    {
        "khasi": "ka-kupli",
        "english": "the formidable river goddess of the Kopili River revered across Jaintia and Khasi realms",
        "hindi": "कोपिली नदी की अधिष्ठात्री देवी",
        "pos": "noun",
        "gender": "ka",
        "category": "deities",
        "dialect_variants": {"sohra": "ka-kupli", "pnar": "ka-kupli", "war": "ka-kupli", "bhoi": "ka-kupli"}
    },
    {
        "khasi": "blai-synteng",
        "english": "the divine supreme protector and ancestral sovereign of the Jaintia (Pnar) people",
        "hindi": "जयंतिया (पनार) समुदाय के संरक्षक इष्टदेव",
        "pos": "noun",
        "gender": "u",
        "category": "deities",
        "dialect_variants": {"sohra": "blei-synteng", "pnar": "blai-synteng", "war": "blai-synteng", "bhoi": "blei-synteng"}
    },

    # --- SACRED SITES, MONOLITHS & SHRINES ---
    {
        "khasi": "law-kyntang",
        "english": "sacred forest grove protected by inviolable customary taboo where nature is preserved undisturbed",
        "hindi": "पवित्र देववन / धार्मिक निषेध द्वारा संरक्षित प्राचीन वन",
        "pos": "noun",
        "gender": "ka",
        "category": "sacred_sites",
        "dialect_variants": {"sohra": "law-kyntang", "pnar": "khlaw-kyntang", "war": "khlo-kyntang", "bhoi": "law-kyntang"}
    },
    {
        "khasi": "law-adong",
        "english": "customary reserved village catchment forest where logging and resource extraction are banned",
        "hindi": "ग्राम-पंचायत द्वारा संरक्षित जल-स्रोत वन",
        "pos": "noun",
        "gender": "ka",
        "category": "sacred_sites",
        "dialect_variants": {"sohra": "law-adong", "pnar": "khlaw-adong", "war": "khlo-adong", "bhoi": "law-adong"}
    },
    {
        "khasi": "mawbynna",
        "english": "monumental megalithic menhir or standing stone erected in remembrance of ancestors",
        "hindi": "पूर्वजों की स्मृति में स्थापित महापाषाण (मेनहिर)",
        "pos": "noun",
        "gender": "u",
        "category": "sacred_sites",
        "dialect_variants": {"sohra": "mawbynna", "pnar": "moobynna", "war": "mawbynna", "bhoi": "mawbynna"}
    },
    {
        "khasi": "maw-shynrang",
        "english": "upright vertical male standing stone in a megalithic alignment",
        "hindi": "ऊर्ध्वाधर पुरुष पाषाण-स्तंभ",
        "pos": "noun",
        "gender": "u",
        "category": "sacred_sites",
        "dialect_variants": {"sohra": "maw-shynrang", "pnar": "moo-chynrang", "war": "maw-shynrang", "bhoi": "maw-shynrang"}
    },
    {
        "khasi": "maw-kynthei",
        "english": "horizontal flat female dolmen stone resting on support pedestals",
        "hindi": "सपाट स्त्री महापाषाण (डोलमेन)",
        "pos": "noun",
        "gender": "ka",
        "category": "sacred_sites",
        "dialect_variants": {"sohra": "maw-kynthei", "pnar": "moo-kynthai", "war": "maw-kynthei", "bhoi": "maw-kynthei"}
    },
    {
        "khasi": "mawbah",
        "english": "the grand central stone ossuary or ancestral sepulchre containing the bones of the whole clan",
        "hindi": "कुल की मुख्य महापाषाण अस्थि-मंजूषा",
        "pos": "noun",
        "gender": "u",
        "category": "sacred_sites",
        "dialect_variants": {"sohra": "mawbah", "pnar": "moobah", "war": "mawbah", "bhoi": "mawbah"}
    },
    {
        "khasi": "duwan",
        "english": "consecrated stone sacrificial altar where prayers and libations are offered",
        "hindi": "यज्ञ-वेदी / अनुष्ठानिक पाषाण वेदी",
        "pos": "noun",
        "gender": "ka",
        "category": "sacred_sites",
        "dialect_variants": {"sohra": "duwan", "pnar": "duwan", "war": "duwan", "bhoi": "duwan"}
    },
    {
        "khasi": "kpep",
        "english": "consecrated clan cremation ground or ancestral funerary pyre terrace",
        "hindi": "कुल का पारंपरिक श्मशान घाट",
        "pos": "noun",
        "gender": "ka",
        "category": "sacred_sites",
        "dialect_variants": {"sohra": "kpep", "pnar": "kpep", "war": "kpep", "bhoi": "kpep"}
    },
    {
        "khasi": "kor-shongthait",
        "english": "monumental stone resting bench along ancient mountain walking paths for burden-bearers",
        "hindi": "पहाड़ी मार्ग पर भारवाहकों के विश्राम हेतु निर्मित पाषाण-आसन",
        "pos": "noun",
        "gender": "ka",
        "category": "sacred_sites",
        "dialect_variants": {"sohra": "kor-shongthait", "pnar": "kor-shongthait", "war": "kor-songthait", "bhoi": "kor-shongthait"}
    }
]

def main():
    print("Loading words.json...")
    with open(WORDS_FILE, "r", encoding="utf-8") as f:
        words = json.load(f)

    existing_khasi = {w.get("khasi", "").lower().strip(): i for i, w in enumerate(words)}
    print(f"Current total words: {len(words)}")

    added = 0
    updated = 0
    for item in NEW_CULTURAL_WORDS:
        kh = item["khasi"].lower().strip()
        if kh in existing_khasi:
            idx = existing_khasi[kh]
            words[idx].update(item)
            updated += 1
        else:
            words.append(item)
            existing_khasi[kh] = len(words) - 1
            added += 1

    print(f"Added new cultural words: {added}")
    print(f"Updated existing words with deep cultural metadata: {updated}")
    print(f"New total word count: {len(words)}")

    with open(WORDS_FILE, "w", encoding="utf-8") as f:
        json.dump(words, f, ensure_ascii=False, indent=2)

    print("words.json successfully saved!")

if __name__ == "__main__":
    main()
