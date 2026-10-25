import urllib.request
import urllib.parse
import json
import os
import ssl
import sys

# Disable SSL verification for archive.org cluster downloads
ctx = ssl._create_unverified_context()

os.makedirs("data/english_books", exist_ok=True)

english_books = [
    {
        "id": "tales_of_darkness_and_light_soso_tham",
        "title": "Tales of Darkness and Light: Soso Tham's The Old Days of the Khasis (Complete English Translation by Janet Hujon)",
        "author": "Soso Tham / Janet Hujon",
        "year": "2018",
        "ia_id": "dli.doa.167",
        "filename": "Tales_of_Darkness_and_Light_Soso_Tham_English.pdf"
    },
    {
        "id": "grammar_of_khassi_language_roberts",
        "title": "A Grammar of the Khassi Language",
        "author": "Rev. H. Roberts",
        "year": "1891",
        "ia_id": "grammarofkhassil00roberich",
        "filename": "A_Grammar_of_the_Khassi_Language_Rev_H_Roberts_1891.pdf"
    },
    {
        "id": "the_khasis_gurdon",
        "title": "The Khasis (Complete English Edition with Folklore, Traditions & Laws)",
        "author": "Major P. R. T. Gurdon & U Nissor Singh",
        "year": "1914",
        "ia_id": "cu31924024052874",
        "filename": "The_Khasis_PRT_Gurdon_1914.pdf"
    },
    {
        "id": "folktales_of_the_khasis_rafy",
        "title": "Folk-Tales of the Khasis (Complete English Folktales Collection)",
        "author": "Mrs. K. U. Rafy",
        "year": "1920",
        "ia_id": "folktalesofkhasi00rafy",
        "filename": "Folk_Tales_of_the_Khasis_Mrs_Rafy_1920.pdf"
    },
    {
        "id": "khasi_english_dictionary_nissor_singh",
        "title": "Khasi-English Dictionary",
        "author": "U Nissor Singh",
        "year": "1906",
        "ia_id": "khasienglishdict00singrich",
        "filename": "Khasi_English_Dictionary_U_Nissor_Singh_1906.pdf"
    },
    {
        "id": "khasi_english_course_grammar_mondon_bareh",
        "title": "Khasi-English Course and Grammar",
        "author": "U Mondon Bareh",
        "year": "1969",
        "ia_id": "in.ernet.dli.2015.464837",
        "filename": "Khasi_English_Course_and_Grammar_Mondon_Bareh.pdf"
    },
    {
        "id": "english_khasi_dictionary_hajom_kissor_singh",
        "title": "English-Khasi Dictionary",
        "author": "U Hajom Kissor Singh",
        "year": "1920",
        "ia_id": "in.ernet.dli.2015.42078",
        "filename": "English_Khasi_Dictionary_Hajom_Kissor_Singh_1920.pdf"
    },
    {
        "id": "khasi_culture_and_society_hamlet_bareh",
        "title": "Khasi Culture and Society",
        "author": "Dr. Hamlet Bareh",
        "year": "1998",
        "ia_id": "in.ernet.dli.2015.464892",
        "filename": "Khasi_Culture_and_Society_Hamlet_Bareh.pdf"
    },
    {
        "id": "pilgrims_progress_english",
        "title": "The Pilgrim's Progress (English Original of Ka Jingïaid U Pilgrim)",
        "author": "John Bunyan",
        "year": "1890",
        "ia_id": "pilgrimsprogress00buny_1",
        "filename": "The_Pilgrims_Progress_John_Bunyan_English.pdf"
    },
    {
        "id": "folk_tales_of_assam_pakrasi",
        "title": "Folk Tales Of Assam (including Khasi & Jaintia Tales)",
        "author": "Mira Pakrasi",
        "year": "1960",
        "ia_id": "in.ernet.dli.2015.124533",
        "filename": "Folk_Tales_Of_Assam_Pakrasi_1960.pdf"
    }
]

def download_ia_pdf(item):
    out_path = os.path.join("data/english_books", item['filename'])
    if os.path.exists(out_path) and os.path.getsize(out_path) > 50000:
        print(f"[EXISTS] {item['filename']} ({os.path.getsize(out_path)/1024/1024:.2f} MB)", flush=True)
        return True

    ia_id = item['ia_id']
    print(f"\n[QUERY] Checking {ia_id} ({item['title']})...", flush=True)
    meta_url = f"https://archive.org/metadata/{ia_id}"
    req = urllib.request.Request(meta_url, headers={'User-Agent': 'Mozilla/5.0'})
    
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            meta = json.loads(resp.read().decode('utf-8'))
            files = meta.get('files', [])
            pdf_files = [f for f in files if f.get('name', '').lower().endswith('.pdf')]
            if not pdf_files:
                print(f"[SKIP] No PDF files in {ia_id}", flush=True)
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
            print(f"[DOWNLOADING] {pdf_name} ({size_mb:.2f} MB) -> {item['filename']}...", flush=True)
            
            dl_req = urllib.request.Request(dl_url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(dl_req, context=ctx, timeout=180) as dl_resp, open(out_path, 'wb') as out_f:
                received = 0
                while True:
                    chunk = dl_resp.read(128 * 1024)
                    if not chunk:
                        break
                    out_f.write(chunk)
                    received += len(chunk)
            print(f"[COMPLETED] {item['filename']} ({os.path.getsize(out_path)/1024/1024:.2f} MB)", flush=True)
            return True
    except Exception as e:
        print(f"[ERROR] Failed for {ia_id}: {e}", flush=True)
        if os.path.exists(out_path):
            try:
                os.remove(out_path)
            except:
                pass
        return False

print("Starting English books download for Khasi literature...", flush=True)
for item in english_books:
    download_ia_pdf(item)

# Save metadata registry of English companion books
registry_path = "data/english_books/english_books_registry.json"
with open(registry_path, "w", encoding="utf-8") as f:
    json.dump(english_books, f, indent=2, ensure_ascii=False)
print(f"\nSaved metadata registry to {registry_path}", flush=True)
print("All English book downloads finished!", flush=True)
