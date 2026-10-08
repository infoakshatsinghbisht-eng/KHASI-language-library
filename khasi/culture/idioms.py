# -*- coding: utf-8 -*-
"""
Khasi Idioms (Ki Ktien Kynnoh) & Metaphorical Expressions (Ki Pharshi).
Coupled rhyming words, idiomatic pairs, and traditional figures of speech.
"""

from typing import Dict, List, Any, Optional

IDIOMS: List[Dict[str, Any]] = [
    {
        "idiom": "Horkit-hordang",
        "type": "Ktien Kynnoh (Coupled Idiom)",
        "literal": "Through tight constraints and trials",
        "meaning": "Resolutely / through thick and thin / persevering against all odds and difficulties.",
        "hindi": "हर परिस्थिति में / दृढ़तापूर्वक / चाहे जो हो जाए।"
    },
    {
        "idiom": "Bamngem-bamsap",
        "type": "Ktien Kynnoh",
        "literal": "Swallowing illicitly and concealing corruption",
        "meaning": "Taking bribes / corrupt graft / illicitly consuming public funds.",
        "hindi": "रिश्वतखोरी / भ्रष्टाचार / अवैध धन हड़पना।"
    },
    {
        "idiom": "Batai-satai",
        "type": "Ktien Kynnoh",
        "literal": "Explaining and clarifying in minute detail",
        "meaning": "Elaborating thoroughly / providing an exhaustive explanation.",
        "hindi": "विस्तारपूर्वक समझाना / एक-एक बात खोलकर बताना।"
    },
    {
        "idiom": "Duk-suk",
        "type": "Ktien Kynnoh",
        "literal": "Poverty and prosperity / sorrow and joy",
        "meaning": "The ups and downs of human existence / sharing both joys and hardships together.",
        "hindi": "सुख-दुःख / जीवन के उतार-चढ़ाव।"
    },
    {
        "idiom": "Ktien-siaw ktien-sur",
        "type": "Ktien Kynnoh",
        "literal": "Whispered words and melodic murmurs",
        "meaning": "Gossip, rumors, and unverified grapevine talk.",
        "hindi": "कानाफूसी / अफ़वाहें / चर्चा।"
    },
    {
        "idiom": "Bam-khana",
        "type": "Ktien Kynnoh",
        "literal": "Eating food in company",
        "meaning": "A community picnic / joyous outdoor feast with friends and relatives.",
        "hindi": "सामूहिक भोज / पिकनिक / दावत।"
    },
    {
        "idiom": "Khla-thlen",
        "type": "Ktien Kynnoh",
        "literal": "Tiger and Thlen serpent",
        "meaning": "Monsters of folklore / a cruel and villainous predator.",
        "hindi": "राक्षसी स्वभाव का प्राणी / खलनायक।"
    },
    {
        "idiom": "Kamai-spah",
        "type": "Ktien Kynnoh",
        "literal": "Earning wealth and assets",
        "meaning": "Acquiring prosperity through diligent enterprise.",
        "hindi": "धन अर्जित करना / संपत्ति कमाना।"
    },
    {
        "idiom": "Kren-thuh kren-dait",
        "type": "Ktien Kynnoh",
        "literal": "Speaking bitingly and spitefully",
        "meaning": "Sarcastic, abrasive, or spiteful speech aimed at hurting someone.",
        "hindi": "चुभती हुई बातें कहना / ताने मारना।"
    },
    {
        "idiom": "Leit-jngoh leit-i",
        "type": "Ktien Kynnoh",
        "literal": "Going to visit and look upon",
        "meaning": "Visiting loved ones to check on their health and wellbeing.",
        "hindi": "हाल-चाल लेने जाना / मिलने जाना।"
    },
    {
        "idiom": "Maw-bynna maw-nam",
        "type": "Ktien Kynnoh",
        "literal": "Stones of renown and name",
        "meaning": "Monumental memorial monoliths erected to preserve ancestral memory.",
        "hindi": "स्मृति प्रस्तर / पूर्वजों के कीर्ति स्तंभ।"
    },
    {
        "idiom": "Niam-rukom",
        "type": "Ktien Kynnoh",
        "literal": "Religion and customary procedure",
        "meaning": "Sacred rites, traditional ceremonies, and religious protocols.",
        "hindi": "पूजा-पद्धति / रीति-रिवाज / धार्मिक अनुष्ठान।"
    },
    {
        "idiom": "Pule-thoh",
        "type": "Ktien Kynnoh",
        "literal": "Reading and writing",
        "meaning": "Literacy, scholarly education, and formal learning.",
        "hindi": "लिखना-पढ़ना / साक्षरता / विद्या।"
    },
    {
        "idiom": "Ri-kynti",
        "type": "Customary Law Idiom",
        "literal": "Held land by one's own hand",
        "meaning": "Private ancestral clan land, distinct from communal village land (Ri Raid).",
        "hindi": "पैतृक निजी भूमि / कुल की निजी ज़मीन।"
    },
    {
        "idiom": "Trei-shitom",
        "type": "Ktien Kynnoh",
        "literal": "Working with strenuous exertion",
        "meaning": "Diligent hard labor / sweating with honest toil.",
        "hindi": "कड़ा परिश्रम / जी-तोड़ मेहनत।"
    },
    {
        "idiom": "Ummiew-umpohliew",
        "type": "Ktien Kynnoh",
        "literal": "Water of weeping and water of deep springs",
        "meaning": "Pristine mountain spring water bubbling from the deep earth.",
        "hindi": "प्राकृतिक झरने का निर्मल जल।"
    },
    {
        "idiom": "Ynda-shai ynda-step",
        "type": "Ktien Kynnoh",
        "literal": "When dawn breaks and morning comes",
        "meaning": "At the crack of dawn / early the next morning.",
        "hindi": "भोर होते ही / अगली सुबह सवेरे।"
    },
    {
        "idiom": "Kiang-pyrta",
        "type": "Ktien Kynnoh",
        "literal": "Shouting and calling aloud",
        "meaning": "Rallying cry / shouting aloud to gather the community together.",
        "hindi": "हाक लगाना / पुकारना / एकजुट होने की आवाज़।"
    },
    {
        "idiom": "Tip-akor tip-burom",
        "type": "Moral Philosophy Idiom",
        "literal": "Knowing etiquette and knowing honor",
        "meaning": "A truly cultured, dignified, polite, and morally upright personality.",
        "hindi": "संस्कारी और मर्यादावान / शिष्टाचार से परिपूर्ण व्यक्ति।"
    },
    {
        "idiom": "Kha-man kha-san",
        "type": "Ktien Kynnoh",
        "literal": "Paternal relations junior and senior",
        "meaning": "The entire paternal clan network and father's extended kin.",
        "hindi": "पिता पक्ष के समस्त नाते-रिश्तेदार।"
    },
    {
        "idiom": "Kur-kha",
        "type": "Kinship Pair",
        "literal": "Maternal kin and paternal kin",
        "meaning": "The complete social universe of human relations in Khasi society.",
        "hindi": "मातृपक्ष और पितृपक्ष के समस्त स्वजन।"
    },
    {
        "idiom": "Shong-kurim",
        "type": "Life-cycle Idiom",
        "literal": "Taking up residence in marriage",
        "meaning": "To marry / establish a marital household.",
        "hindi": "विवाह करना / गृहस्थी बसाना।"
    },
    {
        "idiom": "Ieit-thoin thoin",
        "type": "Expressive Reduplication",
        "literal": "Loving deeply to the core",
        "meaning": "Cherishing someone with passionate, pure, and profound love.",
        "hindi": "अथाह और निष्कपट प्रेम करना।"
    },
    {
        "idiom": "Kmen-kmen",
        "type": "Expressive Reduplication",
        "literal": "Rejoicing repeatedly",
        "meaning": "Overflowing with radiant joy and celebration.",
        "hindi": "अत्यंत हर्षित और प्रफुल्लित होना।"
    }
]

def list_idioms() -> List[Dict[str, Any]]:
    """Return all catalogued Khasi idioms (Ki Ktien Kynnoh) and figures of speech."""
    return IDIOMS

def get_idiom(query: str) -> Optional[Dict[str, Any]]:
    """Lookup idiom by Khasi expression or meaning."""
    q = query.lower().strip()
    for item in IDIOMS:
        if q in item["idiom"].lower() or q in item["meaning"].lower() or q in item.get("hindi", "").lower():
            return item
    return None

def by_category(cat: str) -> List[Dict[str, Any]]:
    """Filter idioms by category or type."""
    c = cat.lower().strip()
    return [i for i in IDIOMS if c in i.get("type", "").lower()]
