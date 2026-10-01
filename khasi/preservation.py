# -*- coding: utf-8 -*-
"""
Digital Language Preservation & Archival Toolkit for Khasi.
Empowers field researchers, linguists, and community elders to:
- Catalog oral narratives, folklore, and audio recordings
- Record speaker metadata (dialect, region, age, clan)
- Validate orthographic integrity
- Export corpora to JSONL, CSV, and Hugging Face Dataset formats
"""

import json
import csv
from dataclasses import dataclass, field, asdict
from enum import Enum
from pathlib import Path
from typing import List, Dict, Optional, Any
from datetime import date

from .phonetics import normalize, tokenize, is_khasi_word, has_khasi_diacritics
from .constants import Dialect

@dataclass
class PreservationRecord:
    """Metadata and content record for an archival Khasi text or oral recording."""
    id: str
    title_khasi: str
    title_english: str
    khasi_text: str
    english_translation: str
    dialect: str = "sohra"
    region: str = "East Khasi Hills, Meghalaya"
    speaker_name: Optional[str] = None
    speaker_age: Optional[int] = None
    collector_name: Optional[str] = None
    audio_path: Optional[str] = None
    summary: Optional[str] = None
    cultural_notes: Optional[str] = None
    genre: str = "Folktale"
    recording_date: str = field(default_factory=lambda: date.today().isoformat())
    license: str = "CC-BY-NC-SA 4.0"

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

class CorpusManager:
    """Corpus management, validation, and export tool for Khasi preservation."""

    def __init__(self):
        self.records: List[PreservationRecord] = []

    def add_record(self, record: PreservationRecord) -> None:
        self.records.append(record)

    def validate_text(self, text: str) -> Dict[str, Any]:
        words = tokenize(text, keep_punct=False)
        total_words = len(words)
        if total_words == 0:
            return {"valid": False, "total_words": 0, "unknown_words": [], "validity_ratio": 0.0}

        invalid = [w for w in words if not is_khasi_word(w)]
        valid_count = total_words - len(invalid)
        ratio = round(valid_count / total_words, 3)

        return {
            "valid": len(invalid) == 0,
            "total_words": total_words,
            "valid_words": valid_count,
            "unknown_words": invalid,
            "validity_ratio": ratio,
            "has_khasi_diacritics": has_khasi_diacritics(text),
        }

    def export_jsonl(self, output_path: str) -> int:
        out = Path(output_path)
        out.parent.mkdir(parents=True, exist_ok=True)
        with open(out, "w", encoding="utf-8") as f:
            for r in self.records:
                f.write(json.dumps(r.to_dict(), ensure_ascii=False) + "\n")
        return len(self.records)

    def export_csv(self, output_path: str) -> int:
        out = Path(output_path)
        out.parent.mkdir(parents=True, exist_ok=True)
        if not self.records:
            return 0
        keys = list(self.records[0].to_dict().keys())
        with open(out, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            for r in self.records:
                writer.writerow(r.to_dict())
        return len(self.records)

    def export_huggingface_format(self, output_path: str) -> int:
        out = Path(output_path)
        out.parent.mkdir(parents=True, exist_ok=True)
        formatted = []
        for r in self.records:
            formatted.append({
                "id": r.id,
                "translation": {
                    "kha": r.khasi_text,
                    "en": r.english_translation,
                },
                "meta": {
                    "dialect": r.dialect,
                    "region": r.region,
                    "genre": r.genre,
                }
            })
        with open(out, "w", encoding="utf-8") as f:
            json.dump(formatted, f, ensure_ascii=False, indent=2)
        return len(formatted)
