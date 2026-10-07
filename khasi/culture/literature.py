# -*- coding: utf-8 -*-
"""Khasi Literature, Poetry, Folklore, Legends, and Notable Authors."""

from typing import Dict, List, Any

AUTHORS: List[Dict[str, Any]] = [
    {
        "name": "U Soso Tham (1873 - 1940)",
        "title": "Father of Modern Khasi Poetry",
        "masterpiece": "Ki Sngi Barim U Hynniewtrep (1936) & Ki Poitri Khasi (1925)",
        "biography": "The national bard of the Khasi people. His philosophical verse revived deep ancestral memories, Khasi golden age ethics, and pristine highland nature."
    },
    {
        "name": "Babu Jeebon Roy (1838 - 1903)",
        "title": "Father of Modern Khasi Literature & Renaissance Pioneer",
        "masterpiece": "Ka Niam Jong Ki Khasi (1897) & Founder of Ri Khasi Press (1896)",
        "biography": "Trailblazer who established the first indigenous printing press in Shillong and wrote foundational books on Khasi religion, history, and Sanskrit translations."
    },
    {
        "name": "Radhon Singh Berry (1855 - 1904)",
        "title": "Classical Poet & Moral Philosopher",
        "masterpiece": "Ka Jingsneng Tymmen (1902 - Counsel of the Elders)",
        "biography": "Authored the definitive didactic poetic collection of moral proverbs and conduct rules governing youth, character, and societal duty."
    },
    {
        "name": "Dr. H. Lyngdoh (1877 - 1958)",
        "title": "Eminent Historian & Sociologist",
        "masterpiece": "Ka Niam Khasi (1937) & Ki Syiem Khasi bad Synteng (1938)",
        "biography": "Pioneering medical doctor and scholar who documented the detailed constitutional history of Khasi native states (Syiemships) and rituals."
    },
    {
        "name": "U Mondon Bareh (1878 - 1932)",
        "title": "Celebrated Dramatist, Educationist & Grammarian",
        "masterpiece": "Ka Drama U Mihsngi (1929) & Khasi-English Course and Grammar",
        "biography": "Distinguished scholar whose play 'Ka Drama U Mihsngi' stands as a milestone of original Khasi theatrical literature, alongside his foundational grammar and school texts."
    },
    {
        "name": "U Sib Charan Roy (1862 - 1952)",
        "title": "Nationalist Thinker, Editor & Cultural Philosopher",
        "masterpiece": "Ka Niam Ki Khasi: Ka Niam Tip-Blei Tip-Briew (1919) & Kot Tohkit Tir Tir",
        "biography": "Eldest son of Babu Jeebon Roy; fearless editor of the journal 'U Nongphira', who systematized indigenous Khasi ethical theology ('Tip Blei Tip Briew')."
    },
    {
        "name": "U Rabon Singh (c. 1840 - 1910)",
        "title": "Master Folklorist & Chronicler of Sacred Lore",
        "masterpiece": "Ka Kitab Niam-khein Ki Khasi & Ki Parom Hyndai",
        "biography": "One of the earliest and most authoritative recorders of ancient Khasi ceremonial rites, divination, folktales, and mythological traditions."
    }
]

EPICS: List[Dict[str, Any]] = [
    {
        "title": "U Sohpetbneng bad U Jingkieng Ksiar (The Navel of Heaven & Golden Ladder)",
        "theme": "Creation myth & Descent of Ki Hynniewtrep",
        "summary": "According to ancient Khasi belief, humanity originally comprised sixteen families ('Khadhynriew Trep') living in heaven. God placed a sacred Golden Vine atop Mount Sohpetbneng allowing communion between heaven and earth. Seven families ('Ki Hynniewtrep') chose to dwell on earth as caretakers of nature, while nine remained above ('Ki Khyndai Trep')."
    },
    {
        "title": "U Thlen (The Mythical Giant Serpent)",
        "theme": "Allegory of greed, cannibalistic avarice, and moral victory",
        "summary": "A terrifying demon serpent dwelling in the deep limestone caves of Sohra demanded human sacrifice and insatiable greed. The heroic folk figure U Suidnoh, with community courage and red-hot iron, slew the beast, establishing that righteous solidarity overcomes evil."
    },
    {
        "title": "Ka Nohkalikai (The Legend of Likai)",
        "theme": "Tragedy, maternal devotion, and immortal cascade",
        "summary": "The tragic chronicle of a hardworking mother named Likai whose child was slain by a jealous stepfather. Driven by grief upon discovering the horrifying truth, she leaped off the soaring limestone cliffs of Cherrapunji, forever giving her name to India's tallest plunge waterfall."
    },
    {
        "title": "Manik Raitong (The Flute of the Destitute)",
        "theme": "Immortal folk romance and soul-stirring music",
        "summary": "The story of an impoverished orphan boy whose haunting bamboo flute melodies captivated the queen. Condemned to death by fire, he played his sorrowful melody one final time atop the funeral pyre before stepping into eternity."
    }
]

POEMS: List[Dict[str, Any]] = [
    {
        "title": "Ki Sngi Barim U Hynniewtrep (Opening Lines)",
        "poet": "U Soso Tham",
        "text_khasi": "Ha shiteng pyrthei u Blei u thung / Ka Ri ban phyrnai kum ka sngi; / Na kliar ki Lum ki Wah ki tuid, / Ban kiew u Khasi sha bneng.",
        "english_translation": "In the center of the world God established / A land to shine brightly like the sun; / From mountain peaks the rivers flow, / For the Khasi to rise towards heaven."
    },
    {
        "title": "Ka Jingsneng Tymmen (Selected Verse)",
        "poet": "Radhon Singh Berry",
        "text_khasi": "Wat sngewheh ha lade, wat sngewstad ha khmat ki briew, / Ka burom ka hok kaba neh la slem; / To ri ïa ka nongtymmen ka hok bad ka jingshisha.",
        "english_translation": "Be not proud in thyself, nor boastful in human sight, / The honor of righteousness is what endures forever; / Guard the ancient heritage of truth and justice."
    }
]

def authors() -> List[Dict[str, Any]]:
    return AUTHORS

def epics() -> List[Dict[str, Any]]:
    return EPICS

def poems() -> List[Dict[str, Any]]:
    return POEMS
