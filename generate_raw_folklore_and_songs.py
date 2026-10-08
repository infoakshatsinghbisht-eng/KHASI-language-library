# -*- coding: utf-8 -*-
"""
Generate comprehensive raw Khasi folklore, myths, legends, and local songs.
Populates:
- data/raw_sources/folklore/*.txt
- data/raw_sources/songs/*.txt
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent
FOLKLORE_DIR = ROOT / "data" / "raw_sources" / "folklore"
SONGS_DIR = ROOT / "data" / "raw_sources" / "songs"
FOLKLORE_DIR.mkdir(parents=True, exist_ok=True)
SONGS_DIR.mkdir(parents=True, exist_ok=True)

STORIES = {
    "ka_jingkieng_ksier_creation.txt": """KA JINGKIENG KSIER BAD KA THYMMEI U HYNNIEWTREP
(The Golden Ladder and the Genesis of the Seven Huts)

Ha kaba nyngkong eh, haba ka pyrthei ka dang lung bad dang khuid, U Blei Nongbuh Nongthaw U la thaw ia ki Khadhynriew Trep Khadhynriew Skum ha bneng. Ki Khadhynriew Trep ki la shong suk shong sain ryngkat bad U Blei ha ka bneng ba phyrnai, ha kaba ym don jingiap, ym don jingshitom, bad ym don ka pop ne ka jingbymman.

Hynrei U Blei ha ka jingstad bad jingieit bakhraw jong U, U la thaw ia ka pyrthei da ki lum babha, ki wah ba tuid kynjai, ki khlaw ba jyrngam, bad ki mrad ki mreng ba bun jait. Ban pyniasoh ia ka bneng bad ka pyrthei, U Blei U la buh ia Ka Jingkieng Ksier (The Golden Ladder) ha kliar jong U Lum Sohpetbneng. Lum Sohpetbneng u long u sohpet jong ka pyrthei, ka jaka kaba iasoh beit thik bad ka ryngkat jong U Blei Nongthaw.

Ha man la ka sngi, ki khadhynriew tylli ki ïing ki trep ki ju hiar lyngba kane ka Jingkieng Ksier ban wan sha ka pyrthei. Ki wan pule, wan shang, wan lum soh, bad wan sarang ia ki syntiew bad ki mrad. Te haba la jan miet, ki kiew pat sha bneng ban ioh thiah ha ka jaka kyntang ryngkat bad U Kynrad.

Hynrei la poi ka sngi ba U Blei U la kylli ia ki, la mano ba kwah ban shong sah noh ha pyrthei ban ri bad ban sumar ia ka mariang, ban pynroi ia ka jaidbynriew, bad ban rep ban riang ha kane ka Ri baieit. Hynniew ngut ki kynhun trep ki la aiti ialade da ka mon sngewbha ban hiar bad ban shong sah ha ka pyrthei. Kine ki hynniew tylli ki ïing ki la long Ki Hynniewtrep Hynniewskum. Ki Khyndai trep pat ki la shong sah ha bneng, kiba ngi khot Ki Khyndaittrep.

Hadien katto katne por, ki briew ha pyrthei ki la nang roi. Hynrei ka pop bad ka jingkhwan mynsiem ka la rung ha ka pyrthei lyngba ka jingpynkhein ia ka hok. Ka don kawei ka parom ba u briew u la kiew sha Lum Diengiei bad u la thaw ia ka pop kaba khraw, kaba la pynlong ia ka Jingkieng Ksier ban dkut noh. Naduh kata ka sngi, Ki Hynniewtrep ki la sah marwei ha ka pyrthei, bad ka lynti ban kiew sha bneng ka la khang noh. Hynrei U Blei U la ai ha ki ia Ka Niam Ka Rukom, ia Ka Hok bad Ka Sot, ia Ka Khan-Pylleng bad Ka Duwai Ka Phirat, khnang ba kin ioh pyniasoh pat ia la ka mynsiem bad U Blei Trai Kynrad haduh ba kin da poi pat sha ka Dwar jong U ha kaba khatduh.
""",

    "u_diengiei_tree_darkness.txt": """U DIENGIEI BAD KA JINGKHA JONG KA PYRTHEI
(The Colossal Diengiei Tree and the Restoration of Sunlight)

Mynshuwa ha ki por barim bajah, hadien ba Ki Hynniewtrep ki la shong ha kane ka pyrthei, la mih uwei u dieng uba phylla bad uba khraw shibun eh ha kliar jong u Lum Diengiei. Une u dieng u la san ha ka rukom kaba ma bad kaba shyrkhei katta katta. Man la ka sngi u nang heh, u nang jrong, bad ki tnat jong u ki la nang pyniar shaduh ba ki la tap lut ia ka bneng baroh kawei.

Khum ka por ba une u Diengiei u la nang heh, ki sla jong u ki la pynduh lut ia ka jingshai jong ka sngi. Ka pyrthei baroh ka la dum tliw-tliw. Ym don shuh ka sngi, ym don shuh u bnai, bad ki briew ki la im ha ka jingjynjar bad ka jingtieng. Ki jingthung jingtep ki la iap tyrkhong, ki wah ki la dait thah, bad ki mrad ki la lynniar ha ka khlaw. Ki briew ki la shepting ioh ba une u dieng un pynjot lut ia ka pyrthei baroh.

Te ki Hynniewtrep ki la lum ia ka Dorbar Bah ha kliar lum. Ha kane ka Dorbar, baroh ki khun ki hajar ki la rai kut ban pom bad ban pynkyllon noh ia une u Diengiei ban ioh pat ia ka sngi bad ka jingshai. Ki la shim la ki sdie, ki wait, ki kurat, bad ki la leit sha lum ban pom ia u.

Ki la pom baroh shi sngi naduh step haduh janmiet. Ka snep bad ka doh jong une u dieng ka la nang rit bad nang duna. Hynrei haba la jan miet, namar ba la thait palat, ki la iehnoh ia ka kam bad ki la leit phai sha ki ïing jong ki ban shongthait, da kaba thmu ban wan pom pat ha ka step kaba bud.

Hynrei haba ki la wan ha ka step, ki la lyngngoh khraw ban iohi ba u Diengiei u la koit pat kumba u long mynshuwa! Baroh ki jingpom bad ki dak sdie ki la dam lut, bad ka snep ka la biang pat paka. Ki la pyrshang pom biang baroh shi sngi, hynrei ha ka step kaba bud u koit biang kumjuh. Kine ki jingpom ki la neh da ki taiew bad ki bnai, hynrei man la ka miet u diengiei u koit pat kumba ju long.

Ha kaba khatduh, uwei u sim rit (U Phreit) u la wan sha ki briew bad u la ong: "Ko ki briew, phi pom thala baroh shi sngi! Ha ka miet haba phi la leit phai, U Khla u ju wan bad u jliah ia ki dak sdie jong une u dieng da u thylliej jong u, bad ka jingspait ka dieng ka pynkoit pat ia u!"

Ki briew ki la kylli ia u sim: "Kumno ngin leh ban jop ia une u ksuid?" U Sim Phreit u la btai: "Haba phi pom ia u dieng, buh ia ki waitlieh bad ki sdie ba nep da ki khmut kiba shong sha kynjang ha ka khap ba phi pom, khnang ba haba u khla un wan jliah, u thylliej jong u un thaba bad un thlieh noh."

Ki briew ki la bud ia kane ka buit. Haba u khla u la wan ha ka miet ban jliah ia u dieng, u la thlieh u thylliej da ki wait ba nep bad u la phet kynsan da ka jinglynniar sha khlaw. Ha ka step kaba bud, ki briew ki la shem ba u diengiei um shym la koit shuh. Ki la pom bad ki la pynkyllon noh ia u da ka jingkmen bakhraw. Ka sngi ka la shai biang halor ka Ri Hynniewtrep, bad ka jingsuk ka la wan pat ha ka pyrthei.
""",

    "u_sier_lapalang_stag.txt": """U SIER LAPALANG
(The Legend of the Stately Stag and the Mother's Lament)

Ha ka them Ri Dkhar, ha ki madan ba shong phlang jyrngam ha them thor jong ka ri Surma, la shong uwei u sier babha briew bad ba donnam shibun, uba ki khot U Sier Lapalang. Une u sier u don ki reng kiba jrong kiba thaba kumba shna da ka rupa bad ka ksiar, bad ka rynieng jong u ka long kaba kynrei kaba itynnat katta katta.

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

Kine ki jingrwai sngewsih jong ka kmie u Lapalang ki la shoh beit ha ki dohnud jong ki Khasi. Naduh kata ka sngi, haba don ba iap ha ka kur ka jait, ki Khasi ki ju rwai phawar kynud sngewsih ha ka rukom kaba syriem eh ia ka sur jong ka kmie u Sier Lapalang.
""",

    "u_manik_raitong_flute.txt": """U MANIK RAITONG BAD KA SHARATI BA SNGIEWSIH
(Manik the Destitute and the Melodies of the Sharati)

Mynbarim ha ka Hima jong U Syiem, la don uwei u samla uba duk ba kyrduh tam ha ka shnong, uba kyrteng U Manik. U la duh noh ia la ki kmie ki kpa, ki hynmen ki para, baroh ki la iap noh ha ka khlam bakhraw. Um don ïing um don sem, um don kur um don kha. U shong tang ha kawei ka jingshai ba rit ha khap shnong, u phong da ki jainjot, bad u ju sleh ialade da ka dpei khnang ba ki briew kin kyntait bad kin kiar na u. Namar kata, baroh ki briew ki la khot ia u "U Manik Raitong" (Manik the Wretched Orphan).

Hynrei U Manik u don kawei ka sap kaba kyntang kaba U Blei U la pynkup ha u: ka sap ban tem ia ka Sharati (the bamboo flute). Ha ka miet haba baroh ka shnong ka la thiah jar-jar, Manik u ju sei ia la ka sharati bad u tem ia ki sur kiba thiang bad ba sngewsih katta katta. Kine ki sur ki sawa lyngba ki khlaw, ki pynkhih ia ki sla dieng, bad ki rung shaduh ki syngkhoin jong ka dohnud briew.

Ha kato ka por, U Syiem jong ka Hima u la leit jingleit jngai sha kiwei pat ki Ri bad u la sah da ki bnai ki bnai. Ka Mahadei (The Queen), kaba kyrteng Ka Lieng Makaw, ka ju shong marwei ha iing-sad. Man la ka miet haba ka sngap ia ka sur sharati u Manik Raitong, ka dohnud jong ka ka la kiew kynsan da ka jingieit bad jingkwah ban tip mano ba tem ia kine ki sur ba phylla.

Ha kawei ka miet, ka Lieng Makaw ka la bud mian-mian ia ka sur sharati shaduh ka tnum jong u Manik. Haba ka la iohi ia u Manik, la u don ha ka dpei bad jainjot, ka mynsiem jong ka ka la shah ring beit ha ka sap bad ka jingbha-briew kaba rieh ha pyrthei. Ka la rung shapoh bad ki la iasoh jingieit ha kata ka miet.

Hadien katto katne por, ka Mahadei ka la kha ia uwei u khun shynrang babha briew. Hynrei U Syiem um pat shym la wan phai na jingleit. Haba U Syiem u la wan phai, u la sngewbha khraw ban iohi ia u khunlung, hynrei u la kylli da ka jingshyrkhei: "Mano u kpa jong une u khunlung?" Ka Mahadei kam shym la kubur bad kam treh ban iathuh satlak.

U Syiem u la lum ia ka Dorbar Bah jong ka Hima baroh kawei. U la btai ba baroh ki shynrang jong ka hima kin wan ha madan bad kin rah uwei u kpu uba la kyllan da ka ngap. Uta uba u khunlung un leit kdup bad shim ia u kpu, uta un long u kpa ba shisha. Baroh ki myntri, ki riewbha, ki tymmen ki samla ki la wan ialam kpu, hynrei u khunlung um shym la leit sha no sha no ruh.

Ha kaba khatduh, ki la ong ba dang sah sa tang uwei u briew uba duk tam—U Manik Raitong. Ki la phah khot ia u Manik. Haba u Manik u la wan rung ha madan da ki jainjot bad ka dpei, u khunlung u la rynsied kynsan na ka kti ka kmie bad u la leit kdup ia u Manik da ka jingkmen.

Ka Dorbar bad U Syiem ki la pynrem ia u Manik ban iap ha ka ding. Hynrei u Manik u la kyntait ban phet krad; u la pan bor tang ban pynkhreh ialade ia ka kynthei ding (the funeral pyre) bad ban shah pyndep ia ka hok. Haba ka ding ka la meh ba heh, u Manik u la sei ia la ka Sharati bad u la tem ia ka sur kaba sngewsih tam kaba pyrthei kam pat ju sngew. Hadien ba u la kut ka jingtem, u la kiew kynsan shapoh ka ding kaba meh.

Ha kata ka khyllipmat hi, ka Lieng Makaw, kaba la iohi ia ka jingiap u samla ba ka ieit, kam shym la lah shuh ban neh. Ka la phet kynsan lyngba ka paitbah bad ka la rynsied noh shapoh ka ding ryngkat bad u Manik. Naduh kata ka sngi, ka parom u Manik Raitong bad ka Sharati ka la sah kum ka dak jong ka jingieit bakhraw kaba palat ia ka spah bad ka nam pyrthei.
""",

    "ka_nohkalikai_waterfall.txt": """KA PAROM JONG KA NOHKALIKAI
(The Tragedy of Ka Likai and the Leap at the Falls)

Ha ka shnong Rangjyrteh, kaba don ha ki thain Sohra, la shong mynshuwa kawei ka samla kaba kyrteng Ka Likai. Ka Likai ka don uwei u tnga uba ieit eh ia ka, bad ki la ioh ia kawei ka khun kynthei kaba itynnat kaba long ka jingkmen jong ka ïing baroh kawei. Hynrei ka bok kam shym la neh slem; u tnga jong ka u la iap noh kynsan, bad Ka Likai ka la sah marwei kum ka riew-kynthei khun-swet.

Ban bsa bad pynheh ia la ka khun baieit, Ka Likai ka la trei shitom jur. Ka leit kit nar, kit mar, bad trei bylla man la ka sngi na shnong sha shnong. Namar ba ka marwei, ki paralok bad ki kur ki la kyrpad ia ka ban shongkurim biang khnang ba un don u kpa ban sumar bad ban ri ia ka khunlung haba ka leit trei bylla. Te Ka Likai ka la shongkurim bad uwei pat u shynrang.

Hynrei une u tnga ba-ar um shym la long u briew ba bha. U don ka dohnud kaba bishni bad kaba sniew katta katta. Man la ka sngi haba Ka Likai ka wan phai na ka kam, ka ju kdup, ju ñiad, bad ju pynleit jingmut lut tang ia la ka khunlung, khlem da khein briew shuh ia u tnga. Une u shynrang u la nang khwan bad nang thut ka mynsiem man ka sngi.

Ha kawei ka sngi haba Ka Likai ka la leit trei jngai, une u shynrang u la shong marwei ha ïing. Ka jingbishni ka la shoh jur ha ka dohnud jong u shaduh ba u la shim ia ka wait bad u la pyniap noh ia kata ka khunlung kaba lui-lui. Nangta u la shet ia ka doh jong ka khunlung ha u khiew ranei, hynrei ia ki shymprih-kti jong ka u la leit buh rieh ha ka shang kwai.

Haba Ka Likai ka la wan phai da ka jingthait bad jingthngan bakhraw, kam shym la iohi ia la ka khun. U tnga u la ong ba ka khun ka la leit shang sha ki paralok, bad u la ai ja ai doh ia ka ban bam. Ka Likai kaba la thngan jur ka la bam sngewbha khlem da tip eiei.

Hadien ba ka la dep bam, ka la kiew ban shim kwai na ka shang ban bam kynroi kumba ju long ka rukom Khasi. Haba ka la plied ia ka shang kwai, ka la lap ia ki shymprih-kti jong la ka khunlung ba ka ieit! Mar kumta hi, ka la sngewthuh ia ka jingshisha kaba shyrkhei: ba ka la bam thiah ia ka doh jong la ka khun baieit da ki kti jong ka!

Ka jingmut jingpyrkhat jong Ka Likai ka la lamwir kynsan da ka jingsngewsih bad jingshykhei. Ka la shim ia ka waitlam ha la ka kti, ka la pyrta lynniar da ka jinglynniar kaba shyrkhei, bad ka la phet kynsan lyngba ka khlaw shaduh ka khmat riat kaba jrong tam ha Rangjyrteh. Ki briew ki la pyrshang ban khang ia ka, hynrei kam sngap shuh; ka la rynsied noh kynsan shapoh ka thwei ba jylliew jong ka kshaid. Naduh kata ka sngi, ia kata ka kshaid ba jrong bad ba itynnat la khot noh "Ka Kshaid Nohkalikai" (The Leap of Ka Likai).
""",

    "u_bsein_thlen_cave.txt": """U BSEIN THLEN BAD KA JINGJOP HA DAINTHLEN
(The Myth of the Thlen Serpent and the Triumph at Dainthlen)

Ha ki por hyndai, ha kawei ka krem ba shyrkhei kaba don ha Sohra hajan ka wah kaba tuid sha them Surma, la shong uwei u bsein uba khraw bad uba ma katta katta uba ki khot U Thlen. Une u Thlen um dei u bsein uba kum kiwei pat; u dei u ksuid uba bam briew bad uba pynlong ia ka jingshyrkhei ha ka Ri Khasi baroh kawei.

Ka rukom jong une u Thlen ka long ba haba ki briew ki iaid ha ka lynti ba marjan bad ka krem jong u, lada ki iaid arngut, un bam nguid noh ia uwei; lada ki iaid saw ngut, un bam ia ki arngut. Da kumta, ki briew ki la tieng lut ban iaid lyngba kata ka jaka, bad ka shnong ka la duh noh ia ki briew kiba bun. Nalor kata, u Thlen u ju ai spah pynsuk ia kito ki briew kiba man-bieit bad kiba kñia snam briew sha u, kiba ki khot Ki Nongshohnoh.

Haba ka jingshitom ka la jur palat, uwei u riewshlur uba kyrteng U Suidnoh u la thaw ka buit ban pynduh jait ia une u ksuid. U Suidnoh u la leit shajan ka krem u Thlen man la ka sngi bad u la rah ia ka doh blang ban bsa ia u. Man ba u pyrta, u Thlen u ju sei la ka khlieh na ka krem bad u plied la ka shyntur kaba heh, bad U Suidnoh u ju kyntait shapoh ka doh blang. Ha kane ka rukom, u Thlen u la nang shaniah jur ha U Suidnoh.

Haba u la iohi ba u Thlen u la shaniah pura, U Suidnoh u la pynkhreh ia ka buit kaba khatduh. U la shna kawei ka nar ba heh bad u la thang ia ka ha ka dpei ding haduh ba kata ka nar ka la saw hek-hek da ka jingshit bakhraw. Nangta u la shim ia ka nar da ki khnap-nar ba khlain, u la leit sha ka krem u Thlen, bad u la pyrta kumba ju leh.

U Thlen u la pynpaw la ka khlieh bad u la ang la ka shyntur ban pdiang ia ka doh. Hynrei ha ka jaka ka doh blang, U Suidnoh u la theh beit ia kata ka nar ba saw hek-hek shapoh u pdot jong u Thlen! Ka ding ka la bam ia ki snier jong u, u Thlen u la lynniar da ka bor bakhraw, u la kyrsum ha madan bad u la pait ka mynsiem.

Ki Khasi ki la leit tan ia une u bsein na ka krem sha madan hajan ka kshaid. Ha kata ka jaka, ki la dain pynpait ia ka doh jong u ha ki maw kiba heh khnang ban ym pynmih shuh ia ka bih. Ia kata ka jaka la khot mynta Ka Kshaid Dainthlen (The Slaying of the Thlen), bad ki dak jong ki maw ba la dain ia u Thlen ki dang paw haduh kine ki sngi.
"""
}

SONG_TEXTS = {
    "ka_sur_u_sier_lapalang_complete.txt": """KA SUR U SIER LAPALANG (COMPLETE LYRICS & PHAWARTEXT)
(The Full Folk Ballad and Mother's Lament)

[Bynta I: Ka Jingrwai Kmie ha Ri Thor]
Ko Lapalang phrang sngi jong nga,
Kum bating-shein u mankara!
Haba na nga me la khlad noh,
Dohnud sngewsih nga im suhsat.

Shong khop ha la ri them ri thor,
Bam da u khah bam da u nor!
Ngin bam da u jangew jathang,
Baroh shi lyiur baroh shi tlang!

[Bynta II: Ka Jingkiew sha Ri Lum]
Pynban kynrem na nga me khlad,
Sha Ri Khasi me la kiew krad!
U phlang ba thiang u la ring phai,
Ki thwei ba khuid ki la pynkai!

[Bynta III: Ka Jingiap bad Ka Phawar Beh Mrad]
Wow! La shet ka tieh pongdeng,
Ia ka rynieng u kynrem reng!
Wow! La kjit u nam sarang,
Ia ka mynsiem u Lapalang!

Ha kliar Lum Shillong u la noh,
U khnam ba bih u la kem thoh!
Ummat ka kmie ki la shlei tuid,
Ki lum ki them ki la jaw ruid!

[Bynta IV: Ka Ktien Khatduh]
Ko khun baieit ba thiah ha madan,
Ym don shuh u ban pynkyndit kram!
Sah marwei nga ha kane ka sngi,
Ka nam jong me kan neh ha ri!
""",

    "shad_suk_mynsiem_ceremonial_chants.txt": """SUR SHAD SUK MYNSIEM BAD KI PHAWARTYLLAI
(Chants and Melodies of the We-Dance-in-Peace Spring Festival)

[Sur Tangmuri bad Ksing Shynrang]
Teng teng teng, ksing ka la sawa!
Ri lum Ri Khasi ka la kyndit!
Ka sngi ka la kiew ha Weiking,
Ki khun ki kti ki la mih seng!

[Ka Phawar Shad Kynthei]
Ryngkat ka pansngiat ba thaba ksiar,
Ka jainsem dhara ba jop pyrthei!
Ki kynthei lui-lui ki shad mian-mian,
Kum ki angel ba hiar na bneng!

[Ka Phawar Shad Shynrang]
Ki samla shlur ba bat waitlam,
Ryngkat ka symphiah ba pynshad kham!
Ki da ia ka burom ka Kur ka Jait,
Ki ieng ha ka Hok ban ym ju lait!

[Ka Jingduwai Sngewbha]
Khublei ko Blei U Nongbuh Nongthaw!
Ba me la ai ia ka suk ka sain!
Ia u kba u khaw ha ki lum ki them,
Ia ka roi ka par ha ka Hima baroh!
""",

    "phawar_iasiat_khnam_archery_verses.txt": """KI PHAWÁR IASIAT KHNAM (KHASI TRADITIONAL ARCHERY VERSES)
(Coupled Victory and Taunt Verses of Indigenous Khasi Archery)

1.
Hoi kiw! Hoi kiw!
U khnam uba nep u la leit thaba,
U la dung ha ka skum ba la buh ha lyngkba!
Ko samla ka shnong to pyrta jam,
Namar ba u khnam u la jop ia ka nam!

2.
U lum u them u la sawa kynjai,
Ka ryntieh siej-lieng ka la pynhiar kynhai!
U nongsiat ba tbit u la thoh la ka kti,
Ban kyntiew ia ka burom jong la ka Ri!

3.
Ka wait ka stieh ngi kyntait noh,
Tang u khnam u ryntieh ngi bat thoh!
Ka jingsiat ka dei ka akor ka bor,
Kaba neh pateng la pateng ha ka dor!
"""
}

def generate_all():
    print("Writing raw folklore files...")
    for fname, content in STORIES.items():
        fpath = FOLKLORE_DIR / fname
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content.strip() + "\n")
        print(f"  Created: {fpath.name} ({len(content)} chars)")

    print("\nWriting raw song files...")
    for fname, content in SONG_TEXTS.items():
        fpath = SONGS_DIR / fname
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content.strip() + "\n")
        print(f"  Created: {fpath.name} ({len(content)} chars)")

    print("\nCompleted raw folklore and song generation.")

if __name__ == "__main__":
    generate_all()
