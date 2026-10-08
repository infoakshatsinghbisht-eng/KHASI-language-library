# Khasi Language Library (Ka Ktien Khasi) — Complete API Documentation

Comprehensive technical documentation for the `khasi` Python library (version 1.5.0).

---

## 1. Top-Level Facade (`import khasi`)

The root `khasi` package provides direct, high-level access to the most common operations:

### Core Functions

| Function | Signature | Description |
|---|---|---|
| `translate()` | `translate(text, source='auto', target='khasi', dialect='sohra')` | Translates English, Hindi, or Hinglish into Khasi with dialect adaptation. |
| `lookup()` | `lookup(word: str)` | Looks up a word in the 105,000+ trilingual dictionary with prefix stripping fallback. |
| `search()` | `search(query: str)` | Searches for matching words across Khasi, English, and Hindi. |
| `analyze()` | `analyze(word: str)` | Decomposes a word morphologically (lemma, POS, prefixes). |
| `total_word_forms()` | `total_word_forms() -> int` | Returns total combinatorial forms represented (300,000+). |
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

- `khasi.phrases.all()` / `khasi.phrases.random()` : 185+ practical conversational phrases across 15 categories (greetings, dining, travel, hospital, police, school, office, tech, etc.).
- `khasi.proverbs.all()` / `khasi.proverbs.random()` : 65+ authentic moral proverbs (*Ki Ktien Tymmen* / *Phawar*) with literal and contextual translations.
- `khasi.riddles.all()` / `khasi.riddles.random()` : 32+ traditional Khasi riddles (*Ki Jingkyntip*) with solutions and cultural hints.
- `khasi.instruments.all()` / `khasi.instruments.get(name)` : Traditional musical instruments (*Duitara*, *Tangmuri*, *Ksing*, *Nakra*, *Maryngod*, *Mieng*, *Besli*, etc.).
- `khasi.songs.all()` / `khasi.songs.get(title)` : Traditional folk songs, chants, ballads, and lullabies complete with authentic Khasi lyrics and English translations.
- `khasi.rituals.all()` / `khasi.rituals.get(name)` / `khasi.rituals.by_category(c)` : Traditional rituals, egg divination (*Ka Shat Pylleng*), sacrifices, and ceremonies.
- `khasi.deities.all()` / `khasi.deities.get(name)` / `khasi.deities.by_realm(r)` : Indigenous Khasi pantheon, territorial protectors, mountain rulers, and spirits.
- `khasi.sacred_sites.all()` / `khasi.sacred_sites.get(name)` / `khasi.sacred_sites.by_type(t)` : Sacred groves (*Law Kyntang*), prehistoric megalith complexes (*Mawbynna*), and altars.
- `khasi.plants.all()` / `khasi.plants.get(query)` / `khasi.plants.medicinal()` : Ethnomedicinal flora, wild fruits, trees, and orchids with binomial scientific names.
- `khasi.wildlife.all()` / `khasi.wildlife.get(query)` : Native mammals, birds, fish, reptiles, and insects with scientific names and folklore context.
- `khasi.dishes.all()` / `khasi.dishes.get(name)` : Traditional culinary heritage (*Jadoh*, *Dohkhlieh*, *Dohneiiong*, *Tungrymbai*, *Ja Stem*, *Pumaloi*, *Pukhlein*, *Khiew Ranei*).
- `khasi.places.all()` / `khasi.places.get(name)` : Sacred geographical sites, rivers (*Wah*), waterfalls (*Kshaid*), peaks (*Lum*), caves (*Krem*), sacred groves (*Law Kyntang*), root bridges (*Jingkieng Jri*), and Syiemships (*Hima*).
- `khasi.clans.all()` / `khasi.clans.get(name)` / `khasi.clans.search(query)` : Recognized Khasi and Pnar clans (*Kur* and *Jaid*), branches, and historical offices.
- `khasi.idioms.all()` / `khasi.idioms.get(query)` : Coupled rhyming idioms (*Ki Ktien Kynnoh*) and parables (*Ki Pharshi*).

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

Provides direct access to 10 structured Khasi folk songs, chants, archery phawar, and literary song cycles (including H.W. Sten's celebrated 1979 classic *Ki Sur Na Ka Duitara Ksiar*).

```python
import khasi.songs as ks

# Statistical summary
print(ks.songs.summary())

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

