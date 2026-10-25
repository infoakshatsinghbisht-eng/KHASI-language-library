import urllib.request
import urllib.parse
import json
import os
import ssl

ctx = ssl._create_unverified_context()

os.makedirs("data/english_books", exist_ok=True)

additional_books = [
    {
        "id": "introduction_to_khasi_language_pryse",
        "title": "An Introduction to the Khasi Language (Comprising Grammar, Selections for Reading, and Khasi-English Vocabulary)",
        "author": "Rev. William Pryse",
        "year": "1855",
        "ia_id": "in.ernet.dli.2015.460881",
        "filename": "An_Introduction_To_The_Khasi_Language_Rev_W_Pryse_1855.pdf"
    },
    {
        "id": "notes_on_khasi_law_cantlie",
        "title": "Notes on Khasi Law (Foundational Customary Matrilineal Law & Institutions)",
        "author": "Sir Keith Cantlie",
        "year": "1934",
        "ia_id": "in.ernet.dli.2015.463852",
        "filename": "Notes_on_Khasi_Law_Sir_Keith_Cantlie_1934.pdf"
    },
    {
        "id": "khasi_phonetic_reader_nagaraja",
        "title": "Khasi Phonetic Reader (Linguistic Grammar & Pronunciation Analysis)",
        "author": "Dr. K. S. Nagaraja (CIIL)",
        "year": "1990",
        "ia_id": "dli.language.1686",
        "filename": "Khasi_Phonetic_Reader_KS_Nagaraja_1990.pdf"
    },
    {
        "id": "meghalaya_culture_history_hamlet_bareh",
        "title": "Meghalaya: History, People and Culture",
        "author": "Dr. Hamlet Bareh",
        "year": "1974",
        "ia_id": "dli.bengal.10689.12557",
        "filename": "Meghalaya_History_People_Culture_Hamlet_Bareh_1974.pdf"
    },
    {
        "id": "report_khasi_jaintia_mills",
        "title": "Report on the Khasi and Jaintia Hills 1853",
        "author": "A. J. M. Mills",
        "year": "1853",
        "ia_id": "dli.ministry.30166",
        "filename": "Report_on_the_Khasi_and_Jaintia_Hills_AJM_Mills_1853.pdf"
    },
    {
        "id": "u_tirot_singh_hamlet_bareh",
        "title": "U. Tirot Singh: Freedom Fighter of the Khasis",
        "author": "Dr. Hamlet Bareh",
        "year": "1984",
        "ia_id": "U.TIROTSINGH",
        "filename": "U_Tirot_Singh_Freedom_Fighter_Dr_Hamlet_Bareh.pdf"
    }
]

def download_item(b):
    out_path = os.path.join("data/english_books", b['filename'])
    if os.path.exists(out_path) and os.path.getsize(out_path) > 50000:
        print(f"[EXISTS] {b['filename']} ({os.path.getsize(out_path)/1024/1024:.2f} MB)", flush=True)
        return True
        
    ia_id = b['ia_id']
    print(f"\n[QUERY] Checking metadata for {ia_id}...", flush=True)
    meta_url = f"https://archive.org/metadata/{ia_id}"
    req = urllib.request.Request(meta_url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            meta = json.loads(resp.read().decode('utf-8'))
            files = meta.get('files', [])
            pdf_files = [f for f in files if f.get('name', '').lower().endswith('.pdf')]
            if not pdf_files:
                print(f"[SKIP] No PDF in {ia_id}", flush=True)
                return False
                
            chosen = None
            for pf in pdf_files:
                name = pf.get('name', '')
                if not name.endswith('_bw.pdf') and not name.endswith('_text.pdf'):
                    chosen = pf
                    break
            if not chosen:
                chosen = pdf_files[0]
                
            pdf_name = chosen['name']
            size_mb = int(chosen.get('size', 0)) / 1024 / 1024
            dl_url = f"https://archive.org/download/{ia_id}/{urllib.parse.quote(pdf_name)}"
            print(f"[DOWNLOADING] {pdf_name} ({size_mb:.2f} MB) -> {b['filename']}...", flush=True)
            
            dl_req = urllib.request.Request(dl_url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(dl_req, context=ctx, timeout=180) as dl_resp, open(out_path, 'wb') as out_f:
                while True:
                    chunk = dl_resp.read(128 * 1024)
                    if not chunk:
                        break
                    out_f.write(chunk)
            print(f"[COMPLETED] {b['filename']} ({os.path.getsize(out_path)/1024/1024:.2f} MB)", flush=True)
            return True
    except Exception as e:
        print(f"[ERROR] Failed for {ia_id}: {e}", flush=True)
        if os.path.exists(out_path):
            try:
                os.remove(out_path)
            except:
                pass
        return False

print("Starting download of additional English counterpart books...", flush=True)
downloaded_count = 0
for b in additional_books:
    if download_item(b):
        downloaded_count += 1

print(f"\nFinished: {downloaded_count}/{len(additional_books)} additional books verified.", flush=True)

# Update registry with all books
reg_file = "data/english_books/english_books_registry.json"
try:
    with open(reg_file, 'r', encoding='utf-8') as f:
        existing = json.load(f)
except:
    existing = []

existing_ids = {x.get('id') for x in existing}
for b in additional_books:
    if b.get('id') not in existing_ids:
        existing.append(b)

with open(reg_file, 'w', encoding='utf-8') as f:
    json.dump(existing, f, indent=2, ensure_ascii=False)

print(f"Updated registry: {len(existing)} total registered English books.", flush=True)
