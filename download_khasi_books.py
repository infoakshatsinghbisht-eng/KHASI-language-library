# -*- coding: utf-8 -*-
"""
Wikimedia Commons Khasi Books Downloader.

Downloads digitized Khasi books from:
- Category:Khasi-language_books
- Category:Books in Khasi digitised under CIS-A2K NECTAR Project

Saves directly to: C:\\Users\\digit_lgfi273\\Downloads\\Khasi_Books
"""

import sys
import os
import json
import ssl
import urllib.request
from pathlib import Path

TARGET_DIR = Path(r"C:\Users\digit_lgfi273\Downloads\Khasi_Books")
TARGET_DIR.mkdir(parents=True, exist_ok=True)

JSON_FILE = Path(__file__).resolve().parent / "wikimedia_khasi_books.json"

import time

def download_book(title: str, url: str, size_mb: float, max_retries: int = 3):
    # Sanitize filename
    clean_name = title.strip(". ")
    dest = TARGET_DIR / clean_name
    if dest.exists() and dest.stat().st_size > 10000:
        print(f"[Already Exists] {clean_name} ({dest.stat().st_size / (1024*1024):.2f} MB)")
        return True

    print(f"[Downloading] {clean_name} ({size_mb:.2f} MB)...")
    ctx = ssl._create_unverified_context()
    headers = {
        "User-Agent": "KhasiLanguagePreservation/1.0 (https://github.com/infoakshatsinghbisht-eng/KHASI-language-library; infoakshatsinghbisht@gmail.com)"
    }

    for attempt in range(1, max_retries + 1):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, context=ctx, timeout=120) as resp:
                content = resp.read()
            with open(dest, "wb") as f:
                f.write(content)
            print(f"[Complete] Saved to {dest}")
            time.sleep(3)  # Respectful pause for Wikimedia
            return True
        except urllib.error.HTTPError as e:
            if e.code == 429:
                wait_sec = attempt * 5
                print(f"[Rate-limited 429] Waiting {wait_sec}s before retry {attempt}/{max_retries}...")
                time.sleep(wait_sec)
            else:
                print(f"[HTTP Error] {e.code} for {clean_name}: {e.reason}")
                break
        except Exception as e:
            print(f"[Error] Failed to download {clean_name}: {e}")
            time.sleep(2)

    return False

def main():
    if not JSON_FILE.exists():
        print(f"Error: {JSON_FILE} not found.")
        return

    with open(JSON_FILE, "r", encoding="utf-8") as f:
        books = json.load(f)

    print(f"Loaded {len(books)} books available from Wikimedia Commons.")
    print(f"Destination folder: {TARGET_DIR}\n")

    # If user specifies specific indices or "all"
    args = sys.argv[1:]
    if not args:
        # Default: download top 6 foundational cultural and literary books (< 10 MB each)
        print("No arguments provided. Downloading 6 foundational literary and cultural classics...")
        selected_titles = [
            "Ka-Drama-U-Mihsngi--Da-U-Mondon-Bareh.pdf",
            "U-Khasi-Hyndai.pdf",
            "Ki Khasi Poems Ne Ki Sur Khasi.pdf",
            "Ka-Niam-ki-khasi-Ka-Niam-Tip-blei-tip-brieu-Ed-1st.pdf",
            "Ka Kot Pule Ka Balai (Khasi Third Reader).pdf",
            "KA MYNTOI.pdf"
        ]
        for b in books:
            if b["title"] in selected_titles:
                download_book(b["title"], b["url"], b["size_mb"])
    elif args[0].lower() == "all":
        print(f"Downloading ALL {len(books)} books...")
        for b in books:
            download_book(b["title"], b["url"], b["size_mb"])
    else:
        # Query match
        query = " ".join(args).lower()
        matched = [b for b in books if query in b["title"].lower()]
        print(f"Found {len(matched)} books matching '{query}':")
        for b in matched:
            download_book(b["title"], b["url"], b["size_mb"])

if __name__ == "__main__":
    main()
