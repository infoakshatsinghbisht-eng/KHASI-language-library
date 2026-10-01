# -*- coding: utf-8 -*-
"""Khasi Number System, Cardinal/Ordinal Converter, and Numerals."""

from typing import Union

ONES = {
    0: "nod",
    1: "wei",
    2: "ar",
    3: "lai",
    4: "saw",
    5: "san",
    6: "hynriew",
    7: "hynniew",
    8: "phra",
    9: "khyndai"
}

TEENS = {
    10: "shiphew",
    11: "khatwei",
    12: "khat-ar",
    13: "khat-lai",
    14: "khat-saw",
    15: "khat-san",
    16: "khat-hynriew",
    17: "khat-hynniew",
    18: "khat-phra",
    19: "khat-khyndai"
}

TENS = {
    1: "shiphew",
    2: "arphew",
    3: "laiphew",
    4: "sawphew",
    5: "sanphew",
    6: "hynriewphew",
    7: "hynniewphew",
    8: "phraphew",
    9: "khyndaiphew"
}

def num_to_words(n: int) -> str:
    """Convert an integer to formal Khasi words."""
    if n < 0:
        return f"duna {num_to_words(abs(n))}"
    if n == 0:
        return ONES[0]
    if 1 <= n <= 9:
        return ONES[n]
    if 10 <= n <= 19:
        return TEENS[n]
    if 20 <= n <= 99:
        t, r = divmod(n, 10)
        ten_str = TENS[t]
        return ten_str if r == 0 else f"{ten_str} {ONES[r]}"
    if 100 <= n <= 999:
        h, r = divmod(n, 100)
        hundred_str = "shispah" if h == 1 else f"{ONES[h]}spah"
        return hundred_str if r == 0 else f"{hundred_str} {num_to_words(r)}"
    if 1000 <= n <= 99999:
        th, r = divmod(n, 1000)
        th_str = "shihajar" if th == 1 else f"{num_to_words(th)} hajar"
        return th_str if r == 0 else f"{th_str} {num_to_words(r)}"
    if 100000 <= n <= 9999999:
        l, r = divmod(n, 100000)
        l_str = "shilak" if l == 1 else f"{num_to_words(l)} lak"
        return l_str if r == 0 else f"{l_str} {num_to_words(r)}"
    
    c, r = divmod(n, 10000000)
    c_str = "shiklot" if c == 1 else f"{num_to_words(c)} klot"
    return c_str if r == 0 else f"{c_str} {num_to_words(r)}"

def words_to_num(text: str) -> int:
    """Parse a Khasi number expression into an integer."""
    raw = text.lower().strip()
    words = raw.replace("-", " ").split()

    single_map = {
        "nod": 0, "wei": 1, "shi": 1, "ar": 2, "lai": 3, "saw": 4, "san": 5,
        "hynriew": 6, "hynniew": 7, "phra": 8, "khyndai": 9,
        "shiphew": 10, "khatwei": 11, "khat ar": 12, "khat lai": 13, "khat saw": 14,
        "khat san": 15, "khat hynriew": 16, "khat hynniew": 17, "khat phra": 18, "khat khyndai": 19,
        "arphew": 20, "laiphew": 30, "sawphew": 40, "sanphew": 50,
        "hynriewphew": 60, "hynniewphew": 70, "phraphew": 80, "khyndaiphew": 90
    }

    if raw in single_map:
        return single_map[raw]

    total = 0
    current = 0
    for w in words:
        if w in single_map:
            current += single_map[w]
        elif w.endswith("phew"):
            prefix = w[:-4]
            prefix_val = single_map.get(prefix, 1)
            current += prefix_val * 10
        elif w == "shispah":
            current += 100
        elif w.endswith("spah"):
            prefix = w[:-4]
            prefix_val = single_map.get(prefix, 1)
            current += prefix_val * 100
        elif w == "shihajar":
            total += (current if current else 1) * 1000
            current = 0
        elif w == "hajar":
            total += current * 1000
            current = 0
        elif w == "shilak":
            total += (current if current else 1) * 100000
            current = 0
        elif w == "lak":
            total += current * 100000
            current = 0
    total += current
    return total

def ordinal(n: int) -> str:
    """Return the Khasi ordinal form (e.g., 1 -> ba-nyngkong, 2 -> ba-ar)."""
    if n == 1:
        return "ba-nyngkong"
    if n == 2:
        return "ba-ar"
    if n == 3:
        return "ba-lai"
    return f"ba-{num_to_words(n)}"

def fraction(num: int, denom: int) -> str:
    """Return the Khasi fraction expression."""
    if num == 1 and denom == 2:
        return "shiteng"
    if num == 1 and denom == 4:
        return "shikhana"
    if num == 3 and denom == 4:
        return "lai khana"
    return f"{num_to_words(num)} bynta na ka {num_to_words(denom)}"
