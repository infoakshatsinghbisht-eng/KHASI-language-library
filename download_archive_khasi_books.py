# -*- coding: utf-8 -*-
"""
Download newly discovered Digital Library of India (DLI) Khasi books from Internet Archive
that were previously listed as 'No public scan verified' in the spreadsheet!
"""

import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
import urllib.request
import json
import ssl
from pathlib import Path
import time

TARGET_DIR = Path(r"C:\Users\digit_lgfi273\Downloads\Khasi_Books")
TARGET_DIR.mkdir(parents=True, exist_ok=True)

ctx = ssl._create_unverified_context()
headers = {"User-Agent": "KhasiPreservationDownloader/1.0 (infoakshatsinghbisht@gmail.com)"}

DLI_ITEMS = [
    ("in.ernet.dli.2015.464867", "Ka Jingsneng Tymmen Part 1 - Radhon Singh Berry"),
    ("in.ernet.dli.2015.464842", "Ka Jingsneng Tymmen Part 2 - Radhon Singh Berry"),
    ("in.ernet.dli.2015.464818", "U Raikut - Streamlet Dkhar"),
    ("in.ernet.dli.2015.464777", "Na Khriang Ka Dohnud - Streamlet Dkhar"),
    ("in.ernet.dli.2015.464771", "Na Lyngwiar Dpei I Mei - Streamlet Dkhar"),
    ("in.ernet.dli.2015.464713", "Ki Umjer Rupa - Streamlet Dkhar"),
    ("in.ernet.dli.2015.464558", "Ka Jinglong Tynrai U Briew Kat Kum Ki Drama Khasi - Streamlet Dkhar"),
    ("in.ernet.dli.2015.464375", "Ki Sur Na Ka Duitara Ksiar - H.W. Sten"),
    ("in.ernet.dli.2015.464406", "I Mabah Soso Tham - Minette Sibon Tham"),
    ("in.ernet.dli.2015.464378", "U Soso Tham Bad Ki Jingtrei Jong U - Hughlet Warjri"),
    ("in.ernet.dli.2015.464905", "Ka Meiramew Bad U Hynniewtrep - Bevan L. Swer"),
    ("in.ernet.dli.2015.464724", "Ki Symboh History Bad Ka Ri Hynniewtrep - L. Gilbert Shullai"),
    ("in.ernet.dli.2015.464687", "Ki Bor Phylla U Hynniewtrep - Donbok T. Laloo"),
    ("in.ernet.dli.2015.464614", "Ka Ri Hynniewtrep Bad Ka Sixth Schedule - L. Gilbert Shullai"),
    ("in.ernet.dli.2015.464637", "Ka Niam Khasi Tynrai Ha Ka Dur Ka Niam Khristan - S. Synrang Khonglah"),
    ("in.ernet.dli.2015.464929", "Shaphang U Wai U Blai - Jeebon Roy")
]

def get_best_pdf(ident):
    meta_url = f"https://archive.org/metadata/{ident}"
    req = urllib.request.Request(meta_url, headers=headers)
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            files = data.get("files", [])
            pdfs = [f for f in files if f.get("name", "").endswith(".pdf")]
            # prefer text.pdf or smallest valid pdf
            if not pdfs:
                return None
            # Sort: prefer _text.pdf if exists, else first
            text_pdfs = [f for f in pdfs if "_text.pdf" in f["name"]]
            chosen = text_pdfs[0] if text_pdfs else pdfs[0]
            return chosen["name"]
    except Exception as e:
        print(f"Error fetching metadata for {ident}: {e}")
        return None

def download_file(ident, pdf_name, label):
    clean_label = "".join(c for c in label if c.isalnum() or c in " -_().").strip()
    dest = TARGET_DIR / f"{clean_label}.pdf"
    if dest.exists() and dest.stat().st_size > 10000:
        print(f"[Already Exists] {dest.name} ({dest.stat().st_size / (1024*1024):.2f} MB)")
        return True

    url = f"https://archive.org/download/{ident}/{pdf_name}"
    print(f"[Downloading] {label} from {url}...")
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=90) as resp:
            data = resp.read()
        with open(dest, "wb") as f:
            f.write(data)
        print(f"[Complete] Saved {dest.name} ({len(data) / (1024*1024):.2f} MB)")
        time.sleep(2)
        return True
    except Exception as e:
        print(f"[Failed] {label}: {e}")
        return False

def main():
    print(f"Starting download of {len(DLI_ITEMS)} newly discovered Khasi books from Archive.org...")
    success = 0
    for ident, label in DLI_ITEMS:
        pdf_name = get_best_pdf(ident)
        if pdf_name:
            if download_file(ident, pdf_name, label):
                success += 1
        else:
            print(f"[No PDF] for {label} ({ident})")
    print(f"\nFinished: Successfully downloaded {success}/{len(DLI_ITEMS)} books into {TARGET_DIR}")

if __name__ == "__main__":
    main()
