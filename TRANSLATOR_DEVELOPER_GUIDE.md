# Khasi Machine Translation & NLP Developer Guide
=====================================================

This comprehensive guide is designed for **NLP researchers, software engineers, and AI developers** building **Khasi Translation Systems**, Neural Machine Translation (NMT) models, Large Language Model (LLM) fine-tuning pipelines, and Speech-to-Text / Text-to-Speech (ASR/TTS) applications using the `khasi` Python library.

---

## 1. Executive Summary & Library Architecture

The `khasi` library is a complete linguistic and computational standard library for **Ka Ktien Khasi** (Austroasiatic, Meghalaya, Northeast India). It provides everything needed to build state-of-the-art translators without relying on external web APIs:

```
┌────────────────────────────────────────────────────────────────────────┐
│                        KHASI LANGUAGE LIBRARY                          │
├──────────────────────────┬─────────────────────────────────────────────┤
│ 1. Trilingual Lexicon    │ 105,296+ Headwords (Khasi-English-Hindi)    │
│ 2. Morphology Engine     │ 300,000+ Derived Forms & Affix Analyzers    │
│ 3. Dialectology Hub      │ 13,000+ Sub-Lexicons (Pnar, War, Bhoi, etc)│
│ 4. Aligned MT Corpora    │ Bitext & TMX (Sentence-Aligned Benchmarks)  │
│ 5. Whole Books Reader    │ 24 Complete Books (1,980+ Pages, 470k Words)│
│ 6. Folklore & Legends    │ 12 Oral Myths, Section Texts & Translations │
│ 7. Traditional Songs     │ 10 Songs, Archery Phawar & Ballad Cycles    │
│ 8. Speech Audio Waveforms│ 252 Native 16kHz PCM WAV Audio Files        │
│ 9. Syntax & Grammar      │ SVO Syntax, Declensions, Aspect/Tense       │
│ 10. Cultural Ontology    │ Kinship, Clans, Sacred Sites, Rituals       │
└──────────────────────────┴─────────────────────────────────────────────┘
```

---

## 2. Quickstart for Machine Translation Engineers

Install the library:
```bash
pip install --upgrade khasi
```

Verify installation:
```python
import khasi

# 1. Direct Rule-Based / Pivot Translation
res = khasi.translate("How are you?")
print(res.text)  # "Kumno phi long?"

# 2. Universal Dictionary Lookup (with morphological fallback)
entry = khasi.lookup("pynim")
print(entry)
# {'khasi': 'pynim', 'english': 'to revive, save, bring to life', 'pos': 'verb', 'derivation': 'causative (pyn- + im)'}

# 3. Dialect-to-Dialect Translation
war_text = khasi.dialects.translate("U briew u leit sha ïing.", source="sohra", target="war")
print(war_text)  # "U brou u hie sa ïeng."
```

---

## 3. Core Translation Pipelines & Workflows

### Pipeline A: Building Neural Machine Translation (NMT) Datasets

When training neural architectures (such as **NLLB-200**, **MarianMT**, or **mBART**), high-quality sentence-aligned bitext is essential.

#### 1. Extracting Sentence-Aligned Parallel Corpora:
```python
import khasi

corpus = khasi.parallel_corpus

# Summary of parallel datasets
print(corpus.summary())
# {'total_pairs': 121, 'sources': {'ka_niam_jong_ki_khasi': 42, 'ka_jingiaid_u_pilgrim': 45, 'bible_excerpts': 34}}

# Access aligned pairs
for pair in corpus.get_pairs():
    print(f"KHA: {pair['khasi']}")
    print(f"ENG: {pair['english']}")
    print(f"ALIGNMENT CONFIDENCE: {pair['confidence']}")
```

#### 2. Exporting to Training Formats (`.kha`/`.en` Bitext and TMX):
```python
# Export clean bitext files for Fairseq / MarianMT / Hugging Face datasets
bitext = corpus.export_bitext()
with open("train.kha", "w", encoding="utf-8") as fk, open("train.en", "w", encoding="utf-8") as fe:
    fk.write(bitext["khasi"])
    fe.write(bitext["english"])

# Export Translation Memory eXchange (TMX) format for CAT tools
tmx_content = corpus.export_tmx()
with open("khasi_corpus.tmx", "w", encoding="utf-8") as f:
    f.write(tmx_content)
```

---

### Pipeline B: Leveraging the 105,000+ Trilingual Lexicon for Word/Phrase Alignment

Khasi NLP models frequently suffer from out-of-vocabulary (OOV) errors. Use `khasi.lookup()` and `khasi.search()` as lexical constraints during decoding or prompt augmentation:

```python
import khasi

# Word lookup across Khasi, English, and Hindi
result = khasi.lookup("khublei")
print(result["english"])  # "hello / thank you / greetings"
print(result["hindi"])    # "नमस्ते / धन्यवाद / प्रणाम"

# Search by English meaning to find all Khasi candidate lemmas
candidates = khasi.search("wisdom")
for c in candidates[:5]:
    print(f"{c['khasi']} ({c['pos']}): {c['english']}")
```

---

### Pipeline C: Morphological Decomposition & Stemming

Khasi heavily relies on productive prefixes:
- `jing-` : Abstract nominalization (e.g. *stad* 'wise' -> *jingstad* 'wisdom')
- `pyn-` : Causative verb derivation (e.g. *iap* 'die' -> *pyniap* 'kill')
- `nong-` : Agentive nominalization (e.g. *hikai* 'teach' -> *nonghikai* 'teacher')
- `sngew-` : Sensory/experiential verb (e.g. *bha* 'good' -> *sngewbha* 'please / be glad')
- `mar-` : Reciprocal action (e.g. *iatreil* -> *mar-iatreil*)
- `ba-` : Attributive participle / adjective (e.g. *bha* -> *babha* 'good')
- `bym-` : Negative participle / antonym (e.g. *man* -> *bymman* 'evil / unrighteous')

When building tokenizers (BPE / WordPiece / SentencePiece), use the morphology engine to avoid segmenting legitimate morphological stems:

```python
import khasi

# Morphological analysis of complex inflected words
analysis = khasi.analyze("jingpyniap")
print(analysis.is_derived)      # True
print(analysis.prefix)          # "jing-" (nominalizer)
print(analysis.root)            # "pyniap" (causative root from "iap")
print(analysis.derivation_type) # "nominalization"

# Reverse derivation (Generation)
root = "trei"  # work
print(khasi.nominalize(root))    # "jingtrei" (the work / labor)
print(khasi.agent_noun(root))     # "nongtrei" (worker)
print(khasi.causative(root))      # "pyntrei"  (cause to work / employ)
```

---

### Pipeline D: Large Language Model (LLM) Grounding & System Prompting

When prompting models like GPT-4, Claude 3.5, Gemini 1.5 Pro, or LLaMA 3 for Khasi translation, LLMs tend to hallucinate or confuse Khasi with Assamese, Bengali, or Garo.

Use `khasi.get_khasi_prompt()` to generate a linguistically grounded system prompt:

```python
import khasi

# Generate production-ready system prompt for any LLM
system_prompt = khasi.get_khasi_prompt(task="translation", target_dialect="sohra")
print(system_prompt)
```

#### Example LangChain / OpenAI / Gemini Integration:
```python
import khasi

def translate_with_llm(user_english_text: str, client) -> str:
    # 1. Extract potential vocabulary matches from local dictionary
    tokens = user_english_text.lower().split()
    glossary = []
    for token in tokens:
        matches = khasi.search(token)
        if matches:
            top = matches[0]
            glossary.append(f"{token} -> {top['khasi']} ({top['pos']})")

    # 2. Inject vocabulary grounding and grammatical rules into system prompt
    system_instruction = khasi.get_khasi_prompt(task="translation")
    if glossary:
        system_instruction += "\n\nVerified Khasi Vocabulary Constraints:\n" + "\n".join(glossary[:10])

    # 3. Call LLM
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": f"Translate to Khasi: {user_english_text}"}
        ],
        temperature=0.1
    )
    return response.choices[0].message.content
```

---

### Pipeline E: Dialect Adaptation (Pnar, War, Bhoi, Maram)

Standard Khasi (*Ka Ktien Sohra*) differs significantly from regional dialects:

| Concept | Sohra (Standard) | Pnar (Jaintia) | War (Southern Slopes) | Bhoi (Northern Slopes) | Maram (Western Plateau) |
|---|---|---|---|---|---|
| Person / Human | *briew* | *bru* | *brou* | *briu* | *briu* |
| Mother | *mei* | *bei* | *mei* | *mei* | *mei* |
| Father | *kpa* | *pa* | *kpa* | *kpa* | *kpa* |
| House | *ïing* | *ïung* | *ïeng* | *ïing* | *ïing* |
| Water | *um* | *um* | *am* | *um* | *um* |
| Rice (cooked) | *ja* | *ja* | *ba* | *ja* | *ja* |
| Go | *leit* | *lai* | *hie* | *leit* | *leit* |

```python
import khasi

# 1. Cognate Lookup across all dialects
cognates = khasi.dialects.cognates("briew")
print(cognates)
# {'sohra': 'briew', 'pnar': 'bru', 'war': 'brou', 'bhoi': 'briu', 'maram': 'briu'}

# 2. Automated Sentence-Level Dialect Transformation
sohra_sentence = "U briew u leit sha ïing ban bam ja bad dih um."
pnar_sentence = khasi.dialects.translate(sohra_sentence, source="sohra", target="pnar")
war_sentence = khasi.dialects.translate(sohra_sentence, source="sohra", target="war")

print(f"Sohra: {sohra_sentence}")
print(f"Pnar:  {pnar_sentence}")  # "U bru u lai sha ïung ban bam ja bad dih um."
print(f"War:   {war_sentence}")   # "U brou u hie sa ïeng ban bam ba bad dih am."
```

---

### Pipeline F: Whole-Books Full-Text Corpus Mining (`khasi.books`)

The library includes the full texts and pages of **24 foundational classical books** (over **1,980+ pages** and **470,000+ words**). Use this corpus for **language model pre-training**, **unsupervised embedding learning**, and **context-aware translation**:

```python
import khasi.books as kb

# 1. Overview of digitized collection
summary = kb.books.summary()
print(f"Total Books: {summary['total_books']}")
print(f"Total Pages: {summary['total_pages']}")
print(f"Total Words: {summary['total_words']}")

# 2. Access a specific classic book
book = kb.get_book("ka_niam_ki_khasi")
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Total Pages: {book.total_pages}")

# 3. Read page-by-page (clean, tokenizable text)
for page_num in range(1, 5):
    page_text = book.get_page(page_num)
    print(f"--- Page {page_num} ---\n{page_text[:150]}...")

# 4. Search across all 24 books for parallel usage examples
hits = kb.search_books("hynniewtrep", max_results_per_book=2)
for h in hits:
    print(f"[{h['title']} - p.{h['page_number']}]: {h['snippet']}")
```

---

### Pipeline G: Speech Dataset Integration (ASR & TTS)

For speech translation and multi-modal models (Whisper, SeamlessM4T, VITS, Bark):

```python
import khasi

dataset = khasi.audio_dataset

# Inspect dataset
print(f"Total Audio Samples: {len(dataset)}")  # 252 audio samples

# Retrieve specific audio record
item = dataset.get_item("phrase_001")
print(f"Khasi Text:  {item['text']}")
print(f"English:     {item['english']}")
print(f"Dialect:     {item['dialect']}")
print(f"Audio Path:  {item['audio_file']}")
print(f"Sample Rate: {item['sample_rate']} Hz")

# Load raw PCM audio waveform bytes for speech training
raw_bytes = dataset.get_waveform_bytes("phrase_001")
print(f"PCM Waveform Size: {len(raw_bytes)} bytes")
```

---

## 4. Linguistic Specifics Every Translator Must Know

### 1. Gendered Articles and Nominal Classifiers
Every noun in Khasi requires an article that specifies grammatical gender and number:
- `u` : Masculine singular (e.g. *u shynrang* 'the man', *u kpa* 'the father', *u khla* 'the tiger')
- `ka` : Feminine singular (e.g. *ka kynthei* 'the woman', *ka mei* 'the mother', *ka sngi* 'the sun')
- `i` : Diminutive / affectionate singular (e.g. *i khunlung* 'the baby', *i mei* 'my dear mother')
- `ki` : Plural (common gender) (e.g. *ki briew* 'the people', *ki kpa* 'the fathers')

In translation, **never drop the article**:
- Correct: *"Ka sngi ka la shai"* (The sun has shone)
- Incorrect: *"Sngi la shai"*

### 2. SVO Word Order with Subject-Verb Pronoun Copy
Khasi exhibits a distinctive pronoun agreement rule where the subject pronoun must be repeated before the verb:
```
[Subject Noun Phrase] + [Agreement Pronoun] + [Tense Marker] + [Verb] + [Object]
  Ka kmie                ka                     la               shew     ia u khun
 (The mother)           (she)                  (PAST)           (found)  (ACC the son)
```

Use `khasi.build_sentence()` to programmatically construct grammatically validated clauses:
```python
sentence = khasi.build_sentence(
    subject="u kpa",
    verb="thoh",
    object_="ka shithi",
    tense="past"
)
print(sentence)  # "u kpa u la thoh ia ka shithi"
```

### 3. Kinship & Ultimogeniture Sensitivity
In Khasi matrilineal society:
- The youngest daughter (*Ka Khatduh*) inherits ancestral property and cares for family relics.
- Maternal uncle (*U Kni*) exercises clan authority.
- The word for grandmother is *Ka Mei-radha* or *Ka Mei-pun*.

Use `khasi.describe_matrilineal_system()` and `khasi.list_kinship_terms()` to prevent incorrect translations of family relationships.

---

## 5. API Reference Summary

| API Call | Return Type | Description |
|---|---|---|
| `khasi.translate(text, ...)` | `TranslationResult` | Rule-based and pivot translation into Khasi |
| `khasi.lookup(word)` | `dict` | Trilingual dictionary lookup with morphological fallback |
| `khasi.search(query)` | `list[dict]` | Search across Khasi, English, and Hindi lemmas |
| `khasi.analyze(word)` | `MorphAnalysis` | Morphological decomposition (prefix, root, category) |
| `khasi.conjugate(verb, tense, pronoun)` | `str` | Full verb conjugation across tenses and aspects |
| `khasi.build_sentence(...)` | `str` | SVO sentence builder with proper pronoun copies |
| `khasi.parallel_corpus.get_pairs()` | `list[dict]` | Aligned Khasi-English translation sentence pairs |
| `khasi.parallel_corpus.export_bitext()` | `dict[str, str]` | Export sentence-aligned `.kha` and `.en` bitext |
| `khasi.parallel_corpus.export_tmx()` | `str` | Export standard Translation Memory eXchange (TMX) |
| `khasi.dialects.translate(text, src, tgt)` | `str` | Multi-dialect sentence transformer |
| `khasi.dialects.cognates(word)` | `dict[str, str]` | Cognate map across Sohra, Pnar, War, Bhoi, Maram |
| `khasi.books.all()` | `list[dict]` | Summary catalogue of all 24 digitized whole books |
| `khasi.books.get(id_or_title)` | `KhasiBook` | Full book reader object with all pages and chapters |
| `khasi.books.read(id, page)` | `str` | Direct text retrieval of a specific book page |
| `khasi.search_books(query)` | `list[dict]` | Cross-book full-text search across all 1,980+ pages |
| `khasi.folklore.all()` | `list[dict]` | Summary catalogue of all 12 folklore oral legends |
| `khasi.folklore.get(id_or_title)` | `FolkloreStory` | Full story with sections, moral, and translation |
| `khasi.search_folklore(query)` | `list[dict]` | Cross-folklore search across Khasi & English |
| `khasi.songs.all()` | `list[dict]` | Summary index of all 10 songs, phawar, and ballads |
| `khasi.songs.get(id_or_title)` | `Song` | Full song object with stanzas, lyrics, and instruments |
| `khasi.search_songs(query)` | `list[dict]` | Cross-song lyric search across Khasi & English |
| `khasi.audio_dataset.get_item(id)` | `dict` | Audio record with transcription, translation, and path |
| `khasi.get_khasi_prompt(task)` | `str` | Optimized system prompt for LLM translation grounding |

---

## 6. Evaluation & Benchmarks

When benchmarking Khasi translation models:
1. **chrF++** is recommended over standard BLEU for Khasi, as Khasi's agglutinative prefixation and article structure make character n-gram F-score significantly more representative of translation quality than word BLEU.
2. Ensure test sets preserve diacritics (`ï`, `ñ`). Use `khasi.normalize(text)` on both references and hypotheses before evaluation to standardize apostrophes and casing.

---

## 7. Support & Community

- **Repository**: [https://github.com/infoakshatsinghbisht-eng/KHASI-language-library](https://github.com/infoakshatsinghbisht-eng/KHASI-language-library)
- **PyPI Package**: [https://pypi.org/project/khasi/](https://pypi.org/project/khasi/)
- **Author & Maintainer**: Akshat Singh Bisht (<infoakshatsinghbisht@gmail.com>)
- **Official Documentation**: See [`DOCUMENTATION.md`](DOCUMENTATION.md)
