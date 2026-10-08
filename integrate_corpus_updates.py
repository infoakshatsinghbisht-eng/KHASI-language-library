# -*- coding: utf-8 -*-
"""
Integrate authentic Khasi books and vocabulary from Khasi_AI_LLM_Master_Corpus_300_plus.xlsx
into pykhasi.
"""

import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
import zipfile
import xml.etree.ElementTree as ET
import json
import re
from pathlib import Path

# Paths
ROOT = Path(__file__).resolve().parent
CATALOGUE_PATH = ROOT / "khasi" / "culture" / "data" / "khasi_bibliography_catalogue.json"
EXCEL_PATH = ROOT / "data" / "Khasi_AI_LLM_Master_Corpus_300_plus.xlsx"
if not EXCEL_PATH.exists():
    _fallback = Path.home() / "Downloads" / "Khasi_AI_LLM_Master_Corpus_300_plus.xlsx"
    if _fallback.exists():
        EXCEL_PATH = _fallback

# 1. Update Catalogue
with open(CATALOGUE_PATH, "r", encoding="utf-8") as f:
    current_cat = json.load(f)

def clean_key(t):
    return re.sub(r"[^a-zA-Z0-9\u00C0-\u024F]", "", t.lower())

existing_keys = {clean_key(c["title"]): c for c in current_cat}

with zipfile.ZipFile(EXCEL_PATH, "r") as z:
    sheet_xml = z.read("xl/worksheets/sheet1.xml")
    root = ET.fromstring(sheet_xml)
    ns = {"ns": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
    rows = root.findall(".//ns:row", ns)
    
    headers = []
    for c in rows[0].findall("ns:c", ns):
        val = ""
        is_tag = c.find("ns:is", ns)
        if is_tag is not None:
            t = is_tag.find("ns:t", ns)
            if t is not None and t.text: val = t.text
        v_tag = c.find("ns:v", ns)
        if v_tag is not None and v_tag.text:
            val = v_tag.text if not val else val
        headers.append(val)
        
    records = []
    for r in rows[1:]:
        row_vals = []
        for c in r.findall("ns:c", ns):
            val = ""
            is_tag = c.find("ns:is", ns)
            if is_tag is not None:
                t = is_tag.find("ns:t", ns)
                if t is not None and t.text: val = t.text
            v_tag = c.find("ns:v", ns)
            if v_tag is not None and v_tag.text:
                val = v_tag.text if not val else val
            row_vals.append(val)
        while len(row_vals) < len(headers):
            row_vals.append("")
        records.append(dict(zip(headers, row_vals)))

next_id = max(c["id"] for c in current_cat) + 1
new_books_count = 0

for r in records:
    orig = r.get("Originally Khasi?", "").strip()
    title = r.get("Title", "").strip()
    author = r.get("Author", "").strip()
    genre = r.get("Genre", "").strip()
    year_str = r.get("Year", "").strip()
    
    # Exclude non-Khasi texts
    if orig.lower() in ["no / english", "no / translation", "no / translated folktales"]:
        continue
    
    ck = clean_key(title)
    if not ck or ck in existing_keys:
        continue
        
    year = None
    if year_str.isdigit():
        year = int(year_str)
    else:
        m = re.search(r"\b(18\d\d|19\d\d|20\d\d)\b", year_str)
        if m:
            year = int(m.group(1))

    # Master genre classification
    g_lower = genre.lower()
    master_genre = "Original Khasi literature"
    if "history" in g_lower or "politics" in g_lower:
        master_genre = "Khasi history/culture"
    elif "religion" in g_lower or "religious" in g_lower or "moral" in g_lower:
        master_genre = "Khasi religious literature"
    elif "grammar" in g_lower or "linguistics" in g_lower or "language" in g_lower or "primer" in g_lower:
        master_genre = "Khasi grammar/linguistics"
    elif "dictionary" in g_lower or "glossary" in g_lower:
        master_genre = "Khasi dictionaries"
    elif "folklore" in g_lower or "proverb" in g_lower:
        master_genre = "Khasi oral literature / folklore"
    elif "criticism" in g_lower or "prose" in g_lower or "biography" in g_lower:
        master_genre = "Khasi nonfiction / criticism"
    elif "school" in g_lower or "reader" in g_lower:
        master_genre = "Khasi school textbooks"

    work_type = genre.split("/")[0].strip()
    is_trans = "translation" in g_lower or "adaptation" in orig.lower()
    digitized = "public scan verified" in r.get("Public digitized copy?", "").lower()
    
    entry = {
        "id": next_id,
        "title": title,
        "author": author,
        "year": year,
        "genre": master_genre,
        "type": work_type,
        "language": "Khasi" if "mixed" not in orig.lower() else "Khasi / English",
        "is_translation": is_trans,
        "digitized": digitized
    }
    current_cat.append(entry)
    existing_keys[ck] = entry
    next_id += 1
    new_books_count += 1

with open(CATALOGUE_PATH, "w", encoding="utf-8") as f:
    json.dump(current_cat, f, indent=2, ensure_ascii=False)
print(f"Updated Catalogue: Added {new_books_count} new books. Total catalogued works: {len(current_cat)}")

# 2. Update Words Dictionary
with open(WORDS_PATH, "r", encoding="utf-8") as f:
    words_data = json.load(f)

existing_words_set = {w["khasi"].lower() for w in words_data}

from verify_new_entries import NEW_VERIFIED_KHASI_ENTRIES

words_added_count = 0
for entry in NEW_VERIFIED_KHASI_ENTRIES:
    if entry["khasi"].lower() not in existing_words_set:
        words_data.append(entry)
        existing_words_set.add(entry["khasi"].lower())
        words_added_count += 1

with open(WORDS_PATH, "w", encoding="utf-8") as f:
    json.dump(words_data, f, ensure_ascii=False, indent=2)

print(f"Updated Words Dictionary: Added {words_added_count} verified Khasi words. Total entries: {len(words_data):,}")
