# -*- coding: utf-8 -*-
r"""Khasi CLI tool with UTF-8 support on all platforms."""

import sys
import argparse

# Ensure UTF-8 output on Windows consoles
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

import khasi

def main():
    parser = argparse.ArgumentParser(
        prog="khasi",
        description="Khasi (Ka Ktien Khasi) Language Library & Multi-Dialect Tool (Meghalaya, Northeast India)"
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # translate
    t_parser = subparsers.add_parser("translate", help="Translate English/Hindi/Hinglish to Khasi")
    t_parser.add_argument("text", type=str, help="Text to translate")
    t_parser.add_argument("--dialect", "-d", type=str, default="sohra",
                          choices=["sohra", "shillong", "pnar", "war", "bhoi"],
                          help="Khasi dialect variant")

    # lookup
    l_parser = subparsers.add_parser("lookup", help="Look up a Khasi word")
    l_parser.add_argument("word", type=str, help="Word to look up")

    # num
    n_parser = subparsers.add_parser("num", help="Convert numbers to Khasi words")
    n_parser.add_argument("value", type=int, help="Integer value")

    # culture
    c_parser = subparsers.add_parser("culture", help="Explore Khasi culture, proverbs, seasons, and market days")

    # conjugate
    v_parser = subparsers.add_parser("conjugate", help="Conjugate a Khasi verb")
    v_parser.add_argument("verb", type=str, help="Verb root (e.g. wan, leit, bam)")
    v_parser.add_argument("--tense", "-t", type=str, default="present",
                          choices=["present", "past", "future", "future_definite", "habitual"],
                          help="Grammatical tense")
    v_parser.add_argument("--pronoun", "-p", type=str, default="nga",
                          help="Subject pronoun (nga, ngi, phi, u, ka, ki)")

    # riddle
    r_parser = subparsers.add_parser("riddle", help="Get a traditional Khasi riddle (Ki Jingkyntip)")

    # stats
    s_parser = subparsers.add_parser("stats", help="Display Khasi corpus & morphological stats")

    args = parser.parse_args()

    if args.command == "translate":
        res = khasi.translate(args.text, dialect=args.dialect)
        print(f"\nKhasi [{res.dialect}]: {res.text}")
        print(f"Confidence: {res.confidence * 100:.1f}% | Target: {res.target_lang}")

    elif args.command == "lookup":
        d = khasi.lookup(args.word)
        if d:
            print(f"\nWord: {d.get('khasi', args.word)}")
            print(f"Hindi: {d.get('hindi', 'N/A')}")
            print(f"English: {d.get('english', 'N/A')}")
            print(f"POS: {d.get('pos', 'N/A')}")
            if "gender" in d:
                print(f"Gender/Article: {d['gender']}")
            if "dialect_variants" in d:
                print(f"Dialects: {d['dialect_variants']}")
            if "note" in d:
                print(f"Note: {d['note']}")
        else:
            print(f"Word '{args.word}' not found in dictionary.")

    elif args.command == "num":
        w = khasi.num_to_words(args.value)
        o = khasi.ordinal(args.value)
        print(f"\nNumber: {args.value}")
        print(f"Khasi words: {w}")
        print(f"Ordinal: {o}")

    elif args.command == "culture":
        s = khasi.get_current_season()
        m = khasi.get_current_khasi_month()
        print(f"\nCurrent Season (Aïom): {s.get('name_khasi')} ({s.get('name_hindi')}) - {s.get('english_season')}")
        print(f"Traditional Month (Bnai): {m.get('name')} - {m.get('english')} ({m.get('meaning')})")
        print("\nRandom Khasi Proverb (Ki Ktien Tymmen):")
        p = khasi.proverbs.random()
        if p:
            print(f"  \"{p.get('khasi')}\"")
            print(f"  Literal: {p.get('literal')}")
            print(f"  Meaning: {p.get('meaning')}")

    elif args.command == "conjugate":
        result = khasi.conjugate(args.verb, tense=args.tense, pronoun=args.pronoun)
        print(f"\nConjugation ({args.tense}, {args.pronoun}):")
        print(f"  {result}")

    elif args.command == "riddle":
        r = khasi.riddles.random()
        if r:
            print(f"\nTraditional Khasi Riddle:")
            print(f"  \"{r.get('riddle')}\"")
            print(f"  Hint: {r.get('english_hint')}")
            print(f"  Solution: {r.get('solution')}")

    elif args.command == "stats":
        dict_size = len(khasi.KhasiDictionary()._words)
        total_forms = khasi.total_word_forms()
        print("\nKhasi Language Library Statistics:")
        print(f"  ISO 639-3 Code: {khasi.ISO_639_3}")
        print(f"  Native Name: {khasi.NATIVE_NAME}")
        print(f"  Base Dictionary Entries: {dict_size:,} headwords (1 Lakh+)")
        print(f"  Morphological Universe: {total_forms:,}+ inflections & derivations")
        print(f"  Dialects Supported: Sohra, Shillong, Pnar, War, Bhoi, Maram")
        print(f"  Alphabet letters: {len(khasi.KHASI_ALPHABET)}")
        print(f"  Festivals documented: {len(khasi.list_festivals())}")
        print(f"  Traditional market days: {len(khasi.MARKET_CYCLE)}")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
