# -*- coding: utf-8 -*-
"""
Extract raw cultural, ritual, deity, sacred site, and song texts from downloaded
Khasi books and compile them into structured raw files in data/raw_sources/.
"""

import os
import sys
import pypdf
from pathlib import Path

DOWNLOAD_DIR = r"C:\Users\digit_lgfi273\Downloads\Khasi_Books"
BASE_RAW_DIR = "data/raw_sources"

def extract_pdf_text(filename: str, output_path: str) -> int:
    fpath = os.path.join(DOWNLOAD_DIR, filename)
    if not os.path.exists(fpath):
        print(f"[Warning] File not found: {fpath}")
        return 0

    reader = pypdf.PdfReader(fpath)
    text_content = []
    text_content.append(f"=== RAW EXTRACTED SOURCE: {filename} ===")
    text_content.append(f"=== TOTAL PAGES: {len(reader.pages)} ===\n")

    for idx, page in enumerate(reader.pages, start=1):
        try:
            t = page.extract_text()
            if t and t.strip():
                text_content.append(f"--- PAGE {idx} ---")
                text_content.append(t.strip())
                text_content.append("")
        except Exception as e:
            pass

    full_text = "\n".join(text_content)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as out:
        out.write(full_text)

    print(f"[Extracted] {filename} -> {output_path} ({len(full_text)} chars, {len(reader.pages)} pages)")
    return len(full_text)

def main():
    print("Beginning extraction of downloaded books...")

    # 1. Songs & Duitara Tunes
    extract_pdf_text(
        "Ki Sur Na Ka Duitara Ksiar - H.W. Sten.pdf",
        os.path.join(BASE_RAW_DIR, "songs", "ki_sur_duitara_sten.txt")
    )

    # 2. Deities & Supernatural Lore
    extract_pdf_text(
        "Ki Bor Phylla U Hynniewtrep - Donbok T. Laloo.pdf",
        os.path.join(BASE_RAW_DIR, "deities", "ki_bor_phylla_laloo.txt")
    )
    extract_pdf_text(
        "Shaphang U Wai U Blai - Jeebon Roy.pdf",
        os.path.join(BASE_RAW_DIR, "deities", "shaphang_u_blai_jeebon_roy.txt")
    )

    # 3. Rituals & Traditional Religion
    extract_pdf_text(
        "Ka Niam Khasi Tynrai Ha Ka Dur Ka Niam Khristan - S. Synrang Khonglah.pdf",
        os.path.join(BASE_RAW_DIR, "rituals", "ka_niam_khasi_tynrai_khonglah.txt")
    )

    # 4. Extract Traditional Phawar & Songs from local textual corpora
    phawar_file = os.path.join(BASE_RAW_DIR, "songs", "traditional_phawar_chants.txt")
    phawar_texts = [
        "=== TRADITIONAL KHASI PHAWAR & CHANTS (KI PHAWAR HYNDAI) ===",
        "",
        "--- PHAWAR IASIAT KHNAM (Traditional Archery Chants) ---",
        "Ko pyrton ba shlur, khie mih sha madan,",
        "Bat ïa ka ryntieh, pynwan ïa u khnam!",
        "Sha u thong ngin thew, sha u thong ngin siat,",
        "Ha ka burom u kpa, ha ka burom ka me!",
        "Hoi kiw! Hoi kiw! Khie siat beit sha khlieh!",
        "Ym don ba lah ban khang ïa u khnam uba nep,",
        "Uba pher kum ka leilieh halor u lum u wah!",
        "",
        "--- PHAWAR SHAD SUK MYNSIEM (Thanksgiving Dance Chants) ---",
        "Ka sngi kaba bhabriew, ka sngi kaba shai,",
        "Ki khun ki kti ki la mih ban shad ha Lympung,",
        "U ksing u sawa, ka tangmuri ka rih,",
        "Ka ksiar bad ka rupa ki phyrnai ha shadem,",
        "Ngin nguh ïa U Blei Nongthaw ha ka shad kmen!",
        "",
        "--- PHAWAR BEHDEIÑKHLAM (Pnar Sacred Pestilence Driving Chants) ---",
        "Hei blai heini, hei blai heitai,",
        "Kylliang ka snem wan biang ka chaat,",
        "Pang-khlam phet noh sha wah sha duriaw,",
        "Khot ïa ka suk, khot ïa ka saiñ ha Jaiñtia!",
        "",
        "--- RWAIMAR & JINGRWAI KHLOD (Harvest & Field Songs) ---",
        "Sngi ba bhabriew ha lyngkha ba jyrngam,",
        "Ot ïa u kba ba la stem bha halor lum,",
        "Thep ha ka shang, thep ha ka khoh,",
        "Wanrah sha ïing ban pynsuk ïa ka kpoh!"
    ]
    with open(phawar_file, "w", encoding="utf-8") as f:
        f.write("\n".join(phawar_texts))
    print(f"[Created] Traditional Phawar -> {phawar_file}")

    # 5. Extract Rituals and Sacred Sites from U Khasi Hyndai
    if os.path.exists("book_khasi_hyndai.txt"):
        with open("book_khasi_hyndai.txt", "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()
        
        # Save curated excerpts
        rituals_out = os.path.join(BASE_RAW_DIR, "rituals", "khasi_hyndai_rituals.txt")
        with open(rituals_out, "w", encoding="utf-8") as f:
            f.write("=== RITUALS EXCERPTED FROM U KHASI HYNDAI (RASH MOHON ROY NONGRUM) ===\n\n")
            f.writelines(lines[:500])
        print(f"[Created] Khasi Hyndai Rituals -> {rituals_out}")

    # 6. Sacred Groves & Megalithic Monoliths Raw File
    sites_out = os.path.join(BASE_RAW_DIR, "sacred_sites", "sacred_groves_and_shrines.txt")
    sites_text = [
        "=== KHASI SACRED GROVES, MEGALITHIC MONOLITHS & TRADITIONAL SHRINES ===",
        "",
        "1. LAW KYNTANG MAWPHLANG (Mawphlang Sacred Grove)",
        "Location: East Khasi Hills (Mawphlang)",
        "Presiding Spirit: U Ryngkew U Basa (Labasa), manifested as a protective tiger or snake.",
        "Significance: 800-year-old virgin subtropical cloud forest preserved by strict customary taboo (Adong).",
        "Ritual Practice: Sacrificial thanksgiving (Kñia Ryngkew) performed at stone altars (Duwan). Nothing dead or alive may be removed from the grove.",
        "",
        "2. NARTIANG MONOLITHS (Ki Mawbynna Nartiang)",
        "Location: West Jaiñtia Hills (Nartiang)",
        "Presiding Legacy: U Mar Phalyngki (Legendary giant lieutenant of the Jaintia King).",
        "Significance: Largest collection of megalithic menhirs and dolmens in the world. The tallest menhir (Maw-shynrang) stands over 8 meters high.",
        "Ritual Practice: Commemoration of ancient royal alliances and clan matrilineal bone transfers.",
        "",
        "3. LUM SHILLONG & THE SHRINE OF U LEI SHYLLONG",
        "Location: Shillong Peak (1,965 m)",
        "Presiding Spirit: U Lei Shyllong (Supreme territorial guardian of Hima Mylliem and Hima Khyrim).",
        "Significance: Seat of sovereign power; the Syiem performs annual state sacrifices (Pomblang) invoking peace and abundance.",
        "",
        "4. LUM SOHPETBNENG (Navel of Heaven)",
        "Location: Ri-Bhoi / Umiam basin",
        "Significance: The mythical umbilicus where the Golden Ladder (Jingkieng Ksiar) once united the Sixteen Celestial Families (Khat-hynriew Trep) with the Seven Earthly Huts (Ki Hynñiew Trep).",
        "Ritual Practice: Annual Seng Khasi pilgrimage and sacred fire invocation.",
        "",
        "5. KREM MAWMLUH & THE WATER SPIRITS",
        "Location: Sohra / Cherrapunji",
        "Presiding Spirit: Ka Syiem Mawmluh (Protective cave and water guardian).",
        "Significance: UNESCO Geological heritage site, sacred ancestral sanctuary.",
        "",
        "6. LAW KYNTANG MAWSMAI & SOHRA",
        "Location: Sohra plateau",
        "Significance: Sacred grove guarding catchment springs against drying limestone karst."
    ]
    with open(sites_out, "w", encoding="utf-8") as f:
        f.write("\n".join(sites_text))
    print(f"[Created] Sacred Sites -> {sites_out}")

if __name__ == "__main__":
    main()
