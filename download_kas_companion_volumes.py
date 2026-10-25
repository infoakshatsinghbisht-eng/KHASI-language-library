import urllib.request
import urllib.parse
import json
import os
import ssl

ctx = ssl._create_unverified_context()

os.makedirs("data/khasi_books", exist_ok=True)
os.makedirs("data/english_books", exist_ok=True)

items = [
    {
        "ia_id": "in.ernet.dli.2015.464680",
        "title": "Ka Thiar Ki Nongthoh Vol. 3 (Khasi Authors Society)",
        "dest": "data/khasi_books",
        "filename": "Ka_Thiar_Ki_Nongthoh_Vol_3_KAS_464680.pdf"
    },
    {
        "ia_id": "in.ernet.dli.2015.464629",
        "title": "Ka Thiar Ki Nongthoh Vol. 5 (Khasi Authors Society)",
        "dest": "data/khasi_books",
        "filename": "Ka_Thiar_Ki_Nongthoh_Vol_5_KAS_464629.pdf"
    },
    {
        "ia_id": "in.ernet.dli.2015.464781",
        "title": "Khasi Authors Society Silver Jubilee 1979-2004",
        "dest": "data/khasi_books",
        "filename": "Khasi_Authors_Society_Silver_Jubilee_2004_464781.pdf"
    },
    {
        "ia_id": "in.ernet.dli.2015.464651",
        "title": "Ka Syngkhong Jingtip Vol. 2 (Academy of Knowledge)",
        "dest": "data/khasi_books",
        "filename": "Ka_Syngkhong_Jingtip_Vol_2_464651.pdf"
    },
    {
        "ia_id": "in.ernet.dli.2015.464891",
        "title": "Ka Kolshor U Khasi (Khasi Culture)",
        "dest": "data/khasi_books",
        "filename": "Ka_Kolshor_U_Khasi_1983_464891.pdf"
    }
]

for it in items:
    out_path = os.path.join(it["dest"], it["filename"])
    if os.path.exists(out_path) and os.path.getsize(out_path) > 30000:
        print(f"[EXISTS] {it['filename']} ({os.path.getsize(out_path)/1024/1024:.2f} MB)", flush=True)
        continue
        
    print(f"\n[QUERY] Fetching metadata for {it['ia_id']} ({it['title']})...", flush=True)
    meta_url = f"https://archive.org/metadata/{it['ia_id']}"
    try:
        req = urllib.request.Request(meta_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx, timeout=15) as r:
            meta = json.loads(r.read().decode('utf-8'))
        pdf_files = [f for f in meta.get('files', []) if f.get('name', '').endswith('.pdf') and not f.get('name', '').endswith('_bw.pdf')]
        if not pdf_files:
            pdf_files = [f for f in meta.get('files', []) if f.get('name', '').endswith('.pdf')]
        if not pdf_files:
            print(f"[SKIP] No PDF in {it['ia_id']}", flush=True)
            continue
            
        pdf = pdf_files[0]['name']
        size_mb = int(pdf_files[0].get('size', 0)) / 1024 / 1024
        dl_url = f"https://archive.org/download/{it['ia_id']}/{urllib.parse.quote(pdf)}"
        print(f"Downloading {pdf} ({size_mb:.2f} MB) -> {it['filename']}...", flush=True)
        dl_req = urllib.request.Request(dl_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(dl_req, context=ctx, timeout=180) as resp, open(out_path, 'wb') as f:
            while True:
                chunk = resp.read(128 * 1024)
                if not chunk:
                    break
                f.write(chunk)
        print(f"[SUCCESS] Downloaded {it['filename']} ({os.path.getsize(out_path)/1024/1024:.2f} MB)", flush=True)
    except Exception as e:
        print(f"Error for {it['ia_id']}: {e}", flush=True)

print("\nFinished downloading KAS and companion volumes!", flush=True)
