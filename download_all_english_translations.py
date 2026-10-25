import urllib.request
import urllib.parse
import json
import os
import ssl
import sys

ctx = ssl._create_unverified_context()
os.makedirs("data/english_books", exist_ok=True)

with open("data/english_books/discovered_english_candidates.json", "r", encoding="utf-8") as f:
    candidates = json.load(f)

print(f"Loaded {len(candidates)} discovered English candidates.", flush=True)

# Extract barcodes/accession numbers from existing files
def get_existing_accessions():
    accs = set()
    for f in os.listdir("data/english_books"):
        if f.endswith(".pdf"):
            # check numbers in filename
            parts = f.replace(".", "_").replace("-", "_").split("_")
            for p in parts:
                if p.isdigit() and len(p) >= 4:
                    accs.add(p)
    return accs

existing_files = os.listdir("data/english_books")

def download_book_pdf(item):
    ident = item['identifier']
    
    # Check if barcode or ID already in existing files
    ident_clean = ident.replace(".", "_").replace("-", "_")
    for ef in existing_files:
        if not ef.endswith(".pdf"):
            continue
        if ident in ef:
            p = os.path.join("data/english_books", ef)
            print(f"[ALREADY EXISTS] {ef} ({os.path.getsize(p)/1024/1024:.2f} MB)", flush=True)
            return ef
            
    # Also check if title is substantially represented
    title_raw = str(item.get('title', ''))
    title_words = [w.lower() for w in title_raw.split() if len(w) > 4 and w.isalpha()]
    for ef in existing_files:
        if not ef.endswith(".pdf"):
            continue
        ef_lower = ef.lower()
        if len(title_words) >= 3 and sum(1 for w in title_words if w in ef_lower) >= 3:
            p = os.path.join("data/english_books", ef)
            print(f"[ALREADY EXISTS BY TITLE] {ef} ({os.path.getsize(p)/1024/1024:.2f} MB)", flush=True)
            return ef

    title_clean = "".join(c if c.isalnum() or c in " _-" else "_" for c in item.get('title', ident))[:50].strip().replace(" ", "_")
    filename = f"{ident}_{title_clean}.pdf".replace("__", "_")
    out_path = os.path.join("data/english_books", filename)

    print(f"\n[QUERY] Fetching metadata for {ident} ({item.get('title')})...", flush=True)
    meta_url = f"https://archive.org/metadata/{ident}"
    req = urllib.request.Request(meta_url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            meta = json.loads(resp.read().decode('utf-8'))
            files = meta.get('files', [])
            pdf_files = [f for f in files if f.get('name', '').lower().endswith('.pdf')]
            if not pdf_files:
                print(f"[NO PDF] Skipping {ident}", flush=True)
                return None
                
            chosen = None
            for pf in pdf_files:
                name = pf.get('name', '')
                size = int(pf.get('size', 0))
                if not name.endswith('_bw.pdf') and not name.endswith('_text.pdf') and size > 200000:
                    chosen = pf
                    break
            if not chosen:
                chosen = pdf_files[0]
                
            pdf_name = chosen['name']
            size_mb = int(chosen.get('size', 0)) / 1024 / 1024
            dl_url = f"https://archive.org/download/{ident}/{urllib.parse.quote(pdf_name)}"
            print(f"[DOWNLOADING] {ident} ({size_mb:.2f} MB) -> {filename}...", flush=True)
            
            dl_req = urllib.request.Request(dl_url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(dl_req, context=ctx, timeout=180) as dl_resp, open(out_path, 'wb') as out_f:
                while True:
                    chunk = dl_resp.read(128 * 1024)
                    if not chunk:
                        break
                    out_f.write(chunk)
            print(f"[SUCCESS] Downloaded {filename} ({os.path.getsize(out_path)/1024/1024:.2f} MB)", flush=True)
            existing_files.append(filename)
            return filename
    except Exception as e:
        print(f"[ERROR] {ident}: {e}", flush=True)
        if os.path.exists(out_path):
            try:
                os.remove(out_path)
            except:
                pass
        return None

print("\nStarting automated download of English translations & companions...", flush=True)
success = 0
for it in candidates:
    if download_book_pdf(it):
        success += 1

print(f"\nAll downloads completed! Total active English books: {success}", flush=True)
