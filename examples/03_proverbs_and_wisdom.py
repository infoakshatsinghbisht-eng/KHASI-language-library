# -*- coding: utf-8 -*-
"""
Khasi Traditional Wisdom & Proverbs (Ki Ktien Tymmen):
Demonstrates querying, filtering, and studying Khasi moral philosophy and riddles.
"""

import sys
from pathlib import Path

# Add project root to sys.path
sys.path.insert(0, str(Path(__file__).parent.parent))

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

import khasi

def main():
    print("=" * 65)
    print("   Khasi: Traditional Proverbs (Ki Ktien Tymmen) & Riddles   ")
    print("=" * 65)

    all_proverbs = khasi.proverbs.all()
    print(f"\nLoaded {len(all_proverbs)} classical Khasi proverbs:\n")

    for i, p in enumerate(all_proverbs, 1):
        print(f"[{i}] {p['khasi']}")
        print(f"    Literal : {p.get('literal')}")
        print(f"    Meaning : {p.get('meaning')}")
        print(f"    Hindi   : {p.get('hindi')}\n")

    print("\nTraditional Khasi Riddles (Ki Jingkyntip):")
    for j, r in enumerate(khasi.riddles.all(), 1):
        print(f"\n  Riddle {j}: \"{r['riddle']}\"")
        print(f"  Hint    : {r['english_hint']}")
        print(f"  Solution: {r['solution']}")

    print("\n" + "=" * 65)

if __name__ == "__main__":
    main()
