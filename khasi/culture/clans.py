# -*- coding: utf-8 -*-
"""
Khasi Matrilineal Clans (Ki Kur & Ki Jaid), Lineage Systems, Surnames & Traditional Names.
Comprehensive registry of recognized Khasi, Pnar, War, Bhoi, and Maram clans,
ancestral maternal roots (Ka \u00cfawbei), exogamous kinship rules (Ka Sang Ka Ma),
and traditional given names of Meghalaya.
"""

from typing import Dict, List, Any, Optional

CLANS: List[Dict[str, Any]] = [
    {
        "clan_name": "Syiem (Jaid Syiem)",
        "branches": ["Syiemlieh", "Syiemiong", "Khriem", "Nongkhlaw", "Sohra", "Maharam", "Mylliem", "Khyrim", "Nobosohphoh"],
        "category": "Royal / Ruling Clan",
        "historical_role": "Hereditary constitutional chiefs and rulers of Khasi states (Ki Hima); trace descent from the mythological ancestress Ka Pahsyntiew or Ka Lieng Makaw."
    },
    {
        "clan_name": "Lyngdoh",
        "branches": ["Lyngdoh Nonglait", "Lyngdoh Mawphlang", "Lyngdoh Marshillong", "Lyngdoh Nongbri", "Lyngdoh Rngi", "Lyngdoh Kynshi"],
        "category": "Priestly / Administrative Clan",
        "historical_role": "Traditional high priests and prime ministerial ministers; custodians of sacred groves, state sacrifices, and customary religious ceremonies."
    },
    {
        "clan_name": "Nongrum",
        "branches": ["Nongrum", "Roy Nongrum"],
        "category": "Foundational Highland Clan",
        "historical_role": "Prominent highland clan; produced illustrious authors, novelists (K.W. Nongrum), and traditional civic leaders."
    },
    {
        "clan_name": "Wahlang",
        "branches": ["Wahlang", "Kerios Wahlang"],
        "category": "Highland Clan",
        "historical_role": "Ancient clan rooted in the valleys and central ridges; produced revered musicians, folk balladeers, and community elders."
    },
    {
        "clan_name": "Kharbangar",
        "branches": ["Kharbangar", "Tipriti Kharbangar"],
        "category": "Traditional Clan",
        "historical_role": "Prominent clan bearing the traditional 'Khar-' prefix (historically denoting trade and settlement connections); celebrated in culture and the arts."
    },
    {
        "clan_name": "Dkhar (Jaid Dkhar)",
        "branches": ["Dkhar", "Streamlet Dkhar"],
        "category": "Assimilated Matrilineal Lineage",
        "historical_role": "Lineages founded by ancestral mothers of diverse origins who were ceremonially adopted and fully integrated into the matrilineal Khasi Kur system."
    },
    {
        "clan_name": "Rymbai",
        "branches": ["Rymbai"],
        "category": "Pnar / Jai\u00f1tia Clan",
        "historical_role": "Distinguished Pnar clan holding hereditary administrative and judicial offices in the historic Jaintia Kingdom."
    },
    {
        "clan_name": "Khongwir",
        "branches": ["Khongwir"],
        "category": "Shella / Southern Escarpment Clan",
        "historical_role": "Ancient clan from the southern War Khasi region, famed for horticulture, orange groves, and village confederacies."
    },
    {
        "clan_name": "Kharlukhi",
        "branches": ["Kharlukhi"],
        "category": "Highland Clan",
        "historical_role": "Influential clan of scholars, statesmen, and cultural educators across the central Khasi Hills."
    },
    {
        "clan_name": "Mawlong",
        "branches": ["Mawlong"],
        "category": "Highland & War Clan",
        "historical_role": "Ancient clan named after ancestral megalithic settlements; prominent in indigenous metallurgy and trade."
    },
    {
        "clan_name": "Sutnga",
        "branches": ["Sutnga Syiem", "Jait Syiem Sutnga"],
        "category": "Royal / Pnar Dynastic Clan",
        "historical_role": "Founding dynasty of the historic Jaintia Empire; legendary descent from Ka Matsyodari (Ka Lieng Makaw) at Syntu Ksiar."
    },
    {
        "clan_name": "Diengdoh",
        "branches": ["Diengdoh Bah", "Diengdoh Kyndait"],
        "category": "Highland Aristocratic Clan",
        "historical_role": "Revered clan associated with early iron smelting at Sohra and custodians of state councils; produced legendary writers and civil servants."
    },
    {
        "clan_name": "Blah",
        "branches": ["Blah"],
        "category": "Pnar & Khasi Clan",
        "historical_role": "Respected clan across the Khasi and Jaintia Hills, known for diplomacy, civic leadership, and education."
    },
    {
        "clan_name": "Marbaniang",
        "branches": ["Marbaniang"],
        "category": "Highland Clan",
        "historical_role": "Prominent highland clan from the central tableland; produced state ministers, educators, and community leaders."
    },
    {
        "clan_name": "Warjri",
        "branches": ["Warjri"],
        "category": "Southern / Highland Clan",
        "historical_role": "Ancient clan tracing roots to the southern ridges and sacred groves; celebrated for cultural scholarship and leadership."
    },
    {
        "clan_name": "Shabong",
        "branches": ["Shabong"],
        "category": "Highland Clan",
        "historical_role": "Highland lineage known for mastery of customary land tenure, archery traditions, and oral storytelling."
    },
    {
        "clan_name": "Kharkongor",
        "branches": ["Kharkongor"],
        "category": "Foundational Highland Clan",
        "historical_role": "Prominent clan in the Shillong and Mylliem state territories; active in commerce, civic institutions, and the arts."
    },
    {
        "clan_name": "Majaw",
        "branches": ["Majaw", "Lou Majaw"],
        "category": "Highland Clan",
        "historical_role": "Esteemed family renowned for cultural contributions, including pioneering rock balladeer Lou Majaw."
    },
    {
        "clan_name": "Khonglah",
        "branches": ["Khonglah"],
        "category": "War Khasi Clan",
        "historical_role": "Prominent southern War Khasi clan from the southern valleys; builders of living root bridges and betel cultivators."
    },
    {
        "clan_name": "Bareh",
        "branches": ["Bareh", "Hamlet Bareh Ngap Kynta"],
        "category": "Scholarly Clan",
        "historical_role": "Distinguished lineage that produced Padma Shri historian Dr. Hamlet Bareh and pioneering dramatist Victor Bareh."
    },
    {
        "clan_name": "Nongbri",
        "branches": ["Nongbri", "Tiplut Nongbri"],
        "category": "Highland Clan",
        "historical_role": "Celebrated clan that produced eminent sociologists, gender scholars, and constitutional analysts of matrilineal society."
    },
    {
        "clan_name": "Swer",
        "branches": ["Swer"],
        "category": "Highland Clan",
        "historical_role": "Ancient clan rooted in the Sohra and Cherra plateau; custodians of early printing, literary publications, and education."
    },
    {
        "clan_name": "Pariat",
        "branches": ["Pariat"],
        "category": "Pnar / Jai\u00f1tia Clan",
        "historical_role": "Distinguished Pnar family active in trade, public governance, and traditional cultural festivals."
    },
    {
        "clan_name": "Tariang",
        "branches": ["Tariang"],
        "category": "Pnar Clan",
        "historical_role": "Respected Jaintia clan with ancestral ties to Jowai and Nartiang; prominent in municipal and agricultural stewardship."
    },
    {
        "clan_name": "Laloo",
        "branches": ["Laloo"],
        "category": "Pnar Clan",
        "historical_role": "Prominent Pnar lineage in Jowai; produced pioneering administrators, scholars, and civic contributors."
    },
    {
        "clan_name": "Nongtdu",
        "branches": ["Nongtdu"],
        "category": "Pnar Clan",
        "historical_role": "Traditional Jaintia clan prominent in local village governance and cultural festivals."
    },
    {
        "clan_name": "Passah",
        "branches": ["Passah"],
        "category": "Pnar Clan",
        "historical_role": "Esteemed family in West Jaintia Hills that produced master musicians, educators, and community leaders."
    },
    {
        "clan_name": "Lamare",
        "branches": ["Lamare"],
        "category": "Pnar & Khasi Clan",
        "historical_role": "Widespread clan celebrated for agricultural stewardship, trade, and public service."
    },
    {
        "clan_name": "Mukhim",
        "branches": ["Mukhim", "Patricia Mukhim"],
        "category": "Highland Clan",
        "historical_role": "Prominent clan that produced pioneering journalists, Padma Shri recipients, and social commentators."
    },
    {
        "clan_name": "Kharpuri",
        "branches": ["Kharpuri", "Dewan Singh Kharpuri"],
        "category": "Highland Scholarly Clan",
        "historical_role": "Prominent clan of folklorists, educators, and authors; celebrated for documenting the oral mythologies of U Hynniewtrep."
    },
    {
        "clan_name": "Nongkynrih",
        "branches": ["Nongkynrih", "Kynpham Sing Nongkynrih"],
        "category": "Highland Literary Clan",
        "historical_role": "Esteemed clan renowned for contemporary literature, poetry, and academic leadership in Meghalaya."
    },
    {
        "clan_name": "Thangkhiew",
        "branches": ["Thangkhiew"],
        "category": "Highland Clan",
        "historical_role": "Prominent lineage in the East Khasi Hills, active in legal jurisprudence, state administration, and cultural preservation."
    },
    {
        "clan_name": "Basan",
        "branches": ["Basan"],
        "category": "Ministerial & State Clan",
        "historical_role": "Hereditary noble elders (Ki Basan) serving as electors and ministers in traditional Khasi state councils."
    },
    {
        "clan_name": "Mylliemngap",
        "branches": ["Mylliemngap"],
        "category": "Foundational Mylliem Clan",
        "historical_role": "Founding clan of the Hima Mylliem; hereditary keepers of state rites and council deliberations."
    },
    {
        "clan_name": "Sohtun",
        "branches": ["Sohtun"],
        "category": "Highland Clan",
        "historical_role": "Ancient highland clan rooted in the central ranges; respected for community organizing and church history."
    },
    {
        "clan_name": "Mawrie",
        "branches": ["Mawrie", "H. Onderson Mawrie"],
        "category": "Philosophical & Scholarly Clan",
        "historical_role": "Prominent clan of Seng Khasi theologians, philosophers, and writers who codified the moral pillars of Tip-Briew Tip-Blei."
    },
    {
        "clan_name": "Khongjee",
        "branches": ["Khongjee"],
        "category": "War Khasi Clan",
        "historical_role": "Southern War clan celebrated for spice cultivation (black pepper, bay leaf) and traditional stone masonry."
    },
    {
        "clan_name": "Kharsati",
        "branches": ["Kharsati"],
        "category": "Highland Clan",
        "historical_role": "Traditional lineage of artisans, traders, and cultural advocates in the East and West Khasi Hills."
    },
    {
        "clan_name": "Rapthap",
        "branches": ["Rapthap"],
        "category": "Highland Clan",
        "historical_role": "Ancient clan from the central tablelands, respected in municipal service and agricultural stewardship."
    },
    {
        "clan_name": "Sumer",
        "branches": ["Sumer"],
        "category": "Pnar & Bhoi Clan",
        "historical_role": "Widespread lineage across Jaintia and Ri-Bhoi; active in traditional wet-rice agriculture and forest conservation."
    },
    {
        "clan_name": "Myntdu",
        "branches": ["Myntdu"],
        "category": "Pnar Clan",
        "historical_role": "Jaintia clan named after the sacred Myntdu River ('Ka Tawiar Takan'); guardians of riverine ceremonies."
    },
    {
        "clan_name": "Chyrmang",
        "branches": ["Chyrmang"],
        "category": "Pnar Clan",
        "historical_role": "Ancient Pnar clan holding traditional responsibilities in the Behdienkhlam festivals of Jowai."
    },
    {
        "clan_name": "Pohshna",
        "branches": ["Pohshna"],
        "category": "Pnar Clan",
        "historical_role": "Respected lineage from the Jaintia Hills, known for skilled metalcraft, carpentry, and civic leadership."
    },
    {
        "clan_name": "Dhar",
        "branches": ["Dhar"],
        "category": "Pnar & Khasi Clan",
        "historical_role": "Major merchant and administrative clan active across Shillong and Jaintia Hills in enterprise and politics."
    },
    {
        "clan_name": "Challam",
        "branches": ["Challam"],
        "category": "Pnar Clan",
        "historical_role": "Distinguished Pnar lineage associated with the sacred groves and high priesthood of the Jaintia kingdom."
    },
    {
        "clan_name": "Phawa",
        "branches": ["Phawa"],
        "category": "Pnar Clan",
        "historical_role": "Esteemed family in West Jaintia Hills known for musicality, oral chanting, and traditional dance participation."
    },
    {
        "clan_name": "Biam",
        "branches": ["Biam"],
        "category": "Pnar Clan",
        "historical_role": "Ancient clan rooted in the eastern Jaintia valleys; famed for cattle breeding and hill cultivation."
    },
    {
        "clan_name": "Shadap",
        "branches": ["Shadap"],
        "category": "Bhoi & Khasi Clan",
        "historical_role": "Prominent clan in northern Ri-Bhoi district; bridges Khasi highland and valley customs with agrarian expertise."
    },
    {
        "clan_name": "Pohchen",
        "branches": ["Pohchen"],
        "category": "War & Pnar Clan",
        "historical_role": "Lineage residing in the deep southern gorges and southern Jaintia slopes, renowned for orange and arecanut groves."
    },
    {
        "clan_name": "Shullai",
        "branches": ["Shullai", "L. Gilbert Shullai"],
        "category": "Pnar & Khasi Scholarly Clan",
        "historical_role": "Prominent family that produced revered historians, archivists, and collectors of Khasi-Pnar customary laws."
    },
    {
        "clan_name": "Toi",
        "branches": ["Toi"],
        "category": "Pnar Clan",
        "historical_role": "Respected Pnar family active in civic affairs, education, and the preservation of indigenous religious tenets."
    },
    {
        "clan_name": "Kyndiah",
        "branches": ["Kyndiah", "P.R. Kyndiah"],
        "category": "Pnar Statesman Clan",
        "historical_role": "Illustrious family that produced Union Cabinet ministers, Governors, authors, and national freedom advocates."
    },
    {
        "clan_name": "Lipon",
        "branches": ["Lipon"],
        "category": "Pnar Clan",
        "historical_role": "Traditional Jaintia clan associated with community festivals and customary dispute resolution."
    },
    {
        "clan_name": "Hadem",
        "branches": ["Hadem"],
        "category": "Eastern Jaintia Clan",
        "historical_role": "Border clan of the eastern plateaus near the Kupli (Kopili) River, known for intercultural harmony and trade."
    },
    {
        "clan_name": "Sungoh",
        "branches": ["Sungoh"],
        "category": "Pnar Clan",
        "historical_role": "Respected lineage in Jowai and surrounding elakas; active in community youth movements and sports."
    },
    {
        "clan_name": "Ryntathiang",
        "branches": ["Ryntathiang"],
        "category": "Highland Clan",
        "historical_role": "Ancient clan from the central plateau, respected for devotion to matrilineal clan purity (Ka Kur Ka Jait)."
    },
    {
        "clan_name": "Ryngksai",
        "branches": ["Ryngksai"],
        "category": "Highland Clan",
        "historical_role": "Highland lineage known for archery craftsmanship, bow making, and traditional athletic contests."
    },
    {
        "clan_name": "Kharmalki",
        "branches": ["Kharmalki"],
        "category": "Highland Clan",
        "historical_role": "Prominent clan from the Malki locality of Shillong; active in early civic development and education."
    },
    {
        "clan_name": "Kharumnuid",
        "branches": ["Kharumnuid"],
        "category": "Highland Clan",
        "historical_role": "Ancient clan rooted in the valleys around Shillong Peak; guardians of sacred mountain water springs."
    },
    {
        "clan_name": "Kharsyntiew",
        "branches": ["Kharsyntiew"],
        "category": "Highland Clan",
        "historical_role": "Distinguished lineage meaning 'Flower clan'; celebrated for weaving, floral aesthetics, and community leadership."
    },
    {
        "clan_name": "Kharnaior",
        "branches": ["Kharnaior"],
        "category": "Highland Clan",
        "historical_role": "Prominent clan known for craftsmanship, commercial trade, and active support of tribal schools."
    },
    {
        "clan_name": "Nongspung",
        "branches": ["Nongspung", "Jaid Syiem Nongspung"],
        "category": "Territorial & Princely Clan",
        "historical_role": "Hereditary rulers and noble families of the historic Hima Nongspung, famous for ancient iron foundry sites."
    },
    {
        "clan_name": "Nongrang",
        "branches": ["Nongrang"],
        "category": "West Khasi Clan",
        "historical_role": "Respected clan from West Khasi Hills, prominent in forest stewardship and timber craftsmanship."
    },
    {
        "clan_name": "Nongkseh",
        "branches": ["Nongkseh"],
        "category": "Foundational Highland Clan",
        "historical_role": "Historic clan associated with the ancient capital of the Shillong Syiemship at Nongkseh near Lum Shyllong."
    },
    {
        "clan_name": "Nongbet",
        "branches": ["Nongbet"],
        "category": "Highland Clan",
        "historical_role": "Ancient clan noted for traditional medicine practitioners and herbal healers (Ki Nong-ai Dawai)."
    },
    {
        "clan_name": "Mawnai",
        "branches": ["Mawnai"],
        "category": "Megalithic Highland Clan",
        "historical_role": "Prominent clan with historical connections to the sacred monolithic sites and stone carving traditions of the highlands."
    },
    {
        "clan_name": "Marwein",
        "branches": ["Marwein"],
        "category": "Highland Clan",
        "historical_role": "Ancient clan from the central and western uplands; leaders in customary village durbars."
    },
    {
        "clan_name": "Syiemiong",
        "branches": ["Syiemiong"],
        "category": "Royal Branch Clan",
        "historical_role": "'The Black Syiem' branch; co-ruling royal dynasty of the Hima Khyrim and Hima Mylliem."
    },
    {
        "clan_name": "Syiemlieh",
        "branches": ["Syiemlieh", "David R. Syiemlieh"],
        "category": "Royal Branch & Scholarly Clan",
        "historical_role": "'The White Syiem' branch; produced eminent historians, UPSC Chairmen, and educational leaders."
    },
    {
        "clan_name": "Hynniewta",
        "branches": ["Hynniewta"],
        "category": "Scholarly Clan",
        "historical_role": "Distinguished clan known for high academic achievement, botanical research, and civil services."
    },
    {
        "clan_name": "Langstieh",
        "branches": ["Langstieh"],
        "category": "Highland Clan",
        "historical_role": "Ancient clan celebrated for traditional weaving, silkworm rearing (Ryndia), and domestic handicrafts."
    },
    {
        "clan_name": "Kurkalang",
        "branches": ["Kurkalang"],
        "category": "Highland Clan",
        "historical_role": "Respected clan from the upper ridges; guardians of ancestral boundaries and folk legends."
    },
    {
        "clan_name": "Rani",
        "branches": ["Rani"],
        "category": "Bhoi & Highland Clan",
        "historical_role": "Prominent clan bridging Ri-Bhoi and East Khasi Hills, known for agricultural productivity and commerce."
    },
    {
        "clan_name": "Ryndem",
        "branches": ["Ryndem"],
        "category": "Highland Clan",
        "historical_role": "Respected family active in community service, village welfare societies, and cultural preservation."
    },
    {
        "clan_name": "Riahtam",
        "branches": ["Riahtam"],
        "category": "Highland Clan",
        "historical_role": "Ancient clan associated with high altitude pastures and cattle herds in the high Khasi hills."
    },
    {
        "clan_name": "Snaitang",
        "branches": ["Snaitang"],
        "category": "Highland Clan",
        "historical_role": "Highland clan known for legal advocacy, church leadership, and local village durbars."
    },
    {
        "clan_name": "Slong",
        "branches": ["Slong"],
        "category": "Pnar Clan",
        "historical_role": "Traditional Jaintia clan prominent in religious rituals, brass casting, and community leadership."
    },
    {
        "clan_name": "Suting",
        "branches": ["Suting"],
        "category": "Highland & War Clan",
        "historical_role": "Prominent clan along the southern slopes; celebrated for horticulture and honey harvesting."
    },
    {
        "clan_name": "Tangsong",
        "branches": ["Tangsong"],
        "category": "War Khasi Clan",
        "historical_role": "Southern War clan renowned for living root bridge maintenance and ancestral stone trails."
    },
    {
        "clan_name": "Thabah",
        "branches": ["Thabah"],
        "category": "Highland Clan",
        "historical_role": "Respected clan active in education, healthcare, and traditional sports in the East Khasi Hills."
    },
    {
        "clan_name": "Thubru",
        "branches": ["Thubru"],
        "category": "Pnar Clan",
        "historical_role": "Ancient Pnar clan prominent in Jaintia oral literature, folk dancing, and community festivals."
    },
    {
        "clan_name": "Wankhar",
        "branches": ["Wankhar"],
        "category": "Highland & Scholarly Clan",
        "historical_role": "Famous family of entomologists, photographers, and educators; established the historic Wankhar Butterfly Museum in Shillong."
    },
    {
        "clan_name": "Nongkhlaw",
        "branches": ["Nongkhlaw", "U Tirot Sing Nongkhlaw"],
        "category": "Princely & Patriot Clan",
        "historical_role": "Ancestral dynasty of the legendary hero and freedom fighter U Tirot Sing Syiem, hero of the Anglo-Khasi War (1829-1833)."
    },
    {
        "clan_name": "Nongstoin",
        "branches": ["Nongstoin", "Jaid Syiem Nongstoin"],
        "category": "Royal / Western Princely Clan",
        "historical_role": "Ruling dynasty of the largest Khasi state (Hima Nongstoin), famous for rich forests, minerals, and traditional independence."
    },
    {
        "clan_name": "Mawsmai",
        "branches": ["Mawsmai"],
        "category": "Sohra Plateau Clan",
        "historical_role": "Ancestral clan residing near the world-renowned Mawsmai Caves and Nohsngithiang Falls in Sohra."
    },
    {
        "clan_name": "Laitphlang",
        "branches": ["Laitphlang"],
        "category": "Highland Clan",
        "historical_role": "Ancient clan from the grassy uplands; known for grazing commons and traditional weaving."
    },
    {
        "clan_name": "Mawthoh",
        "branches": ["Mawthoh"],
        "category": "Highland Clan",
        "historical_role": "Prominent clan meaning 'Inscribed Stone'; ancestral custodians of megalithic boundary markers."
    },
    {
        "clan_name": "Mawshun",
        "branches": ["Mawshun"],
        "category": "Highland Clan",
        "historical_role": "Lineage associated with limestone quarrying, indigenous lime-kilns, and building craftsmanship."
    },
    {
        "clan_name": "Nongpoh",
        "branches": ["Nongpoh"],
        "category": "Ri-Bhoi Clan",
        "historical_role": "Prominent clan from the central trading post of Ri-Bhoi district, linking the hills with the Brahmaputra plains."
    },
    {
        "clan_name": "Nongbsap",
        "branches": ["Nongbsap"],
        "category": "Highland Clan",
        "historical_role": "Respected clan from the upper hills, active in community welfare and customary land councils."
    },
    {
        "clan_name": "Mawblei",
        "branches": ["Mawblei"],
        "category": "Highland Clan",
        "historical_role": "Clan whose name signifies 'God's Rock'; associated with reverence for the sacred natural landscape."
    },
    {
        "clan_name": "Kshiar",
        "branches": ["Kshiar"],
        "category": "Pnar & Khasi Clan",
        "historical_role": "Lineage meaning 'Pure Gold'; esteemed for integrity, goldsmithing, and ceremonial regalia ornaments."
    },
    {
        "clan_name": "Nongmin",
        "branches": ["Nongmin"],
        "category": "Highland Clan",
        "historical_role": "Traditional lineage active in agriculture, community storytelling, and local village affairs."
    },
    {
        "clan_name": "Khongsdam",
        "branches": ["Khongsdam"],
        "category": "War Khasi Clan",
        "historical_role": "Prominent southern War clan from the subtropical slopes; master cultivators of betel leaf and black pepper."
    },
    {
        "clan_name": "Khonglam",
        "branches": ["Khonglam", "Dr. F.A. Khonglam"],
        "category": "War & Highland Clan",
        "historical_role": "Distinguished lineage that produced state Chief Ministers, medical doctors, and public leaders."
    },
    {
        "clan_name": "Khongsti",
        "branches": ["Khongsti"],
        "category": "War Khasi Clan",
        "historical_role": "Ancient War clan famed for canyon trails, river crossing bridges, and organic horticulture."
    },
    {
        "clan_name": "Khongji",
        "branches": ["Khongji"],
        "category": "War Khasi Clan",
        "historical_role": "Respected clan along the Bangladesh border slopes, known for cross-border trade and citrus orchards."
    },
    {
        "clan_name": "Khongthohrem",
        "branches": ["Khongthohrem"],
        "category": "War Khasi Clan",
        "historical_role": "Southern clan preserving ancient Austroasiatic linguistic forms and deep horticultural heritage."
    },
    {
        "clan_name": "Khongmawloh",
        "branches": ["Khongmawloh"],
        "category": "War Khasi Clan",
        "historical_role": "Lineage rooted in the rugged limestone ravines, skilled in building dry-stone terraces."
    },
    {
        "clan_name": "Khongwet",
        "branches": ["Khongwet"],
        "category": "War Khasi Clan",
        "historical_role": "Ancient southern family celebrated for ginger, turmeric, and broom-grass farming."
    },
    {
        "clan_name": "Khongdup",
        "branches": ["Khongdup"],
        "category": "War Khasi Clan",
        "historical_role": "Distinguished clan that produced prominent authors, educationists, and social pioneers."
    },
    {
        "clan_name": "Rapsang",
        "branches": ["Rapsang"],
        "category": "Highland Clan",
        "historical_role": "Prominent highland clan active in entrepreneurship, civic development, and modern sports."
    },
    {
        "clan_name": "Rynjah",
        "branches": ["Rynjah"],
        "category": "Highland Clan",
        "historical_role": "Ancient lineage from Shillong tableland; gave their name to the historic Rynjah township."
    },
    {
        "clan_name": "Nongbri-Nonglait",
        "branches": ["Nongbri-Nonglait"],
        "category": "Highland Aristocratic Clan",
        "historical_role": "Noble lineage holding traditional priestly and ministerial roles in the historic Hima Nongkhlaw."
    },
    {
        "clan_name": "Lyngkhoi",
        "branches": ["Lyngkhoi"],
        "category": "West Khasi Clan",
        "historical_role": "Respected clan in West Khasi Hills, custodians of pristine highland streams and pine forests."
    },
    {
        "clan_name": "Myrthong",
        "branches": ["Myrthong"],
        "category": "Highland Clan",
        "historical_role": "Prominent clan active in public administration, community legal advocacy, and education."
    },
    {
        "clan_name": "Nongkhyriem",
        "branches": ["Nongkhyriem"],
        "category": "Highland Clan",
        "historical_role": "Ancient lineage tied to the sacred hills of the historic Khyrim kingdom."
    },
    {
        "clan_name": "Nongpluh",
        "branches": ["Nongpluh"],
        "category": "Highland Clan",
        "historical_role": "Respected family active in traditional ironcraft and civic life across the Khasi plateau."
    }
]

TRADITIONAL_NAMES: List[Dict[str, Any]] = [
    {
        "name": "Kynpham",
        "gender": "male",
        "meaning": "Remembrance / Counsel / Memory of the heart",
        "cultural_note": "Revered name signifying thoughtful wisdom and deep reflection; famously borne by celebrated poet Kynpham Sing Nongkynrih."
    },
    {
        "name": "Banrap",
        "gender": "male",
        "meaning": "One who aids, sustains, or brings helpful support",
        "cultural_note": "Derived from Khasi verb 'ïarap' (to help); bestowed in hope that the son will be a pillar to his mother and family."
    },
    {
        "name": "Daplin",
        "gender": "unisex",
        "meaning": "Abundant fullness and peaceful calm",
        "cultural_note": "From 'dap' (full) and 'lin' (calm/smooth); denotes a peaceful and spiritually satisfied life."
    },
    {
        "name": "Shaphrang",
        "gender": "male",
        "meaning": "Pioneer / Leader marching in the vanguard",
        "cultural_note": "Bestowed upon boys destined to show courage, lead community movements, and stand in front for truth."
    },
    {
        "name": "Wanphrang",
        "gender": "male",
        "meaning": "Arriving with foremost excellence and leadership",
        "cultural_note": "Auspicious name celebrating a child brought into the world to excel and bring honour to the clan."
    },
    {
        "name": "Pynshngain",
        "gender": "male",
        "meaning": "Bringer of peace, comfort, and security",
        "cultural_note": "Rooted in 'shngain' (safe/secure); given to sons whose presence provides comforting shelter to the domestic hearth."
    },
    {
        "name": "Jingmut",
        "gender": "male",
        "meaning": "Purpose, intellect, thought, and noble intention",
        "cultural_note": "Signifies a person guided by deliberate discernment, righteous purpose, and clarity of mind."
    },
    {
        "name": "Bantei",
        "gender": "male",
        "meaning": "Master builder / One who constructs",
        "cultural_note": "Derived from 'tei' (to build); symbolizes building the home, clan honour, and society."
    },
    {
        "name": "Sngewbha",
        "gender": "unisex",
        "meaning": "Joy, contentment, goodwill, and delight",
        "cultural_note": "One of the most beloved Khasi moral names, expressing universal hospitality, graciousness, and cheerfulness."
    },
    {
        "name": "Lariti",
        "gender": "female",
        "meaning": "Gentle grace / Delicate sweetness of nature",
        "cultural_note": "Bestowed upon daughters representing gentle elegance, affectionate hospitality, and refined speech."
    },
    {
        "name": "Donbok",
        "gender": "male",
        "meaning": "Blessed with good fortune and auspicious luck",
        "cultural_note": "From 'don' (possess) and 'bok' (blessing/fortune); invokes divine favour and prosperity."
    },
    {
        "name": "Mawkordor",
        "gender": "unisex",
        "meaning": "Precious jewel / Priceless gemstone",
        "cultural_note": "From 'maw' (stone) and 'kordor' (precious); expresses that the child is more valuable than rare diamonds."
    },
    {
        "name": "Pynbiang",
        "gender": "male",
        "meaning": "One who fulfills and makes everything sufficient",
        "cultural_note": "Derived from 'biang' (complete/enough); a child whose birth completes the joy of the maternal family."
    },
    {
        "name": "Khrawbok",
        "gender": "male",
        "meaning": "Endowed with immense fortune and great blessings",
        "cultural_note": "Given to sons destined for expansive achievements and prosperous blessings in life."
    },
    {
        "name": "Kmen",
        "gender": "unisex",
        "meaning": "Rejoicing / Pure joy and gladness",
        "cultural_note": "A short, radiant name expressing unclouded happiness and thanksgiving to U Blei."
    },
    {
        "name": "Kyrshan",
        "gender": "male",
        "meaning": "Support / Pillar of endurance and strength",
        "cultural_note": "From 'kyrshan' (to support/uphold); symbolizes unshakeable familial endurance and dependability."
    },
    {
        "name": "Teibor",
        "gender": "male",
        "meaning": "Strength, power, and enduring resilience",
        "cultural_note": "Rooted in 'bor' (power/vitality); invokes moral fortitude and physical resilience."
    },
    {
        "name": "Phyrnai",
        "gender": "female",
        "meaning": "Radiant brilliance / Shining luminous light",
        "cultural_note": "Celebrates maternal brilliance and clarity of heart; reflects the dazzling beauty of morning sunlight."
    },
    {
        "name": "Badap",
        "gender": "female",
        "meaning": "Full of grace, abundance, and completion",
        "cultural_note": "Given to daughters who bring wholeness, domestic prosperity, and peace to the matrilineal home."
    },
    {
        "name": "Banylla",
        "gender": "female",
        "meaning": "Pure, unsullied, and sweet-natured",
        "cultural_note": "A poetic Khasi virtue name representing innocent moral purity and sincerity."
    },
    {
        "name": "Deilin",
        "gender": "female",
        "meaning": "Gentle ripple of tranquil water",
        "cultural_note": "Symbolizes serene poise, grace, and steady emotional peace within the family."
    },
    {
        "name": "Hunlang",
        "gender": "female",
        "meaning": "Collective contentment / Harmonious peace",
        "cultural_note": "Derived from 'hun' (content) and 'lang' (together); signifies unanimous clan harmony and happiness."
    },
    {
        "name": "Kynsai",
        "gender": "unisex",
        "meaning": "Choice flower / Most exquisite and selected",
        "cultural_note": "Bestowed to express that the child is the treasured, chosen jewel of the hearth."
    },
    {
        "name": "Maphi",
        "gender": "female",
        "meaning": "Gentle, forgiving, and merciful heart",
        "cultural_note": "Related to 'map' (forgive); represents benevolent kindness, patience, and warmth."
    },
    {
        "name": "Nylla",
        "gender": "female",
        "meaning": "Sweetness, innocence, and delicate purity",
        "cultural_note": "Traditional feminine name evoking the fresh blossoms of highland mountain orchards."
    },
    {
        "name": "Pynsuk",
        "gender": "unisex",
        "meaning": "Bringer of eternal peace and reconciliation",
        "cultural_note": "From 'pyn-' (causative) and 'suk' (peace); bestowed to foster lifelong serenity and mutual affection."
    },
    {
        "name": "Rishan",
        "gender": "male",
        "meaning": "Pillar of truth and upright dignity",
        "cultural_note": "Rooted in 'shan' (lean upon / support); represents moral uprightness and staunch integrity."
    },
    {
        "name": "Theikordor",
        "gender": "female",
        "meaning": "Measure of priceless worth and honour",
        "cultural_note": "Given to beloved daughters representing the high value and dignity of the matrilineal kur."
    },
    {
        "name": "Wandashisha",
        "gender": "female",
        "meaning": "Arrived with pure, unvarnished truth",
        "cultural_note": "From 'wan' (come) and 'shisha' (true); one of the most classic Khasi names testifying to divine truth."
    },
    {
        "name": "Balawan",
        "gender": "female",
        "meaning": "She who is brought by divine grace",
        "cultural_note": "Expresses gratitude for a long-awaited daughter born into the clan lineage."
    },
    {
        "name": "Ibadahun",
        "gender": "female",
        "meaning": "Loving heart that brings total contentment",
        "cultural_note": "Combines 'ieit' (love) and 'hun' (satisfy); represents warm maternal affection."
    },
    {
        "name": "Rikynti",
        "gender": "unisex",
        "meaning": "Sacred ancestral inheritance / Land held in trust",
        "cultural_note": "Reflects the sacred concept of Ri-Kynti (freehold clan land); reminds the bearer of custody over mother earth."
    },
    {
        "name": "Pynhok",
        "gender": "male",
        "meaning": "Upholder and promoter of divine righteousness",
        "cultural_note": "From 'hok' (justice/righteousness); ties directly to the first Khasi moral pillar 'Tip-Briew Tip-Hok'."
    },
    {
        "name": "Bhalang",
        "gender": "male",
        "meaning": "Common welfare / Goodness shared with all",
        "cultural_note": "Signifies civic altruism, community spirit, and working for the universal benefit of society."
    },
    {
        "name": "Kordor",
        "gender": "unisex",
        "meaning": "Precious / High worth and venerated dignity",
        "cultural_note": "Short, eloquent name celebrating the irreplaceable value of human life."
    },
    {
        "name": "Pahsyntiew",
        "gender": "female",
        "meaning": "She who entices with radiant blossoms",
        "cultural_note": "Legendary name of the mythological maiden Ka Pahsyntiew who emerged from the cave at Marngar to found the Khyrim/Mylliem dynasties."
    },
    {
        "name": "Tirot",
        "gender": "male",
        "meaning": "Steadfast, patient, and unshakeable in battle",
        "cultural_note": "Immortalized by U Tirot Sing Syiem, hero of Khasi national resistance against colonial subjugation."
    },
    {
        "name": "Wickliffe",
        "gender": "male",
        "meaning": "Courageous independence and visionary spirit",
        "cultural_note": "Borne by legendary Khasi visionary and freedom defender Wickliffe Syiem, founder of early constitutional rights."
    },
    {
        "name": "Sibcharan",
        "gender": "male",
        "meaning": "Devotee of virtue and indigenous sacred heritage",
        "cultural_note": "Associated with U Sib Charan Roy, founder of Seng Khasi literature and defender of ancestral faith."
    },
    {
        "name": "Soso",
        "gender": "male",
        "meaning": "Melodious bard / Poetic visionary",
        "cultural_note": "Immortalized by U Soso Tham (1873-1940), the national poet laureate of the Khasi language."
    },
    {
        "name": "Jeebon",
        "gender": "male",
        "meaning": "Life-giver and pioneering father of modern progress",
        "cultural_note": "Borne by Babu Jeebon Roy (1838-1903), father of modern Khasi literature, industry, and enterprise."
    },
    {
        "name": "Hajom",
        "gender": "male",
        "meaning": "Reformer / Illumination of brotherhood",
        "cultural_note": "Borne by U Hajom Kissor Singh, co-compiler of the 1920 Dictionary and founder of the Unitarian faith in Meghalaya."
    },
    {
        "name": "Dohory",
        "gender": "male",
        "meaning": "Noble counselor / Wise magistrate",
        "cultural_note": "Borne by Rai Sahib Dohory Ropmay, pioneer Khasi scholar and lexicographer."
    },
    {
        "name": "Ka Sngi",
        "gender": "female",
        "meaning": "Born on Sunday / Celestial Sun Maiden",
        "cultural_note": "Traditional market day name given to girls born on market day or Sunday, invoking the sun's life-giving light."
    },
    {
        "name": "U Hat",
        "gender": "male",
        "meaning": "Born on the historic Weekly Market Day",
        "cultural_note": "Traditional Khasi market-day naming custom celebrating vibrant community commerce and community gathering."
    },
    {
        "name": "Ka Iew",
        "gender": "female",
        "meaning": "Born on the Grand Market Day (Ka Iewduh)",
        "cultural_note": "Honours the great market day of the hills, wishing the child prosperity and abundant trade."
    },
    {
        "name": "Ka Musiang",
        "gender": "female",
        "meaning": "Born on Musiang Day (Pnar eight-day market cycle)",
        "cultural_note": "Ancient Pnar market-day name honouring the primary trading fair of Jowai and the Jaintia kingdom."
    },
    {
        "name": "U Muchai",
        "gender": "male",
        "meaning": "Born on Muchai Day (Pnar sacred market day)",
        "cultural_note": "Pnar market day name associated with ancient state festivals and community dances."
    },
    {
        "name": "Jingkmen",
        "gender": "unisex",
        "meaning": "Wellspring of festive rejoicing and delight",
        "cultural_note": "Celebrates a birth that brings renewed hope, smiles, and laughter to the domestic fireplace."
    },
    {
        "name": "Pynrap",
        "gender": "male",
        "meaning": "He who adds blessing unto blessing",
        "cultural_note": "Bestowed to express that each child adds another precious layer to the strength of the matrilineal hearth."
    },
    {
        "name": "Rikynthei",
        "gender": "female",
        "meaning": "Daughter of the sacred land and maternal clan",
        "cultural_note": "From 'ri' (land/preserve) and 'kynthei' (woman); highlights the central status of women as custodians of clan heritage."
    },
    {
        "name": "Tip-Blei",
        "gender": "unisex",
        "meaning": "One who knows and walks in the presence of God",
        "cultural_note": "Directly derived from the sacred Khasi motto 'Tip-Briew Tip-Blei' (Know Man and Know God)."
    }
]

def list_clans() -> List[Dict[str, Any]]:
    """Return all catalogued Khasi, Pnar, War, Bhoi, and Maram clans."""
    return CLANS

def get_clan(name: str) -> Optional[Dict[str, Any]]:
    """Lookup clan by name or branch."""
    q = name.lower().strip()
    for c in CLANS:
        if q in c["clan_name"].lower() or any(q in b.lower() for b in c["branches"]):
            return c
    return None

def search_clans(query: str) -> List[Dict[str, Any]]:
    """Search clans by keyword in name, branches, category, or historical role."""
    q = query.lower().strip()
    return [c for c in CLANS if (
        q in c["clan_name"].lower() or
        any(q in b.lower() for b in c["branches"]) or
        q in c["category"].lower() or
        q in c["historical_role"].lower()
    )]

def total_clans() -> int:
    """Return total count of catalogued clans."""
    return len(CLANS)

def list_names(gender: Optional[str] = None) -> List[Dict[str, Any]]:
    """Return catalogued Khasi traditional given names, optionally filtered by gender ('male', 'female', 'unisex')."""
    if not gender:
        return TRADITIONAL_NAMES
    g = gender.lower().strip()
    return [n for n in TRADITIONAL_NAMES if n["gender"] == g or n["gender"] == "unisex"]

def get_name(name: str) -> Optional[Dict[str, Any]]:
    """Lookup a traditional Khasi given name by name."""
    q = name.lower().strip()
    for n in TRADITIONAL_NAMES:
        if n["name"].lower() == q or q in n["name"].lower():
            return n
    return None

def search_names(query: str) -> List[Dict[str, Any]]:
    """Search traditional names by keyword in name, meaning, or cultural note."""
    q = query.lower().strip()
    return [n for n in TRADITIONAL_NAMES if (
        q in n["name"].lower() or
        q in n["meaning"].lower() or
        q in n["cultural_note"].lower()
    )]

def total_names() -> int:
    """Return total count of traditional names."""
    return len(TRADITIONAL_NAMES)
