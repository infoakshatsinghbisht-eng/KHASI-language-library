# 🌿 Khasi (Ka Ktien Khasi) Language Library

[![PyPI Version](https://img.shields.io/pypi/v/khasi.svg)](https://pypi.org/project/khasi/)
[![Python Versions](https://img.shields.io/pypi/pyversions/khasi.svg)](https://pypi.org/project/khasi/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Repository](https://img.shields.io/badge/GitHub-KHASI--language--library-blue.svg)](https://github.com/infoakshatsinghbisht-eng/KHASI-language-library)
[![Website](https://img.shields.io/badge/Website-akshatsinghbisht.com-orange.svg)](https://akshatsinghbisht.com/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Akshat_Singh_Bisht-0077b5.svg)](https://www.linkedin.com/in/akshat-singh-bisht-digital-performance-marketing-specialist/)
[![ResearchGate](https://img.shields.io/badge/ResearchGate-Akshat_Bisht-00ccbb.svg)](https://www.researchgate.net/profile/Akshat-Bisht-8)
[![Amazon Author](https://img.shields.io/badge/Amazon-Author_Page-FF9900.svg)](https://www.amazon.com/stores/Akshat-Singh-Bisht/author/B0D5TYDT28)

A standard-library-style Python package, NLP toolkit, and computational linguistics engine for the **Khasi language (*Ka Ktien Khasi*)** — an Austroasiatic (Mon-Khmer) language spoken by over 1.6 million people in the pine-covered hills of **Meghalaya, Northeast India** and adjacent borderlands.

Khasi is globally renowned for its distinct grammatical features, rich prefix morphology, and the deep cultural heritage of the **world's largest surviving matrilineal society**.

---

## 🌟 Key Capabilities

1. **📚 300,000+ Morphological Word Forms (`khasi.lexicon.morphology`)**:
   - Dynamic inflectional and derivational engine generating extensive verbal TAM forms, nominalizations (`jing-`), causatives (`pyn-`), agentives (`nong-`), experientials (`sngew-`), and prepositional case declensions across noun gender articles (`u`, `ka`, `i`, `ki`).
2. **🔄 Multi-Dialect Universal Translation Engine (`khasi.translator`)**:
   - Rule-based, conversational, and lexical translation across **English $\leftrightarrow$ Khasi**, **Hindi $\leftrightarrow$ Khasi**, and **Hinglish $\leftrightarrow$ Khasi**.
   - Dialect adaptations for **Sohra** (Standard Literary), **Shillong** (Colloquial Urban), **Pnar** (Jaiñtia Hills), **War** (Southern escarpment), and **Bhoi** (Ri-Bhoi).
3. **📖 100,000+ (1 Lakh+) Trilingual Lexicon & Dictionary (`khasi.lexicon`)**:
   - Massive 100,000+ Khasi-English-Hindi lexical database extracted from 16 classical reference works and digitized texts (including U Mondon Bareh's *Khasi-English Course and Grammar*, U Nissor Singh's *Khasi-English Dictionary*, the *English-Khasi Dictionary*, Babu Jeebon Roy's foundational readers, and U Sib Charan Roy's philosophy) with part-of-speech, gender, etymology, and root fallback.
4. **🔡 Orthography, Phonetics & Normalizer (`khasi.phonetics`)**:
   - Unicode NFC standardizer, smart contraction expander (`nga'm` $\rightarrow$ `nga ym`, `u'n` $\rightarrow$ `u yn`), and diacritic restorer (`ï`, `ñ`).
   - Syllabification engine and bidirectional Devanagari $\leftrightarrow$ Latin transliteration.
5. **🔢 Base-10 Numeral & Number Engine (`khasi.numbers`)**:
   - Converts numbers up to crores/billions into formal Khasi words (`num_to_words`), ordinals (`ordinal`), and fractions.
6. **🌸 Matrilineal Heritage, Culture, Literature & Calendar (`khasi.culture`)**:
   - Complete documentation of the matrilineal kinship structure (*Kur* and *Kha*, *Ka Khadduh*, *U Kñi*, *Kmie-san*, *Kpa-san*, *Khun-kha*, *Shi-kur*, *Shi-kpoh*).
   - 7 classical literary figures (U Soso Tham, Babu Jeebon Roy, Radhon Singh Berry, Dr. H. Lyngdoh, U Mondon Bareh, U Sib Charan Roy, U Rabon Singh).
   - 15 traditional proverbs (*Ki Ktien Tymmen* / *Phawar*), 4 foundational folk epics (*U Sohpetbneng*, *U Thlen*, *Ka Nohkalikai*, *Manik Raitong*), 12 traditional lunar months (*Ki Bnai*), 4 seasons (*Ki Aïom*), and the 8-day rotating market cycle (*Sngi Iew*).
7. **🎙️ Voice Synthesis & SSML (`khasi.voice`)**:
   - SSML markup generator and PCM audio waveform generator for speech synthesis pipelines.
8. **🏛️ Digital Archival & Field Preservation (`khasi.preservation`)**:
   - Schema and metadata cataloging for field researchers, oral folktale archiving, orthographic health scoring, and export to **JSONL**, **CSV**, and **Hugging Face** formats.
9. **💻 Interactive CLI (`khasi`)**:
   - Command-line tool for translation, dictionary lookups, verb conjugation, cultural exploration, and statistics.

---

## 🚀 Installation

```bash
# Install directly from repository
pip install .

# Or install in editable mode for development
pip install -e .
```

---

## ⚡ Quick Start

```python
import khasi

# 1. Universal Multi-Dialect Translation
res = khasi.translate("How are you?")
print(res.text)  # "Kumno phi long?"

# Dialect variation (Pnar / Jaintia)
res_pnar = khasi.translate("I love you", dialect="pnar")
print(res_pnar.text)  # "Nga maya ïa phi."

# Hindi to Khasi
res_hi = khasi.translate("आप कैसे हैं?")
print(res_hi.text)  # "Kumno phi long?"

# 2. Dictionary & Lexical Lookup
entry = khasi.lookup("khublei")
print(entry["english"])  # "hello / thank you / greetings"
print(entry["hindi"])    # "नमस्ते / धन्यवाद / प्रणाम"

# 3. Numbers & Ordinals
print(khasi.num_to_words(42))   # "sawphew ar"
print(khasi.ordinal(1))         # "ba-nyngkong"
print(khasi.words_to_num("sawphew ar"))  # 42

# 4. Grammar & Verb Conjugation
# Tense-Aspect-Mood (TAM)
print(khasi.conjugate("wan", tense="past", pronoun="u"))     # "u la wan" (he came)
print(khasi.conjugate("wan", tense="future", pronoun="u"))   # "un wan" (he will come)

# Productive Derivations
print(khasi.causative("ïap"))     # "pynïap" (cause to die -> kill)
print(khasi.nominalize("stad"))   # "jingstad" (wise -> wisdom)
print(khasi.agent_noun("hikai"))  # "nonghikai" (teach -> teacher)

# 5. Morphological Analysis (300,000+ forms)
analysis = khasi.analyze("jingstad")
print(analysis.lemma)        # "stad"
print(analysis.pos)          # "derived_jing"
print(khasi.total_word_forms())  # 312,500+

# 6. Culture, Seasons & Market Cycle
season = khasi.get_current_season()
print(season["name_khasi"])  # e.g., "Aïom Synrai" (Autumn)

market_day = khasi.get_market_day(1)
print(market_day["name"])     # "Sngi Iewduh" (Shillong Barabazar)

# 7. Traditional Proverbs (Ki Ktien Tymmen)
p = khasi.proverbs.random()
print(f"\"{p['khasi']}\" - {p['meaning']}")
# "Kamai ïa ka hok." - Live by honest toil and upright conduct.
```

---

## 🖥️ Command Line Interface (CLI)

The library provides a standalone CLI command `khasi`:

```bash
# 1. Translate sentences into Khasi
khasi translate "How are you?"
khasi translate "Where are you going?" --dialect pnar

# 2. Look up a word in the dictionary
khasi lookup khublei
khasi lookup kshaid

# 3. Number conversions
khasi num 42
khasi num 2500

# 4. Conjugate verbs
khasi conjugate wan --tense past --pronoun u
khasi conjugate leit --tense future --pronoun nga

# 5. Culture, season & proverbs
khasi culture

# 6. Traditional riddles (Ki Jingkyntip)
khasi riddle

# 7. Corpus & dictionary statistics (105,000+ headwords)
khasi stats
```

---

## 📁 Project Architecture

```
khasi/
├── __init__.py           # Unified top-level standard library API & facades
├── constants.py          # ISO codes, alphabet, phonemes, dialects, moral pillars
├── phonetics.py          # Orthography normalizer, syllabifier, transliteration
├── cli.py                # Command-line interface
├── preservation.py       # Archival corpus manager, health scorer & dataset exporter
├── numbers/
│   ├── __init__.py
│   └── converter.py      # Base-10 Khasi number & ordinal engine
├── grammar/
│   ├── __init__.py
│   ├── nouns.py          # Noun gender articles (u, ka, i, ki) & declensions
│   ├── prepositions.py   # Case prepositions (jong, ha, sha, na, bad, ban, ïa)
│   ├── pronouns.py       # Pronominal paradigm & interrogatives
│   ├── verbs.py          # TAM conjugation & productive prefixes (pyn-, jing-, nong-)
│   └── syntax.py         # SVO sentence & question builder
├── lexicon/
│   ├── __init__.py
│   ├── dictionary.py     # Trilingual lookup & root fallback engine
│   ├── morphology.py     # 300,000+ inflectional & derivational universe engine
│   └── data/
│       ├── words.json    # Core vocabulary with dialect variants
│       ├── phrases.json  # Conversational phrases
│       ├── proverbs.json # Ki Ktien Tymmen / Phawar
│       └── riddles.json  # Traditional riddles (Ki Jingkyntip)
├── culture/
│   ├── __init__.py
│   ├── calendar.py       # Months (Ki Bnai), Seasons (Ki Aïom), 8-day Market Cycle
│   ├── festivals.py      # Shad Suk Mynsiem, Pomblang Nongkrem, Behdeinkhlam
│   ├── literature.py     # U Soso Tham, Babu Jeebon Roy, epics & folklore
│   └── kinship.py        # Matrilineal kinship system (Kur & Kha, Khadduh, Kñi)
├── translator/
│   ├── __init__.py
│   ├── engine.py         # Main translation coordinator
│   ├── rule_based.py     # Conversational maps & multi-dialect adaptations
│   ├── pivot.py          # Pivot translation engine
│   └── llm_adapter.py    # Generative neural prompt generator
└── voice/
    ├── __init__.py
    └── engine.py         # KhasiVoiceSynthesizer, SSML & PCM audio generation
```

---

## 📜 Linguistic & Cultural Notes

- **Language Family**: Austroasiatic $\rightarrow$ Mon-Khmer branch (sharing ancient linguistic affinity with Mon and Khmer in Southeast Asia, distinct from surrounding Tibeto-Burman and Indo-Aryan languages).
- **Four-Article Gender System**:
  - `u` : Masculine singular (e.g., *u briew* - the man, *u lum* - the mountain)
  - `ka`: Feminine singular (e.g., *ka kynthei* - the woman, *ka ïing* - the house, *ka wah* - the river)
  - `i`  : Diminutive / Affectionate (e.g., *i khunlung* - the baby)
  - `ki` : Plural for all genders (e.g., *ki briew* - the people)
- **Three Supreme Moral Pillars**:
  1. *Kamai ïa ka hok* : Earn righteousness through honest hard work.
  2. *Tip kur, tip kha* : Honor and know maternal lineage (*Kur*) and paternal heritage (*Kha*).
  3. *Tip briew, tip Blei* : Know and respect human dignity to know God.

---

## 👨‍💻 Author & Maintainer

**Akshat Singh Bisht**
- **Website**: [https://akshatsinghbisht.com/](https://akshatsinghbisht.com/)
- **Email**: [infoakshatsinghbisht@gmail.com](mailto:infoakshatsinghbisht@gmail.com)
- **LinkedIn**: [Akshat Singh Bisht](https://www.linkedin.com/in/akshat-singh-bisht-digital-performance-marketing-specialist/)
- **Amazon Author**: [Akshat Singh Bisht on Amazon](https://www.amazon.com/stores/Akshat-Singh-Bisht/author/B0D5TYDT28)
- **ResearchGate**: [Akshat Bisht](https://www.researchgate.net/profile/Akshat-Bisht-8)
- **GitHub**: [infoakshatsinghbisht-eng](https://github.com/infoakshatsinghbisht-eng)

---

## 📄 License

This project is licensed under the **MIT License**.
