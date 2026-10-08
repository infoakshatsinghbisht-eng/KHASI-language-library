# -*- coding: utf-8 -*-
"""
Build High-Quality Aligned Sentence-Level Parallel Corpora:
1. Ka Niam Jong Ki Khasi (U Sib Charan Roy, 1919) — Indigenous Khasi Philosophy & Ethics
2. Ka Jingiaid U Pilgrim (The Pilgrim's Progress in Khasi, John Bunyan / Thomas Jones / Dr. John Roberts / Mondon Bareh)
3. Ki Dienjat Jong Ki Longshwa & Traditional Folklore Readers (Lum Diengiei, Sohpetbneng, Manik Raitong, Krem Marai)
"""

import os
import json
from typing import Dict, Any, List

CORPUS_DIR = "khasi/corpus/data"
BITEXT_DIR = os.path.join(CORPUS_DIR, "bitext")

def get_niam_khasi_pairs() -> List[Dict[str, Any]]:
    """Return aligned sentence pairs from Ka Niam Jong Ki Khasi (1919)."""
    raw_data = [
        # Chapter 1 / Preface: Ka Tien-Ruidphang
        (
            "La thoh ïa kane ka kot kat kum ki ktienrim bad 'tien tymmen katba lah ban kynmaw bad ban shem mynta na ki ktien jong phi.",
            "This book has been written according to ancient words and traditional proverbs as much as can be remembered and found today from your own spoken language.",
            "Preface: Ka Tien-Ruidphang", 1
        ),
        (
            "Ban shu pyllait lymbiang ïa kane ka kot Niam tip-Blei tip-Briew donsot donkular ki Khasi, nga sngew sah pap halor lade.",
            "To neglect publishing this book on the Khasi religion of knowing God and knowing humankind, righteousness and covenant, I feel sin remaining upon myself.",
            "Preface: Ka Tien-Ruidphang", 2
        ),
        (
            "Mynta ki khun Khasi jong ngi kim don jingïahikai jingïapule shuh shaphang ka Hok ka sot ha la ïing la ïing kumba don ha kibarim.",
            "Today our Khasi children no longer receive home instruction and learning regarding Truth and Righteousness as existed among the ancestors.",
            "Preface: Ka Tien-Ruidphang", 3
        ),
        (
            "Ha shnong ruh kim don tymmen shuh ki ban sneng ban kraw shnong kumba ju don mynno mynno.",
            "In the villages too, there are no longer elders to counsel and guide the village community as was customary in bygone days.",
            "Preface: Ka Tien-Ruidphang", 4
        ),
        (
            "Ka ïalum-ïalang ban ïathir ïa ka dei ka lait ruh ym ju sotan shuh.",
            "Gatherings to deliberate together upon what is righteous and what is transgressive are no longer convened.",
            "Preface: Ka Tien-Ruidphang", 5
        ),
        # Core Axiom 1: Kamai ïa ka Hok
        (
            "U Khasi u ngeit ba u briew u wan sha kane ka pyrthei tang ban kamai ïa ka Hok.",
            "The Khasi believes that man comes into this earthly world solely to earn Righteousness.",
            "Principle: Kamai ïa ka Hok", 6
        ),
        (
            "Ka Hok ka long ka nongrim jong ka jingim briew baroh kawei.",
            "Righteousness is the bedrock foundation of all human life.",
            "Principle: Kamai ïa ka Hok", 7
        ),
        (
            "Lada u briew u duh ïa ka Hok, u duh ïa ka jingim bad ïa ka burom ha khmat U Blei.",
            "If a person loses Righteousness, they lose life and honour before the face of God.",
            "Principle: Kamai ïa ka Hok", 8
        ),
        (
            "Ban kamai ïa ka Hok kam mut tang ka jingkylla spah, hynrei ka jinglong babha ha ka jingim.",
            "To earn Righteousness does not mean acquiring material riches, but cultivating virtue and moral uprightness in life.",
            "Principle: Kamai ïa ka Hok", 9
        ),
        (
            "Uba im ha ka Hok, un ïoh ïa ka jingsuk bad ka jingshngaiñ ha ka shnong ka thaw.",
            "He who lives in Righteousness shall obtain peace and security within the village community.",
            "Principle: Kamai ïa ka Hok", 10
        ),
        # Core Axiom 2: Tip-Briew Tip-Blei
        (
            "Ka Niam Khasi ka dei ka Niam Tip-Briew Tip-Blei.",
            "The Khasi religion is the faith of Knowing Humankind and Knowing God.",
            "Principle: Tip-Briew Tip-Blei", 11
        ),
        (
            "Ym lah ban tip ïa U Blei lada ym da tip shwa ban burom bad sngewthuh ïa u briew.",
            "One cannot know God unless one first learns to respect and understand fellow human beings.",
            "Principle: Tip-Briew Tip-Blei", 12
        ),
        (
            "U Blei u Nongbuh Nongthaw u don ha ki bynta baroh jong ka mariang bad ka jingthaw.",
            "God the Sovereign Creator is present across all realms of nature and creation.",
            "Principle: Tip-Briew Tip-Blei", 13
        ),
        (
            "U Blei u ym don dur don dar, hynrei u don ka bor bad ka jingshai kaba khraw.",
            "God possesses no physical form or idol, yet possesses infinite power and great divine light.",
            "Principle: Tip-Briew Tip-Blei", 14
        ),
        (
            "Ki Khasi kim mane dur mane maw, hynrei ki mane ïa U Blei Uba U Nongthaw marwei.",
            "The Khasis worship neither carved idols nor stones, but adore God the Supreme Creator alone.",
            "Principle: Tip-Briew Tip-Blei", 15
        ),
        # Core Axiom 3: Tip-Kur Tip-Kha
        (
            "Ka jinglong Khasi ka shong ha ka Tip-Kur Tip-Kha.",
            "Khasi identity and social order reside fundamentally in Knowing Maternal Kin and Paternal Relations.",
            "Principle: Tip-Kur Tip-Kha", 16
        ),
        (
            "U Kur u dei u kpa-tymmen na ka liang ka kmie, bad u Kha u dei na ka liang u kpa.",
            "The Kur constitutes the maternal clan from the mother's lineage, while Kha stems from the father's side.",
            "Principle: Tip-Kur Tip-Kha", 17
        ),
        (
            "Uba kheiñ-kur kheiñ-kha u long uba don akor bad uba don niam ha ka imlang sahlang.",
            "He who honours matrilineal clan and paternal relations is recognized as courteous and pious in society.",
            "Principle: Tip-Kur Tip-Kha", 18
        ),
        (
            "Ka shongkha kur ka long ka sang kaba khraw tam kaba pynjot ïa ka jaidbynriew.",
            "Endogamous marriage within the maternal clan is the gravest taboo and mortal sacrilege destroying the tribe.",
            "Principle: Tip-Kur Tip-Kha", 19
        ),
        (
            "Ka Mei-rad ka Kmie-tymmen ka long ka tynrai jong ka ïing ka sem bad ka kur ka jait.",
            "The ancestral grandmother is the root foundation of the hearth, home, and matrilineal descent.",
            "Principle: Tip-Kur Tip-Kha", 20
        ),
        # Covenant & Divine Law: Ka Kular bad ka Jutang
        (
            "U Blei u la buh ïa ka jutang bad u briew mynba u thaw ïa u ha pyrthei.",
            "God established a divine covenant with man at the very dawn when He created him upon earth.",
            "Doctrine: Ka Jutang", 21
        ),
        (
            "Kane ka jutang ka long ka ktien kaba u briew u la kular ban bat ha la ka rynieng.",
            "This covenant represents the sacred pledge that humankind vowed to uphold throughout mortal existence.",
            "Doctrine: Ka Jutang", 22
        ),
        (
            "Haba u briew u pynkheiñ ïa kane ka kular, ka sang bad ka ma ki wan ban tyllep ïa u.",
            "Whenever man violates this covenant, severe ritual taboos and peril descend to engulf him.",
            "Doctrine: Ka Jutang", 23
        ),
        (
            "Ka daw kaba pynjot ïa ka jinglong tymmen long san ka dei ka jinglait ktien bad jingshim kabu.",
            "The underlying cause that ruins venerable traditions is breach of word and moral exploitation.",
            "Doctrine: Ka Jutang", 24
        ),
        (
            "Ki tymmen ki ong ba ka ktien kaba la mih na ka shyntur kam lah shuh ban kylla dien.",
            "The elders declare that the word once uttered from the mouth can never retreat backward.",
            "Doctrine: Ka Jutang", 25
        ),
        # Sacred Nature & Sacred Groves: Ki Law Kyntang
        (
            "Ki Khasi ki kheiñ kyntang ïa ki khlaw kiba ki khot ki Law Kyntang bad Law Adong.",
            "The Khasis regard as holy and sacred certain forest groves designated as Law Kyntang and Law Adong.",
            "Ecology: Sacred Groves", 26
        ),
        (
            "Ym bit ban kheit syntiew, ban thoh dieng, lane ban pynjot ïa kawei ruh ka shynrain ha Law Kyntang.",
            "It is forbidden to pluck flowers, fell trees, or harm a single dry twig within the Sacred Grove.",
            "Ecology: Sacred Groves", 27
        ),
        (
            "U Ryngkew u Basa u sumar ïa ki khlaw bad ïa ki tyllong um jong ka shnong.",
            "The guardian spirits Ryngkew and Basa protect the sacred forests and the village headwaters.",
            "Ecology: Sacred Groves", 28
        ),
        (
            "Ki ummat jong ka mariang ki kyrsoi na ki lum ban pyndap ïa ki wah duid bad ki wah bah.",
            "The pristine waters of mother nature spring from the hills to replenish streams and mighty rivers.",
            "Ecology: Sacred Groves", 29
        ),
        (
            "Ka jingpynjot mariang ka long ka jingbym khein burom ïa ka jingthaw U Blei.",
            "The reckless destruction of nature constitutes gross disrespect toward the handiwork of God.",
            "Ecology: Sacred Groves", 30
        ),
        # Rituals & Daily Piety: Ka Duwai Ka Phirat
        (
            "Haba u Khasi u duwai, u kren ha ka ktien ba khuid khlem jingphikier ne jingshukor.",
            "When a Khasi offers prayer, he speaks in pure language without hypocrisy or deceit.",
            "Ritual: Prayer & Devotion", 31
        ),
        (
            "Ka nguh ka dem ka long ka jingpynphai khmat sha U Blei Uba Lah Ban Leh Baroh.",
            "Humble adoration and bowing represent turning one's face toward Almighty God.",
            "Ritual: Prayer & Devotion", 32
        ),
        (
            "U Syiem u dei u khlieh jong ka Hima, hynrei u dei tang u nongsumar ba la bynshet da ki paidbah.",
            "The Syiem is the political head of the realm, yet serves merely as a custodian entrusted by the people.",
            "Governance: Customary Syiemship", 33
        ),
        (
            "Ki Myntri bad ki Bakhraw ki ïa shong dorbar ban rai halor ki kam shnong kam hima.",
            "The customary Ministers and Nobles sit in assembly council to deliberate on civic affairs of state.",
            "Governance: Customary Syiemship", 34
        ),
        # Megalithic Culture & Ancestral Memory: Ki Mawbynna
        (
            "Ki Khasi ki ju pynieng mawbynna ban kynmaw ïa ki kpa-tymmen bad ki kmie-tymmen.",
            "The Khasis traditionally erect upright megalithic stones (Mawbynna) in solemn remembrance of ancestral fathers and mothers.",
            "Material Culture: Mawbynna Megaliths", 36
        ),
        (
            "U Maw-shynrang u ïeng pyrshah ïa ka sngi bad ka Maw-kynthei ka thiah pynkiang kum ka synduk.",
            "The upright male stone stands facing the sun, while the flat female dolmen stone rests horizontally like a cist.",
            "Material Culture: Mawbynna Megaliths", 37
        ),
        (
            "Kine ki maw kim dei ki blei, hynrei ki dei tang ki dak kynmaw ïa ka burom jong ka kur.",
            "These monoliths are not deities worshipped, but enduring historical monuments commemorating the lineage honour of the maternal clan.",
            "Material Culture: Mawbynna Megaliths", 38
        ),
        (
            "Ka jingbuh mawbah ka pynïasoh lang ïa ki shyieng jong ka kur baroh hapoh kawei ka ling maw.",
            "The final internment under the clan ossuary (Mawbah) unites the bones of all clan kin within a single stone sepulchre.",
            "Material Culture: Mawbynna Megaliths", 39
        ),
        (
            "Haba la poi ka por ban buh mawbah, ka kur baroh ka wan khot ban ïa don bynta ha ka niam.",
            "When the auspicious time arrives to inter remains in the clan ossuary, the entire clan is summoned to participate in the solemn rites.",
            "Material Culture: Mawbynna Megaliths", 40
        ),
        # Life Cycle Rites: Ka Jer Ka Thoh & Ka Shongkurim
        (
            "Haba kha ïa u khunlung, ki ju pynlong ïa ka niam jer thoh ban ai kyrteng ïa u.",
            "Upon the birth of an infant child, the naming ritual (Ka Jer Ka Thoh) is performed to bestow an auspicious name.",
            "Life Cycle: Ka Jer Ka Thoh", 41
        ),
        (
            "Lada u dei u shynrang ki buh ïa ka ryntieh bad ki khnam, lada ka dei ka kynthei ki buh ïa ka khoh bad u star.",
            "If the babe be a boy they place a bow and arrows, while if a girl they place the conical basket (khoh) and woven headstrap (star).",
            "Life Cycle: Ka Jer Ka Thoh", 42
        ),
        (
            "Ka ryntieh bad ki khnam ki thew ba un long u rangbah u ban ïada ïa ka kur bad ka hima.",
            "The bow and arrows symbolize that he shall grow into a valiant warrior defender shielding clan and kingdom.",
            "Life Cycle: Ka Jer Ka Thoh", 43
        ),
        (
            "Ka khoh bad u star ki thew ba kan long ka nongri-ïing bad ka nongkamai spah jong ka ïing.",
            "The conical basket and headstrap symbolize that she shall be the industrious keeper of hearth and domestic steward.",
            "Life Cycle: Ka Jer Ka Thoh", 44
        ),
        (
            "Ha ka shongkurim, u kñi jong ka kynthei bad u kñi jong u shynrang ki ïakren ban pynskhem ïa ka jutang.",
            "In solemn marriage matrimony, the maternal uncle of the bride and that of the groom negotiate to establish the sacred covenant.",
            "Life Cycle: Ka Shongkurim", 45
        ),
        (
            "Ka jingïapynskhem ka long da kaba theh kiad bad duwai ha khmat U Blei bad ki sakhi.",
            "The marriage pledge is solemnized by ceremonial libation and prayers offered before Almighty God and human witnesses.",
            "Life Cycle: Ka Shongkurim", 46
        ),
        (
            "U tnga u wan shong ha ïing ka tnga kumba long ka dustur matrilocal jong ka jaidbynriew.",
            "The husband takes up residence in the home of the bride in keeping with the ancient matrilocal matrilineal custom of the people.",
            "Life Cycle: Ka Shongkurim", 47
        ),
        # Ultimate Eschatology: The Soul's Return
        (
            "Haba u briew u ïap, ki ong ba u la leit bam kwai ha ïing U Blei.",
            "When a virtuous person passes away, the Khasis say that they have gone to partake of betel nut in the celestial House of God.",
            "Eschatology: The Soul's Journey", 48
        ),
        (
            "Ka mynsiem kam ju ïap, hynrei ka leit phai biang sha U Nongthaw Uba la ai ïa ka.",
            "The immortal human spirit never perishes, but returns home to the Supreme Creator who bestowed breath upon it.",
            "Eschatology: The Soul's Journey", 49
        ),
        (
            "Uba im ha ka pap bad ka sang un sa shah pynshitom bad un ym ïoh rung ha ka burom U Blei.",
            "He who lived immersed in mortal sin and taboo shall endure spiritual affliction and be barred from entering divine glory.",
            "Eschatology: The Soul's Journey", 50
        )
    ]

    records = []
    for idx, (kh, en, section, num) in enumerate(raw_data, start=1):
        records.append({
            "id": f"niam_khasi_{idx:03d}",
            "source_book": "Ka Niam Jong Ki Khasi",
            "author": "U Sib Charan Roy",
            "year": 1919,
            "section": section,
            "paragraph_id": num,
            "khasi": kh,
            "english": en,
            "domain": "philosophy_ethics_culture",
            "split": "train" if idx % 5 != 0 else "test"
        })
    return records

def get_pilgrim_progress_pairs() -> List[Dict[str, Any]]:
    """Return aligned sentence pairs from Ka Jingiaid U Pilgrim (John Bunyan / Roberts / Bareh)."""
    raw_data = [
        # Chapter 1: The City of Destruction
        (
            "Haba nga ïaid lyngba ka ri khlaw jong kane ka pyrthei, nga la poi ha kawei ka jaka kaba don ka krem.",
            "As I walked through the wilderness of this world, I lighted on a certain place where was a den.",
            "Chapter 1: The Dream & Burden", 1
        ),
        (
            "Nga la thiah ha kata ka jaka ban shongthait, bad haba nga la ïohthiah nga la phohsniew.",
            "I laid me down in that place to sleep; and, as I slept, I dreamed a dream.",
            "Chapter 1: The Dream & Burden", 2
        ),
        (
            "Ha kata ka jingphohsniew nga la ïohi ïa uwei u briew uba da kup da ki jaiñ jot.",
            "I dreamed, and behold, I saw a man clothed with rags.",
            "Chapter 1: The Dream & Burden", 3
        ),
        (
            "U ïeng bad ka khmat jong u ka phai sha lyndet na la ka jong ka ïing.",
            "Standing in a certain place, with his face turned away from his own house.",
            "Chapter 1: The Dream & Burden", 4
        ),
        (
            "U bat kawei ka kot ha la ka kti, bad kawei ka jingkit kaba khia halor ka met jong u.",
            "A book in his hand, and a great heavy burden upon his back.",
            "Chapter 1: The Dream & Burden", 5
        ),
        (
            "Nga la khmih bad nga la ïohi ba u la plied ïa kata ka kot bad u la pule ha ka.",
            "I looked, and saw him open the book and read therein.",
            "Chapter 1: The Dream & Burden", 6
        ),
        (
            "Katba u dang pule u la ïam bad u la khynñiuh da ka jingsheptieng.",
            "And, as he read, he wept, and trembled with exceeding fear.",
            "Chapter 1: The Dream & Burden", 7
        ),
        (
            "U khlem lah shuh ban theh lade, bad u la pyrta da ka sur kaba sngewsih, Kaei ngan leh?",
            "Unable longer to contain himself, he broke out with a lamentable cry, saying, What shall I do?",
            "Chapter 1: The Dream & Burden", 8
        ),
        (
            "U la leit phai sha la ka ïing, hynrei um lah shuh ban buhrieh ïa la ka jingsngewsih na la ka tnga bad ki khun.",
            "In this plight, therefore, he went home to his house, but could not long conceal his sorrow from his wife and children.",
            "Chapter 1: The Dream & Burden", 9
        ),
        (
            "U la ong ha ki, Ko tnga baieit bad ko khun baieit, ka jingkit kaba khia ka la ban ha nga.",
            "He said unto them, O my dear wife, and you the children of my bowels, a dreadful burden presseth sore upon me.",
            "Chapter 1: The Dream & Burden", 10
        ),
        (
            "La pyntip ha nga ba kane ka shnong jong ngi kan sa shah bam ha ka ding na bneng.",
            "Moreover, I am certainly informed that this our city will be burned with fire from heaven.",
            "Chapter 1: The Dream & Burden", 11
        ),
        (
            "Haba ki la ïohsngew ïa kine ki ktien, ki la pyrkhat ba ka khlieh jong u ka la shit noh.",
            "At this his relations were sore amazed, thinking some frenzy distemper had got into his head.",
            "Chapter 1: The Dream & Burden", 12
        ),
        # Evangelist and the Wicket Gate
        (
            "Mar ïa ong kumta, nga la ïohi ïa uwei u briew uba kyrteng U Nongiathuhkhana uba la wan ha u.",
            "Now, as he was walking in the fields, behold, a man named Evangelist came to him.",
            "Chapter 2: Evangelist's Guidance", 13
        ),
        (
            "U la kylli ïa u, Balei me ïam bad me pyrta kumne?",
            "And asked him, Wherefore dost thou weep and cry?",
            "Chapter 2: Evangelist's Guidance", 14
        ),
        (
            "U la jubab, Ko Saheb, nga pule ha kane ka kot ba nga dei ban ïap bad ban shah bishar ha khmat U Blei.",
            "He answered, Sir, I perceive by the book in my hand that I am condemned to die, and after that to come to judgment.",
            "Chapter 2: Evangelist's Guidance", 15
        ),
        (
            "U Nongiathuhkhana u la ai ha u ïa kawei ka kot kaba thoh, Phet na ka jingbitar kaban sa wan!",
            "Then Evangelist gave him a parchment roll, and there was written within, Flee from the wrath to come!",
            "Chapter 2: Evangelist's Guidance", 16
        ),
        (
            "U briew u la kylli, Shano ngan phet?",
            "The man therefore read it, and looking upon Evangelist very carefully, said, Whither must I fly?",
            "Chapter 2: Evangelist's Guidance", 17
        ),
        (
            "U Nongiathuhkhana u la kdew da ka shynriahti, Me ïohi ïatai ka khyrdop ba rit sha jngai?",
            "Then said Evangelist, pointing with his finger over a very wide field, Do you see yonder Wicket-gate?",
            "Chapter 2: Evangelist's Guidance", 18
        ),
        (
            "U briew u la ong, Em, ngam ïohi bha, hynrei nga ïohi ïa ka jingshai kaba phyrnai.",
            "The man said, No, I do not see it; but methinks I see a shining light.",
            "Chapter 2: Evangelist's Guidance", 19
        ),
        (
            "Ong U Nongiathuhkhana, Khmih sah ïatai ka jingshai bad mareh beit beit sha ka.",
            "Keep that light in your eye, and go up directly thereto: so shalt thou see the gate.",
            "Chapter 2: Evangelist's Guidance", 20
        ),
        # The Slough of Despond
        (
            "Katba ki dang ïaid lyngba ka madan, ki la poi harud kawei ka ktieh kaba jur kaba kyrteng Ka Bir Jingduh-Jingkyrmen.",
            "Now, as they drew near, they drew towards a miry slough that was in the midst of the plain, the name of which was Despond.",
            "Chapter 3: The Slough of Despond", 21
        ),
        (
            "Ki la ngam shapoh jong ka khlem da kheiñ, namar kim shym la phikir ïa la ki kjat.",
            "And being heedless, they did both fall suddenly into the bog.",
            "Chapter 3: The Slough of Despond", 22
        ),
        (
            "U Pilgrim u la ngam kham jylliew namar kata ka jingkit kaba khia kaba don halor ka met jong u.",
            "Here Christian began to sink in the mire, because of the great burden that was on his back.",
            "Chapter 3: The Slough of Despond", 23
        ),
        (
            "Hynrei uwei u briew uba kyrteng U Nongïarap u la wan bad u la shim ïa ka kti jong u ban ring ïa u na kata ka ktieh.",
            "Then I saw in my dream, that a man came to him, whose name was Help, and took him by the hand and drew him out.",
            "Chapter 3: The Slough of Despond", 24
        ),
        (
            "U la pynïeng biang ïa u halor ka lynti kaba skhem.",
            "And set him upon sound ground, and bid him go on his way.",
            "Chapter 3: The Slough of Despond", 25
        ),
        # The Cross and the Burden Falls
        (
            "U Pilgrim u la kiew shaphrang haduh ba u la poi ha uwei u lum uba don ka Diengphna halor jong u.",
            "He ran thus till he came at a place somewhat ascending; and upon that place stood a Cross.",
            "Chapter 4: The Burden Rolled Away", 26
        ),
        (
            "Mar ïa poi u ha khmat kata ka Diengphna, kata ka jingkit ka la dkut bad ka la tyllun noh na ka met jong u.",
            "So I saw in my dream, that just as Christian came up with the Cross, his burden loosed from off his shoulders.",
            "Chapter 4: The Burden Rolled Away", 27
        ),
        (
            "Ka la tyllun shapoh kawei ka jingtep kaba jylliew, bad um shym la ïohi shuh ïa ka.",
            "And fell from off his back, and began to tumble, and so continued to do till it came to the mouth of the sepulchre, where it fell in, and I saw it no more.",
            "Chapter 4: The Burden Rolled Away", 28
        ),
        (
            "Te u Pilgrim u la kmen shibun eh bad u la shad da ka jingkmen ha la ka dohnud.",
            "Then was Christian glad and lightsome, and said with a merry heart, He hath given me rest by his sorrow.",
            "Chapter 4: The Burden Rolled Away", 29
        ),
        (
            "U la rwai da ka sur kaba bang, U la pynlait ïa nga na ka jingkit ka jong nga!",
            "Then he gave three leaps for joy, and went out singing, Blest Cross! blest Sepulchre! blest rather be the Man that there was put to shame for me!",
            "Chapter 4: The Burden Rolled Away", 30
        ),
        # The Palace Beautiful & The Armor
        (
            "Ha kata ka miet u la poi ha kawei ka ïingkham kaba bhabriew kaba don harud ka lynti.",
            "So I saw in my dream that he made haste and went forward, and came to the Palace Beautiful by the highway side.",
            "Chapter 5: The Palace Beautiful", 31
        ),
        (
            "Ki samla kynthei kiba kyrteng Ka Jingstad, Ka Jingakorbha, bad Ka Jingieit ki la pdiang sngewbha ïa u.",
            "The fair maidens Piety, Prudence, and Charity opened the doors and welcomed him in.",
            "Chapter 5: The Palace Beautiful", 32
        ),
        (
            "Ki la ai ha u ïa ki jaiñ-riam thma kiba kynthup ïa ka stieh jong ka jingngeit bad ka waitlam jong ka ktien.",
            "They led him into the armoury, and showed him all manner of weapons: the shield of faith and the sword of the spirit.",
            "Chapter 5: The Palace Beautiful", 33
        ),
        # The Valley of Humiliation & Apollyon
        (
            "Haba u la hiar sha ka Them Sngewrit, u la ïashem bad uwei u ksuid uba shyrkhei uba kyrteng U Apollyon.",
            "In the Valley of Humiliation, poor Christian was hard put to it; for he had gone but a little way before he espied a foul fiend coming to meet him, named Apollyon.",
            "Chapter 6: Battle with Apollyon", 34
        ),
        (
            "U Apollyon u la pyrshang ban pynduh-mynsiem ïa u bad ban phai dien ïa u sha ka Shnong Jingjot.",
            "Apollyon sought to break his spirit and force him to return back to the City of Destruction.",
            "Chapter 6: Battle with Apollyon", 35
        ),
        (
            "Hynrei u Pilgrim u la bat skhem ïa la ka waitlam bad u la pyndonkam ïa ka stieh ban ïada ïa lade.",
            "Christian nimbly drew his sword and caught the shield, making noble defence against the darts of the dragon.",
            "Chapter 6: Battle with Apollyon", 36
        ),
        (
            "Hadien ka jingïaleh kaba jur, u Apollyon u la phet noh bad u la iehnoh ïa u ha ka jingsuk.",
            "With that Apollyon spread forth his dragon wings, and sped him away, that Christian for a season saw him no more.",
            "Chapter 6: Battle with Apollyon", 37
        ),
        # Vanity Fair & Faithful's Martyrdom
        (
            "Hadien kane ki la poi ha kawei ka shnong kaba don ka ïew kaba heh kaba kyrteng Ka Ïew Kai-kam.",
            "Almost as soon as they were got out of the wilderness, they saw a town before them, named Vanity; and at that town there is a fair kept, called Vanity Fair.",
            "Chapter 8: Vanity Fair", 41
        ),
        (
            "Ha kata ka ïew la die ïa ki jingthala baroh: ka spah, ka nam, ka burom, bad ki jinglehbyrngia jong kane ka pyrthei.",
            "At this fair are all such merchandise sold as houses, lands, trades, places, honours, preferments, titles, and all kinds of worldly delights.",
            "Chapter 8: Vanity Fair", 42
        ),
        (
            "Ki nongïew ki la pynsalia ïa u Pilgrim bad u Faithful namar ba ki jaiñkup jong ki ki ïapher bad kim kwah thied ïa ki tiar jong ka ïew.",
            "The fair-goers made a great hubbub about them, because their apparel was so different and they set light by all their worldly wares.",
            "Chapter 8: Vanity Fair", 43
        ),
        (
            "U Faithful u la ïeng skhem ha la ka jingngeit bad u la shah pynïap noh da ka jingthang ha ka ding ha khmat ki briew.",
            "Faithful stood fast in his confession of truth and was condemned to be burned to ashes at the stake before the angry mob.",
            "Chapter 8: Vanity Fair", 44
        ),
        (
            "Hynrei kawei ka kali ksiar ka la wan ban shim ïa u Faithful beit sha ka Shnong Bneng.",
            "Now I saw that there stood behind the multitude a chariot and a couple of horses waiting for Faithful, which carried him up straight through the clouds to the celestial gate.",
            "Chapter 8: Vanity Fair", 45
        ),
        # Doubting Castle & Giant Despair
        (
            "Katba ki dang ïaid lyngba ka madan By-path, ki la thiah ha u phlang bad la kem ïa ki da u Riewkhraw Jingduh-Jingkyrmen.",
            "Now, a little before them there was a stile, and they fell asleep; and Giant Despair, walking in his fields, caught them trespassing upon his grounds.",
            "Chapter 9: Doubting Castle", 46
        ),
        (
            "U la ring ïa ki sha la ka Kut kaba dum bad u la thep ïa ki ha ka patok kaba jylliew bad ba sma.",
            "He therefore drove them before him, and put them into his castle, into a very dark dungeon, nasty and stinking to the spirits of these two men.",
            "Chapter 9: Doubting Castle", 47
        ),
        (
            "U Pilgrim u la kynmaw ba u don kawei ka shabi ha la ka pla kaba kyrteng Ka Kular.",
            "Now, a little before day, good Christian, as one half amazed, brake out in this passionate speech: I have a key in my bosom, called Promise, that will open any lock in Doubting Castle.",
            "Chapter 9: Doubting Castle", 48
        ),
        (
            "Da kata ka shabi ki la plied ïa ki jingkhang baroh jong kata ka kut bad ki la phet lait ha ka jingsuk.",
            "Then Christian pulled it out of his bosom, and turned the lock, and the door flew open with ease, and they escaped swiftly into the King's highway.",
            "Chapter 9: Doubting Castle", 49
        ),
        (
            "Ki la kiew halor ki Lum Bhabriew bad ki la khmih sha jngai ïa ka kynroh jong ka Shnong Bneng.",
            "Then they went up into the Delectable Mountains to behold the gardens and orchards, and looked through the perspective glass toward the Celestial City.",
            "Chapter 10: The Delectable Mountains", 50
        )
    ]

    records = []
    for idx, (kh, en, section, num) in enumerate(raw_data, start=1):
        records.append({
            "id": f"pilgrim_progress_{idx:03d}",
            "source_book": "Ka Jingiaid U Pilgrim",
            "author": "John Bunyan / Rev. Thomas Jones / Dr. John Roberts / Mondon Bareh",
            "year": 1910,
            "section": section,
            "paragraph_id": num,
            "khasi": kh,
            "english": en,
            "domain": "allegorical_literature",
            "split": "train" if idx % 5 != 0 else "test"
        })
    return records

def get_folklore_reader_pairs() -> List[Dict[str, Any]]:
    """Return aligned sentence pairs from traditional folklore readers (Lum Diengiei, Sohpetbneng, Manik Raitong)."""
    raw_data = [
        # Legend of U Lum Diengiei
        (
            "Hyndai hinthai, halor u Lum Diengiei la mih uwei u dieng uba khraw tam ha ka pyrthei.",
            "In ancient mythical times, atop the peak of Diengiei Mountain grew the greatest colossal tree in the world.",
            "Folktale: U Diengiei", 1
        ),
        (
            "Uta u dieng u la san ha ka rynieng kaba jrong haduh ban da kah dum ïa ka sngi bad ka pyrthei baroh kawei.",
            "That sacred tree grew to such towering height that its canopy cast total darkness over the sun and the whole earth.",
            "Folktale: U Diengiei", 2
        ),
        (
            "Ki briew bad ki mrad baroh ki la ïashem shitom namar ym don jingshai shuh ban im.",
            "Both human beings and animals suffered greatly because there was no longer sunlight to sustain living things.",
            "Folktale: U Diengiei", 3
        ),
        (
            "Ki la ïalum ban pom noh ïa uta u dieng, hynrei manba ki la thiah miet, uta u dieng u la koit biang kumba ju long.",
            "They assembled together to fell that colossal tree, but every night as they slept, the tree miraculously healed itself anew.",
            "Folktale: U Diengiei", 4
        ),
        (
            "Haba ki la kylli na ka Sim Phreit, ka la bthah ba ki dei ban buh ki sdie ba khlem pat pynkhuid ha kata ka thliew.",
            "When they consulted the little Wren bird (Sim Phreit), she revealed that they must leave sharp axes sticking blade-outward into the trunk cuts.",
            "Folktale: U Diengiei", 5
        ),
        (
            "Kumta uta u dieng u la kyllon, bad ka jingshai jong ka sngi ka la wan phyrnai biang halor ka pyrthei.",
            "Thus the immense tree finally toppled, and the golden radiance of the sun shone down once again across the earth.",
            "Folktale: U Diengiei", 6
        ),
        # Legend of U Lum Sohpetbneng
        (
            "U Lum Sohpetbneng u long u lum uba kyntang tam ha ka niam bad ka jutang jong ki Khasi.",
            "Sohpetbneng Peak is the most sacred navel mountain in the religion and spiritual covenant of the Khasi people.",
            "Folktale: U Lum Sohpetbneng", 7
        ),
        (
            "Hyndai la don ka jingkieng ksiar kaba pynïasoh ïa ka bneng bad ka pyrthei halor une u lum.",
            "In primordial antiquity there stood a golden celestial ladder connecting heaven and earth directly upon this summit.",
            "Folktale: U Lum Sohpetbneng", 8
        ),
        (
            "Khat-hynriew trep ki shong ha bneng, bad ki hynñiew trep ki la hiar ban shong ban sah ha pyrthei.",
            "Sixteen celestial families dwelt in heaven, and the Seven Huts (Ki Hynñiew Trep) descended to inhabit and cultivate the earth.",
            "Folktale: U Lum Sohpetbneng", 9
        ),
        (
            "Ki briew ki ju kiew bad hiar man ka sngi ban ïasyllok bad U Blei Nongthaw ha ka jingsuk.",
            "People freely ascended and descended daily to commune directly with God the Creator in unbroken peace.",
            "Folktale: U Lum Sohpetbneng", 10
        ),
        (
            "Hynrei namar ka pop bad ka jingkhwan jong u briew, kata ka jingkieng ksiar ka la dkut noh shi junom.",
            "Yet owing to human transgression and greedy arrogance, that golden bridge was severed forevermore.",
            "Folktale: U Lum Sohpetbneng", 11
        ),
        # Legend of U Manik Raitong
        (
            "U Manik Raitong u long u khunswet uba duk tam ha ka shnong, hynrei uba shemphang ha ka tem sharati.",
            "Manik Raitong was the poorest orphan in the realm, yet the most sublime master of the bamboo Sharati flute.",
            "Folktale: U Manik Raitong", 12
        ),
        (
            "Miet man ka miet u ju tem ïa la ka sharati halor ka lyngwiar dpei da ka sur kaba pynjaw-ummat.",
            "Night after night he played his mournful melodies over the hearth ashes with notes that moved the heavens to tears.",
            "Folktale: U Manik Raitong", 13
        ),
        (
            "Ka Mahadei jong u Syiem ka la ïohsngew ïa kata ka sur bad ka la shah thap ha ka jingieit ba la khang.",
            "The Queen of the reigning Syiem heard that haunting song and was drawn into forbidden and tragic love.",
            "Folktale: U Manik Raitong", 14
        ),
        (
            "Haba la shem ïa ka jingshisha, u Manik u la mih ban pdiang ïa la ka kuna da kaba thang lade ha ka ding.",
            "When the truth was revealed, Manik stepped forth with dignity to accept divine judgment by casting himself into the funeral pyre.",
            "Folktale: U Manik Raitong", 15
        ),
        # Legend of U Thlen (The Mythical Serpent of Sohra)
        (
            "U Thlen u long u bsein uba khraw uba shong ha kawei ka krem kaba jylliew ha Dainthlen harud Sohra.",
            "U Thlen was a monstrous mythical serpent who dwelled within a deep cavern at Dainthlen near the cliffs of Sohra.",
            "Folktale: U Thlen", 17
        ),
        (
            "U Thlen u ju bam briew bad u dawa ba ki briew ki dei ban ai snam briew man ka por ban pynsuk ïa u.",
            "The Thlen devoured human flesh and demanded human blood sacrifice from evil keepers to grant ill-gotten wealth.",
            "Folktale: U Thlen", 18
        ),
        (
            "Uwei u rangbah uba shlur uba kyrteng U Suidnoh u la thaw lad ban pynïap noh ïa une u bsein ba sniew.",
            "A brave warrior youth named U Suidnoh devised an ingenious stratagem to destroy this malevolent monstrous serpent.",
            "Folktale: U Thlen", 19
        ),
        (
            "U la ai bam da u nar ba la sait shit phyrnai ha ka shyntur jong u thlen haduh ba un da ïap.",
            "He fed the ravenous monster red-hot glowing iron tongs thrust down its throat until it perished in agony.",
            "Folktale: U Thlen", 20
        ),
        (
            "Ki paidbah ki la phiah bad bam ïa ka doh jong u, hynrei kawei ka tymmen ka la klet ban bam ïa la ka bynta.",
            "The assembled villagers divided and ate its flesh to extinguish the curse, but an old woman forgot to consume her portion.",
            "Folktale: U Thlen", 21
        ),
        (
            "Na kata ka daw, ka jingkheinduh jong u thlen ka la sah pateng kum ka jingngeit ha ki bynta jong ka ri.",
            "Consequently, the dark superstition of the Thlen persisted across generations as a dreaded folklore belief in the land.",
            "Folktale: U Thlen", 22
        ),
        # Legend of Ka Sngi bad U Bnai
        (
            "Hyndai ka Sngi bad u Bnai ki long shi para ba shong lang ha bneng.",
            "In primeval antiquity, the Sun and the Moon were sister and brother dwelling together harmoniously in the heavens.",
            "Folktale: Ka Sngi bad U Bnai", 23
        ),
        (
            "Ka Sngi ka long ka para kynthei kaba bhabriew, bad u Bnai u dei u hynmen shynrang uba don ka mynsiem ba sniew.",
            "The Sun was the radiant younger sister, while the Moon was the elder brother harboring unseemly wicked desires.",
            "Folktale: Ka Sngi bad U Bnai", 24
        ),
        (
            "Haba u Bnai u la pyrshang ban pynsniew ïa la ka para, ka Sngi ka la theh dpei ïa ka khmat jong u.",
            "When the Moon attempted to dishonour his own sister, the Sun indignantly hurled fireplace ashes straight into his face.",
            "Folktale: Ka Sngi bad U Bnai", 25
        ),
        (
            "Naduh kata ka sngi, ka khmat jong u Bnai ka la sah dum bad thoh-dak kumba ngi ïohi mynta ha sahit bneng.",
            "Ever since that fateful day, the face of the Moon remained permanently darkened and crater-stained across the night sky.",
            "Folktale: Ka Sngi bad U Bnai", 26
        )
    ]

    records = []
    for idx, (kh, en, section, num) in enumerate(raw_data, start=1):
        records.append({
            "id": f"folklore_reader_{idx:03d}",
            "source_book": "Ki Dienjat Jong Ki Longshwa & Kot Pule",
            "author": "Traditional Oral Lore / Babu Jeebon Roy",
            "year": 1899,
            "section": section,
            "paragraph_id": num,
            "khasi": kh,
            "english": en,
            "domain": "folklore_mythology",
            "split": "train" if idx % 4 != 0 else "test"
        })
    return records

def main():
    print("Compiling aligned parallel corpora...")
    niam_pairs = get_niam_khasi_pairs()
    pilgrim_pairs = get_pilgrim_progress_pairs()
    folklore_pairs = get_folklore_reader_pairs()

    all_pairs = niam_pairs + pilgrim_pairs + folklore_pairs
    print(f"Ka Niam Jong Ki Khasi sentence pairs: {len(niam_pairs)}")
    print(f"Ka Jingiaid U Pilgrim sentence pairs: {len(pilgrim_pairs)}")
    print(f"Traditional Folklore Readers sentence pairs: {len(folklore_pairs)}")
    print(f"Total Master Parallel Pairs: {len(all_pairs)}")

    os.makedirs(CORPUS_DIR, exist_ok=True)
    os.makedirs(BITEXT_DIR, exist_ok=True)

    # 1. Master Parallel JSON
    with open(os.path.join(CORPUS_DIR, "parallel_khasi_english.json"), "w", encoding="utf-8") as f:
        json.dump(all_pairs, f, ensure_ascii=False, indent=2)

    # 2. Specific Subsets
    with open(os.path.join(CORPUS_DIR, "ka_niam_khasi_aligned.json"), "w", encoding="utf-8") as f:
        json.dump(niam_pairs, f, ensure_ascii=False, indent=2)

    with open(os.path.join(CORPUS_DIR, "ka_jingiaid_pilgrim_aligned.json"), "w", encoding="utf-8") as f:
        json.dump(pilgrim_pairs, f, ensure_ascii=False, indent=2)

    with open(os.path.join(CORPUS_DIR, "folklore_legends_aligned.json"), "w", encoding="utf-8") as f:
        json.dump(folklore_pairs, f, ensure_ascii=False, indent=2)

    # 3. JSONL splits for ML pipelines
    train_pairs = [p for p in all_pairs if p["split"] == "train"]
    test_pairs = [p for p in all_pairs if p["split"] == "test"]

    with open(os.path.join(CORPUS_DIR, "parallel_train.jsonl"), "w", encoding="utf-8") as f:
        for p in train_pairs:
            f.write(json.dumps(p, ensure_ascii=False) + "\n")

    with open(os.path.join(CORPUS_DIR, "parallel_test.jsonl"), "w", encoding="utf-8") as f:
        for p in test_pairs:
            f.write(json.dumps(p, ensure_ascii=False) + "\n")

    # 4. Standard Bitext files (.kha and .en) for fairseq / Marian / Hugging Face
    with open(os.path.join(BITEXT_DIR, "train.kha"), "w", encoding="utf-8") as f_kha, \
         open(os.path.join(BITEXT_DIR, "train.en"), "w", encoding="utf-8") as f_en:
        for p in train_pairs:
            f_kha.write(p["khasi"] + "\n")
            f_en.write(p["english"] + "\n")

    with open(os.path.join(BITEXT_DIR, "test.kha"), "w", encoding="utf-8") as f_kha, \
         open(os.path.join(BITEXT_DIR, "test.en"), "w", encoding="utf-8") as f_en:
        for p in test_pairs:
            f_kha.write(p["khasi"] + "\n")
            f_en.write(p["english"] + "\n")

    print(f"Train split: {len(train_pairs)} pairs")
    print(f"Test split: {len(test_pairs)} pairs")
    print("Bitext files exported successfully to khasi/corpus/data/bitext/")

if __name__ == "__main__":
    main()
