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

## 🌟 Key Capabilities (Version 1.3.0 Milestone Expansion)

1. **🗣️ Dedicated Dialect Sub-Lexicons (`khasi.dialects` / `khasi.lexicon.dialects`)**:
   - **5,500+ words** for **Pnar / Synteng** (Jaiñtia Hills: Jowai, Shangpung) with authentic palatal shifts (`sh` $\rightarrow$ `ch`, `sng` $\rightarrow$ `sñ`), vowel shifts (`ie` $\rightarrow$ `u`/`e`, `ei` $\rightarrow$ `ai`), and lexical cognates (`bru`, `ïung`, `maya`, `bei`, `pa`, `chaat`, `lai`).
   - **5,300+ words** for **War Khasi** (Southern Slopes & Shella) with archaic Mon-Khmer root preservation (`brou`, `ïeng`, `am`, `ba`, `da`, `hie`, `van`, `thaw`).
   - **1,250+ words** for **Bhoi Khasi** (Ri-Bhoi) and **1,250+ words** for **Maram Khasi** (West Khasi Hills).
   - Unified cross-dialect bidirectional translation (`translate_dialect`), cognate discovery (`find_cognates`), and dialect statistics (`get_dialect_statistics`).
2. **🎙️ Audio Waveform Dataset for ASR & TTS (`khasi.audio_dataset` / `khasi.voice.dataset`)**:
   - **252 native speech recordings** in standard **16,000 Hz, 16-bit Mono Linear PCM WAV** format on disk.
   - 187 practical conversational phrases paired with `phrase_001.wav` through `phrase_187.wav`.
   - 65 traditional chanted proverbs paired with `proverb_001.wav` through `proverb_065.wav`.
   - Comprehensive multi-format dataset manifests (`audio_manifest.json`, `audio_manifest.jsonl`) with train/validation/test splits, speaker profiles (Female `SPK_KHA_F01`, Male `SPK_KHA_M01`), and 1-click exporters for **Hugging Face Audio Datasets** and **Mozilla Common Voice TSV**.
3. **📜 Aligned Parallel Corpora & MT Benchmarks (`khasi.parallel_corpus` / `khasi.corpus`)**:
   - Sentence-by-sentence parallel alignment between Khasi and English across public domain masterworks:
     - *Ka Niam Jong Ki Khasi* (U Sib Charan Roy, 1919) — Indigenous theology, ethics, sacred groves, and covenant philosophy.
     - *Ka Jingiaid U Pilgrim* (*The Pilgrim's Progress* in Khasi, John Bunyan / Thomas Jones / Dr. John Roberts / Mondon Bareh) — Foundational literary prose.
     - *Ki Dienjat Jong Ki Longshwa & Kot Pule* — Classic folklore (*Lum Diengiei*, *Lum Sohpetbneng*, *Manik Raitong*, *U Thlen*, *Ka Sngi bad u Bnai*).
   - Standard Bitext exports (`train.kha`, `train.en`, `test.kha`, `test.en`), **TMX 1.4b Translation Memory XML**, and built-in BLEU score calculation toolkit for Machine Translation evaluation.
4. **📚 300,000+ Morphological Word Forms (`khasi.lexicon.morphology`)**:
   - Dynamic inflectional and derivational engine generating extensive verbal TAM forms, nominalizations (`jing-`), causatives (`pyn-`), agentives (`nong-`), experientials (`sngew-`), and prepositional case declensions across noun gender articles (`u`, `ka`, `i`, `ki`).
5. **📖 105,225+ Trilingual Lexicon & Dictionary (`khasi.lexicon`)**:
   - Massive 105,225+ Khasi-English-Hindi lexical database enriched with verified modern terminology: **Technology & AI**, **Government & Law**, **Jobs & Banking**, **Education & Science**, **Crime & Public Safety**, **Ethnomedicinal Botany**, **Highland Wildlife**, **Traditional Cuisine**, **Indigenous Rituals**, and **Local Deities**.
6. **💬 187 Practical Conversational Phrases (`khasi.phrases`)**:
   - Comprehensive situational phrasebook covering 15 life categories: Greetings, Courtesy, Directions & Travel, Market (*Iewduh*) Shopping, Dining & Tea Stalls (*Dukan Sha*), Home Hospitality, Parenting & Children, School, Office & Business, Health & Emergencies, Police & Cyber Safety, Technology & WiFi, Highland Weather, and Festive Blessings.
7. **📜 65 Authentic Proverbs & 32 Traditional Riddles (`khasi.proverbs`, `khasi.riddles`)**:
   - Moral philosophy proverbs (*Ki Ktien Tymmen* / *Phawar*) with literal translation, contextual meaning, and Hindi translation.
   - Traditional mountain riddles (*Ki Jingkyntip*) with cultural explanations.
8. **🎵 Khasi Music, Song Lyrics & Organology (`khasi.music`, `khasi.songs`)**:
   - 12 traditional instruments (*Duitara*, *Tangmuri*, *Ksing Shynrang*, *Ksing Kynthei*, *Nakra*, *Padiah*, *Maryngod*, *Mieng*, *Besli*, *Shyngwiang*, *Kynshaw*, *Symphiah*).
   - 8 authentic folk songs, thanksgiving chants, and laments complete with **full Khasi verses and English translations** (*Phawar Shad Suk Mynsiem*, *Phawar Iasiat Khnam*, *Phawar Behdeiñkhlam*, *Ka Sur U Sier Lapalang*, *Ka Sur Manik Raitong*, *Ka Jingrwai Thiah Khunlung*, *Ka Jingrwai U Hynniewtrep*, *Ka Sur Tirot Sing*).
   - Registry of legendary balladeers (Bah Kerios Wahlang, Dr. Helen Giri, Lou Majaw, Skendrowell Syiemlieh, Da-Thymmei, Soulmate).
9. **⚡ Indigenous Rituals & Divination (`khasi.rituals`)**:
   - Comprehensive documentation of 10+ core ceremonial practices: egg divination (*Ka Shat Pylleng*), thunder omen interpretation (*Ka Khan Pyrthat*), cock mediator sacrifice (*U Syiar Ryngkew*), royal goat sacrifice (*Ka Pomblang Nongkrem*), clan megalithic bone internment (*Ka Thep Mawbah*), naming dedication (*Ka Jer Ka Thoh*), matrilocal marriage covenant (*Ka Shongkurim*), village cleansing (*Ka Kñia Shnong*), genealogical invocation (*Ka Tangsnoing*), and serpent curse expiation (*Ka Pyllait Thlen*).
10. **🏔️ Khasi Pantheon & Territorial Deities (`khasi.deities`)**:
    - Complete indigenous theological registry: Supreme Creator (*U Blei Nongbuh Nongthaw*), Mother Earth (*Ka Meiramew*), mountain ruler (*U Lei Shyllong*), primal maternal intercessor (*U Suidnia*), primal matriarch (*Ka Iawbei*), primal father (*U Thawlang*), forest guardians (*U Ryngkew U Basa / Labasa*), rock sovereign (*U Leisymper*), river goddess (*Ka Kupli*), righteous wealth deity (*U Lei Longspah*), and Pnar guardian (*U Blai Synteng*).
11. **🗿 Sacred Sites, Megaliths & Sacred Groves (`khasi.sacred_sites`)**:
    - Prehistoric megalith complexes (*Ki Mawbynna Nartiang* with the world's tallest 8.3m menhir), 800-year-old virgin cloud forests (*Law Kyntang Mawphlang*), mythological summits (*Lum Sohpetbneng*, *Lum Shillong*), ceremonial mud pools (*Ka Aitnar* in Jowai), and sacred limestone cave sanctuaries (*Krem Mawmluh*).
12. **🌿 Ethnomedicinal Botany & Biodiversity (`khasi.botany`)**:
    - 30+ verified Khasi plants, wild fruits, and healing herbs with binomial scientific names, families, and indigenous medicinal applications (*Nepenthes khasiana*, *Prunus nepalensis*, *Myrica esculenta*, *Elaeagnus latifolia*, *Houttuynia cordata*, *Centella asiatica*, *Clerodendrum colebrookianum*, *Pinus kesiya*, *Ficus elastica*, *Curcuma longa var. Lakadong*, etc.).
13. **🐾 Highland Wildlife & Fauna (`khasi.wildlife`)**:
    - 22+ native wildlife species with scientific names and folklore context (*Neofelis nebulosa*, *Panthera tigris*, *Rusa unicolor*, *Ursus thibetanus*, *Buceros bicornis*, *Tor putitora*, *Python bivittatus*, *Bufoides meghalayanus*, *Samia cynthia ricini*, etc.).
14. **🍲 Traditional Gastronomy & Food Culture (`khasi.cuisine`)**:
    - 17 traditional culinary entries (*Jadoh*, *Dohkhlieh*, *Dohneiiong*, *Tungrymbai*, *Ja Stem*, *Pumaloi*, *Pukhlein*, *Tungtap*, *Kwai bad Tympew*, *Sha Saw*, *Khiew Ranei*, *Saraw*).
15. **🏞️ Geography, Topography & Landscapes (`khasi.geography`)**:
    - 27 documented sites: crystal rivers (*Wah Umngot*, *Wah Umiam*), towering waterfalls (*Kshaid Nohkalikai*, *Dainthlen*), limestone caves (*Krem Liat Prah*, *Krem Puri*), living root bridges (*Jingkieng Jri Nongriat*), and traditional Syiemships (*Hima Khyrim*, *Hima Mylliem*, *Hima Sohra*, *Hima Nongkhlaw*).
16. **👥 Matrilineal Kinship, Clans & Idioms (`khasi.kinship`, `khasi.clans`, `khasi.idioms`)**:
    - 45+ kinship terms, clan exogamy taboos (*Sang*), and ultimogeniture inheritance by *Ka Khadduh*.
    - 29 documented Khasi and Pnar clans (*Syiem*, *Lyngdoh*, *Nongrum*, *Wahlang*, *Kharbangar*, *Dkhar*, *Rymbai*, *Laloo*, *Tham*, *Bareh*, etc.).
    - 24 coupled rhyming idioms (*Ki Ktien Kynnoh*) and parables (*Ki Pharshi*).
17. **📚 Master Khasi Bibliography & Corpus Catalogue (`khasi.catalogue`)**:
    - Structured digital catalogue of **344 definitive Khasi literary works, historical monographs, grammatical treatises, and dictionaries** across 8 core genres with queryable metadata for NLP research and corpus linguistics.
18. **📂 Raw Digital Sources Archive (`data/raw_sources/`)**:
    - Over **400,000 characters** of transcribed raw text extracted from digitized books, poetry compilations, and ritual treatises across songs (`songs/`), rituals (`rituals/`), deities (`deities/`), and sacred sites (`sacred_sites/`).

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

# 2. Dictionary & Lexical Lookup (105,000+ words)
entry = khasi.lookup("khublei")
print(entry["english"])  # "hello / thank you / greetings"

tech_entry = khasi.lookup("kompiwter")
print(tech_entry["english"])  # "computer"

# 3. Traditional Organology & Musical Instruments
duitara = khasi.instruments.get("duitara")
print(duitara["description"])
# "The four-stringed plucked folk lute, revered as the living archive..."

# 4. Ethnomedicinal Botany & Scientific Names
sohiong = khasi.plants.get("sohiong")
print(sohiong["scientific_name"])  # "Prunus nepalensis"
print(sohiong["family"])           # "Rosaceae"

# 5. Native Wildlife
leopard = khasi.wildlife.get("khla-lyngngoh")
print(leopard["scientific_name"])  # "Neofelis nebulosa"
print(leopard["status"])           # "State Animal of Meghalaya"

# 6. Traditional Cuisine & Utensils
jadoh = khasi.dishes.get("jadoh")
print(jadoh["description"])  # "The crown jewel of Khasi gastronomy..."

# 7. Sacred Geography & Landscapes
cave = khasi.places.get("Mawmluh")
print(cave["significance"])  # "Global geological type-locality for the 'Meghalayan Age'..."

# 8. Matrilineal Clans & Coupled Idioms
lyngdoh_clan = khasi.clans.get("lyngdoh")
print(lyngdoh_clan["category"])  # "Priestly / Administrative Clan"

idiom = khasi.idioms.get("horkit")
print(idiom["meaning"])  # "Resolutely / through thick and thin..."

# 9. Proverbs & Riddles
proverb = khasi.proverbs.random()
print(f"\"{proverb['khasi']}\" - {proverb['meaning']}")

riddle = khasi.riddles.random()
print(f"Riddle: {riddle['riddle']} -> Solution: {riddle['solution']}")

# 10. Master Bibliography Catalogue (344 Works)
print(khasi.catalogue.summary())
# {'total_works': 344, 'genres': {'Original Khasi literature': 165, ...}}

# 11. Dedicated Dialect Sub-Lexicons & Cognate Mapping (13,000+ entries)
print(khasi.dialects.cognates("briew"))
# {'sohra': 'briew', 'pnar': 'bru', 'war': 'brou', 'bhoi': 'briu', 'maram': 'briu'}

pnar_translated = khasi.dialects.translate("U briew u ieit ia ka mei bad u kpa ha ïing.", "sohra", "pnar")
print(pnar_translated)
# "U bru u maya ia ka bei bad u pa ha ïung."

war_translated = khasi.dialects.translate("U briew u leit sha ïing ban bam ja bad dih um.", "sohra", "war")
print(war_translated)
# "U brou u hie sa ïeng ban bam ba bad dih am."

# 12. Audio Waveform Dataset (252 Waveforms for ASR/TTS Pipelines)
audio_item = khasi.audio_dataset.get_item("phrase_001")
print(audio_item["khasi_text"], audio_item["sample_rate"])
# "Khublei!" 16000

# Export dataset directly to Hugging Face or Common Voice format
khasi.audio_dataset.export_huggingface_format("dataset_audio.jsonl")
khasi.audio_dataset.export_common_voice_tsv("common_voice_khasi.tsv")

# 13. Aligned Parallel Corpora & MT Evaluation (BLEU)
pairs = khasi.parallel_corpus.get_pairs()
print(f"Loaded {len(pairs)} aligned Khasi-English sentence pairs.")
sample_kh, sample_en = pairs[0]
print(f"Kha: {sample_kh}\nEng: {sample_en}")

# Compute BLEU baseline for machine translation hypotheses
bleu_results = khasi.parallel_corpus.compute_bleu(
    hypotheses=["U briew u wan sha kane ka pyrthei ban kamai ïa ka Hok."],
    references=["U briew u wan sha kane ka pyrthei tang ban kamai ïa ka Hok."]
)
print(f"Sentence BLEU: {bleu_results['bleu']}%")
```

---

## 🖥️ Command Line Interface (CLI)

The package provides a built-in interactive CLI:

```bash
# Look up word
khasi lookup khublei

# Translate phrase
khasi translate "Where is the road to Sohra?" --dialect sohra

# Conjugate verb
khasi conjugate wan --tense past --pronoun u

# Show random proverb
khasi proverb

# Show random riddle
khasi riddle

# Show library statistics
khasi stats
```

---

## 🧪 Testing

```bash
# Run unit tests
python -m unittest discover -s tests
```

---

## 📄 License & Attribution

Distributed under the **MIT License**. Created and maintained by **Akshat Singh Bisht** (2026).
Contributions welcome via GitHub issues and pull requests.
