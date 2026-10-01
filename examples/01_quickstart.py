# -*- coding: utf-8 -*-
"""
Khasi (Ka Ktien Khasi) Quickstart Demo:
Demonstrating fundamental features of the Khasi language library.
"""

import sys
from pathlib import Path

# Add project root to sys.path for standalone script execution
sys.path.insert(0, str(Path(__file__).parent.parent))

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

import khasi

def main():
    print("=" * 65)
    print("   Khasi Language Library (Meghalaya, Northeast India)   ")
    print(f"   Version {khasi.__version__} | Author: {khasi.__author__}")
    print("=" * 65)

    # 1. Multi-Dialect Translation
    print("\n1. Universal Translation:")
    t1 = khasi.translate("How are you?")
    print(f"   'How are you?' -> {t1.text} (dialect: {t1.dialect})")

    t2 = khasi.translate("I love you", dialect="pnar")
    print(f"   'I love you' (Pnar dialect) -> {t2.text}")

    t3 = khasi.translate("आप कैसे हैं?")
    print(f"   'आप कैसे हैं?' -> {t3.text}")

    # 2. Dictionary & Lexical Lookup
    print("\n2. Trilingual Dictionary (Khasi <-> English <-> Hindi):")
    word = "khublei"
    entry = khasi.lookup(word)
    if entry:
        print(f"   Lookup '{word}':")
        print(f"     English: {entry.get('english')}")
        print(f"     Hindi  : {entry.get('hindi')}")
        print(f"     POS    : {entry.get('pos')}")

    # 3. Numbers & Ordinals
    print("\n3. Number Conversion:")
    for num in [1, 7, 15, 42, 100, 2500]:
        print(f"   {num:5d} -> {khasi.num_to_words(num)} (ordinal: {khasi.ordinal(num)})")
    print(f"   'sawphew ar' -> {khasi.words_to_num('sawphew ar')}")

    # 4. Grammar & Verb Conjugation
    print("\n4. Grammar & Verb Conjugation:")
    print("   Verb: 'wan' (to come)")
    print(f"     Past (u / he)       : {khasi.conjugate('wan', tense='past', pronoun='u')}")
    print(f"     Future (u / he)     : {khasi.conjugate('wan', tense='future', pronoun='u')}")
    print(f"     Progressive (nga / I): {khasi.conjugate('wan', tense='present', pronoun='nga', aspect='progressive')}")
    print(f"     Causative ('ïap' -> die) -> {khasi.causative('ïap')} (kill)")
    print(f"     Nominalize ('stad' -> wise) -> {khasi.nominalize('stad')} (wisdom)")
    print(f"     Agent noun ('hikai' -> teach) -> {khasi.agent_noun('hikai')} (teacher)")

    # 5. Morphological Universe (300,000+ forms)
    print("\n5. Morphological Decomposition:")
    analysis = khasi.analyze("jingstad")
    if analysis:
        print(f"   Analyzed 'jingstad' -> lemma='{analysis.lemma}', pos='{analysis.pos}', prefix='{analysis.prefix_type}'")
    print(f"   Total Morphological Combinations: {khasi.total_word_forms():,}+")

    # 6. Culture, Calendar & Traditional Market Days
    print("\n6. Himalayan / Northeast Heritage & Calendar:")
    season = khasi.get_current_season()
    month = khasi.get_current_khasi_month()
    market = khasi.get_market_day(1)
    print(f"   Current Season (Aïom) : {season['name_khasi']} ({season['english_season']})")
    print(f"   Current Month (Bnai)  : {month['name']} ({month['english']}) - {month['meaning']}")
    print(f"   Traditional Market Day: {market['name']} ({market['location']})")

    # 7. Matrilineal Kinship Philosophy
    print("\n7. Matrilineal Kinship & Philosophy:")
    kin = khasi.describe_matrilineal_system()
    print(f"   Inheritance Rule: {kin['inheritance_rule']}")
    p = khasi.proverbs.random()
    if p:
        print(f"   Proverb: \"{p['khasi']}\"")
        print(f"     Literal: {p['literal']}")
        print(f"     Meaning: {p['meaning']}")

    # 8. Voice & Speech Synthesis
    print("\n8. Voice Synthesis SSML:")
    ssml = khasi.KhasiVoiceSynthesizer.get_speech_ssml("Khublei shibun!")
    print(f"   Generated SSML:\n{ssml}")

    print("\n" + "=" * 65)

if __name__ == "__main__":
    main()
