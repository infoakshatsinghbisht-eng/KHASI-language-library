import urllib.request
import urllib.parse
import json
import os
import ssl

ctx = ssl._create_unverified_context()
os.makedirs("data/english_books", exist_ok=True)

items = [
    {
        "ia_id": "tragedyofjuliusc00shakiala",
        "title": "The Tragedy of Julius Caesar",
        "filename": "Julius_Caesar_Shakespeare_English_Original.pdf"
    },
    {
        "ia_id": "asyoulikeit00shakiala",
        "title": "As You Like It",
        "filename": "As_You_Like_It_Shakespeare_English_Original.pdf"
    }
]

for it in items:
    out_path = os.path.join("data/english_books", it["filename"])
    if os.path.exists(out_path) and os.path.getsize(out_path) > 50000:
        print(f"[EXISTS] {it['filename']} ({os.path.getsize(out_path)/1024/1024:.2f} MB)", flush=True)
        continue
    
    print(f"Fetching metadata for {it['ia_id']}...", flush=True)
    meta_url = f"https://archive.org/metadata/{it['ia_id']}"
    try:
        req = urllib.request.Request(meta_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx, timeout=20) as r:
            meta = json.loads(r.read())
        pdf_files = [f for f in meta.get('files', []) if f.get('name', '').endswith('.pdf') and not f.get('name', '').endswith('_bw.pdf')]
        if not pdf_files:
            pdf_files = [f for f in meta.get('files', []) if f.get('name', '').endswith('.pdf')]
        pdf = pdf_files[0]['name']
        dl_url = f"https://archive.org/download/{it['ia_id']}/{urllib.parse.quote(pdf)}"
        print(f"Downloading {pdf} -> {it['filename']}...", flush=True)
        dl_req = urllib.request.Request(dl_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(dl_req, context=ctx, timeout=120) as resp, open(out_path, 'wb') as f:
            while True:
                chunk = resp.read(128 * 1024)
                if not chunk:
                    break
                f.write(chunk)
        print(f"[SUCCESS] {it['filename']} ({os.path.getsize(out_path)/1024/1024:.2f} MB)", flush=True)
    except Exception as e:
        print(f"Error for {it['ia_id']}: {e}", flush=True)

print("Finished downloading Shakespeare originals!", flush=True)
