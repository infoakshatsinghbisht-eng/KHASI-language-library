# -*- coding: utf-8 -*-
"""Khasi Voice Synthesis & SSML Speech Generator."""

import math
import struct
from typing import Dict, List, Any
from ..phonetics import syllables, normalize

class KhasiVoiceSynthesizer:
    """Provides speech synthesis markup (SSML), phonetic breakdown, and PCM audio generation."""

    @staticmethod
    def get_speech_ssml(text: str, rate: str = "medium", pitch: str = "+0%") -> str:
        """Generate standardized SSML speech tags for Khasi text."""
        norm_text = normalize(text)
        return f"""<speak>
  <prosody rate="{rate}" pitch="{pitch}">
    <lang xml:lang="en-IN">{norm_text}</lang>
  </prosody>
</speak>"""

    @staticmethod
    def get_phonetic_script(text: str) -> Dict[str, Any]:
        """Produce syllable breakdown and phonetic profile for speech engines."""
        norm = normalize(text)
        words = norm.split()
        breakdown = []
        for w in words:
            breakdown.append({"word": w, "syllables": syllables(w)})
        return {
            "text": norm,
            "phonetic_breakdown": breakdown,
            "language": "khasi",
            "orthography": "latin_adapted"
        }

    @staticmethod
    def generate_pcm_wav(duration_seconds: float = 0.5, freq: float = 440.0) -> bytes:
        """Synthesize pure sinusoidal PCM WAV wave for testing audio pipelines."""
        sample_rate = 16000
        num_samples = int(sample_rate * duration_seconds)
        data = bytearray()
        for i in range(num_samples):
            t = float(i) / sample_rate
            env = math.sin(math.pi * t / duration_seconds)
            val = int(32767.0 * 0.6 * math.sin(2.0 * math.pi * freq * t) * env)
            data.extend(struct.pack("<h", max(-32768, min(32767, val))))

        # 44-byte WAV header
        header = bytearray(b"RIFF")
        header.extend(struct.pack("<I", 36 + len(data)))
        header.extend(b"WAVEfmt ")
        header.extend(struct.pack("<I", 16))
        header.extend(struct.pack("<H", 1))
        header.extend(struct.pack("<H", 1))
        header.extend(struct.pack("<I", sample_rate))
        header.extend(struct.pack("<I", sample_rate * 2))
        header.extend(struct.pack("<H", 2))
        header.extend(struct.pack("<H", 16))
        header.extend(b"data")
        header.extend(struct.pack("<I", len(data)))
        return bytes(header + data)
