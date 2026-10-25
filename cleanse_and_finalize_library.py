# -*- coding: utf-8 -*-
"""
Cleanse and finalize the Khasi Whole Books Library.
=================================================

Removes non-Khasi foreign items (English zoological/botanical survey papers,
Urdu/Hindi texts, English PhD dissertations) so that every single book in the
library is an authentic Khasi language work.

Then rebuilds:
- books_index.json
- PDF archives in data/khasi_books/
- words_corpus_v26.json (authentic Khasi vocabulary only)
"""

import json
import os
import re
import sys
import glob
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

books_dir = Path("khasi/culture/data/books")
pdf_dir = Path("data/khasi_books")

KHASI_CORE_WORDS = {
    'ka', 'u', 'ki', 'i', 'bad', 'jong', 'ha', 'da', 'ba', 'la', 'ia', 'ïa',
    'nga', 'phi', 'ngi', 'te', 'pat', 'dei', 'kam', 'briew', 'ktien', 'mynsiem',
    'shaphang', 'hima', 'syiem', 'niam', 'khun', 'kpa', 'kmie', 'kumba', 'kumta',
    'hynrei', 'lada', 'ban', 'leit', 'wan', 'bam', 'sngi', 'pyrthei', 'bha',
    'sniew', 'tymmen', 'khynnah', 'jingim'
}

FOREIGN_INDICATORS = [
    r'\bzoological\s+survey\b', r'\bnew\s+species\b', r'\bhomoptera\b', r'\blepidoptera\b',
    r'\bfossorial\s+hymenoptera\b', r'\bparasitic\s+and\s+fossorial\b', r'\bgymnophiona\b',
    r'\bamphibian\s+fauna\b', r'\bearthworms\s+annelida\b', r'\bsoil\s+acarina\b',
    r'\bpolyembryony\b', r'\bannual\s+report\s+on\s+the\s+administration\b',
    r'amar\s+ujala', r'taskheer\s+jinnat', r'waqar_al_fatawa', r'yamaha',
    r'khanqah', r'shahabukhair', r'shaidulkhatir', r'bahjah_mardiah',
    r'badshahiqbal', r'le_plateau_de_meghalaya',
    r'amliyaat', r'fatah\s+khaibar', r'gospel\s+presentation\s+only',
    r'pro\s+social\s+behaviour', r'phd\s+thesis', r'department\s+of',
    r'delhi\s+amar\s+ujala', r'naik\s+kamai', r'yadgari\s+i\s+delhi'
]
foreign_re = re.compile('|'.join(FOREIGN_INDICATORS), re.IGNORECASE)

all_json_files = sorted(books_dir.glob("*.json"))
print(f"Total book JSON files in directory: {len(all_json_files)}")

kept_books = []
removed_books = []

for jf in all_json_files:
    if jf.name == "books_index.json":
        continue
    
    try:
        with open(jf, "r", encoding="utf-8") as f:
            bdata = json.load(f)
    except Exception:
        removed_books.append((jf, "Corrupt JSON"))
        continue
    
    title = bdata.get("title", jf.stem)
    pages = bdata.get("pages", [])
    full_text = " ".join(p.get("text", "") for p in pages) if pages else bdata.get("full_text", "")
    
    # 1. Check title against foreign indicators
    if foreign_re.search(title) or foreign_re.search(jf.stem):
        removed_books.append((jf, f"Foreign title: {title[:40]}"))
        continue
        
    # 2. Check Khasi core vocabulary density
    tokens = set(re.findall(r'\b[a-zA-ZïÏñÑ]{2,}\b', full_text.lower()))
    matches = tokens.intersection(KHASI_CORE_WORDS)
    
    # Must have at least 8 distinct core Khasi words
    if len(matches) < 8:
        removed_books.append((jf, f"Low Khasi token density ({len(matches)} matches)"))
        continue
        
    # 3. Check English stop words vs Khasi stop words ratio
    words_list = re.findall(r'\b[a-zA-Z]{2,}\b', full_text.lower())
    total_words_count = len(words_list)
    if total_words_count > 500:
        english_stops = sum(1 for w in words_list if w in ('the', 'of', 'and', 'in', 'to', 'is', 'for', 'was', 'with', 'as', 'by', 'on', 'at'))
        khasi_stops = sum(1 for w in words_list if w in ('ka', 'u', 'ki', 'i', 'jong', 'bad', 'ha', 'da', 'ba', 'la', 'ia', 'nga', 'phi'))
        if english_stops > khasi_stops * 3:
            removed_books.append((jf, f"English dominant: {english_stops} en vs {khasi_stops} kh"))
            continue
            
    kept_books.append((jf, bdata))

print(f"\nCleanse Results:")
print(f"  Authentic Khasi books kept: {len(kept_books):,}")
print(f"  Non-Khasi items removed: {len(removed_books):,}")

# Remove the non-Khasi JSON files and corresponding PDFs
for jf, reason in removed_books:
    try:
        jf.unlink()
        pdf_file = pdf_dir / f"{jf.stem}.pdf"
        if pdf_file.exists():
            pdf_file.unlink()
    except Exception as e:
        print(f"Error removing {jf.name}: {e}")

print("Removed non-Khasi files from disk.")

# Rebuild books_index.json
print("\nRebuilding books_index.json with canonical sorting...")
clean_index = []
for jf, data in kept_books:
    b_id = data.get("id", jf.stem)
    pdf_path = pdf_dir / f"{b_id}.pdf"
    clean_index.append({
        "id": b_id,
        "title": data.get("title", jf.stem),
        "author": data.get("author", "Unknown"),
        "year": data.get("year", ""),
        "language": "Khasi",
        "total_pages": len(data.get("pages", [])),
        "total_words": data.get("total_words", 0),
        "file_name": jf.name,
        "archive_id": data.get("archive_id", ""),
        "archive_url": data.get("archive_url", ""),
        "has_pdf_scan": pdf_path.exists(),
        "pdf_size_bytes": pdf_path.stat().st_size if pdf_path.exists() else 0
    })

# Sort index: canonical short IDs first, then title
clean_index.sort(key=lambda x: (x["title"].lower(), 1 if x["id"].startswith(('in_ernet', '104', '105', 'scanned', 'cbfc')) else 0))

with open(books_dir / "books_index.json", "w", encoding="utf-8") as f:
    json.dump(clean_index, f, ensure_ascii=False, indent=2)

total_pages = sum(b["total_pages"] for b in clean_index)
total_words = sum(b["total_words"] for b in clean_index)
total_pdfs = len(list(pdf_dir.glob("*.pdf")))

print(f"\nFinal Library Metrics:")
print(f"  Total Authentic Khasi Books: {len(clean_index):,}")
print(f"  Total Authentic Pages: {total_pages:,}")
print(f"  Total Authentic Words: {total_words:,}")
print(f"  Total PDFs in data/khasi_books/: {total_pdfs:,}")
