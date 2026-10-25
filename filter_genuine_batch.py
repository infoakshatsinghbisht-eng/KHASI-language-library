# -*- coding: utf-8 -*-
import json
import re
from pathlib import Path

WORKSPACE_DIR = Path(r"c:\Users\digit_lgfi273\OneDrive\Desktop\pykhasi")
CANDIDATES_FILE = WORKSPACE_DIR / "undiscovered_khasi_candidates.json"

with open(CANDIDATES_FILE, encoding='utf-8') as f:
    items = json.load(f)

print(f"Total candidates to filter: {len(items)}")

non_khasi_tokens = [
    'ibn', 'syarhil', 'al-', 'dor al', 'tareeq', 'giflaf', 'kaba', 'shabeer',
    'genghis', 'pdfbooksfree', 'swachh', 'kalpana', 'lougan', 'sarbaz', 'khaste',
    'khasais', 'bait al', 'awara', 'badshah', 'kandari', 'dr bhandarkar',
    'vuong', 'vietnamese', 'arabic', 'persian', 'urdu', 'hindi', 'bangla',
    'marathi', 'tamil', 'telugu', 'kannada', 'malayalam', 'sanskrit',
    'bukhari', 'hadith', 'islam', 'quran', 'fiqh', 'surah', 'prophet', 'janwar'
]

genuine = []

for item in items:
    title = str(item.get('title', '')).strip()
    ident = str(item.get('identifier', '')).strip()
    creator = str(item.get('creator', '')).strip()
    desc = str(item.get('description', '')).strip()
    lang = str(item.get('language', '')).strip().lower()

    combined = f"{title.lower()} {ident.lower()} {creator.lower()} {desc.lower()}"

    if any(tok in combined for tok in non_khasi_tokens):
        continue

    # Must have positive evidence
    has_evidence = False
    if 'kha' in lang:
        has_evidence = True
    elif '464' in ident:
        has_evidence = True
    elif any(k in combined for k in [
        'khasi', 'khassi', 'khasia', 'cossyah', 'sohra', 'cherra', 'shillong',
        'meghalaya', 'pnar', 'synteng', 'jaintia', 'hynniewtrep', 'ka niam',
        'kot pule', 'jingsneng', 'khanatang', 'soso tham', 'jeebon roy',
        'radhon singh', 'welsh mission', 'thomas jones'
    ]):
        has_evidence = True
    elif any(k in creator.lower() for k in [
        'lyngdoh', 'sten', 'tham', 'roy', 'bareh', 'laloo', 'dkhar', 'marbaniang',
        'syiem', 'kharkongor', 'warjri', 'nongrum', 'mawrie', 'pugh', 'roberts', 'hooker'
    ]):
        has_evidence = True

    if has_evidence:
        genuine.append(item)

print(f"Retained genuine candidates: {len(genuine)}")

out_path = WORKSPACE_DIR / "verified_batch_candidates.json"
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(genuine, f, indent=2, ensure_ascii=False)

for idx, g in enumerate(genuine[:30], 1):
    print(f"{idx}. [{g['identifier']}] {g['title']} ({g.get('year')}) by {g['creator']}")
