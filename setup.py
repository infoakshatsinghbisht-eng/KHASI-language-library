# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, "README.md")
long_description = open(readme_path, encoding="utf-8").read() if os.path.exists(readme_path) else ""

setup(
    name="khasi",
    version="1.3.0",
    author="Akshat Singh Bisht",
    author_email="infoakshatsinghbisht@gmail.com",
    maintainer="Akshat Singh Bisht",
    maintainer_email="infoakshatsinghbisht@gmail.com",
    description="Khasi (Ka Ktien Khasi) Language Library: 105,000+ Headwords, 13,000+ Dialect Lexicons (Pnar/War/Bhoi/Maram), 252 Native Audio Waveforms, Aligned MT Parallel Corpora, and Meghalaya Cultural Heritage",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/infoakshatsinghbisht-eng/KHASI-language-library",
    project_urls={
        "Homepage": "https://akshatsinghbisht.com/",
        "GitHub": "https://github.com/infoakshatsinghbisht-eng/KHASI-language-library",
        "LinkedIn": "https://www.linkedin.com/in/akshat-singh-bisht-digital-performance-marketing-specialist/",
        "Amazon Author": "https://www.amazon.com/stores/Akshat-Singh-Bisht/author/B0D5TYDT28",
        "ResearchGate": "https://www.researchgate.net/profile/Akshat-Bisht-8",
        "Bug Tracker": "https://github.com/infoakshatsinghbisht-eng/KHASI-language-library/issues",
    },
    packages=find_packages(exclude=["tests*", "examples*"]),
    include_package_data=True,
    package_data={
        "khasi.lexicon": ["data/*.json", "data/dialects/*.json"],
        "khasi.culture": ["data/*.json"],
        "khasi.voice": ["data/*.json", "data/*.jsonl", "data/audio/*/*.wav"],
        "khasi.corpus": ["data/*.json", "data/*.jsonl", "data/bitext/*"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: Linguistic",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "khasi=khasi.cli:main",
        ],
    },
)
