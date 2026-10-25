import urllib.request
import urllib.parse
import json
import os
import ssl
import sys

ctx = ssl._create_unverified_context()
os.makedirs("data/english_books", exist_ok=True)

queries = [
    'title:("Story of a Khasi")',
    'title:("Khasi Canvas")',
    'title:("Khasi Milieu")',
    'title:("Impact of the West on Khasis")',
    'title:("The Ramayana") AND creator:("Romesh") AND mediatype:(texts)',
    'title:("The Mahabharata") AND creator:("Romesh") AND mediatype:(texts)',
    'title:("Robinson Crusoe") AND creator:("Defoe") AND mediatype:(texts) AND downloads:[1000 TO 999999]',
    'title:("Aesop") AND title:("Fables") AND mediatype:(texts) AND language:(eng) AND downloads:[1000 TO 999999]',
    'title:("Tribal Folk-Tales of Assam") AND mediatype:(texts)',
    'title:("Khasi Heritage") AND mediatype:(texts)',
    'title:("Short History of Khasi Literature")'
]

discovered = {}
print("Step 1: Searching for additional counterparts...", flush=True)

for q in queries:
    url = f"https://archive.org/advancedsearch.php?q={urllib.parse.quote(q)}&fl[]=identifier,title,creator,year,downloads&sort[]=downloads+desc&rows=10&page=1&output=json"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx, timeout=15) as r:
            docs = json.loads(r.read().decode('utf-8'))['response']['docs']
            for d in docs:
                ident = d.get('identifier')
                if ident and ident not in discovered:
                    discovered[ident] = d
    except Exception as e:
        print(f"Error on query {q}: {e}", flush=True)

print(f"Discovered {len(discovered)} candidates.", flush=True)

# Select top relevant items
target_books = [
    {
        "id": "robinson_crusoe_defoe",
        "title": "The Life and Adventures of Robinson Crusoe (English Original of Ka Jingïaid U Robinson Crusoe)",
        "author": "Daniel Defoe",
        "ia_id": "lifeandadventur00defogoog",
        "fallback_ia_id": "lifeandstrange00defoiala",
        "filename": "Robinson_Crusoe_Daniel_Defoe_English_Original.pdf"
    },
    {
        "id": "aesop_fables_english",
        "title": "Aesop's Fables (English Original of Ki Puriskam U Aesop)",
        "author": "Aesop / Tr. V. S. Vernon Jones",
        "ia_id": "aesopsfables00aesoiala",
        "filename": "Aesops_Fables_English_Original.pdf"
    },
    {
        "id": "the_ramayana_romesh_dutt",
        "title": "The Ramayana: Epic of Rama, Prince of India (English Counterpart of Ka Ramayana by Babu Jeebon Roy)",
        "author": "Romesh Chunder Dutt",
        "ia_id": "ramayanaepicofra00duttiala",
        "filename": "The_Ramayana_English_Romesh_Dutt.pdf"
    },
    {
        "id": "the_mahabharata_romesh_dutt",
        "title": "The Mahabharata: Epic of Ancient India (English Counterpart of Ka Mahabharata by Babu Jeebon Roy)",
        "author": "Romesh Chunder Dutt",
        "ia_id": "mahabharataepico00duttiala",
        "filename": "The_Mahabharata_English_Romesh_Dutt.pdf"
    }
]

# Add any discovered Khasi specific items
for k, v in discovered.items():
    t = str(v.get('title','')).lower()
    if 'khasi' in t or 'assam' in t:
        target_books.append({
            "id": k,
            "title": v.get('title'),
            "author": v.get('creator'),
            "ia_id": k,
            "filename": f"{k}_{v.get('title', 'book')[:30].strip().replace(' ', '_')}.pdf".replace('/', '_').replace(':', '_')
        })

def download_file(item):
    out_path = os.path.join("data/english_books", item['filename'])
    if os.path.exists(out_path) and os.path.getsize(out_path) > 30000:
        print(f"[EXISTS] {item['filename']} ({os.path.getsize(out_path)/1024/1024:.2f} MB)", flush=True)
        return True

    ia_id = item['ia_id']
    print(f"\n[QUERY] Fetching metadata for {ia_id} ({item['title']})...", flush=True)
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
                size = int(pf.get('size', 0))
                if not name.endswith('_bw.pdf') and size > 20000:
                    chosen = pf
                    break
            if not chosen:
                chosen = pdf_files[0]
                
            pdf_name = chosen['name']
            size_mb = int(chosen.get('size', 0)) / 1024 / 1024
            dl_url = f"https://archive.org/download/{ia_id}/{urllib.parse.quote(pdf_name)}"
            print(f"[DOWNLOADING] {ia_id} -> {item['filename']} ({size_mb:.2f} MB)...", flush=True)
            
            dl_req = urllib.request.Request(dl_url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(dl_req, context=ctx, timeout=180) as dl_resp, open(out_path, 'wb') as out_f:
                while True:
                    chunk = dl_resp.read(128 * 1024)
                    if not chunk:
                        break
                    out_f.write(chunk)
            print(f"[SUCCESS] Downloaded {item['filename']} ({os.path.getsize(out_path)/1024/1024:.2f} MB)", flush=True)
            return True
    except Exception as e:
        print(f"[ERROR] Failed for {ia_id}: {e}", flush=True)
        if os.path.exists(out_path):
            try:
                os.remove(out_path)
            except:
                pass
        return False

print("\nStep 2: Downloading selected counterpart books...", flush=True)
count = 0
for it in target_books:
    if download_file(it):
        count += 1

print(f"\nAll done! Verified {count}/{len(target_books)} books.", flush=True)
