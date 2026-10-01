# -*- coding: utf-8 -*-
"""
Khasi Folklore & Oral Heritage Preservation Workflow:
- Recording oral storytelling metadata (speaker, village, dialect, audio file)
- Orthographic validation & health score
- Exporting to JSONL (for LLM fine-tuning/HuggingFace datasets) and CSV (for linguists)
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
    print("   Khasi: Digital Oral Heritage & Corpus Preservation    ")
    print("=" * 65)

    manager = khasi.CorpusManager()

    # 1. Archiving a new elder oral story
    new_story = khasi.PreservationRecord(
        id="folklore-003",
        title_khasi="Ka Nohkalikai",
        title_english="The Legend of Ka Likai Waterfall",
        genre="Tragic Legend",
        dialect="sohra",
        region="Sohra (Cherrapunji), East Khasi Hills",
        speaker_name="Kong Kmenlang",
        speaker_age=78,
        collector_name="Preservation Team",
        audio_path="recordings/audio_folklore_003.wav",
        khasi_text=(
            "Ha Sohra la don kawei ka samla kaba kyrteng ka Likai. "
            "Ka la don i khunlung iba rit. Hadien ba u kpa jong i u la ïap, "
            "ka la shongkurim biang bad uwei pat u briew. U kpa-nah u la bishni bad "
            "u la pynïap ïa i khunlung. Ynda ka Likai ka la tip ïa kane ka jingshisha "
            "kaba sniew, ka la phet sha khlieh ka kshaid bad ka la ryngkoh sha them. "
            "Kumta la khot ïa kata ka kshaid 'Ka Nohkalikai'."
        ),
        english_translation=(
            "In Sohra there lived a young woman named Likai who had an infant child. "
            "After the child's father died, she remarried. The stepfather grew jealous "
            "and killed the child. When Likai discovered this terrible tragedy, she ran "
            "to the crest of the waterfall and leaped into the abyss. Henceforth that "
            "waterfall was named 'Ka Nohkalikai' (The Leap of Ka Likai)."
        ),
        cultural_notes="Legend explains the naming of Nohkalikai Falls, the tallest plunge waterfall in India."
    )

    manager.add_record(new_story)
    print(f"\n[+] Added Record: {new_story.title_khasi} ({new_story.title_english})")

    # 2. Text Validation
    validation = manager.validate_text(new_story.khasi_text)
    print("\nText Validation & Orthography Health:")
    print(f"  - Total words      : {validation['total_words']}")
    print(f"  - Valid words      : {validation['valid_words']}")
    print(f"  - Validity ratio   : {validation['validity_ratio'] * 100:.1f}%")
    print(f"  - Has diacritics   : {validation['has_khasi_diacritics']}")

    # 3. Export formats
    out_dir = Path(__file__).parent / "exports"
    jsonl_count = manager.export_jsonl(str(out_dir / "khasi_corpus.jsonl"))
    csv_count = manager.export_csv(str(out_dir / "khasi_corpus.csv"))
    hf_count = manager.export_huggingface_format(str(out_dir / "huggingface_khasi.json"))

    print("\nExport Outputs Generated:")
    print(f"  - JSONL format (Fine-tuning ready) : {out_dir / 'khasi_corpus.jsonl'} ({jsonl_count} records)")
    print(f"  - CSV format (Field linguistics)   : {out_dir / 'khasi_corpus.csv'} ({csv_count} records)")
    print(f"  - Hugging Face translation format  : {out_dir / 'huggingface_khasi.json'} ({hf_count} records)")
    print("=" * 65)

if __name__ == "__main__":
    main()
