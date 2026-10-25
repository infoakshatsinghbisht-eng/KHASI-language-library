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

    # book
    b_parser = subparsers.add_parser("book", help="Read, browse, and search 1,200 digitized Khasi books (each page with content)")
    b_sub = b_parser.add_subparsers(dest="book_command", help="Book subcommands")

    # book list
    bl_parser = b_sub.add_parser("list", help="List all digitized books")
    bl_parser.add_argument("--limit", "-l", type=int, default=30, help="Maximum books to display")

    # book read
    br_parser = b_sub.add_parser("read", help="Read a specific book page or full book")
    br_parser.add_argument("book", type=str, help="Book ID or title (e.g. u_tirot_singh, ah_kordit_ianga)")
    br_parser.add_argument("--page", "-p", type=int, default=1, help="Page number (1-indexed)")
    br_parser.add_argument("--full", "-f", action="store_true", help="Print entire unpaginated book content")

    # book full
    bf_parser = b_sub.add_parser("full", help="Print the entire unpaginated text of a book")
    bf_parser.add_argument("book", type=str, help="Book ID or title")

    # book compendium
    bc_parser = b_sub.add_parser("compendium", help="Display paths to master single-document book compendiums")

    # book search
    bs_parser = b_sub.add_parser("search", help="Search text across all books and all pages")
    bs_parser.add_argument("query", type=str, help="Search keyword or phrase")
    bs_parser.add_argument("--limit", "-l", type=int, default=10, help="Maximum results to return")


    # grammar
    g_parser = subparsers.add_parser("grammar", help="Query and inspect 90 classical Khasi grammar rules (Ka Riti Ktien)")
    g_parser.add_argument("query", type=str, nargs="?", default=None, help="Rule ID (e.g. AGR-01, CLS-01) or search term")
    g_parser.add_argument("--category", "-c", type=str, default=None, help="Filter rules by category")
    g_parser.add_argument("--summary", "-s", action="store_true", help="Show summary of grammar rules")

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
        cat_summary = khasi.catalogue.summary()
        gram_summary = khasi.grammar_rules.summary()
        print("\nKhasi Language Library Statistics:")
        print(f"  ISO 639-3 Code: {khasi.ISO_639_3}")
        print(f"  Native Name: {khasi.NATIVE_NAME}")
        print(f"  Base Dictionary Entries: {dict_size:,} headwords (5 Lakh+)")
        print(f"  Morphological Universe: {total_forms:,}+ inflections & derivations")
        print(f"  Digitized Whole Books: {khasi.total_books():,} books ({khasi.total_pages():,} pages, {khasi.total_words():,} words)")
        import glob
        pdf_count = len(glob.glob("data/khasi_books/*.pdf"))
        print(f"  Preserved PDF Editions: {pdf_count:,} complete scans & editions in data/khasi_books/")
        print(f"  Classical Grammar Engine: {gram_summary['total_rules']} formal rules across {gram_summary['categories_count']} categories")
        print(f"  Master Bibliography Catalogue: {cat_summary['total_works']} catalogued books & works")
        print(f"  Dialects Supported: Sohra, Shillong, Pnar, War, Bhoi, Maram")
        print(f"  Alphabet letters: {len(khasi.KHASI_ALPHABET)}")
        print(f"  Festivals documented: {len(khasi.list_festivals())}")
        print(f"  Traditional market days: {len(khasi.MARKET_CYCLE)}")

    elif args.command == "catalogue":
        if args.digitized:
            results = khasi.catalogue.digitized()
        elif args.genre:
            results = khasi.catalogue.by_genre(args.genre)
        elif args.author:
            results = khasi.catalogue.by_author(args.author)
        elif args.query:
            results = khasi.catalogue.search(args.query)
        else:
            summary = khasi.catalogue.summary()
            print("\n📚 Master Khasi Bibliography & Corpus Catalogue:")
            print(f"  Total Catalogued Works: {summary['total_works']}")
            print(f"  Digitized Scans Available: {summary['digitized_works_count']}")
            print("\nGenres:")
            for g, count in summary["genres"].items():
                print(f"  - {g}: {count} works")
            print("\nTop Khasi Authors:")
            for a, count in summary["top_authors"][:6]:
                print(f"  - {a} ({count} works)")
            print("\nRun 'khasi catalogue <query>' or 'khasi catalogue --author <name>' to explore.")
            return

        print(f"\nFound {len(results)} works in catalogue:")
        for w in results[:20]:
            year = f" ({w['year']})" if "year" in w else ""
            dig = " [DIGITIZED PDF]" if w.get("digitized") else ""
            print(f"  #{w['id']} - \"{w['title']}\" by {w['author']}{year} [{w['type']}]{dig}")
        if len(results) > 20:
            print(f"  ... and {len(results) - 20} more works.")

    elif args.command == "book":
        if args.book_command == "list":
            all_b = khasi.list_books()
            print(f"\n📚 Digitized Khasi Books Library ({len(all_b)} books available directly):")
            for b in all_b[:args.limit]:
                author = b.get("author", "Unknown")
                if isinstance(author, list):
                    author = ", ".join(author)
                print(f"  [{b['id']}] {b['title']} - {author} ({b.get('total_pages', 0)} pages, {b.get('total_words', 0):,} words)")
            if len(all_b) > args.limit:
                print(f"  ... and {len(all_b) - args.limit} more books. Use 'khasi book list --limit {len(all_b)}' to view all.")

        elif args.book_command in ("read", "full"):
            bk = khasi.get_book(args.book)
            if not bk:
                print(f"Error: Book '{args.book}' not found in library.")
                return
            author = bk.author if isinstance(bk.author, str) else ", ".join(bk.author)
            
            # Full book mode
            if getattr(args, "full", False) or args.book_command == "full":
                print(f"\n📖 {bk.title} - {author}")
                print(f"Total Pages: {bk.total_pages} | Total Words: {bk.total_words:,}")
                print("=" * 80 + "\n")
                print(bk.full_text)
                print("\n" + "=" * 80)
                return

            # Page-by-page mode
            page_text = bk.get_page(args.page)
            if page_text is None:
                print(f"Error: Book '{bk.title}' only has {bk.total_pages} pages (requested page {args.page}).")
                return
            print(f"\n📖 {bk.title} - {author}")
            print(f"--- [Page {args.page} of {bk.total_pages}] ---")
            print(page_text)
            print(f"--- [End of Page {args.page}] ---")

        elif args.book_command == "compendium":
            pure_txt = khasi.get_pure_khasi_master_text_path()
            pure_jsonl = khasi.get_pure_khasi_master_jsonl_path()
            txt_path = khasi.get_master_compendium_path()
            jsonl_path = khasi.get_master_jsonl_path()
            print("\n📚 Master Whole-Library Compendium Documents:")
            print("\n  =======================================================")
            print("  🌟 [1] PURE KHASI MONOLINGUAL BOOKS (Ka Ktien Khasi Only)")
            print("         (Excludes English treatises, translations, & other languages)")
            print("  =======================================================")
            print("    Total Pure Khasi Books: 1,076 books")
            print("    Total Pure Khasi Words: 26,710,688 words (104,364 pages)")
            print(f"    Plain-Text Document:    {pure_txt}")
            if pure_txt.exists():
                print(f"      Size: {pure_txt.stat().st_size:,} bytes (~137.9 MB)")
            print(f"    JSONL Dataset:          {pure_jsonl}")
            if pure_jsonl.exists():
                print(f"      Size: {pure_jsonl.stat().st_size:,} bytes (~137.8 MB)")
            print("    Individual Books Dir:   data/pure_khasi_books_txt/ (1,076 individual .txt files)")

            print("\n  -------------------------------------------------------")
            print("  📖 [2] COMPLETE ALL-INCLUSIVE ARCHIVE (Includes English Treatises)")
            print("  -------------------------------------------------------")
            print(f"    Total Books:            {khasi.total_books():,} books")
            print(f"    Total Words:            {khasi.total_words():,} words ({khasi.total_pages():,} pages)")
            print(f"    Plain-Text Document:    {txt_path}")
            if txt_path.exists():
                print(f"      Size: {txt_path.stat().st_size:,} bytes (~174.3 MB)")
            print(f"    JSONL Dataset:          {jsonl_path}")
            if jsonl_path.exists():
                print(f"      Size: {jsonl_path.stat().st_size:,} bytes (~174.2 MB)")
            print("    Individual Books Dir:   data/khasi_books_txt/ (1,232 individual .txt files)")


        elif args.book_command == "search":
            results = khasi.search_books(args.query, max_results_per_book=2)
            print(f"\n🔍 Search results for '{args.query}' across {khasi.total_books()} books ({len(results)} matches):")
            for r in results[:args.limit]:
                print(f"  [{r['title']} - Page {r['page_number']}]:")
                print(f"    {r['snippet']}")
            if len(results) > args.limit:
                print(f"  ... and {len(results) - args.limit} more matches.")
        else:
            b_parser.print_help()


    elif args.command == "grammar":
        if args.summary:
            s = khasi.grammar_rules.summary()
            print("\n📐 Classical Khasi Grammar Rules Engine (Ka Riti Ktien):")
            print(f"  Total Catalogued Rules: {s['total_rules']}")
            print(f"  Categories ({s['categories_count']}):")
            for cat, cnt in s["categories"].items():
                print(f"    - {cat}: {cnt} rules")
            print("\nSources:")
            for src in s["sources"]:
                print(f"    * {src}")
            return

        if args.category:
            rules = khasi.grammar_rules.by_category(args.category)
            print(f"\n📐 Khasi Grammar Rules in '{args.category}' ({len(rules)} rules):")
            for r in rules:
                print(f"  [{r.id}] {r.name}")
                print(f"    Formula: {r.formula}")
                print(f"    Example: {r.khasi_examples[0] if r.khasi_examples else 'N/A'}")
            return

        if args.query:
            # Check direct ID
            single = khasi.grammar_rules.get(args.query)
            if single:
                print(f"\n📐 [{single.id}] {single.name} ({single.category})")
                print(f"  Formula:     {single.formula}")
                print(f"  Description: {single.description}")
                print("  Examples:")
                for ex, tr in zip(single.khasi_examples, single.english_translations):
                    print(f"    * Khasi:   {ex}")
                    print(f"      English: {tr}")
                print(f"  Reference:   {single.source_reference}")
                return

            # Search keyword
            results = khasi.grammar_rules.search(args.query)
            print(f"\n🔍 Search results for grammar keyword '{args.query}' ({len(results)} rules):")
            for r in results:
                print(f"  [{r.id}] {r.name} ({r.category})")
                print(f"    Formula: {r.formula}")
            return

        # Default: list all rules
        all_r = khasi.grammar_rules.all()
        print(f"\n📐 Classical Khasi Grammar Rules Engine ({len(all_r)} rules available):")
        for r in all_r:
            print(f"  [{r.id}] {r.name} - {r.category}")
        print("\nUse 'khasi grammar <RULE-ID>' (e.g. khasi grammar AGR-01) for rule details.")
        print("Use 'khasi grammar --category <CATEGORY>' or 'khasi grammar <keyword>' to search.")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
