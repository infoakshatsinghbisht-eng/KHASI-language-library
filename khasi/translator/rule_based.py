# -*- coding: utf-8 -*-
"""Comprehensive Rule-Based Khasi Translation Engine with Multi-Dialect Support."""

import re
from typing import Dict, List, Any, Optional, Tuple

CONVERSATIONAL_HINGLISH_KHASI_MAP: List[Tuple[str, str]] = [
    # Greetings & Well-being
    (r"\b(?:kya|kaise)\s*haal\s*(?:hai)?\b|\bkaise\s*ho\??\b|\baap\s*kaise\s*hain\??\b", "Kumno phi long?"),
    (r"\bmain\s*(?:theek|achha|badiya)\s*(?:hoon|hu)\b", "Nga khlain bha, khublei."),
    (r"\b(?:aapka|tera|tumhara)\s*naam\s*kya\s*hai\??\b", "Kumno ka kyrteng jong phi?"),
    (r"\bmera\s*naam\s+([a-zA-Z]+)\s*(?:hai)?\b", r"Ka kyrteng jong nga ka dei \1."),
    (r"\b(?:dhanyawad|shukriya|thanks|thank\s*you)\b", "Khublei shibun!"),
    (r"\b(?:namaste|pranam|hello|hi)\b", "Khublei!"),
    
    # Love & Emotion
    (r"\bmujhe\s*tumse\s*pyar\s*hai\b|\bmain\s*tumhe\s*pyar\s*karta\s*hoon\b", "Nga ieit ïa phi."),
    (r"\btum\s*bahut\s*(?:achhe|sundar|khoobsoorat)\s*ho\b", "Phi bhabriew shibun."),
    
    # Travel, Direction & Questions
    (r"\b(?:kahan|kidhar)\s*ja\s*rahe\s*ho\??\b|\baap\s*kahan\s*ja\s*rahe\s*hain\??\b", "Shano phi leit?"),
    (r"\bmain\s*ghar\s*ja\s*raha\s*hoon\b", "Nga leit sha ïing."),
    (r"\bmain\s*shillong\s*ja\s*raha\s*hoon\b", "Nga leit sha Shillong."),
    (r"\b(?:iska|ye)\s*kitne\s*ka\s*hai\??\b|\bkitna\s*paisa\s*lagega\??\b|\bkitna\s*daam\s*hai\??\b", "Katno ka dor?"),
    (r"\brasta\s*kahan\s*hai\??\b", "Hangno ka lynti?"),
    (r"\bmadad\s*karo\b|\bmeri\s*madad\s*karo\b", "Sngewbha ïarap ïa nga!"),
    (r"\byahan\s*aao\b|\bkripya\s*yahan\s*aao\b", "Sngewbha wan shane."),
    
    # Food & Hospitality
    (r"\b(?:kya\s*)?khana\s*kha\s*liya\??\b", "Phi la bam ja?"),
    (r"\bhaan\s*maine\s*kha\s*liya\b|\bmain\s*khana\s*kha\s*chuka\s*hoon\b", "Hooid, nga la bam ja."),
    (r"\bchai\s*peeyenge\??\b|\bchai\s*pee\s*lo\b", "Dih sha seh!"),
    (r"\bpaani\s*chahiye\b", "Nga kwah um."),

    # Parting
    (r"\balvida\b|\bbai\b|\bphir\s*milenge\b", "Ngan sa wan biang! Suk ka leit ka wan.")
]

CONVERSATIONAL_EN_KHASI_MAP: List[Tuple[str, str]] = [
    # Greetings
    (r"\bhow\s+are\s+you\??\b", "Kumno phi long?"),
    (r"\bi\s+am\s+(?:fine|good|well)\b", "Nga khlain bha, khublei."),
    (r"\bwhat\s+is\s+your\s+name\??\b", "Kumno ka kyrteng jong phi?"),
    (r"\bmy\s+name\s+is\s+([a-zA-Z]+)\b", r"Ka kyrteng jong nga ka dei \1."),
    (r"\bthank\s+you(?:\s+very\s+much)?\b", "Khublei shibun!"),
    (r"\bhello\b|\bgreetings\b", "Khublei!"),
    (r"\bwelcome\b", "Pdiang sngewbha!"),
    (r"\bplease\b", "Sngewbha."),
    (r"\bplease\s+come\s+here\b", "Sngewbha wan shane."),
    
    # Love & Relationship
    (r"\bi\s+love\s+you\b", "Nga ieit ïa phi."),
    (r"\byou\s+are\s+beautiful\b", "Phi bhabriew shibun."),
    
    # Travel & Direction
    (r"\bwhere\s+are\s+you\s+going\??\b", "Shano phi leit?"),
    (r"\bi\s+am\s+going\s+home\b", "Nga leit sha ïing."),
    (r"\bi\s+am\s+going\s+to\s+shillong\b", "Nga leit sha Shillong."),
    (r"\bhow\s+much(?:\s+is\s+it|\s+does\s+it\s+cost)?\??\b", "Katno ka dor?"),
    (r"\bwhere\s+is\s+the\s+way\??\b|\bwhere\s+is\s+the\s+road\??\b", "Hangno ka lynti?"),
    (r"\bhelp\s+me\b|\bplease\s+help\s+me\b", "Sngewbha ïarap ïa nga!"),
    
    # Food & Daily Life
    (r"\bhave\s+you\s+eaten(?:\s+food|\s+rice)?\??\b", "Phi la bam ja?"),
    (r"\bi\s+have\s+eaten\b", "Nga la bam ja."),
    (r"\bhave\s+some\s+tea\b", "Dih sha seh!"),
    (r"\bi\s+want\s+water\b", "Nga kwah um."),
    
    # Parting
    (r"\bgoodbye\b|\bsee\s+you\s+again\b", "Ngan sa wan biang! Suk ka leit ka wan."),
    (r"\bgood\s+morning\b", "Khublei step!"),
    (r"\bgood\s+night\b", "Khublei miet!")
]

CONVERSATIONAL_HI_KHASI_MAP: List[Tuple[str, str]] = [
    (r"आप\s+कैसे\s+हैं\??|तुम\s+कैसे\s+हो\??|क्या\s+हाल\s+है\??", "Kumno phi long?"),
    (r"मैं\s+ठीक\s+हूँ|सब\s+ठीक\s+है", "Nga khlain bha, khublei."),
    (r"आपका\s+नाम\s+क्या\s+है\??|तेरा\s+नाम\s+क्या\s+है\??", "Kumno ka kyrteng jong phi?"),
    (r"धन्यवाद|बहुत\s+धन्यवाद|शुक्रिया", "Khublei shibun!"),
    (r"नमस्ते|प्रणाम", "Khublei!"),
    (r"कृपया\s+यहाँ\s+आइए|इधर\s+आओ", "Sngewbha wan shane."),
    (r"मुझे\s+तुमसे\s+प्यार\s+है|मैं\s+तुमसे\s+प्रेम\s+करता\s+हूँ", "Nga ieit ïa phi."),
    (r"आप\s+कहाँ\s+जा\s+रहे\s+हैं\??|कहाँ\s+जा\s+रहे\s+हो\??", "Shano phi leit?"),
    (r"मैं\s+घर\s+जा\s+रहा\s+हूँ", "Nga leit sha ïing."),
    (r"इसका\s+दाम\s+कितना\s+है\??|कितने\s+रुपये\??", "Katno ka dor?"),
    (r"मेरी\s+मदद\s+करो|कृपया\s+सहायता\s+करें", "Sngewbha ïarap ïa nga!"),
    (r"क्या\s+आपने\s+खाना\s+खाया\??", "Phi la bam ja?"),
    (r"शुभ\s+प्रभात", "Khublei step!"),
    (r"शुभ\s+रात्रि", "Khublei miet!"),
    (r"अलविदा|फिर\s+मिलेंगे", "Ngan sa wan biang! Suk ka leit ka wan.")
]

CONVERSATIONAL_KHASI_EN_MAP: List[Tuple[str, str]] = [
    (r"\bkhublei\s+shibun\b", "Thank you very much!"),
    (r"\bkhublei\s+step\b", "Good morning!"),
    (r"\bkhublei\s+miet\b", "Good night!"),
    (r"\bkhublei\b", "Hello / Greetings / Thank you"),
    (r"\bkumno\s+phi\s+long\??\b", "How are you?"),
    (r"\bnga\s+khlain\s+bha\b", "I am very well, thank you."),
    (r"\bkumno\s+ka\s+kyrteng\s+jong\s+phi\??\b", "What is your name?"),
    (r"\bka\s+kyrteng\s+jong\s+nga\s+ka\s+dei\s+([a-zA-Z]+)\b", r"My name is \1."),
    (r"\bnga\s+ieit\s+ïa\s+phi\b|\bnga\s+ieit\s+ia\s+phi\b", "I love you."),
    (r"\bshano\s+phi\s+leit\??\b", "Where are you going?"),
    (r"\bnga\s+leit\s+sha\s+ïing\b|\bnga\s+leit\s+sha\s+iing\b", "I am going home."),
    (r"\bnga\s+leit\s+sha\s+shillong\b", "I am going to Shillong."),
    (r"\bkatno\s+ka\s+dor\??\b", "How much does it cost?"),
    (r"\bhangno\s+ka\s+lynti\??\b", "Where is the way?"),
    (r"\bsngewbha\s+ïarap\s+ïa\s+nga\b", "Please help me!"),
    (r"\bsngewbha\s+wan\s+shane\b", "Please come here."),
    (r"\bphi\s+la\s+bam\s+ja\??\b", "Have you eaten your meal?"),
    (r"\bhooid,?\s*nga\s+la\s+bam\s+ja\b", "Yes, I have eaten."),
    (r"\bdih\s+sha\s+seh\b", "Do have some tea!"),
    (r"\bnga\s+kwah\s+um\b", "I want water."),
    (r"\bngan\s+sa\s+wan\s+biang\b", "I will come again."),
    (r"\bsuk\s+ka\s+leit\s+ka\s+wan\b", "Safe travels and peaceful journey!")
]

CONVERSATIONAL_KHASI_HI_MAP: List[Tuple[str, str]] = [
    (r"\bkhublei\s+shibun\b", "बहुत-बहुत धन्यवाद!"),
    (r"\bkhublei\s+step\b", "शुभ प्रभात!"),
    (r"\bkhublei\s+miet\b", "शुभ रात्रि!"),
    (r"\bkhublei\b", "नमस्ते / धन्यवाद"),
    (r"\bkumno\s+phi\s+long\??\b", "आप कैसे हैं?"),
    (r"\bnga\s+khlain\s+bha\b", "मैं बिल्कुल ठीक हूँ।"),
    (r"\bkumno\s+ka\s+kyrteng\s+jong\s+phi\??\b", "आपका नाम क्या है?"),
    (r"\bka\s+kyrteng\s+jong\s+nga\s+ka\s+dei\s+([a-zA-Z]+)\b", r"मेरा नाम \1 है।"),
    (r"\bnga\s+ieit\s+ïa\s+phi\b|\bnga\s+ieit\s+ia\s+phi\b", "मुझे तुमसे प्यार है।"),
    (r"\bshano\s+phi\s+leit\??\b", "आप कहाँ जा रहे हैं?"),
    (r"\bnga\s+leit\s+sha\s+ïing\b|\bnga\s+leit\s+sha\s+iing\b", "मैं घर जा रहा हूँ।"),
    (r"\bnga\s+leit\s+sha\s+shillong\b", "मैं शिलांग जा रहा हूँ।"),
    (r"\bkatno\s+ka\s+dor\??\b", "इसका कितना दाम है?"),
    (r"\bhangno\s+ka\s+lynti\??\b", "रास्ता कहाँ है?"),
    (r"\bsngewbha\s+ïarap\s+ïa\s+nga\b", "कृपया मेरी मदद कीजिए!"),
    (r"\bsngewbha\s+wan\s+shane\b", "कृपया यहाँ आइए।"),
    (r"\bphi\s+la\s+bam\s+ja\??\b", "क्या आपने खाना खा लिया?"),
    (r"\bdih\s+sha\s+seh\b", "चाय तो पी लीजिए!"),
    (r"\bnga\s+kwah\s+um\b", "मुझे पानी चाहिए।"),
    (r"\bngan\s+sa\s+wan\s+biang\b", "मैं फिर आऊँगा।"),
    (r"\bsuk\s+ka\s+leit\s+ka\s+wan\b", "आपकी यात्रा मंगलमय हो!")
]

def apply_dialect(text: str, dialect: str = "sohra") -> str:
    """Applies authentic Khasi dialectal phonetic and lexical variations."""
    clean = text.strip()
    if not clean or dialect == "sohra":
        return clean

    words = clean.split()
    res = []
    for w in words:
        punct = ""
        while w and w[-1] in ".,?!;:\"'":
            punct = w[-1] + punct
            w = w[:-1]

        low = w.lower()

        if dialect == "pnar":  # Jaintia Hills variant
            if low == "ïing": w = "ïung"
            elif low == "briew": w = "bru"
            elif low == "mei": w = "bei"
            elif low == "ieit": w = "maya"
            elif low == "blei": w = "blai"
            elif low == "khublei": w = "khublei"
            elif low == "shad": w = "chaat"
            elif low == "leit": w = "lai"
            elif low == "sngap": w = "sñiaw"
            elif low == "sngewbha": w = "sñiawbha"
            elif low == "bah": w = "waheh"
        elif dialect == "shillong":  # Urban colloquial
            if low == "kmie-tymmen": w = "mei-rad"
            elif low == "kpa-tymmen": w = "pa-rad"
        elif dialect == "war":  # Southern border variant
            if low == "mei": w = "me"
        elif dialect == "bhoi":  # Ri-Bhoi variant
            if low == "khlaw": w = "khlaw-heh"

        res.append(w + punct)
    return " ".join(res)
