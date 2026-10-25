# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, "README.md")
long_description = open(readme_path, encoding="utf-8").read() if os.path.exists(readme_path) else ""

setup(
    name="khasi",
    version="1.16.0",
    author="Akshat Singh Bisht",
    author_email="infoakshatsinghbisht@gmail.com",
    maintainer="Akshat Singh Bisht",
    description="Khasi (Ka Ktien Khasi) Language Library: 608,086+ Headwords, 100 Classical Grammar Rules Engine across 9 Categories, 2,598 Digitized Books (384,803 Pages, 87.56M+ Words), 1,939 Preserved PDF Editions, 300 Traditional Songs & Phawar, 39 Deities, 112 Flora, 89 Fauna, 66 Riddles, and Universal Lexicon",
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
    include_package_data=False,
    package_data={
        "khasi.lexicon": ["data/*.json", "data/dialects/*.json"],
        "khasi.culture": ["data/*.json", "data/books/books_index.json", "data/folklore/*.json", "data/songs/*.json"],
        "khasi.voice": ["data/*.json", "data/*.jsonl", "data/audio/*/*.wav"],
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
