# Khasi Language Library (Ka Ktien Khasi) — Complete API Documentation

Comprehensive technical documentation for the `khasi` Python library (version 1.0.0).

---

## 1. Top-Level Facade (`import khasi`)

The root `khasi` package provides direct, high-level access to the most common operations:

### Functions

| Function | Signature | Description |
|---|---|---|
| `translate()` | `translate(text, source='auto', target='khasi', dialect='sohra')` | Translates English, Hindi, or Hinglish into Khasi with dialect adaptation. |
| `lookup()` | `lookup(word: str)` | Looks up a word in the trilingual dictionary with prefix stripping fallback. |
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
| `list_festivals()` | `list_festivals() -> List[Dict[str, Any]]` | Returns documented traditional Khasi festivals. |

### Facade Objects

- `khasi.proverbs.all()` / `khasi.proverbs.random()` : Access traditional proverbs (*Ki Ktien Tymmen* / *Phawar*).
- `khasi.phrases.all()` / `khasi.phrases.random()` : Conversational daily phrases.
- `khasi.riddles.all()` / `khasi.riddles.random()` : Traditional Khasi riddles (*Ki Jingkyntip*).

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
  - `i`  : Diminutive / Affectionate
  - `ki` : Plural
- Functions: `pluralize()`, `decline_noun()`, `make_diminutive()`, `make_augmentative()`

### Prepositions (`khasi.grammar.prepositions`)
Khasi uses prepositions rather than postpositions:
- `jong` (genitive: of)
- `ha` (locative: in/at/on)
- `sha` (allative: to/towards)
- `na` (ablative: from)
- `da` (instrumental: by/with)
- `bad` (comitative: with/and)
- `ïa` (accusative/dative object marker)
- `ban` (purposive/infinitive: to/for)

### Verbs & Tense-Aspect-Mood (`khasi.grammar.verbs`)
- Tenses: `past` (`la`), `present` (unmarked or `dang`), `future` (`yn` / `’n`), `future_definite` (`daw`), `habitual` (`ju`).
- Modals: potential (`lah ban`), obligation (`dei ban`).
- Contraction handling: `ngam`, `um`, `kam`, `kim`, `phim`, `ngan`, `un`, `kan`, `kin`, `phin`.

### Syntax Engine (`khasi.grammar.syntax`)
- `build_sentence(subject, verb, obj=None, tense='present', aspect='simple', negative=False)`: Constructs valid SVO sentences.
- `interrogative_sentence(interrogative, subject, verb)`: Generates Khasi questions.

---

## 4. Lexicon & Morphological Universe (`khasi.lexicon`)

- `KhasiDictionary`: Full bilingual and trilingual dictionary engine loaded with 100,000+ (1 Lakh+) entries from `words.json`, `phrases.json`, `proverbs.json`, `riddles.json`. Extracted from U Mondon Bareh's *Khasi-English Course and Grammar*, U Nissor Singh's *Khasi-English Dictionary*, and the *English-Khasi Dictionary*.
- `KhasiMorphologyEngine`: Dynamically handles 300,000+ morphological forms with prefix stripping and affix analysis.
- `MorphAnalysis`: Data container with `token`, `lemma`, `pos`, `gender`, `number`, `case`, `english_meaning`, `hindi_meaning`, `prefix_type`.

---

## 5. Universal Translation Engine (`khasi.translator`)

- Multi-dialect support:
  - `sohra` : Standard Literary Khasi
  - `shillong` : Colloquial urban dialect
  - `pnar` : Jaiñtia Hills variant
  - `war` : Southern slopes variant
  - `bhoi` : Ri-Bhoi variant
- `TranslationResult`: Named tuple containing `text`, `source_lang`, `target_lang`, `confidence`, and `dialect`.

---

## 6. Culture, Calendar, Literature & Matrilineal Kinship (`khasi.culture`)

- `describe_matrilineal_system()`: Complete description of matrilineal kinship, clan exogamy rules (*Sang*), and ultimogeniture inheritance by *Ka Khadduh*.
- `list_kinship_terms()`: Comprehensive dictionary of kinship roles (*Mei*, *Pa*, *Khadduh*, *Kñi*, *Kur*, *Kha*, *Kong*, *Bah*, *Hep*).
- `MARKET_CYCLE`: The historic 8-day rotating market cycle of the Khasi Hills.
- `KHASI_MONTHS`: 12 traditional lunar/solar months with cultural meanings.
- `KHASI_FESTIVALS`: Detailed documentation of *Shad Suk Mynsiem*, *Ka Pomblang Nongkrem*, *Behdeinkhlam*, *Seng Kut Snem*, and *Shad Wangala*.
- `authors()`: Documented classical literary luminaries (U Soso Tham, Babu Jeebon Roy, Radhon Singh Berry, Dr. H. Lyngdoh, U Mondon Bareh, U Sib Charan Roy, U Rabon Singh).
- `epics()`: Traditional Khasi epics (*U Sohpetbneng*, *U Thlen*, *Ka Nohkalikai*, *Manik Raitong*).
- `poems()`: Classical poetry with English translations.
- `khasi.proverbs.all()`: Traditional moral proverbs (*Ki Ktien Tymmen* / *Phawar*).

---

## 7. Voice & Speech Synthesis (`khasi.voice`)

- `KhasiVoiceSynthesizer.get_speech_ssml(text, rate='medium', pitch='+0%')`: Generates standard SSML XML.
- `KhasiVoiceSynthesizer.get_phonetic_script(text)`: Produces syllable decomposition and orthographic profiles.
- `KhasiVoiceSynthesizer.generate_pcm_wav(duration, freq)`: Pure sinusoidal PCM audio wave generator.

---

## 8. Digital Archival & Field Preservation (`khasi.preservation`)

- `PreservationRecord`: Dataclass capturing metadata (ID, title, speaker name/age/clan, dialect, audio file, translation, license).
- `CorpusManager`: Archiving manager with:
  - `validate_text()` : Orthographic integrity & health check.
  - `export_jsonl()` : LLM fine-tuning format.
  - `export_csv()` : Tabular format for field linguists.
  - `export_huggingface_format()` : Direct format for Hugging Face datasets.
