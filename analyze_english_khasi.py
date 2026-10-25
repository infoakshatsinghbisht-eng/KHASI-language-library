import json
import os
import urllib.request

with open('found_english_khasi_books.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

print(f"Total found items: {len(items)}")

os.makedirs("data/english_books", exist_ok=True)

# Select key English books / English translations of Khasi literature / grammars / dictionaries / folklores
english_candidates = []

keywords = [
    'grammar', 'dictionary', 'folklore', 'folk-lore', 'folk-tales', 'tales',
    'khasis', 'bareh', 'gurdon', 'roberts', 'nissor', 'pilgrim', 'history',
    'customs', 'religion', 'culture', 'literature', 'lyngdoh', 'roy', 'singh'
]

for it in items:
    title = str(it.get('title', ''))
    creator = str(it.get('creator', ''))
    desc = str(it.get('description', ''))
    combined = (title + " " + creator + " " + desc).lower()
    
    # check if relevant
    score = sum(1 for kw in keywords if kw in combined)
    if score > 0:
        english_candidates.append({
            "identifier": it.get('identifier'),
            "title": title,
            "creator": creator,
            "year": it.get('year'),
            "score": score
        })

# Sort by relevance score
english_candidates.sort(key=lambda x: x['score'], reverse=True)

print(f"\nTop English counterparts & references ({len(english_candidates)} found):")
for c in english_candidates[:30]:
    print(f"[{c['score']}] {c['identifier']}: {c['title']} by {c['creator']} ({c['year']})")

with open("english_khasi_candidates.json", "w", encoding="utf-8") as f:
    json.dump(english_candidates, f, indent=2, ensure_ascii=False)
