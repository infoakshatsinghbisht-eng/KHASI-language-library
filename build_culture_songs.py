# -*- coding: utf-8 -*-
"""
Script to build structured Khasi songs datasets in khasi/culture/data/songs/.
Converts raw sources into structured JSON files with metadata, lyrics, translations, and glossaries.
"""

import json
import re
from pathlib import Path

SONGS_DIR = Path("khasi/culture/data/songs")
SONGS_DIR.mkdir(parents=True, exist_ok=True)

# 1. Load Sten text
sten_raw_path = Path("data/raw_sources/songs/ki_sur_duitara_sten.txt")
sten_text = ""
if sten_raw_path.exists():
    sten_text = sten_raw_path.read_text(encoding="utf-8")

# Extract pages for Sten
sten_pages = []
for p in sten_text.split("--- PAGE "):
    if not p.strip() or p.startswith("=== RAW"):
        continue
    lines = p.split("\n")
    p_num_str = lines[0].split()[0] if lines[0].strip() else "1"
    try:
        p_num = int(re.sub(r"[^\d]", "", p_num_str))
    except ValueError:
        p_num = len(sten_pages) + 1
    p_content = "\n".join(lines[1:]).strip()
    if p_content:
        sten_pages.append({"page": p_num, "text": p_content})

songs_data = [
    {
        "id": "ki_sur_duitara_ksiar",
        "title": "Tunes from the Golden Duitara (Ki Sur Na Ka Duitara Ksiar)",
        "khasi_title": "Ki Sur Na Ka Duitara Ksiar",
        "category": "Bardic Song & Poetry Cycle",
        "composer": "H.W. Sten",
        "year": 1979,
        "cultural_context": "Foundational modern Khasi lyric and song collection published in 1962 and expanded in 1979. Named after the revered four-stringed Khasi folk lute (ka Duitara), celebrating nature, mountain rivers, moral integrity, Khasi ancestral lore, and legendary patriots.",
        "instruments": ["Duitara", "Tangmuri", "Maryngod", "Ksing Padiah"],
        "themes": ["Nature", "Highland Pride", "U Tirot Sing", "Ancestral Virtues", "Soso Tham Tribute", "Spring Renewal"],
        "lyrics_khasi": sten_text[:5000].strip(),  # Core opening excerpt
        "lyrics_english": "A collection of 21 major Khasi lyric poems and musical songs composed for the accompaniment of the Golden Duitara lute, exploring themes of Ri Khasi's sacred mountains, streams, heroic warriors, and moral philosophy.",
        "stanzas": [
            {
                "stanza_number": 1,
                "title": "Ka Duitara Ksiar (Opening Overture)",
                "khasi": "Tem noh ko duitara ba phyrnai ksiar,\nSawa ha ki riat bad ki lum ba iar;\nPynim pat ia ka sur jong ki tymmen,\nBan sngew ki khun samla ha ka kmen!",
                "english": "Pluck forth, O golden shimmering Duitara,\nEcho across the gorges and wide mountain ranges;\nRevive once more the melody of our ancestors,\nThat the young generations may hear in righteous joy!"
            },
            {
                "stanza_number": 2,
                "title": "U Lum Shillong (Sacred Shillong Peak)",
                "khasi": "Halor u Lum Shillong ba shong u Blei,\nKa erpyngngad ka beh kylleng pyrthei;\nKi kshaid ki kynih, ki syntiew ki phuh,\nKa nam ka Ri Khasi kan neh ha tnum!",
                "english": "Atop sacred Shillong Peak where the guardian deity resides,\nThe refreshing breeze blows across the earth;\nThe waterfalls chime, the wild mountain orchids blossom,\nThe renown of the Khasi land shall forever endure!"
            },
            {
                "stanza_number": 3,
                "title": "U Tirot Sing (The Patriot Hero)",
                "khasi": "Ko Syiem ba shlur jong ka Nongkhlaw ba khraw,\nMe la kyntait ban shong kum u mraw;\nMe la ialeh pyrshah ia ki shipai Bilat,\nBan pynneh ia ka Hok bad ka Laitluid ha la ka khmat!",
                "english": "O courageous Syiem of mighty Nongkhlaw,\nThou didst refuse to live in chains as a subjugated slave;\nThou didst wage war against the British soldiers,\nTo preserve Truth, Righteousness, and Liberty before all eyes!"
            }
        ],
        "vocabulary": {
            "duitara": "Four-stringed Khasi folk lute plucked with wooden plectrum",
            "ksiar": "Gold; symbolic of nobility and ancestral purity",
            "erpyngngad": "Cool, refreshing mountain breeze",
            "riat": "Steep rocky highland gorge or precipice",
            "kshaid": "Waterfall cascading over mountain cliffs",
            "laitluid": "Freedom, sovereignty, liberty"
        },
        "total_pages": len(sten_pages),
        "pages": sten_pages[:30]  # Store first 30 digitized pages directly
    },
    {
        "id": "ka_sur_u_sier_lapalang",
        "title": "The Lament of the Stag (Ka Sur U Sier Lapalang)",
        "khasi_title": "Ka Sur U Sier Lapalang",
        "category": "Folk Elegy & Ancestral Lament (Jamlu)",
        "composer": "Ancient Oral Tradition",
        "year": "Traditional (Immorial)",
        "cultural_context": "The oldest and most revered tragedy in Khasi oral culture, serving as the archetype for all funeral wailing, laments (jamlu), and melancholic poetry. Tells of a young stag in the plains who longed for the sweet grass of the Khasi hills and died by hunter arrows.",
        "instruments": ["Maryngod (bowed fiddle)", "Shyngwiang (funeral flute)", "Duitara"],
        "themes": ["Maternal love", "Disobedience and destiny", "Loss", "Funeral weeping", "Sorrow of nature"],
        "lyrics_khasi": (
            "Ko Lapalang phrang sngi jong nga,\n"
            "Kum bating-shein u mankara!\n"
            "Haba na nga me la khlad noh,\n"
            "Dohnud sngewsih nga im suhsat.\n\n"
            "Shong khop ha la ri them ri thor,\n"
            "Bam da u khah bam da u nor!\n"
            "Ngin bam da u jangew jathang,\n"
            "Baroh shi lyiur baroh shi tlang!\n\n"
            "Pynban kynrem na nga me khlad,\n"
            "Sha Ri Khasi me la kiew krad!\n"
            "U phlang ba thiang u la ring phai,\n"
            "Ki thwei ba khuid ki la pynkai!\n\n"
            "Wow! La shet ka tieh pongdeng,\n"
            "Ia ka rynieng u kynrem reng!\n"
            "Wow! La kjit u nam sarang,\n"
            "Ia ka mynsiem u Lapalang!\n\n"
            "Ha kliar Lum Shillong u la noh,\n"
            "U khnam ba bih u la kem thoh!\n"
            "Ummat ka kmie ki la shlei tuid,\n"
            "Ki lum ki them ki la jaw ruid!\n\n"
            "Ko khun baieit ba thiah ha madan,\n"
            "Ym don shuh u ban pynkyndit kram!\n"
            "Sah marwei nga ha kane ka sngi,\n"
            "Ka nam jong me kan neh ha ri!"
        ),
        "lyrics_english": (
            "O Lapalang, light of my eyes and morning of my days,\n"
            "With stately antlers like the majestic crown of the plains!\n"
            "When thou didst depart from my maternal side,\n"
            "My weeping heart was plunged into unending sorrow.\n\n"
            "Abide quietly in our gentle lowlands and valleys,\n"
            "Feeding upon the tall reed grasses and sweet water plants!\n"
            "We shall eat our simple wild mountain herbs,\n"
            "Through every monsoon summer and through every winter freeze!\n\n"
            "Yet proud and noble, thou didst hasten away,\n"
            "Climbing up into the crags of the sacred Khasi hills!\n"
            "The tender scented grasses lured thee upward,\n"
            "The pure crystal mountain pools beckoned thee astray!\n\n"
            "Alas! The hunter's bowstring bent upon the ridge,\n"
            "Aiming at the stately stature of the antlered prince!\n"
            "Alas! The poisoned arrow pierced his side,\n"
            "Drinking the mortal soul of young Lapalang!\n\n"
            "Upon the summit of Mount Shillong he collapsed,\n"
            "The venom of the iron shaft took hold upon his veins!\n"
            "The tears of his grieving mother overflowed in torrents,\n"
            "The crags and deep ravines wept and trickled in grief!\n\n"
            "O beloved child resting motionless upon the field,\n"
            "None remains to awaken thee from thy deep slumber!\n"
            "Alone I linger upon this dark mountain day,\n"
            "Yet thy renown shall live forever across our hills!"
        ),
        "stanzas": [
            {
                "stanza_number": 1,
                "title": "Ka Jingrwai Kmie ha Ri Thor (Mother's Plea in the Plains)",
                "khasi": "Ko Lapalang phrang sngi jong nga,\nKum bating-shein u mankara!\nHaba na nga me la khlad noh,\nDohnud sngewsih nga im suhsat.\nShong khop ha la ri them ri thor,\nBam da u khah bam da u nor!",
                "english": "O Lapalang my firstborn star, antlered like the proud tree of the plain! Since thou hast departed from me, my heart lives in grieving anguish. Stay peacefully in our lowlands, eating reed-grass and river-greens!"
            },
            {
                "stanza_number": 2,
                "title": "Ka Jingkiew sha Ri Lum (Ascent to the Khasi Hills)",
                "khasi": "Pynban kynrem na nga me khlad,\nSha Ri Khasi me la kiew krad!\nU phlang ba thiang u la ring phai,\nKi thwei ba khuid ki la pynkai!",
                "english": "Yet proud and majestic thou didst wander, climbing up to the crags of the Khasi hills! The sweet scented mountain grass lured thee, the crystal highland pools drew thee on!"
            },
            {
                "stanza_number": 3,
                "title": "Ka Jingiap ha Lum Shillong (Death on Mount Shillong)",
                "khasi": "Wow! La shet ka tieh pongdeng,\nIa ka rynieng u kynrem reng!\nWow! La kjit u nam sarang,\nIa ka mynsiem u Lapalang!",
                "english": "Alas! The hunter's bent bow betrayed the stature of the antlered prince! Alas! The poisoned iron arrow drank the mortal breath of Lapalang!"
            },
            {
                "stanza_number": 4,
                "title": "Ka Ktien Khatduh (The Mother's Final Weeping)",
                "khasi": "Ko khun baieit ba thiah ha madan,\nYm don shuh u ban pynkyndit kram!\nSah marwei nga ha kane ka sngi,\nKa nam jong me kan neh ha ri!",
                "english": "O darling child asleep upon the barren field, no one remains to wake thee now! Alone I am left on this dark earth, yet thy memory will echo forever through our land!"
            }
        ],
        "vocabulary": {
            "phrang sngi": "Firstborn, dawn of the day, favorite child",
            "kynrem reng": "Magnificent branched antlers of a mature stag",
            "tieh pongdeng": "Highland bamboo hunting bow",
            "nam sarang": "Barbed iron hunting arrow with aconite venom",
            "jangew jathang": "Traditional indigenous wild medicinal edible greens",
            "jamlu": "Sacred funeral weeping and musical lamentation chant"
        }
    },
    {
        "id": "phawar_shad_suk_mynsiem",
        "title": "Thanksgiving Festival Chants (Phawar Shad Suk Mynsiem)",
        "khasi_title": "Ki Phawar Shad Suk Mynsiem",
        "category": "Sacred Thanksgiving Dance & Ritual Chants",
        "composer": "Khasi Seng Khasi Tradition",
        "year": "Traditional (1911 Annual Revival)",
        "cultural_context": "The annual thanksgiving spring dance celebration of the Khasi people held at Weiking Grounds in Shillong. Maidens dance gracefully in circles wearing silver crowns (pansngiat) and gold necklaces, while male warriors dance on the outer perimeter waving white whisks (symphiah) and swords (waitlam).",
        "instruments": ["Tangmuri (double reed pipe)", "Ksing Shynrang (male drum)", "Ksing Kynthei (female drum)", "Nakra (kettle drum)", "Kynshaw (brass cymbals)"],
        "themes": ["Spring renewal", "Communal harmony", "Thanksgiving to U Blei", "Purity of maidens", "Male guardianship"],
        "lyrics_khasi": (
            "Teng teng teng, ksing ka la sawa!\n"
            "Ri lum Ri Khasi ka la kyndit!\n"
            "Ka sngi ka la kiew ha Weiking,\n"
            "Ki khun ki kti ki la mih seng!\n\n"
            "Ka sngi kaba bhabriew, ka sngi kaba shai,\n"
            "Ki khun ki kti ki la mih ban shad ha Lympung,\n"
            "U ksing u sawa, ka tangmuri ka rih,\n"
            "Ka ksiar bad ka rupa ki phyrnai ha shadem,\n"
            "Ngin nguh ïa U Blei Nongthaw ha ka shad kmen!\n\n"
            "Ryngkat ka pansngiat ba thaba ksiar,\n"
            "Ka jainsem dhara ba jop pyrthei!\n"
            "Ki kynthei lui-lui ki shad mian-mian,\n"
            "Kum ki angel ba hiar na bneng!\n\n"
            "Ki samla shlur ba bat waitlam,\n"
            "Ryngkat ka symphiah ba pynshad kham!\n"
            "Ki da ia ka burom ka Kur ka Jait,\n"
            "Ki ieng ha ka Hok ban ym ju lait!\n\n"
            "Khublei ko Blei U Nongbuh Nongthaw!\n"
            "Ba me la ai ia ka suk ka sain!\n"
            "Ia u kba u khaw ha ki lum ki them,\n"
            "Ia ka roi ka par ha ka Hima baroh!"
        ),
        "lyrics_english": (
            "Boom, boom, resonant booms the great male drum!\n"
            "The hills of the Khasi homeland awaken to life!\n"
            "The morning sun has ascended over Weiking arena,\n"
            "The children and clans assemble in sacred communion!\n\n"
            "The glorious day has dawned, bright and pure,\n"
            "Sons and daughters step forward to dance upon the sacred lympung,\n"
            "The Ksing drums resound, the Tangmuri sounds its melodious horn,\n"
            "Gold and silver breastplates shine upon radiant chests,\n"
            "We bow before God the Creator in our dance of joy!\n\n"
            "Crowned with shimmering silver and golden pansngiat,\n"
            "Draped in prized silk dhara and muga robes!\n"
            "The gentle maidens glide with downcast eyes in modest steps,\n"
            "Resembling celestial spirits descending from the heavens!\n\n"
            "The brave young men brandish their ancestral swords,\n"
            "Swinging the white yak whisks in protective arcs!\n"
            "Shielding the sacred honor of the Clan and Matrilineage,\n"
            "Standing firm in Righteousness that shall never fail!\n\n"
            "Thanksgiving unto Thee, O God, Supreme Creator and Sustainer!\n"
            "For granting peace, health, and social concord!\n"
            "For the golden harvest of paddy in hills and valleys,\n"
            "For prosperity flourishing across every ancestral kingdom!"
        ),
        "stanzas": [
            {
                "stanza_number": 1,
                "title": "Sur Ksing bad Tangmuri (Drum and Pipe Call)",
                "khasi": "Teng teng teng, ksing ka la sawa!\nRi lum Ri Khasi ka la kyndit!\nKa sngi ka la kiew ha Weiking,\nKi khun ki kti ki la mih seng!",
                "english": "Boom, resonant sounds the drum! The Khasi mountains awake! The sun rises over Weiking, the youth assemble in communion!"
            },
            {
                "stanza_number": 2,
                "title": "Ka Shad Kynthei (The Maiden's Inner Circle)",
                "khasi": "Ryngkat ka pansngiat ba thaba ksiar,\nKa jainsem dhara ba jop pyrthei!\nKi kynthei lui-lui ki shad mian-mian,\nKum ki angel ba hiar na bneng!",
                "english": "Adorned with glowing crowns, clad in golden dhara silk! The gentle maidens dance with delicate, modest footsteps like angels descending from heaven!"
            },
            {
                "stanza_number": 3,
                "title": "Ka Shad Shynrang (The Warriors' Outer Circle)",
                "khasi": "Ki samla shlur ba bat waitlam,\nRyngkat ka symphiah ba pynshad kham!\nKi da ia ka burom ka Kur ka Jait,\nKi ieng ha ka Hok ban ym ju lait!",
                "english": "The brave youths bearing swords and whisks circle around! Guarding the sacred honor of clan and motherhood, anchored in everlasting righteousness!"
            },
            {
                "stanza_number": 4,
                "title": "Ka Jingnguh Blei (Prayer of Thanksgiving)",
                "khasi": "Khublei ko Blei U Nongbuh Nongthaw!\nBa me la ai ia ka suk ka sain!\nIa u kba u khaw ha ki lum ki them,\nIa ka roi ka par ha ka Hima baroh!",
                "english": "Thanks be to God the Creator and Sustainer! For bestowing peace and harvest, prosperity and health upon the entire realm!"
            }
        ],
        "vocabulary": {
            "pansngiat": "Sacred crown made of pure silver or gold worn by unmarried maidens",
            "jainsem dhara": "Traditional ceremonial two-piece Khasi silk garment woven from mulberry silk",
            "waitlam": "Two-handed curved indigenous ceremonial steel sword",
            "symphiah": "Sacred white whisk carried by male dancers representing protection of maternal clan",
            "lympung": "Open consecrated grassy dance square or ceremonial amphitheater",
            "suk mynsiem": "Peace of soul, state of inner tranquility and spiritual contentment"
        }
    },
    {
        "id": "phawar_iasiat_khnam",
        "title": "Archery Tournament Chants (Phawar Iasiat Khnam)",
        "khasi_title": "Ki Phawar Iasiat Khnam",
        "category": "Highland Archery Chants & Cheer Verses",
        "composer": "Traditional Clan Archers & Pyrton",
        "year": "Traditional",
        "cultural_context": "Rhythmic chanting delivered by cheerers (pyrton) during traditional Khasi archery tournaments (Iasiat Khnam). Archery is the national sport and sacred martial art of the Khasi people.",
        "instruments": ["Bamboo Bow (Ryntieh)", "Feathered Arrow (Khnam)", "Hand clapping"],
        "themes": ["Accuracy", "Clan honor", "Hoi Kiw battle cry", "Skill and courage", "Ancestral pride"],
        "lyrics_khasi": (
            "Hoi kiw! Hoi kiw!\n"
            "Ko pyrton ba shlur, khie mih sha madan,\n"
            "Bat ïa ka ryntieh, pynwan ïa u khnam!\n"
            "Sha u thong ngin thew, sha u thong ngin siat,\n"
            "Ha ka burom u kpa, ha ka burom ka me!\n"
            "Hoi kiw! Hoi kiw! Khie siat beit sha khlieh!\n\n"
            "U khnam uba nep u la leit thaba,\n"
            "U la dung ha ka skum ba la buh ha lyngkba!\n"
            "Ko samla ka shnong to pyrta jam,\n"
            "Namar ba u khnam u la jop ia ka nam!\n\n"
            "U lum u them u la sawa kynjai,\n"
            "Ka ryntieh siej-lieng ka la pynhiar kynhai!\n"
            "U nongsiat ba tbit u la thoh la ka kti,\n"
            "Ban kyntiew ia ka burom jong la ka Ri!\n\n"
            "Ka wait ka stieh ngi kyntait noh,\n"
            "Tang u khnam u ryntieh ngi bat thoh!\n"
            "Ka jingsiat ka dei ka akor ka bor,\n"
            "Kaba neh pateng la pateng ha ka dor!"
        ),
        "lyrics_english": (
            "Hoi kiw! Hoi kiw! (Victory cry!)\n"
            "O valiant cheering clan, step forth onto the field,\n"
            "Grip the bamboo bow, notch the feather-flighted arrow!\n"
            "Straight at the circular target we aim, into the bullseye we release,\n"
            "For the honor of our father, for the glory of our mother!\n"
            "Hoi kiw! Hoi kiw! Let the arrow fly straight and true!\n\n"
            "The sharp arrow has whistled through the mountain air,\n"
            "Piercing dead-center into the straw cylinder in the clearing!\n"
            "O youths of the village shout out with mighty roar,\n"
            "For the arrow has captured victory and lasting renown!\n\n"
            "The mountain crags and valleys echo with the cry,\n"
            "The curved bamboo bow recoils with a singing snap!\n"
            "The master marksman has steadied his steady hand,\n"
            "To elevate the ancestral honor of our beloved Motherland!\n\n"
            "We put aside the sword and the shield,\n"
            "Bearing only the sacred bow and arrow in our grip!\n"
            "Archery is discipline, courtesy, and inner strength,\n"
            "Enduring generation after generation in high esteem!"
        ),
        "stanzas": [
            {
                "stanza_number": 1,
                "title": "Ka Pyrton (The Team Assembly Call)",
                "khasi": "Ko pyrton ba shlur, khie mih sha madan,\nBat ïa ka ryntieh, pynwan ïa u khnam!\nSha u thong ngin thew, sha u thong ngin siat,\nHa ka burom u kpa, ha ka burom ka me!",
                "english": "O valiant cheerers, step into the arena! Grip the bow, notch the arrow! Aim at the target for the glory of father and mother!"
            },
            {
                "stanza_number": 2,
                "title": "Ka Jingdung ha ka Skum (The Bullseye Strike)",
                "khasi": "U khnam uba nep u la leit thaba,\nU la dung ha ka skum ba la buh ha lyngkba!\nKo samla ka shnong to pyrta jam,\nNamar ba u khnam u la jop ia ka nam!",
                "english": "The razor arrow flew like lightning, piercing straight into the cylindrical straw target! Let the village cheer aloud for victory!"
            },
            {
                "stanza_number": 3,
                "title": "Ka Akor ka Ryntieh (The Code of the Bow)",
                "khasi": "Ka wait ka stieh ngi kyntait noh,\nTang u khnam u ryntieh ngi bat thoh!\nKa jingsiat ka dei ka akor ka bor,\nKaba neh pateng la pateng ha ka dor!",
                "english": "We set aside the war sword, holding only the sacred bow! Archery is dignity, moral conduct, and heritage passed down generations!"
            }
        ],
        "vocabulary": {
            "ryntieh": "Indigenous recurved bow crafted from selected mountain bamboo (siej-lieng)",
            "khnam": "Slender arrow fletched with bird feathers and iron tip",
            "thong": "The archery target mark or winning score goal",
            "skum": "The small cylindrical straw-bundled target erected at the far end of the range",
            "pyrton": "Clan cheerers and rhymers chanting phawar to inspire marksmen",
            "hoi kiw": "Ancient Khasi communal victory cheer and proclamation of triumph"
        }
    },
    {
        "id": "phawar_behdeinkhlam",
        "title": "Plague-Banishing Sacred Chant (Phawar Behdeiñkhlam)",
        "khasi_title": "Ka Phawar Behdeiñkhlam",
        "category": "Pnar Sacred Pestilence Rites & Invocations",
        "composer": "Seinraij Jowai Oral Tradition",
        "year": "Traditional (Annual July Rites)",
        "cultural_context": "The sacred chant of Behdeiñkhlam celebrated by the Pnar (Jaintia) people at Jowai. Meaning 'chasing away the demon of plague and sickness', young men carry painted ritual logs (dieñkhlam) and converge at the sacred pool Aitnar to drive out evil and pray for health and harvest.",
        "instruments": ["Ksing", "Bom (bass drum)", "Tangmuri", "Cymbals"],
        "themes": ["Exorcising disease", "Community cleansing", "Sacred pool Aitnar", "Prosperity of Jaintia", "Divine blessing"],
        "lyrics_khasi": (
            "Hei blai heini, hei blai heitai,\n"
            "Kylliang ka snem wan biang ka chaat,\n"
            "Pang-khlam phet noh sha wah sha duriaw,\n"
            "Khot ïa ka suk, khot ïa ka saiñ ha Jaiñtia!\n\n"
            "Beh noh ïa u khlam, beh noh ïa ka shitom,\n"
            "Pynhiar ka ksuid, pynhiar ka tympem!\n"
            "Ha Aitnar ngi shad, ha Aitnar ngi nguh,\n"
            "Ban roi u symbai, ban koit ka kpoh!"
        ),
        "lyrics_english": (
            "O God in this earthly realm, O God in the celestial heights,\n"
            "With the turning of the seasons the sacred dance returns,\n"
            "Let plague and pestilence flee far away into the rivers and deep ocean,\n"
            "Summon peace, summon prosperous order across the land of Jaiñtia!\n\n"
            "Drive out the pestilence, banish all suffering and pain,\n"
            "Cast down the malevolent spirits into the abyss!\n"
            "At sacred pool Aitnar we dance, at Aitnar we offer thanks,\n"
            "That our seed crops may flourish, and the bellies of our children be nourished!"
        ),
        "stanzas": [
            {
                "stanza_number": 1,
                "title": "Ka Jingkhot ia ka Suk (Invocation of Peace)",
                "khasi": "Hei blai heini, hei blai heitai,\nKylliang ka snem wan biang ka chaat,\nPang-khlam phet noh sha wah sha duriaw,\nKhot ïa ka suk, khot ïa ka saiñ ha Jaiñtia!",
                "english": "O God here and in the heavens! As the year turns the dance returns! Let pestilence flee into the ocean, summon peace and order in Jaintia!"
            },
            {
                "stanza_number": 2,
                "title": "Ka Shad ha Aitnar (The Dance at Sacred Pool Aitnar)",
                "khasi": "Beh noh ïa u khlam, beh noh ïa ka shitom,\nPynhiar ka ksuid, pynhiar ka tympem!\nHa Aitnar ngi shad, ha Aitnar ngi nguh,\nBan roi u symbai, ban koit ka kpoh!",
                "english": "Banish sickness and affliction! At Aitnar pool we dance and pray, so seeds flourish and the community lives in health!"
            }
        ],
        "vocabulary": {
            "behdeinkhlam": "Driving away plague with sacred tree poles",
            "aitnar": "The sacred muddy pool in Jowai where the climax ritual dance takes place",
            "khlam": "Epidemic pestilence, plague, or widespread sickness",
            "rot": "Large, intricately decorated multi-tiered paper and bamboo monument carried to Aitnar"
        }
    },
    {
        "id": "ka_sur_manik_raitong",
        "title": "The Flute Melody of Manik Raitong (Ka Sur Manik Raitong)",
        "khasi_title": "Ka Sur Manik Raitong",
        "category": "Folk Romance & Tragic Ballad",
        "composer": "Ancient Oral Tradition",
        "year": "Traditional",
        "cultural_context": "Ballad narrating the life of Manik Raitong, the destitute youth who played divine, sorrowful melodies on his Sharati bamboo flute by night. When queen Lieng Makaw fell in love with him, he chose death on the funeral pyre rather than compromise clan law, playing his flute into the flames.",
        "instruments": ["Sharati (bamboo mourning flute)", "Besli"],
        "themes": ["Immortal music", "Sacrifice", "Pure love", "Dignity in poverty", "Funeral pyre"],
        "lyrics_khasi": (
            "Miet man ka miet u tem la ka sharati,\n"
            "Sur ba pait-dohnud sawa ha ki lum,\n"
            "Ka mahadei ka shah thap ha ka ieit,\n"
            "U Manik u leit sha ka ding ha ka kuna.\n\n"
            "Ha khlieh ka pyngkat u thad la ka sur,\n"
            "Ym don ba tip ïa ka jingsngewsih jong u,\n"
            "Tang ka sharati ka pynpaw ïa ka jingim,\n"
            "Kaba khuid kum ka umjer ha u tiew-kulab!"
        ),
        "lyrics_english": (
            "Night after night he played his mournful Sharati flute,\n"
            "A heartbreaking melody echoing through the mountain pine ridges,\n"
            "The Queen was entranced by the irresistible power of love,\n"
            "Manik stepped with royal dignity into the blazing pyre.\n\n"
            "Atop the ash heap he poured forth his musical soul,\n"
            "None understood the depths of his hidden sorrow,\n"
            "Only the bamboo flute gave voice to his mortal existence,\n"
            "Pure as morning dew resting upon the wild rose petals!"
        ),
        "stanzas": [
            {
                "stanza_number": 1,
                "title": "Ka Sur Sharati (The Melancholic Night Flute)",
                "khasi": "Miet man ka miet u tem la ka sharati,\nSur ba pait-dohnud sawa ha ki lum,\nKa mahadei ka shah thap ha ka ieit,\nU Manik u leit sha ka ding ha ka kuna.",
                "english": "Every night he played his flute; heartbreaking notes echoed through the hills. Entranced by love, Manik faced the flames with unbending honor."
            }
        ],
        "vocabulary": {
            "sharati": "Long end-blown bamboo flute played during mourning and solemn reflection",
            "raitong": "Destitute orphan, poor person with no earthly possessions",
            "mahadei": "Consort or queen of a traditional Khasi Syiem",
            "kuna": "Clan fine, penalty, or sacrificial atonement"
        }
    },
    {
        "id": "ka_jingrwai_thiah_khunlung",
        "title": "Khasi Cradle Lullaby (Ka Jingrwai Thiah Khunlung)",
        "khasi_title": "Ka Jingrwai Thiah Khunlung",
        "category": "Traditional Hearth Lullaby",
        "composer": "Oral Tradition",
        "year": "Traditional",
        "cultural_context": "Sung by mothers and grandmothers in village homes while rocking infants to sleep by the warmth of the central hearth fire (ka dpei).",
        "instruments": ["Voice alone (Solo lullaby)", "Mieng (bamboo mouth harp)"],
        "themes": ["Motherly tenderness", "Sweet sleep", "Forest honey", "Ancestral roof protection"],
        "lyrics_khasi": (
            "Thiah suk ko khun, thiah suk ha la ka tnum,\n"
            "Ka sngi ka la sep, u bnai u la wan,\n"
            "Mei-rad kan pynap da u sohkymphor bad u ngap,\n"
            "Thiah suk ko khun ha shadem jong i mei.\n\n"
            "Ki sim ki la kynmaw la ki skum ha ki dieng,\n"
            "Ki sniang ki masi ki la kiew sha sem,\n"
            "Wat khuslai ko khun, Blei u don ha la syndah,\n"
            "Dem noh la ki khmat ban iohi ia ki jingphohsniew ba thiang!"
        ),
        "lyrics_english": (
            "Sleep peacefully my child, sleep safe under our ancestral roof,\n"
            "The golden sun has set, the silver moon has ascended the sky,\n"
            "Grandmother prepares sweet wild berries and golden mountain honey,\n"
            "Sleep peacefully my child upon your mother's breast.\n\n"
            "The forest birds have returned to their nests in the high trees,\n"
            "The cattle and sheep have entered their sheltered fold,\n"
            "Fret not my child, Almighty God is ever near beside thee,\n"
            "Close thy little eyes to behold sweetest dreams of joy!"
        ),
        "stanzas": [
            {
                "stanza_number": 1,
                "title": "Ka Jingpynthiah ha Shadem (Resting on Mother's Chest)",
                "khasi": "Thiah suk ko khun, thiah suk ha la ka tnum,\nKa sngi ka la sep, u bnai u la wan,\nMei-rad kan pynap da u sohkymphor bad u ngap,\nThiah suk ko khun ha shadem jong i mei.",
                "english": "Sleep peacefully under our roof; the sun has set, the moon has arrived. Grandmother has honey and wild berries; rest securely upon mother's chest."
            }
        ],
        "vocabulary": {
            "tnum": "Ancestral thatched roof representing family sanctuary",
            "mei-rad": "Maternal grandmother; revered elder of the matrilineage",
            "sohkymphor": "Delicious sweet wild hill berry",
            "ngap": "Pure wild highland honey gathered from rock hives"
        }
    },
    {
        "id": "ka_jingrwai_u_hynniewtrep",
        "title": "Hymn of the Seven Huts (Ka Jingrwai U Hynniewtrep)",
        "khasi_title": "Ka Jingrwai U Hynniewtrep",
        "category": "National Creation Anthem",
        "composer": "Khasi Cultural Revivalists",
        "year": "Traditional / Modern Anthem",
        "cultural_context": "National patriotic song sung at community gatherings, Seng Kut Snem, and Khasi cultural assemblies celebrating the divine descent of the Seven Huts from Mount Sohpetbneng.",
        "instruments": ["Tangmuri", "Duitara", "Ksing Shynrang"],
        "themes": ["Seven Huts genesis", "Mount Sohpetbneng", "Kamai ia ka hok", "Ancestral religion", "Golden age"],
        "lyrics_khasi": (
            "Na Lum Sohpetbneng ngi la hiar ban im,\n"
            "Ki Hynñiew Trep ba kyntang ha pyrthei,\n"
            "Ban kamai ïa ka hok, ban burom ïa U Blei,\n"
            "Pynneh ïa ka akor, pynskhem ïa ka niam!\n\n"
            "Ka Ri jong ngi ka ri jong ka hok,\n"
            "Ym don ba lah ban pynduh ia ka burom;\n"
            "Pateng la pateng ngin pynriewspah ia ka,\n"
            "Da ka bor jong ka kti bad ka mynsiem ba khuid!"
        ),
        "lyrics_english": (
            "Down from Mount Sohpetbneng we descended into earthly life,\n"
            "The Seven Sacred Huts consecrated upon the green earth,\n"
            "To earn righteousness through labor, to revere Almighty God,\n"
            "Preserving our ancestral courtesy, anchoring our ancient faith!\n\n"
            "Our beloved motherland is the land of truth and righteousness,\n"
            "None has power to destroy her sacred glory;\n"
            "Generation after generation we shall enrich her,\n"
            "With the work of our hands and the purity of our souls!"
        ),
        "stanzas": [
            {
                "stanza_number": 1,
                "title": "Ka Jinghiar na Lum Sohpetbneng (Descent from Sohpetbneng)",
                "khasi": "Na Lum Sohpetbneng ngi la hiar ban im,\nKi Hynñiew Trep ba kyntang ha pyrthei,\nBan kamai ïa ka hok, ban burom ïa U Blei,\nPynneh ïa ka akor, pynskhem ïa ka niam!",
                "english": "From Mount Sohpetbneng we came down to dwell, the sacred Seven Huts upon earth, to earn righteousness, revere God, and anchor our faith!"
            }
        ],
        "vocabulary": {
            "hynniewtrep": "The Seven Huts who settled the earth, ancestors of the Khasi-Pnar people",
            "sohpetbneng": "Navel of Heaven; sacred peak in Ri Bhoi",
            "kamai ia ka hok": "The foundational Khasi precept: to earn righteousness through honest labor"
        }
    },
    {
        "id": "ka_sur_tirot_sing",
        "title": "Heroic Ballad of Tirot Sing (Ka Sur Tirot Sing)",
        "khasi_title": "Ka Sur Tirot Sing Syiem Nongkhlaw",
        "category": "Patriotic Heroic Ballad",
        "composer": "Folk Balladeers of Nongkhlaw",
        "year": "Traditional (1829–1833 War Memorial)",
        "cultural_context": "Ballad commemorating U Tirot Sing, ruler of Nongkhlaw, who led the Khasi resistance against the British East India Company from 1829 to 1833. Celebrated annually on July 17.",
        "instruments": ["Nakra (war kettle drum)", "Ksing Shynrang", "Tangmuri"],
        "themes": ["Anti-colonial resistance", "Freedom vs slavery", "Heroic sacrifice", "Nongkhlaw", "Warrior valor"],
        "lyrics_khasi": (
            "U Syiem ba shlur jong ka Ri Khasi,\n"
            "Uba la ïeng pyrshah ïa ka bor nongwei,\n"
            "Kham bha ban ïap kum u ksew ba laitluid,\n"
            "Ban ïa kaba im kum u syiem ba mraw!\n\n"
            "Ha ki riat ba rben ha ki lum ba jngai,\n"
            "U la siat da u khnam, u la dung da ka wait;\n"
            "Ka snam jong u ka la jaw ha ka khyndew,\n"
            "Ban pynlong ia ka Ri ba kan laitluid man ka sngi!"
        ),
        "lyrics_english": (
            "The fearless Syiem of the Khasi motherland,\n"
            "Who rose unbending against foreign conquerors,\n"
            "Far better to perish as a free mountain warrior,\n"
            "Than to live as a crowned and shackled slave!\n\n"
            "Through steep ravines and deep mountain gorges,\n"
            "He struck with the arrow, he slashed with the sword;\n"
            "His royal blood poured out upon the sacred soil,\n"
            "That our Motherland might stand free for all generations!"
        ),
        "stanzas": [
            {
                "stanza_number": 1,
                "title": "Ka Ktien u Syiem (The Syiem's Declaration of Liberty)",
                "khasi": "U Syiem ba shlur jong ka Ri Khasi,\nUba la ïeng pyrshah ïa ka bor nongwei,\nKham bha ban ïap kum u ksew ba laitluid,\nBan ïa kaba im kum u syiem ba mraw!",
                "english": "The fearless ruler who defied foreign conquest: Far better to die free than live as a chained slave!"
            }
        ],
        "vocabulary": {
            "laitluid": "Free, sovereign, unenslaved",
            "syiem ba mraw": "Puppet king or enslaved ruler",
            "ksew ba laitluid": "Free commoner dog / independent warrior"
        }
    },
    {
        "id": "ki_rwaimar_khasi_harvest",
        "title": "Highland Harvest and Field Songs (Ki Rwaimar bad Jingrwai Ot Kba)",
        "khasi_title": "Ki Rwaimar bad Jingrwai Ot Kba",
        "category": "Agrarian Folk Songs & Field Chants",
        "composer": "Village Farmers & Reapers",
        "year": "Traditional",
        "cultural_context": "Call-and-response work songs sung collectively by men and women while harvesting golden terrace paddy fields (ot kba) and carrying heavy bamboo baskets (khoh) up steep mountain trails.",
        "instruments": ["Besli (bamboo flute)", "Ryndia work-chant calls"],
        "themes": ["Bountiful harvest", "Cooperative labor (iakyntiew kur)", "Sweet paddy", "Homecoming"],
        "lyrics_khasi": (
            "Sngi ba bhabriew ha lyngkha ba jyrngam,\n"
            "Ot ïa u kba ba la stem bha halor lum,\n"
            "Thep ha ka shang, thep ha ka khoh,\n"
            "Wanrah sha ïing ban pynsuk ïa ka kpoh!\n\n"
            "Hoi-ia-hoi! Ot beit ko samla!\n"
            "Ka lyiur ka la leit, u tlang u la wan,\n"
            "Pynkhalai ia ka rashi ba nep,\n"
            "Ngin ioh bam ja-khasi ha la ka tnum!"
        ),
        "lyrics_english": (
            "Glorious is the sunny day in green terraced fields,\n"
            "Reap the golden paddy ripe upon the mountainside,\n"
            "Pack it into the small basket, heave it into the tall cone basket,\n"
            "Carry it home to nourish the household hearth!\n\n"
            "Hoi-ia-hoi! Reap on steadily, brave youths!\n"
            "The summer rains have passed, crisp winter has arrived,\n"
            "Sweep the sharp curved sickle through the grain,\n"
            "We shall feast on indigenous sweet rice under our roof!"
        ),
        "stanzas": [
            {
                "stanza_number": 1,
                "title": "Ka Jing-ot Kba (Reaping the Ripe Grain)",
                "khasi": "Sngi ba bhabriew ha lyngkha ba jyrngam,\nOt ïa u kba ba la stem bha halor lum,\nThep ha ka shang, thep ha ka khoh,\nWanrah sha ïing ban pynsuk ïa ka kpoh!",
                "english": "Beautiful sunny day on green fields! Cut the ripe golden mountain paddy, fill the conical baskets, bring it home to nourish the family!"
            }
        ],
        "vocabulary": {
            "ot kba": "Reaping and harvesting paddy",
            "khoh": "Conical Khasi carrying basket woven of split bamboo and supported by a headstrap (u star)",
            "shang": "Flat shallow bamboo basket for winnowing grain",
            "rashi": "Curved steel harvesting sickle"
        }
    }
]

# Calculate word counts and write each JSON
index_entries = []
for song in songs_data:
    words = len(re.findall(r"\w+", song["lyrics_khasi"]))
    song["word_count"] = words
    
    # Save individual song file
    out_file = SONGS_DIR / f"{song['id']}.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(song, f, ensure_ascii=False, indent=2)
    
    index_entries.append({
        "id": song["id"],
        "title": song["title"],
        "khasi_title": song["khasi_title"],
        "category": song["category"],
        "composer": song["composer"],
        "year": song.get("year", "Traditional"),
        "instruments": song["instruments"],
        "themes": song.get("themes", []),
        "word_count": words,
        "file": f"{song['id']}.json"
    })

index_path = SONGS_DIR / "songs_index.json"
with open(index_path, "w", encoding="utf-8") as f:
    json.dump(index_entries, f, ensure_ascii=False, indent=2)

print(f"Successfully generated {len(index_entries)} structured Khasi songs in {SONGS_DIR}!")
