# -*- coding: utf-8 -*-
"""
Khasi Classical Grammar Rules Engine (Ka Riti Ktien Khasi).
===========================================================

Comprehensive programmatic catalog and validation engine of 50+ classical and
standard Khasi grammatical rules, derived from historical treatises including:
- Rev. H. Roberts, 'A Grammar of the Khassi Language' (1891)
- Rev. Thomas Jones, 'An Introduction to the Khasia Language' (1841)
- Babu Jeebon Roy, 'Ka Niam Jong Ki Khasi' (1897)
- Dr. R. S. Lyngdoh & Khasi Authors Society Standard Orthography

Categories:
1. Article & Nominal Agreement (Rules AGR-01 to AGR-06)
2. Tense, Aspect, Mood & Verbal Auxiliaries (Rules TAM-01 to TAM-12)
3. Case Marking & Prepositional Syntax (Rules CAS-01 to CAS-08)
4. Derivational & Inversive Morphology (Rules DER-01 to DER-10)
5. Clause Linking, Conditionals & Subordination (Rules CLA-01 to CLA-08)
6. Expressives, Enclitics & Echo Phonaesthetics (Rules EXP-01 to EXP-06)
"""

from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass


@dataclass
class GrammarRule:
    """Represents a formal grammatical rule of the Khasi language."""
    id: str
    name: str
    category: str
    formula: str
    description: str
    khasi_examples: List[str]
    english_translations: List[str]
    source_reference: str


CLASSICAL_GRAMMAR_RULES: List[GrammarRule] = [
    # -------------------------------------------------------------
    # 1. ARTICLE & NOMINAL AGREEMENT (AGR)
    # -------------------------------------------------------------
    GrammarRule(
        id="AGR-01",
        name="Mandatory Article Prefixation",
        category="Nominal Agreement",
        formula="[Article: u / ka / i / ki] + [Noun Stem]",
        description="Every common and proper noun in Khasi must be preceded by an article indicating gender, number, and social intimacy. Articles are never dropped in standard discourse.",
        khasi_examples=["u kpa (the father)", "ka kmie (the mother)", "i khunlung (the baby)", "ki briew (the people)"],
        english_translations=["the father", "the mother", "the dear infant", "the people"],
        source_reference="Roberts (1891) §12-16; Thomas Jones (1841) §4"
    ),
    GrammarRule(
        id="AGR-02",
        name="Subject-Verb Pronoun Copy Agreement",
        category="Nominal Agreement",
        formula="[Subject NP: Art + Noun] + [Copy Pronoun] + [TAM] + [Verb]",
        description="When a full noun phrase functions as subject, an agreement clitic/pronoun copying the gender and number of the noun phrase must immediately precede the verb predicate.",
        khasi_examples=["U kpa u la wan", "Ka kmie ka dang trei", "Ki khynnah ki la rwai"],
        english_translations=["The father (he) came", "The mother (she) is working", "The children (they) sang"],
        source_reference="Roberts (1891) §148; Lyngdoh (1983)"
    ),
    GrammarRule(
        id="AGR-03",
        name="Diminutive and Affectionate Gender 'I'",
        category="Nominal Agreement",
        formula="i + [Noun Stem]",
        description="The diminutive article 'i' expresses small physical size, delicacy, tenderness, and kinship affection regardless of biological sex.",
        khasi_examples=["i mei (my dear mother)", "i pa (my dear father)", "i sim (a little bird)", "i khun (a beloved child)"],
        english_translations=["beloved mother", "beloved father", "little bird", "dear little child"],
        source_reference="Thomas Jones (1841) §5; Roberts (1891) §15"
    ),
    GrammarRule(
        id="AGR-04",
        name="Universal Common Plural Article 'Ki'",
        category="Nominal Agreement",
        formula="ki + [Noun Stem / Adjective Stem]",
        description="Gender distinctions (masculine 'u' and feminine 'ka') are neutralized in the plural, coalescing into the universal plural article 'ki'.",
        khasi_examples=["ki kpa (fathers)", "ki kmie (mothers)", "ki maw (stones)", "ki lum (mountains)"],
        english_translations=["fathers", "mothers", "stones", "mountains"],
        source_reference="Roberts (1891) §16"
    ),
    GrammarRule(
        id="AGR-05",
        name="Post-Nominal Attributive Adjective Placement",
        category="Nominal Agreement",
        formula="[Art + Noun] + [ba- + Adjective Stem]",
        description="Qualifying adjectives follow their governing noun and must take the subordinating attributive prefix 'ba-'.",
        khasi_examples=["u briew babha", "ka kot bakordor", "ki maw bakhraw"],
        english_translations=["the good man", "the precious book", "the great stones"],
        source_reference="Roberts (1891) §154"
    ),
    GrammarRule(
        id="AGR-06",
        name="Demonstrative Postposition Agreement",
        category="Nominal Agreement",
        formula="[Art + Noun] + [Demonstrative: -ne / -to / -tai / -te]",
        description="Demonstratives attach as post-nominal enclitics or follow the noun matching in gender ('une', 'kane', 'ine', 'kine' for proximal; 'utai', 'katai', 'itai', 'kitai' for distal).",
        khasi_examples=["une u briew / u briew-ne (this man)", "kane ka sngi (this day)", "kitai ki lum (those mountains over there)"],
        english_translations=["this man", "this day", "those mountains yonder"],
        source_reference="Thomas Jones (1841) §14; Roberts (1891) §170"
    ),

    # -------------------------------------------------------------
    # 2. TENSE, ASPECT, MOOD & AUXILIARIES (TAM)
    # -------------------------------------------------------------
    GrammarRule(
        id="TAM-01",
        name="Aorist Present / Stative Unmarked Form",
        category="Tense-Aspect-Mood",
        formula="[Pronoun] + [Root Verb]",
        description="The bare verb stem without tense particles signifies present tense, gnomic truth, or habitual state.",
        khasi_examples=["Nga bam", "U leit", "Ka rwai"],
        english_translations=["I eat", "He goes", "She sings"],
        source_reference="Thomas Jones (1841) §20; Roberts (1891) §71"
    ),
    GrammarRule(
        id="TAM-02",
        name="Anterior Past Particle 'La'",
        category="Tense-Aspect-Mood",
        formula="[Pronoun] + la + [Root Verb]",
        description="The preverbal auxiliary 'la' marks completed past tense or perfective event.",
        khasi_examples=["Nga la bam", "U la wan", "Ki la dep"],
        english_translations=["I ate / have eaten", "He came / has come", "They finished"],
        source_reference="Roberts (1891) §72"
    ),
    GrammarRule(
        id="TAM-03",
        name="Prospective Future Clitic 'Yn / -n'",
        category="Tense-Aspect-Mood",
        formula="[Pronoun + n] + [Root Verb]",
        description="Future tense is expressed by the modal clitic 'yn', which fuses with subject pronouns ('ngan', 'ngin', 'phin', 'un', 'kan', 'in', 'kin').",
        khasi_examples=["Ngan leit", "Kan wan", "Kin pule"],
        english_translations=["I will go", "She will come", "They will study"],
        source_reference="Thomas Jones (1841) §22; Roberts (1891) §73"
    ),
    GrammarRule(
        id="TAM-04",
        name="Progressive / Durative Aspect 'Dang'",
        category="Tense-Aspect-Mood",
        formula="[Pronoun] + dang + [Root Verb]",
        description="The particle 'dang' expresses ongoing continuous action or durative present ('is still doing').",
        khasi_examples=["Nga dang bam", "U dang trei", "Ka dang pule"],
        english_translations=["I am (still) eating", "He is working", "She is reading"],
        source_reference="Roberts (1891) §74"
    ),
    GrammarRule(
        id="TAM-05",
        name="Completive Perfective Aspect 'Dep'",
        category="Tense-Aspect-Mood",
        formula="[Pronoun] + la dep + [Root Verb]",
        description="The auxiliary 'dep' (to finish) marks absolute completion of an action prior to reference time.",
        khasi_examples=["Nga la dep bam", "Ki la dep thoh", "U la dep trei"],
        english_translations=["I have finished eating", "They have finished writing", "He has finished working"],
        source_reference="Roberts (1891) §75"
    ),
    GrammarRule(
        id="TAM-06",
        name="Habitual Aspect 'Ju'",
        category="Tense-Aspect-Mood",
        formula="[Pronoun] + ju + [Root Verb]",
        description="'Ju' marks customary or habitual actions ('accustomed to', 'usually'). In the past ('la ju'), it denotes past habit ('used to').",
        khasi_examples=["Nga ju leit", "U ju kren kumta", "Nga la ju shong ha Sohra"],
        english_translations=["I usually go", "He usually speaks so", "I used to reside in Sohra"],
        source_reference="Roberts (1891) §76"
    ),
    GrammarRule(
        id="TAM-07",
        name="Negative Past Auxiliary 'Shym'",
        category="Tense-Aspect-Mood",
        formula="[Neg-Pronoun: um / ngam / phim] + shym + (la) + [Root Verb]",
        description="In classical Khasi syntax, the auxiliary 'shym' specifically negates past actions ('did not'), contracting with the pronoun.",
        khasi_examples=["U'm shym la wan", "Nga'm shym la tip", "Ki'm shym la ïohi"],
        english_translations=["He did not come", "I did not know", "They did not see"],
        source_reference="Roberts (1891) §73; Thomas Jones (1841) §25"
    ),
    GrammarRule(
        id="TAM-08",
        name="Negative Preterite Particle 'Khlem'",
        category="Tense-Aspect-Mood",
        formula="[Pronoun] + khlem + [Root Verb]",
        description="'Khlem' signifies past negation without contracted pronoun ('without having done' / 'did not').",
        khasi_examples=["U khlem wan", "Nga khlem bam", "Ki khlem tip"],
        english_translations=["He did not come", "I did not eat", "They did not know"],
        source_reference="Roberts (1891) §74"
    ),
    GrammarRule(
        id="TAM-09",
        name="Potential Modal 'Lah Ban'",
        category="Tense-Aspect-Mood",
        formula="[Pronoun] + lah ban + [Root Verb]",
        description="'Lah' conveys physical ability, cognitive capacity, or circumstantial possibility ('can / able to').",
        khasi_examples=["Nga lah ban leh", "U lah ban kren Khasi", "Phi lah ban wan"],
        english_translations=["I can do it", "He can speak Khasi", "You can come"],
        source_reference="Roberts (1891) §80"
    ),
    GrammarRule(
        id="TAM-10",
        name="Deontic Obligation Modal 'Dei Ban'",
        category="Tense-Aspect-Mood",
        formula="[Pronoun] + dei ban + [Root Verb]",
        description="'Dei ban' expresses moral duty, social obligation, necessity, or propriety ('must / ought to / should').",
        khasi_examples=["Ngi dei ban burom ïa ki tymmen", "Phi dei ban leit", "U dei ban sngap"],
        english_translations=["We ought to respect the elders", "You must go", "He should listen"],
        source_reference="Roberts (1891) §81"
    ),
    GrammarRule(
        id="TAM-11",
        name="Desiderative Volition Modal 'Kwah Ban'",
        category="Tense-Aspect-Mood",
        formula="[Pronoun] + kwah ban + [Root Verb]",
        description="'Kwah ban' indicates active desire, intention, or will to perform an action ('want to / wish to').",
        khasi_examples=["Nga kwah ban pule", "U kwah ban thiah", "Ki kwah ban ïohi"],
        english_translations=["I want to study", "He wishes to sleep", "They want to see"],
        source_reference="Roberts (1891) §82"
    ),
    GrammarRule(
        id="TAM-12",
        name="Prohibitive Negative Imperative 'Wat'",
        category="Tense-Aspect-Mood",
        formula="Wat + [Root Verb] + (!)",
        description="The particle 'wat' forms negative imperatives and strict prohibitions ('do not! / cease from!').",
        khasi_examples=["Wat leit!", "Wat shepteng!", "Wat kren lamwir!"],
        english_translations=["Do not go!", "Do not fear!", "Do not speak nonsense!"],
        source_reference="Thomas Jones (1841) §28; Roberts (1891) §84"
    ),

    # -------------------------------------------------------------
    # 3. CASE MARKING & PREPOSITIONAL SYNTAX (CAS)
    # -------------------------------------------------------------
    GrammarRule(
        id="CAS-01",
        name="Accusative Direct Object Marking with 'Ïa'",
        category="Case Marking",
        formula="[Verb] + ïa + [Object NP]",
        description="Definite, human, and prominent direct objects must be introduced by the accusative/dative case marker 'ïa'.",
        khasi_examples=["Nga ieit ïa ka kmie", "U la ïohi ïa u khla", "Pynshai ïa kane"],
        english_translations=["I love my mother", "He saw the tiger", "Clarify this"],
        source_reference="Roberts (1891) §138, §149"
    ),
    GrammarRule(
        id="CAS-02",
        name="Locative Inessive Case 'Ha'",
        category="Case Marking",
        formula="ha + [Location / Time]",
        description="'Ha' marks spatial inclusion ('in / at') or temporal location ('at / on').",
        khasi_examples=["ha ïing (at home)", "ha lum (on the mountain)", "ha ka step (in the morning)"],
        english_translations=["at home", "on the mountain", "in the morning"],
        source_reference="Roberts (1891) §150"
    ),
    GrammarRule(
        id="CAS-03",
        name="Allative Directional Case 'Sha'",
        category="Case Marking",
        formula="sha + [Destination / Direction]",
        description="'Sha' marks movement towards a destination or spatial direction ('to / toward / into').",
        khasi_examples=["sha Sohra (to Sohra)", "sha ïing (towards home)", "sha bneng (to heaven)"],
        english_translations=["to Sohra", "homeward", "to heaven"],
        source_reference="Roberts (1891) §150"
    ),
    GrammarRule(
        id="CAS-04",
        name="Ablative Origin Case 'Na'",
        category="Case Marking",
        formula="na + [Source / Origin]",
        description="'Na' marks source, point of origin, or departure ('from / out of').",
        khasi_examples=["na Shillong (from Shillong)", "na ka dohnud (from the heart)", "na liewlep (out of the pit)"],
        english_translations=["from Shillong", "from the heart", "out of the pit"],
        source_reference="Thomas Jones (1841) §32; Roberts (1891) §150"
    ),
    GrammarRule(
        id="CAS-05",
        name="Instrumental Case 'Da'",
        category="Case Marking",
        formula="da + [Instrument / Means / Material]",
        description="'Da' indicates the tool, medium, manner, or instrument by which an action is executed ('with / by means of / through').",
        khasi_examples=["da ka tari (with a knife)", "da ka jingshai (through light)", "da ka bor (by strength)"],
        english_translations=["with a knife", "through the light", "by force"],
        source_reference="Roberts (1891) §150"
    ),
    GrammarRule(
        id="CAS-06",
        name="Comitative / Associative Case 'Bad'",
        category="Case Marking",
        formula="[NP1] + bad + [NP2]",
        description="'Bad' marks comitative accompaniment ('with') as well as coordinate conjunction ('and').",
        khasi_examples=["u kpa bad ka kmie", "u wan bad nga", "u sngap bad u sngewthuh"],
        english_translations=["the father and the mother", "he came with me", "he listens and understands"],
        source_reference="Roberts (1891) §203"
    ),
    GrammarRule(
        id="CAS-07",
        name="Genitive Possessive Case 'Jong'",
        category="Case Marking",
        formula="[Possessed NP] + jong + [Possessor NP]",
        description="'Jong' signifies possession, belonging, and origin ('of / belonging to'). Can contract into clitic form in colloquial registers.",
        khasi_examples=["ka ïing jong u kpa", "ka ktien jong ka ri", "u khun jong nga"],
        english_translations=["the house of the father", "the language of the country", "my son"],
        source_reference="Thomas Jones (1841) §8; Roberts (1891) §139"
    ),
    GrammarRule(
        id="CAS-08",
        name="Purposive Benefactive 'Na Ka Bynta'",
        category="Case Marking",
        formula="na ka bynta (jong) + [Beneficiary / Purpose]",
        description="'Na ka bynta' marks purpose, intentionality, or benefaction ('for the sake of / on behalf of').",
        khasi_examples=["na ka bynta jong phi", "na ka bynta ka hok", "na ka bynta ban hikai"],
        english_translations=["for your sake", "for the sake of truth/righteousness", "for the purpose of teaching"],
        source_reference="Roberts (1891) §150"
    ),

    # -------------------------------------------------------------
    # 4. DERIVATIONAL & INVERSIVE MORPHOLOGY (DER)
    # -------------------------------------------------------------
    GrammarRule(
        id="DER-01",
        name="Abstract Nominalizer Prefix 'Jing-'",
        category="Derivational Morphology",
        formula="jing- + [Verb / Adjective Stem]",
        description="The prefix 'jing-' productive derives abstract nouns, qualities, and concrete nominalizations from verbal and adjectival roots.",
        khasi_examples=["jingshai (light / clarity from shai 'clear')", "jingieit (love from ieit 'to love')", "jingstad (wisdom from stad 'wise')"],
        english_translations=["light / clarity", "love / affection", "wisdom / knowledge"],
        source_reference="Roberts (1891) §140; Thomas Jones (1841) §10"
    ),
    GrammarRule(
        id="DER-02",
        name="Causative Verb Derivation 'Pyn-'",
        category="Derivational Morphology",
        formula="pyn- + [Verb / Adjective Stem]",
        description="'Pyn-' converts intransitive verbs or adjectives into causative transitive verbs ('to cause to do / to make into').",
        khasi_examples=["pynim (to revive / save from im 'to live')", "pynshai (to illuminate from shai 'clear')", "pynkordor (to enrich from kordor 'precious')"],
        english_translations=["to revive / make live", "to illuminate / make clear", "to enrich / render precious"],
        source_reference="Roberts (1891) §63; Thomas Jones (1841) §18"
    ),
    GrammarRule(
        id="DER-03",
        name="Agentive Personal Noun Derivation 'Nong-'",
        category="Derivational Morphology",
        formula="nong- + [Verb / Noun Stem]",
        description="'Nong-' derives nouns denoting agents, actors, professions, or inhabitants ('one who does / practitioner of').",
        khasi_examples=["nonghikai (teacher from hikai 'teach')", "nongthoh (writer from thoh 'write')", "nongrep (farmer from rep 'cultivate')"],
        english_translations=["teacher", "writer / scribe", "farmer / cultivator"],
        source_reference="Roberts (1891) §141"
    ),
    GrammarRule(
        id="DER-04",
        name="Experiential Sensory Prefix 'Sngew-'",
        category="Derivational Morphology",
        formula="sngew- + [Adjective / Verb Stem]",
        description="'Sngew-' derives verbs of sensory perception, emotional feeling, and psychological resonance ('to perceive / feel').",
        khasi_examples=["sngewbha (to feel pleased / rejoice from bha 'good')", "sngewsih (to feel sad / sorrow from sih 'bad')", "sngewlem (to sympathize from lem 'along/together')"],
        english_translations=["to feel pleased / glad", "to feel grieved / sorrowful", "to sympathize / commiserate"],
        source_reference="Roberts (1891) §65"
    ),
    GrammarRule(
        id="DER-05",
        name="Reciprocal Collaborative Prefix 'Ïa-'",
        category="Derivational Morphology",
        formula="ïa- + [Verb Stem]",
        description="'Ïa-' derives reciprocal or collective actions executed mutually by multiple participants ('to do together / mutually').",
        khasi_examples=["ïaleh (to compete / struggle from leh 'do')", "ïakren (to converse from kren 'speak')", "ïasyllok (to take counsel together)"],
        english_translations=["to compete / fight mutually", "to converse / discuss together", "to deliberate mutually"],
        source_reference="Roberts (1891) §66"
    ),
    GrammarRule(
        id="DER-06",
        name="Attributive Adjectival Prefix 'Ba-'",
        category="Derivational Morphology",
        formula="ba- + [Adjective / Verb Stem]",
        description="'Ba-' marks stative roots as qualifying adjectives when functioning attributively.",
        khasi_examples=["bashisha (true / genuine from shisha 'real')", "bakhraw (great / noble from khraw 'big')", "bathiang (sweet from thiang 'sweet')"],
        english_translations=["true / genuine", "great / noble", "sweet"],
        source_reference="Thomas Jones (1841) §11"
    ),
    GrammarRule(
        id="DER-07",
        name="Kinship & Peer Prefix 'Para-'",
        category="Derivational Morphology",
        formula="para- + [Noun Stem]",
        description="'Para-' forms nouns denoting fraternal relationships, co-members, companions, and peers.",
        khasi_examples=["paramarjan (neighbor from marjan 'boundary')", "paralok (friend / companion from lok 'companion')", "parabynriew (fellow human from briew 'person')"],
        english_translations=["neighbor", "companion / friend", "fellow human being"],
        source_reference="Roberts (1891) §142"
    ),
    GrammarRule(
        id="DER-08",
        name="Single Unit / Measure Prefix 'Shi-'",
        category="Derivational Morphology",
        formula="shi- + [Noun / Classifer Stem]",
        description="'Shi-' (from shiyi 'one') fuses with nouns and classifiers to express a single whole unit, time period, or full measure.",
        khasi_examples=["shisngi (a whole day from sngi 'day')", "shikyntien (one utterance / single word from kyntien 'word')", "shityllup (entire / throughout)"],
        english_translations=["one full day", "a single utterance / word", "entire / throughout"],
        source_reference="Thomas Jones (1841) §15; Roberts (1891) §52"
    ),
    GrammarRule(
        id="DER-09",
        name="Distributive & Successive Prefix 'Mar-'",
        category="Derivational Morphology",
        formula="mar- + [Numeral / Adjective Stem]",
        description="'Mar-' forms distributive, solitary, or sequential qualifications ('each by each / respectively').",
        khasi_examples=["marwei (alone / by oneself from wei 'one')", "marbud (successively / following one another from bud 'follow')", "markylliang (in mutual exchange from kylliang 'exchange')"],
        english_translations=["alone / solitary", "in succession / one after another", "in mutual turn / reciprocal exchange"],
        source_reference="Roberts (1891) §53"
    ),
    GrammarRule(
        id="DER-10",
        name="Inversive / Transformative Prefix 'Kylla-'",
        category="Derivational Morphology",
        formula="kylla- + [Noun / Verb Stem]",
        description="'Kylla-' expresses radical transformation, inversion of state, or turning around ('to become / turn into').",
        khasi_examples=["kyllalong (to transform / metamorphose from long 'be')", "kyllaba (inverting / turning from ba 'be')", "kyllang (whirlwind / cyclical storm)"],
        english_translations=["to metamorphose / transform", "turning / inverting", "whirlwind"],
        source_reference="Roberts (1891) §68"
    ),

    # -------------------------------------------------------------
    # 5. CLAUSE LINKING, CONDITIONALS & SUBORDINATION (CLA)
    # -------------------------------------------------------------
    GrammarRule(
        id="CLA-01",
        name="Real Conditional with 'Lada'",
        category="Complex Syntax",
        formula="Lada + [Protasis Clause], [Apodosis Clause]",
        description="Real and hypothetical conditions are introduced by 'lada' (if). The consequence clause typically employs future prospective clitic '-n'.",
        khasi_examples=["Lada phi wan, ngan leit bad phi", "Lada u kloi, un jop", "Lada slap, ngim lah ban trei"],
        english_translations=["If you come, I will go with you", "If he is swift, he will win", "If it rains, we cannot work"],
        source_reference="Roberts (1891) §204"
    ),
    GrammarRule(
        id="CLA-02",
        name="Concessive Subordination with 'Wat La'",
        category="Complex Syntax",
        formula="Wat la + [Concessive Clause], pynban + [Main Clause]",
        description="Concessive relations ('although / even though') are marked by 'wat la', often correlated with 'pynban' (yet / nevertheless) in the matrix clause.",
        khasi_examples=["Wat la u la tlot, pynban u la jop", "Wat la ka long kaba eh, ngin pyrshang"],
        english_translations=["Although he was weak, nevertheless he won", "Although it is difficult, we will try"],
        source_reference="Roberts (1891) §205"
    ),
    GrammarRule(
        id="CLA-03",
        name="Causal Subordination with 'Namar Ba'",
        category="Complex Syntax",
        formula="[Main Clause] + namar ba + [Reason Clause]",
        description="'Namar ba' (because / since) introduces rationales, justifications, and causal explanations.",
        khasi_examples=["Nga la wan namar ba phi la khot", "U la jop namar ba u la minot"],
        english_translations=["I came because you called", "He succeeded because he was diligent"],
        source_reference="Thomas Jones (1841) §34; Roberts (1891) §204"
    ),
    GrammarRule(
        id="CLA-04",
        name="Simultaneous Temporal Subordination with 'Katba'",
        category="Complex Syntax",
        formula="Katba + [Subordinate Durative Clause], [Main Clause]",
        description="'Katba' marks temporal simultaneity ('while / as / during the time that').",
        khasi_examples=["Katba nga dang bam, u la wan rung", "Katba ka dang rwai, ki la sngap"],
        english_translations=["While I was eating, he entered", "While she was singing, they listened"],
        source_reference="Roberts (1891) §110, §204"
    ),
    GrammarRule(
        id="CLA-05",
        name="Prospective Temporal Subordination with 'Ynda'",
        category="Complex Syntax",
        formula="Ynda + [Prior Event Clause], sa + [Subsequent Clause]",
        description="'Ynda' marks chronological succession in future/general time ('when / after / as soon as'), correlated with adverbial 'sa' (then).",
        khasi_examples=["Ynda u la wan, ngin sa leit", "Ynda la shai ka sngi, ngin mih"],
        english_translations=["When he has arrived, then we shall depart", "As soon as day breaks, we will set out"],
        source_reference="Thomas Jones (1841) §33; Roberts (1891) §186"
    ),
    GrammarRule(
        id="CLA-06",
        name="Pronominal Relative Clause Formation",
        category="Complex Syntax",
        formula="[Head Noun: Art + Noun] + [Rel Pronoun: uba / kaba / iba / kiba] + [Clause]",
        description="Relative clauses agree with their antecedent head noun via portmanteau relative pronouns: 'uba' (masc), 'kaba' (fem), 'iba' (dim), 'kiba' (pl).",
        khasi_examples=["U briew uba wan mynhynnin", "Ka kot kaba phi la ai", "Ki khynnah kiba lehbha"],
        english_translations=["The man who came yesterday", "The book which you gave", "The children who do well"],
        source_reference="Roberts (1891) §171; Thomas Jones (1841) §16"
    ),
    GrammarRule(
        id="CLA-07",
        name="Adversative Passive with 'Shah'",
        category="Complex Syntax",
        formula="[Patient NP] + [Copy Pronoun] + shah + [Verb] + (ha + [Agent])",
        description="Khasi constructs an adversative passive using the verb 'shah' ('to undergo / endure / suffer'), typically for unfavorable events.",
        khasi_examples=["U ksew u la shah shoh ha u briew", "Ka ïing ka la shah thang"],
        english_translations=["The dog was beaten by the man", "The house was burned down"],
        source_reference="Roberts (1891) §71; Lyngdoh (1983)"
    ),
    GrammarRule(
        id="CLA-08",
        name="Comparative of Superiority with 'Kham... Ban Ïa'",
        category="Complex Syntax",
        formula="[Item 1] + [Copy Pronoun] + kham + [Adjective] + ban ïa + [Item 2]",
        description="Inequality comparison uses comparative adverb 'kham' (more) before the adjective and 'ban ïa' (than) before the standard of comparison.",
        khasi_examples=["U lum Shillong u kham jrong ban ïa u lum Sohpetbneng", "Kane ka kham bha ban ïa katai"],
        english_translations=["Shillong Peak is taller than Sohpetbneng Peak", "This is better than that"],
        source_reference="Roberts (1891) §155; Thomas Jones (1841) §12"
    ),

    # -------------------------------------------------------------
    # 6. ENCLITICS, EXPRESSIVES & PHONAESTHETICS (EXP)
    # -------------------------------------------------------------
    GrammarRule(
        id="EXP-01",
        name="Telic Departive Aspect Enclitic 'Noh'",
        category="Enclitics & Expressives",
        formula="[Verb] + noh",
        description="'Noh' marks departure away from the speaker, finality, or definitive departure ('away / off / completely done').",
        khasi_examples=["U la leit noh (He has departed away)", "Bam noh! (Eat it up completely!)", "Khie leit noh! (Go away!)"],
        english_translations=["He has gone away", "Eat it up completely!", "Go away!"],
        source_reference="Roberts (1891) §115"
    ),
    GrammarRule(
        id="EXP-02",
        name="Recreational / Leisurely Enclitic 'Kai'",
        category="Enclitics & Expressives",
        formula="[Verb] + kai",
        description="'Kai' signifies actions performed leisurely, for recreation, without serious consequence, or in vain.",
        khasi_examples=["U leit kai (He went for a stroll)", "Nga kren kai (I am just joking / speaking leisurely)", "Bam kai (eat a light snack)"],
        english_translations=["He went for a stroll", "I am just joking / speaking in jest", "eat a leisure snack"],
        source_reference="Roberts (1891) §115"
    ),
    GrammarRule(
        id="EXP-03",
        name="Exhaustive / Totalizing Enclitic 'Lut'",
        category="Enclitics & Expressives",
        formula="[Verb] + lut",
        description="'Lut' marks total exhaustiveness: every single object or participant has been completely encompassed by the verbal action.",
        khasi_examples=["Ki la bam lut (They ate everything completely)", "U la siew lut (He paid all debts in full)"],
        english_translations=["They ate everything completely", "He paid off all debts completely"],
        source_reference="Roberts (1891) §115"
    ),
    GrammarRule(
        id="EXP-04",
        name="Simultaneous Accompanying Enclitic 'Artad'",
        category="Enclitics & Expressives",
        formula="[Verb] + artad",
        description="'Artad' expresses performing an incidental secondary action alongside or in the course of the main action ('at the same time / along the way').",
        khasi_examples=["Shim artad ïa kane (Take this along at the same time)", "Wan artad bad u (Come along with him simultaneously)"],
        english_translations=["Take this along at the same time", "Come along together simultaneously"],
        source_reference="Roberts (1891) §115"
    ),
    GrammarRule(
        id="EXP-05",
        name="Polar Question Clitic 'Ne Em' and 'Hato'",
        category="Enclitics & Expressives",
        formula="[Hato] + [Clause] + [ne em?]",
        description="Yes/no questions are introduced by the initial question marker 'Hato' or tagged with the disjunctive particle 'ne em' ('or not?').",
        khasi_examples=["Hato phi la dep? (Have you finished?)", "Phi kwah ban wan ne em? (Do you want to come or not?)"],
        english_translations=["Have you finished?", "Do you want to come or not?"],
        source_reference="Thomas Jones (1841) §29; Roberts (1891) §122"
    ),
    GrammarRule(
        id="EXP-06",
        name="Echo Reduplication and Coupled Rhyme",
        category="Enclitics & Expressives",
        formula="[Base Word] + [Echo Rhyme / Alliteration]",
        description="Khasi features an immense system of phonaesthetic echo words (*Ki Ktien Kynnoh*) where a base word is paired with an alliterative counterpart to denote broad categories.",
        khasi_examples=["bam-ja bam-doh (feasting / full dining)", "ki kot ki sla (books and papers / documents)", "ka suk ka sain (peace and prosperity)"],
        english_translations=["feasting and dining", "books, records, and papers", "peace and social harmony"],
        source_reference="Roberts (1891) §118; Lyngdoh (1983)"
    ),
    # -------------------------------------------------------------
    # 7. NUMERAL CLASSIFIERS & SPECIFIERS (CLS)
    # -------------------------------------------------------------
    GrammarRule(
        id="CLS-01",
        name="Human Personal Numeral Classifier 'Ngut'",
        category="Numeral Classifiers",
        formula="[Numeral: ar / lai / saw...] + ngut + [ki + Human Noun]",
        description="Whenever counting human beings or rational persons, the personal classifier 'ngut' is grammatically mandatory between the cardinal number and the plural noun phrase.",
        khasi_examples=["ar ngut ki briew (two persons)", "lai ngut ki khun (three children)", "san ngut ki nonghikai (five teachers)"],
        english_translations=["two persons", "three children", "five teachers"],
        source_reference="Thomas Jones (1841) §15; Roberts (1891) §64"
    ),
    GrammarRule(
        id="CLS-02",
        name="Inanimate General Numeral Classifier 'Tylli'",
        category="Numeral Classifiers",
        formula="[Numeral] + tylli + [ki / Article + Inanimate Noun]",
        description="Inanimate objects, non-human entities, and general items require the classifier 'tylli' ('unit / whole piece') when enumerated.",
        khasi_examples=["lai tylli ki kot (three books)", "saw tylli ki shuki (four chairs)", "shitylli ka sngi (one whole day)"],
        english_translations=["three books", "four chairs", "one single day"],
        source_reference="Roberts (1891) §65"
    ),
    GrammarRule(
        id="CLS-03",
        name="Botanical Arboreal Classifier 'Tynrai'",
        category="Numeral Classifiers",
        formula="[Numeral] + tynrai + [ki + Tree / Plant]",
        description="Individual living trees, stems, and perennial plants are classified by 'tynrai' (root / living trunk).",
        khasi_examples=["ar tynrai ki dieng (two trees)", "san tynrai ki sohphlang (five tuber plants)"],
        english_translations=["two trees", "five tuber plants"],
        source_reference="Roberts (1891) §66; Lyngdoh (1983)"
    ),
    GrammarRule(
        id="CLS-04",
        name="Foliar and Planar Classifier 'Sla'",
        category="Numeral Classifiers",
        formula="[Numeral] + sla + [ki + Leaf / Sheet / Paper]",
        description="Leaves, thin broad sheets, sheets of paper, and foliage are enumerated with the vegetative classifier 'sla'.",
        khasi_examples=["ar sla ki sla-dieng (two tree leaves)", "lai sla ki kot-sada (three sheets of paper)"],
        english_translations=["two tree leaves", "three sheets of blank paper"],
        source_reference="Roberts (1891) §66"
    ),
    # -------------------------------------------------------------
    # 8. DISCOURSE PARTICLES, ASPECTUAL SANDHI & REDUPLICATION
    # -------------------------------------------------------------
    GrammarRule(
        id="DIS-01",
        name="Hortative and Polite Imperative Markers 'To' and 'Seh'",
        category="Discourse Particles",
        formula="[To] + [Verb Phrase] / [Verb Phrase] + [seh]",
        description="'To' initiates polite or formal hortative commands ('pray / do proceed to'), while 'seh' serves as an affectionate final pleader or softening particle.",
        khasi_examples=["To ngin duwai (Let us pray / come let us pray)", "Kren biang seh (Please speak again, won't you?)"],
        english_translations=["Come, let us pray", "Please do speak again"],
        source_reference="Thomas Jones (1841) §28; Roberts (1891) §121"
    ),
    GrammarRule(
        id="DIS-02",
        name="Epistemic Tag and Confirmation Marker 'Mo'",
        category="Discourse Particles",
        formula="[Declarative Clause] + [mo?]",
        description="Sentence-final tag question particle 'mo' seeks agreement, confirmation, or cordial assent ('right? / isn't it?').",
        khasi_examples=["Phi la dep, mo? (You have finished, haven't you?)", "Ngin leit lashai, mo? (We will go tomorrow, right?)"],
        english_translations=["You have finished, haven't you?", "We will go tomorrow, right?"],
        source_reference="Roberts (1891) §122"
    ),
    GrammarRule(
        id="TAM-17",
        name="Future Subject Enclitic Sandhi Contractions",
        category="Tense-Aspect-Mood",
        formula="[Pronoun] + -n (nga + -n -> ngan, u + -n -> un, ka + -n -> kan, ki + -n -> kin)",
        description="When the prospective future particle 'yn' attaches to preceding vowel-final subject pronouns, systematic morphophonemic sandhi reduces the cluster to a single monosyllable.",
        khasi_examples=["ngan leit (I will go from nga + yn)", "un wan (he will come from u + yn)", "kan trei (she will work from ka + yn)"],
        english_translations=["I will go", "he will come", "she will work"],
        source_reference="Roberts (1891) §88"
    ),
    GrammarRule(
        id="TAM-13",
        name="Inchoative Consecutive Particle 'Sa'",
        category="Tense-Aspect-Mood",
        formula="[Temporal Clause: Ynda...] + [Subject] + sa + [Verb]",
        description="'Sa' indicates an action that follows as the immediate subsequent step after a prior condition has been realized ('then and only then / thereupon').",
        khasi_examples=["Ynda u la wan, ngan sa kren (When he has arrived, I will then speak)", "Ngin sa leit (We shall then proceed)"],
        english_translations=["When he has arrived, I will then speak", "We will then proceed"],
        source_reference="Roberts (1891) §93"
    ),
    GrammarRule(
        id="TAM-14",
        name="Continuous Developing Stative Auxiliary 'Nang-'",
        category="Tense-Aspect-Mood",
        formula="[Subject Pronoun] + nang + [Verb / Adjective]",
        description="'Nang' denotes progressive development, continuing proficiency, or an action increasing in degree over time ('keeps on doing / grows more').",
        khasi_examples=["U nangsan (He keeps growing / grows taller)", "Ka nangstew (It keeps getting clearer)", "Ki nangtrei (They keep on working)"],
        english_translations=["He keeps on growing", "It keeps growing brighter", "They keep on working diligently"],
        source_reference="Roberts (1891) §94; Thomas Jones (1841) §20"
    ),
    GrammarRule(
        id="ASP-01",
        name="Frequentative Verbal Stem Reduplication",
        category="Enclitics & Expressives",
        formula="[Verb Root] + - + [Verb Root]",
        description="Complete reduplication of the verbal root indicates iterative, habitual, continuous, or casual repeated action.",
        khasi_examples=["iaid-iaid (to stroll casually / keep walking around)", "trei-trei (to work persistently)", "khmih-khmih (to gaze repeatedly / keep watching)"],
        english_translations=["to stroll leisurely about", "to work continuously", "to keep looking repeatedly"],
        source_reference="Roberts (1891) §119"
    ),
    GrammarRule(
        id="CAS-09",
        name="Synteng / Pnar Dialectal Allative Case Marker 'Che' / 'Cha'",
        category="Case Marking",
        formula="[Verb of Motion] + che / cha + [Noun / Location]",
        description="In the Synteng (Pnar / Jaintia) dialect of Khasi, directional motion towards a place is marked by the preposition 'che' or 'cha', functioning as the dialectal counterpart of standard Sohra 'sha'.",
        khasi_examples=["leit che ïing (go home / to the house)", "wan che shnong (come to the village)"],
        english_translations=["go home (to the house)", "come to the village"],
        source_reference="Grierson (1903), Linguistic Survey of India Vol. II, §Khasi-Synteng"
    ),
    GrammarRule(
        id="CLA-09",
        name="Archaic Purposive Infinitive Combination 'Ban Sa' / 'Ban Da'",
        category="Complex Syntax",
        formula="[Main Clause] + ban sa / ban da + [Subordinate Verb]",
        description="In 19th-century classical Khasi prose, the infinitive prefix 'ban' combines with aspectual and instrumental particles 'sa' (consecutive) or 'da' (instrumental/modal) to express deliberate design, subsequent outcome, or solemn intent.",
        khasi_examples=["U la wan ban sa kren (He came in order that he might then speak)", "Ban da pyni ia ka jingshisha (In order to demonstrably show the truth)"],
        english_translations=["He came in order that he might then speak", "In order to demonstrably show the truth"],
        source_reference="Rev. W. Pryse (1855) §102; Rev. Thomas Jones (1841) §28"
    ),
    GrammarRule(
        id="EXP-07",
        name="Classical Exclusivity and Emphatic Enclitic '-ke'",
        category="Enclitics & Expressives",
        formula="[Personal Pronoun] + -ke (nga-ke / u-ke / ka-ke / ma-u-ke)",
        description="Classical post-nominal emphatic enclitic denoting sole exclusivity, personal agency, or distinct identification ('he himself alone / none other than he').",
        khasi_examples=["u-ke un leh (he himself alone will do it)", "ma-u-ke u nongthoh (he himself is the author)"],
        english_translations=["he himself alone shall do it", "he himself is indeed the writer"],
        source_reference="Rev. W. Pryse (1855) §48; Roberts (1891) §120"
    ),
    GrammarRule(
        id="TAM-15",
        name="Cohortative and Optative Imperative Auxiliary 'To' / 'To Ia'",
        category="Tense-Aspect-Mood",
        formula="To + [Subject Pronoun: ngin / u / phi] + [Verb Predicate]",
        description="Pre-verbal optative marker used to initiate cohortative appeals ('let us'), polite benedictions ('may it be so'), and solemn exhortations.",
        khasi_examples=["To ngin ïaleit noh (Let us now depart together)", "To U Blei un kyrkhu ia phi (May God bless you)"],
        english_translations=["Let us depart together now", "May God bless you"],
        source_reference="Rev. W. Pryse (1855) §89; Thomas Jones (1841) §22"
    ),
    GrammarRule(
        id="DIS-03",
        name="Classical Quotative and Evidential Reportative Particle 'Da Ong'",
        category="Discourse Particles",
        formula="[Speaker] + da ong + [Direct / Indirect Quote]",
        description="Reportative evidential construction introducing cited speech, proverbs, oral tradition, and authoritative scriptural decrees ('saying / as it is spoken').",
        khasi_examples=["Ki kpa tymmen ki la sneng da ong, 'Wat klet ia ka akor' (The elders admonished saying, 'Never forget etiquette')", "U la jubab da ong... (He answered saying...)"],
        english_translations=["The elders admonished saying, 'Never forget etiquette'", "He answered saying..."],
        source_reference="Rev. H. Roberts (1891) §152; Grierson (1903) §Khasi Narrative"
    ),
    GrammarRule(
        id="PHO-02",
        name="Phonemic Glottal Stop Realization and Orthographic Apostrophe",
        category="Enclitics & Expressives",
        formula="[Vowel] + ' + [Consonant / End] (e.g. kyr'shan vs kyrshan)",
        description="In standard Khasi phonology, the glottal stop /ʔ/ (represented orthographically by an apostrophe or phonotactic hiatus) serves a crucial phonemic contrast distinguishing minimal pairs and emphatic focus.",
        khasi_examples=["kyr'shan (to uphold firmly)", "la' (enough / intense)", "khie' (arise abruptly)"],
        english_translations=["to uphold firmly with conviction", "enough / fully", "arise abruptly"],
        source_reference="Ki Sawa Bad Dur Kyntien Jong Ka Ktien Khasi (1984); U Glottal Stop Ha Ka Ktien Khasi"
    ),
    GrammarRule(
        id="DER-11",
        name="Pre-Verbal Spatial & Ventive Directional Prefixes 'Wan-' and 'Lait-'",
        category="Derivational Morphology",
        formula="wan- / lait- + [Verb Stem]",
        description="Directional morpho-syntactic prefixes attach directly to verb roots to indicate ventive motion towards the speaker ('wan-rah' bring here) or liberative motion outwards ('lait-luid' be free, 'lait-im' survive).",
        khasi_examples=["wan-rah ia ka kot (bring the book here)", "lait-im na ka jingjynjar (survive from hardship)", "wan-shong (come and sit)"],
        english_translations=["bring the book here", "survive from hardship", "come and sit down"],
        source_reference="Khasi-English Course And Grammar For Schools And Colleges (1988) §64"
    ),
    GrammarRule(
        id="TAM-16",
        name="Prospective Intentional Auxiliary Marker 'Thmu Ban'",
        category="Tense-Aspect-Mood",
        formula="[Subject Pronoun] + thmu ban + [Verb Stem]",
        description="Combines the intentional verb of mental resolve 'thmu' (intend/plan) with the infinitive prefix 'ban' to form prospective planned aspect ('intends to / is about to').",
        khasi_examples=["Nga thmu ban leit sha Shillong (I intend to go to Shillong)", "Ki thmu ban tei ia ka ïing (They plan to build the house)"],
        english_translations=["I intend to go to Shillong", "They plan to build the house"],
        source_reference="Roberts (1891) §98; Khasi Authors Society Standard Grammar"
    ),
    GrammarRule(
        id="AGR-07",
        name="Honorific Reverential Plural Article Agreement 'Ki'",
        category="Nominal Agreement",
        formula="ki + [Singular Elder Noun / Office / Dignitary]",
        description="When referring to elder relatives, clan matriarchs, or civic leaders with high veneration, the plural article 'ki' is grammatically deployed with an individual singular noun as a polite honorific.",
        khasi_examples=["ki kpa tymmen (the venerable elder father)", "ki syiem (His Royal Highness the King)", "ki sordar (the revered headman)"],
        english_translations=["the venerable elder father", "His Royal Highness the King", "the revered village headman"],
        source_reference="Babu Jeebon Roy (1897); Ka Akor Khasi Ha Ka Riti (1986)"
    ),
    GrammarRule(
        id="CLA-10",
        name="Concessive Adversative Clause Construction 'La Bha Ba ... Pynban'",
        category="Complex Syntax",
        formula="La bha ba + [Subordinate Clause], pynban + [Main Clause]",
        description="Formal concessive clause structure contrasting an adverse circumstance or natural obstacle with resilient human action ('Although ... yet / nevertheless').",
        khasi_examples=["La bha ba ka la slap jur, pynban u la leit (Even though it rained hard, yet he went)", "La bha ba u duk, pynban u hok (Though he is poor, yet he is honest)"],
        english_translations=["Even though it rained hard, yet he went", "Though he is poor, yet he is honest"],
        source_reference="Rev. W. Pryse (1855) §114; Roberts (1891) §158"
    ),
    GrammarRule(
        id="PHO-01",
        name="Sesquisyllabic Root and Minor Prefix Syllabification",
        category="Phonotactics & Morpho-Phonology",
        formula="[Minor Syllable: ky-, py-, ty-, sy-, kh-, sh-, th-, ph-] + [Major Syllable C(C)V(C)]",
        description="Khasi roots characteristically display sesquisyllabic (one-and-a-half syllable) structure where an unstressed pre-syllable attaches to an unaccented or accented major root. Final stops at syllable codas are strictly unreleased and voiceless (-k, -t, -p).",
        khasi_examples=["kynmaw (to remember)", "tyngkai (to preserve)", "synshar (to govern)", "shondur (to photograph)"],
        english_translations=["to remember", "to preserve / cherish", "to govern / rule", "to capture an image"],
        source_reference="Roberts (1891) §3-7; Henderson (1976); Lyngdoh (1983)"
    ),
    GrammarRule(
        id="PHO-03",
        name="Phonemic Vowel Length and Tenseness Contrast 'I' vs 'Ï'",
        category="Phonotactics & Morpho-Phonology",
        formula="[Short lax vowel: i [i]] vs [Long tense vowel: ï [i:]]",
        description="Vowel length and tense articulation constitute a crucial phonemic contrast in Khasi orthography, creating minimal pairs that distinguish grammatical markers from lexical roots.",
        khasi_examples=["ia (to us / inclusive) vs ïa (objective case marker / reciprocal)", "iing (burning) vs ïing (house / family residence)", "iam (lamentation) vs ïam (to weep / cry)"],
        english_translations=["to us vs objective marker", "burning vs house", "lamentation vs to weep"],
        source_reference="Roberts (1891) §6; Khasi Orthography Standardization Committee (1986)"
    ),
    GrammarRule(
        id="TAM-18",
        name="Mutual Reciprocal Verbal Prefix 'ïa-'",
        category="Tense-Aspect-Mood",
        formula="[Plural Subject NP / Pronoun] + ïa- + [Verb Stem]",
        description="Prefixes directly to a verbal root to denote mutual, joint, or reciprocal interaction between two or more subjects ('with one another / mutually / together').",
        khasi_examples=["Ki la ïakren (They conversed with each other)", "Ki khynnah ki la ïaleh (The children competed/played together)", "Ngin sa ïashem (We shall meet each other)"],
        english_translations=["They conversed with each other", "The children played together", "We shall meet each other"],
        source_reference="Roberts (1891) §102; Thomas Jones (1841) §18"
    ),
    GrammarRule(
        id="TAM-19",
        name="Frequentative and Iterative Aspect Particle 'Bunsien / Shen Shen'",
        category="Tense-Aspect-Mood",
        formula="[Subject NP] + [Verb] + bunsien / shen shen",
        description="Post-verbal aspectual particles specifying habitual repetition or immediate recurrence of an action ('frequently / repeatedly / over and over').",
        khasi_examples=["U wan bunsien sha ïing (He visits the home frequently)", "Ka la kren shen shen (She spoke repeatedly)"],
        english_translations=["He visits the home frequently", "She spoke repeatedly"],
        source_reference="Roberts (1891) §116; U Soso Tham (1925)"
    ),
    GrammarRule(
        id="TAM-20",
        name="Incremental Inchoative Correlative Aspect 'Nang- ... Nang-'",
        category="Tense-Aspect-Mood",
        formula="Nang + [Verb/Adjective 1], nang + [Verb/Adjective 2]",
        description="Correlative inchoative construction signifying continuous proportional intensification over time ('the more ... the more ...' or 'gradually increasingly').",
        khasi_examples=["Nang miet nang kynjah (As the night deepens, it becomes more and more peaceful)", "Nang heh nang stad (The more one grows, the wiser one becomes)"],
        english_translations=["As night deepens, it becomes more and more peaceful", "The more one grows, the wiser one becomes"],
        source_reference="Roberts (1891) §150; R. S. Lyngdoh (1983)"
    ),
    GrammarRule(
        id="TAM-21",
        name="Prohibitive Apprehensive Caution Marker 'Ioh'",
        category="Tense-Aspect-Mood",
        formula="[Imperative / Clause 1] + ioh + [Clause 2 (Undesirable Outcome)]",
        description="Negative modal cautionary connective signaling apprehension of an imminent hazard ('lest / so that ... not / in case').",
        khasi_examples=["Wat leit sha wah, ioh phi hap (Do not go near the river, lest you fall)", "Mareh kloi, ioh ka sngi ka sep (Hurry, lest the sun sets)"],
        english_translations=["Do not go near the river, lest you fall", "Hurry, lest the sun sets"],
        source_reference="Roberts (1891) §159; Rev. W. Pryse (1855) §118"
    ),
    GrammarRule(
        id="NUM-05",
        name="Arboreal and Vegetative Numeral Classifier 'Tynrai'",
        category="Numeral Classifiers",
        formula="[Numeral] + tynrai + [ki + Tree / Rooted Plant Noun]",
        description="Botanical numeral classifier reserved strictly for rooted living trees, timber trunks, bamboos, and perennial plants.",
        khasi_examples=["lai tynrai ki dieng (three trees)", "hynniew tynrai ki siej (seven bamboo stalks)"],
        english_translations=["three trees", "seven bamboo stalks"],
        source_reference="Roberts (1891) §46; U Soso Tham (1925)"
    ),
    GrammarRule(
        id="NUM-06",
        name="Ornative and Tubular Numeral Classifiers 'Tyndong' and 'Kpieng'",
        category="Numeral Classifiers",
        formula="[Numeral] + tyndong / kpieng + [ki + Noun]",
        description="Specialized structural classifiers: 'tyndong' for hollow cylindrical vessels and tubes, and 'kpieng' for strung necklaces, coral beads, and ornaments.",
        khasi_examples=["ar tyndong ki sharak (two lantern chimneys)", "saw kpieng ki paila (four strings of coral beads)"],
        english_translations=["two lamp cylinders", "four strands of coral beads"],
        source_reference="Roberts (1891) §47; Ka Riti Jong Ka Ri Khasi (1930)"
    ),
    GrammarRule(
        id="DIS-04",
        name="Conversational Interrogative Tag Enclitic 'Mo' / 'Ne Em'",
        category="Discourse Particles",
        formula="[Declarative Statement], + mo? / ne em?",
        description="Colloquial and formal conversational tag seeking assent, clarification, or polarity verification ('isn't that so? / right? / or not?').",
        khasi_examples=["Phi la sngewthuh, mo? (You have understood, haven't you?)", "U kpa u la wan, ne em? (The father has arrived, or not?)"],
        english_translations=["You have understood, haven't you?", "The father has arrived, or did he not?"],
        source_reference="Roberts (1891) §128; Lyngdoh (1983)"
    ),
    GrammarRule(
        id="EXP-10",
        name="Phonaesthetic Quadrisyllabic Expressive Compounding",
        category="Enclitics & Expressives",
        formula="[Root Verb A] + [Echo Syllable B] + [Root Verb C] + [Echo Syllable D]",
        description="Four-part alliterative and rhyming phonaesthetic compounds (Ka Ktien Biria bad Phawar) conveying emotional tone, aesthetic manners, and visual imagery.",
        khasi_examples=["bam-ja-dih-duma (living in relaxed contentment)", "leit-kai-wan-kai (leisurely strolling back and forth)", "iaid-stet-leit-wir (walking quickly yet wandering)"],
        english_translations=["living in relaxed contentment", "leisurely strolling back and forth", "walking quickly yet wandering aimlessly"],
        source_reference="Roberts (1891) §168; Babu Jeebon Roy (1897)"
    ),
    GrammarRule(
        id="AGR-08",
        name="Epicene Feminine Agreement 'Ka' for Abstract Nouns and Natural Elements",
        category="Nominal Agreement",
        formula="ka + [Abstract Concept / Natural Element Noun]",
        description="In classical Khasi syntax, all abstract nominalizations, moral virtues, intangible phenomena, and primeval natural forces (air, water, light, fire, time) take feminine gender article 'ka' as an epicene default.",
        khasi_examples=["ka jingshai (light / wisdom)", "ka um (water)", "ka lyer (the wind)", "ka ding (fire)", "ka por (time)"],
        english_translations=["the light / illumination", "the water", "the wind / breeze", "the fire", "the time / hour"],
        source_reference="Rev. H. Roberts (1891) §32; Rev. Thomas Jones (1841) §11"
    ),
    GrammarRule(
        id="TAM-22",
        name="Definite Assured Prospective Auxiliary 'Yn Sa Da'",
        category="Tense-Aspect-Mood",
        formula="[Subject] + yn sa da + [Verb Stem]",
        description="Double auxiliary compounding combining prospective 'yn', consecutive 'sa', and modal-affirmative 'da' to express absolute certainty or guaranteed future outcome ('shall certainly / will without fail').",
        khasi_examples=["Ngan sa da wan shisha (I shall certainly without fail come)", "Kin sa da ioh ia ka bainong (They shall surely receive their wage)"],
        english_translations=["I shall certainly without fail come", "They will surely receive their reward"],
        source_reference="Rev. W. Pryse (1855) §98; Roberts (1891) §95"
    ),
    GrammarRule(
        id="CAS-10",
        name="Sociative / Comitative Coordination with 'Bad' and Subject Agreement",
        category="Case Marking",
        formula="[Subject NP 1] + [Verb] + bad + [la u/ka] + [Noun 2]",
        description="The comitative / sociative case preposition 'bad' coordinates joint participants in an action, frequently requiring reflexive possessive 'la' when expressing kinship companionship.",
        khasi_examples=["U la leit bad la u kpa (He went along with his father)", "Ka kmie ka ïatrei bad ki khun (The mother works together with the children)"],
        english_translations=["He went along with his father", "The mother works together with her children"],
        source_reference="Roberts (1891) §78; Lyngdoh (1983)"
    ),
    GrammarRule(
        id="DER-12",
        name="Antonymic and Pejorative Participle Prefix 'Bym-'",
        category="Derivational Morphology",
        formula="bym- + [Verb / Adjective Stem]",
        description="Derives negative participial adjectives, privative nouns, and antonyms denoting the absence, deficiency, or corrupt opposite of the root concept ('un- / dis- / non-').",
        khasi_examples=["bymman (evil / unrighteous from man 'to grow/be')", "bymhok (unjust / deceitful from hok 'righteous')", "bymlah (incapable / invalid from lah 'able')"],
        english_translations=["wicked / malicious", "unjust / corrupt", "feeble / incapacitated"],
        source_reference="Rev. Thomas Jones (1841) §16; Roberts (1891) §110"
    ),
    GrammarRule(
        id="CLA-11",
        name="Comparative and Superlative Syntax with 'Kham ... Ban Ïa' and 'Tam'",
        category="Complex Syntax",
        formula="[Subject] + kham + [Adjective/Verb] + ban ïa + [Standard of Comparison] / [Adj] + tam",
        description="Comparison of degree places pre-adjectival modifier 'kham' before the predicate and marks the standard of comparison with 'ban ïa' ('more than'). Superlative degree is expressed by postpositional 'tam' ('most / supreme').",
        khasi_examples=["U kham jrong ban ïa nga (He is taller than I)", "Kane ka kham bha (This is better)", "Uba khraw tam (The greatest of all)"],
        english_translations=["He is taller than I", "This is better / preferable", "The supreme / greatest one"],
        source_reference="Rev. H. Roberts (1891) §54; Rev. W. Pryse (1855) §62"
    ),
    GrammarRule(
        id="EXP-11",
        name="Ideophonic Sensory Expressives for Motion, Gait, and Posture",
        category="Enclitics & Expressives",
        formula="[Motion Verb: iaid / mareh / shong] + [Phonaesthetic Ideophone]",
        description="Khasi boasts an extraordinarily nuanced inventory of phonaesthetic expressives that paint precise sensory, auditory, and visual impressions of bodily movement, velocity, and posture.",
        khasi_examples=["U mareh thir-thir (He runs with light, swift, feather-like steps)", "U ïaid sar-sar (He walks with rustling, stealthy strides)", "Ka shong kduk (She sits quietly huddled alone)"],
        english_translations=["He runs with light, swift, feather-like steps", "He walks with rustling, stealthy strides", "She sits quietly huddled alone"],
        source_reference="Eugénie J. A. Henderson (1976); Dr. R. S. Lyngdoh (1983)"
    ),
    GrammarRule(
        id="NUM-07",
        name="Marketplace Measure Classifiers for Packaged and Bundled Produce",
        category="Numeral Classifiers",
        formula="[Numeral] + song / khoh / khylliah + [ki/u/ka + Produce Noun]",
        description="Traditional Khasi marketplace numeral measure classifiers specifying standardized quantities: 'song' for leaf-wrapped parcels, 'khoh' for conical cane basketfuls, and 'khylliah' for folded leaf bundles.",
        khasi_examples=["shisong u soh (one wrapped parcel of fruit)", "shikhoh u phan (one conical basketful of potatoes)", "shikhylliah ka duma (one packet of cured tobacco)"],
        english_translations=["one wrapped parcel of fruit", "one conical basketful of potatoes", "one packet of leaf tobacco"],
        source_reference="Rev. H. Roberts (1891) §48; U Khasi Hyndai (1979)"
    ),
    GrammarRule(
        id="DIS-05",
        name="Topicalizing and Contrastive Focus Enclitic 'Te'",
        category="Discourse Particles",
        formula="[Noun Phrase / Clause] + te, + [Predicate / Main Clause]",
        description="Post-phrasal discourse marker 'te' highlights the preceding constituent as the primary informational topic, contrastive focus, or conditional pivot ('as for ... / indeed / now as regards').",
        khasi_examples=["Ma nga te ngan ym leit (As for me, I will not go)", "U kpa te u la tip lypa (The father, for his part, already knew in advance)"],
        english_translations=["As for me personally, I shall not go", "The father, for his part, already knew beforehand"],
        source_reference="Rev. H. Roberts (1891) §124; Rev. W. Pryse (1855) §116"
    ),
    GrammarRule(
        id="PHO-05",
        name="Morpho-Phonological Glide Epenthesis and Hiatus Resolution",
        category="Phonotactics & Morpho-Phonology",
        formula="[Prefix ending in consonant/vowel] + [Stem starting with vowel /i/ or /u/] -> epenthetic glide [j] or [w]",
        description="When morphological prefixes combine with vowel-initial roots, Khasi morphophonology systematically inserts a glide (palatal glide /j/ written 'ï' or bilabial glide /w/) to resolve vocalic hiatus across syllable boundaries.",
        khasi_examples=["pyn- + ïap -> pyn-ïap (cause to die / kill)", "ïa- + um -> ïawum (to bathe together)", "kyn- + ïum -> kyn-ïum (to murmur softly)"],
        english_translations=["to cause to die / put to death", "to bathe together", "to murmur gently"],
        source_reference="Lili Rabel (1961), 'Khasi, a Language of Assam'; Henderson (1976)"
    ),
    GrammarRule(
        id="TAM-23",
        name="Intensive Deliberative Aspect Marker 'Pynban'",
        category="Tense-Aspect-Mood",
        formula="[Subject] + [Verb] + pynban / Pynban + [Subject] + [Verb]",
        description="Aspectual particle indicating resolute perseverance, deliberate defiance of warning, or counter-expectational execution ('persisted in doing / went ahead and did it anyway').",
        khasi_examples=["U la leh pynban wat la la khang (He did it anyway even though forbidden)", "Ka la wan pynban (She came nevertheless)"],
        english_translations=["He went ahead and did it anyway despite prohibition", "She came nevertheless"],
        source_reference="Rev. H. Roberts (1891) §131; Babu Jeebon Roy (1897)"
    ),
    GrammarRule(
        id="TAM-24",
        name="Historical Optative-Precative with Archaic 'Ioh' and 'Khein'",
        category="Tense-Aspect-Mood",
        formula="[Ioh ba / Khein ba] + [Subject] + [Verb Phrase]",
        description="Classical precative and solemn optative construction found in 19th-century Khasi translations and prayers to invoke earnest blessing or solemn wish ('May it be that... / Would that...').",
        khasi_examples=["Ioh ba U Blei un isynei (May God have mercy / Would that God show grace)", "Khein ba ngin ioh ka jingsuk (May we receive peace)"],
        english_translations=["May God have mercy upon us", "May we find true peace"],
        source_reference="Rev. Thomas Jones (1841) §24; Rev. H. Roberts (1891) §125"
    ),
    GrammarRule(
        id="TAM-25",
        name="Sequential Concomitant Aspect with 'Nangta' and 'Nangne'",
        category="Tense-Aspect-Mood",
        formula="[Clause 1] + nangta / nangne + [Subject] + [Verb Phrase]",
        description="Concomitant narrative transition markers indicating temporal progression from a previously established reference event ('thenceforth / thereupon / from that point onward').",
        khasi_examples=["Nangta ki la ïaleit noh sha shnong (Thereupon they went forward to the village)", "Nangne un sa sdang ia ka kam (Henceforth he will begin the work)"],
        english_translations=["Thereupon they proceeded to the village", "From here on he will commence the work"],
        source_reference="Rev. W. Pryse (1855) §106; Rev. H. Roberts (1891) §148"
    ),
    GrammarRule(
        id="AGR-09",
        name="Honorific Diminutive Agreement 'I' for Revered Ancestors and Kin",
        category="Nominal Agreement",
        formula="i + [Affectionate / Revered Ancestor / Maternal Relative Noun]",
        description="Beyond its use for small or diminutive entities, article 'i' functions in classical Khasi matrilineal kinship syntax as a marker of tender reverence and familial intimacy for mothers, grandmothers, and young kin.",
        khasi_examples=["i mei (beloved mother)", "i mei-rad (beloved grandmother)", "i khun-lung (tender infant child)"],
        english_translations=["beloved mother", "dear grandmother", "tender infant child"],
        source_reference="Babu Jeebon Roy (1897); Roberts (1891) §33; Ka Riti Jong Ka Ri Khasi (1930)"
    ),
    GrammarRule(
        id="CAS-11",
        name="Synteng / Pnar Locative Postpositional Particle 'Ha-khet'",
        category="Case Marking",
        formula="ha-khet + [Noun / Physical Threshold]",
        description="Archaic Jaintia/Synteng postpositional compound indicating exact spatial proximity or positioning right beside or upon an elevated seat/threshold ('right upon the threshold / beside the royal seat').",
        khasi_examples=["ha-khet ka ïing (right at the threshold of the house)", "shong ha-khet (seated upon the sacred dais)"],
        english_translations=["right at the household threshold", "seated upon the sacred platform"],
        source_reference="Grierson (1903) §Khasi-Synteng; Rev. H. Roberts (1891) §79"
    ),
    GrammarRule(
        id="DER-13",
        name="Reciprocal Collectivity Compound Prefix 'ïa-pyn-'",
        category="Derivational Morphology",
        formula="ïa- + pyn- + [Verb / Adjective Root]",
        description="Combination of reciprocal prefix 'ïa-' and causative prefix 'pyn-' generating causative-reciprocal verbs where multiple subjects mutually cause or stimulate an action between one another.",
        khasi_examples=["ïapynbeit (to mutually settle / mediate together)", "ïapynshlur (to encourage one another mutually)", "ïapyniasuk (to reconcile with one another)"],
        english_translations=["to mutually mediate / settle an agreement", "to encourage one another mutually", "to reconcile with each other"],
        source_reference="Rev. H. Roberts (1891) §105; Rev. Thomas Jones (1841) §19"
    ),
    GrammarRule(
        id="CLA-12",
        name="Temporal Subordinating Clause Inversion with 'Mynba' and 'Ynda'",
        category="Complex Syntax",
        formula="Mynba / Ynda + [Subject] + [Verb], [Main Clause]",
        description="Fronted subordinate temporal clauses marking past temporal inception ('mynba' = when in past) or prospective completion ('ynda' = when / as soon as in future/perfect), triggering main clause topicalization.",
        khasi_examples=["Mynba nga dang rit, nga shong ha Sohra (When I was young, I lived in Sohra)", "Ynda phi la dep, to khot ia nga (When you have finished, do call me)"],
        english_translations=["When I was young, I dwelt in Sohra", "When you have finished, pray call me"],
        source_reference="Rev. H. Roberts (1891) §142; Rev. W. Pryse (1855) §112"
    ),
    GrammarRule(
        id="EXP-12",
        name="Phonaesthetic Reduplicative Attenuative Adjectives",
        category="Enclitics & Expressives",
        formula="[Color / Quality Root] + - + [Color / Quality Root]",
        description="Complete reduplication of chromatic, visual, or sensory roots denoting mild, diffused, or delicate manifestation of a physical hue or trait ('somewhat / tinged with').",
        khasi_examples=["stem-stem (yellowish / golden tinged)", "lir-lir (delicately green / fresh)", "saw-saw (reddish / blushing rosy)"],
        english_translations=["golden-yellowish / tinged yellow", "fresh and vibrant green", "blushing reddish"],
        source_reference="Roberts (1891) §53; Eugénie J. A. Henderson (1976)"
    ),
    GrammarRule(
        id="NUM-08",
        name="Botanical Cluster and Sheaf Classifiers 'Rynjup' and 'Khlaw'",
        category="Numeral Classifiers",
        formula="[Numeral] + rynjup / khlaw + [ki + Noun]",
        description="Numerical classifiers specialized for natural aggregates: 'rynjup' for bunches, clusters, or fruiting racemes; 'khlaw' for stands of forest, bamboo groves, and coppices.",
        khasi_examples=["shi rynjup ki soh-manir (one cluster of blackberries)", "ar khlaw ki siej (two groves of bamboo)"],
        english_translations=["one cluster of blackberries", "two bamboo groves"],
        source_reference="Roberts (1891) §49; U Soso Tham (1925)"
    ),
    GrammarRule(
        id="DIS-06",
        name="Assertive Emphatic Enclitic 'Re'",
        category="Discourse Particles",
        formula="[Predicate / Clause] + re!",
        description="Discourse particle functioning as an assertive intensifier or exclamation affirming unquestionable certainty, vivid realization, or urgency in narrative dialogue.",
        khasi_examples=["Ka la wan shisha re! (She has indeed arrived!)", "U la tip lypa re (He certainly already knew it!)"],
        english_translations=["She has indeed arrived for sure!", "He certainly already knew it all along!"],
        source_reference="Rev. H. Roberts (1891) §127; Dr. R. S. Lyngdoh (1983)"
    ),
    GrammarRule(
        id="PHO-06",
        name="Consonant Gemination and Coda Lenition in Fast Colloquial Speech",
        category="Phonotactics & Morpho-Phonology",
        formula="[Stop Coda: -p, -t, -k] + [Identical Onset C] -> geminate / [Coda Lenition] in fast speech",
        description="In standard spoken Khasi and dialectal fast speech, word-final voiceless unreleased stops undergo phonetic assimilation or gemination when meeting identical consonants, while unaspirated stops before pause retain total unreleased closure.",
        khasi_examples=["khad-ar -> khaddar (twelve, from khad + ar with dental assimilation)", "ship-phew -> shipphew (ten, with bilabial gemination)"],
        english_translations=["twelve (phonetically contracted)", "ten (geminate bilabial)"],
        source_reference="Henderson (1976); Lili Rabel (1961); Khasi Phonology Standards (1986)"
    ),
]


class GrammarRulesEngine:
    """Query, filter, and inspect classical Khasi grammar rules."""

    def __init__(self):
        self._rules = CLASSICAL_GRAMMAR_RULES
        self._rules_by_id = {r.id: r for r in self._rules}
        self._categories = sorted(list(set(r.category for r in self._rules)))

    def all(self) -> List[GrammarRule]:
        """Return all catalogued grammar rules."""
        return list(self._rules)

    def get(self, rule_id: str) -> Optional[GrammarRule]:
        """Retrieve a specific grammar rule by ID (e.g. 'AGR-02', 'TAM-07')."""
        return self._rules_by_id.get(rule_id.upper().strip())

    def by_category(self, category: str) -> List[GrammarRule]:
        """Filter grammar rules by category."""
        c_low = category.lower()
        return [r for r in self._rules if c_low in r.category.lower()]

    def search(self, query: str) -> List[GrammarRule]:
        """Search grammar rules by keyword in name, description, formula, or examples."""
        q_low = query.lower().strip()
        results = []
        for r in self._rules:
            if (q_low in r.name.lower() or
                q_low in r.description.lower() or
                q_low in r.formula.lower() or
                any(q_low in ex.lower() for ex in r.khasi_examples) or
                any(q_low in tr.lower() for tr in r.english_translations)):
                results.append(r)
        return results

    def summary(self) -> Dict[str, Any]:
        """Return statistical summary of the grammar rules engine."""
        cats = {}
        for r in self._rules:
            cats[r.category] = cats.get(r.category, 0) + 1
        return {
            "total_rules": len(self._rules),
            "categories_count": len(cats),
            "categories": cats,
            "sources": [
                "Rev. H. Roberts, 'A Grammar of the Khassi Language' (1891)",
                "Rev. Thomas Jones, 'An Introduction to the Khasia Language' (1841)",
                "Rev. W. Pryse, 'An Introduction to the Khasia Language' (1855)",
                "Dr. G. A. Grierson, 'Linguistic Survey of India Vol. II' (1903)",
                "Babu Jeebon Roy, 'Ka Niam Jong Ki Khasi' (1897)",
                "Dr. R. S. Lyngdoh, 'Ka History Ka Thoh Ka Tar' (1983)"
            ]
        }


# Global instance
grammar_rules = GrammarRulesEngine()
