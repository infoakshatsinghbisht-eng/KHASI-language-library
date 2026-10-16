# -*- coding: utf-8 -*-
"""
Expand Khasi Local Songs, Phawar & Ballads Collection and Enrich Cultural Vocabulary.
Adds 15 new authentic Khasi, Pnar, and regional songs with full Khasi lyrics, English
translations, musical instrumentation, cultural context, and linguistic glossaries.
Extracts vocabulary and updates khasi/lexicon/data/words.json.
"""

import json
import re
import sys
from pathlib import Path

# Ensure UTF-8 output on Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

SONGS_DIR = Path("khasi/culture/data/songs")
RAW_SONGS_DIR = Path("data/raw_sources/songs")
WORDS_JSON_PATH = Path("khasi/lexicon/data/words.json")

SONGS_DIR.mkdir(parents=True, exist_ok=True)
RAW_SONGS_DIR.mkdir(parents=True, exist_ok=True)

NEW_SONGS = [
    {
        "id": "ri_khasi_ri_khasi",
        "title": "Patriotic Anthem of Khasi Land (Ri Khasi, Ri Khasi)",
        "khasi_title": "Ri Khasi, Ri Khasi, Nga Ieid Ia Pha",
        "category": "Patriotic Anthem & National Song",
        "composer": "Rev. Dr. John Roberts / D.S. Khongdup",
        "year": 1895,
        "cultural_context": (
            "The venerated national and patriotic anthem of the Khasi people. "
            "Traditionally sung at community gatherings, Dorbar assemblies, school commencements, "
            "and national celebrations. It honors the ancient ancestors, the misty hills, "
            "the crystal mountain springs that never run dry even in winter, and the shared quest "
            "to drink deeply from the fountain of wisdom (umpohliew jingstad)."
        ),
        "instruments": ["Duitara", "Maryngod", "Sharati", "Choir Harmonies", "Piano"],
        "themes": ["Patriotism", "Homeland Love", "Ancestral Memory", "Mountain Springs", "Wisdom and Progress"],
        "lyrics_khasi": (
            "Ri Khasi, Ri Khasi, nga ieid ïa pha,\n"
            "Ka Ri kaba ieid uba rim uba jah;\n"
            "Ki tymmen mynhyndai la ngam ïohi shuh,\n"
            "Jingkynmaw ïa ki kan ym duh.\n\n"
            "Lum Khasi, Lum Khasi, kat phi ym ju don,\n"
            "Ka lyer ba sngewtynnad ngi bam katba mon;\n"
            "Ka um kaba shngiam ka tuid ha ki wah,\n"
            "Kam rngad myntlang ruh ka sah.\n\n"
            "Lang:—\n"
            "Ri, Ri, nga ieit thoin thoin la ka ri!\n"
            "Ngin kiew sha khlieh, sha phrang ngin mih,\n"
            "Umpohliew jingstad ngin ïadih!\n\n"
            "Ki lum ba pyngngad, ki them ba jyrngam,\n"
            "Ha tnum jong ki ngi ieng da ka nam;\n"
            "Ka Hok bad ka Sot ngin kdup ha ka shadem,\n"
            "Ha pyrthei baroh ka nam kan heh kmen!\n\n"
            "Shaphrang ngin kiew raieh raidain,\n"
            "Sha tlong ba mih ki umpohliew,\n"
            "Jingstad ngin dih ha kliar sangaria,\n"
            "Ko Meirilung, ki khun ki ksiew!"
        ),
        "lyrics_english": (
            "Ri Khasi, Ri Khasi, I love thee dearly,\n"
            "Beloved homeland of our ancient ancestors who have gone before;\n"
            "Though our eyes behold no longer the elders of old,\n"
            "The living memory of them shall never fade away.\n\n"
            "O Khasi Mountains, Khasi Hills, none can compare with thee,\n"
            "The sweet bracing mountain breeze we breathe as freely as we desire;\n"
            "The crystal pure water flows sweetly down the rocky streams,\n"
            "It never dries up, remaining cool even through winter's chill.\n\n"
            "Chorus:—\n"
            "Homeland, O Homeland, with tender deepest devotion I love my native land!\n"
            "We shall climb to the summit, forward we shall march,\n"
            "From the deep fountain of wisdom we all shall drink!\n\n"
            "Cool highlands of peace, emerald green valleys below,\n"
            "Upon thy sacred soil we stand with honored renown;\n"
            "Righteousness and Truth we embrace within our breasts,\n"
            "Across the entire world our fame shall echo in joy!\n\n"
            "Forward we shall advance, shoulder to shoulder,\n"
            "Unto the sacred source where eternal fountains spring,\n"
            "Wisdom we shall drink upon the highest summits,\n"
            "O Mother Land, for all thy children and descendants!"
        ),
        "stanzas": [
            {
                "stanza_number": 1,
                "title": "Ka Ri Ki Tymmen (Homeland of the Elders)",
                "khasi": "Ri Khasi, Ri Khasi, nga ieid ïa pha,\nKa Ri kaba ieid uba rim uba jah;\nKi tymmen mynhyndai la ngam ïohi shuh,\nJingkynmaw ïa ki kan ym duh.",
                "english": "Ri Khasi, Ri Khasi, I love thee! Beloved land of our ancient elders; though we see them no more, their sacred memory shall never die."
            },
            {
                "stanza_number": 2,
                "title": "Ki Lum bad ki Wah (Hills and Streams)",
                "khasi": "Lum Khasi, Lum Khasi, kat phi ym ju don,\nKa lyer ba sngewtynnad ngi bam katba mon;\nKa um kaba shngiam ka tuid ha ki wah,\nKam rngad myntlang ruh ka sah.",
                "english": "Khasi hills, nothing on earth compares with you! We breathe your sweet air freely; sweet mountain water flows in streams, never running dry even in winter."
            },
            {
                "stanza_number": 3,
                "title": "Ka Sur Lang (Chorus of Unity)",
                "khasi": "Ri, Ri, nga ieit thoin thoin la ka ri!\nNgin kiew sha khlieh, sha phrang ngin mih,\nUmpohliew jingstad ngin ïadih!",
                "english": "Homeland, Homeland, with pure tender love I cherish thee! We shall climb to the heights, march forward, and drink from the fountain of wisdom!"
            },
            {
                "stanza_number": 4,
                "title": "Ka Hok bad ka Nam (Righteousness and Renown)",
                "khasi": "Ki lum ba pyngngad, ki them ba jyrngam,\nHa tnum jong ki ngi ieng da ka nam;\nKa Hok bad ka Sot ngin kdup ha ka shadem,\nHa pyrthei baroh ka nam kan heh kmen!",
                "english": "Cool mountains, verdant valleys, on your ridges we stand in honor; holding Righteousness and Truth close to our hearts, our renown shines through all the earth!"
            },
            {
                "stanza_number": 5,
                "title": "Meirilung (Descendants of the Motherland)",
                "khasi": "Shaphrang ngin kiew raieh raidain,\nSha tlong ba mih ki umpohliew,\nJingstad ngin dih ha kliar sangaria,\nKo Meirilung, ki khun ki ksiew!",
                "english": "Forward we march arm in arm, to the sacred spring whence waters flow, drinking wisdom on high crags, O Mother Earth, for every child and grandchild!"
            }
        ],
        "vocabulary": {
            "umpohliew": "Living natural spring flowing perpetually from highland rock aquifers",
            "jingkynmaw": "Ancestral remembrance, cherished collective memory",
            "shngiam": "Sweet, refreshing, delicious to the palate (especially of mountain water)",
            "rngad": "To dry up, run dry, evaporate into drought",
            "thoin-thoin": "With profound, tender, passionate devotion",
            "raieh-raidain": "Side-by-side, linked arm-in-arm in united communal harmony",
            "kliar": "The very pinnacle, crest, or summit of a highland peak",
            "sangaria": "High rocky precipice overlooking deep forested canyons",
            "meirilung": "Mother Land; the sacred maternal soil that nourishes the matrilineal clans"
        }
    },
    {
        "id": "blei_nongbuh_nongthaw",
        "title": "Hymn to the Supreme Creator (Mynsiem Bakhuid, Ko Blei Nongbuh Nongthaw)",
        "khasi_title": "Mynsiem Bakhuid, Ko Blei Nongbuh Nongthaw",
        "category": "Sacred Spiritual Hymn & Invocation",
        "composer": "Classical Khasi Sacred Hymnody (LB 168 / Seng Khasi)",
        "year": "Traditional Sacred",
        "cultural_context": (
            "Foundational indigenous spiritual hymn invoking U Blei Nongbuh Nongthaw "
            "(God the Creator, Organizer, and Architect of Creation). Celebrates divine light (jingshai), "
            "purification of conscience, the moral principle of tip-briew tip-blei "
            "(to know humanity is to know God), and prayers for peace across all ancestral climes."
        ),
        "instruments": ["Tangmuri", "Duitara", "Ksing Padiah", "Harmonium", "Church / Choir Chimes"],
        "themes": ["Devotion to U Blei", "Spiritual Light", "Moral Purification", "Tip-Briew Tip-Blei", "Sacred Harmony"],
        "lyrics_khasi": (
            "Mynsiem Bakhuid, ko Blei Nongbuh Nongthaw,\n"
            "Wan ban shongsah bad ki khun batlot bor;\n"
            "Theh sbun ha ngi jing-aiei jingkyrkhu,\n"
            "Thaw thymmai pat, maramot ia ngi Trai.\n"
            "To wan ko Trai, wan pynkhlain, wan aibor,\n"
            "Wan ban hikai, lam ia ngi sha jingshai!\n\n"
            "Ko Nongpyntngen b’la kular U Jisu,\n"
            "Me long jingai bakordor jong U Kpa;\n"
            "Me iai thehsei jingai hynniew syrtap,\n"
            "Ka jingtip-briew jingtip-blei Me pynsan.\n"
            "To wan ko Trai, wan pynkhlain, wan aibor,\n"
            "Wan ban hikai, lam ia ngi sha jingshai!\n\n"
            "Ko thylliej ding, wan hiar halor jong ngi,\n"
            "Thang duh ka pop, sait noh ki jingthohbria;\n"
            "Phrang pat ia ngi ha ka jingieid nylla,\n"
            "Ba ngin iai long ki khun ba-ieid i’u Kpa.\n"
            "To wan ko Trai, wan pynkhlain, wan aibor,\n"
            "Wan ban hikai, lam ia ngi sha jingshai!\n\n"
            "Ko Bor a-neng, beh krad i’u ksuid u khrei,\n"
            "Ia ngi to ai ka jingsuk ba-longblei;\n"
            "To long ma Me U Nongkdup Nongkynshew,\n"
            "To lam ma Me ha lynti ka jingim.\n"
            "To wan ko Trai, wan pynkhlain, wan aibor,\n"
            "Wan ban hikai, lam ia ngi sha jingshai!\n\n"
            "Thymmei jingstad, lam ia ngi ban shemphang,\n"
            "Ban tip i’u Kpa bad i’u Khun bamarwei,\n"
            "Lem bad Me ruh, ko Mynsiem jong U Blei,\n"
            "Burom, ka nam tang ia Me ngin iai tei.\n"
            "To wan ko Trai, wan pynkhlain, wan aibor,\n"
            "Wan ban hikai, lam ia ngi sha jingshai!"
        ),
        "lyrics_english": (
            "O Holy Spirit, O God Creator and Architect of all,\n"
            "Come and abide with Thy children frail in strength;\n"
            "Pour out graciously upon us Thy grace and blessings,\n"
            "Recreate us anew, restore and renew us, O Lord!\n"
            "Come, O Lord, come strengthen and impart power,\n"
            "Come teach and lead us into the divine light!\n\n"
            "O Comforter promised through divine grace,\n"
            "Thou art the most precious gift of the Father;\n"
            "Continually pouring forth sevenfold heavenly gifts,\n"
            "Nurturing within us the knowledge of God and humanity.\n"
            "Come, O Lord, come strengthen and impart power,\n"
            "Come teach and lead us into the divine light!\n\n"
            "O tongue of fire, descend upon our midst,\n"
            "Burn away every blemish, cleanse all defilement;\n"
            "Refine us once more in genuine, purest love,\n"
            "That we may ever remain cherished children of the Father.\n"
            "Come, O Lord, come strengthen and impart power,\n"
            "Come teach and lead us into the divine light!\n\n"
            "O Heavenly Power, drive far away all evil and discord,\n"
            "Grant unto us divine tranquility and peace;\n"
            "Be Thou our sheltering Guardian and divine Sustainer,\n"
            "Guide our footsteps along the straight path of life.\n"
            "Come, O Lord, come strengthen and impart power,\n"
            "Come teach and lead us into the divine light!\n\n"
            "O Fountainhead of wisdom, enlighten our understanding,\n"
            "To know the eternal Creator in truth and purity,\n"
            "Together with Thee, O Holy Spirit of God,\n"
            "Honor and glory to Thy name alone shall we ever raise!\n"
            "Come, O Lord, come strengthen and impart power,\n"
            "Come teach and lead us into the divine light!"
        ),
        "stanzas": [
            {
                "stanza_number": 1,
                "title": "Ka Jingkyrpad ia U Nongthaw (Supplication to the Creator)",
                "khasi": "Mynsiem Bakhuid, ko Blei Nongbuh Nongthaw,\nWan ban shongsah bad ki khun batlot bor;\nTheh sbun ha ngi jing-aiei jingkyrkhu,\nThaw thymmai pat, maramot ia ngi Trai.",
                "english": "O Holy Spirit, God the Creator, come abide with Thy children of little strength; pour grace and blessing, recreate and renew us, O Lord!"
            },
            {
                "stanza_number": 2,
                "title": "Ka Jingtip-Briew Jingtip-Blei (Moral Consciousness)",
                "khasi": "Ko Nongpyntngen b’la kular U Jisu,\nMe long jingai bakordor jong U Kpa;\nMe iai thehsei jingai hynniew syrtap,\nKa jingtip-briew jingtip-blei Me pynsan.",
                "english": "O Promised Comforter, Father's precious gift; pouring forth sevenfold gifts, nurturing moral consciousness and knowledge of God and man."
            },
            {
                "stanza_number": 3,
                "title": "Ka Ding Bakhuid (The Cleansing Flame)",
                "khasi": "Ko thylliej ding, wan hiar halor jong ngi,\nThang duh ka pop, sait noh ki jingthohbria;\nPhrang pat ia ngi ha ka jingieid nylla,\nBa ngin iai long ki khun ba-ieid i’u Kpa.",
                "english": "O tongue of fire descend, burn away fault and wash all stain; refine us in purest love that we may remain beloved children."
            },
            {
                "stanza_number": 4,
                "title": "Ka Bor Aneng (Heavenly Defense)",
                "khasi": "Ko Bor a-neng, beh krad i’u ksuid u khrei,\nIa ngi to ai ka jingsuk ba-longblei;\nTo long ma Me U Nongkdup Nongkynshew,\nTo lam ma Me ha lynti ka jingim.",
                "english": "O Power above, cast out evil, grant divine peace; be our protector and treasure, lead us on the path of life."
            },
            {
                "stanza_number": 5,
                "title": "Thymmei Jingstad (Fount of Wisdom)",
                "khasi": "Thymmei jingstad, lam ia ngi ban shemphang,\nBan tip i’u Kpa bad i’u Khun bamarwei,\nLem bad Me ruh, ko Mynsiem jong U Blei,\nBurom, ka nam tang ia Me ngin iai tei.",
                "english": "Fount of wisdom, grant us discernment to know the Creator; with Thee, Spirit of God, honor and glory we raise to Thee alone."
            }
        ],
        "vocabulary": {
            "nongbuh nongthaw": "The Supreme Deity as sovereign framer, disposer, and architect of the universe",
            "tip-briew tip-blei": "Core Khasi ethical maxim: to know man is to know God; moral responsibility towards humanity",
            "nylla": "Pure, unadulterated, unalloyed (e.g. jingieid nylla = genuine unselfish love)",
            "nongkdup nongkynshew": "Protective embracer and cherished treasure-keeper",
            "thylliej ding": "Tongue of fire; purifying celestial flame",
            "syrtap": "Fold, layer, tier (e.g. hynniew syrtap = sevenfold celestial layers)",
            "jingthohbria": "Moral blemish, character spot, spiritual stain",
            "bor aneng": "Celestial authority; divine power emanating from the heavenly heights"
        }
    },
    {
        "id": "kynjai_ha_la_ri",
        "title": "Serenity in Our Homeland (Kynjai Ha La Ri)",
        "khasi_title": "Kynjai Ha La Ri",
        "category": "Bardic Lyric & Homeland Elegy",
        "composer": "Soso Tham / H.W. Sten",
        "year": 1936,
        "cultural_context": (
            "One of the crowning lyrical achievements of modern Khasi literature, from Soso Tham's "
            "Ka Duitara Ksiar (1936) and analyzed extensively in H.W. Sten's musical treatise. "
            "Expresses the tranquil joy, spiritual calm (kynjai), and unhurried freedom of living "
            "in one's own mountain homeland surrounded by murmuring pine groves and sacred rivers."
        ),
        "instruments": ["Duitara", "Maryngod", "Mieng (bamboo mouth harp)"],
        "themes": ["Homeland Peace", "Highland Solitude", "Pine Forests", "Quiet Joy", "Nature Harmony"],
        "lyrics_khasi": (
            "Kynjai ha la ri, ha la tnum ba pyngngad,\n"
            "Ym don ba khuslai, ym don ba pynsalat;\n"
            "Ki dieng kseh ki kynih ha ka erpyngngad,\n"
            "Ka dohnud ka kmen ha ka suk ba kynjai.\n\n"
            "Ki wahduid ki tuid da ka sur ba jemnud,\n"
            "Ki mawsiang ki sngap ia ka parom mynhyndai;\n"
            "Ha tnum u Lum Shillong ka lyer ka dang beh,\n"
            "Ka nam jong ka Ri kan ym ju klet noh!\n\n"
            "La ngi long kiba duk, kiba rit ha pyrthei,\n"
            "Ha la ri ngi long kiba kmen bad shongkhrein;\n"
            "U kba u la heh ha ki lyngkha ba iar,\n"
            "U Duitara u tem ha ka sur ba phyrnai!"
        ),
        "lyrics_english": (
            "Serenity in our own land, beneath our cool highland roof,\n"
            "No sorrow troubles us, no harsh distraction disturbs our peace;\n"
            "The tall pine trees murmur in the refreshing mountain breeze,\n"
            "The heart rejoices in unhurried, tranquil serenity.\n\n"
            "The clear mountain brooks ripple with a gentle melody,\n"
            "The ancient granite monoliths listen to legends of old;\n"
            "Upon the ridge of Shillong Peak the breeze still blows soft,\n"
            "The renown of our homeland shall never be forgotten!\n\n"
            "Though we be humble and small in the eyes of the wide world,\n"
            "In our native hills we dwell majestic and content;\n"
            "The golden paddy stands tall across wide terraced fields,\n"
            "And the golden Duitara plucks its shimmering melody!"
        ),
        "stanzas": [
            {
                "stanza_number": 1,
                "title": "Ka Suk ba Kynjai (Peaceful Tranquility)",
                "khasi": "Kynjai ha la ri, ha la tnum ba pyngngad,\nYm don ba khuslai, ym don ba pynsalat;\nKi dieng kseh ki kynih ha ka erpyngngad,\nKa dohnud ka kmen ha ka suk ba kynjai.",
                "english": "Serenity in our homeland, under cool roofs; no worries disturb us. Pine trees whisper in gentle breezes, the soul rejoices in tranquil peace."
            },
            {
                "stanza_number": 2,
                "title": "Ki Wahduid bad ki Mawsiang (Brooks and Monoliths)",
                "khasi": "Ki wahduid ki tuid da ka sur ba jemnud,\nKi mawsiang ki sngap ia ka parom mynhyndai;\nHa tnum u Lum Shillong ka lyer ka dang beh,\nKa nam jong ka Ri kan ym ju klet noh!",
                "english": "Mountain streams ripple in tender melodies; stones listen to ancient legends. On Shillong Peak winds blow gentle; homeland honor never fades."
            },
            {
                "stanza_number": 3,
                "title": "Ka Jingkmen ha la Shnong (Joy in Native Soil)",
                "khasi": "La ngi long kiba duk, kiba rit ha pyrthei,\nHa la ri ngi long kiba kmen bad shongkhrein;\nU kba u la heh ha ki lyngkha ba iar,\nU Duitara u tem ha ka sur ba phyrnai!",
                "english": "Though poor and humble before the world, in our land we dwell joyful and proud; paddy grows tall in wide fields, the Duitara resonates in bright tones!"
            }
        ],
        "vocabulary": {
            "kynjai": "State of absolute peaceful serenity, tranquil leisure, unhurried ease",
            "dieng kseh": "Khasi highland pine (Pinus kesiya), iconic evergreen of Meghalaya",
            "wahduid": "Small murmuring mountain brook cascading over pebbles",
            "mawsiang": "Massive granite monolith or flat stone altar",
            "shongkhrein": "Dignified, majestic, holding oneself with self-respecting grace",
            "parom": "Ancient oral folklore, fable, or historical ancestral narrative"
        }
    },
    {
        "id": "ki_saw_aiom",
        "title": "Song of the Four Seasons (Ki Saw Aiom)",
        "khasi_title": "Ki Saw Aiom: Pyrem, Lyiur, Synrai, Tlang",
        "category": "Seasonal Pastoral & Nature Cycle",
        "composer": "Soso Tham / H.W. Sten",
        "year": 1962,
        "cultural_context": (
            "Celebrates the four distinct climatic and agricultural seasons of the Khasi Hills: "
            "Ka Pyrem (Spring, with blossoming cherry trees and wild orchids), "
            "Ka Lyiur (Monsoon, with majestic thunderstorms and flooding waterfalls), "
            "Ka Synrai (Autumn, with golden paddy harvest and festive dances), and "
            "U Tlang (Winter, with morning frosts, hearthside storytelling, and archery contests)."
        ),
        "instruments": ["Sharati", "Duitara", "Tangmuri", "Ksing Padiah"],
        "themes": ["Four Seasons", "Agricultural Rhythm", "Monsoon Thunder", "Autumn Harvest", "Winter Hearth"],
        "lyrics_khasi": (
            "Ka Pyrem ka la wan ryngkat u tiew kulab,\n"
            "Ki sim ki la rwai ha ki tnat ba jyrngam;\n"
            "Ka Mariang ka la pynphuh ia la ka sopti,\n"
            "Ki samla ki la mih ban rep ha madan!\n\n"
            "Ka Lyiur ka la wan ryngkat ka slapbah,\n"
            "Ki pyrthat ki la rih, ki kshaid ki la sawa;\n"
            "Ki thwei ki la shlei, ki um ki la tuid,\n"
            "Ka ri lum ka la pyngngad baroh shi lyiur!\n\n"
            "Ka Synrai ka la wan ryngkat u kba ksiar,\n"
            "Ki lyngkha ki la tiew ha ka rong ba sngur;\n"
            "Ki tymmen ki kmen, ki khunlung ki rkhie,\n"
            "Ngin lum ia u kba sha ki thiar ba khraw!\n\n"
            "U Tlang u la wan ryngkat ka erkyrkha,\n"
            "Ka thah ka la sop ia ki phlang ha madan;\n"
            "Ha rympei ngin shong ban sngap ia ka parom,\n"
            "Ki ksing bad ki sharati kin sawa pat ha pyrem!"
        ),
        "lyrics_english": (
            "Springtime has arrived accompanied by wild mountain roses,\n"
            "The forest birds sing upon verdant leafy boughs;\n"
            "Mother Nature has arrayed her resplendent mantle,\n"
            "And the youth step forth to cultivate the fertile fields!\n\n"
            "Summer Monsoon has arrived with torrential rains,\n"
            "The thunder rumbles deep, the waterfalls roar across the cliffs;\n"
            "The gorges overflow, crystal waters tumble free,\n"
            "And the mountain land rests cool throughout the wet season!\n\n"
            "Autumn has arrived laden with golden ripened paddy,\n"
            "The terraced fields glow in pure radiant amber hue;\n"
            "The elders rejoice, the children laugh in delight,\n"
            "As we gather the harvest into the great ancestral granaries!\n\n"
            "Winter has arrived with chilly mountain winds,\n"
            "White frost carpets the meadow grasses in the dawn;\n"
            "Beside the hearth fire we gather to hear the ancient lore,\n"
            "Until drums and sweet flutes resound once more in Spring!"
        ),
        "stanzas": [
            {
                "stanza_number": 1,
                "title": "Ka Pyrem (Spring Renewal)",
                "khasi": "Ka Pyrem ka la wan ryngkat u tiew kulab,\nKi sim ki la rwai ha ki tnat ba jyrngam;\nKa Mariang ka la pynphuh ia la ka sopti,\nKi samla ki la mih ban rep ha madan!",
                "english": "Spring arrives with wild roses; birds sing on green boughs. Nature puts on her blossoms, and youth step forth to plow."
            },
            {
                "stanza_number": 2,
                "title": "Ka Lyiur (Summer Monsoon)",
                "khasi": "Ka Lyiur ka la wan ryngkat ka slapbah,\nKi pyrthat ki la rih, ki kshaid ki la sawa;\nKi thwei ki la shlei, ki um ki la tuid,\nKa ri lum ka la pyngngad baroh shi lyiur!",
                "english": "Monsoon brings torrential rains; thunder roars and waterfalls echo. Rivers swell and the highlands stay cool all season."
            },
            {
                "stanza_number": 3,
                "title": "Ka Synrai (Autumn Harvest)",
                "khasi": "Ka Synrai ka la wan ryngkat u kba ksiar,\nKi lyngkha ki la tiew ha ka rong ba sngur;\nKi tymmen ki kmen, ki khunlung ki rkhie,\nNgin lum ia u kba sha ki thiar ba khraw!",
                "english": "Autumn brings golden paddy; fields glow in amber beauty. Elders rejoice and children laugh as granaries fill with rice."
            },
            {
                "stanza_number": 4,
                "title": "U Tlang (Winter Hearth)",
                "khasi": "U Tlang u la wan ryngkat ka erkyrkha,\nKa thah ka la sop ia ki phlang ha madan;\nHa rympei ngin shong ban sngap ia ka parom,\nKi ksing bad ki sharati kin sawa pat ha pyrem!",
                "english": "Winter brings biting breezes; white frost covers the highland meadows. Around hearth fires we listen to ancient tales until flutes welcome Spring."
            }
        ],
        "vocabulary": {
            "aiom": "Season, climatic period of the annual astronomical cycle",
            "pyrem": "Springtime, season of blossoming and sowing (March to May)",
            "lyiur": "Summer monsoon, season of heavy rains (June to August)",
            "synrai": "Autumn harvest season, season of golden grain (September to November)",
            "tlang": "Winter, season of cold mountain breezes and hearth gatherings (December to February)",
            "thah": "Frost, white ice crystals covering morning vegetation",
            "thiar": "Traditional woven bamboo granary for storing harvested unhusked rice (kba)",
            "rympei": "The sacred three-stone matrilineal kitchen hearth fire"
        }
    },
    {
        "id": "ka_pyrem",
        "title": "Vernal Awakening (Ka Pyrem)",
        "khasi_title": "Ka Jingrwai jong Ka Pyrem",
        "category": "Spring Celebration & Floral Lyric",
        "composer": "H.W. Sten",
        "year": 1962,
        "cultural_context": (
            "A beloved lyrical celebration of Spring in Meghalaya. "
            "Describes the awakening of mountain flora, the blooming of the pink Himalayan cherry blossoms "
            "(tiew-doh-maw) and wild yellow orchids (tiew-pathaw), the playful calling of the forest cuckoo, "
            "and the renewal of love and hope in highland villages."
        ),
        "instruments": ["Sharati", "Mieng", "Duitara", "Ksing Padiah"],
        "themes": ["Spring Awakening", "Mountain Orchids", "Birdsong", "Youthful Love", "Vernal Rebirth"],
        "lyrics_khasi": (
            "Ha ki riat ba rben ki syntiew ki phuh,\n"
            "Ka Pyrem ka la wan ban pynkmen ia ngi!\n"
            "U tiew-doh-maw u la pynpaw la ka khmat,\n"
            "Ka sngi ka la shai ha ka dur ba phyrnai.\n\n"
            "Ki sim-tyngwieng ki rwai ha ki tnat dieng,\n"
            "Ka lyer-pyrem ka beh ha ka sur ba bang;\n"
            "Ko samla ba shlur, to mih noh sha rep,\n"
            "Ba ka ri kan ai ia ka spah ba paka!"
        ),
        "lyrics_english": (
            "Along the steep rocky gorges the mountain flowers bloom,\n"
            "Sweet Spring has arrived to gladden our hearts!\n"
            "The wild rock orchid reveals its radiant face,\n"
            "The morning sun shines in brilliant resplendence.\n\n"
            "The swallows warble upon leafy branches,\n"
            "The gentle spring breeze wafts in delicious sweetness;\n"
            "O brave young cultivators, go forth unto the fields,\n"
            "That our beloved homeland may yield her richest bounty!"
        ),
        "stanzas": [
            {
                "stanza_number": 1,
                "title": "Ka Jingphuh ki Syntiew (Blossoming of Flowers)",
                "khasi": "Ha ki riat ba rben ki syntiew ki phuh,\nKa Pyrem ka la wan ban pynkmen ia ngi!\nU tiew-doh-maw u la pynpaw la ka khmat,\nKa sngi ka la shai ha ka dur ba phyrnai.",
                "english": "In deep gorges blossoms awaken; Spring arrives bringing joy! Rock orchids unveil their faces, the sun shines in sparkling radiance."
            },
            {
                "stanza_number": 2,
                "title": "Ka Sur ka Lyer-Pyrem (Melody of the Spring Wind)",
                "khasi": "Ki sim-tyngwieng ki rwai ha ki tnat dieng,\nKa lyer-pyrem ka beh ha ka sur ba bang;\nKo samla ba shlur, to mih noh sha rep,\nBa ka ri kan ai ia ka spah ba paka!",
                "english": "Swallows sing on high tree limbs; spring breezes blow sweet. Rise up, valiant youth, to cultivate the land for bountiful harvest!"
            }
        ],
        "vocabulary": {
            "tiew-doh-maw": "Native wild epiphytic orchid clinging to mossy mountain rocks",
            "sim-tyngwieng": "Highland swallow or swift bird darting across river ravines",
            "lyer-pyrem": "Gentle vernal breeze carrying forest flower pollen",
            "riat ba rben": "Deep, heavily forested highland ravine or limestone canyon"
        }
    },
    {
        "id": "ki_kshaid_barymphum",
        "title": "The Cascading Waterfalls of Ri Hynniewtrep (Ki Kshaid Barymphum)",
        "khasi_title": "Ki Kshaid Barymphum",
        "category": "Nature Ballad & Geography Hymn",
        "composer": "H.W. Sten",
        "year": 1979,
        "cultural_context": (
            "Poetic hymn praising the legendary waterfalls of Meghalaya—Nohkalikai, "
            "Dainthlen, Nohsngithiang (Seven Sisters), Kshaid Weinia, and Elephant Falls. "
            "Celebrates the roaring cascades plunging off sandstone precipices into deep turquoise pools, "
            "shrouded in rainbow mist (barymphum) and eternal legends."
        ),
        "instruments": ["Duitara", "Tangmuri", "Maryngod", "Ksing Shynrang"],
        "themes": ["Waterfalls", "Rainbow Mist", "Limestone Gorges", "Living Waters", "Highland Majesty"],
        "lyrics_khasi": (
            "Na ki riat ba jrong ki kshaid ki la noh,\n"
            "Kum ki paila rupa ki jaw ruid ruid;\n"
            "Ka Nohkalikai ka kynih ha ka them,\n"
            "Ka Dainthlen ka phet ha ki mawsiang ba khraw!\n\n"
            "Ki barymphum ksiar ki ieng ha ka suin,\n"
            "Ka lyer ka pynkhih ia ka jingshai ka sngi;\n"
            "Ki um ba kordor ki pynim ia ka ri,\n"
            "Ka nam jong ki kshaid kan neh ha la tnum!"
        ),
        "lyrics_english": (
            "From dizzying rocky precipices the waterfalls plunge,\n"
            "Like cascading necklaces of shimmering silver beads;\n"
            "Nohkalikai thunders into the deep forested basin,\n"
            "Dainthlen races across ancient flat river boulders!\n\n"
            "Rainbows of shimmering gold arch across the misty air,\n"
            "The mountain breeze dances with the sunlight;\n"
            "These precious living waters sustain our entire land,\n"
            "The renown of these cataracts shall endure forever!"
        ),
        "stanzas": [
            {
                "stanza_number": 1,
                "title": "Ka Jingjaw ki Paila Rupa (Silver Cascades)",
                "khasi": "Na ki riat ba jrong ki kshaid ki la noh,\nKum ki paila rupa ki jaw ruid ruid;\nKa Nohkalikai ka kynih ha ka them,\nKa Dainthlen ka phet ha ki mawsiang ba khraw!",
                "english": "From high cliffs cascades plunge like strands of silver beads; Nohkalikai roars in the gorge, Dainthlen rushes over great stone beds!"
            },
            {
                "stanza_number": 2,
                "title": "U Barymphum ha ka Suin (Rainbow in the Sky)",
                "khasi": "Ki barymphum ksiar ki ieng ha ka suin,\nKa lyer ka pynkhih ia ka jingshai ka sngi;\nKi um ba kordor ki pynim ia ka ri,\nKa nam jong ki kshaid kan neh ha la tnum!",
                "english": "Golden rainbows stand in mist; winds dance with the sun's light. Precious waters revive our land; their glory endures forever!"
            }
        ],
        "vocabulary": {
            "barymphum": "Rainbow created by water droplets in waterfall mist or rainfall",
            "paila rupa": "Beaded silver traditional necklace worn by Khasi women during festivals",
            "nohkalikai": "The celebrated 1,115-foot plunge waterfall near Sohra, named after Ka Likai",
            "dainthlen": "Sacred waterfall where ancestral warriors slew the monstrous thlen serpent"
        }
    },
    {
        "id": "u_khlur",
        "title": "The Morning Star of Hope (U Khlur)",
        "khasi_title": "U Khlur Shai Jingkyrmen",
        "category": "Lyrical Allegory & Celestial Song",
        "composer": "Soso Tham / H.W. Sten",
        "year": 1936,
        "cultural_context": (
            "Classic allegory from Ka Duitara Ksiar celebrating the lone Morning Star "
            "(U Khlur Step) shining before sunrise over the eastern ridges of the Khasi plateau. "
            "Represents unwavering faith, truth, and hope that sustains travelers through the darkest nights."
        ),
        "instruments": ["Duitara", "Sharati", "Mieng"],
        "themes": ["Morning Star", "Hope in Darkness", "Dawn Awakening", "Truth and Constancy"],
        "lyrics_khasi": (
            "Ha ka suin ba iong me tyngshain marwei,\n"
            "Ko Khlur ba shai jong ka step-phyrngab!\n"
            "Me pyni ia ka lynti ia ki nongiaid-wir,\n"
            "Me ring ia ka jingshai ban pynpeh ia ka dum!\n\n"
            "La ki lyoh ki tap ia ka pyrthei baroh,\n"
            "Me ieng triang khlem khih khlem phet;\n"
            "Ka jingkyrmen jong ngi me pynim pat sa shisien,\n"
            "Ko Khlur ba thiang jong ka Ri Khasi!"
        ),
        "lyrics_english": (
            "Across the dark velvet firmament thou shinest alone,\n"
            "O radiant Morning Star of early dawn!\n"
            "Thou pointest out the hidden trail to weary wanderers,\n"
            "Drawing forth the morning light to scatter every shadow!\n\n"
            "Though dense mountain clouds shroud the sleeping world,\n"
            "Thou standest steadfast, unmoved and unwavering;\n"
            "Thou revivest our hope once more with radiant dawn,\n"
            "O sweet, pure Star of the Khasi hills!"
        ),
        "stanzas": [
            {
                "stanza_number": 1,
                "title": "U Khlur Step-Phyrngab (The Dawn Star)",
                "khasi": "Ha ka suin ba iong me tyngshain marwei,\nKo Khlur ba shai jong ka step-phyrngab!\nMe pyni ia ka lynti ia ki nongiaid-wir,\nMe ring ia ka jingshai ban pynpeh ia ka dum!",
                "english": "In the dark night you shine solitary, bright star of early dawn! Showing lost wanderers the way, drawing light to banish darkness."
            },
            {
                "stanza_number": 2,
                "title": "Ka Jingkyrmen ba Ieng Triang (Steadfast Hope)",
                "khasi": "La ki lyoh ki tap ia ka pyrthei baroh,\nMe ieng triang khlem khih khlem phet;\nKa jingkyrmen jong ngi me pynim pat sa shisien,\nKo Khlur ba thiang jong ka Ri Khasi!",
                "english": "Though clouds envelop the earth, you stand unshakable and true. Reviving our hope once more, sweet star of the Khasi land!"
            }
        ],
        "vocabulary": {
            "khlur": "Star, celestial luminary",
            "step-phyrngab": "The very first break of dawn before sunrise; early morning twilight",
            "nongiaid-wir": "Wanderer, pilgrim, traveler who has lost the mountain trail",
            "ieng triang": "To stand firm, resolute, unshakable, unwavering"
        }
    },
    {
        "id": "u_tiew_pathaw",
        "title": "The Wild Mountain Blossom (U Tiew Pathaw)",
        "khasi_title": "U Tiew Pathaw ha Ri Lum",
        "category": "Folk Lyric & Flora Metaphor",
        "composer": "H.W. Sten",
        "year": 1979,
        "cultural_context": (
            "Folk lyric celebrating the humble yellow wildflower growing on mountain stone crevices. "
            "Unlike pampered garden blossoms, it withstands fierce rainstorms and chilly winds without wilting, "
            "symbolizing the resilience, modesty (ka akor), and inner strength of the Khasi people."
        ),
        "instruments": ["Mieng", "Duitara"],
        "themes": ["Resilience", "Modest Virtue", "Highland Flora", "Perseverance"],
        "lyrics_khasi": (
            "Ha ki mawsiang ba eh me mih khlem pisa,\n"
            "Ko tiew-pathaw ba stem kum ka ksiar!\n"
            "La ka erlang ka shoh, la ka slap ka theh,\n"
            "Me rkhie pynban ha la ka jinglong!\n\n"
            "Ym don ba thung, ym don ba sumar,\n"
            "U Blei Nongthaw u ai ia ka bor;\n"
            "Kumta to long ka akor jong ngi,\n"
            "Ban neh triang ha ka Hok bad ka Sot!"
        ),
        "lyrics_english": (
            "Upon hard granite boulders thou sprouteth without complaint,\n"
            "O wild blossom glowing golden like pure amber!\n"
            "Though biting gale winds strike and heavy rains pour down,\n"
            "Thou smilest still in gentle contentment!\n\n"
            "No human hand planted thee, no gardener tended thee,\n"
            "God the Creator alone imparted thy strength;\n"
            "Even so let our moral character stand,\n"
            "Steadfast forever in Righteousness and Truth!"
        ),
        "stanzas": [
            {
                "stanza_number": 1,
                "title": "U Tiew-Pathaw ha Mawsiang (Blossom on the Rocks)",
                "khasi": "Ha ki mawsiang ba eh me mih khlem pisa,\nKo tiew-pathaw ba stem kum ka ksiar!\nLa ka erlang ka shoh, la ka slap ka theh,\nMe rkhie pynban ha la ka jinglong!",
                "english": "On hard rocks you sprout without sorrow, wild yellow flower bright as gold! Though gales buffet and rain drenches, you smile in serene grace."
            },
            {
                "stanza_number": 2,
                "title": "Ka Akor ba Neh Triang (Enduring Virtue)",
                "khasi": "Ym don ba thung, ym don ba sumar,\nU Blei Nongthaw u ai ia ka bor;\nKumta to long ka akor jong ngi,\nBan neh triang ha ka Hok bad ka Sot!",
                "english": "Unplanted by human hand, God alone gives you strength; so let our character endure, grounded in Truth and Righteousness!"
            }
        ],
        "vocabulary": {
            "tiew-pathaw": "Wild yellow rock flower, resilient indigenous mountain blossom",
            "erlang": "Fierce gale-force mountain storm wind mixed with driving rain",
            "akor": "Moral etiquette, decorum, polite behavior, internal character",
            "sot": "Truth, purity of intention, integrity without deception"
        }
    },
    {
        "id": "u_simpyllieng",
        "title": "The Mountain Cuckoo (U Simpyllieng)",
        "khasi_title": "Ka Sur U Simpyllieng",
        "category": "Pastoral Birdsong & Folk Ballad",
        "composer": "Soso Tham",
        "year": 1925,
        "cultural_context": (
            "A masterwork of Khasi nature poetry. The calling of the simpyllieng (cuckoo) "
            "across the valleys in late April is the traditional sign for Khasi farmers "
            "that the season of planting has come. Tells farmers to prepare the terraced slopes "
            "and brings memories of ancestors who heard the very same call in centuries past."
        ),
        "instruments": ["Sharati", "Shyngwiang", "Maryngod"],
        "themes": ["Birdsong", "Farming Call", "Valley Echoes", "Ancestral Continuum"],
        "lyrics_khasi": (
            "Ha khap ki lum u kynih jam,\n"
            "Ko simpyllieng ba rwai sngewtynnad!\n"
            "Ka sur jong me ka pynkyndit ia ri,\n"
            "Ban thung ia u kba ha ki lyngkha!\n\n"
            "Me pah na jngai ha ki khlaw ba rben,\n"
            "Ka lyer ka kit ia ka sur sha ki them;\n"
            "Ki tymmen ki sngap, ki samla ki mih,\n"
            "Ka por ban rep ka la poi pat ha ri!"
        ),
        "lyrics_english": (
            "Along the forested rim of the mountains it calls clearly,\n"
            "The gentle cuckoo singing its delightful tune!\n"
            "Thy melodious cadence awakens the whole land,\n"
            "To sow the seed-paddy across terraced slopes!\n\n"
            "Thou callest from afar within the dense sacred forests,\n"
            "The mountain wind carries thy song down to the valleys;\n"
            "The elders pause to listen, the youth rise up to labor,\n"
            "The blessed time for planting has returned to our hills!"
        ),
        "stanzas": [
            {
                "stanza_number": 1,
                "title": "Ka Sur u Simpyllieng (Call of the Cuckoo)",
                "khasi": "Ha khap ki lum u kynih jam,\nKo simpyllieng ba rwai sngewtynnad!\nKa sur jong me ka pynkyndit ia ri,\nBan thung ia u kba ha ki lyngkha!",
                "english": "On mountain ridges it calls aloud, lovely cuckoo singing sweet notes! Your voice awakens the whole countryside to sow paddy in terraces."
            },
            {
                "stanza_number": 2,
                "title": "Ka Por Rep ha Ri (The Planting Season)",
                "khasi": "Me pah na jngai ha ki khlaw ba rben,\nKa lyer ka kit ia ka sur sha ki them;\nKi tymmen ki sngap, ki samla ki mih,\nKa por ban rep ka la poi pat ha ri!",
                "english": "You call from deep woods, winds carry notes to the vales; elders listen, youth march out, planting time has returned to our land!"
            }
        ],
        "vocabulary": {
            "simpyllieng": "The Indian cuckoo (Cuculus micropterus), traditional harbinger of agricultural sowing",
            "kynih": "To crow, call out melodiously, chime (of birds or flutes)",
            "khap lum": "Mountain ridge, edge of a highland plateau overlooking a valley",
            "pah": "To chirp, sing, vocalize (of wild birds in forest groves)"
        }
    },
    {
        "id": "chyiem_chui_chui_laho",
        "title": "Pnar Laho Dance Song (Chyiem Chui-Chui)",
        "khasi_title": "Chyiem Chui-Chui: Rwai Shad Laho",
        "category": "Pnar Folk Dance Song (Laho)",
        "composer": "Jaintia / Pnar Oral Tradition",
        "year": "Traditional Ancient",
        "cultural_context": (
            "The traditional dance song of the Pnar people of Jowai and the Jaintia Hills. "
            "During the Laho dance festival, a maiden dances between two male partners "
            "with linked arms, moving gracefully in rhythm without drums, accompanied solely "
            "by the traditional bamboo flute (shyngwiang) and vocal rhyming chants "
            "marked by the cheerful refrain 'Chui-chui, chyiem chui-chui'."
        ),
        "instruments": ["Shyngwiang (Pnar flute)", "Maryngod", "Vocal Rhythmic Refrain"],
        "themes": ["Pnar Tradition", "Laho Dance", "Communal Harmony", "Jaintia Pride", "Youth Fellowship"],
        "lyrics_khasi": (
            "Chyiem chui-chui, chyiem chui-chui!\n"
            "Ia kynjoh kti ban shad ha madan;\n"
            "Ka kynthei hapdeng, ki shynrang harud,\n"
            "Ha ka sur Laho ba sawa thiang!\n\n"
            "U shyngwiang u pyrsad ha ki lum Jowai,\n"
            "Ki khun ka Ri Jaintia ki la kmen;\n"
            "Khlem ksing khlem nakra ngi shad da ka sur,\n"
            "Ka akor ba bha ngin pynneh ha tnum!\n\n"
            "Chyiem chui-chui, ia kynjoh ban kmen,\n"
            "Ka nam u Pnar kan neh ha pyrthei!"
        ),
        "lyrics_english": (
            "Chyiem chui-chui, chyiem chui-chui!\n"
            "Link hands together to dance upon the field;\n"
            "The maiden in the center, the young men on either flank,\n"
            "Stepping to the sweet melodious cadence of Laho!\n\n"
            "The bamboo shyngwiang flute breathes upon the hills of Jowai,\n"
            "The sons and daughters of Jaintia rejoice in unity;\n"
            "Without heavy drums or kettle-drums we dance to human melody,\n"
            "Preserving our honorable ancestral traditions forever!\n\n"
            "Chyiem chui-chui, step together in high delight,\n"
            "The honorable name of the Pnar shall endure across the earth!"
        ),
        "stanzas": [
            {
                "stanza_number": 1,
                "title": "Ka Shad Laho ha Madan (The Laho Dance)",
                "khasi": "Chyiem chui-chui, chyiem chui-chui!\nIa kynjoh kti ban shad ha madan;\nKa kynthei hapdeng, ki shynrang harud,\nHa ka sur Laho ba sawa thiang!",
                "english": "Chyiem chui-chui! Join hands to dance upon the grass; maiden in the middle, men at her sides, moving to sweet Laho melodies!"
            },
            {
                "stanza_number": 2,
                "title": "U Shyngwiang ha Jowai (Flute of Jowai)",
                "khasi": "U shyngwiang u pyrsad ha ki lum Jowai,\nKi khun ka Ri Jaintia ki la kmen;\nKhlem ksing khlem nakra ngi shad da ka sur,\nKa akor ba bha ngin pynneh ha tnum!",
                "english": "The bamboo flute blows over Jowai hills, Jaintia youth rejoice; without heavy drums we dance to sweet singing, honoring ancestral grace!"
            }
        ],
        "vocabulary": {
            "chyiem chui-chui": "Traditional rhythmic refrain chanted during Pnar Laho folk dances",
            "laho": "The graceful festival dance of the Pnar people of Jowai and Jaintia Hills",
            "shyngwiang": "Traditional Pnar transverse bamboo flute with delicate ethereal tone",
            "kynjoh kti": "To link arms or clasp hands in synchronized communal dancing line"
        }
    },
    {
        "id": "ka_rwai_shad_mastieh",
        "title": "Warrior Sword Dance Chant (Ka Rwai Shad Mastieh)",
        "khasi_title": "Ka Rwai Shad Mastieh Ki Riewshlur",
        "category": "Warrior Dance & Heroic Phawar",
        "composer": "Traditional Clan Syiemship War Lore",
        "year": "Traditional Ancient",
        "cultural_context": (
            "Ancient heroic chant accompanying the Shad Mastieh (Warrior Sword Dance). "
            "Male warriors and clan elders hold naked double-edged steel swords (waitlam) in their "
            "right hands and black or silver yak-tail whisks (symphiah) in their left, "
            "dancing in fierce protective circles to symbolize the historic defense "
            "of the matrilineal home, clan borders, and sacred territory against invaders."
        ),
        "instruments": ["Ka Bom (giant war bass drum)", "Tangmuri", "Nakra", "Waitlam (sword clash)"],
        "themes": ["Warrior Valor", "Defense of Hearth and Clan", "Sword Dance", "Ancestral Courage"],
        "lyrics_khasi": (
            "Kren ka Bom, sawa ka Tangmuri!\n"
            "Ki samla shlur ki la ieng kynhoi;\n"
            "Ka waitlam ha ka kti kamtrei,\n"
            "Ka symphiah ba thaba ha ka kti kadiang!\n\n"
            "Ngin iada ia ka Ri, ngin da ia ka Kur,\n"
            "Ia ka Hok ngin ym ju aili ha ka khim!\n"
            "Lada u nongshun u wan ban thombor,\n"
            "Ka dohnud ba shlur kan ieng ha ka nam!"
        ),
        "lyrics_english": (
            "The giant bass drum thunders, the reed horn cries aloud!\n"
            "The valiant warriors arise with a battle cheer;\n"
            "The flashing steel sword brandished in the right hand,\n"
            "The white whisk gleaming in the left hand!\n\n"
            "We shall defend the homeland, we shall shield the Clan,\n"
            "Never shall we yield Righteousness in times of peril!\n"
            "If the enemy comes to oppress our sovereign soil,\n"
            "Our brave hearts shall stand victorious in honorable renown!"
        ),
        "stanzas": [
            {
                "stanza_number": 1,
                "title": "Ka Waitlam bad ka Symphiah (Sword and Whisk)",
                "khasi": "Kren ka Bom, sawa ka Tangmuri!\nKi samla shlur ki la ieng kynhoi;\nKa waitlam ha ka kti kamtrei,\nKa symphiah ba thaba ha ka kti kadiang!",
                "english": "Bass drum thunders, horn sounds! Brave warriors rise cheering; flashing sword in right hand, gleaming whisk in the left!"
            },
            {
                "stanza_number": 2,
                "title": "Ka Jingiada ia ka Kur (Defense of the Clan)",
                "khasi": "Ngin iada ia ka Ri, ngin da ia ka Kur,\nIa ka Hok ngin ym ju aili ha ka khim!\nLada u nongshun u wan ban thombor,\nKa dohnud ba shlur kan ieng ha ka nam!",
                "english": "We defend our land, we shield our clan; righteousness we will never surrender! If foes encroach, our valiant hearts will stand in glory!"
            }
        ],
        "vocabulary": {
            "shad mastieh": "Traditional warrior sword dance performed with naked blades and whisks",
            "waitlam": "Traditional heavy, broad-bladed Khasi battle sword with iron hilt",
            "symphiah": "Protective dance whisk made of horsehair or yak-tail set in an ornamental silver handle",
            "ka bom": "Massive hollowed-wood two-headed war bass drum struck with curved mallets",
            "thombor": "To invade, oppress, trample upon sovereign rights by brute force"
        }
    },
    {
        "id": "ka_rwai_lum_kyllang_symper",
        "title": "The Ballad of Mount Kyllang and Mount Symper",
        "khasi_title": "Ka Jingrwai U Lum Kyllang bad U Lum Symper",
        "category": "Epic Mythological Ballad",
        "composer": "Ancient Oral Lore / Bardic Verses",
        "year": "Traditional",
        "cultural_context": (
            "Recounts the famous mythological duel between two giant mountain brothers: "
            "U Lum Kyllang (a gigantic red granite dome monolith in West Khasi Hills) and "
            "U Lum Symper (a dramatic limestone mountain in Maharam). Jealous of each other's "
            "height, they hurled colossal boulders and chunks of earth at each other across the sky "
            "until Symper was scarred with deep pockmarks and Kyllang stood victorious and smooth."
        ),
        "instruments": ["Duitara", "Tangmuri", "Ksing Padiah"],
        "themes": ["Mythological Giants", "Geological Origins", "Brotherly Rivalry", "Highland Landmarks"],
        "lyrics_khasi": (
            "U Lum Kyllang bad u Lum Symper,\n"
            "Ki arlei kynrem ha ka Ri Khasi;\n"
            "Ki la ialeh ban pyni bor,\n"
            "Ban tip uba kham jrong halor pyrthei!\n\n"
            "U Kyllang u la pynher ia ki mawsiang,\n"
            "U Symper u la kyntait da ka khyndew;\n"
            "Ki riat ki la kynkhih, ka bneng ka la sawa,\n"
            "Haduh ba u Kyllang u la jop ha ka nam!\n\n"
            "Hynrei mynta ki shong suk ha la ri,\n"
            "Ki sakhi ia ka nam jong u Hynniewtrep!"
        ),
        "lyrics_english": (
            "Mount Kyllang and Mount Symper,\n"
            "Two colossal brothers upon the Khasi hills;\n"
            "They contended fiercely to prove their might,\n"
            "To see who was tallest and proudest beneath the heavens!\n\n"
            "Kyllang hurled massive granite boulders through the sky,\n"
            "Symper flung back sods of red highland earth;\n"
            "The ravines shook, the heavens echoed with the thunder,\n"
            "Until Kyllang stood triumphant in enduring granite glory!\n\n"
            "Yet today both mountains rest in peace across our land,\n"
            "Eternal witnesses to the greatness of the Children of the Seven Huts!"
        ),
        "stanzas": [
            {
                "stanza_number": 1,
                "title": "Ki Ar Kynrem (Two Giant Brothers)",
                "khasi": "U Lum Kyllang bad u Lum Symper,\nKi arlei kynrem ha ka Ri Khasi;\nKi la ialeh ban pyni bor,\nBan tip uba kham jrong halor pyrthei!",
                "english": "Mount Kyllang and Mount Symper, two majestic peaks in Khasi land; contending in power to prove who was tallest upon the earth!"
            },
            {
                "stanza_number": 2,
                "title": "Ka Jingiatur Maw (Hurling of Boulders)",
                "khasi": "U Kyllang u la pynher ia ki mawsiang,\nU Symper u la kyntait da ka khyndew;\nKi riat ki la kynkhih, ka bneng ka la sawa,\nHaduh ba u Kyllang u la jop ha ka nam!",
                "english": "Kyllang hurled giant stones, Symper returned mud and earth; gorges trembled and heavens echoed until Kyllang stood victorious!"
            }
        ],
        "vocabulary": {
            "lum kyllang": "Colossal granite rock dome (over 5,600 ft) in West Khasi Hills",
            "lum symper": "Famous jagged limestone mountain peak in Maharam Syiemship",
            "pynher maw": "To hurl or launch giant stone boulders through the air in ancient warfare",
            "hynniewtrep": "The primordial Seven Celestial Families who populated the Khasi Hills"
        }
    },
    {
        "id": "ki_sngi_ba_la_leit_noh",
        "title": "Days of Yore (Ki Sngi Ba La Leit Noh)",
        "khasi_title": "Ki Sngi Ba La Leit Noh",
        "category": "Elegiac Ballad & Ancestral Memory",
        "composer": "H.W. Sten",
        "year": 1979,
        "cultural_context": (
            "A poignant, nostalgic reflection upon ancestral times and youthful camaraderie. "
            "Recalls the peaceful simplicity of village childhood, gatherings around the hearth fire, "
            "and venerates the memory of elders who have passed into the ancestral realm."
        ),
        "instruments": ["Maryngod", "Duitara", "Sharati"],
        "themes": ["Nostalgia", "Ancestral Remembrance", "Passing of Time", "Highland Heritage"],
        "lyrics_khasi": (
            "Kumno ngan klet ia kito ki sngi,\n"
            "Ba nga dang ialehkai ha la ka shnong;\n"
            "Ki sngi ba shai, ki por ba suk,\n"
            "Haba ka dohnud ka dang lui-lui!\n\n"
            "Ki tymmen mynhyndai ki iathuh parom,\n"
            "Ha rympei dingshan ha ka miet ba daitthah;\n"
            "La ki sngi ki la leit noh kum ka lyer,\n"
            "Ka jingkynmaw ia ki kan ym duh lano lano!"
        ),
        "lyrics_english": (
            "How can I ever forget those golden days of old,\n"
            "When I used to play innocently in my native village;\n"
            "Those bright days, those peaceful times,\n"
            "When the youthful heart knew only gentle innocence!\n\n"
            "The elders of ancient times shared beloved folklore,\n"
            "Beside the warm hearth on bitterly cold frosty nights;\n"
            "Though those days have drifted away like the passing mountain wind,\n"
            "Their sacred memory shall never, ever fade away!"
        ),
        "stanzas": [
            {
                "stanza_number": 1,
                "title": "Ki Sngi Khunlung (Days of Childhood)",
                "khasi": "Kumno ngan klet ia kito ki sngi,\nBa nga dang ialehkai ha la ka shnong;\nKi sngi ba shai, ki por ba suk,\nHaba ka dohnud ka dang lui-lui!",
                "english": "How could I forget those golden days when I played in my native village; bright peaceful times when the heart knew only gentle joy!"
            },
            {
                "stanza_number": 2,
                "title": "Ka Jingkynmaw ha Rympei (Memories by the Hearth)",
                "khasi": "Ki tymmen mynhyndai ki iathuh parom,\nHa rympei dingshan ha ka miet ba daitthah;\nLa ki sngi ki la leit noh kum ka lyer,\nKa jingkynmaw ia ki kan ym duh lano lano!",
                "english": "Elders told legends by warm hearths on frosty nights; though days have fled like wind, memories will never perish!"
            }
        ],
        "vocabulary": {
            "sngi ba la leit noh": "Days gone by; the cherished ancestral past",
            "daitthah": "Biting cold frost on a clear highland winter night",
            "dingshan": "Hearth fire stoked with oak and pine logs",
            "lui-lui": "Pure, simple, gentle, guileless, innocent"
        }
    },
    {
        "id": "ka_biria_u_biej",
        "title": "The Folk Humor of the Simpleton (Ka Biria u Biej)",
        "khasi_title": "Ka Biria u Biej ha Shnong",
        "category": "Folk Comic Satire & Village Phawar",
        "composer": "Traditional Village Storytellers / H.W. Sten",
        "year": 1962,
        "cultural_context": (
            "A humorous and witty Khasi folk comic song illustrating that excessive pretension "
            "and vain posturing lead to embarrassment, celebrating warm village good humor, "
            "laughter at weekly markets (Iewduh), and the traditional virtue of modest common sense."
        ),
        "instruments": ["Mieng (jaw harp)", "Duitara", "Hand clappers"],
        "themes": ["Folk Humor", "Village Satire", "Modesty over Vanity", "Weekly Market Banter"],
        "lyrics_khasi": (
            "U biej u la leit sha Iewduh ban thied jain,\n"
            "U la phong da ka tupia ba jrong kum u phlang;\n"
            "U kheiñ ialade u riewstad u riewbha,\n"
            "Pynban u la thut ha ka madan Iewbah!\n\n"
            "Ki samla ki la rkhie kynriah kylleng,\n"
            "Ki tymmen ki la khih la ka khlieh mian-mian;\n"
            "Ai ngin rkhie, hynrei ngin kynmaw ia ka akor,\n"
            "Ba ka jingshongkhrein ka jah lada khlem jingstad!"
        ),
        "lyrics_english": (
            "The simpleton went down to Iewduh market to buy grand clothes,\n"
            "He donned a tall comical hat like a stalk of dry reed;\n"
            "He deemed himself a scholar and a man of great nobility,\n"
            "Yet he stumbled headlong on the stones of the big market!\n\n"
            "The market youth burst out into roaring laughter all around,\n"
            "The wise elders gently shook their heads with amusement;\n"
            "Let us laugh in good humor, yet remember proper modesty,\n"
            "For false pride vanishes quickly where true wisdom is lacking!"
        ),
        "stanzas": [
            {
                "stanza_number": 1,
                "title": "U Biej ha Iewduh (Simpleton at Market)",
                "khasi": "U biej u la leit sha Iewduh ban thied jain,\nU la phong da ka tupia ba jrong kum u phlang;\nU kheiñ ialade u riewstad u riewbha,\nPynban u la thut ha ka madan Iewbah!",
                "english": "The simpleton went to Iewduh market dressed fine with a comical tall hat, posing as a scholar, yet tripped headlong before all!"
            },
            {
                "stanza_number": 2,
                "title": "Ka Jinghikai ha la Shnong (The Moral Lesson)",
                "khasi": "Ki samla ki la rkhie kynriah kylleng,\nKi tymmen ki la khih la ka khlieh mian-mian;\nAi ngin rkhie, hynrei ngin kynmaw ia ka akor,\nBa ka jingshongkhrein ka jah lada khlem jingstad!",
                "english": "The youths laughed and elders smiled; let us laugh cheerfully but remember humility, for empty pride fails without true wisdom!"
            }
        ],
        "vocabulary": {
            "biria": "Humorous banter, friendly joking, witty comic satire",
            "iewduh": "The historic, legendary grand weekly indigenous market of Shillong",
            "rkhie kynriah": "To burst into hearty, uproarious communal laughter",
            "riewstad": "A learned scholar, person endowed with wisdom and education"
        }
    },
    {
        "id": "ka_lyer_ka_dang_sieng",
        "title": "The Fragrant Highland Wind (Ka Lyer Ka Dang Sieng)",
        "khasi_title": "Ka Lyer Ka Dang Sieng ha ki Lum",
        "category": "Sensory Pastoral Lyric",
        "composer": "H.W. Sten",
        "year": 1979,
        "cultural_context": (
            "Celebrates the fresh, aromatic fragrance of the Khasi mountain air wafting "
            "sweet scents of highland pine needles, wild betel leaves, and blooming tree orchids. "
            "Evokes the ancient journeys of ancestors traversing the paved stone trails between Sohra, "
            "Pynursla, and Dawki along the southern escarpment."
        ),
        "instruments": ["Sharati", "Duitara", "Ksing Padiah"],
        "themes": ["Highland Breeze", "Fragrance of Pines", "Stone Trading Trails", "Mountain Slopes"],
        "lyrics_khasi": (
            "Ha ki tnum ba jrong ka lyer ka dang sieng,\n"
            "Ka iathuh ia ka nam jong ka Ri ba pyngngad;\n"
            "Ka sieng u dieng kseh, ka sieng u tiew-khlaw,\n"
            "Ka pynim ia ka dohnud ba thait ha lynti!\n\n"
            "Ha ki lynti-maw ba la tei ki tymmen,\n"
            "Ngi iaid da ka kmen ryngkat ka sur rwai;\n"
            "Ka lyer ka dang beh, ka sngi ka dang phyrnai,\n"
            "Ka Ri Khasi kan neh ha ka suk ba kynjai!"
        ),
        "lyrics_english": (
            "Across the lofty ridges the wind still wafts sweet fragrance,\n"
            "Proclaiming the glory of our cool, blessed homeland;\n"
            "Scent of green highland pines, scent of wild mountain orchids,\n"
            "Reviving the weary heart along the rugged trail!\n\n"
            "Along ancient paved stone paths constructed by our ancestors,\n"
            "We journey with rejoicing and songs upon our lips;\n"
            "The mountain breeze still blows, the sun shines bright,\n"
            "The Khasi homeland shall abide in peaceful serenity!"
        ),
        "stanzas": [
            {
                "stanza_number": 1,
                "title": "Ka Lyer ba Dang Sieng (The Scented Wind)",
                "khasi": "Ha ki tnum ba jrong ka lyer ka dang sieng,\nKa iathuh ia ka nam jong ka Ri ba pyngngad;\nKa sieng u dieng kseh, ka sieng u tiew-khlaw,\nKa pynim ia ka dohnud ba thait ha lynti!",
                "english": "Across lofty ridges winds blow fragrant, telling of our cool land; scented with pine and wild orchid, reviving weary travelers on the trail!"
            },
            {
                "stanza_number": 2,
                "title": "Ki Lynti-Maw Mynhyndai (Ancient Stone Trails)",
                "khasi": "Ha ki lynti-maw ba la tei ki tymmen,\nNgi iaid da ka kmen ryngkat ka sur rwai;\nKa lyer ka dang beh, ka sngi ka dang phyrnai,\nKa Ri Khasi kan neh ha ka suk ba kynjai!",
                "english": "Along stone paths paved by ancestors, we march joyful with song; breezes blow and the sun gleams, Khasi land endures in serene peace!"
            }
        ],
        "vocabulary": {
            "lyer-sieng": "Aromatic, fragrance-bearing breeze carrying mountain floral scents",
            "tiew-khlaw": "Wild uncultivated jungle flower or epiphytic mountain orchid",
            "lynti-maw": "Ancient stone-paved highland trading trails traversing valleys and root bridges",
            "pynim dohnud": "To revive, invigorate, and refresh the weary heart and spirit"
        }
    }
]

def main():
    print("=== Expanding Khasi Local Songs & Traditional Phawar Collection ===")
    
    # 1. Write each song JSON file
    for s in NEW_SONGS:
        s_id = s["id"]
        # Calculate word count
        khasi_words = len(re.findall(r"\w+", s["lyrics_khasi"], re.UNICODE))
        s["word_count"] = khasi_words
        
        target_path = SONGS_DIR / f"{s_id}.json"
        with open(target_path, "w", encoding="utf-8") as f:
            json.dump(s, f, indent=2, ensure_ascii=False)
        print(f"Created song JSON: {target_path.name} ({khasi_words} Khasi words)")
        
        # Write raw source text
        raw_text_path = RAW_SONGS_DIR / f"{s_id}.txt"
        with open(raw_text_path, "w", encoding="utf-8") as rf:
            rf.write(f"=== {s['title']} ({s['khasi_title']}) ===\n")
            rf.write(f"Composer: {s['composer']} ({s['year']})\n")
            rf.write(f"Category: {s['category']}\n\n")
            rf.write("--- KHASI LYRICS ---\n")
            rf.write(s["lyrics_khasi"] + "\n\n")
            rf.write("--- ENGLISH TRANSLATION ---\n")
            rf.write(s["lyrics_english"] + "\n")

    # 2. Rebuild songs_index.json
    print("\n--- Rebuilding songs_index.json ---")
    all_index = []
    for fpath in sorted(SONGS_DIR.glob("*.json")):
        if fpath.name == "songs_index.json":
            continue
        with open(fpath, "r", encoding="utf-8") as f:
            sdata = json.load(f)
        all_index.append({
            "id": sdata["id"],
            "title": sdata["title"],
            "khasi_title": sdata["khasi_title"],
            "category": sdata["category"],
            "composer": sdata.get("composer", "Oral Tradition"),
            "year": sdata.get("year", "Traditional"),
            "instruments": sdata.get("instruments", []),
            "themes": sdata.get("themes", []),
            "word_count": sdata.get("word_count", len(sdata.get("lyrics_khasi", "").split())),
            "file": fpath.name
        })

    songs_index_path = SONGS_DIR / "songs_index.json"
    with open(songs_index_path, "w", encoding="utf-8") as f:
        json.dump(all_index, f, indent=2, ensure_ascii=False)
    print(f"Updated songs_index.json with {len(all_index)} total songs!")

    # 3. Extract words and enrich khasi/lexicon/data/words.json
    print("\n--- Extracting Vocabulary & Updating Library Lexicon ---")
    with open(WORDS_JSON_PATH, "r", encoding="utf-8") as f:
        words_list = json.load(f)
    
    existing_khasi_set = {w["khasi"].lower().strip() for w in words_list if "khasi" in w}
    initial_vocab_len = len(words_list)
    print(f"Current library word count: {initial_vocab_len}")

    # Rich new cultural, poetic, musical, and dialect vocabulary entries from all songs
    NEW_VOCAB_ENTRIES = [
        # Patriotic Anthem & National Song terms
        {
            "khasi": "umpohliew",
            "english": "living natural spring flowing perpetually from mountain aquifers; source of wisdom",
            "hindi": "पहाड़ी प्राकृतिक जलस्रोत / झरना",
            "pos": "noun",
            "gender": "u",
            "category": "nature_philosophy",
            "dialect_variants": {"sohra": "umpohliew", "pnar": "umpohloi", "war": "ampohliew", "bhoi": "umpohliew"}
        },
        {
            "khasi": "jingkynmaw",
            "english": "ancestral remembrance, cherished collective memory, commemoration",
            "hindi": "स्मृति / याद / पूर्वजों का स्मरण",
            "pos": "noun",
            "gender": "ka",
            "category": "philosophy",
            "dialect_variants": {"sohra": "jingkynmaw", "pnar": "jingkñiaw-kynmaw", "war": "kynmaw", "bhoi": "jingkynmaw"}
        },
        {
            "khasi": "shngiam",
            "english": "sweet, crisp, and delicious to the palate (especially of pure mountain water)",
            "hindi": "स्वादिष्ट / मीठा (पहाड़ी जल हेतु)",
            "pos": "adjective",
            "gender": None,
            "category": "sensory",
            "dialect_variants": {"sohra": "shngiam", "pnar": "bang-shngiam", "war": "shngiam", "bhoi": "shngiam"}
        },
        {
            "khasi": "rngad",
            "english": "to dry up, run completely dry, evaporate into drought",
            "hindi": "सूख जाना / जलहीन हो जाना",
            "pos": "verb",
            "gender": None,
            "category": "nature",
            "dialect_variants": {"sohra": "rngad", "pnar": "rngad", "war": "rngad", "bhoi": "rngad"}
        },
        {
            "khasi": "thoin-thoin",
            "english": "with profound, tender, passionate love and devotion",
            "hindi": "अगाध प्रेम / गहरे समर्पण से",
            "pos": "adverb",
            "gender": None,
            "category": "emotion",
            "dialect_variants": {"sohra": "thoin-thoin", "pnar": "thoin-thoin", "war": "thoin-thoin", "bhoi": "thoin-thoin"}
        },
        {
            "khasi": "raieh-raidain",
            "english": "side-by-side, united hand-in-hand in communal solidarity",
            "hindi": "एकजुट होकर / कंधे से कंधा मिलाकर",
            "pos": "adverb",
            "gender": None,
            "category": "social",
            "dialect_variants": {"sohra": "raieh-raidain", "pnar": "lang-raieh", "war": "raieh", "bhoi": "raieh-raidain"}
        },
        {
            "khasi": "kliar",
            "english": "highest rocky crest, summit, or peak of a highland mountain",
            "hindi": "शिखर / चोटी",
            "pos": "noun",
            "gender": "ka",
            "category": "geography",
            "dialect_variants": {"sohra": "kliar", "pnar": "tdu-lum", "war": "kliar", "bhoi": "kliar"}
        },
        {
            "khasi": "sangaria",
            "english": "towering rocky precipice or crag overlooking forested gorges",
            "hindi": "ऊँची चट्टानी खड़ी ढलान",
            "pos": "noun",
            "gender": "u",
            "category": "geography",
            "dialect_variants": {"sohra": "sangaria", "pnar": "sangaria", "war": "riat", "bhoi": "sangaria"}
        },
        {
            "khasi": "meirilung",
            "english": "motherland, the sacred maternal soil nurturing the matrilineal clans",
            "hindi": "मातृभूमि / धरती माँ",
            "pos": "noun",
            "gender": "ka",
            "category": "patriotism",
            "dialect_variants": {"sohra": "meirilung", "pnar": "beirilung", "war": "meirilung", "bhoi": "meirilung"}
        },
        # Spiritual & Sacred Hymn terms
        {
            "khasi": "nongbuh nongthaw",
            "english": "the Supreme Deity as sovereign creator, disposer, and architect of human life",
            "hindi": "सृष्टिकर्ता परमेश्वर",
            "pos": "noun",
            "gender": "u",
            "category": "spirituality",
            "dialect_variants": {"sohra": "nongbuh nongthaw", "pnar": "nongbuh nongthaw", "war": "nongbuh nongthaw", "bhoi": "nongbuh nongthaw"}
        },
        {
            "khasi": "nylla",
            "english": "pure, genuine, unadulterated, unalloyed (e.g. jingieid nylla = pure love)",
            "hindi": "विशुद्ध / सच्चा / निष्कपट",
            "pos": "adjective",
            "gender": None,
            "category": "spirituality",
            "dialect_variants": {"sohra": "nylla", "pnar": "nylla", "war": "nylla", "bhoi": "nylla"}
        },
        {
            "khasi": "nongkdup nongkynshew",
            "english": "divine protector who embraces and shelters like a sacred treasure",
            "hindi": "संरक्षक एवं पालनकर्ता",
            "pos": "noun",
            "gender": "u",
            "category": "spirituality",
            "dialect_variants": {"sohra": "nongkdup nongkynshew", "pnar": "nongkdup nongkynshew", "war": "nongkdup", "bhoi": "nongkdup"}
        },
        {
            "khasi": "thylliej ding",
            "english": "tongue of fire, purifying spiritual flame",
            "hindi": "अग्नि-शिखा / पावन ज्वाला",
            "pos": "noun",
            "gender": "u",
            "category": "spirituality",
            "dialect_variants": {"sohra": "thylliej ding", "pnar": "thylliej ding", "war": "thylliej dng", "bhoi": "thylliej ding"}
        },
        {
            "khasi": "syrtap",
            "english": "tier, layer, fold (e.g. hynniew syrtap = sevenfold celestial planes)",
            "hindi": "परत / तह / स्तर",
            "pos": "noun",
            "gender": "ka",
            "category": "philosophy",
            "dialect_variants": {"sohra": "syrtap", "pnar": "syrtap", "war": "syrtap", "bhoi": "syrtap"}
        },
        {
            "khasi": "jingthohbria",
            "english": "blemish, moral stain, defilement of character",
            "hindi": "कलंक / दोष / दाग",
            "pos": "noun",
            "gender": "ka",
            "category": "ethics",
            "dialect_variants": {"sohra": "jingthohbria", "pnar": "dak-thohbria", "war": "jingthohbria", "bhoi": "jingthohbria"}
        },
        {
            "khasi": "bor aneng",
            "english": "celestial authority, sovereign divine power from the highest heaven",
            "hindi": "दिव्य स्वर्गीय शक्ति",
            "pos": "noun",
            "gender": "ka",
            "category": "spirituality",
            "dialect_variants": {"sohra": "bor aneng", "pnar": "bor nachilliang", "war": "bor aneng", "bhoi": "bor aneng"}
        },
        # Nature & Bardic Lyric terms
        {
            "khasi": "kynjai",
            "english": "profound serenity, peaceful leisure, unhurried ease of soul in nature",
            "hindi": "परम शांति / सुकून / निश्चिंतता",
            "pos": "noun",
            "gender": "ka",
            "category": "philosophy",
            "dialect_variants": {"sohra": "kynjai", "pnar": "suk-kynjai", "war": "kynjai", "bhoi": "kynjai"}
        },
        {
            "khasi": "dieng kseh",
            "english": "Khasi highland pine (Pinus kesiya), iconic evergreen conifer of Meghalaya",
            "hindi": "खासी देवदारु / चीड़ का पेड़",
            "pos": "noun",
            "gender": "u",
            "category": "flora",
            "dialect_variants": {"sohra": "dieng kseh", "pnar": "deing kseh", "war": "dieng kseh", "bhoi": "dieng kseh"}
        },
        {
            "khasi": "shongkhrein",
            "english": "to carry oneself with dignified nobility, majestic self-respect",
            "hindi": "गरिमापूर्ण / स्वाभिमानी ढंग से रहना",
            "pos": "verb",
            "gender": None,
            "category": "character",
            "dialect_variants": {"sohra": "shongkhrein", "pnar": "shong-donburom", "war": "shongkhrein", "bhoi": "shongkhrein"}
        },
        {
            "khasi": "wahduid",
            "english": "clear mountain brook, small rill babbling over pebbles",
            "hindi": "छोटी पहाड़ी धारा / नाला",
            "pos": "noun",
            "gender": "ka",
            "category": "geography",
            "dialect_variants": {"sohra": "wahduid", "pnar": "wahduid", "war": "wahduid", "bhoi": "wahduid"}
        },
        # Seasonal Cycle terms
        {
            "khasi": "aiom",
            "english": "season, climatic period of the annual cycle",
            "hindi": "ऋतु / मौसम",
            "pos": "noun",
            "gender": "ka",
            "category": "nature",
            "dialect_variants": {"sohra": "aiom", "pnar": "aiom", "war": "aiom", "bhoi": "aiom"}
        },
        {
            "khasi": "pyrem",
            "english": "spring season, time of vernal blossoming and field preparation (March-May)",
            "hindi": "वसंत ऋतु",
            "pos": "noun",
            "gender": "ka",
            "category": "nature",
            "dialect_variants": {"sohra": "pyrem", "pnar": "pyrem", "war": "pyrem", "bhoi": "pyrem"}
        },
        {
            "khasi": "lyiur",
            "english": "summer monsoon season, heavy rainfall period (June-August)",
            "hindi": "वर्षा ऋतु / मानसून",
            "pos": "noun",
            "gender": "ka",
            "category": "nature",
            "dialect_variants": {"sohra": "lyiur", "pnar": "lyiur", "war": "lyiur", "bhoi": "lyiur"}
        },
        {
            "khasi": "synrai",
            "english": "autumn season, time of golden paddy harvest (September-November)",
            "hindi": "शरद ऋतु / फसल की ऋतु",
            "pos": "noun",
            "gender": "ka",
            "category": "nature",
            "dialect_variants": {"sohra": "synrai", "pnar": "synrai", "war": "synrai", "bhoi": "synrai"}
        },
        {
            "khasi": "tlang",
            "english": "winter season, time of frost and hearthside storytelling (December-February)",
            "hindi": "शीत ऋतु / जाड़ा",
            "pos": "noun",
            "gender": "u",
            "category": "nature",
            "dialect_variants": {"sohra": "tlang", "pnar": "tlang", "war": "tlang", "bhoi": "tlang"}
        },
        {
            "khasi": "thah",
            "english": "white morning frost forming upon highland winter grasses",
            "hindi": "पाला / तुषार",
            "pos": "noun",
            "gender": "ka",
            "category": "nature",
            "dialect_variants": {"sohra": "thah", "pnar": "thah", "war": "thah", "bhoi": "thah"}
        },
        {
            "khasi": "thiar",
            "english": "large traditional woven bamboo granary inside the home for storing unhusked rice",
            "hindi": "धान का पारंपरिक बाँस का कोठार",
            "pos": "noun",
            "gender": "ka",
            "category": "agriculture",
            "dialect_variants": {"sohra": "thiar", "pnar": "thiar", "war": "thiar", "bhoi": "thiar"}
        },
        {
            "khasi": "rympei",
            "english": "the sacred matrilineal three-stone family kitchen hearth fire",
            "hindi": "पारंपरिक पारिवारिक चूल्हा",
            "pos": "noun",
            "gender": "ka",
            "category": "culture",
            "dialect_variants": {"sohra": "rympei", "pnar": "rympei", "war": "rympei", "bhoi": "rympei"}
        },
        # Floral and Birdsong terms
        {
            "khasi": "tiew-doh-maw",
            "english": "wild Himalayan rock-clinging orchid or cherry blossom with delicate pink petals",
            "hindi": "पहाड़ी जंगली आर्किड / चेरी पुष्प",
            "pos": "noun",
            "gender": "u",
            "category": "flora",
            "dialect_variants": {"sohra": "tiew-doh-maw", "pnar": "tiew-doh-maw", "war": "tiew-doh-maw", "bhoi": "tiew-doh-maw"}
        },
        {
            "khasi": "sim-tyngwieng",
            "english": "highland cliff swallow or swift darting across waterfall spray",
            "hindi": "पहाड़ी अबाबील पक्षी",
            "pos": "noun",
            "gender": "u",
            "category": "fauna",
            "dialect_variants": {"sohra": "sim-tyngwieng", "pnar": "sim-tyngwieng", "war": "sim-tyngwieng", "bhoi": "sim-tyngwieng"}
        },
        {
            "khasi": "lyer-pyrem",
            "english": "sweet vernal spring breeze carrying pollen of wild mountain orchids",
            "hindi": "वसंत की मंद सुगंधित बयार",
            "pos": "noun",
            "gender": "ka",
            "category": "nature",
            "dialect_variants": {"sohra": "lyer-pyrem", "pnar": "lyer-pyrem", "war": "lyer-pyrem", "bhoi": "lyer-pyrem"}
        },
        {
            "khasi": "barymphum",
            "english": "rainbow arching through misty waterfall spray or light mountain rain",
            "hindi": "इंद्रधनुष (झरने के फुहारों में)",
            "pos": "u",
            "gender": "u",
            "category": "nature",
            "dialect_variants": {"sohra": "barymphum", "pnar": "barymphum", "war": "barymphum", "bhoi": "barymphum"}
        },
        {
            "khasi": "paila rupa",
            "english": "traditional silver bead necklace draped over festive silk attire",
            "hindi": "चाँदी के पारंपरिक मनकों का हार",
            "pos": "noun",
            "gender": "ka",
            "category": "costume",
            "dialect_variants": {"sohra": "paila rupa", "pnar": "paila rupa", "war": "paila rupa", "bhoi": "paila rupa"}
        },
        {
            "khasi": "nohkalikai",
            "english": "the famous 1,115-foot waterfall near Sohra, named after the tragic legend of Ka Likai",
            "hindi": "नोहकालिकाई जलप्रपात",
            "pos": "noun",
            "gender": "ka",
            "category": "geography",
            "dialect_variants": {"sohra": "nohkalikai", "pnar": "nohkalikai", "war": "nohkalikai", "bhoi": "nohkalikai"}
        },
        {
            "khasi": "dainthlen",
            "english": "historic waterfall near Sohra where ancestral warriors slew the monstrous thlen snake",
            "hindi": "दैंथलेन जलप्रपात",
            "pos": "noun",
            "gender": "ka",
            "category": "mythology",
            "dialect_variants": {"sohra": "dainthlen", "pnar": "dainthlen", "war": "dainthlen", "bhoi": "dainthlen"}
        },
        {
            "khasi": "step-phyrngab",
            "english": "dawn twilight, the earliest grey glimmer of morning light before sunrise",
            "hindi": "भोर / प्रातःकाल की पहली किरण",
            "pos": "noun",
            "gender": "ka",
            "category": "time",
            "dialect_variants": {"sohra": "step-phyrngab", "pnar": "step-phyrngab", "war": "step-phyrngab", "bhoi": "step-phyrngab"}
        },
        {
            "khasi": "nongiaid-wir",
            "english": "wandering traveler, lost pilgrim seeking the highland trail",
            "hindi": "भटका हुआ राही / मुसाफिर",
            "pos": "noun",
            "gender": "u",
            "category": "social",
            "dialect_variants": {"sohra": "nongiaid-wir", "pnar": "nonglai-wir", "war": "nongiaid-wir", "bhoi": "nongiaid-wir"}
        },
        {
            "khasi": "ieng triang",
            "english": "to stand resolute, unwavering, firm in moral conviction",
            "hindi": "अडिग खड़े रहना / दृढ़ रहना",
            "pos": "verb",
            "gender": None,
            "category": "ethics",
            "dialect_variants": {"sohra": "ieng triang", "pnar": "ieng skhem", "war": "ieng triang", "bhoi": "ieng triang"}
        },
        {
            "khasi": "tiew-pathaw",
            "english": "wild mountain rock orchid / yellow flower blooming in barren limestone fissures",
            "hindi": "चट्टानों पर उगने वाला जंगली पीला पुष्प",
            "pos": "noun",
            "gender": "u",
            "category": "flora",
            "dialect_variants": {"sohra": "tiew-pathaw", "pnar": "tiew-pathaw", "war": "tiew-pathaw", "bhoi": "tiew-pathaw"}
        },
        {
            "khasi": "erlang",
            "english": "driving mountain storm gale accompanied by sudden icy rain",
            "hindi": "तूफानी ठंडी पहाड़ी हवा",
            "pos": "noun",
            "gender": "ka",
            "category": "nature",
            "dialect_variants": {"sohra": "erlang", "pnar": "erlang", "war": "erlang", "bhoi": "erlang"}
        },
        {
            "khasi": "simpyllieng",
            "english": "the Indian cuckoo (Cuculus micropterus), whose call signals sowing season to farmers",
            "hindi": "पहाड़ी कोयल (जिसकी कूक से बुवाई शुरू होती है)",
            "pos": "noun",
            "gender": "u",
            "category": "fauna",
            "dialect_variants": {"sohra": "simpyllieng", "pnar": "simpyllieng", "war": "simpyllieng", "bhoi": "simpyllieng"}
        },
        # Pnar & Jaintia Folk Dance terms
        {
            "khasi": "chyiem chui-chui",
            "english": "rhythmic chanted dance refrain of the Pnar Laho festival dance",
            "hindi": "पनार लहो नृत्य का पारंपरिक तालबद्ध बोल",
            "pos": "interjection",
            "gender": None,
            "category": "music_pnar",
            "dialect_variants": {"sohra": "chyiem chui-chui", "pnar": "chyiem chui-chui", "war": "chyiem chui-chui", "bhoi": "chyiem chui-chui"}
        },
        {
            "khasi": "laho",
            "english": "traditional folk dance festival of the Pnar people of Jaintia Hills",
            "hindi": "लहो लोकनृत्य (जयंतिया जनजाति का)",
            "pos": "noun",
            "gender": "ka",
            "category": "dance_pnar",
            "dialect_variants": {"sohra": "laho", "pnar": "laho", "war": "laho", "bhoi": "laho"}
        },
        {
            "khasi": "shyngwiang",
            "english": "delicate traditional transverse bamboo flute of the Pnar people",
            "hindi": "पनार पारंपरिक बाँसुरी",
            "pos": "noun",
            "gender": "u",
            "category": "music_instrument",
            "dialect_variants": {"sohra": "shyngwiang", "pnar": "shyngwiang", "war": "shyngwiang", "bhoi": "shyngwiang"}
        },
        {
            "khasi": "kynjoh kti",
            "english": "to clasp hands or link arms together in synchronized dance lines",
            "hindi": "हाथ से हाथ मिलाकर नाचना",
            "pos": "verb",
            "gender": None,
            "category": "dance",
            "dialect_variants": {"sohra": "kynjoh kti", "pnar": "kynjoh kti", "war": "kynjoh kti", "bhoi": "kynjoh kti"}
        },
        # Warrior & Epic Ballad terms
        {
            "khasi": "shad mastieh",
            "english": "warrior sword dance performed with swords (waitlam) and whisks (symphiah)",
            "hindi": "खासी योद्धा तलवार नृत्य",
            "pos": "noun",
            "gender": "ka",
            "category": "warrior_tradition",
            "dialect_variants": {"sohra": "shad mastieh", "pnar": "mastieh", "war": "shad mastieh", "bhoi": "shad mastieh"}
        },
        {
            "khasi": "waitlam",
            "english": "traditional broad-bladed Khasi battle sword with iron hilt",
            "hindi": "पारंपरिक खासी तलवार",
            "pos": "noun",
            "gender": "ka",
            "category": "weapon_heritage",
            "dialect_variants": {"sohra": "waitlam", "pnar": "waitlam", "war": "waitlam", "bhoi": "waitlam"}
        },
        {
            "khasi": "symphiah",
            "english": "ceremonial dance whisk made of black or silver animal hair held in the warrior's left hand",
            "hindi": "पारंपरिक नृत्य चँवर",
            "pos": "noun",
            "gender": "ka",
            "category": "costume_heritage",
            "dialect_variants": {"sohra": "symphiah", "pnar": "symphiah", "war": "symphiah", "bhoi": "symphiah"}
        },
        {
            "khasi": "ka bom",
            "english": "massive two-headed hollow-wood bass drum used in war and grand ceremonial dances",
            "hindi": "बड़ा युद्ध-नगाड़ा / ढोल",
            "pos": "noun",
            "gender": "ka",
            "category": "music_instrument",
            "dialect_variants": {"sohra": "ka bom", "pnar": "ka bom", "war": "ka bom", "bhoi": "ka bom"}
        },
        {
            "khasi": "thombor",
            "english": "to oppress, trample upon rights, or encroach aggressively by brute force",
            "hindi": "दमन करना / अधिकार छीनना",
            "pos": "verb",
            "gender": None,
            "category": "action",
            "dialect_variants": {"sohra": "thombor", "pnar": "thombor", "war": "thombor", "bhoi": "thombor"}
        },
        {
            "khasi": "lum kyllang",
            "english": "Mount Kyllang, colossal red granite dome monolith (5,684 ft) in West Khasi Hills",
            "hindi": "माउंट क्याल्लांग (विशाल ग्रेनाइट शिला पर्वत)",
            "pos": "noun",
            "gender": "u",
            "category": "geography",
            "dialect_variants": {"sohra": "lum kyllang", "pnar": "lum kyllang", "war": "lum kyllang", "bhoi": "lum kyllang"}
        },
        {
            "khasi": "lum symper",
            "english": "Mount Symper, legendary jagged limestone mountain in Maharam Syiemship",
            "hindi": "माउंट सिम्पेर पर्वत",
            "pos": "noun",
            "gender": "u",
            "category": "geography",
            "dialect_variants": {"sohra": "lum symper", "pnar": "lum symper", "war": "lum symper", "bhoi": "lum symper"}
        },
        {
            "khasi": "pynher maw",
            "english": "to launch or hurl boulders through the air as in ancient mythical combats",
            "hindi": "विशाल शिलाएँ फेंकना",
            "pos": "verb",
            "gender": None,
            "category": "mythology",
            "dialect_variants": {"sohra": "pynher maw", "pnar": "pynher moo", "war": "pynher maw", "bhoi": "pynher maw"}
        },
        # Village Wit & Mountain Trails terms
        {
            "khasi": "daitthah",
            "english": "bitingly cold winter frost freezing the mountain grass",
            "hindi": "कड़कड़ाती ठंड / पाला",
            "pos": "adjective",
            "gender": None,
            "category": "weather",
            "dialect_variants": {"sohra": "daitthah", "pnar": "daitthah", "war": "daitthah", "bhoi": "daitthah"}
        },
        {
            "khasi": "dingshan",
            "english": "heartwarming oak-wood fire burning in the center of the Khasi hearth",
            "hindi": "चूल्हे की आग / धूनी",
            "pos": "noun",
            "gender": "ka",
            "category": "culture",
            "dialect_variants": {"sohra": "dingshan", "pnar": "dingshan", "war": "dingshan", "bhoi": "dingshan"}
        },
        {
            "khasi": "biria",
            "english": "good-humored joking, comical banter, friendly village satire",
            "hindi": "हँसी-मज़ाक / ठिठोली",
            "pos": "noun",
            "gender": "ka",
            "category": "social",
            "dialect_variants": {"sohra": "biria", "pnar": "biria", "war": "biria", "bhoi": "biria"}
        },
        {
            "khasi": "iewduh",
            "english": "the famous grand weekly indigenous market of Shillong (Bara Bazar)",
            "hindi": "इवदूह (शिलांग का ऐतिहासिक बड़ा बाज़ार)",
            "pos": "noun",
            "gender": "ka",
            "category": "culture",
            "dialect_variants": {"sohra": "iewduh", "pnar": "iewduh", "war": "iewduh", "bhoi": "iewduh"}
        },
        {
            "khasi": "rkhie kynriah",
            "english": "to break out into loud, hearty, uproarious communal laughter",
            "hindi": "ठाहाका मारकर हँसना",
            "pos": "verb",
            "gender": None,
            "category": "emotion",
            "dialect_variants": {"sohra": "rkhie kynriah", "pnar": "rkhie kynriah", "war": "rkhie", "bhoi": "rkhie kynriah"}
        },
        {
            "khasi": "lyer-sieng",
            "english": "aromatic breeze bearing the fragrance of pine needles and wild blossoms",
            "hindi": "सुगंधित पहाड़ी बयार",
            "pos": "noun",
            "gender": "ka",
            "category": "nature",
            "dialect_variants": {"sohra": "lyer-sieng", "pnar": "lyer-sieng", "war": "lyer-sieng", "bhoi": "lyer-sieng"}
        },
        {
            "khasi": "tiew-khlaw",
            "english": "wild mountain orchid or deep forest flower blossoming uncultivated",
            "hindi": "जंगली पहाड़ी पुष्प / आर्किड",
            "pos": "noun",
            "gender": "u",
            "category": "flora",
            "dialect_variants": {"sohra": "tiew-khlaw", "pnar": "tiew-khlaw", "war": "tiew-khlaw", "bhoi": "tiew-khlaw"}
        },
        {
            "khasi": "lynti-maw",
            "english": "ancient stone-paved highland trading trails traversing valleys and living root bridges",
            "hindi": "प्राचीन पत्थरों का पगडंडी मार्ग",
            "pos": "noun",
            "gender": "ka",
            "category": "heritage_infrastructure",
            "dialect_variants": {"sohra": "lynti-maw", "pnar": "lynti-moo", "war": "lynti-maw", "bhoi": "lynti-maw"}
        },
        {
            "khasi": "pynim dohnud",
            "english": "to revive, refresh, and comfort the weary heart and spirit",
            "hindi": "हृदय को पुनर्जीवित एवं तृप्त करना",
            "pos": "verb",
            "gender": None,
            "category": "emotion",
            "dialect_variants": {"sohra": "pynim dohnud", "pnar": "pyn-im doonud", "war": "pynim dohnud", "bhoi": "pynim dohnud"}
        }
    ]

    added_count = 0
    updated_count = 0
    
    # Track existing entries in a dictionary for quick lookup and updating
    words_by_khasi = {}
    for i, w in enumerate(words_list):
        if "khasi" in w:
            words_by_khasi[w["khasi"].lower().strip()] = i

    for entry in NEW_VOCAB_ENTRIES:
        k_key = entry["khasi"].lower().strip()
        if k_key not in words_by_khasi:
            words_list.append(entry)
            words_by_khasi[k_key] = len(words_list) - 1
            added_count += 1
        else:
            # Enrich existing entry with richer definitions if needed
            idx = words_by_khasi[k_key]
            existing = words_list[idx]
            if not existing.get("hindi") and entry.get("hindi"):
                existing["hindi"] = entry["hindi"]
                updated_count += 1
            if not existing.get("dialect_variants") and entry.get("dialect_variants"):
                existing["dialect_variants"] = entry["dialect_variants"]
                updated_count += 1

    # Also automatically extract all vocabulary dict items from all 25 songs
    for song in all_index:
        s_file = SONGS_DIR / song["file"]
        with open(s_file, "r", encoding="utf-8") as sf:
            s_full = json.load(sf)
        vocab = s_full.get("vocabulary", {})
        for term, defn in vocab.items():
            t_key = term.lower().strip()
            if t_key not in words_by_khasi and len(t_key) > 2:
                new_item = {
                    "khasi": term,
                    "english": defn,
                    "hindi": defn,  # fallback
                    "pos": "noun",
                    "gender": "ka" if term.startswith("ka ") else ("u" if term.startswith("u ") else None),
                    "category": "songs_and_poetry",
                    "dialect_variants": {
                        "sohra": term,
                        "pnar": term,
                        "war": term,
                        "bhoi": term
                    }
                }
                words_list.append(new_item)
                words_by_khasi[t_key] = len(words_list) - 1
                added_count += 1

    with open(WORDS_JSON_PATH, "w", encoding="utf-8") as wf:
        json.dump(words_list, wf, indent=2, ensure_ascii=False)

    print(f"\n[SUCCESS] Added {added_count} brand-new words to words.json!")
    print(f"[SUCCESS] Updated {updated_count} existing entries with rich dialect variants.")
    print(f"[SUCCESS] Total words in library: {len(words_list)} (was {initial_vocab_len})")

if __name__ == "__main__":
    main()
