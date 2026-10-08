# -*- coding: utf-8 -*-
"""
Build Khasi Folklore & Mythology Datasets for khasi.culture.folklore.
Compiles 12 foundational Khasi oral folktales, origin myths, and legends
with full Khasi narratives, English translations, cultural analysis, and vocabulary.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FOLKLORE_DATA_DIR = ROOT / "khasi" / "culture" / "data" / "folklore"
FOLKLORE_DATA_DIR.mkdir(parents=True, exist_ok=True)

STORIES_DATA = [
    {
        "id": "ka_jingkieng_ksier",
        "title": "Ka Jingkieng Ksier (The Golden Ladder & Genesis of the Seven Huts)",
        "khasi_title": "Ka Jingkieng Ksier bad Ka Thymmei U Hynniewtrep",
        "category": "Creation Myth & Cosmology",
        "geographic_origin": "Lum Sohpetbneng (Ri-Bhoi / Khasi Hills)",
        "characters": ["U Blei Nongbuh Nongthaw (The Creator)", "Ki Khadhynriew Trep (The Sixteen Huts)", "Ki Hynniewtrep (The Seven Huts)"],
        "cultural_moral": "Humility, divine covenant of righteousness (Ka Hok), and humanity's sacred responsibility as stewards of Mother Earth (Ka Meiramew).",
        "khasi_text": """Ha kaba nyngkong eh, haba ka pyrthei ka dang lung bad dang khuid, U Blei Nongbuh Nongthaw U la thaw ia ki Khadhynriew Trep Khadhynriew Skum ha bneng. Ki Khadhynriew Trep ki la shong suk shong sain ryngkat bad U Blei ha ka bneng ba phyrnai, ha kaba ym don jingiap, ym don jingshitom, bad ym don ka pop ne ka jingbymman.

Hynrei U Blei ha ka jingstad bad jingieit bakhraw jong U, U la thaw ia ka pyrthei da ki lum babha, ki wah ba tuid kynjai, ki khlaw ba jyrngam, bad ki mrad ki mreng ba bun jait. Ban pyniasoh ia ka bneng bad ka pyrthei, U Blei U la buh ia Ka Jingkieng Ksier (The Golden Ladder) ha kliar jong U Lum Sohpetbneng. Lum Sohpetbneng u long u sohpet jong ka pyrthei, ka jaka kaba iasoh beit thik bad ka ryngkat jong U Blei Nongthaw.

Ha man la ka sngi, ki khadhynriew tylli ki ïing ki trep ki ju hiar lyngba kane ka Jingkieng Ksier ban wan sha ka pyrthei. Ki wan pule, wan shang, wan lum soh, bad wan sarang ia ki syntiew bad ki mrad. Te haba la jan miet, ki kiew pat sha bneng ban ioh thiah ha ka jaka kyntang ryngkat bad U Kynrad.

Hynrei la poi ka sngi ba U Blei U la kylli ia ki, la mano ba kwah ban shong sah noh ha pyrthei ban ri bad ban sumar ia ka mariang, ban pynroi ia ka jaidbynriew, bad ban rep ban riang ha kane ka Ri baieit. Hynniew ngut ki kynhun trep ki la aiti ialade da ka mon sngewbha ban hiar bad ban shong sah ha ka pyrthei. Kine ki hynniew tylli ki ïing ki la long Ki Hynniewtrep Hynniewskum. Ki Khyndai trep pat ki la shong sah ha bneng, kiba ngi khot Ki Khyndaittrep.

Hadien katto katne por, ki briew ha pyrthei ki la nang roi. Hynrei ka pop bad ka jingkhwan mynsiem ka la rung ha ka pyrthei lyngba ka jingpynkhein ia ka hok. Ka don kawei ka parom ba u briew u la kiew sha Lum Diengiei bad u la thaw ia ka pop kaba khraw, kaba la pynlong ia ka Jingkieng Ksier ban dkut noh. Naduh kata ka sngi, Ki Hynniewtrep ki la sah marwei ha ka pyrthei, bad ka lynti ban kiew sha bneng ka la khang noh. Hynrei U Blei U la ai ha ki ia Ka Niam Ka Rukom, ia Ka Hok bad Ka Sot, ia Ka Khan-Pylleng bad Ka Duwai Ka Phirat, khnang ba kin ioh pyniasoh pat ia la ka mynsiem bad U Blei Trai Kynrad haduh ba kin da poi pat sha ka Dwar jong U ha kaba khatduh.""",
        "english_translation": """In the primeval beginning, when the world was young and immaculate, God the Architect and Creator (U Blei Nongbuh Nongthaw) created the Sixteen Celestial Huts (Khadhynriew Trep) in heaven. They lived in unbroken bliss and fellowship with the Divine in the radiant realm where sorrow, death, and transgression did not exist.

In His infinite wisdom and love, the Creator fashioned the terrestrial world with undulating emerald hills, crystal mountain streams, deep virgin forests, and multifaceted flora and fauna. To unite heaven and earth, God set a magnificent Golden Ladder (Ka Jingkieng Ksier) upon the sacred peak of Lum Sohpetbneng ('The Navel of Heaven'). Lum Sohpetbneng was revered as the spiritual umbilical cord linking humanity to their Maker.

Every day, the sixteen families descended down this Golden Ladder to cultivate the earth, marvel at flowers and beasts, and rejoice in nature. When twilight fell, they ascended back to the celestial abode to rest in the presence of God.

Eventually, the Creator inquired among them who would volunteer to dwell permanently upon the earth to tend the soil, nurture the ecosystems, and establish human lineages. Seven celestial families stepped forward willingly to inhabit the mountains, becoming 'Ki Hynniewtrep' (The Seven Huts), while the remaining Nine Families stayed in heaven ('Ki Khyndaittrep').

Centuries passed, and humanity prospered. But when moral corruption and selfishness breached the sacred covenant of righteousness (Ka Hok), the Golden Ladder was severed. Cut off from direct celestial ascent, the Seven Huts remained on earth. Yet God in His mercy bequeathed them the Sacred Covenant (Ka Niam Ka Rukom), the moral law of righteousness, and divination rites (Ka Khan-Pylleng), assuring that every righteous soul shall return to the Golden Threshold of God when mortal life concludes.""",
        "sections": [
            {"title": "The Golden Age & Sixteen Families", "paragraph": 1},
            {"title": "The Golden Ladder of Lum Sohpetbneng", "paragraph": 2},
            {"title": "The Descent of the Seven Huts", "paragraph": 3},
            {"title": "The Severing and the Covenant of Hok", "paragraph": 4}
        ],
        "vocabulary": {
            "khadhynriewtrep": "sixteen celestial clans in Khasi cosmogony",
            "hynniewtrep": "the seven original terrestrial Khasi families",
            "khyndaittrep": "the nine celestial clans remaining in heaven",
            "jingkieng_ksier": "golden ladder or celestial bridge",
            "sohpetbneng": "navel of heaven (the sacred mountain in Ri-Bhoi)",
            "nongbuh_nongthaw": "the Supreme Architect and Creator God"
        }
    },
    {
        "id": "u_diengiei",
        "title": "U Diengiei (The Tree of Eclipsing Darkness)",
        "khasi_title": "U Diengiei bad Ka Jingkha jong Ka Jingshai",
        "category": "Cosmological Legend & Allegory",
        "geographic_origin": "Lum Diengiei (East Khasi Hills)",
        "characters": ["U Diengiei (The Giant Tree)", "U Khla (The Tiger Spirit)", "U Sim Phreit (The Wren / Little Bird)", "Ki Hynniewtrep (Khasi Elders)"],
        "cultural_moral": "Perils of hubris and greed, the environmental triumph of collective cooperation, and the wisdom of the humble over brute force.",
        "khasi_text": """Mynshuwa ha ki por barim bajah, hadien ba Ki Hynniewtrep ki la shong ha kane ka pyrthei, la mih uwei u dieng uba phylla bad uba khraw shibun eh ha kliar jong u Lum Diengiei. Une u dieng u la san ha ka rukom kaba ma bad kaba shyrkhei katta katta. Man la ka sngi u nang heh, u nang jrong, bad ki tnat jong u ki la nang pyniar shaduh ba ki la tap lut ia ka bneng baroh kawei.

Khum ka por ba une u Diengiei u la nang heh, ki sla jong u ki la pynduh lut ia ka jingshai jong ka sngi. Ka pyrthei baroh ka la dum tliw-tliw. Ym don shuh ka sngi, ym don shuh u bnai, bad ki briew ki la im ha ka jingjynjar bad ka jingtieng. Ki jingthung jingtep ki la iap tyrkhong, ki wah ki la dait thah, bad ki mrad ki la lynniar ha ka khlaw. Ki briew ki la shepting ioh ba une u dieng un pynjot lut ia ka pyrthei baroh.

Te ki Hynniewtrep ki la lum ia ka Dorbar Bah ha kliar lum. Ha kane ka Dorbar, baroh ki khun ki hajar ki la rai kut ban pom bad ban pynkyllon noh ia une u Diengiei ban ioh pat ia ka sngi bad ka jingshai. Ki la shim la ki sdie, ki wait, ki kurat, bad ki la leit sha lum ban pom ia u.

Ki la pom baroh shi sngi naduh step haduh janmiet. Ka snep bad ka doh jong une u dieng ka la nang rit bad nang duna. Hynrei haba la jan miet, namar ba la thait palat, ki la iehnoh ia ka kam bad ki la leit phai sha ki ïing jong ki ban shongthait, da kaba thmu ban wan pom pat ha ka step kaba bud.

Hynrei haba ki la wan ha ka step, ki la lyngngoh khraw ban iohi ba u Diengiei u la koit pat kumba u long mynshuwa! Baroh ki jingpom bad ki dak sdie ki la dam lut, bad ka snep ka la biang pat paka. Ki la pyrshang pom biang baroh shi sngi, hynrei ha ka step kaba bud u koit biang kumjuh. Kine ki jingpom ki la neh da ki taiew bad ki bnai, hynrei man la ka miet u diengiei u koit pat kumba ju long.

Ha kaba khatduh, uwei u sim rit (U Phreit) u la wan sha ki briew bad u la ong: "Ko ki briew, phi pom thala baroh shi sngi! Ha ka miet haba phi la leit phai, U Khla u ju wan bad u jliah ia ki dak sdie jong une u dieng da u thylliej jong u, bad ka jingspait ka dieng ka pynkoit pat ia u!"

Ki briew ki la kylli ia u sim: "Kumno ngin leh ban jop ia une u ksuid?" U Sim Phreit u la btai: "Haba phi pom ia u dieng, buh ia ki waitlieh bad ki sdie ba nep da ki khmut kiba shong sha kynjang ha ka khap ba phi pom, khnang ba haba u khla un wan jliah, u thylliej jong u un thaba bad un thlieh noh."

Ki briew ki la bud ia kane ka buit. Haba u khla u la wan ha ka miet ban jliah ia u dieng, u la thlieh u thylliej da ki wait ba nep bad u la phet kynsan da ka jinglynniar sha khlaw. Ha ka step kaba bud, ki briew ki la shem ba u diengiei um shym la koit shuh. Ki la pom bad ki la pynkyllon noh ia u da ka jingkmen bakhraw. Ka sngi ka la shai biang halor ka Ri Hynniewtrep, bad ka jingsuk ka la wan pat ha ka pyrthei.""",
        "english_translation": """Long ago, on the towering summit of Lum Diengiei, an unnatural and monstrous tree sprouted and expanded at a terrifying pace. Day by day, its gargantuan trunk thickened and its canopy spread until it eclipsed the sun and moon, plunging the world into total, freezing darkness.

In this perpetual night, vegetation withered, streams froze, and animals and humans cried out in despair. Fearing utter annihilation, the Khasi clans summoned a Great Council (Ka Dorbar Bah) and resolved to fell the colossal tree. Taking axes, adzes, and saws, they chopped into the trunk from dawn till dusk.

Yet every morning upon returning, they stood dumbfounded: the tree had miraculously healed overnight, its bark pristine and unscarred. Week after week the futile labor continued.

Finally, a tiny wren (U Sim Phreit) perched nearby and revealed the mystery: 'You labor in vain! Every night when you depart, the Tiger Spirit comes and licks the gashes with his magical tongue, healing the tree.' When the people asked for counsel, the little bird advised: 'Affix your sharpened axes and billhooks with their cutting edges outward within the cut trunk.'

The people followed the bird's advice. When the Tiger returned at midnight to lick the wound, the razor-sharp blades sliced his tongue, and he fled howling into the abyss. Deprived of the supernatural healing, the tree could not recover. The next day, with mighty strokes, the clans toppled the Diengiei. Sunlight burst forth across the Khasi hills, restoring warmth and life to the world.""",
        "sections": [
            {"title": "The Eclipse of the Diengiei", "paragraph": 1},
            {"title": "The Peril of Darkness", "paragraph": 2},
            {"title": "The Self-Healing Mystery", "paragraph": 4},
            {"title": "The Counsel of the Wren and the Slaying", "paragraph": 6}
        ],
        "vocabulary": {
            "diengiei": "the mythical monstrous tree on Lum Diengiei",
            "sim_phreit": "the little wren / munia bird whose wisdom saved humanity",
            "sdie": "indigenous iron woodsman axe",
            "waitlieh": "long-bladed dao / billhook used in hill forestry"
        }
    },
    {
        "id": "u_sier_lapalang",
        "title": "U Sier Lapalang (The Stately Stag and the Mother's Lament)",
        "khasi_title": "U Sier Lapalang bad Ka Jinglynniar jong Ka Kmie",
        "category": "Tragic Epic & Mother-Child Elegy",
        "geographic_origin": "Ri Thor (Surma Plains) to Lum Shillong (East Khasi Hills)",
        "characters": ["U Sier Lapalang (The Young Stag)", "Ka Kmie u Lapalang (The Mother Deer)", "Ki Nongshongshnong Khasi (The Hill Hunters)"],
        "cultural_moral": "Heed parental wisdom, beware the vanity of untested ambition, and honor maternal love which forms the basis of Khasi funeral dirges.",
        "khasi_text": """Ha ka them Ri Dkhar, ha ki madan ba shong phlang jyrngam ha them thor jong ka ri Surma, la shong uwei u sier babha briew bad ba donnam shibun, uba ki khot U Sier Lapalang. Une u sier u don ki reng kiba jrong kiba thaba kumba shna da ka rupa bad ka ksiar, bad ka rynieng jong u ka long kaba kynrei kaba itynnat katta katta.

U Sier Lapalang u shong ryngkat bad la ka kmie kaba ieit eh ia u. Ka kmie jong u ka ju sneng ju kraw man ka sngi: "Ko khun baieit jong nga, to shong khop ha kane ka ri them ri thor. Bam da u khah, bam da u nor, bam da u jangew jathang baroh shi lyiur baroh shi tlang. Wat ju kiew sha ki lum ba jrong jong ki Khasi, namar ha kato ka ri ki briew ki long kiba siah wait bad kiba tbit ban siat khnam da ki ryntieh ba khraw!"

Hynrei U Sier Lapalang um shym la sngap ia ka ktien ka kmie. Ka mynsiem samla jong u ka la thrang ban iohi ia ki lum ba jyrngam, ban mad ia u phlang ba thiang jong ki lum Khasi, bad ban dih ia ka um kshaid kaba pynkhriat ha ki thwei ba khuid. Te ha kawei ka sngi, khlem da iathuh ha la ka kmie, u la kiew sha ki lum ba heh jong ka Ri Khasi.

Haba u la poi ha ki lum ba jrong, u la kmen bad u la rynsied ha ki madan phlang. Hynrei ki nongshong shnong Khasi ki la iohi ia u. Mar kumta hi, la sawa ka pyrta shnong: "Kaw! Kaw! U sier uba heh reng u la wan ha ri jong ngi!" Ki samla shnong ki la shim la ki ryntieh, ki khnam ba la kyllan da ka bih, bad ki la beh pyrkhing ia u ryngkat ki ksew beh mrad.

U Sier Lapalang u la phet kynsan da ka jingtieng kaba khraw. U la phet lyngba ki lum, ki them, ki khlaw, bad ki thwei, hynrei ki Khasi ki la ker tawiar ia u na baroh ki liang. Ha kaba khatduh, ha kliar jong u Lum Shillong, uwei u khnam ba nep u la thaba beit ha ka dohnud jong u Lapalang. U Lapalang u la hap noh ha madan bad u la ktha la ka mynsiem.

Haba ka kmie jong u ka la sngew ba u khun um don shuh, ka la kiew da ka jingsngewsih bakhraw sha ki lum Khasi ban wad ia u. Haba ka la lap ia u ba u la thiah iap ha madan, ka dohnud jong ka ka la pait pnat. Ka la lynniar da ka jingsngewsih kaba jur katta katta shaduh ba ki maw ki dieng ki la sngewsynei bad ki khlieh lum ki la sawa mian-mian. Ka la rwai ia ka Sur Phawar ba sngewsih:

"Ko Lapalang phrang sngi jong nga,
Kum ba-tingshein u mankara!
Haba na nga me la khlad noh,
Dohnud sngewsih nga im suhsat!

Wow! La shet ka tieh pongdeng,
Ia ka rynieng u kynrem reng!
Wow! La kjit u nam sarang,
Ia ka mynsiem u Lapalang!

Nga ong ko khun ynnai leit kiew,
Sha ri Khasi sha ri ki briew!
Shong khop ha la ri them ri thor,
Bam da u khah bam da u nor!
Pynban kynrem na nga me khlad,
Marwei ha pyrthei nga jaw ummat!"

Kine ki jingrwai sngewsih jong ka kmie u Lapalang ki la shoh beit ha ki dohnud jong ki Khasi. Naduh kata ka sngi, haba don ba iap ha ka kur ka jait, ki Khasi ki ju rwai phawar kynud sngewsih ha ka rukom kaba syriem eh ia ka sur jong ka kmie u Sier Lapalang.""",
        "english_translation": """In the fertile grassy plains of the Surma valley lived a magnificent young stag named U Sier Lapalang, adorned with sweeping antlers that shimmered like gold and silver. He lived under the doting care of his mother, who constantly cautioned him: 'Stay contented, my beloved child, in our lowland plains. Feast on the sweet marsh reeds and tender shoots through summer and winter. Never ascend the high Khasi hills, for there dwell hunters deadly with the bow and arrow.'

Restless and fascinated by the blue misty mountains, Lapalang spurned his mother's warning and bounded up into the Khasi highlands. Seeing such an enormous and majestic trophy, village hunters sounded the hunting call: 'Kaw! Kaw!' Surrounding him with hounds and envenomed arrows, they hunted him relentlessly across ravines and crags until, on the summit of Lum Shillong, an arrow struck his heart.

Learning of her son's fate, the grief-stricken mother climbed the steep mountains. Finding his lifeless form stretched out on the cold stone, her heart shattered. Her mournful wailing and poetic elegy reverberated across every cliff, moving the hunters themselves to tears. That heartbroken lament became the archetype for traditional Khasi funeral laments and dirges (*Ki Kynud Sngewsih*) sung to this day.""",
        "sections": [
            {"title": "The Lowland Paradise & Maternal Counsel", "paragraph": 1},
            {"title": "The Disobedience and the Ascent", "paragraph": 3},
            {"title": "The Great Hunt on Lum Shillong", "paragraph": 4},
            {"title": "The Mother's Lament and Cultural Dirge", "paragraph": 6}
        ],
        "vocabulary": {
            "sier_lapalang": "the legendary stag of Khasi folklore",
            "reng": "antlers / horns",
            "ryntieh": "traditional Khasi bamboo recurve bow",
            "kynud_sngewsih": "funeral mourning dirge / rhythmic lamentation"
        }
    },
    {
        "id": "u_manik_raitong",
        "title": "U Manik Raitong (The Melodies of the Sharati & Tragic Love)",
        "khasi_title": "U Manik Raitong bad Ka Sharati ba Sngewsih",
        "category": "Romantic Tragedy & Musical Origin",
        "geographic_origin": "Hima Sohra / Khasi Chieftaincy",
        "characters": ["U Manik Raitong (The Wretched Orphan Musician)", "Ka Lieng Makaw (The Queen / Mahadei)", "U Syiem (The King)"],
        "cultural_moral": "The transcendent purity of artistic devotion and true love over caste, poverty, and sovereign decree.",
        "khasi_text": """Mynbarim ha ka Hima jong U Syiem, la don uwei u samla uba duk ba kyrduh tam ha ka shnong, uba kyrteng U Manik. U la duh noh ia la ki kmie ki kpa, ki hynmen ki para, baroh ki la iap noh ha ka khlam bakhraw. Um don ïing um don sem, um don kur um don kha. U shong tang ha kawei ka jingshai ba rit ha khap shnong, u phong da ki jainjot, bad u ju sleh ialade da ka dpei khnang ba ki briew kin kyntait bad kin kiar na u. Namar kata, baroh ki briew ki la khot ia u "U Manik Raitong" (Manik the Wretched Orphan).

Hynrei U Manik u don kawei ka sap kaba kyntang kaba U Blei U la pynkup ha u: ka sap ban tem ia ka Sharati (the bamboo flute). Ha ka miet haba baroh ka shnong ka la thiah jar-jar, Manik u ju sei ia la ka sharati bad u tem ia ki sur kiba thiang bad ba sngewsih katta katta. Kine ki sur ki sawa lyngba ki khlaw, ki pynkhih ia ki sla dieng, bad ki rung shaduh ki syngkhoin jong ka dohnud briew.

Ha kato ka por, U Syiem jong ka Hima u la leit jingleit jngai sha kiwei pat ki Ri bad u la sah da ki bnai ki bnai. Ka Mahadei (The Queen), kaba kyrteng Ka Lieng Makaw, ka ju shong marwei ha iing-sad. Man la ka miet haba ka sngap ia ka sur sharati u Manik Raitong, ka dohnud jong ka ka la kiew kynsan da ka jingieit bad jingkwah ban tip mano ba tem ia kine ki sur ba phylla.

Ha kawei ka miet, ka Lieng Makaw ka la bud mian-mian ia ka sur sharati shaduh ka tnum jong u Manik. Haba ka la iohi ia u Manik, la u don ha ka dpei bad jainjot, ka mynsiem jong ka ka la shah ring beit ha ka sap bad ka jingbha-briew kaba rieh ha pyrthei. Ka la rung shapoh bad ki la iasoh jingieit ha kata ka miet.

Hadien katto katne por, ka Mahadei ka la kha ia uwei u khun shynrang babha briew. Hynrei U Syiem um pat shym la wan phai na jingleit. Haba U Syiem u la wan phai, u la sngewbha khraw ban iohi ia u khunlung, hynrei u la kylli da ka jingshyrkhei: "Mano u kpa jong une u khunlung?" Ka Mahadei kam shym la kubur bad kam treh ban iathuh satlak.

U Syiem u la lum ia ka Dorbar Bah jong ka Hima baroh kawei. U la btai ba baroh ki shynrang jong ka hima kin wan ha madan bad kin rah uwei u kpu uba la kyllan da ka ngap. Uta uba u khunlung un leit kdup bad shim ia u kpu, uta un long u kpa ba shisha. Baroh ki myntri, ki riewbha, ki tymmen ki samla ki la wan ialam kpu, hynrei u khunlung um shym la leit sha no sha no ruh.

Ha kaba khatduh, ki la ong ba dang sah sa tang uwei u briew uba duk tam—U Manik Raitong. Ki la phah khot ia u Manik. Haba u Manik u la wan rung ha madan da ki jainjot bad ka dpei, u khunlung u la rynsied kynsan na ka kti ka kmie bad u la leit kdup ia u Manik da ka jingkmen.

Ka Dorbar bad U Syiem ki la pynrem ia u Manik ban iap ha ka ding. Hynrei u Manik u la kyntait ban phet krad; u la pan bor tang ban pynkhreh ialade ia ka kynthei ding (the funeral pyre) bad ban shah pyndep ia ka hok. Haba ka ding ka la meh ba heh, u Manik u la sei ia la ka Sharati bad u la tem ia ka sur kaba sngewsih tam kaba pyrthei kam pat ju sngew. Hadien ba u la kut ka jingtem, u la kiew kynsan shapoh ka ding kaba meh.

Ha kata ka khyllipmat hi, ka Lieng Makaw, kaba la iohi ia ka jingiap u samla ba ka ieit, kam shym la lah shuh ban neh. Ka la phet kynsan lyngba ka paitbah bad ka la rynsied noh shapoh ka ding ryngkat bad u Manik. Naduh kata ka sngi, ka parom u Manik Raitong bad ka Sharati ka la sah kum ka dak jong ka jingieit bakhraw kaba palat ia ka spah bad ka nam pyrthei.""",
        "english_translation": """Long ago lived Manik, an orphan who lost his entire clan to pestilence. Destitute and clad in tattered rags and ashes to repel society, he was called 'Manik Raitong' (The Wretched). Yet God had endowed him with peerless musical genius: at midnight, when the village slumbered, Manik played his bamboo flute (Ka Sharati), pouring out melodies of sublime pathos that enchanted the forest.

While the King was absent on long state journeys, Queen Lieng Makaw listened night after night to the haunting notes. Drawn irresistibly to his humble hut, she fell in love with the pure soul behind the ashes.

When a son was born in the King's absence, the returned monarch assembled the Great Parliament. To determine paternity, every man offered the infant a honeyed rice cake. The child ignored all nobles, ministers, and warriors until the ash-smeared Manik was brought forward, whereupon the infant leapt with joy into his arms.

Condemned to the funeral pyre for high treason, Manik refused flight, asking only to light his own pyre. As the flames soared, he played his Sharati one final time with transcendent devotion, drove the flute upside down into the earth, and stepped into the inferno. In that instant, Queen Lieng Makaw broke through the throng and cast herself into the flames beside him, sealing their eternal union in folklore.""",
        "sections": [
            {"title": "The Solitary Flutist in Rags", "paragraph": 1},
            {"title": "The Queen and the Midnight Melody", "paragraph": 3},
            {"title": "The Honey Cake Trial", "paragraph": 6},
            {"title": "The Final Song on the Pyre", "paragraph": 8}
        ],
        "vocabulary": {
            "raitong": "destitute, wretched orphan without family",
            "sharati": "traditional Khasi bamboo flute played at funerals and ceremonies",
            "mahadei": "queen consort of a Khasi Syiem",
            "iing_sad": "royal ceremonial court of the Syiem"
        }
    },
    {
        "id": "ka_nohkalikai",
        "title": "Ka Nohkalikai (The Leap of Likai & Waterfall of Tears)",
        "khasi_title": "Ka Parom jong Ka Nohkalikai",
        "category": "Historical Folktale & Toponymic Legend",
        "geographic_origin": "Rangjyrteh / Sohra (Cherrapunji)",
        "characters": ["Ka Likai (The Hardworking Mother)", "U Tnga ba-ar (The Jealous Stepfather)", "Ka Khunlung (The Innocent Infant)"],
        "cultural_moral": "Warning against malice, cruelty, and domestic jealousy, while honoring maternal sacrifice.",
        "khasi_text": """Ha ka shnong Rangjyrteh, kaba don ha ki thain Sohra, la shong mynshuwa kawei ka samla kaba kyrteng Ka Likai. Ka Likai ka don uwei u tnga uba ieit eh ia ka, bad ki la ioh ia kawei ka khun kynthei kaba itynnat kaba long ka jingkmen jong ka ïing baroh kawei. Hynrei ka bok kam shym la neh slem; u tnga jong ka u la iap noh kynsan, bad Ka Likai ka la sah marwei kum ka riew-kynthei khun-swet.

Ban bsa bad pynheh ia la ka khun baieit, Ka Likai ka la trei shitom jur. Ka leit kit nar, kit mar, bad trei bylla man la ka sngi na shnong sha shnong. Namar ba ka marwei, ki paralok bad ki kur ki la kyrpad ia ka ban shongkurim biang khnang ba un don u kpa ban sumar bad ban ri ia ka khunlung haba ka leit trei bylla. Te Ka Likai ka la shongkurim bad uwei pat u shynrang.

Hynrei une u tnga ba-ar um shym la long u briew ba bha. U don ka dohnud kaba bishni bad kaba sniew katta katta. Man la ka sngi haba Ka Likai ka wan phai na ka kam, ka ju kdup, ju ñiad, bad ju pynleit jingmut lut tang ia la ka khunlung, khlem da khein briew shuh ia u tnga. Une u shynrang u la nang khwan bad nang thut ka mynsiem man ka sngi.

Ha kawei ka sngi haba Ka Likai ka la leit trei jngai, une u shynrang u la shong marwei ha ïing. Ka jingbishni ka la shoh jur ha ka dohnud jong u shaduh ba u la shim ia ka wait bad u la pyniap noh ia kata ka khunlung kaba lui-lui. Nangta u la shet ia ka doh jong ka khunlung ha u khiew ranei, hynrei ia ki shymprih-kti jong ka u la leit buh rieh ha ka shang kwai.

Haba Ka Likai ka la wan phai da ka jingthait bad jingthngan bakhraw, kam shym la iohi ia la ka khun. U tnga u la ong ba ka khun ka la leit shang sha ki paralok, bad u la ai ja ai doh ia ka ban bam. Ka Likai kaba la thngan jur ka la bam sngewbha khlem da tip eiei.

Hadien ba ka la dep bam, ka la kiew ban shim kwai na ka shang ban bam kynroi kumba ju long ka rukom Khasi. Haba ka la plied ia ka shang kwai, ka la lap ia ki shymprih-kti jong la ka khunlung ba ka ieit! Mar kumta hi, ka la sngewthuh ia ka jingshisha kaba shyrkhei: ba ka la bam thiah ia ka doh jong la ka khun baieit da ki kti jong ka!

Ka jingmut jingpyrkhat jong Ka Likai ka la lamwir kynsan da ka jingsngewsih bad jingshykhei. Ka la shim ia ka waitlam ha la ka kti, ka la pyrta lynniar da ka jinglynniar kaba shyrkhei, bad ka la phet kynsan lyngba ka khlaw shaduh ka khmat riat kaba jrong tam ha Rangjyrteh. Ki briew ki la pyrshang ban khang ia ka, hynrei kam sngap shuh; ka la rynsied noh kynsan shapoh ka thwei ba jylliew jong ka kshaid. Naduh kata ka sngi, ia kata ka kshaid ba jrong bad ba itynnat la khot noh "Ka Kshaid Nohkalikai" (The Leap of Ka Likai).""",
        "english_translation": """In the ancient village of Rangjyrteh near Sohra lived a young widow named Ka Likai with her infant daughter. Carrying heavy loads of iron ore between villages as a porter, she labored tirelessly to provide for her child. Pressured to remarry so someone would watch the child while she worked, she wed a second husband.

Consuming jealousy poisoned the stepfather's heart, resentful of the devotion Likai poured into the child. One afternoon while Likai was hauling goods afar, the man murdered the child in a fit of rage, cooked the meat, and concealed the severed fingers in the betel-nut basket.

Returning famished, Likai ate the prepared stew gratefully. When she reached for betel nut (*kwai*) after her meal, she uncovered the tiny severed fingers. The catastrophic horror drove her to instant madness. Brandishing a billhook, she sprinted through the village to the brink of the towering precipice and leapt into the abyss. Today, the majestic waterfall bears her name: Nohkalikai ('The Leap of Likai').""",
        "sections": [
            {"title": "The Devoted Widow of Rangjyrteh", "paragraph": 1},
            {"title": "The Stepfather's Dark Jealousy", "paragraph": 3},
            {"title": "The Horrific Discovery in the Kwai Basket", "paragraph": 6},
            {"title": "The Plunge into the Abyss", "paragraph": 7}
        ],
        "vocabulary": {
            "nohkalikai": "the leap of Likai (tallest plunge waterfall in India)",
            "shang_kwai": "woven bamboo basket for betel nut and lime",
            "riat": "sheer mountain cliff / precipice",
            "waitlam": "Khasi ceremonial double-edged sword / billhook"
        }
    },
    {
        "id": "u_bsein_thlen",
        "title": "U Bsein Thlen (The Monster Serpent and the Slaying at Dainthlen)",
        "khasi_title": "U Bsein Thlen bad Ka Jingjop ha Dainthlen",
        "category": "Heroic Myth & Cautionary Allegory",
        "geographic_origin": "Dainthlen / Sohra (Cherrapunji)",
        "characters": ["U Thlen (The Man-Eating Serpent Demon)", "U Suidnoh (The Heroic Hunter)", "Ki Nongshongshnong (The Khasi Clan Assembly)"],
        "cultural_moral": "Denunciation of illicit greed, human exploitation, and sacrificial cults, honoring courage and community vigilance.",
        "khasi_text": """Ha ki por hyndai, ha kawei ka krem ba shyrkhei kaba don ha Sohra hajan ka wah kaba tuid sha them Surma, la shong uwei u bsein uba khraw bad uba ma katta katta uba ki khot U Thlen. Une u Thlen um dei u bsein uba kum kiwei pat; u dei u ksuid uba bam briew bad uba pynlong ia ka jingshyrkhei ha ka Ri Khasi baroh kawei.

Ka rukom jong une u Thlen ka long ba haba ki briew ki iaid ha ka lynti ba marjan bad ka krem jong u, lada ki iaid arngut, un bam nguid noh ia uwei; lada ki iaid saw ngut, un bam ia ki arngut. Da kumta, ki briew ki la tieng lut ban iaid lyngba kata ka jaka, bad ka shnong ka la duh noh ia ki briew kiba bun. Nalor kata, u Thlen u ju ai spah pynsuk ia kito ki briew kiba man-bieit bad kiba kñia snam briew sha u, kiba ki khot Ki Nongshohnoh.

Haba ka jingshitom ka la jur palat, uwei u riewshlur uba kyrteng U Suidnoh u la thaw ka buit ban pynduh jait ia une u ksuid. U Suidnoh u la leit shajan ka krem u Thlen man la ka sngi bad u la rah ia ka doh blang ban bsa ia u. Man ba u pyrta, u Thlen u ju sei la ka khlieh na ka krem bad u plied la ka shyntur kaba heh, bad U Suidnoh u ju kyntait shapoh ka doh blang. Ha kane ka rukom, u Thlen u la nang shaniah jur ha U Suidnoh.

Haba u la iohi ba u Thlen u la shaniah pura, U Suidnoh u la pynkhreh ia ka buit kaba khatduh. U la shna kawei ka nar ba heh bad u la thang ia ka ha ka dpei ding haduh ba kata ka nar ka la saw hek-hek da ka jingshit bakhraw. Nangta u la shim ia ka nar da ki khnap-nar ba khlain, u la leit sha ka krem u Thlen, bad u la pyrta kumba ju leh.

U Thlen u la pynpaw la ka khlieh bad u la ang la ka shyntur ban pdiang ia ka doh. Hynrei ha ka jaka ka doh blang, U Suidnoh u la theh beit ia kata ka nar ba saw hek-hek shapoh u pdot jong u Thlen! Ka ding ka la bam ia ki snier jong u, u Thlen u la lynniar da ka bor bakhraw, u la kyrsum ha madan bad u la pait ka mynsiem.

Ki Khasi ki la leit tan ia une u bsein na ka krem sha madan hajan ka kshaid. Ha kata ka jaka, ki la dain pynpait ia ka doh jong u ha ki maw kiba heh khnang ban ym pynmih shuh ia ka bih. Ia kata ka jaka la khot mynta Ka Kshaid Dainthlen (The Slaying of the Thlen), bad ki dak jong ki maw ba la dain ia u Thlen ki dang paw haduh kine ki sngi.""",
        "english_translation": """In ancient times, a terrifying serpent demon called U Thlen dwelt within a cavern beside the Sohra gorge, terrorizing the countryside. Whenever travelers traversed the road, the Thlen would devour half of their party, demanding blood and fear. Moreover, superstitious persons seeking ill-gotten wealth began making covert pacts with the demon, giving rise to the feared 'Nongshohnoh' human-sacrificers.

A valiant man named U Suidnoh resolved to deliver his people from this evil. Visiting the cave daily, he fed the serpent roasted goat meat, conditioning the beast to open its vast maw upon hearing his call.

When the serpent trusted him fully, Suidnoh heated a heavy iron ingot in a furnace until it burned incandescent red. Carrying the glowing iron with blacksmith tongs, he called the Thlen. As the demon opened its jaws in anticipation, Suidnoh plunged the molten iron into its throat. Howling in agony, the demon convulsed and perished.

The clans dragged the carcass onto the flat riverbed rock and chopped its body to pieces to extinguish the curse forever. The place was named Dainthlen ('Where the Thlen was Cleaved'), where the natural chiselled furrows in the riverbed rocks remain as the legendary marks of the serpent's destruction.""",
        "sections": [
            {"title": "The Reign of the Serpent Demon", "paragraph": 1},
            {"title": "The Cult of Illicit Wealth", "paragraph": 2},
            {"title": "Suidnoh's Red-Hot Ingot Trap", "paragraph": 4},
            {"title": "The Cleaving at Dainthlen", "paragraph": 6}
        ],
        "vocabulary": {
            "thlen": "mythical serpentine evil spirit associated with ill-gotten wealth",
            "dainthlen": "where the Thlen was cut / sliced (famous waterfall)",
            "nongshohnoh": "hired assailant in Thlen folklore folklore",
            "suidnoh": "the hero of the Thlen slaying legend"
        }
    },
    {
        "id": "ka_sngi_bad_u_bnai",
        "title": "Ka Sngi bad U Bnai (The Sun, the Moon & the Ash of Shame)",
        "khasi_title": "Ka Sngi bad U Bnai ha Ka Pyrthei Barim",
        "category": "Astronomy & Kinship Morality Myth",
        "geographic_origin": "Khasi Celestial Lore",
        "characters": ["Ka Sngi (The Sun - Sister)", "U Bnai (The Moon - Brother)", "Ki Khlur (The Stars)"],
        "cultural_moral": "Strict enforcement of clan exogamy (Tip-Kur Tip-Kha) and prohibition against incestuous transgressions (Ka Sang Ka Ma).",
        "khasi_text": """Ha ki por hyndai haba ka bneng ka dang jan bad ka pyrthei, Ka Sngi bad U Bnai ki dei shipara kiba shong ryngkat ha ka ryngkat bneng. Ka Sngi ka dei ka hynmen kynthei kaba bha briew, kaba shai bad kaba phyrnai kumba shna da ka ksiar kaba thiang. U Bnai pat u dei u para shynrang uba don ka rynieng kaba itynnat bad ka khmat kaba pyngngad.

Hynrei U Bnai u la nang pynleit jingmut sniew ha la ka dohnud. U la klet noh ia ka niam kur niam kha bad u la klet ba Ka Sngi ka dei ka hynmen kynthei jong u hi. Ka jingkwah sniew ka la pynduh ia ka jingmut jingpyrkhat jong u haduh ba ha kawei ka sngi, u la pyrshang ban kdup bad ban leh thurmur ia la ka hynmen.

Ka Sngi ka la bitar jur katta katta halor kane ka jingpynkhein niam bakhraw (Ka Sang). Ka la kyntait kynsan ia u, ka la kura da ka kti ia ka dpei ding kaba meh ha dpei, bad ka la theh beit ia kata ka dpei kaba saw sha ka khmat jong U Bnai!

Kata ka dpei ka la thang bad ka la pynsaw ia ka khmat jong U Bnai, bad ki dak dpei ki la sah ha ka khmat jong u haduh mynta. U Bnai u la sngewlehrain jur katta katta halor la ka pop. Um nud shuh ban paw ha ka por sngi haba Ka Sngi ka shai phyrnai. Naduh kata ka por, U Bnai u shong sah tang ha ka miet haba ka pyrthei ka dum, bad ki dak dpei ki dang paw ha ka khmat jong u kum ka dak jong ka jingbymman kaba u la leh.""",
        "english_translation": """In ancient cosmology, the Sun (Ka Sngi, feminine) and the Moon (U Bnai, masculine) were sister and brother dwelling in the celestial court. Ka Sngi shone with golden warmth and righteousness, while U Bnai possessed cool, silvery poise.

Overcome by forbidden passion, U Bnai forgot the sacred taboo of clan incest (Ka Sang) and improperly propositioned his sister. Outraged by this heinous violation of moral law, Ka Sngi scooped up a handful of burning hearth ash (dpei) from the fire and hurled it across her brother's face.

The smouldering ash scarred his countenance forever. Overwhelmed by shame and dishonor, U Bnai fled and never dared show his face during the brilliant daylight when his sister rides the heavens. To this day, the Moon emerges only in darkness, bearing dark ash patches across his pale face as an eternal badge of shame and a warning against incest.""",
        "sections": [
            {"title": "The Celestial Brother and Sister", "paragraph": 1},
            {"title": "The Breach of Clan Taboo (Ka Sang)", "paragraph": 2},
            {"title": "The Hearth Ash of Wrath", "paragraph": 3},
            {"title": "The Eternal Night Exile", "paragraph": 4}
        ],
        "vocabulary": {
            "ka_sngi": "the Sun (feminine in Khasi culture)",
            "u_bnai": "the Moon (masculine in Khasi culture)",
            "dpei": "the traditional hearth / cooking fireplace",
            "ka_sang": "sacrilegious taboo / incest / unpardonable sin"
        }
    },
    {
        "id": "u_klew_bad_ka_sngi",
        "title": "U Klew bad Ka Sngi (The Peacock's Love for the Sun)",
        "khasi_title": "U Klew bad Ka Sngi ha Ki Kper Bneng",
        "category": "Romance & Natural Folktale",
        "geographic_origin": "Ri Khasi Valleys",
        "characters": ["U Klew (The Peacock)", "Ka Sngi (The Sun Deity)"],
        "cultural_moral": "Unconditional devotion, unrequited spiritual yearning, and how pure love beautifies the soul.",
        "khasi_text": """Mynbarim eh, U Klew um shym la don ki sner kiba phyrnai kumba u don mynta. U dei tang u sim uba lieh lum uba shong ha ki khlaw ba jyrngam. Hynrei U Klew u don ka mynsiem kaba ieit jur ia Ka Sngi bakhraw kaba pynshai ia ka bneng. Man la ka step haba Ka Sngi ka kiew na Mihsngi, U Klew u ju ieng ha kliar lum bad u peit seh sha ka da ka jingthrang bakhraw.

U Klew u ju shad, ju rynsied, bad ju pynieng ia la ki sner baroh ban pynkmen ia Ka Sngi. Ka jingieit jong u ka long kaba khuid bad kaba shida katta katta. Hynrei Ka Sngi ka long kaba jngai palat ha bneng, bad um lah ban poi sha ka.

Haba Ka Sngi ka la iohi ia kane ka jingieit ba shisha bad ka jingshad ba phyrnai jong U Klew man la ka sngi, ka dohnud jong ka ka la sngewsynei bad ka la pdiang ia ka mynsiem jong u. Ban pyndonburom ia une u sim baieit, Ka Sngi ka la phah ia ki kjat-sngi ba phyrnai jong ka, bad ka la tah ia ki khmat sngi ba ksiar bad ba rupa ha man la ka sner jong U Klew.

Naduh kata ka sngi, U Klew u la kylla long u sim uba itynnat tam ha ka pyrthei. Man ba ka sngi ka mih ne haba u iohi ia ka jingrang ha bneng, u pyniar ia la ki sner kiba don da ki hajar tylli ki khmat-sngi (ki 'mat-klew) ban shad phawar ia Ka Sngi kaba u ieit.""",
        "english_translation": """In ancient days, the peacock (U Klew) did not possess dazzling iridescent plumes, but was merely an ordinary woodland bird. Yet he possessed a deep, spiritual devotion to the Sun (Ka Sngi). Every morning at dawn, he ascended high ridges, gazing upward in adoration as she rose.

Spreading his humble feathers, the peacock danced tirelessly to celebrate her golden brilliance. Moved by his selfless and faithful love across the vast cosmic chasm, Ka Sngi bent her rays downward and kissed each of his feathers, stamping her own radiant golden eyes across his plumage (*ki 'mat-klew*).

From that hour forward, the peacock became the most magnificent bird of the mountains. Whenever the sun breaks through rain clouds, he fans out his resplendent emerald and golden train in dance, celebrating the divine lady of his heart.""",
        "sections": [
            {"title": "The Humble Woodland Bird", "paragraph": 1},
            {"title": "The Dance of Morning Adoration", "paragraph": 2},
            {"title": "The Sun's Golden Gift", "paragraph": 3}
        ],
        "vocabulary": {
            "klew": "peacock (symbol of pride, beauty, and devotion)",
            "mat_klew": "the iridescent 'eye' patterns on a peacock's train",
            "kjat_sngi": "sunbeams / rays of light"
        }
    },
    {
        "id": "ka_wah_umiam_bad_umngot",
        "title": "Ka Wah Umïam bad Ka Wah Umngot (The Twin Sister Rivers)",
        "khasi_title": "Ka Parom jong Ka Wah Umïam bad Ka Wah Umngot",
        "category": "Landscape Legend & River Lore",
        "geographic_origin": "Shillong Plateau to Dawki / Sylhet",
        "characters": ["Ka Umïam (The Elder Sister / Weeping Waters)", "Ka Umngot (The Younger Sister / Gentle Crystal Waters)"],
        "cultural_moral": "Patience and grace triumph over reckless haste and pride.",
        "khasi_text": """Mynbarim la don arngut ki samla kiba dei shipara, Ka Umïam bad Ka Umngot, kiba shong ha kliar jong ki lum Khasi. Baroh arngut ki long kiba itynnat bad kiba sngur ka mynsiem. Ha kawei ka sngi, ki la iakop ba kin phet-iaw na kliar lum shaduh ki madan ba shong phlang ha them thor jong ka ri Surma.

Ka Umïam, kaba dei ka hynmen, ka la sngewsarong bad ka la thmu ba kan jop suk ia ka para. Ka la phet kynsan da ka bor bad ka jingthok, ka khein pait ia ki lum, ka pait ia ki maw, bad ka shlei kynsan lyngba ki riat. Namar kata ka jingphet kynsan, ka la jah lynti bad ka la hap noh ha ki them ba jylliew, kaba la pynlong ia ka ban lynniar bad ban ïam sngewsih ha lynti. Ka um jong ka ka la kylla long kaba dum bad ba khluit, kaba pynmih ia ka kyrteng "Um-ïam" (Weeping Waters).

Ka Umngot pat, kaba dei ka para ba lui-lui, kam shym la leh sarong. Ka la tuid mian-mian da ka jingsngur, ka iaid lyngba ki mawsiang, ka shad kynjai ha ki kshaid, bad ka ri ia ka jingkhuid jong ka um kumba pynshai da ka kristal. Ka la poi suk bad sngur shaduh Dawki ha them Surma, kaba pynlong ia ka haduh mynta ban long ka wah kaba sngur tam ha ka pyrthei baroh kawei.""",
        "english_translation": """Two divine sisters, Ka Umïam and Ka Umngot, dwelt atop the high Khasi plateau. One sunny day, they engaged in a playful race to reach the vast Sylhet plains below.

Ka Umïam, the elder sister, confident in her strength, surged forward in reckless haste. She tore through granite crags and crashed down precipices, carving wild gorges. In her frantic rush, she lost her way, twisting back and weeping in frustration. Her waters became turbulent and laden with tears, giving her the name 'Um-ïam' (The Weeping River).

Ka Umngot, the modest younger sister, flowed gently, gracefully contouring around mountains, preserving her turquoise crystal clarity. She reached Dawki and the plains effortlessly, retaining her world-famous glass-like transparency to this day.""",
        "sections": [
            {"title": "The Divine Sister Rivers", "paragraph": 1},
            {"title": "The Frenzy and Tears of Umïam", "paragraph": 2},
            {"title": "The Grace and Clarity of Umngot", "paragraph": 3}
        ],
        "vocabulary": {
            "umiam": "weeping water / river of tears",
            "umngot": "clear, sparkling river (Dawki river)",
            "wah": "river / stream",
            "sngur": "crystal-clear, transparent, pure"
        }
    },
    {
        "id": "ka_krem_lamet_latang",
        "title": "Ka Krem Lamet Latang (The Great Council Cave of Animals)",
        "khasi_title": "Ka Dorbar Bah ha Krem Lamet Latang",
        "category": "Fauna Lore & Council Legend",
        "geographic_origin": "Krem Lamet Latang (Raid Nongkhlaw)",
        "characters": ["U Khla (The Tiger Chief)", "U Sier (The Deer)", "Ki Mrad ki Mreng (The Beasts of the Forest)"],
        "cultural_moral": "Democratic covenant, sanctity of contracts (Ka Jutang), and animal coexistence.",
        "khasi_text": """Ha ki por hyndai haba ki mrad ki dang nang ban kren kum ki briew, la don kawei ka dorbar kaba khraw tam ha ka pyrthei kaba ki khot Ka Dorbar Bah ha Krem Lamet Latang. Baroh ki jait mrad, ki sim, ki bsein, bad ki khniang ki la iawan lang ban iasoh ha kane ka krem ba heh ban pynbeit ia ka rukom im bad ka synshar khadar ha khlaw.

Ha kane ka Dorbar, man la u mrad u la ioh la ka burom bad la ka bynta. U Khla u la bat ia ka nam kum u kynrad khlaw, U Sier u la ioh ia ka jingkyrkhu ban mareh stet, bad ki sim ki la ioh ia ka bor ban her sha suin bad ban rwai phawar. Ki la kular ha khmat U Blei ba kin nym ia bam duh pynjot paralok khlem daw, bad ba kin sumar ia ka mariang.

Hynrei hadien ba u briew u la pynkhein ia ka hok ha pyrthei, ka jutang ha Krem Lamet Latang ka la kylla, bad ki mrad ki la duh noh ia ka ktien briew. Hynrei ki dak jong kata ka dorbar ki dang sah ha ka jingriew spah jong ka khlaw bad ka jingiadei hapdeng u briew bad ka mariang.""",
        "english_translation": """In the mythic age when beasts still spoke the language of mankind, the great parliament of all living creatures assembled at the legendary cavern of Krem Lamet Latang. All four-footed beasts, birds of the air, and creatures of the soil met to establish the Great Covenant of the forest.

In this divine assembly, each animal received its role: the Tiger was appointed guardian of the wild tracts, the Deer received agility and grace, and the Birds were given flight and melody. They swore a sacred oath before God to live in equilibrium and preserve the living world. When humanity later broke the covenant of righteousness (Ka Hok), the beasts lost the human tongue, yet the memory of that primal parliament remains embedded in Khasi ecological lore.""",
        "sections": [
            {"title": "The Primal Parliament of Beasts", "paragraph": 1},
            {"title": "The Covenant of Equilibrium", "paragraph": 2},
            {"title": "The Severed Tongue and Ecological Legacy", "paragraph": 3}
        ],
        "vocabulary": {
            "lamet_latang": "legendary council cave where animals held assembly",
            "jutang": "solemn covenant / sacred pact",
            "mrad": "animal / wild beast"
        }
    },
    {
        "id": "u_mawbynna_megaliths",
        "title": "Ki Mawbynna bad Ki Mawlynti (The Sacred Megalithic Stones & Ancestral Spirits)",
        "khasi_title": "Ki Mawbynna, Ki Maw Umkoi bad Ka Nam Kpa",
        "category": "Megalithic Ancestor Lore",
        "geographic_origin": "Nartiang / Sohra / Mawphlang",
        "characters": ["Ki Tymmen Mynbarim (The Ancestors)", "U Kni (The Maternal Uncle)", "Ka Kmie-Radha (The Great Mother)"],
        "cultural_moral": "Deep reverence for ancestors (Tip-Kur Tip-Kha), matrilineal remembrance, and honoring the maternal uncles and fathers.",
        "khasi_text": """Ki Mawbynna ki long ki maw ba kyntang tam ha ka dustur Khasi bad Pnar. Naduh hyndai hinthai, haba ki kpa tymmen ki la iap, ki kur ki ju pynieng ia kine ki maw ba heh ban kynmaw ia ka nam, ka burom, bad ka jingtrei jong ki ha pyrthei.

Ki maw kiba ieng ba jrong ki dei Ki Mawshynrang (Mawthoh), kiba pyni ia ka bor bad ka jingiada jong ki kni ki kpa. Ki maw kiba thiah pat ki dei Ki Mawkynthai (Mawkjat), kiba pyni ia ka jingshaniah, ka jingpynheh pynsan, bad ka jingri-kur jong ka kmie.

Haba u Khasi u iohi ia kine ki mawbah ha ryngkat lynti ne ha madan, um ju leh klet ia la ki kpa tymmen. U tip ba ka jingshai bad ka burom kaba u don mynta ka wan na ka snam bad ka jingshitom jong kito kiba la leit sha ka Dwar jong U Blei. Kine ki maw ki ieng kum ki sakhi ba neh jong ka Hok bad ka Riti Khasi.""",
        "english_translation": """The Megalithic Standing Stones (Ki Mawbynna) are the sacred spiritual monuments of Khasi-Jaintia civilisation. Erected along ancient trade routes and village commons, they commemorate deceased ancestors and honor the maternal uncles and fathers.

The upright vertical menhirs (Ki Mawshynrang) represent the protective strength and spiritual guidance of the maternal uncles (*Ki Kni*), while the flat horizontal dolmens (Ki Mawkynthai) signify the nurturing bosom, sustenance, and lineage continuity of the clan mothers (*Ki Kmie*). They stand as immortal witnesses along the misty ridges of Meghalaya, ensuring no generation forgets the moral path (*Ka Hok*) of their forebears.""",
        "sections": [
            {"title": "The Ancestral Megaliths", "paragraph": 1},
            {"title": "Vertical Menhirs and Horizontal Dolmens", "paragraph": 2},
            {"title": "The Living Witnesses of Ka Hok", "paragraph": 3}
        ],
        "vocabulary": {
            "mawbynna": "commemorative standing monolith / menhir",
            "mawshynrang": "upright male menhir honoring maternal uncles",
            "mawkynthai": "flat horizontal dolmen stone honoring clan mothers",
            "maw_umkoi": "purification stones erected near sacred pools"
        }
    },
    {
        "id": "ka_pansngiat_meiramew",
        "title": "Ka Pansngiat Ksiar Ka Meiramew (The Golden Crown of Mother Earth & The Seasons)",
        "khasi_title": "Ka Pansngiat Ksiar jong Ka Meiramew bad Ki Saw Aiom",
        "category": "Ecological Myth & Seasonal Lore",
        "geographic_origin": "Meghalaya Tablelands",
        "characters": ["Ka Meiramew (Mother Earth)", "Ka Aiom Pyrem (Spring)", "Ka Aiom Lyiur (Monsoon)", "Ka Aiom Synrai (Autumn)", "Ka Aiom Tlang (Winter)"],
        "cultural_moral": "Harmony with nature's cyclic rhythms, gratitude for harvest, and protecting the sacred groves (Law Kyntang).",
        "khasi_text": """Ha kawei ka por ba barim, Ka Meiramew (Mother Earth) ka la lum ia ki saw tylli ki Aiom jong ka snem: Ka Pyrem (Spring), Ka Lyiur (Monsoon), Ka Synrai (Autumn), bad Ka Tlang (Winter). Ka la kwah ban ai ia la ka Pansngiat Ksiar (The Golden Crown) ha kata ka aiom kaba lah ban ai ia ka jingkyrkhu kaba khraw tam halor ki khun ki hajar.

Ka Pyrem ka la wan ryngkat ki syntiew ba bun rong, ki khing-khang ba thiang, bad ka jingkyndit thymmai jong ka khlaw. Ka Lyiur ka la wan ryngkat u slap ba jur, ki um kshaid ba sawa jam, bad u kba ba jyrngam ha ki lyngkha. Ka Synrai ka la wan ryngkat ka jingot kba, u bnai ba shai, bad ka suk ha ki ïing ki sem. Ka Tlang pat ka la wan ryngkat ka jingpyngngad, ka dpei ba syaid, bad ki phawar parom ha ki lyngwiar dpei.

Haba Ka Meiramew ka la peit ia kine baroh, ka la sngewthuh ba ym don kawei ka aiom kaba kham kordor ban ia kawei pat; baroh saw tylli ki donkam lang ban pynim ia ka pyrthei. Te ka la bynta ia la ka pansngiat ha ki saw bynta, da kaba pynlong ia ka snem baroh kawei ban long ka jingrwai ba neh jong ka jingim, ka jingthung, ka jingot, bad ka jingsuk.""",
        "english_translation": """In ancient days, Mother Earth (Ka Meiramew) summoned the four seasons of the Khasi year: Spring (*Ka Pyrem*), Monsoon (*Ka Lyiur*), Autumn (*Ka Synrai*), and Winter (*Ka Tlang*). She wished to bestow her Golden Crown upon the season that brought the greatest blessing to the Seven Huts.

Spring arrived dressed in wildflowers and songbirds; Monsoon poured life-giving rains filling cascades and rice paddies; Autumn arrived laden with golden harvests and serene moonlight; and Winter brought crisp mountain air, warm hearthfires, and ancient storytelling.

Observing them all, Mother Earth realized that no season could exist without the others; all four are vital threads in the tapestry of life. She divided the crown into four jewels, gracing each season with its own sacred glory, establishing the timeless agrarian calendar celebrated across Meghalaya.""",
        "sections": [
            {"title": "The Assembly of the Four Seasons", "paragraph": 1},
            {"title": "The Offerings of Spring, Monsoon, Autumn, and Winter", "paragraph": 2},
            {"title": "The Golden Harmony of the Four Jewels", "paragraph": 3}
        ],
        "vocabulary": {
            "meiramew": "Mother Earth (goddess of nature and life)",
            "pansngiat": "royal crown / ceremonial headpiece",
            "pyrem": "spring season of blooming and renewal",
            "lyiur": "monsoon season of torrential rains and green fields",
            "synrai": "autumn season of golden harvest",
            "tlang": "winter season of cold mists and fireside tales"
        }
    }
]

def build_all_folklore():
    print(f"Building folklore dataset for {len(STORIES_DATA)} foundational legends...")
    index = []
    total_words = 0
    
    for s in STORIES_DATA:
        s_id = s["id"]
        words_c = len(s["khasi_text"].split()) + len(s["english_translation"].split())
        s["word_count"] = words_c
        total_words += words_c
        
        out_file = FOLKLORE_DATA_DIR / f"{s_id}.json"
        with open(out_file, "w", encoding="utf-8") as f:
            json.dump(s, f, ensure_ascii=False, indent=2)
            
        print(f"  [Done] {s['title']} -> {out_file.name} ({words_c} words)")
        
        index.append({
            "id": s["id"],
            "title": s["title"],
            "khasi_title": s["khasi_title"],
            "category": s["category"],
            "geographic_origin": s["geographic_origin"],
            "characters": s["characters"],
            "cultural_moral": s["cultural_moral"],
            "word_count": words_c
        })
        
    index_file = FOLKLORE_DATA_DIR / "folklore_index.json"
    with open(index_file, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=2)
        
    print(f"\nSuccessfully built {len(index)} folklore records ({total_words:,} words total).")

if __name__ == "__main__":
    build_all_folklore()
