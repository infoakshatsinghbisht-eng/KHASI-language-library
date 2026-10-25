import urllib.request
import urllib.parse
import json
import os
import ssl

ctx = ssl._create_unverified_context()
os.makedirs("data/english_books", exist_ok=True)

classics = [
    {
        "id": "the_book_of_good_counsels_hitopadesa_arnold",
        "title": "The Book of Good Counsels: From the Sanskrit of Hitopadesa (English Original of Ka Hit-Upadesa by Babu Jeebon Roy)",
        "author": "Sir Edwin Arnold",
        "year": "1893",
        "ia_id": "cu31924074412994",
        "filename": "The_Book_of_Good_Counsels_Hitopadesa_Edwin_Arnold_1893.pdf"
    },
    {
        "id": "chanakya_niti_english_sutras",
        "title": "Chanakya Neeti - English Translation with Sutras (English Counterpart of Ka Chanakya Niti Darpana by Babu Jeebon Roy)",
        "author": "Chanakya / English Edition",
        "year": "2018",
        "ia_id": "chanakya-chanakya-neeti-2018",
        "filename": "Chanakya_Niti_English_Translation_With_Sutras.pdf"
    },
    {
        "id": "the_light_of_asia_buddha_arnold",
        "title": "The Light of Asia: Life and Teaching of Gautama Buddha (English Counterpart of Buddha Deb Charitra by Babu Jeebon Roy)",
        "author": "Sir Edwin Arnold",
        "year": "1890",
        "ia_id": "lightasia00arnogoog",
        "filename": "The_Light_of_Asia_Life_of_Buddha_Edwin_Arnold.pdf"
    },
    {
        "id": "julius_caesar_shakespeare",
        "title": "The Tragedy of Julius Caesar (English Original of Julius Caesar Drama by Frank M. Pugh)",
        "author": "William Shakespeare",
        "year": "1914",
        "ia_id": "tragedyofjuliusc00shakiala",
        "filename": "Julius_Caesar_Shakespeare_English_Original.pdf"
    },
    {
        "id": "as_you_like_it_shakespeare",
        "title": "As You Like It (English Original of As You Like It Drama by Frank M. Pugh)",
        "author": "William Shakespeare",
        "year": "1912",
        "ia_id": "asyoulikeit00shakiala",
        "filename": "As_You_Like_It_Shakespeare_English_Original.pdf"
    }
]

def download_item(item):
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

print("Starting download of classical source and counterpart translations...", flush=True)
count = 0
for it in classics:
    if download_item(it):
        count += 1

print(f"\nFinished: Verified {count}/{len(classics)} classical counterpart books.", flush=True)
