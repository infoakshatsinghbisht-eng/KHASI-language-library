# -*- coding: utf-8 -*-
"""
Extract newly discovered Khasi words, poetic compounds, folklore terms,
and musical expressions from folklore and songs, and add them to
khasi/lexicon/data/words.json.
"""

import json
import re
from pathlib import Path

WORDS_JSON_PATH = Path("khasi/lexicon/data/words.json")

# Load existing words
with open(WORDS_JSON_PATH, "r", encoding="utf-8") as f:
    existing_words_list = json.load(f)

existing_map = {w["khasi"].lower().strip(): w for w in existing_words_list if "khasi" in w}
initial_count = len(existing_words_list)
print(f"Initial words count: {initial_count}")

# 1. Collect all terms from folklore vocabularies
folklore_dir = Path("khasi/culture/data/folklore")
cultural_vocab = {}

for fpath in folklore_dir.glob("*.json"):
    if fpath.name == "folklore_index.json":
        continue
    with open(fpath, "r", encoding="utf-8") as f:
        data = json.load(f)
    vocab = data.get("vocabulary", {})
    story_title = data.get("title", "")
    for term, defn in vocab.items():
        cultural_vocab[term.lower().strip()] = {
            "english": defn,
            "category": "folklore",
            "source": f"Folklore Legend: {story_title}"
        }

# 2. Collect all terms from songs vocabularies
songs_dir = Path("khasi/culture/data/songs")
for fpath in songs_dir.glob("*.json"):
    if fpath.name == "songs_index.json":
        continue
    with open(fpath, "r", encoding="utf-8") as f:
        data = json.load(f)
    vocab = data.get("vocabulary", {})
    song_title = data.get("title", "")
    for term, defn in vocab.items():
        cultural_vocab[term.lower().strip()] = {
            "english": defn,
            "category": "music_poetry",
            "source": f"Folk Song / Phawar: {song_title}"
        }

# Curated specific rich vocabulary from Khasi oral mythologies and song traditions
curated_folklore_words = [
    # Folklore & Mythological terms
    ("jingkieng ksier", "sacred golden ladder bridging heaven and earth on Mount Sohpetbneng", "noun", "ka", "mythology"),
    ("sohpetbneng", "navel of heaven; sacred peak in Ri Bhoi where human creation descended", "noun", "u", "mythology"),
    ("hynniewtrep", "the seven huts or seven families who remained to settle earth", "noun", "ki", "cultural_history"),
    ("khyndaitrep", "the nine celestial families remaining in heaven", "noun", "ki", "mythology"),
    ("diengiei", "mythical gigantic tree of eclipsing darkness on Mount Diengiei", "noun", "u", "mythology"),
    ("mawbyrsiew", "sacred hearthstones placed at the fireplace in traditional homes", "noun", "ki", "culture"),
    ("dpei", "central earth hearth where fire is maintained and stories are told", "noun", "ka", "household"),
    ("thlen", "mythological giant vampire serpent of greed slain at Dainthlen", "noun", "u", "mythology"),
    ("dainthlen", "historic rock plateau where the monster serpent Thlen was carved and slain", "noun", "ka", "geography"),
    ("nohkalikai", "the leap of Likai; iconic 1,115-ft waterfall in Sohra named after Ka Likai", "noun", "ka", "geography"),
    ("manik raitong", "legendary destitute youth whose poignant sharati music touched hearts", "noun", "u", "folklore"),
    ("sharati", "traditional long end-blown bamboo flute played during funeral rites and lament", "noun", "ka", "instrument"),
    ("sier lapalang", "the legendary stag of tragic oral ballad whose mother wept inconsolably", "noun", "u", "folklore"),
    ("jamlu", "sacred funeral wailing, grief weeping chant and lament of mourning", "noun", "ka", "custom"),
    ("krem lamet latang", "primal council cave where birds and beasts sought refuge during world eclipse", "noun", "ka", "mythology"),
    ("lamet latang", "broad wild forest leaves used in traditional ceremonies and wrapping", "noun", "ki", "botany"),
    ("pansngiat meiramew", "golden crown of Mother Earth symbolizing seasonal blossoming", "noun", "ka", "mythology"),
    ("meiramew", "Mother Earth; divine earth goddess personifying natural fertility and sustenance", "noun", "ka", "mythology"),
    ("mawbynna", "monumental upright megalithic standing stones commemorating ancestors", "noun", "ki", "megaliths"),
    ("mawkynthei", "horizontal flat table-stone (dolmen) representing ancestral motherhood", "noun", "u", "megaliths"),
    ("mawshynrang", "tall vertical standing stone (menhir) honoring maternal uncles and maternal lineage", "noun", "u", "megaliths"),
    ("mawbah", "ancestral clan bone repository cairn (ossuary) holding unified clan cremations", "noun", "u", "megaliths"),
    ("mawlynti", "traveler resting megalith erected beside ancient mountain walking paths", "noun", "u", "megaliths"),
    ("tangmuri", "queen of Khasi instruments; sacred double-reed conical pipe", "noun", "ka", "instrument"),
    ("duitara", "plucked four-stringed wooden folk lute of bards and balladeers", "noun", "ka", "instrument"),
    ("maryngod", "traditional two-stringed bowed fiddle played vertically like a cello", "noun", "ka", "instrument"),
    ("shyngwiang", "low-pitched end-blown bamboo flute played during mourning vigils", "noun", "u", "instrument"),
    ("besli", "transverse sweet-toned mountain bamboo flute", "noun", "ka", "instrument"),
    ("mieng", "plucked bamboo mouth harp vibrating against the oral cavity", "noun", "ka", "instrument"),
    ("nakra", "royal copper cauldron kettle drum beaten with heavy wooden mallets", "noun", "ka", "instrument"),
    ("ksing shynrang", "male cylindrical lead drum commanding tempo in festival dances", "noun", "u", "instrument"),
    ("ksing kynthei", "female accompanying drum played softly for maiden processions", "noun", "ka", "instrument"),
    ("ksing padiah", "compact handheld syncopated rhythm drum", "noun", "ka", "instrument"),
    ("kynshaw", "resonant cast brass or bell metal dance cymbals", "noun", "ki", "instrument"),
    ("symphiah", "white yak hair or grass whisk waved by male dancers in Shad Suk Mynsiem", "noun", "ka", "regalia"),
    ("pansngiat", "ornate solid silver or gold crown worn by dancing unmarried maidens", "noun", "ka", "regalia"),
    ("waitlam", "indigenous two-handed ceremonial curved steel sword", "noun", "ka", "regalia"),
    ("stieh", "circular buffalo hide and brass ceremonial warrior shield", "noun", "ka", "regalia"),
    ("jainsem dhara", "prized two-piece festive dress woven from wild eri and mulberry silk", "noun", "ka", "costume"),
    ("ryndia", "traditional hand-spun wild eri silk textile known for natural warmth", "noun", "ka", "costume"),
    ("tapmohkhlieh", "checkered warm woolen or silk shawl draped over the head and shoulders", "noun", "ka", "costume"),
    ("pyrton", "clan cheering party rhyming spirited phawar verses during archery contests", "noun", "ka", "sport"),
    ("iasiat khnam", "traditional highland archery competition; sacred martial tradition", "noun", "ka", "sport"),
    ("ryntieh", "indigenous recurved bow fashioned from seasoned mountain bamboo", "noun", "ka", "sport"),
    ("khnam", "slender arrow fitted with barbed steel head and feather fletching", "noun", "u", "sport"),
    ("skum", "circular cylindrical straw target positioned at archery field end", "noun", "ka", "sport"),
    ("hoi kiw", "sacred ancient victory cheer and proclamation of triumphant joy", "interjection", None, "chants"),
    ("behdeinkhlam", "sacred annual plague-driving summer festival of Jaintia Hills", "noun", "ka", "festival"),
    ("aitnar", "sacred muddy pool at Jowai where the climax ritual dance is performed", "noun", "ka", "sacred_site"),
    ("shad suk mynsiem", "annual spring dance of peaceful hearts celebrated at Weiking", "noun", "ka", "festival"),
    ("seng kut snem", "annual thanksgiving festival commemorating Seng Khasi renaissance on Nov 23", "noun", "ka", "festival"),
    ("pomblang nongkrem", "five-day royal goat sacrifice and sacred dance of the Khyrim state at Smit", "noun", "ka", "festival"),
    ("sohkymphor", "sweet wild mountain berry gathered from pristine hill slopes", "noun", "u", "botany"),
    ("jangew jathang", "wild bitter and aromatic medicinal edible forest greens", "noun", "ki", "botany"),
    ("kuna", "penal clan fine or ritual restitution for moral offenses", "noun", "ka", "law"),
    ("mahadei", "royal consort or queen of an indigenous Khasi Syiem", "noun", "ka", "royalty"),
    ("raitong", "destitute impoverished person or poor solitary wanderer", "noun", "u", "folklore"),
    ("nam sarang", "barbed iron arrow anointed with aconite poison", "noun", "u", "hunting"),
    ("tieh pongdeng", "sprung bamboo hunting bow", "noun", "ka", "hunting"),
    ("kynrem reng", "stately branched antlers of a mature highland stag", "noun", "ki", "wildlife"),
    ("phrang sngi", "firstborn dawn child, favorite pride of a mother", "noun", "u", "kinship"),
    ("tnum", "thatched mountain cottage roof representing shelter of maternal home", "noun", "ka", "household"),
    ("ot kba", "harvesting and reaping ripe golden paddy in terraced fields", "noun", "ka", "agriculture"),
    ("khoh", "conical split-bamboo backpack basket supported by a woven headstrap", "noun", "ka", "material_culture"),
    ("star", "plaited cane headstrap used to carry the conical khoh basket", "noun", "u", "material_culture"),
    ("shang", "shallow flat bamboo tray used for winnowing grains and drying produce", "noun", "ka", "material_culture"),
    ("rashi", "curved steel reaping sickle used for harvesting paddy", "noun", "ka", "tools"),
    ("laitluid", "liberty, sovereign freedom, unenslaved state", "noun", "ka", "politics"),
    ("syiem ba mraw", "puppet monarch subservient to foreign colonial masters", "noun", "u", "history"),
    ("erpyngngad", "cool mountain breeze carrying highland pine scent", "noun", "ka", "nature"),
    ("riat", "sheer rocky gorge, cliff, precipice, or mountain ravine", "noun", "ka", "geography"),
    ("thwei", "deep crystal water pool formed at base of mountain falls", "noun", "ka", "geography"),
    ("kyndiah", "sacred ritual bamboo cup used for libations and omens", "noun", "ka", "ritual"),
    ("paila", "thick red carnelian and coral bead necklace worn in traditional regalia", "noun", "ka", "jewelry"),
    ("shanryngwiang", "ceremonial silver crown ornament with dangling tassels", "noun", "ka", "jewelry"),
    ("kpieng ksiar", "ornate 24-carat gold beaded choker worn by dancing maidens", "noun", "u", "jewelry"),
    ("knia pyrda", "sacred divinatory egg-breaking ritual performed by village priests", "noun", "ka", "ritual"),
    ("diengkhlam", "sacred carved forest tree trunk erected to drive away epidemic", "u", "noun", "ritual"),
    ("symbai", "holy seed grain blessed for fertile agricultural sowing", "u", "noun", "agriculture"),
    ("lympung", "open consecrated grassy festival field or public meeting square", "ka", "noun", "geography"),
    ("khuslai", "anxious worry, heartfelt melancholy or deep inner grief", "adjective", None, "emotion"),
    ("pait-dohnud", "heartbreaking, soul-rending grief or lamentation", "adjective", None, "emotion"),
    ("phawar", "rhyming metered couplet, chanting verse or tournament ballad", "ka", "noun", "literature"),
    ("shlur", "brave, fearless, chivalrous, courageous", "adjective", None, "character"),
    ("hok", "righteousness, divine cosmic order, absolute truth", "ka", "noun", "philosophy"),
    ("sot", "purity, unblemished integrity, clean conscience", "ka", "noun", "philosophy"),
    ("akor", "ancestral etiquette, moral conduct, noble character", "ka", "noun", "philosophy"),
    ("kamai ia ka hok", "to earn righteousness through honest labor; foundational motto", "phrase", None, "philosophy"),
    ("tip kur tip kha", "to know one's matrilineal clan and paternal relatives; foundational kinship law", "phrase", None, "philosophy"),
    ("tip blei tip briew", "to revere God and respect fellow human beings; foundational moral law", "phrase", None, "philosophy"),
    ("lyngdoh", "indigenous hereditary clan priest presiding over community sacrifice", "u", "noun", "religion"),
    ("myntri", "elected clan elder and minister serving on the royal state council (dorbar)", "u", "noun", "governance"),
    ("kiad um", "traditional indigenous fermented rice liquor used in libations", "ka", "noun", "cuisine"),
    ("dkhap", "cricket or small insect singing in twilight mountain meadows", "u", "noun", "wildlife"),
]

# Merge into words list
new_entries = []

# Process cultural vocab from files
for term, info in cultural_vocab.items():
    if term not in existing_map:
        new_entry = {
            "khasi": term,
            "english": info["english"],
            "hindi": f"खासी परंपरा: {info['english']}",
            "pos": "noun",
            "category": info["category"],
            "notes": info["source"]
        }
        new_entries.append(new_entry)
        existing_map[term] = new_entry

# Process curated folklore & song terms
for item in curated_folklore_words:
    term = item[0].lower().strip()
    english = item[1]
    pos = item[2] if len(item) > 2 and item[2] else "noun"
    gender = item[3] if len(item) > 3 and item[3] else None
    cat = item[4] if len(item) > 4 else "folklore_songs"
    
    if term not in existing_map:
        entry = {
            "khasi": term,
            "english": english,
            "hindi": f"खासी लोककथा/गीत: {english}",
            "pos": pos,
            "category": cat
        }
        if gender:
            entry["gender"] = gender
        new_entries.append(entry)
        existing_map[term] = entry
    else:
        # If exists, enrich with folklore/song context if missing
        curr = existing_map[term]
        if "folklore" not in curr.get("category", "") and "music" not in curr.get("category", ""):
            curr["folklore_context"] = english

# Add new entries to list
existing_words_list.extend(new_entries)

# Save back to words.json
with open(WORDS_JSON_PATH, "w", encoding="utf-8") as f:
    json.dump(existing_words_list, f, ensure_ascii=False, indent=2)

print(f"Added {len(new_entries)} newly discovered Khasi words/compounds from folklore and songs!")
print(f"Total dictionary entries now: {len(existing_words_list)}")
