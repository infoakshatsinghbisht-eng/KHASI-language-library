# -*- coding: utf-8 -*-
"""
Khasi Echo Words, Paired Compounds & Rhyming Couplets (Ki Ktien Kynhun / Kyntien Pynkhraw).
Echo words in Khasi combine two rhythmic elements to denote a holistic concept,
broadening literal meanings to encompass all related aspects of life and culture.
"""

from typing import Dict, List, Any, Optional

ECHO_WORDS: List[Dict[str, str]] = [
    {
        "compound": "ka ja - ka doh",
        "literal": "the rice - the meat",
        "meaning": "food and sustenance / daily nourishment / complete meal",
        "hindi": "खान-पान / आहार",
        "example": "U trei shitom na ka bynta ka ja ka doh."
    },
    {
        "compound": "ka kot - ka sla",
        "literal": "the book - the leaf/paper",
        "meaning": "education, literacy, studies, and documents",
        "hindi": "पढ़ाई-लिखाई / शिक्षा",
        "example": "Ki khynnah ki dei ban minot ha ka kot ka sla."
    },
    {
        "compound": "ki lum - ki wah",
        "literal": "the mountains - the rivers",
        "meaning": "the native homeland / geography / Mother Nature / ecology of Meghalaya",
        "hindi": "पहाड़ और नदियाँ / मातृभूमि",
        "example": "Nga sngewbha ban sah ha ki lum ki wah jong ka Ri Khasi."
    },
    {
        "compound": "ka sngi - ka miet",
        "literal": "the day - the night",
        "meaning": "unceasingly / continuously / around the clock",
        "hindi": "दिन-रात / निरंतर",
        "example": "Ka kmie ka duwai ka sngi ka miet na ka bynta ki khun."
    },
    {
        "compound": "ka leit - ka wan",
        "literal": "the going - the coming",
        "meaning": "travels / voyages / comings and goings",
        "hindi": "आना-जाना / यात्रा",
        "example": "Suk ka leit ka wan ha phi baroh!"
    },
    {
        "compound": "ka kren - ka khana",
        "literal": "the speaking - the telling",
        "meaning": "conversation / dialogue / discussion / friendly talk",
        "hindi": "बातचीत / संवाद",
        "example": "Ngim pat don por ban ïakren ïakhana."
    },
    {
        "compound": "ka suk - ka saiñ",
        "literal": "the peace - the order/governance",
        "meaning": "peace, social harmony, and communal tranquility",
        "hindi": "शांति और व्यवस्था / अमन-चैन",
        "example": "To ai ba ka suk ka saiñ kan shong ha ka Ri."
    },
    {
        "compound": "ka bam - ka dih",
        "literal": "the eating - the drinking",
        "meaning": "feasting / hospitality / meals and refreshments",
        "hindi": "खान-पान / दावत",
        "example": "La don ka bam ka dih kaba heh ha ka sngi shad."
    },
    {
        "compound": "ka khih - ka khan",
        "literal": "the working - the calculating/planning",
        "meaning": "livelihood / work and enterprise / earning a living",
        "hindi": "रोजी-रोटी / काम-काज",
        "example": "U briew u im da ka khih ka khan."
    },
    {
        "compound": "ka sneng - ka kraw",
        "literal": "the counsel - the greatness/guidance",
        "meaning": "traditional moral guidance and instruction from ancestors and elders",
        "hindi": "बुजुर्गों की सीख और मार्गदर्शन",
        "example": "To burom ïa ka sneng ka kraw ki tymmen."
    },
    {
        "compound": "ka hok - ka sot",
        "literal": "the righteousness - the absolute truth",
        "meaning": "uncompromising moral integrity, justice, and truth",
        "hindi": "सत्य और न्याय / पूर्ण ईमानदारी",
        "example": "U Khasi u bat skhem ïa ka hok ka sot."
    },
    {
        "compound": "u kur - u kha",
        "literal": "the maternal clan - the paternal clan",
        "meaning": "all clan relatives / whole community of kin",
        "hindi": "कुल और संबंधी / समस्त कुटुम्ब",
        "example": "La ïalum lang u kur u kha baroh."
    }
]

def list_echo_words() -> List[Dict[str, str]]:
    """Return all documented traditional Khasi paired echo compounds."""
    return ECHO_WORDS

def find_echo_word(query: str) -> Optional[Dict[str, str]]:
    """Find echo compound matching query."""
    q = query.lower().strip()
    for e in ECHO_WORDS:
        if q in e["compound"].lower() or q in e["meaning"].lower() or q in e["hindi"].lower():
            return e
    return None
