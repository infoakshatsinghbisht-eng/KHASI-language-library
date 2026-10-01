# -*- coding: utf-8 -*-
"""
Khasi Adverbs, Expressives, Ideophones (Ki Kyntien Pynbynta), and Reduplication.
Khasi possesses an extraordinarily rich system of descriptive adverbs and ideophones
that describe subtle sensory perceptions, speed, manner, space, and time.
"""

from typing import Dict, List, Any, Optional

KHASI_ADVERBS: Dict[str, Dict[str, str]] = {
    # Manner
    "suki": {"type": "manner", "english": "slowly", "hindi": "धीरे-धीरे"},
    "kloi": {"type": "manner", "english": "quickly / promptly", "hindi": "जल्दी से"},
    "stet": {"type": "manner", "english": "fast / swiftly", "hindi": "तेज़ी से"},
    "bha": {"type": "manner", "english": "well / properly", "hindi": "अच्छी तरह"},
    "sniew": {"type": "manner", "english": "badly / poorly", "hindi": "बुरी तरह"},
    "jai-jai": {"type": "manner", "english": "peacefully / calmly", "hindi": "शांतिपूर्वक"},

    # Expressives & Ideophones (Sensory & Emotional nuancing)
    "jar-jar": {"type": "ideophone", "english": "silently / quietly", "hindi": "चुपचाप / शांत"},
    "kyndit": {"type": "ideophone", "english": "suddenly / abruptly / with shock", "hindi": "अचानक / चौंककर"},
    "shen-shen": {"type": "ideophone", "english": "speedily / punctually", "hindi": "तुरंत / समय पर"},
    "phreit": {"type": "ideophone", "english": "alertly / briskly / sprightly", "hindi": "फुर्ती से"},
    "kynjah": {"type": "ideophone", "english": "lonely / desolate / in silence", "hindi": "सुनसान / एकांत में"},
    "lyngngoh": {"type": "ideophone", "english": "wonderingly / perplexed", "hindi": "आश्चर्यचकित होकर"},

    # Time
    "mynta": {"type": "time", "english": "now / today", "hindi": "अब / आज"},
    "mynstep": {"type": "time", "english": "in the morning", "hindi": "सुबह / प्रातःकाल"},
    "mynmiet": {"type": "time", "english": "at night", "hindi": "रात में"},
    "mynshai": {"type": "time", "english": "tomorrow", "hindi": "कल (आने वाला)"},
    "mynnin": {"type": "time", "english": "yesterday", "hindi": "कल (बीता हुआ)"},
    "hynne": {"type": "time", "english": "earlier today / just now", "hindi": "अभी-अभी / कुछ देर पहले"},
    "barabor": {"type": "time", "english": "always / regularly", "hindi": "हमेशा / सदैव"},
    "teng-teng": {"type": "time", "english": "sometimes / now and then", "hindi": "कभी-कभी"},
    "biang": {"type": "time", "english": "again / once more", "hindi": "फिर से / पुनः"},
    "pat": {"type": "time", "english": "yet / still / again", "hindi": "अभी भी / फिर"},
    "shen": {"type": "time", "english": "soon", "hindi": "जल्द ही"},

    # Place
    "hangne": {"type": "place", "english": "here (in this place)", "hindi": "यहाँ"},
    "hangto": {"type": "place", "english": "there (visible / near)", "hindi": "वहाँ"},
    "hangtai": {"type": "place", "english": "over there (distant)", "hindi": "वहाँ दूर"},
    "shane": {"type": "place", "english": "hither / towards here", "hindi": "इधर"},
    "shata": {"type": "place", "english": "thither / towards there", "hindi": "उधर"},
    "shajngai": {"type": "place", "english": "far away", "hindi": "दूर"},
    "shajan": {"type": "place", "english": "nearby / close by", "hindi": "पास"},

    # Degree & Intensity
    "shibun": {"type": "degree", "english": "much / a lot / greatly", "hindi": "बहुत / अधिक"},
    "eh": {"type": "degree", "english": "very / exceedingly / too", "hindi": "बहुत / अत्यंत"},
    "thik": {"type": "degree", "english": "exactly / precisely", "hindi": "बिल्कुल / ठीक"},
    "tang": {"type": "degree", "english": "only / merely / solely", "hindi": "केवल / सिर्फ"},
    "khadduh": {"type": "degree", "english": "finally / at last", "hindi": "अंततः / आख़िरकार"},
}

def reduplicate_adverb(adverb: str) -> str:
    """
    Form emphatic Khasi reduplicated adverb.
    e.g., 'suki' -> 'suki-suki' (very gently/slowly)
          'kloi' -> 'kloi-kloi' (in great haste)
    """
    clean = adverb.strip().lower()
    if "-" in clean:
        return clean
    return f"{clean}-{clean}"

def get_adverbs_by_type(adv_type: str) -> List[Dict[str, str]]:
    """Retrieve all adverbs belonging to a specific linguistic type."""
    t = adv_type.strip().lower()
    res = []
    for word, data in KHASI_ADVERBS.items():
        if data["type"] == t:
            res.append({"khasi": word, **data})
    return res

def classify_adverb(word: str) -> Optional[Dict[str, str]]:
    """Look up grammatical classification and semantics of an adverb."""
    clean = word.strip().lower()
    if clean in KHASI_ADVERBS:
        return KHASI_ADVERBS[clean]
    # Check if reduplicated form
    if "-" in clean:
        base = clean.split("-")[0]
        if base in KHASI_ADVERBS:
            info = KHASI_ADVERBS[base].copy()
            info["note"] = "Reduplicated intensive form"
            return info
    return None
