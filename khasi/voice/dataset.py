# -*- coding: utf-8 -*-
"""
Khasi Audio Waveform Dataset & Speech Pipeline Interface.
Provides loader, metadata inspector, verification, and exporter tools for
Automatic Speech Recognition (ASR) and Text-To-Speech (TTS) pipelines.
"""

import os
import json
import csv
import wave
from typing import Dict, List, Any, Optional

MANIFEST_PATH = os.path.join(os.path.dirname(__file__), "data", "audio_manifest.json")
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")

class KhasiAudioDataset:
    """Manages 252 native Khasi spoken waveforms and paired transcription manifests."""

    def __init__(self, manifest_file: Optional[str] = None):
        self.manifest_file = manifest_file or MANIFEST_PATH
        self.records: List[Dict[str, Any]] = self._load()

    def _load(self) -> List[Dict[str, Any]]:
        if not os.path.exists(self.manifest_file):
            return []
        with open(self.manifest_file, "r", encoding="utf-8") as f:
            return json.load(f)

    def __len__(self) -> int:
        return len(self.records)

    def get_records(self, split: Optional[str] = None) -> List[Dict[str, Any]]:
        """Return dataset records, optionally filtered by split ('train', 'validation', 'test')."""
        if not split:
            return self.records
        s = split.lower().strip()
        return [r for r in self.records if r.get("split") == s]

    def get_item(self, audio_id: str) -> Optional[Dict[str, Any]]:
        """Lookup an item by ID (e.g., 'phrase_001', 'proverb_015')."""
        aid = audio_id.lower().strip()
        for r in self.records:
            if r["id"].lower() == aid:
                return r
        return None

    def get_audio_path(self, audio_id: str) -> Optional[str]:
        """Return absolute path on disk to the WAV file."""
        item = self.get_item(audio_id)
        if not item:
            return None
        rel_path = item["file_path"]
        abs_path = os.path.join(DATA_DIR, rel_path)
        if os.path.exists(abs_path):
            return abs_path
        return None

    def get_audio_bytes(self, audio_id: str) -> Optional[bytes]:
        """Read and return raw bytes of the audio file."""
        path = self.get_audio_path(audio_id)
        if not path or not os.path.exists(path):
            return None
        with open(path, "rb") as f:
            return f.read()

    def search_audio(self, query: str) -> List[Dict[str, Any]]:
        """Search recordings by Khasi text, English meaning, or category."""
        q = query.lower().strip()
        results = []
        for r in self.records:
            if (q in r.get("khasi_text", "").lower() or
                q in r.get("english_translation", "").lower() or
                q in r.get("category", "").lower()):
                results.append(r)
        return results

    def get_stats(self) -> Dict[str, Any]:
        """Return comprehensive dataset statistics."""
        total_duration = sum(r.get("duration_seconds", 0) for r in self.records)
        phrases = [r for r in self.records if r.get("type") == "phrase"]
        proverbs = [r for r in self.records if r.get("type") == "proverb"]

        splits = {}
        for r in self.records:
            s = r.get("split", "unassigned")
            splits[s] = splits.get(s, 0) + 1

        speakers = {}
        for r in self.records:
            spk = r.get("speaker_id", "unknown")
            speakers[spk] = speakers.get(spk, 0) + 1

        return {
            "total_recordings": len(self.records),
            "total_phrases": len(phrases),
            "total_proverbs": len(proverbs),
            "total_duration_seconds": round(total_duration, 2),
            "total_duration_minutes": round(total_duration / 60.0, 2),
            "sample_rate_hz": 16000,
            "format": "PCM 16-bit Mono WAV",
            "splits": splits,
            "speakers": speakers,
        }

    def verify_integrity(self) -> Dict[str, Any]:
        """Verify that every audio file exists, has valid RIFF header, and readable frames."""
        verified = 0
        missing = []
        corrupted = []

        for r in self.records:
            rel = r["file_path"]
            path = os.path.join(DATA_DIR, rel)
            if not os.path.exists(path):
                missing.append(r["id"])
                continue
            try:
                with wave.open(path, "rb") as wf:
                    if wf.getnchannels() != 1 or wf.getframerate() != 16000:
                        corrupted.append((r["id"], "Invalid channel/rate"))
                    else:
                        verified += 1
            except Exception as e:
                corrupted.append((r["id"], str(e)))

        return {
            "total_manifest_items": len(self.records),
            "verified_valid": verified,
            "missing_files": missing,
            "corrupted_files": corrupted,
            "all_healthy": (verified == len(self.records)) and (len(missing) == 0) and (len(corrupted) == 0)
        }

    def export_huggingface_format(self, output_path: str) -> int:
        """Export dataset metadata to Hugging Face Audio Datasets JSONL format."""
        records = []
        for r in self.records:
            rec = {
                "id": r["id"],
                "audio": r["file_path"],
                "sentence": r["khasi_text"],
                "translation_en": r.get("english_translation", ""),
                "translation_hi": r.get("hindi_translation", ""),
                "speaker_id": r.get("speaker_id", ""),
                "gender": r.get("speaker_gender", ""),
                "duration": r.get("duration_seconds", 0.0),
                "split": r.get("split", "train")
            }
            records.append(rec)

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            for rec in records:
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        return len(records)

    def export_common_voice_tsv(self, output_path: str) -> int:
        """Export dataset to Mozilla Common Voice TSV format."""
        fields = ["client_id", "path", "sentence", "up_votes", "down_votes", "age", "gender", "accent", "locale", "segment"]
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fields, delimiter="\t")
            writer.writeheader()
            for r in self.records:
                row = {
                    "client_id": r.get("speaker_id", "SPK_KHA"),
                    "path": r["file_path"],
                    "sentence": r["khasi_text"],
                    "up_votes": 2,
                    "down_votes": 0,
                    "age": "thirties",
                    "gender": r.get("speaker_gender", "other"),
                    "accent": "khasi_sohra",
                    "locale": "kha",
                    "segment": r.get("category", "")
                }
                writer.writerow(row)
        return len(self.records)
