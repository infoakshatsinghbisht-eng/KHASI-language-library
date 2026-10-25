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

## 🌟 Key Capabilities (Version 1.16.0 Milestone Expansion)

- **📖 608,086+ Headwords Lexicon (`khasi.lexicon`)**: Massively expanded vocabulary with verified words harvested directly across all 2,598 digitized authentic classical Khasi books, complete with English definitions, parts of speech, and literature source citations across `words.json` through `words_corpus_v28.json`.
- **📐 100 Classical Grammar Rules Engine (`khasi.grammar_rules`)**: Programmatic rule catalog, validation, and advanced syntax engine derived from historical, morphological, and dialectal treatises (Rev. H. Roberts 1891, Rev. Thomas Jones 1841, Rev. W. Pryse 1855, Dr. G. A. Grierson 1903, Babu Jeebon Roy 1897, Dr. R. S. Lyngdoh 1983), covering 9 categories: Nominal Agreement (9 rules), Tense-Aspect-Mood (25 rules), Case Marking (11 rules), Derivational Morphology (13 rules), Complex Syntax (12 rules), Enclitics & Expressives (12 rules), Numeral Classifiers (8 rules), Discourse Particles (6 rules), and Phonotactics & Morpho-Phonology (4 rules).
- **🌐 Parallel Sentence Alignment & MT Evaluation Toolkit (`khasi.parallel_corpus` / `khasi.corpus`)**: Parallel corpus management toolkit with bitext exporters for Hugging Face JSONL, TMX 1.4b, and parallel bitext (.kha, .en) formats, along with standard BLEU score calculation.
- **📚 2,598 Digitized Classical Books Directly in Library (`khasi.books` / `khasi.culture.books`)**: 384,803 individual pages and 87,565,954 words built directly into the Python package with page-by-page reading (`book.get_page(N)`), full text access (`book.full_text`), in-book search, and universal search across all 2,598 books. Complete with 1,939 preserved historical PDF scans and full-text editions in `data/khasi_books/`.
- **📄 1,939 Preserved Historical Book PDFs (`data/khasi_books/`)**: Preserved classical scans and full editions from Digital Library of India (DLI), Asiatic Society of Bengal, NEHU collections, and regional archives covering original Khasi folklore, literature, drama, poetry, grammar, history, and ethnography with full coverage.
- **📜 4,200,000+ Classical Grammatical Sentences**: Over 4.2 million standard sentences across all 2,598 digitized books segmented by Khasi orthographic and grammatical punctuation rules.
- **🎶 300 Traditional Songs & Phawar (`khasi.songs` / `khasi.culture.songs`)**: Complete lyrics, English translations, instrumentation, and cultural contexts across 58 genres.
- **⚡ 39 Indigenous Deities & Sacred Spirits (`khasi.culture.deities`)**: Complete pantheon of creator, celestial, mountain, river, gate, market, and guardian deities.
- **🌿 112 Native Flora & 89 Fauna (`khasi.culture.botany` / `khasi.culture.wildlife`)**: Comprehensive biological and ethnobotanical database of Meghalaya.
- **🧩 66 Traditional Riddles & 223 Colloquial Phrases (`khasi.riddles` / `khasi.phrases`)**: Everyday expressions, marketplace bargaining, slangs, moral sayings, and ancient folk riddles (*Ki Kyntip*).
- **🏛️ Khasi Oral Folklore, Myths & Legends (`khasi.folklore` / `khasi.culture.folklore`)**:
   - **12 foundational Khasi oral myths and legendary allegories** (over 6,950+ words of authentic Khasi prose and poetry):
     - *Ka Jingkieng Ksier* (The Sacred Golden Ladder & Genesis of the Seven Huts on Lum Sohpetbneng)
     - *U Diengiei* (The Tree of Eclipsing Darkness & Council of Lum Diengiei)
     - *U Sier Lapalang* (The Stately Stag & The Mother's Inconsolable Mountain Lament)
     - *U Manik Raitong* (The Melodies of the Sharati Flute & Tragic Devotion)
     - *Ka Nohkalikai* (The Leap of Likai & Waterfall of Tears)
     - *U Bsein Thlen* (The Monster Serpent & Slaying at Dainthlen)
     - *Ka Sngi bad U Bnai* (The Sun, the Moon & the Ash of Shame)
     - *U Klew bad Ka Sngi* (The Peacock's Love for the Sun)
     - *Ka Wah Umïam bad Ka Wah Umngot* (The Twin Sister Rivers)
     - *Ka Krem Lamet Latang* (The Primal Council Cave of Animals)
     - *Ki Mawbynna bad Ki Mawlynti* (The Megalithic Monoliths & Ancestral Guardians)
     - *Ka Pansngiat Ksiar Ka Meiramew* (The Golden Crown of Mother Earth & Seasons)
   - Section-by-section narratives, character registries, geographical origins, cultural moral tenets, full English translations, and indigenous glossaries.

2. **🎶 Traditional Songs, Ballads, Archery Phawar & Lyric Cycles (`khasi.songs` / `khasi.culture.songs`)**:
   - **10 structured traditional Khasi folk songs, chants, archery phawar, and literary song cycles**:
     - *Ki Sur Na Ka Duitara Ksiar* (H.W. Sten's monumental 1979 collection across 21 lyric poems and songs for the golden lute)
     - *Ka Sur U Sier Lapalang* (Complete multi-part epic lament and hunter verses)
     - *Phawar Shad Suk Mynsiem* (Spring thanksgiving dance chants and royal Weiking festival songs)
     - *Phawar Iasiat Khnam* (Traditional archery tournament victory cheers and battle couplets)
     - *Phawar Behdeiñkhlam* (Sacred Pnar plague-expelling chant at sacred pool Aitnar)
     - *Ka Sur Manik Raitong* (Sharati flute ballad and immortal romance)
     - *Ka Jingrwai Thiah Khunlung* (Traditional hearth lullaby)
     - *Ka Jingrwai U Hynniewtrep* (National creation hymn of the Seven Huts)
     - *Ka Sur Tirot Sing* (Patriotic freedom anthem of the Syiem of Nongkhlaw)
     - *Ki Rwaimar bad Jingrwai Ot Kba* (Highland harvest work songs and paddy calls)
   - Verse-by-verse bilingual lyrics, musical instrumentation catalog (*Duitara*, *Tangmuri*, *Maryngod*, *Sharati*, *Besli*, *Mieng*, *Nakra*, *Ksing*), and poetic vocabulary.

3. **🗣️ Dedicated Dialect Sub-Lexicons (`khasi.dialects` / `khasi.lexicon.dialects`)**:
   - **5,500+ words** for **Pnar / Synteng** (Jaiñtia Hills: Jowai, Shangpung).
   - **5,300+ words** for **War Khasi** (Southern Slopes & Shella).
   - **1,250+ words** for **Bhoi Khasi** (Ri-Bhoi) and **1,250+ words** for **Maram Khasi** (West Khasi Hills).
   - Unified cross-dialect bidirectional translation (`translate_dialect`), cognate discovery (`find_cognates`), and dialect statistics (`get_dialect_statistics`).

4. **🎙️ Audio Waveform Dataset for ASR & TTS (`khasi.audio_dataset` / `khasi.voice.dataset`)**:
   - **252 native speech recordings** in standard **16,000 Hz, 16-bit Mono Linear PCM WAV** format on disk (187 conversational phrases + 65 proverbs).
   - Exporters for **Hugging Face Audio Datasets** and **Mozilla Common Voice TSV**.

5. **📜 Parallel Corpus & MT Evaluation Toolkit (`khasi.parallel_corpus` / `khasi.corpus`)**:
   - Sentence-by-sentence parallel alignment benchmarks in **Khasi** and **English** across published masterworks.
   - High-level methods: `get_pairs()`, `get_book_sentences(book_id)`, and `search(query)`.
   - Exporters for **Hugging Face JSONL**, **TMX 1.4b**, and **parallel bitext** (.kha, .en).
   - Standard BLEU score calculation toolkit (`compute_bleu`).

8. **📂 Raw Digital Sources Archive (`data/raw_sources/`)**:
   - Raw source archives including dedicated folklore legends (`data/raw_sources/folklore/`) and authentic song manuscripts and collections (`data/raw_sources/songs/`).

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

# 2. Dictionary & Lexical Lookup (572,000+ words)
entry = khasi.lookup("khublei")
print(entry["english"])  # "hello / thank you / greetings"

# Newly harvested book vocabulary
rare_word = khasi.lookup("pynsneng")
print(rare_word)

# 3. Classical Grammar Rules Engine & Syntax Builders (90 Rules)
rule = khasi.grammar_rules.get("AGR-01")
print(rule.name)       # "Mandatory Article Prefixation"
print(rule.formula)    # "[Article: u / ka / i / ki] + [Noun Stem]"
print(rule.khasi_examples)

# Build advanced complex & conditional sentences
cond = khasi.build_conditional_sentence("phi wan", "ngan leit")
print(cond)  # "Lada phi wan, ngan leit."

comp = khasi.build_comparative_sentence("u ksew", "ka miaw", "heh")
print(comp)  # "u ksew u kham heh ban ïa ka miaw."

rel = khasi.build_relative_clause("ka samla", "trei shitom", gender="ka")
print(rel)   # "ka samla kaba trei shitom"

# 4. Traditional Organology & Musical Instruments
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

# 10. Digitized Whole Books Preservation Reader (1,100 Books, 114,177 Pages, 28.62M+ Words)
print(khasi.books.summary())
# {'total_books': 1100, 'total_pages': 114177, 'total_words': 28622094, ...}

# Read any book page directly from within the library
book = khasi.get_book("u_khasi_rodborne_t")
print(book.title)        # "U Khasi"
print(book.total_pages)  # 295
print(book.get_page(1))  # Full text of page 1!

# Universal full-text search across all 1,100 books
results = khasi.search_books("sohpetbneng")
print(f"Found {len(results)} occurrences across classical books.")

# 11. Khasi Oral Folklore, Myths & Legends (12 Master Narratives)
import khasi.folklore as kf
print(kf.folklore.summary())
# {'total_stories': 12, 'total_words': 6951, ...}

story = kf.get_story("ka_jingkieng_ksier")
print(story.khasi_title)          # "Ka Jingkieng Ksier bad Ki Hynñiew Trep"
print(story.geographic_origin)    # "Lum Sohpetbneng (Ri-Bhoi)"
print(story.khasi_text[:120])     # Genesis narrative
print(story.english_translation[:120])

# Search folklore legends
thlen_matches = kf.search_folklore("u thlen")
print(f"Found {len(thlen_matches)} stories mentioning U Thlen.")

# 12. Traditional Songs, Ballads & Phawar (10 Collections)
import khasi.songs as ks
print(ks.songs.summary())
# {'total_songs': 10, 'total_words': 2470, ...}

lapalang = ks.get_song("ka_sur_u_sier_lapalang")
print(lapalang.khasi_title)       # "Ka Sur U Sier Lapalang"
print(lapalang.instruments)       # ['Maryngod (bowed fiddle)', 'Shyngwiang', 'Duitara']
print(lapalang.lyrics_khasi[:100])

# Search songs and phawar couplets
archery_verses = ks.search_songs("khnam")
print(f"Found {len(archery_verses)} songs with archery terms.")

# 13. Master Bibliography Catalogue (344 Works)
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

## 👤 Author & Creator

- **Author & Principal Architect**: **Akshat Singh Bisht**
- **Website**: [akshatsinghbisht.com](https://akshatsinghbisht.com/)
- **Email**: `infoakshatsinghbisht@gmail.com`
- **GitHub**: [@infoakshatsinghbisht-eng](https://github.com/infoakshatsinghbisht-eng/KHASI-language-library)
- **LinkedIn**: [Akshat Singh Bisht](https://www.linkedin.com/in/akshat-singh-bisht-digital-performance-marketing-specialist/)
- **Amazon Author**: [Akshat Singh Bisht](https://www.amazon.com/stores/Akshat-Singh-Bisht/author/B0D5TYDT28)
- **ResearchGate**: [Akshat Bisht](https://www.researchgate.net/profile/Akshat-Bisht-8)

---

## 📜 Citation & Mandatory Attribution

If you use this library, its digitized texts, lexicons, grammar rules, cultural databases, audio recordings, or any derived software, computational models, or academic research, **you are required to provide prominent attribution and cite the author**:

### BibTeX
```bibtex
@software{bisht2026khasi,
  author       = {Akshat Singh Bisht},
  title        = {Khasi Language Library (Ka Ktien Khasi): Comprehensive NLP Engine, Classical Grammar, and Preserved Literature Archive},
  year         = {2026},
  publisher    = {GitHub},
  version      = {1.16.0},
  url          = {https://github.com/infoakshatsinghbisht-eng/KHASI-language-library}
}
```

### APA Format
> Bisht, A. S. (2026). *Khasi Language Library (Ka Ktien Khasi): Comprehensive NLP Engine, Classical Grammar, and Preserved Literature Archive* (Version 1.16.0) [Computer software]. https://github.com/infoakshatsinghbisht-eng/KHASI-language-library

---

## 📄 License & Terms

Distributed under the **MIT License**. Copyright (c) 2026 **Akshat Singh Bisht**. All rights reserved.  
Any redistribution, derivative application, research paper, or model trained on this library must retain the copyright notice, author attribution, and citation to **Akshat Singh Bisht**.
