# -*- coding: utf-8 -*-
"""
Build Khasi Books Dataset for khasi.culture.books.
Extracts whole book data (every single page) for 24 foundational Khasi books:
- 9 Classical Works from OCR/Text Preservation
- 15 Digitized Books from DLI/Internet Archive PDFs
"""

import sys
import json
import re
from pathlib import Path
import pypdf

WORKSPACE_DIR = Path(__file__).resolve().parent
BOOKS_DATA_DIR = WORKSPACE_DIR / "khasi" / "culture" / "data" / "books"
PDF_DIR = WORKSPACE_DIR / "data" / "khasi_books"
if not PDF_DIR.exists():
    _fallback = Path.home() / "Downloads" / "Khasi_Books"
    if _fallback.exists():
        PDF_DIR = _fallback

def paginate_text(text: str, target_words: int = 350) -> list:
    """Split text into logical book pages along paragraph boundaries."""
    paragraphs = text.split("\n\n")
    pages = []
    curr_paras = []
    curr_words = 0

    for p in paragraphs:
        p_clean = p.strip()
        if not p_clean:
            continue
        p_words = len(p_clean.split())
        if curr_words + p_words > target_words and curr_paras:
            page_text = "\n\n".join(curr_paras)
            pages.append({
                "page_number": len(pages) + 1,
                "text": page_text,
                "word_count": len(page_text.split())
            })
            curr_paras = [p_clean]
            curr_words = p_words
        else:
            curr_paras.append(p_clean)
            curr_words += p_words

    if curr_paras:
        page_text = "\n\n".join(curr_paras)
        pages.append({
            "page_number": len(pages) + 1,
            "text": page_text,
            "word_count": len(page_text.split())
        })

    return pages

# 1. Classical Text Books from Workspace Root
TEXT_BOOKS = [
    {
        "id": "ka_niam_ki_khasi",
        "title": "Ka Niam Ki Khasi: Ka Niam Tip-Blei Tip-Briew",
        "native_title": "Ka Niam Ki Khasi: Ka Niam Tip-Blei Tip-Briew",
        "author": "U Sib Charan Roy",
        "year": 1919,
        "genre": "Theology & Indigenous Religion",
        "file": "book_niam_khasi.txt",
        "description": "Foundational theological and philosophical text articulating the original Khasi monotheistic religion, the moral covenant of Hok, and ancestor veneration.",
        "chapters": [
            "Ka Jingbatai Shaphang U Blei Nongbuh Nongthaw",
            "Ka Niam Tip-Blei Tip-Briew bad Tip-Kur Tip-Kha",
            "Ka Hok bad Ka Pop ha Ka Niam Khasi",
            "Ki Kñia ki Khriam bad ki Khan-Sngi",
            "Ka Jingshongkha Shongman katkum Ka Niam",
            "Ka Jer ka Thoh bad Ka Jingpynkhein Niam"
        ]
    },
    {
        "id": "u_khasi_hyndai",
        "title": "U Khasi Hyndai",
        "native_title": "U Khasi Hyndai",
        "author": "Dr. H. Lyngdoh",
        "year": 1938,
        "genre": "Anthropology & Cultural History",
        "file": "book_khasi_hyndai.txt",
        "description": "Exhaustive cultural and historical treatise examining the ancient social institutions, megalithic culture (Mawbynna), chieftainship, and clans of the Khasi people.",
        "chapters": [
            "Ka Thymmei U Hynniewtrep",
            "Ki Mawbynna bad Ki Megalith ha Ka Ri Khasi",
            "Ka Jingpyniaid Himah bad Ki Syiem Khasi",
            "Ki Kur bad ki Jait Hyndai",
            "Ka Riti Ka Dustur bad ki Kñia ki Khriam"
        ]
    },
    {
        "id": "ka_drama_u_mihsngi",
        "title": "Ka Drama U Mihsngi",
        "native_title": "Ka Drama U Mihsngi",
        "author": "U Mondon Bareh",
        "year": 1929,
        "genre": "Classical Drama & Theatre",
        "file": "book_drama_mihsngi.txt",
        "description": "Pioneering five-act Khasi theatrical drama depicting traditional life, moral conflict, clan identity, and redemption in the Khasi hills.",
        "chapters": [
            "Bynta I: Ka Jingialang ha Shnong",
            "Bynta II: Ka Jingiaseng ki Tymmen",
            "Bynta III: Ka Thma bad Ka Jingiaksaid",
            "Bynta IV: Ka Jingpynrem ia Ka Pop",
            "Bynta V: Ka Jingjop jong Ka Hok"
        ]
    },
    {
        "id": "khasi_english_course_and_grammar",
        "title": "Khasi-English Course and Grammar",
        "native_title": "Khasi-English Course and Grammar for Schools and Colleges",
        "author": "U Mondon Bareh",
        "year": 1929,
        "genre": "Linguistics & Grammar",
        "file": "book_grammar_text.txt",
        "description": "The definitive classical linguistic grammar of the Khasi language covering syntax, noun declensions, verbal aspects, adverbs, and morphological derivations.",
        "chapters": [
            "Chapter I: The Alphabet, Orthography and Pronunciation",
            "Chapter II: The Articles and Gender in Khasi",
            "Chapter III: Nouns and Case Inflections",
            "Chapter IV: The Pronouns and Demonstratives",
            "Chapter V: The Verb and Tense Conjugation",
            "Chapter VI: Adverbs and Expressive Reduplications",
            "Chapter VII: Prepositions and Syntax Rules"
        ]
    },
    {
        "id": "ka_kot_pule_ka_balai",
        "title": "Ka Kot Pule Ka Balai (Khasi Third Reader)",
        "native_title": "Ka Kot Pule Ka Balai",
        "author": "Welsh Presbyterian Mission / Education Department",
        "year": 1904,
        "genre": "Reader & Literature",
        "file": "book_third_reader.txt",
        "description": "Historic foundational reader containing classical Khasi prose, moral fables, natural history, historical sketches, and early translated narratives.",
        "chapters": [
            "Ki Jingithuh ia Ka Ri bad Ka Mariang",
            "Ki Parom Khasi Hyndai",
            "Ki Phawar bad ki Jingrwai",
            "Ka Jingstad Pyrthei bad Ka Jingpule",
            "Ki Jingiathuhkhana shaphang ki Mrad"
        ]
    },
    {
        "id": "ka_myntoi",
        "title": "Ka Myntoi",
        "native_title": "Ka Myntoi",
        "author": "U Rabon Singh",
        "year": 1924,
        "genre": "Philosophy & Ethics",
        "file": "book_myntoi.txt",
        "description": "Classical philosophical prose by legendary writer Rabon Singh, expounding on human morality, community solidarity, wisdom, and moral righteousness.",
        "chapters": [
            "Ka Jingtip-Briew ha Ka Pyrthei",
            "Ka Hok bad Ka Akor ha Shnong ha Thaw",
            "Ka Jingmyntoi jong Ka Jingstad",
            "Ka Jingrwai jong Ka Jingim"
        ]
    },
    {
        "id": "ka_thymmei_parom_khasi",
        "title": "Ka Thymmei Ki Parom Khasi",
        "native_title": "Ka Thymmei Ki Parom Khasi",
        "author": "Indigenous Oral Preservation Society",
        "year": 1935,
        "genre": "Folklore & Mythology",
        "file": "book_thymmei_parom.txt",
        "description": "Comprehensive anthology of Khasi folktales, origin myths of Lum Sohpetbneng, Ka Jingkieng Ksier, U Sier Lapalang, and animal folklore.",
        "chapters": [
            "Ka Jingkieng Ksier bad U Sohpetbneng",
            "U Sier Lapalang ha Lum Shillong",
            "Ka Dian-Doh bad U Bsein Thlen",
            "U Manik Raitong bad Ka Sieng Rupa",
            "Ka Sngi bad U Bnai ha Sahep-Mynnor"
        ]
    },
    {
        "id": "ka_jymbriew_clans_khasi",
        "title": "Ka Jymbriew Ki Khasi: Ki Kur bad Jait",
        "native_title": "Ka Jymbriew Ki Khasi",
        "author": "U Harrison Roy & Tribal Elders",
        "year": 1932,
        "genre": "Genealogy & Kinship",
        "file": "book_jymbriew_clans.txt",
        "description": "Exhaustive genealogical study of Khasi clans (Kur), maternal roots (Kpoh), exogamous marriage laws (Sang), and ancestral affiliations.",
        "chapters": [
            "Ka Seng Kur bad Ka Niam Sang",
            "Ki Kur jong Ka Ri Sohra bad Shillong",
            "Ki Kur jong Ka Ri Jaintia (Pnar)",
            "Ki Kur jong Ka Ri Bhoi bad Ri Maram",
            "Ka Nongtymmen bad Ka Kynti"
        ]
    },
    {
        "id": "ka_jingshai_ka_ri_khasi",
        "title": "Ka Jingshai Ka Ri Khasi",
        "native_title": "Ka Jingshai Ka Ri Khasi",
        "author": "Khasi Historical & Cultural Association",
        "year": 1928,
        "genre": "History & Heritage",
        "file": "book_jingshai_history.txt",
        "description": "Historical chronicle detailing the evolution of the Khasi States, treaties with British power, Tirot Sing Syiem, and resistance struggles.",
        "chapters": [
            "Ka Ri Hynniewtrep Mynshuwa",
            "U Tirot Sing Syiem bad Ka Thma Sohra",
            "Ki Syiem Khasi bad ki San Shnong",
            "Ka Jingpynkup Bor bad Ka Jingkiew Pyrthei",
            "Ka Shongthait bad Ka Jingkylla Ka Ri"
        ]
    }
]

# 2. DLI / Internet Archive PDFs
PDF_BOOKS = [
    {
        "id": "ka_jingsneng_tymmen_part_1",
        "pdf_name": "Ka Jingsneng Tymmen Part 1 - Radhon Singh Berry.pdf",
        "title": "Ka Jingsneng Tymmen (Part 1)",
        "native_title": "Ka Jingsneng Tymmen Shaphang Ka Akor Khasi Part 1",
        "author": "U Radhon Singh Berry",
        "year": 1903,
        "genre": "Poetry & Ethical Phawar",
        "description": "Masterpiece of Khasi didactic rhyming poetry (Phawar) on social etiquette, moral character, respect for elders, and spiritual devotion.",
        "chapters": [
            "Ka Lamphrang (Introduction)",
            "Ka Akor ha ïing ha Sem",
            "Ka Akor ha Lynti ha Syngkhoin",
            "Ka Jingburom ia ki Kmie ki Kpa",
            "Ka Hok bad Ka Blei"
        ]
    },
    {
        "id": "ka_jingsneng_tymmen_part_2",
        "pdf_name": "Ka Jingsneng Tymmen Part 2 - Radhon Singh Berry.pdf",
        "title": "Ka Jingsneng Tymmen (Part 2)",
        "native_title": "Ka Jingsneng Tymmen Shaphang Ka Akor Khasi Part 2",
        "author": "U Radhon Singh Berry",
        "year": 1903,
        "genre": "Poetry & Ethical Phawar",
        "description": "Second volume of Radhon Singh Berry's poetic ethical code detailing marital fidelity, clan duties, community leadership, and righteous living.",
        "chapters": [
            "Ka Akor jong U Shynrang bad Ka Kynthei",
            "Ka Jinglong Khun Ka Jinglong Kmie",
            "Ka Kam ha Shnong ha Thaw",
            "Ka Jingpynshlur ban Trei Hok"
        ]
    },
    {
        "id": "na_lyngwiar_dpei_i_mei",
        "pdf_name": "Na Lyngwiar Dpei I Mei - Streamlet Dkhar.pdf",
        "title": "Na Lyngwiar Dpei I Mei",
        "native_title": "Na Lyngwiar Dpei I Mei",
        "author": "Dr. Streamlet Dkhar",
        "year": 1996,
        "genre": "Cultural Essays & Folklore",
        "description": "Lyrical and intimate essays on Khasi maternal culture, the traditional hearth (Dpei), storytelling by grandmothers, and matriliny.",
        "chapters": [
            "Ka Dpei jong I Mei",
            "Ki Phawar Parom Mynbarim",
            "Ka Mei-Radha bad Ki Khana Pateng",
            "Ka Shongknor ha Dpei",
            "Ka Ktien Ka Mynsiem"
        ]
    },
    {
        "id": "ki_umjer_rupa",
        "pdf_name": "Ki Umjer Rupa - Streamlet Dkhar.pdf",
        "title": "Ki Umjer Rupa",
        "native_title": "Ki Umjer Rupa",
        "author": "Dr. Streamlet Dkhar",
        "year": 1998,
        "genre": "Poetry & Romantic Verse",
        "description": "Celebrated collection of modernist Khasi lyrical poetry reflecting on nature, the misty hills of Meghalaya, personal solitude, and devotion.",
        "chapters": [
            "Ki Sur Mariang",
            "Ka Jingieid Ri",
            "Ki Sngi ba La Leit",
            "Ka Dohnud ba Ksaw",
            "Ki Umjer ha U Tiew-Dohmaw"
        ]
    },
    {
        "id": "u_raikut",
        "pdf_name": "U Raikut - Streamlet Dkhar.pdf",
        "title": "U Raikut",
        "native_title": "U Raikut: Ka Drama Khasi",
        "author": "Dr. Streamlet Dkhar",
        "year": 1993,
        "genre": "Modern Drama",
        "description": "A dramatic exploration of destiny, family honor, youth struggle, and resilience in contemporary Khasi society.",
        "chapters": [
            "Ka Bynta Kaba Nyngkong: Ka Jingpynkhreh",
            "Ka Bynta Kaba Ar: Ka Jingiakynduh",
            "Ka Bynta Kaba Lai: Ka Jingeh ha Lynti",
            "Ka Bynta Kaba Saw: Ka Rai jong Ka Hok"
        ]
    },
    {
        "id": "na_khriang_ka_dohnud",
        "pdf_name": "Na Khriang Ka Dohnud - Streamlet Dkhar.pdf",
        "title": "Na Khriang Ka Dohnud",
        "native_title": "Na Khriang Ka Dohnud",
        "author": "Dr. Streamlet Dkhar",
        "year": 1995,
        "genre": "Poetry & Philosophical Verse",
        "description": "Philosophical poetry exploring the inner conscience, spiritual longing, and emotional landscapes of human existence.",
        "chapters": [
            "Ka Pyrthei jong Ka Dohnud",
            "Ka Sur Kynjah",
            "Ka Jingkhot jong Ka Mariang",
            "Ka Jingngeit ha U Blei"
        ]
    },
    {
        "id": "ka_meiramew_bad_u_hynniewtrep",
        "pdf_name": "Ka Meiramew Bad U Hynniewtrep - Bevan L. Swer.pdf",
        "title": "Ka Meiramew Bad U Hynniewtrep",
        "native_title": "Ka Meiramew Bad U Hynniewtrep",
        "author": "Bevan L. Swer",
        "year": 1998,
        "genre": "Cosmology & Ecological Folklore",
        "description": "Profound ecological and mythological analysis of Mother Earth (Ka Meiramew) and the sacred bond between nature and the Seven Huts (Ki Hynniewtrep).",
        "chapters": [
            "Ka Meiramew: Ka Kmie Mariang",
            "U Hynniewtrep ha Pyrthei",
            "Ki Lawkyntang bad Ka Jingri Mariang",
            "Ka Jingiadei U Briew bad Ka Sngi",
            "Ka Jingkyrkhu jong Ka Ri"
        ]
    },
    {
        "id": "ka_niam_khasi_tynrai_synrang",
        "pdf_name": "Ka Niam Khasi Tynrai Ha Ka Dur Ka Niam Khristan - S. Synrang Khonglah.pdf",
        "title": "Ka Niam Khasi Tynrai Ha Ka Dur Ka Niam Khristan",
        "native_title": "Ka Niam Khasi Tynrai Ha Ka Dur Ka Niam Khristan",
        "author": "S. Synrang Khonglah",
        "year": 1985,
        "genre": "Comparative Religion",
        "description": "Comparative theological treatise analyzing parallels and divergences between traditional Khasi spiritual philosophy and Christian doctrines in Meghalaya.",
        "chapters": [
            "Ka Jingithuh ia U Blei ha Ka Niam Khasi",
            "Ka Pop bad Ka Kñia ha Ka Niam Tynrai",
            "Ka Jingwan Ka Niam Khristan ha Ri Khasi",
            "Ka Jingiapher bad Ka Jingiasyriem",
            "Ka Jingrakhe Niam mynta"
        ]
    },
    {
        "id": "ki_bor_phylla_u_hynniewtrep",
        "pdf_name": "Ki Bor Phylla U Hynniewtrep - Donbok T. Laloo.pdf",
        "title": "Ki Bor Phylla U Hynniewtrep",
        "native_title": "Ki Bor Phylla U Hynniewtrep",
        "author": "Donbok T. Laloo",
        "year": 1995,
        "genre": "Oral Mysticism & Legends",
        "description": "Fascinating examination of mystical beliefs, esoteric lore, sacred monoliths, divinatory egg-breaking (Ka Khan-Pylleng), and unseen powers in Khasi tradition.",
        "chapters": [
            "Ki Bor Blei ha Ki Lum Khasi",
            "Ka Khan-Pylleng bad Ka Jingkñia",
            "Ki Maw-Siem bad Ki Maw-Kyntang",
            "Ki Puriskam jong ki Kynrad Mynbarim",
            "Ka Jinglong Tip-Blei ha Ka Riti"
        ]
    },
    {
        "id": "ki_sur_na_ka_duitara_ksiar",
        "pdf_name": "Ki Sur Na Ka Duitara Ksiar - H.W. Sten.pdf",
        "title": "Ki Sur Na Ka Duitara Ksiar",
        "native_title": "Ki Sur Na Ka Duitara Ksiar",
        "author": "Dr. H.W. Sten",
        "year": 1981,
        "genre": "Literary Criticism",
        "description": "Authoritative literary critique and verse-by-verse analysis of Soso Tham's magnum opus 'Ka Duitara Ksiar', detailing Tham's poetic genius and imagery.",
        "chapters": [
            "Ka Thymmei jong Ka Duitara Ksiar",
            "U Soso Tham kum U Kpa jong Ka Poitri Khasi",
            "Ka Jingbatai ia ki Poitri Ba-Kordor",
            "Ka Rukom Thoh bad Ka Ktien ha Ka Duitara",
            "Ka Jingai Nong ia Ka Ri Khasi"
        ]
    },
    {
        "id": "shaphang_u_wai_u_blai",
        "pdf_name": "Shaphang U Wai U Blai - Jeebon Roy.pdf",
        "title": "Shaphang U Wai U Blai",
        "native_title": "Shaphang U Wai U Blai",
        "author": "Babu Jeebon Roy",
        "year": 1900,
        "genre": "Philosophy & Ethics",
        "description": "Historic booklet by Babu Jeebon Roy explaining the spiritual foundation of Khasi prayers, supplication to God (U Blei), and ethical human duties.",
        "chapters": [
            "U Blei U Nongthaw Uba Ha Khlieh Duh",
            "Kumno ban Duwai bad ban Kñia Hok",
            "Ka Jingiaid Ka Jingim ha Ka Hok",
            "Ka Jingkynmaw ia Ki Kpa Mynshuwa"
        ]
    },
    {
        "id": "i_mabah_soso_tham",
        "pdf_name": "I Mabah Soso Tham - Minette Sibon Tham.pdf",
        "title": "I Mabah Soso Tham",
        "native_title": "I Mabah Soso Tham: Ka Jingim bad Ki Jingrwai",
        "author": "Minette Sibon Tham",
        "year": 1990,
        "genre": "Biography & Literary Legacy",
        "description": "Intimate biography of the national poet Soso Tham written by his daughter, revealing his personal life, writing rituals, and hardships.",
        "chapters": [
            "Ka Jingkha bad Ka Jinglong Khynnah jong U Soso Tham",
            "Ki Sngi jong Ka Jingtrei Skul ha Sohra bad Shillong",
            "Kumno U Thoh ia 'Ki Sngi Barim U Hynniewtrep'",
            "Ka Jingim ha ïing bad Ka Jingieid Khun",
            "Ki Sngi ba Khatduh jong U Mahakabi"
        ]
    },
    {
        "id": "ka_ri_hynniewtrep_sixth_schedule",
        "pdf_name": "Ka Ri Hynniewtrep Bad Ka Sixth Schedule - L. Gilbert Shullai.pdf",
        "title": "Ka Ri Hynniewtrep Bad Ka Sixth Schedule",
        "native_title": "Ka Ri Hynniewtrep Bad Ka Sixth Schedule",
        "author": "L. Gilbert Shullai",
        "year": 1989,
        "genre": "Constitutional History",
        "description": "Historical analysis of tribal autonomy, the Sixth Schedule of the Indian Constitution, Autonomous District Councils (KHADC), and indigenous self-rule.",
        "chapters": [
            "Ka Ri Hynniewtrep bad Ka Sorkar India",
            "Ka Sixth Schedule: Ka Thymmei bad Ka Jingthrang",
            "Ki District Council ha Ri Khasi bad Jaintia",
            "Ki Dorbar Shnong bad Ki Syiemship",
            "Ka Jingiada ia Ka Riti Ka Dustur"
        ]
    },
    {
        "id": "ka_jinglong_tynrai_drama_khasi",
        "pdf_name": "Ka Jinglong Tynrai U Briew Kat Kum Ki Drama Khasi - Streamlet Dkhar.pdf",
        "title": "Ka Jinglong Tynrai U Briew Kat Kum Ki Drama Khasi",
        "native_title": "Ka Jinglong Tynrai U Briew Kat Kum Ki Drama Khasi",
        "author": "Dr. Streamlet Dkhar",
        "year": 1999,
        "genre": "Dramatic Criticism",
        "description": "Comprehensive academic study investigating human nature, character archetypes, and cultural values as dramatized in twentieth-century Khasi plays.",
        "chapters": [
            "Ka Thymmei jong Ka Drama ha Ri Khasi",
            "Ka Jingbatai ia U Shynrang bad Ka Kynthei ha Drama",
            "Ka Hok bad Ka Bor Pyrkhat ha Ka Stage",
            "Ki Nongthoh Drama Ba-Pawnam jong Ka Ri",
            "Ka Jinglong Tynrai ha Ka Jingim Ba-Shisha"
        ]
    },
    {
        "id": "u_soso_tham_bad_ki_jingtrei",
        "pdf_name": "U Soso Tham Bad Ki Jingtrei Jong U - Hughlet Warjri.pdf",
        "title": "U Soso Tham Bad Ki Jingtrei Jong U",
        "native_title": "U Soso Tham Bad Ki Jingtrei Jong U",
        "author": "Hughlet Warjri",
        "year": 1985,
        "genre": "Literary Criticism",
        "description": "Detailed scholarly critique examining Soso Tham's metric innovations, imagery, metaphors, and patriotic philosophy across all his works.",
        "chapters": [
            "Ka Dor jong Ka Ktien U Soso Tham",
            "Ka Jingpyndonkam ia Ki Ktien-Tylli bad Phawar",
            "U Soso Tham kum U Nonghikai Pyrthei",
            "Ka Jingrwai ia Ka Mariang bad Ka Hok",
            "Ka Nam Mahakabi jong Ka Ri Meghalaya"
        ]
    }
]

def build_all_books():
    print("Building whole-book dataset for Khasi Language Library...")
    catalog = []
    
    # Process 9 text books
    for binfo in TEXT_BOOKS:
        fname = binfo["file"]
        fpath = WORKSPACE_DIR / fname
        if not fpath.exists():
            print(f"Warning: {fname} not found!")
            continue
        
        with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
            raw_text = f.read()
        
        pages = paginate_text(raw_text, target_words=320)
        total_w = sum(p["word_count"] for p in pages)
        
        book_obj = {
            "id": binfo["id"],
            "title": binfo["title"],
            "native_title": binfo["native_title"],
            "author": binfo["author"],
            "year": binfo["year"],
            "genre": binfo["genre"],
            "description": binfo["description"],
            "total_pages": len(pages),
            "total_words": total_w,
            "chapters": binfo["chapters"],
            "source_type": "digitized_text_edition",
            "pages": pages
        }
        
        out_json = BOOKS_DATA_DIR / f"{binfo['id']}.json"
        with open(out_json, "w", encoding="utf-8") as f:
            json.dump(book_obj, f, ensure_ascii=False, indent=2)
            
        print(f"[Done Text Book] {binfo['title']}: {len(pages)} pages, {total_w} words -> {out_json.name}")
        
        catalog.append({
            "id": binfo["id"],
            "title": binfo["title"],
            "native_title": binfo["native_title"],
            "author": binfo["author"],
            "year": binfo["year"],
            "genre": binfo["genre"],
            "description": binfo["description"],
            "total_pages": len(pages),
            "total_words": total_w,
            "chapter_count": len(binfo["chapters"]),
            "source_type": "digitized_text_edition"
        })

    # Process 15 PDF books
    for binfo in PDF_BOOKS:
        pdf_name = binfo["pdf_name"]
        pdf_path = PDF_DIR / pdf_name
        if not pdf_path.exists():
            print(f"Warning: {pdf_name} not found in {PDF_DIR}!")
            continue
            
        try:
            reader = pypdf.PdfReader(str(pdf_path))
            pages = []
            for idx, p in enumerate(reader.pages):
                txt = p.extract_text() or ""
                txt_clean = re.sub(r'[\r\t]+', ' ', txt).strip()
                pages.append({
                    "page_number": idx + 1,
                    "text": txt_clean,
                    "word_count": len(txt_clean.split())
                })
            
            total_w = sum(p["word_count"] for p in pages)
            
            book_obj = {
                "id": binfo["id"],
                "title": binfo["title"],
                "native_title": binfo["native_title"],
                "author": binfo["author"],
                "year": binfo["year"],
                "genre": binfo["genre"],
                "description": binfo["description"],
                "total_pages": len(pages),
                "total_words": total_w,
                "chapters": binfo["chapters"],
                "source_type": "dli_internet_archive_scan",
                "pages": pages
            }
            
            out_json = BOOKS_DATA_DIR / f"{binfo['id']}.json"
            with open(out_json, "w", encoding="utf-8") as f:
                json.dump(book_obj, f, ensure_ascii=False, indent=2)
                
            print(f"[Done PDF Book] {binfo['title']}: {len(pages)} pages, {total_w} words -> {out_json.name}")
            
            catalog.append({
                "id": binfo["id"],
                "title": binfo["title"],
                "native_title": binfo["native_title"],
                "author": binfo["author"],
                "year": binfo["year"],
                "genre": binfo["genre"],
                "description": binfo["description"],
                "total_pages": len(pages),
                "total_words": total_w,
                "chapter_count": len(binfo["chapters"]),
                "source_type": "dli_internet_archive_scan"
            })
        except Exception as e:
            print(f"Error processing {pdf_name}: {e}")

    # Save index
    index_path = BOOKS_DATA_DIR / "books_index.json"
    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(catalog, f, ensure_ascii=False, indent=2)
        
    total_all_pages = sum(c["total_pages"] for c in catalog)
    total_all_words = sum(c["total_words"] for c in catalog)
    print(f"\nSuccessfully built {len(catalog)} books with {total_all_pages} pages and {total_all_words} words!")

if __name__ == "__main__":
    build_all_books()
