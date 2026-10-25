# -*- coding: utf-8 -*-
"""
Harvest and integrate newly discovered genuine historical Khasi works into the library:
- in.ernet.dli.2015.22730 (Report On The Administration Of The Cossyah And Jynteah Hill Territory)
- ecossais-the-khasi-saga-first-edition-2006 (ECOSSAIS The Khasi Saga)
- khasijaintiafolk0000sens (Khasi-Jaintia folklore: context, discourse, and history)
- jstor-3014361 (On the Khasia Tribe)
- lifeworkinkhasia01jenk (Life and work in Khasia)
- lalanguekhasiat00hovegoog (La langue khasia)
- lifecultureofmat0000dasg (Life and culture of matrilineal tribe of Meghalaya)
- 21.-lenamiki-khonglah (Naming the Land: Linguistic Exploration of Khasi Toponyms)
- 1986Meghalaya8 (The Meghalaya Succession to Self Acquired Property Khasi and Jaintia Special Provision Act, 1986)
- himalayanjournal0435hook (Himalayan Journals - Khasia Mountains Vol 1)
- himalayanjournal0335hook (Himalayan Journals - Khasia Mountains Vol 2)
- dli.csl.5921 (Himalayan Journals - Khasia Mountains DLI)
- dli.csl.5026 (Himalayan Journals Vol 2 DLI)
- biostor-149971 (Butterflies of Khasia and Jaintia Hills)
- biostor-50936 (Lepidoptera of the Khasia Hills)
- nelumbo-2455-376x-18-1-4-225-227 (Notes on Rare Plants from Khasi Hills)
- biostor-281191 (List of Chiroptera inhabiting the Khasia Hills)
and many more!
"""

import os
import json
import re
import ssl
import urllib.request
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

ctx = ssl._create_unverified_context()

WORKSPACE_DIR = Path(r"c:\Users\digit_lgfi273\OneDrive\Desktop\pykhasi")
BOOKS_DIR = WORKSPACE_DIR / "khasi" / "culture" / "data" / "books"
PDF_DIR = WORKSPACE_DIR / "data" / "khasi_books"
INDEX_FILE = BOOKS_DIR / "books_index.json"
ARCHIVE_MAP_FILE = WORKSPACE_DIR / "data" / "all_books_archive_map.json"

BOOKS_DIR.mkdir(parents=True, exist_ok=True)
PDF_DIR.mkdir(parents=True, exist_ok=True)

with open(WORKSPACE_DIR / "undiscovered_khasi_candidates.json", encoding='utf-8') as f:
    raw_candidates = json.load(f)

# Load existing index
existing_ids = set()
with open(INDEX_FILE, encoding='utf-8') as f:
    existing_index = json.load(f)
    for b in existing_index:
        existing_ids.add(b['id'].lower())
        if b.get('archive_id'):
            existing_ids.add(b['archive_id'].lower())

# Filter strictly for genuine Khasi candidates
banned_words = ['janwar', 'qurbani', 'lufthansa', 'dr bhandarkar', 'delhi', 'tarzan']

target_candidates = []
for c in raw_candidates:
    ident = c['identifier']
    ident_l = ident.lower()
    title = c['title']
    title_l = title.lower()
    
    if ident_l in existing_ids or any(ident_l in k for k in existing_ids):
        continue
    if any(bw in title_l or bw in ident_l for bw in banned_words):
        continue
        
    if re.search(r'\b(khasi|khasia|khassi|cossyah|cherra|sohra|shillong|meghalaya|pnar)\b', title, re.I):
        target_candidates.append(c)

print(f"Targeting {len(target_candidates)} brand new verified historical Khasi candidates!")

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '_', text).strip('_')
    return text[:60] if text else "book"

def fetch_json(url, timeout=20):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=timeout) as resp:
            return json.loads(resp.read().decode('utf-8'))
    except Exception:
        return None

def fetch_bytes(url, timeout=30):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=timeout) as resp:
            return resp.read()
    except Exception:
        return None

def download_file(url, out_path, timeout=60):
    content = fetch_bytes(url, timeout=timeout)
    if content and len(content) > 1000:
        with open(out_path, 'wb') as f:
            f.write(content)
        return len(content)
    return 0

def process_item(item):
    ident = item['identifier']
    title = item['title']
    author = item.get('creator', 'Khasi Heritage Authors')
    year = item.get('year') or 'Unknown'
    
    slug_base = slugify(f"{title}_{author}")
    if len(slug_base) < 5:
        slug_base = slugify(ident)
        
    json_path = BOOKS_DIR / f"{slug_base}.json"
    pdf_path = PDF_DIR / f"{ident}.pdf"
    
    # 1. Fetch file list
    meta_url = f"https://archive.org/metadata/{ident}/files"
    meta = fetch_json(meta_url)
    if not meta or 'result' not in meta:
        return None, f"No metadata for {ident}"
        
    files = meta.get('result', [])
    
    # Find text file
    txt_file = None
    for f in files:
        fname = f.get('name', '')
        fmt = f.get('format', '')
        if fmt == 'DjVuTXT' or fname.endswith('_djvu.txt'):
            txt_file = fname
            break
    if not txt_file:
        for f in files:
            fname = f.get('name', '')
            if fname.endswith('.txt') and not fname.endswith('_meta.txt') and not fname.endswith('_files.txt'):
                txt_file = fname
                break
    if not txt_file:
        return None, f"No text file for {ident}"
        
    # Find PDF file
    pdf_file = None
    for f in files:
        fname = f.get('name', '')
        if fname.endswith('.pdf') and not fname.endswith('_text.pdf'):
            pdf_file = fname
            break
    if not pdf_file:
        for f in files:
            fname = f.get('name', '')
            if fname.endswith('.pdf'):
                pdf_file = fname
                break
                
    # Download text
    txt_url = f"https://archive.org/download/{ident}/{txt_file}"
    raw_txt = fetch_bytes(txt_url)
    if not raw_txt or len(raw_txt) < 100:
        return None, f"Could not download text for {ident}"
        
    txt_str = raw_txt.decode('utf-8', errors='ignore')
    
    if '\x0c' in txt_str:
        raw_pages = txt_str.split('\x0c')
    else:
        lines = [l for l in txt_str.splitlines() if l.strip()]
        raw_pages = []
        chunk = []
        for line in lines:
            chunk.append(line)
            if len(chunk) >= 35:
                raw_pages.append('\n'.join(chunk))
                chunk = []
        if chunk:
            raw_pages.append('\n'.join(chunk))
            
    pages = []
    total_words = 0
    p_num = 1
    for p in raw_pages:
        p_clean = p.strip()
        if not p_clean:
            continue
        words = len(re.findall(r'\b\w+\b', p_clean))
        if words < 2:
            continue
        total_words += words
        pages.append({
            "page_number": p_num,
            "text": p_clean,
            "word_count": words
        })
        p_num += 1
        
    if not pages:
        return None, f"Zero valid pages for {ident}"
        
    book_record = {
        "id": slug_base,
        "title": title,
        "author": author,
        "year": str(year),
        "language": "Khasi",
        "archive_id": ident,
        "archive_url": f"https://archive.org/details/{ident}",
        "total_pages": len(pages),
        "total_words": total_words,
        "pdf_download_url": f"https://archive.org/download/{ident}/{pdf_file}" if pdf_file else f"https://archive.org/details/{ident}",
        "description": item.get('description', f"Authentic Khasi literature by {author} ({year})."),
        "pages": pages
    }
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(book_record, f, indent=2, ensure_ascii=False)
        
    pdf_size = 0
    if pdf_file:
        if not pdf_path.exists() or pdf_path.stat().st_size < 1000:
            pdf_url = f"https://archive.org/download/{ident}/{pdf_file}"
            pdf_size = download_file(pdf_url, pdf_path, timeout=60)
        else:
            pdf_size = pdf_path.stat().st_size
            
    meta_entry = {
        "id": slug_base,
        "title": title,
        "author": author,
        "year": str(year),
        "language": "Khasi",
        "archive_id": ident,
        "archive_url": f"https://archive.org/details/{ident}",
        "total_pages": len(pages),
        "total_words": total_words,
        "has_pdf_scan": pdf_path.exists() and pdf_path.stat().st_size > 1000,
        "pdf_size_bytes": pdf_size,
        "file_name": f"{slug_base}.json"
    }
    
    return meta_entry, f"Processed '{title[:35]}' [{ident}] ({len(pages)} pgs, {total_words} wds)"

def main():
    new_entries = []
    processed = 0
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(process_item, c): c for c in target_candidates}
        for future in as_completed(futures):
            c = futures[future]
            processed += 1
            try:
                meta, msg = future.result()
                if meta:
                    new_entries.append(meta)
                    print(f"[{processed}/{len(target_candidates)}] SUCCESS: {msg}", flush=True)
                else:
                    print(f"[{processed}/{len(target_candidates)}] SKIP: {msg}", flush=True)
            except Exception as e:
                print(f"[{processed}/{len(target_candidates)}] ERROR on {c.get('identifier')}: {e}", flush=True)
                
    print(f"\nIntegration finished! Added {len(new_entries)} brand new historical Khasi works!", flush=True)
    
    # Merge into books_index
    index_map = {b['id']: b for b in existing_index}
    for e in new_entries:
        index_map[e['id']] = e
        
    final_books = list(index_map.values())
    final_books.sort(key=lambda x: str(x.get('title', '')).lower())
    
    with open(INDEX_FILE, 'w', encoding='utf-8') as f:
        json.dump(final_books, f, indent=2, ensure_ascii=False)
        
    print(f"Updated books_index.json -> Total: {len(final_books)} books", flush=True)

if __name__ == '__main__':
    main()
