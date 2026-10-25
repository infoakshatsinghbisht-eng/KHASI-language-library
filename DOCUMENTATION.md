# Khasi Language Library (Ka Ktien Khasi) — Complete API Documentation

Comprehensive technical documentation for the `khasi` Python library (version 1.16.0).

---

## 1. Top-Level Facade (`import khasi`)

The root `khasi` package provides direct, high-level access to the most common operations:

### Core Functions

| Function | Signature | Description |
|---|---|---|
| `translate()` | `translate(text, source='auto', target='khasi', dialect='sohra')` | Translates English, Hindi, or Hinglish into Khasi with dialect adaptation. |
| `lookup()` | `lookup(word: str)` | Looks up a word in the 608,000+ comprehensive dictionary with prefix stripping fallback. |
| `search()` | `search(query: str)` | Searches for matching words across Khasi, English, and Hindi. |
| `analyze()` | `analyze(word: str)` | Decomposes a word morphologically (lemma, POS, prefixes). |
| `total_word_forms()` | `total_word_forms() -> int` | Returns total combinatorial forms represented (600,000+). |
| `build_sentence()` | `build_sentence(subject, verb, obj, tense, aspect, negative)` | Generates complete grammatical simple sentences with copy agreement. |
| `build_complex_sentence()` | `build_complex_sentence(main, sub, conjunction)` | Links clauses with subordinate conjunctions (`namar ba`, `ba`, `katba`). |
| `build_conditional_sentence()` | `build_conditional_sentence(condition, consequence, concessive)` | Generates conditional (`Lada...`) and concessive (`Wat la... pynban...`) sentences. |
| `build_relative_clause()` | `build_relative_clause(antecedent, verb_clause, gender)` | Constructs relative clauses (`uba`, `kaba`, `kiba`, `iba`). |
| `build_comparative_sentence()` | `build_comparative_sentence(item1, item2, adjective)` | Builds comparative superiority clauses (`kham... ban ïa`). |
| `build_passive_sentence()` | `build_passive_sentence(patient, verb, agent, adversative)` | Constructs adversative (`shah`) and neutral passives. |
| `num_to_words()` | `num_to_words(n: int) -> str` | Converts integer to formal Khasi words. |
| `words_to_num()` | `words_to_num(text: str) -> int` | Converts Khasi word number back to integer. |
| `ordinal()` | `ordinal(n: int) -> str` | Returns ordinal form (e.g., 1 -> `ba-nyngkong`). |
| `fraction()` | `fraction(num: int, denom: int) -> str` | Returns fraction expression (e.g., `shiteng`). |
| `conjugate()` | `conjugate(verb, tense='present', pronoun='nga', aspect='simple', negative=False)` | Generates full TAM verb clauses. |
| `causative()` | `causative(verb: str) -> str` | Derives causative verb form (`pyn-`). |
| `nominalize()` | `nominalize(word: str) -> str` | Derives abstract noun (`jing-`). |
| `agent_noun()` | `agent_noun(verb: str) -> str` | Derives agentive doer noun (`nong-`). |
| `get_current_season()` | `get_current_season() -> Dict[str, str]` | Returns current Khasi season (*Ki Aïom*). |
| `get_current_khasi_month()`| `get_current_khasi_month() -> Dict[str, Any]` | Returns current Khasi month (*Ki Bnai*). |
| `get_market_day()` | `get_market_day(day_index: int) -> Dict[str, Any]` | Information from the 8-day traditional *Sngi Iew* cycle. |
| `list_festivals()` | `list_festivals() -> List[Dict[str, Any]]` | Returns 18 documented traditional Khasi festivals. |
| `get_festival()` | `get_festival(query: str) -> Optional[Dict[str, Any]]` | Finds festival by name, location, or tradition. |

### Top-Level Facade Objects

- `khasi.phrases.all()` / `khasi.phrases.random()` : 206 practical conversational phrases across 15 categories (greetings, dining, travel, hospital, police, school, office, tech, etc.).
- `khasi.proverbs.all()` / `khasi.proverbs.random()` : 65+ authentic moral proverbs (*Ki Ktien Tymmen* / *Phawar*) with literal and contextual translations.
- `khasi.riddles.all()` / `khasi.riddles.random()` : 52 traditional Khasi riddles (*Ki Jingkyntip*) with solutions and cultural hints.
- `khasi.instruments.all()` / `khasi.instruments.get(name)` : Traditional musical instruments (*Duitara*, *Tangmuri*, *Ksing*, *Nakra*, *Maryngod*, *Mieng*, *Besli*, etc.).
- `khasi.books.all()` / `khasi.books.get(id_or_title)` / `khasi.books.read(id, page)` : Whole digitized books reader with **1,233 foundational classical and academic masterworks directly in the library** (127,880 pages, 32,456,918 words), supporting page-by-page reading, in-book text search, and cross-book full-text search without any external PDF dependencies. Complete with 1,939 preserved historical PDF scans and full editions in `data/khasi_books/`.
- `khasi.grammar_rules.all()` / `khasi.grammar_rules.get(id)` / `khasi.grammar_rules.by_category(c)` : **100 Classical Khasi Grammar Rules Engine** catalogued across 9 formal grammatical categories (Nominal Agreement, TAM, Case Marking, Derivational Morphology, Complex Syntax, Enclitics & Expressives, Numeral Classifiers, Discourse Particles, Phonotactics & Morpho-Phonology).
- `khasi.clothing.all()` / `khasi.clothing.get(name)` / `khasi.clothing.by_gender(g)` : Traditional garments (*Jaiñsem*, *Dhara*, *Jaiñkup*, *Kyrshah*, *Tapmohkhlieh*, *Jaiñpien*, *Jymphong*, *Spong*, *Jaiñboit*).
- `khasi.jewellery.all()` / `khasi.jewellery.get(name)` / `khasi.jewellery.by_gender(g)` : Traditional jewellery & ornaments (*Pansngiat*, *Paila Mukmor*, *Kynjri Ksiar*, *Kynjri Rupa*, *Shanryndang*, *Siar Kynthei*, *Mahu*, *Ta-kora*, *Sa-shiah*, *Siatsngi*, *Kynjri Tabah*).
- `khasi.fabrics.all()` / `khasi.fabrics.get(name)` : Indigenous sacred handloom textiles (*Ryndia* peace silk from Ri Bhoi, *Thoh Khyrwang* from Jaintia, *Jaiñsem Muga*, *Sulan*).
- `khasi.regalia.all()` / `khasi.regalia.get(name)` : Martial dance regalia & sacred arms (*Waitlam*, *Stieh*, *Symphiah*, *Ryntieh bad Khnam*, *Wait-bnoh*, *Pah-wait*).
- `khasi.rituals.all()` / `khasi.rituals.get(name)` / `khasi.rituals.by_category(c)` : 15 traditional rituals, egg divination (*Ka Shat Pylleng*), sacrifices, megalith consecration (*Ka Kñia Mawbynna*), and pestilence-chasing (*Behdeinkhlam*).
- `khasi.deities.all()` / `khasi.deities.get(name)` / `khasi.deities.by_realm(r)` : 29 indigenous Khasi pantheon, creator, celestial, territorial protectors, mountain rulers, and spirits.
- `khasi.sacred_sites.all()` / `khasi.sacred_sites.get(name)` / `khasi.sacred_sites.by_type(t)` : Sacred groves (*Law Kyntang*), prehistoric megalith complexes (*Mawbynna*), and altars.
- `khasi.plants.all()` / `khasi.plants.get(query)` / `khasi.plants.medicinal()` : 105 ethnomedicinal flora, wild fruits, trees, and orchids with binomial scientific names.
- `khasi.wildlife.all()` / `khasi.wildlife.get(query)` : 80 native mammals, birds, fish, reptiles, amphibians, and insects with scientific names and folklore context.
- `khasi.dishes.all()` / `khasi.dishes.get(name)` : Traditional culinary heritage (*Jadoh*, *Dohkhlieh*, *Dohneiiong*, *Tungrymbai*, *Ja Stem*, *Pumaloi*, *Pukhlein*, *Khiew Ranei*).
- `khasi.places.all()` / `khasi.places.get(name)` : Sacred geographical sites, rivers (*Wah*), waterfalls (*Kshaid*), peaks (*Lum*), caves (*Krem*), sacred groves (*Law Kyntang*), root bridges (*Jingkieng Jri*), and Syiemships (*Hima*).
- `khasi.clans.all()` / `khasi.clans.get(name)` / `khasi.clans.search(query)` : 105+ recognized Khasi, Pnar, War, Bhoi, and Maram clans (*Kur* and *Jaid*), branches, and historical offices.
- `khasi.list_names()` / `khasi.get_name(name)` : 52 traditional given names (male, female, unisex, market day) with meanings and etymology.
- `khasi.idioms.all()` / `khasi.idioms.get(query)` : 34 coupled rhyming idioms (*Ki Ktien Kynnoh*) and parables (*Ki Pharshi*).
- `khasi.roots.all()` / `khasi.roots.get(root)` / `khasi.roots.by_category(c)` : Authentic Austroasiatic/Mon-Khmer roots (*Ki Ktien Tynrai*) for anatomy, elements, moral pillars, and verbs with etymological cognates.
- `khasi.expressives.all()` / `khasi.expressives.get(name)` / `khasi.expressives.by_domain(d)` : World-famous Khasi phonaesthetic ideophones (*Ki Ktien Pynshai Dur*) vividly expressing colors, textures, temperatures, gaits, and sounds.
- `khasi.grammar_rules.all()` / `khasi.grammar_rules.get(id)` / `khasi.grammar_rules.by_category(c)` / `khasi.grammar_rules.search(q)` : 90 classical grammar rules engine (*Ka Riti Ktien Khasi*) covering 9 categories: nominal agreement (8 rules), tense-aspect-mood (23 rules), case marking (10 rules), derivational morphology (12 rules), complex syntax & clause subordination (11 rules), enclitics & expressives (11 rules), numeral classifiers (7 rules), discourse particles (5 rules), and phonotactics & morpho-phonology (3 rules).

---

## 2. Phonetics & Orthography (`khasi.phonetics`)

- `normalize(text: str) -> str`: Normalizes Unicode to NFC, standardizes apostrophes, and restores diacritics (`ï`, `ñ`).
- `tokenize(text: str, lower=False, keep_punct=True) -> List[str]`: Tokenizes preserving internal apostrophes, hyphens, and diacritics.
- `syllables(word: str) -> List[str]`: Syllabification engine tailored for Khasi phonotactics.
- `latin_to_devanagari(text: str) -> str`: Transliterates Latin Khasi into Devanagari.
- `devanagari_to_latin(text: str) -> str`: Converts Devanagari transliteration back to Latin Khasi.
- `is_khasi_word(word: str) -> bool`: Checks orthographic validity.
- `has_khasi_diacritics(text: str) -> bool`: Checks presence of `ï` or `ñ`.

---

## 3. Grammar & Morphology (`khasi.grammar`)

### Nouns & Gender Articles (`khasi.grammar.nouns`)
- Gender articles:
  - `u` : Masculine singular
  - `ka`: Feminine singular
  - `i` : Diminutive / Affectionate
  - `ki`: Plural
- `pluralize(phrase: str) -> str`: Smartly converts article-marked noun phrases to plural (`u briew` -> `ki briew`).
- `make_diminutive(phrase: str) -> str`: Converts to affectionate/diminutive form (`u khunlung` -> `i khunlung`).
- `decline_noun(lemma, article) -> Dict[str, str]`: Generates grammatical case declensions (Nominative, Accusative, Genitive, Dative, Locative, Ablative, Allative, Instrumental).

### Verb Conjugation & TAM (`khasi.grammar.verbs`)
- `conjugate(verb, tense, pronoun, aspect, negative)`: Generates full verbal clauses across Past, Present, Future, Future Definite, Habitual, and Progressive aspects.
- Derivational prefixes:
  - `causative(verb)` : `pyn-` (e.g. `ïap` -> `pynïap`)
  - `nominalize(word)` : `jing-` (e.g. `stad` -> `jingstad`)
  - `agent_noun(verb)` : `nong-` (e.g. `hikai` -> `nonghikai`)
  - `experiential(adj)` : `sngew-` (e.g. `bha` -> `sngewbha`)

### Adjectives & Adverbs (`khasi.grammar.adjectives`, `khasi.grammar.adverbs`)
- `make_attributive(adj)`: Generates participle adjective (`ba-` prefix: `bha` -> `ba-bha`).
- `make_comparative(adj, than)`: Generates comparative grade (`kham ... ban ïa ...`).
- `make_superlative(adj)`: Generates superlative grade (`ba-... tam`).
- `reduplicate_adverb(adv)`: Generates expressive adverbial reduplications (`suki` -> `suki-suki`).
- `list_echo_words()`: Returns authentic Khasi echo/jingle words.

---

## 4. Multi-Dialect Translation Engine (`khasi.translator`)

- `translate(text, source='auto', target='khasi', dialect='sohra')`: Rule-based and lexical translator supporting:
  - `sohra` : Standard literary Khasi
  - `shillong`: Urban colloquial Khasi
  - `pnar` : Jaiñtia variant
  - `war` : Southern slope variant
  - `bhoi` : Ri-Bhoi variant
- `TranslationResult`: Result object with `text`, `source_lang`, `target_lang`, `confidence`, and `dialect`.

---

## 5. Culture, Heritage & Ethnoscience (`khasi.culture`)

### Kinship System (`khasi.culture.kinship`)
- `list_kinship_terms()`: 45+ terms documenting the world's largest surviving matrilineal system (*Mei*, *Pa*, *Khadduh*, *Kñi*, *Kur*, *Kha*, *Shi-kur*, *Shi-kpoh*, *Kpoh*, *Sang*, *Ma*, *Poikha*, *Thep Mawbah*).
- `describe_matrilineal_system()`: Complete overview of matrilineal organization, clan exogamy, and ultimogeniture inheritance.

### Literature, Epics & Authors (`khasi.culture.literature`)
- `authors()`: 24 prominent authors (U Soso Tham, Babu Jeebon Roy, Radhon Singh Berry, Dr. H. Lyngdoh, U Mondon Bareh, U Sib Charan Roy, U Rabon Singh, Prof. Streamlet Dkhar, Victor G. Bareh, Dr. Hamlet Bareh, Prof. Kynpham Sing Nongkynrih, Prof. Desmond Kharmawphlang, Prof. Esther Syiem, Donbok T. Laloo, K.W. Nongrum, K.K. Kharlukhi, etc.).
- `epics()`: 15 classical epics (*U Sohpetbneng*, *U Thlen*, *Ka Nohkalikai*, *Manik Raitong*, *Ka Pansngiat Ksiar Ka Meiramew*, *Ka Krem Tirot*, *U Sier Lapalang*, *Ka Sngi bad U Bnai*, *U Klew bad Ka Sngi*, *U Lum Diengiei*, *U Mawlongbna*, *Ka Krem Lamet Latang*, *Ka Umïam*, *U Sim Pyllieng*, *Ki Mawbynna U Hynniewtrep*).
- `poems()`: Classical verse collections with English translations.

### Music & Organology (`khasi.culture.music`)
- `list_instruments()` / `get_instrument(name)`: 12 traditional instruments (*Duitara*, *Tangmuri*, *Ksing Shynrang*, *Ksing Kynthei*, *Nakra*, *Padiah*, *Maryngod*, *Mieng*, *Besli*, *Shyngwiang*, *Kynshaw*, *Symphiah*).
- `list_songs()` / `get_song(title)`: 8 folk songs, thanksgiving chants, and funeral laments.
- `list_musicians()`: Renowned artists (Bah Kerios Wahlang, Dr. Helen Giri, Lou Majaw, Skendrowell Syiemlieh, Da-Thymmei, Soulmate).

### Botany & Ethnomedicine (`khasi.culture.botany`)
- `list_plants()` / `get_plant(query)` / `medicinal_plants()`: 30+ verified Khasi plants with scientific binomial names, families, and indigenous applications (*Nepenthes khasiana*, *Prunus nepalensis*, *Myrica esculenta*, *Elaeagnus latifolia*, *Houttuynia cordata*, *Centella asiatica*, *Clerodendrum colebrookianum*, *Paris polyphylla*, *Pinus kesiya*, *Ficus elastica*, *Curcuma longa var. Lakadong*, etc.).

### Wildlife & Fauna (`khasi.culture.wildlife`)
- `list_wildlife()` / `get_animal(query)` / `by_wildlife_class(c)`: 22+ native wildlife species with scientific names and folklore context (*Neofelis nebulosa*, *Panthera tigris*, *Rusa unicolor*, *Ursus thibetanus*, *Buceros bicornis*, *Tor putitora*, *Python bivittatus*, *Bufoides meghalayanus*, *Apis cerana himalaya*, *Samia cynthia ricini*, etc.).

### Cuisine & Food Culture (`khasi.culture.cuisine`)
- `list_dishes()` / `get_dish(name)` / `by_cuisine_category(c)`: 17 traditional culinary entries (*Jadoh*, *Dohkhlieh*, *Dohneiiong*, *Tungrymbai*, *Ja Stem*, *Pumaloi*, *Pukhlein*, *Tungtap*, *Kwai bad Tympew*, *Sha Saw*, *Khiew Ranei*, *Saraw*, etc.).

### Geography & Sacred Landscapes (`khasi.culture.geography`)
- `list_places()` / `get_place(name)` / `by_geography_type(t)`: 27 documented sites including crystal rivers (*Wah Umngot*), soaring cascades (*Nohkalikai*, *Dainthlen*), holy peaks (*Lum Shillong*, *Lum Sohpetbneng*), record-holding caves (*Krem Liat Prah*, *Krem Puri*, *Krem Mawmluh*), 800-year-old virgin groves (*Law Kyntang Mawphlang*), double-decker living root bridges (*Jingkieng Jri Nongriat*), and historic Syiemships (*Hima Khyrim*, *Hima Mylliem*, *Hima Sohra*, *Hima Nongkhlaw*).

### Clans & Surnames (`khasi.culture.clans`)
- `list_clans()` / `get_clan(name)` / `search_clans(query)`: 29 documented Khasi and Pnar clans (*Syiem*, *Lyngdoh*, *Nongrum*, *Wahlang*, *Kharbangar*, *Dkhar*, *Rymbai*, *Laloo*, *Tham*, *Bareh*, etc.).

### Idioms & Coupled Expressions (`khasi.culture.idioms`)
- `list_idioms()` / `get_idiom(query)`: 24 coupled idioms (*Ktien Kynnoh*) and parables (*Ki Pharshi*).

---

## 6. Digitized Whole Books & Preservation Reader (`khasi.books` / `khasi.culture.books`)

Access the **whole book data** (all pages, chapters, and full texts) for **24 foundational Khasi literary, theological, historical, dramatic, and linguistic classics** (over **1,980+ pages** and **470,000+ words** preserved in full text):

- **Radhon Singh Berry**: *Ka Jingsneng Tymmen Part 1 & Part 2* (1903) — Classical rhyming ethical verse (*Phawar*).
- **Dr. Streamlet Dkhar**: *Na Lyngwiar Dpei I Mei*, *Ki Umjer Rupa*, *U Raikut*, *Na Khriang Ka Dohnud*, *Ka Jinglong Tynrai U Briew Kat Kum Ki Drama Khasi*.
- **U Sib Charan Roy**: *Ka Niam Ki Khasi: Ka Niam Tip-Blei Tip-Briew* (1919) — Foundational theological treatise on Khasi monotheism.
- **Dr. H. Lyngdoh**: *U Khasi Hyndai* (1938) — Exhaustive cultural, megalithic (*Mawbynna*), and social history.
- **U Mondon Bareh**: *Ka Drama U Mihsngi* (1929) & *Khasi-English Course and Grammar for Schools and Colleges* (1929).
- **Babu Jeebon Roy**: *Shaphang U Wai U Blai* (1900) — Treatise on prayers and worship.
- **U Rabon Singh**: *Ka Myntoi* (1924) — Philosophical prose and moral ethics.
- **Welsh Mission**: *Ka Kot Pule Ka Balai* (Khasi Third Reader, 1904).
- **Bevan L. Swer**: *Ka Meiramew Bad U Hynniewtrep* (1998) — Ecological and cosmological mythology.
- **Donbok T. Laloo**: *Ki Bor Phylla U Hynniewtrep* (1995) — Mysticism, sacred stones, and divination.
- **Dr. H.W. Sten**: *Ki Sur Na Ka Duitara Ksiar* (1981) — Comprehensive literary critique of Soso Tham.
- **Minette Sibon Tham**: *I Mabah Soso Tham* (1990) — Intimate biography of the national poet.
- **Hughlet Warjri**: *U Soso Tham Bad Ki Jingtrei Jong U* (1985) — Literary analysis of Tham's poetry.
- **L. Gilbert Shullai**: *Ka Ri Hynniewtrep Bad Ka Sixth Schedule* (1989) — Constitutional history and tribal governance.
- **S. Synrang Khonglah**: *Ka Niam Khasi Tynrai Ha Ka Dur Ka Niam Khristan* (1985) — Comparative religion.
- **Classical Heritage**: *Ka Thymmei Ki Parom Khasi*, *Ka Jymbriew Ki Khasi: Ki Kur bad Jait*, *Ka Jingshai Ka Ri Khasi*.

### APIs:
```python
import khasi

# 1. Inspect library summary
print(khasi.books.summary())
# {'total_books': 24, 'total_pages': 1987, 'total_words': 473168, ...}

# 2. List all available books
all_books = khasi.list_books()

# 3. Retrieve a specific whole book
book = khasi.get_book("ka_niam_ki_khasi")
print(book.title)        # "Ka Niam Ki Khasi: Ka Niam Tip-Blei Tip-Briew"
print(book.author)       # "U Sib Charan Roy"
print(book.total_pages)  # 64
print(book.chapters)     # List of chapter titles

# 4. Page-by-page reading
page_1 = book.get_page(1)
print(page_1)

# Or via facade
page_5 = khasi.books.read("ka_jingsneng_tymmen_part_1", 5)

# 5. Access full book text
full_text = book.full_text

# 6. In-book keyword search across all pages
hits = book.search("blei")
for hit in hits:
    print(f"Page {hit['page_number']}: {hit['snippet']}")

# 7. Cross-book universal search across all 24 books and all pages
universal_hits = khasi.search_books("hynniewtrep")
for hit in universal_hits:
    print(f"[{hit['title']} p.{hit['page_number']}]: {hit['snippet']}")
```

---

## 7. Master Bibliography Catalogue (`khasi.catalogue`)

Curated metadata database of **344 catalogued Khasi literary works, historical monographs, linguistic primers, and dictionaries** across 8 genres.

Methods:
- `khasi.catalogue.all()`: List of all 344 works.
- `khasi.catalogue.by_genre(genre)`: Filter by genre.
- `khasi.catalogue.by_author(author)`: Filter by author name.
- `khasi.catalogue.by_type(type)`: Filter by format/type.
- `khasi.catalogue.search(query)`: Search across title, author, genre, and type.
- `khasi.catalogue.digitized()`: Filter to works with digitized scans available.
- `khasi.catalogue.summary()`: Statistical summary of total works, genre distributions, and top authors.

---

## 7. Dedicated Dialect Sub-Lexicons (`khasi.dialects` / `khasi.lexicon.dialects`)

Provides dedicated sub-lexicons (over 13,000 entries across 4 key regional varieties):
- **Pnar / Synteng** (`pnar`): 5,500+ words (Jaiñtia Hills: Jowai, Shangpung, Khliehriat).
- **War Khasi** (`war`): 5,300+ words (Southern Slopes & Shella borderlands).
- **Bhoi Khasi** (`bhoi`): 1,250+ words (Ri-Bhoi District: Nongpoh, Umsning).
- **Maram Khasi** (`maram`): 1,250+ words (West Khasi Hills: Nongstoin, Mairang).

Methods:
- `khasi.dialects.list()`: Returns list of supported dialects (`['pnar', 'war', 'bhoi', 'maram', 'sohra', 'shillong']`).
- `khasi.dialects.info(dialect)`: Returns geographical, sociological, and linguistic shift metadata.
- `khasi.dialects.lookup(word, dialect)`: Looks up a word in a specific dialect or its Sohra standard equivalent.
- `khasi.dialects.translate(text, from_dialect='sohra', to_dialect='pnar')`: Full text translation across dialects with punctuation and case preservation.
- `khasi.dialects.cognates(word)`: Returns dictionary of cognate forms across all 5 dialects.
- `khasi.dialects.stats()`: Returns vocabulary counts and phonological shift counts.

---

## 8. Audio Waveform Dataset & Speech Pipeline (`khasi.audio_dataset` / `khasi.voice.dataset`)

Manages **252 native speech audio recordings** in standard **16,000 Hz, 16-bit Mono Linear PCM WAV** format for Automatic Speech Recognition (ASR) and Text-To-Speech (TTS) research:
- 187 Conversational Phrases (`phrase_001.wav` to `phrase_187.wav`).
- 65 Traditional Proverbs (`proverb_001.wav` to `proverb_065.wav`).
- Total audio duration: ~9.5 minutes.
- Balanced across native speakers (`SPK_KHA_F01` female, `SPK_KHA_M01` male).
- Standard split: 204 train (80%), 24 validation (10%), 24 test (10%).

Methods:
- `len(khasi.audio_dataset)`: Total recordings (252).
- `khasi.audio_dataset.get_records(split=None)`: List of manifest records.
- `khasi.audio_dataset.get_item(audio_id)`: Lookup metadata record by ID (`phrase_001`, `proverb_015`).
- `khasi.audio_dataset.get_audio_path(audio_id)`: Returns absolute path to WAV file.
- `khasi.audio_dataset.get_audio_bytes(audio_id)`: Reads and returns raw PCM WAV bytes.
- `khasi.audio_dataset.search_audio(query)`: Search recordings by text, meaning, or category.
- `khasi.audio_dataset.verify_integrity()`: Verifies that all 252 audio files physically exist and conform to 16kHz mono WAV format.
- `khasi.audio_dataset.export_huggingface_format(path)`: Exports dataset to Hugging Face Audio JSONL format.
- `khasi.audio_dataset.export_common_voice_tsv(path)`: Exports dataset to Mozilla Common Voice TSV format.

---

## 9. Aligned Parallel Corpora & MT Evaluation (`khasi.parallel_corpus` / `khasi.corpus`)

Sentence-by-sentence parallel alignment between Khasi and English across public domain masterworks:
1. *Ka Niam Jong Ki Khasi* (U Sib Charan Roy, 1919) — Indigenous theology, ethics, sacred groves, and covenant philosophy (49 aligned pairs).
2. *Ka Jingiaid U Pilgrim* (*The Pilgrim's Progress* in Khasi, John Bunyan / Thomas Jones / Dr. John Roberts / Mondon Bareh) — Foundational literary prose (47 aligned pairs).
3. *Ki Dienjat Jong Ki Longshwa & Kot Pule* — Classic folklore (*Lum Diengiei*, *Lum Sohpetbneng*, *Manik Raitong*, *U Thlen*, *Ka Sngi bad u Bnai*) (25 aligned pairs).

Methods:
- `len(khasi.parallel_corpus)`: Total sentence pairs (121).
- `khasi.parallel_corpus.get_records(source=None, split=None, domain=None)`: Filtered parallel records.
- `khasi.parallel_corpus.get_pairs(source=None, split=None)`: Returns raw `(khasi_text, english_text)` tuples.
- `khasi.parallel_corpus.search(query)`: Searches across Khasi and English parallel sentences.
- `khasi.parallel_corpus.get_stats()`: Source breakdown, word counts, and average sentence lengths.
- `khasi.parallel_corpus.export_bitext(khasi_path, english_path, split=None)`: Exports aligned plain-text bitext (`.kha` and `.en`).
- `khasi.parallel_corpus.export_tmx(output_path)`: Exports to Translation Memory eXchange (TMX 1.4b XML).
- `khasi.parallel_corpus.export_huggingface_format(output_path)`: Exports to Hugging Face MT dataset format.
- `ParallelCorpus.compute_bleu(hypotheses, references, max_order=4)`: Standalone BLEU score evaluation toolkit (1-gram through 4-gram precision with brevity penalty).

---

## 10. Rituals, Deities & Sacred Sites (`khasi.rituals`, `khasi.deities`, `khasi.sacred_sites`)

Documented from authentic ethnographical records, customary court rolls, and native treatises:

### Traditional Rituals (`khasi.rituals`)
- `khasi.rituals.all()`: List of 10+ documented traditional rituals.
- `khasi.rituals.get(name)`: Lookup ritual by Khasi name, English name, or ID.
- `khasi.rituals.by_category(category)`: Filter by category (`divination`, `sacrifice`, `funerary`, `rite_of_passage`, `marriage`, `purification`).
- Key rites covered:
  - *Ka Shat Pylleng* (Egg Divination on consecrated board)
  - *Ka Khan Pyrthat* (Thunder & celestial omen interpretation)
  - *U Syiar Ryngkew* (Cock mediator sacrifice)
  - *Ka Pomblang Nongkrem* (Royal goat sacrifice)
  - *Ka Thep Mawbah* (Clan bone internment in central megalith)
  - *Ka Jer Ka Thoh* (Infant naming dedication)
  - *Ka Shongkurim* (Matrilocal marriage covenant)
  - *Ka Tangsnoing* (Clan genealogical invocation)
  - *Ka Pyllait Thlen* (Curse cleansing & destruction of evil wealth)

### Indigenous Pantheon & Deities (`khasi.deities`)
- `khasi.deities.all()`: List of 11+ documented deities and spirit guardians.
- `khasi.deities.get(name)`: Lookup deity by name or title.
- `khasi.deities.by_realm(realm)`: Filter by spiritual realm (`celestial_supreme`, `terrestrial_nature`, `mountain_sovereign`, `ancestral_matrilineal`, `river_water`, etc.).
- Divine entities covered:
  - *U Blei Nongbuh Nongthaw* (Supreme Transcendent Creator)
  - *Ka Meiramew* (Mother Earth / Nurturing Primal Goddess)
  - *U Lei Shyllong* (Paramount Mountain Lord of Shillong Peak)
  - *U Suidnia* (Primal Maternal Uncle & Divine Intercessor)
  - *Ka Iawbei* (Primal Ancestral Mother of the Clan)
  - *U Thawlang* (Primal Father of the Lineage)
  - *U Ryngkew U Basa (Labasa)* (Territorial Guardian Spirits of Groves)
  - *U Leisymper* (Guardian Deity of Symper Rock)
  - *Ka Kupli* (Sovereign Goddess of the Kopili River)
  - *U Lei Longspah* (Deity of Righteous Wealth)
  - *U Blai Synteng* (Supreme Divine Presence of Jaintia)

### Sacred Megaliths, Shrines & Groves (`khasi.sacred_sites`)
- `khasi.sacred_sites.all()`: List of documented sacred sites and megaliths.
- `khasi.sacred_sites.get(name)`: Lookup by site name or location.
- `khasi.sacred_sites.by_type(site_type)`: Filter by type (`sacred_grove`, `megalithic_monolith`, `mountain_sanctuary`, etc.).
- Sacred locations covered:
  - *Law Kyntang Mawphlang* (800-year-old virgin forest, residence of Labasa)
  - *Ki Mawbynna Nartiang* (Largest megalithic cluster in the world, 8.3m menhir)
  - *Lum Shillong* (Throne of U Lei Shyllong, highest peak of Khasi Hills)
  - *Lum Sohpetbneng* (Navel of Heaven, cradle of the Seven Huts)
  - *Ka Aitnar* (Sacred pool in Jowai for Behdeiñkhlam mud dance)
  - *Krem Mawmluh* (Sacred cave sanctuary of subterranean springs)
  - *Lum Kyllang* (Colossal 300m single granite dome)

---

## 10. Khasi Oral Folklore, Myths & Legends (`khasi.folklore`)

Provides structured access to 12 foundational Khasi oral myths, legends, fables, and cultural allegories (6,950+ words of authentic Khasi prose and poetry) with section narratives, character registries, moral tenets, and English translations.

```python
import khasi.folklore as kf

# Statistical summary
print(kf.folklore.summary())

# Retrieve story
story = kf.get_story("ka_jingkieng_ksier")
print(story.title)               # The Golden Ladder & Genesis of the Seven Huts
print(story.khasi_title)         # Ka Jingkieng Ksier bad Ki Hynñiew Trep
print(story.geographic_origin)   # Lum Sohpetbneng (Ri-Bhoi)
print(story.characters)          # ['Ki Hynñiew Trep', 'Ki Khyndai Trep', 'U Blei Nongbuh']
print(story.cultural_moral)      # Sacred duty to earn righteousness through labor (Kamai ïa ka Hok)
print(story.khasi_text)          # Full Khasi text
print(story.english_translation) # Full English translation

# Access narrative sections
for sec in story.sections:
    print(sec["title"], len(sec["khasi"]))

# Universal search across all stories
results = kf.search_folklore("u thlen")

# Stories by category
creation_tales = kf.stories_by_category("Creation Myth")
```

---

## 11. Traditional Songs, Ballads & Phawar (`khasi.songs`)

Provides direct access to **161 structured Khasi folk songs, chants, archery phawars, sacred hymns** (including published songs from *Ki Sur Jingrwai U Hynniew Trep*, *Ka Phawar Ksan Rngiew*, *Ri Khasi, Ri Khasi*, and *Mynsiem Bakhuid, Ko Blei Nongbuh Nongthaw*), across 46 cultural categories with full Khasi lyrics, English stanza translations, instruments, and glossaries.

```python
import khasi.songs as ks

# Statistical summary
print(ks.songs.summary())
# {'total_songs': 161, 'categories_count': 46, 'total_words': 11890}

# Retrieve song
lapalang = ks.get_song("ka_sur_u_sier_lapalang")
print(lapalang.title)           # The Lament of the Stag
print(lapalang.khasi_title)     # Ka Sur U Sier Lapalang
print(lapalang.category)        # Folk Elegy & Ancestral Lament (Jamlu)
print(lapalang.instruments)     # ['Maryngod (bowed fiddle)', 'Shyngwiang', 'Duitara']
print(lapalang.lyrics_khasi)    # Complete Khasi song verses
print(lapalang.lyrics_english)  # English poetic translation

# Access stanzas
for stanza in lapalang.stanzas:
    print(f"Stanza {stanza['stanza_number']}: {stanza['title']}")
    print(stanza["khasi"])
    print(stanza["english"])

# Search songs and chants
results = ks.search_songs("duitara")

# Filter by category
archery_songs = ks.songs_by_category("Archery")
```

---

## 12. Whole-Books Reader & Classical Literature (`khasi.books`)

Provides structured, digitized, whole-book reading, page navigation, and universal search across **119 foundational Khasi classical books** (**3,777 pages** and **1,081,284 words**), spanning history, statecraft, theology, customary law, early readers by Babu Jeebon Roy, epic poetry by U Soso Tham, dramas by Victor Bareh, Father H. Elias's legends, and dictionaries by U Nissor Singh.

```python
import khasi.books as kb

# 1. Collection summary
summary = kb.books.summary()
print(f"Total Books: {summary['total_books']}")   # 119
print(f"Total Pages: {summary['total_pages']}")   # 3,777
print(f"Total Words: {summary['total_words']}")   # 1,081,284

# 2. Retrieve a specific masterwork
book = kb.get_book("ka_niam_ki_khasi")
print(book.title)           # Ka Niam Jong Ki Khasi (U Sib Charan Roy)
print(book.author)          # U Sib Charan Roy
print(book.total_pages)     # Pages in digital reader
print(book.chapters)        # Chapter outline

# 3. Read page-by-page
page_1 = book.get_page(1)
print(page_1[:200])

# 4. In-book keyword search
hits = book.search("Hok")
for h in hits:
    print(f"Page {h['page_number']}: {h['snippet']}")

# 5. Universal cross-book search across all 100 books
all_hits = kb.search_books("ri kynti", max_results_per_book=1)
print(f"Found matches across {len(all_hits)} books")
```

---

## 13. Traditional Attire, Handloom, Jewellery & Regalia (`khasi.clothing`, `khasi.jewellery`, `khasi.fabrics`, `khasi.regalia`, `khasi.attire`)

Comprehensive ethnographical coverage of indigenous garments, sacred peace-silks, matrilineal heirloom ornaments, and warrior regalia:

### Traditional Garments (`khasi.clothing` / `khasi.culture.attire`)
- **Ka Jaiñsem**: Signature two-piece draped silk or cotton garment pinned across opposite shoulders.
- **Ka Dhara (Jaiñsem Dhara)**: Heavy raw brocade mulberry silk worn during *Shad Suk Mynsiem*, *Shad Nongkrem*, and royal weddings.
- **Ka Jaiñkup**: Warm cashmere/woolen mantle-shawl draped over the shoulders by matriarchs and elders.
- **Ka Kyrshah**: Diagonal checkered working wrap fastened on one shoulder during domestic and hearth labor.
- **Ka Tapmohkhlieh**: Rectangular headscarf wrapped snugly around the head and chin for highland warmth.
- **Ka Jaiñpien**: Lower inner wraparound skirt serving as the foundation under outer silk garments.
- **U Jymphong**: Sleeveless long male tunic open down the front and fastened with silver cords or frogged buttons.
- **U Spong (Jaiñspong)**: Prestigious silk turban wrapped with spiral folds and fan crest for kings, priests, and elders.
- **Ka Jaiñboit / Ka Dhoti Khasi**: Unstitched pleated silk lower wrapper tied at the waist for agility in martial dance.

### Sacred Textiles & Indigenous Handloom (`khasi.fabrics`)
- **Ka Ryndia (Eri Peace-Silk)**: Non-violent, organic peace silk of Ri Bhoi (*Samia ricini*) hand-dyed with lac, turmeric, and walnut bark; naturally thermal and hypoallergenic.
- **Ka Jaiñ Thoh Khyrwang**: Traditional geometric handloom weave in bold black, crimson, and ivory from Jaintia Hills.
- **Ka Jaiñsem Muga**: Lustrous golden Assam-Meghalaya silk worn by queens and high-clan brides.
- **Ka Jaiñ Sulan**: Coarse handspun cotton blanket used by mountain travelers and forest porters.

### Heirloom Jewellery & Ornaments (`khasi.jewellery`)
- **Ka Pansngiat**: Golden/silver maiden crown with vertical plume (*tiew lasubon*) worn by unmarried maidens in sacred dances.
- **Ka Paila (Paila Mukmor)**: Treasured matrilineal heirloom necklace of large red coral beads alternating with hollow 24k gold spheres.
- **U Kynjri Ksiar / U Kynjri Rupa**: Multi-strand gold chains and silver warrior pectoral cords.
- **U Shanryndang**: Intricate filigree gold choker necklace clasping the throat.
- **Ki Siar Kynthei / Ki Khadu**: Massive solid gold or silver forearm cuffs worn in pairs by dancers.
- **Ki Mahu**: Warrior silver armlets worn tightly around the biceps above the elbows.
- **Ka Ta-kora**: Embossed circular silver pectoral medallion suspended across the chest.
- **Ki Sa-shiah / Thiah-shiah**: Handcrafted gold ornamental pins and brooches.
- **Ki Siatsngi**: Golden sunburst chandelier earrings honoring *Ka Sngi* (the Sun Mother).

### Martial Dance Regalia & Sacred Arms (`khasi.regalia`)
- **Ka Waitlam**: Two-handed straight ceremonial steel broadsword wielded aloft in *Shad Mastieh*.
- **Ka Stieh**: Embossed circular brass or silver shield warding off physical and spiritual adversaries.
- **U Symphiah**: Sacred white yak-tail or goat-hair whisk waved by dancers to cleanse the sacred dancing ring (*Lympung*).
- **Ka Ryntieh bad Ki Khnam**: Mountain bamboo recurve bow and iron-tipped arrows representing defense and sovereignty.
- **Ka Wait-bnoh**: Hooked billhook chopper knife for rainforest trails and woodsman utility.
- **Ka Pah-wait**: Ornamental chased silver scabbard and baldric.

```python
import khasi

# 1. Garments lookup and gender filtering
female_garments = khasi.clothing.by_gender("female")
dhara = khasi.clothing.get("dhara")
print(dhara["name"])          # Ka Dhara (Jaiñsem Dhara)
print(dhara["materials"])     # ['Heavy raw mulberry silk', 'Gold thread brocade']

# 2. Sacred fabrics
ryndia = khasi.fabrics.get("ryndia")
print(ryndia["origin_region"])  # Ri Bhoi (Umden, Nongpoh, Saiden)
print(ryndia["properties"])     # Thermal insulation, non-violent peace silk...

# 3. Heirloom jewellery
paila = khasi.jewellery.get("paila")
print(paila["cultural_significance"]) # Heirloom passed to Ka Khadduh

# 4. Dance regalia
waitlam = khasi.regalia.get("waitlam")
print(waitlam["occasions"])    # ['Shad Mastieh', 'Shad Suk Mynsiem', 'Funeral of royal chieftains']
```

---

## 14. Traditional Rituals, Divination & Customs (`khasi.rituals`)

Documents **15 authentic Khasi and Pnar religious rituals, ceremonies, and sacrifices** derived from classical treatises (*Ka Niam Jong Ki Khasi*, *Ka Riti Jong Ka Ri Khasi*):

| Ritual ID | Khasi Name | English Name | Category | Primary Occasion |
|---|---|---|---|---|
| `shat_pylleng` | Ka Shat Pylleng | Egg Divination Rite | Divination | Sickness, foundation of house, choosing elders |
| `syiar_ryngkew` | U Syiar Ryngkew | Sacrifice of the Cock Mediator | Sacrifice | Annual state rites, hearth purification |
| `thep_mawbah` | Ka Thep Mawbah | Clan Megalithic Bone Internment | Funerary | Periodic internment in ancestral cairn |
| `jer_thoh` | Ka Jer Ka Thoh | Naming & Dedication Ceremony | Rite of Passage | Infant birth (bow/arrows for boy, basket for girl) |
| `shongkurim_niam` | Ka Shongkurim Katkum Ka Niam Tynrai | Customary Matrimonial Covenant | Marriage | Matrilocal clan alliance |
| `behdeinkhlam_tapmohkhlieh` | Ka Tap-Mohkhlieh bad Ka Shad Behdeinkhlam | Pestilence-Chasing & Pool Dancing | Communal / Agricultural | Mid-summer harvest festival in Jowai |
| `knia_mawbynna` | Ka Kñia Mawbynna | Megalith Erection & Consecration | Memorial | Erecting menhirs (Maw-shynrang) & dolmens |
| `knia_pyrda_kmie` | Ka Kñia Pyrda / Ka Kñia Kmie | Maternal Hearth Ancestral Sacrifice | Ancestral | Propitiating Ka Iawbei at family hearth |
| `pyniasoh_kpoh` | Ka Pyniasoh Kpoh | Clan Adoption & Lineage Grafting | Kinship | Averting extinction (Iapduh) |
| `khan_pylleng_jingpang` | Ka Khan-Pylleng ha Ka Jingpang | Diagnostic Healing Divination | Healing | Mysterious illnesses and spiritual cleansing |
| `pomblang_nongkrem` | Ka Pomblang Nongkrem | Royal Goat Decapitation Rite | Sacrifice | Autumn state festival at Smit |
| `knia_shnong` | Ka Kñia Shnong | Village Sanctification Sacrifice | Agricultural | Village boundary sanctification |
| `tangsnoing` | Ka Tangsnoing | Ancestral Lineage Recitation | Genealogy | Clan continuity before megalith rites |
| `pyllait_thlen` | Ka Pyllait Thlen | Severing of the Thlen Curse | Purification | Casting out serpent curse and destroying tainted wealth |
| `khan_pyrthat` | Ka Khan Pyrthat | Celestial Thunder Divination | Divination | Severe unseasonal storms and divine warnings |

```python
import khasi

# List all rituals
all_rituals = khasi.rituals.all()
print(f"Total rituals: {len(all_rituals)}")  # 15

# Query specific ritual
behdein = khasi.rituals.get("behdeinkhlam")
print(behdein["english_name"])  # Pnar Sanctification & Pestilence-Chasing Rite
print(behdein["materials"])     # ['Deinkhlam (Sacred poles)', 'Rots...', 'Ka Aitnar...']

# Filter by category
divinations = khasi.rituals.by_category("divination")
```

---

## 15. Original Words: Austroasiatic Roots (Ki Ktien Tynrai) & Phonaesthetics (`khasi.roots`, `khasi.expressives`, `khasi.tynrai`)

Khasi represents an ancient Austroasiatic (Mon-Khmer) linguistic island in the hills of Meghalaya. The `tynrai` subsystem provides deep etymological access to original native roots, derivational base families, and world-renowned phonaesthetic ideophones:

### Indigenous Roots (`khasi.roots` / `khasi.lexicon.tynrai`)
- **Anatomy & Senses**: *khmat* (eye, Mon *mat*, Viet *mắt*), *shkor* (ear), *khmut* (nose), *ktien* (mouth/speech), *shyntur* (lips), *bniat* (teeth), *thylliej* (tongue), *kti* (hand/arm, Mon *tai*, Khmer *dai*), *kjat* (foot/leg), *doh* (flesh), *snam* (blood, Mon *chim*, Khmer *chheam*), *shyieng* (bone), *kpoh* (womb/matrilineal branch), *klong-sngi* (heart).
- **Cosmos & Primal Elements**: *ka sngi* (sun/day, Mon *tŋi*), *u bnai* (moon/month, Mon *gnoa*), *u khlur* (star), *ka bneng* (sky/heaven), *ka khyndew* (earth/soil), *ka um* (water, Mon *dàik*, Khmer *tœk*), *ka ding* (fire), *ka lyer* (wind/air), *u lum* (mountain), *ka wah* (river), *ka thwei* (deep water pool), *ka dpei* (hearth fire altar), *u lapbah* (monsoon torrent).
- **Moral Philosophy & Customs**: *ka hok* (righteousness/truth), *ka sot* (integrity/purity), *ka niam* (sacred faith), *ka riti* (unwritten customary law), *ka sang* (moral taboo/incest), *ka ma* (spiritual peril), *ka rngiew* (spiritual aura/divine charisma), *ka burom* (honor/respect), *kamai ia ka hok* (earn righteousness).
- **Primal Action Verbs**: *im* (to live), *ïap* (to die), *tip* (to know), *trei* (to work), *shong* (to sit/dwell -> *shnong* village), *kren* (to speak), *ieid* (to love), *bam* (to eat), *dih* (to drink), *thiah* (to sleep).

### Phonaesthetic Expressives & Ideophones (`khasi.expressives` / `khasi.ideophones`)
A celebrated defining characteristic of Khasi is its rich palette of ideophonic expressives (*Ki Ktien Pynshai Dur*):
- **Light & Radiance**: *lieh phyrnai* (dazzling shimmering white), *lieh pup* (chalky pale white), *iong thiej* (deep pitch black), *saw hynñiang* (crimson blood-red), *stem mluh* (bright saffron yellow), *jyrngam duk* (deep verdant green), *shai kdar* (crystal clear light), *dum kput* (pitch dark).
- **Temperature & Tactile**: *khluit thar* (scalding burning hot), *syaid lumbor* (soothing gentle warmth), *khriat jur-jur* (shivering biting cold), *pjah thait* (ice cold), *eh tian* (rock-hard unyielding), *jem pudep* (cloud-soft/cushioned), *stang rynghang* (whisper thin), *rben khap-khap* (densely thick).
- **Gait & Movement**: *iaid wiar-wiar* (walking with slow maternal grace), *iaid thwiat-thwiat* (walking with brisk energetic strides), *phet kyrthep* (stampeding in terror), *khih phet-phet* (trembling rapidly), *thiah lyng-ngai* (sleeping in sweet serene peace).
- **Acoustics & Voice**: *sawa kdup-kdup* (deep rhythmic drum pounding), *phuh mut-mut* (beaming with serene quiet joy), *khmih pyrkhing* (gazing sternly with unblinking scrutiny).

```python
import khasi

# 1. Access Austroasiatic roots
eye = khasi.roots.get("khmat")
print(eye["austroasiatic_family"])  # Mon 'mat', Khmer 'phnek/mat', Vietnamese 'mắt'
print(eye["derived_forms"])         # ['peit khmat', 'khmat-sngi', 'mar-khmat']

# 2. Filter roots by category
anatomy = khasi.roots.by_category("anatomy")
print(f"Anatomical roots: {len(anatomy)}")

# 3. Explore phonaesthetic expressives
warmth = khasi.expressives.get("syaid lumbor")
print(warmth["english"])        # pleasantly, soothingly warm and comfortable
print(warmth["usage_example"])  # Ka dpei kaba syaid lumbor ha tlang...

# 4. Search across all original roots and expressives
results = khasi.tynrai.search("white")
for r in results:
    print(r.get("root") or r.get("expressive"), "->", r["english"])
```

---

## 16. Speech Audio Waveforms & Spoken Corpus (`khasi.audio_dataset`)

Provides **500 studio-grade spoken Khasi audio recordings** in standard **16,000 Hz, 16-bit Mono Linear PCM WAV** format with paired transcriptions, English/Hindi translations, speaker metadata (male & female native speakers), and direct export formats for Hugging Face Audio Datasets and Mozilla Common Voice.

```python
import khasi

# 1. Access the audio dataset
ds = khasi.audio_dataset
print(f"Total Spoken Recordings: {len(ds)}")   # 500

# 2. Dataset statistics
stats = ds.get_stats()
print(f"Sample Rate: {stats['sample_rate_hz']} Hz")
print(f"Format: {stats['format']}")
print(f"Total Duration: {stats['total_duration_minutes']} minutes")

# 3. Integrity verification
integrity = ds.verify_integrity()
print(f"All Files Valid & Healthy: {integrity['all_healthy']}")  # True

# 4. Retrieve recording by ID and read PCM bytes
item = ds.get_item("phrase_001")
print(item["khasi_text"])            # "Khublei!"
print(item["english_translation"])   # "Hello / Thank you / Greetings"
wav_bytes = ds.get_audio_bytes("phrase_001")
print(f"WAV File Size: {len(wav_bytes)} bytes")

# 5. Export dataset for ASR / TTS fine-tuning
ds.export_huggingface_format("khasi_asr_dataset.jsonl")
ds.export_common_voice_tsv("common_voice_khasi.tsv")
```

---

## 17. Matrilineal Clans, Surnames & Traditional Given Names (`khasi.clans`, `khasi.list_names`)

Comprehensive anthropological registry of over **105 matrilineal Khasi, Pnar, War, Bhoi, and Maram clans (*Ki Kur & Ki Jaid*)** and **52 traditional given names (*Ki Kyrteng Tynrai*)** with meanings, gender associations, and cultural naming rituals.

```python
import khasi

# 1. Clans lookup and search
total_clans = khasi.total_clans()
print(f"Catalogued Clans: {total_clans}")  # 105+

syiem_clan = khasi.get_clan("Syiem")
print(syiem_clan["category"])        # Royal / Ruling Clan
print(syiem_clan["branches"])        # ['Syiemlieh', 'Syiemiong', 'Nongkhlaw', ...]

# 2. Traditional Given Names
total_names = khasi.total_names()
print(f"Traditional Names: {total_names}")  # 52

# Lookup by name
kynpham = khasi.get_name("kynpham")
print(kynpham["meaning"])            # Remembrance / Counsel / Memory of the heart
print(kynpham["gender"])             # male

# Filter names by gender
girls_names = khasi.list_names(gender="female")
for g in girls_names[:5]:
    print(f"{g['name']}: {g['meaning']}")

# Search names by virtue or theme
peace_names = khasi.search_names("peace")
for p in peace_names:
    print(f"{p['name']} ({p['gender']}): {p['meaning']}")
```

---

## 18. Ethnobotany & Wildlife Zoology (`khasi.plants`, `khasi.wildlife`)

Complete scientific and indigenous encyclopedia of **85+ flora species** (trees, medicinal herbs, sacred grove trees, wild mountain fruits, orchids, bamboos, canes, and edible mushrooms) and **65+ fauna species** (mammals, birds, reptiles, amphibians, fish, and insects) of Meghalaya.

```python
import khasi

# 1. Indigenous Botany & Wild Fruits
total_plants = khasi.total_plants()
print(f"Total Catalogued Plants: {total_plants}")  # 85+

pitcher = khasi.get_plant("Nepenthes khasiana")
print(pitcher["khasi_name"])      # Tiew-rakot / Kynbat-khlieng
print(pitcher["cultural_use"])    # Traditional medicinal eye ailments & sacred taboo

# Filter medicinal herbs
meds = khasi.medicinal_plants()
print(f"Medicinal Plants: {len(meds)}")

# 2. Highland Wildlife & Fauna
total_wildlife = khasi.total_wildlife()
print(f"Total Fauna Species: {total_wildlife}")    # 65+

clouded = khasi.get_animal("khla-lyngngoh")
print(clouded["common_name"])     # Clouded Leopard
print(clouded["scientific_name"]) # Neofelis nebulosa
print(clouded["status"])          # State Animal of Meghalaya

# Filter by zoological class
birds = khasi.by_wildlife_class("bird")
print(f"Documented Bird Species: {len(birds)}")
```

---

## 19. Parallel Corpus & MT Toolkit (`khasi.parallel_corpus` / `khasi.corpus`)

Sentence-aligned parallel dataset and machine translation benchmarking suite for Khasi language computational linguistics:

```python
import khasi
from khasi import parallel_corpus, ParallelCorpus

# 1. Corpus Statistics
stats = parallel_corpus.get_stats()
print(f"Total Sentences: {stats['total_records']:,}")
print(f"Sources Represented: {stats['sources']}")

# 2. Retrieve Parallel Sentence Pairs
pairs = parallel_corpus.get_pairs()
for kh, en in pairs[:3]:
    print(f"Khasi:   {kh}")
    print(f"English: {en}\n")

# 3. Filter by Source Book or Book ID
book_sents = parallel_corpus.get_records(source="Pilgrim")
for s in book_sents[:2]:
    print(f"{s['khasi']} -> {s['english']}")

# 4. Search Parallel Corpus
matches = parallel_corpus.search("Hok")

# 5. Export for Hugging Face or Bitext Training
parallel_corpus.export_huggingface_format("hf_parallel.jsonl")
parallel_corpus.export_bitext("train.kha", "train.en")

# 6. Evaluate Machine Translation BLEU Scores
hypotheses = ["U briew u leit sha ïing"]
references = ["U briew u leit sha ïing"]
bleu = ParallelCorpus.compute_bleu(hypotheses, references)
print(f"BLEU: {bleu['bleu']}")  # 100.0
```

---

## 20. Classical Khasi Grammar Rules Engine (`khasi.grammar_rules`)

The `khasi.grammar_rules` engine formalizes **100 authoritative classical Khasi grammar rules** derived directly from historical foundational grammars and treatises (*Rev. H. Roberts 1891*, *Rev. Thomas Jones 1841*, *Rev. W. Pryse 1855*, *Dr. G. A. Grierson 1903*, *Babu Jeebon Roy 1897*, *Dr. R. S. Lyngdoh 1983*):

### Distribution Across 9 Grammatical Categories:
1. **Nominal Agreement (`AGR`)**: 9 formal rules (Article Prefixation, Gender Harmony, Pronominal Copy Agreement, Kinship Honorific Plural, Diminutive Reverence).
2. **Tense-Aspect-Mood (`TAM`)**: 25 formal rules (Habitual, Definite Future, Perfective Consecutive 'Sa', Optative 'To', Apprehensive 'Ioh', Concomitant 'Nangta').
3. **Case Marking (`CAS`)**: 11 formal rules (Differential Object Marking with 'ïa', Dative-Benefactive, Locative, Synteng Allative 'che'/'cha', Postpositional 'ha-khet').
4. **Derivational Morphology (`DER`)**: 13 formal rules (Causative 'pyn-', Nominalizer 'jing-', Agentive 'nong-', Privative 'bym-', Reciprocal-Causative 'ïa-pyn-').
5. **Complex Syntax (`CLA`)**: 12 formal rules (Subordinate Clause Order, Comparative 'kham... ban ïa', Concessive 'La bha ba... pynban', Temporal Inversion).
6. **Enclitics & Expressives (`EXP`)**: 12 formal rules (Echo Reduplication, Coupled Rhyme, Attenuative Reduplication 'stem-stem', Ideophonic Motion).
7. **Numeral Classifiers (`NUM`) / (`CLS`)**: 8 formal rules (Personal 'ngut', Inanimate 'tylli', Arboreal 'tynrai', Foliar 'sla', Sheaf 'rynjup').
8. **Discourse Particles (`DIS`)**: 6 formal rules (Hortative 'To'/'Seh', Confirmation Tag 'Mo', Reportative 'Da Ong', Focus Enclitic 'Te', Assertive 'Re').
9. **Phonotactics & Morpho-Phonology (`PHO`)**: 4 formal rules (Glottal Stop '/ʔ/', Minor Syllables, Vowel Contrast 'I' vs 'Ï', Glide Epenthesis, Coda Gemination).

### Example Python Usage:

```python
import khasi

# 1. Inspect engine summary
summary = khasi.grammar_rules.summary()
print(f"Total Rules: {summary['total_rules']}")         # 100
print(f"Categories: {summary['categories_count']}")     # 9

# 2. Retrieve a specific rule by ID
rule = khasi.grammar_rules.get("TAM-24")
print(rule.name)          # Historical Optative-Precative with Archaic 'Ioh' and 'Khein'
print(rule.formula)       # [Ioh ba / Khein ba] + [Subject] + [Verb Phrase]
print(rule.khasi_examples) # ['Ioh ba U Blei un isynei', 'Khein ba ngin ioh ka jingsuk']

# 3. Filter rules by category
tam_rules = khasi.grammar_rules.by_category("Tense-Aspect-Mood")
print(f"TAM Rules: {len(tam_rules)}")  # 25

# 4. Search rules by keyword
classifier_rules = khasi.grammar_rules.search("classifier")
for r in classifier_rules:
    print(f"[{r.id}] {r.name}: {r.formula}")
```


