# -*- coding: utf-8 -*-
"""
Production Multi-threaded Downloader for Newly Discovered Khasi Language Books.
Expands the library to maximum available books on Internet Archive.
Resolves exact metadata PDF filenames and downloads with parallel worker threads.
"""

import os
import sys
import json
import time
import ssl
import urllib.request
import urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed

DEST_DIR = os.path.abspath("data/khasi_books")
CANDIDATES_FILE = "verified_new_khasi_books.json"

if not os.path.exists(DEST_DIR):
    os.makedirs(DEST_DIR, exist_ok=True)

with open(CANDIDATES_FILE, "r", encoding="utf-8") as f:
    candidates = json.load(f)

# Exclude non-Khasi misclassifications
filtered = []
for c in candidates:
    ident = c.get("identifier", "")
    title = c.get("title", "")
    if "lougan" in ident.lower() or "lougan" in title.lower():
        continue
    filtered.append(c)

print(f"Total Verified Khasi Books to Download: {len(filtered)}")

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 pykhasi-library/2.0"
}

def resolve_and_download(book):
    ident = book["identifier"]
    title = book.get("title", "")
    out_path = os.path.join(DEST_DIR, f"{ident}.pdf")
    
    # Check if already downloaded
    if os.path.exists(out_path) and os.path.getsize(out_path) > 50000:
        return {"ident": ident, "title": title, "status": "already_exists", "size": os.path.getsize(out_path)}
        
    meta_url = f"https://archive.org/metadata/{ident}/files"
    meta_req = urllib.request.Request(meta_url, headers=headers)
    
    main_pdf = None
    try:
        with urllib.request.urlopen(meta_req, timeout=15, context=ctx) as r:
            m_data = json.loads(r.read())
            pdf_files = [f for f in m_data.get("result", []) if f.get("name", "").endswith(".pdf")]
            # Prefer clean non-_text scan
            for pf in pdf_files:
                pname = pf.get("name", "")
                if not pname.endswith("_text.pdf"):
                    main_pdf = pname
                    break
            if not main_pdf and pdf_files:
                main_pdf = pdf_files[0].get("name", "")
    except Exception as e:
        return {"ident": ident, "title": title, "status": f"meta_error_{str(e)[:25]}", "size": 0}
        
    if not main_pdf:
        return {"ident": ident, "title": title, "status": "no_pdf_in_metadata", "size": 0}
        
    # Download the main PDF file
    enc_name = urllib.parse.quote(main_pdf)
    dl_url = f"https://archive.org/download/{ident}/{enc_name}"
    dl_req = urllib.request.Request(dl_url, headers=headers)
    
    try:
        with urllib.request.urlopen(dl_req, timeout=60, context=ctx) as r:
            content = r.read()
            if len(content) > 10000 and content.startswith(b"%PDF"):
                with open(out_path, "wb") as f:
                    f.write(content)
                return {"ident": ident, "title": title, "status": "downloaded", "size": len(content), "filename": main_pdf}
            else:
                return {"ident": ident, "title": title, "status": "corrupt_pdf", "size": len(content)}
    except urllib.error.HTTPError as e:
        return {"ident": ident, "title": title, "status": f"http_{e.code}", "size": 0}
    except Exception as e:
        return {"ident": ident, "title": title, "status": f"error_{str(e)[:25]}", "size": 0}

print("\nStarting Parallel Downloads (5 workers)...")
sys.stdout.flush()

success = 0
already = 0
failed = 0
total = len(filtered)
start_time = time.time()

with ThreadPoolExecutor(max_workers=5) as executor:
    futures = {executor.submit(resolve_and_download, b): b for b in filtered}
    
    for idx, fut in enumerate(as_completed(futures), 1):
        res = fut.result()
        st = res["status"]
        mb = round(res["size"] / (1024 * 1024), 2)
        ident = res["ident"]
        t_short = res["title"][:35]
        
        if st == "downloaded":
            success += 1
            print(f"[{idx}/{total}] [DOWNLOADED] {ident} -> {mb} MB ({t_short})")
        elif st == "already_exists":
            already += 1
            print(f"[{idx}/{total}] [EXISTS]     {ident} ({mb} MB)")
        else:
            failed += 1
            print(f"[{idx}/{total}] [SKIP]       {ident} -> {st} ({t_short})")
        sys.stdout.flush()

elapsed = round(time.time() - start_time, 1)
print(f"\n==========================================")
print(f"BATCH DOWNLOAD COMPLETED in {elapsed}s")
print(f"Newly Downloaded: {success}")
print(f"Already Present:  {already}")
print(f"Failed/Skipped:   {failed}")
print(f"==========================================")
