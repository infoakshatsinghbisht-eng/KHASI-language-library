# -*- coding: utf-8 -*-
"""
Khasi Traditional Music, Folk Instruments, Ballads, and Musicians.
Living organology and musical archive of the Khasi Hills (Meghalaya).
"""

from typing import Dict, List, Any, Optional

INSTRUMENTS: List[Dict[str, Any]] = [
    {
        "name": "Duitara",
        "category": "Chordophone (Stringed Lute)",
        "materials": "Jackfruit wood body, dried animal parchment resonator, muga/eri silk strings",
        "description": "The four-stringed plucked folk lute, revered as the living archive of Khasi oral history and genealogies. Played with a small wooden pick.",
        "cultural_role": "Central to bardic ballads, fireside storytelling, and folk songs celebrating ancestral nature.",
        "tuning": "Four strings symbolically representing family harmony and clan unity."
    },
    {
        "name": "Tangmuri",
        "category": "Aerophone (Double-reed Wind)",
        "materials": "Hardwood chanter with 7 finger holes, bamboo reed ('u spar'), flared wooden bell",
        "description": "Conical-bore double-reed pipe, honored as the 'Queen of Instruments' in Khasi sacred culture. High-pitched, penetrating, and resonant.",
        "cultural_role": "Played during Ka Pomblang Nongkrem, royal Syiem ceremonies, and sacred festival dances.",
        "symbolism": "Spiritual acoustic bridge between the living community and ancestral spirits."
    },
    {
        "name": "Ksing Shynrang",
        "category": "Membranophone (Male Lead Drum)",
        "materials": "Hollowed wood cylinder, double cowhide/deerskin membrane, leather tuning straps",
        "description": "Large cylindrical drum played by male master drummers with wooden sticks, setting the primary tempo and cadence for all public dances.",
        "cultural_role": "Indispensable in Shad Suk Mynsiem, Pomblang Nongkrem, and Seng Kut Snem processions.",
        "symbolism": "Represents the protective, steadfast strength of men in matrilineal society."
    },
    {
        "name": "Ksing Kynthei",
        "category": "Membranophone (Female Dance Drum)",
        "materials": "Wood cylinder, soft animal skin membrane",
        "description": "Smaller, rounder traditional drum providing softer rhythmic accompaniment specifically for maiden dance sequences.",
        "cultural_role": "Accompanies the delicate, gliding footsteps of unmarried maidens in festival squares.",
        "symbolism": "Represents grace, modesty, and the sacred continuum of maternal life."
    },
    {
        "name": "Nakra",
        "category": "Membranophone (Kettle Drum)",
        "materials": "Beaten copper/brass cauldron bowl, heavy leather membrane",
        "description": "Monumental royal kettle drum played with thick wooden beaters, producing a deep booming resonance heard across mountain valleys.",
        "cultural_role": "Stationed at royal Syiem headquarters (such as Smit) to announce assemblies, sacrifices, and solemn state declarations.",
        "symbolism": "Royal sovereignty and ancestral authority of the Syiemship."
    },
    {
        "name": "Ksing Padiah",
        "category": "Membranophone (Hand Drum)",
        "materials": "Small wooden frame, single or double skin membrane",
        "description": "Compact, portable hand drum played with swift fingertip strikes for sharp, syncopated rhythmic patterns.",
        "cultural_role": "Complements the main Ksing drums during dynamic dance shifts.",
        "symbolism": "Lively communal celebration and swift rhythmic agility."
    },
    {
        "name": "Maryngod",
        "category": "Chordophone (Bowed Fiddle)",
        "materials": "Carved hardwood body, parchment soundboard, two silk/gut strings, bamboo horsehair bow",
        "description": "Traditional bowed fiddle held vertically between the knees and played like a cello. Produces a haunting, melancholic tone.",
        "cultural_role": "Sacred mourning instrument played during funeral wakes and ancestral laments ('Jamlu').",
        "symbolism": "Expression of deep communal sorrow and farewell to departed souls."
    },
    {
        "name": "Mieng",
        "category": "Idiophone (Bamboo Jew's Harp)",
        "materials": "Seasoned highland bamboo strip with vibrating central tongue",
        "description": "Small handheld bamboo mouth harp held between the lips; oral cavity acts as variable acoustic resonator while the tongue is plucked.",
        "cultural_role": "Traditionally played by solitary shepherds and cattle herders in high pine meadows.",
        "symbolism": "Intimate pastoral reflection and whisper melodies."
    },
    {
        "name": "Besli",
        "category": "Aerophone (Bamboo Flute)",
        "materials": "Slender wild hill bamboo with 6 finger holes",
        "description": "Transverse bamboo flute played across highland villages, producing sweet, clear mountain airs.",
        "cultural_role": "Folk melodies, pastoral love songs, and accompanying informal evening hearth songs.",
        "symbolism": "Pristine nature and mountain serenity."
    },
    {
        "name": "Shyngwiang",
        "category": "Aerophone (End-blown Funeral Flute)",
        "materials": "Thick bamboo tube with end blowhole",
        "description": "Long end-blown bamboo flute producing solemn, low-pitched notes during bereavement rites.",
        "cultural_role": "Played by elders during funeral vigils to comfort the grieving matrilineal household.",
        "symbolism": "Transition from earthly life to ancestral realms ('Bam kwai ha ïing u Blei')."
    },
    {
        "name": "Kynshaw",
        "category": "Idiophone (Brass Cymbals)",
        "materials": "Bell metal / cast bronze",
        "description": "Small circular brass cymbals struck together to create a continuous shimmering metallic beat.",
        "cultural_role": "Rhythmic accompaniment in festival dance ensembles alongside Ksing and Tangmuri.",
        "symbolism": "Acoustic brilliance and joyous festive celebration."
    },
    {
        "name": "Symphiah",
        "category": "Ceremonial Regalia (Dance Whisk)",
        "materials": "Yak hair / white mountain grass plume, carved silver or polished bamboo handle",
        "description": "Sacred white plume whisk held by male dancers in Shad Suk Mynsiem, waved rhythmically in circles around the maidens.",
        "cultural_role": "Ceremonial protection dance symbol.",
        "symbolism": "Male duty to protect maternal kin, women, and the moral integrity of the clan."
    }
]

FOLK_SONGS: List[Dict[str, Any]] = [
    {
        "title": "Phawar Shad Suk Mynsiem",
        "genre": "Sacred Thanksgiving Chant",
        "theme": "Gratitude to God the Creator and Mother Earth for the spring harvest and communal health.",
        "context": "Chanted at Weiking grounds during the annual April festival.",
        "lyrics_khasi": (
            "Ka sngi kaba bhabriew, ka sngi kaba shai,\n"
            "Ki khun ki kti ki la mih ban shad ha Lympung,\n"
            "U ksing u sawa, ka tangmuri ka rih,\n"
            "Ka ksiar bad ka rupa ki phyrnai ha shadem,\n"
            "Ngin nguh ïa U Blei Nongthaw ha ka shad kmen!"
        ),
        "lyrics_english": (
            "The radiant day has dawned, pure and bright,\n"
            "Children and youths step forth to dance upon the sacred arena,\n"
            "The male drum booms forth, the Tangmuri sounds its melodious pipe,\n"
            "Gold and silver ornaments gleam brightly upon every chest,\n"
            "We bow in thanksgiving to God the Creator in our joyous dance!"
        )
    },
    {
        "title": "Phawar Iasiat Khnam",
        "genre": "Traditional Archery Battle Chant",
        "theme": "Valor, clan honor, and accuracy in highland archery tournaments.",
        "context": "Chanted by clan cheerers (pyrton) during tournament arrow releases.",
        "lyrics_khasi": (
            "Ko pyrton ba shlur, khie mih sha madan,\n"
            "Bat ïa ka ryntieh, pynwan ïa u khnam!\n"
            "Sha u thong ngin thew, sha u thong ngin siat,\n"
            "Ha ka burom u kpa, ha ka burom ka me!\n"
            "Hoi kiw! Hoi kiw! Khie siat beit sha khlieh!"
        ),
        "lyrics_english": (
            "O valiant team, step out boldly onto the field,\n"
            "Grip the bamboo bow, set the feather-flighted arrow!\n"
            "Direct to the target we aim, straight into the bullseye we shoot,\n"
            "For the honor of our father, for the glory of our mother!\n"
            "Hoi kiw! Hoi kiw! Let the arrow strike true!"
        )
    },
    {
        "title": "Phawar Behdeiñkhlam",
        "genre": "Pnar Sacred Pestilence Banishing Chant",
        "theme": "Expelling plague, disease, and social strife into the abyss, inviting peace to Jaintia.",
        "context": "Chanted at Aitnar sacred pool during Behdeiñkhlam at Jowai.",
        "lyrics_khasi": (
            "Hei blai heini, hei blai heitai,\n"
            "Kylliang ka snem wan biang ka chaat,\n"
            "Pang-khlam phet noh sha wah sha duriaw,\n"
            "Khot ïa ka suk, khot ïa ka saiñ ha Jaiñtia!"
        ),
        "lyrics_english": (
            "O God in this realm, O God in the celestial high,\n"
            "With the turning of the seasons, the holy dance returns,\n"
            "Let pestilence and sickness flee far away into the ocean deeps,\n"
            "Summon peace, summon prosperous order over Jaiñtia!"
        )
    },
    {
        "title": "Ka Sur U Sier Lapalang",
        "genre": "Traditional Funeral Elegy (Jamlu)",
        "theme": "Heart-rending maternal lament of the mother deer for her lost son who perished on the high mountain crags.",
        "context": "Foundation of Khasi weeping verse and tragic folk song cycles.",
        "lyrics_khasi": (
            "Ko khun baieit, ko Sier ba shlur,\n"
            "Balei me phet sha ki lum ba jngai?\n"
            "Ki khnam ki la thap, ki wait ki la nep,\n"
            "Me la kyllon ha ki lum ba sngewsih!"
        ),
        "lyrics_english": (
            "O my beloved fawn, O deer so brave and swift,\n"
            "Wherefore didst thou wander to the distant lonely hills?\n"
            "The arrows were set in wait, the hunter blades were sharp,\n"
            "Alas, thou hast fallen upon the sorrowful crags!"
        )
    },
    {
        "title": "Ka Sur Manik Raitong",
        "genre": "Folk Romance Ballad",
        "theme": "Soulful bamboo flute melody of the impoverished lover facing tragic sacrifice on the pyre.",
        "context": "Immortal folk tale celebrating the power of music over destiny.",
        "lyrics_khasi": (
            "Miet man ka miet u tem la ka sharati,\n"
            "Sur ba pait-dohnud sawa ha ki lum,\n"
            "Ka mahadei ka shah thap ha ka ieit,\n"
            "U Manik u leit sha ka ding ha ka kuna."
        ),
        "lyrics_english": (
            "Night after night he played his Sharati bamboo flute,\n"
            "Heart-breaking notes echoed across the lonely pine ridges,\n"
            "The Queen was entranced by the power of forbidden love,\n"
            "Manik stepped with dignity into the flames to accept his fate."
        )
    },
    {
        "title": "Ka Jingrwai Thiah Khunlung",
        "genre": "Traditional Lullaby",
        "theme": "Gentle maternal blessing soothing an infant to peaceful sleep with promises of forest berries and mountain honey.",
        "context": "Sung by mothers and grandmothers beside the evening hearth.",
        "lyrics_khasi": (
            "Thiah suk ko khun, thiah suk ha la ka tnum,\n"
            "Ka sngi ka la sep, u bnai u la wan,\n"
            "Mei-rad kan pynap da u sohkymphor bad u ngap,\n"
            "Thiah suk ko khun ha shadem jong i mei."
        ),
        "lyrics_english": (
            "Sleep peacefully my child, sleep safe under our ancestral roof,\n"
            "The golden sun has set, the silver moon has ascended,\n"
            "Grandmother prepares sweet wild berries and highland honey,\n"
            "Sleep peacefully my child upon your mother's breast."
        )
    },
    {
        "title": "Ka Jingrwai U Hynniewtrep",
        "genre": "National Creation Ballad",
        "theme": "Descent of the Seven Families from Mount Sohpetbneng to cultivate the sacred land in righteousness.",
        "context": "Seng Kut Snem and community cultural celebrations.",
        "lyrics_khasi": (
            "Na Lum Sohpetbneng ngi la hiar ban im,\n"
            "Ki Hynñiew Trep ba kyntang ha pyrthei,\n"
            "Ban kamai ïa ka hok, ban burom ïa U Blei,\n"
            "Pynneh ïa ka akor, pynskhem ïa ka niam!"
        ),
        "lyrics_english": (
            "Down from Mount Sohpetbneng we descended into mortal life,\n"
            "The Seven Sacred Huts consecrated upon the green earth,\n"
            "To earn righteousness through labor, to adore Almighty God,\n"
            "Preserving our ancestral courtesy, anchoring our ancient faith!"
        )
    },
    {
        "title": "Ka Sur Tirot Sing",
        "genre": "Patriotic Heroic Ballad",
        "theme": "The immortal sacrifice and anti-colonial resistance of the Syiem of Nongkhlaw.",
        "context": "U Tirot Sing Day (July 17) commemorations.",
        "lyrics_khasi": (
            "U Syiem ba shlur jong ka Ri Khasi,\n"
            "Uba la ïeng pyrshah ïa ka bor nongwei,\n"
            "Kham bha ban ïap kum u ksew ba laitluid,\n"
            "Ban ïa kaba im kum u syiem ba mraw!"
        ),
        "lyrics_english": (
            "The fearless Syiem of the Khasi motherland,\n"
            "Who stood tall and unyielding against foreign conquest,\n"
            "Far better to perish as a free mountain warrior,\n"
            "Than to rule as a crowned and shackled slave!"
        )
    }
]

MUSICIANS: List[Dict[str, Any]] = [
    {
        "name": "Bah Kerios Wahlang (1927 - 2020)",
        "title": "The Voice of the Khasi Hills & Duitara Maestro",
        "origin": "Mawngap, East Khasi Hills",
        "biography": "Legendary balladeer whose raspy, soulful voice and intricate Duitara picking preserved authentic Khasi folk songs, sacred groves lore, and highland ballads for nearly a century."
    },
    {
        "name": "Dr. Helen Giri",
        "title": "Padma Shri Musicologist & Indigenous Instrument Restorer",
        "origin": "Shillong, Meghalaya",
        "biography": "Pioneering academic and researcher who systematically revitalized traditional Khasi instruments (Duitara, Tangmuri, Maryngod) and founded community folk music training institutes."
    },
    {
        "name": "Lou Majaw (b. 1947)",
        "title": "Shillong Musical Icon & Cultural Balladeer",
        "origin": "Shillong, Meghalaya",
        "biography": "Revered music pioneer known across India for bridging indigenous hill melodies with acoustic folk and rock, symbolizing Shillong's status as India's music capital."
    },
    {
        "name": "Skendrowell Syiemlieh",
        "title": "Padma Shri Khasi Folk Balladeer",
        "origin": "West Khasi Hills",
        "biography": "Beloved folk minstrel whose radio broadcasts and live performances kept ancient Khasi pastoral melodies and village ballads alive in the modern era."
    },
    {
        "name": "Da-Thymmei Cultural Ensemble",
        "title": "Traditional Roots Ensemble",
        "origin": "Shillong",
        "biography": "Dedicated collective of young folk instrumentalists performing exclusively with indigenous instruments: Duitara, Tangmuri, Ksing, Nakra, and Mieng."
    },
    {
        "name": "Soulmate (Tipriti Kharbangar & Rudy Wallang)",
        "title": "Internationally Acclaimed Blues & Khasi Roots Ambassadors",
        "origin": "Shillong",
        "biography": "Pioneered roots blues infused with Khasi vocal cadence, performing on world stages from Memphis to Tokyo."
    }
]

def list_instruments() -> List[Dict[str, Any]]:
    """Return all traditional Khasi musical instruments."""
    return INSTRUMENTS

def get_instrument(name: str) -> Optional[Dict[str, Any]]:
    """Lookup musical instrument by name or classification."""
    q = name.lower().strip()
    for inst in INSTRUMENTS:
        if q in inst["name"].lower() or q in inst["category"].lower() or q in inst["description"].lower():
            return inst
    return None

def list_songs() -> List[Dict[str, Any]]:
    """Return documented traditional Khasi folk songs, chants, and ballads."""
    return FOLK_SONGS

def get_song(title: str) -> Optional[Dict[str, Any]]:
    """Lookup folk song by title or theme."""
    q = title.lower().strip()
    for s in FOLK_SONGS:
        if q in s["title"].lower() or q in s["theme"].lower() or q in s["genre"].lower():
            return s
    return None

def list_musicians() -> List[Dict[str, Any]]:
    """Return prominent Khasi folk balladeers, musicologists, and artists."""
    return MUSICIANS
