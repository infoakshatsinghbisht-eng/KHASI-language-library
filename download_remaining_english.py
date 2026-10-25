import urllib.request
import urllib.parse
import json
import os
import ssl
import sys

ctx = ssl._create_unverified_context()
os.makedirs("data/english_books", exist_ok=True)

target_remaining = [
    {
        "id": "assam_gazetteer_khasi_jaintia_allen_1906",
        "title": "Assam District Gazetteer Vol X: The Khasi and Jaintia Hills",
        "author": "B. C. Allen",
        "year": "1906",
        "ia_id": "dli.ministry.07326",
        "filename": "Assam_District_Gazetteer_Vol_X_Khasi_Jaintia_BC_Allen_1906.pdf"
    },
    {
        "id": "govt_assam_khasi_jaintia_1915",
        "title": "The Khasi and Jaintia Hills, The Garo Hills Vol X",
        "author": "Govt of Assam",
        "year": "1915",
        "ia_id": "in.ernet.dli.2015.17076",
        "filename": "The_Khasi_and_Jaintia_Hills_Govt_Assam_1915.pdf"
    },
    {
        "id": "statistical_account_assam_khasi_jaintia_hunter",
        "title": "A Statistical Account of Assam Vol 2: Khasi and Jaintia Hills",
        "author": "Sir William Wilson Hunter",
        "year": "1879",
        "ia_id": "wbsl.19221",
        "preferred_pdf": "19221_text.pdf",
        "filename": "A_Statistical_Account_Of_Assam_Khasi_Jaintia_Hills_WW_Hunter.pdf"
    },
    {
        "id": "administration_report_khasi_jaintia_1876",
        "title": "Annual Report on the Administration of the Khasi and Jaintia Hills (1876-77)",
        "author": "Administration of Assam",
        "year": "1877",
        "ia_id": "wbsl.3048",
        "filename": "Administration_Report_Khasi_Jaintia_Hills_1876_1877.pdf"
    },
    {
        "id": "khasi_toponyms_linguistic_exploration",
        "title": "Naming the Land: Linguistic Exploration of Khasi Toponyms as Eco-Cultural Markers",
        "author": "Lenamiki Khonglah",
        "year": "2020",
        "ia_id": "21.-lenamiki-khonglah",
        "filename": "Naming_The_Land_Khasi_Toponyms_Linguistic_Exploration.pdf"
    },
    {
        "id": "social_history_khasi_jaintia_lyngdoh",
        "title": "Hospitals in the Khasi-Jaintia Hills: A Social History",
        "author": "Dr. Linda Bessy Lyngdoh",
        "year": "2015",
        "ia_id": "shg.701226-hospitals-in-the-khasi-jaintia-hills-in-the-twentieth-century-a-s",
        "filename": "Khasi_Jaintia_Hills_Social_History_Dr_Linda_Lyngdoh.pdf"
    },
    {
        "id": "handicrafts_women_khasi_ri_bhoi",
        "title": "Impact of Handloom and Handicrafts on Women in East Khasi Hills and Ri Bhoi",
        "author": "Deikimarkor Wahlang",
        "year": "2018",
        "ia_id": "sgng.19642-impact-of-the-handloom-and-handicrafts-industry-on-women-entrepre",
        "filename": "Handloom_Handicrafts_Khasi_Ri_Bhoi_Deikimarkor_Wahlang.pdf"
    },
    {
        "id": "education_mental_health_west_khasi_dkhar",
        "title": "Life Skills and Education in West Khasi Hills",
        "author": "Ainamlin Dkhar",
        "year": "2019",
        "ia_id": "shg.707511-life-skills-education-and-mental-health-among-high-school-student",
        "filename": "Education_West_Khasi_Hills_Ainamlin_Dkhar.pdf"
    },
    {
        "id": "phonology_of_khasi",
        "title": "Phonology of the Khasi Language",
        "author": "Phoible Project",
        "year": "1979",
        "ia_id": "kha_SPA1979_phon",
        "filename": "Phonology_of_the_Khasi_Language_Phoible.pdf"
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
            pref = item.get('preferred_pdf')
            if pref:
                for pf in pdf_files:
                    if pf.get('name') == pref:
                        chosen = pf
                        break
                        
            if not chosen:
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

print("Starting download of remaining English translation and companion books...", flush=True)
count = 0
for it in target_remaining:
    if download_item(it):
        count += 1

print(f"\nCompleted! Verified {count}/{len(target_remaining)} remaining books.", flush=True)
