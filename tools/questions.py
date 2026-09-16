# -*- coding: utf-8 -*-
"""
All six Jeopardy games: questions, answers and the syllabus dot point each one maps to.

This file is only used by build_games.py to CREATE the game files the first time.
After that, the questions live inside each game's HTML file (games/*.html) and
you edit them there. See README.md.

Structure of each game:
  id, title, subtitle, topic, theme
  categories: list of 5, each with
      name       - the category heading shown on the board
      dotpoint   - the syllabus dot point it is built on (shown on the answer key)
      clues      - list of 5 (100 to 500 points), each with q, a
  final: one clue with category, dotpoint, q, a
"""

GAMES = [

# =====================================================================
# SPARTA — GAME 1
# =====================================================================
{
 "id": "sparta-1",
 "title": "Sparta I: The State",
 "subtitle": "Spartan Society to the Battle of Leuctra 371 BC — Game 1 of 2",
 "topic": "Spartan Society to the Battle of Leuctra 371 BC",
 "theme": "sparta",
 "categories": [
  {
   "name": "Geography and significant sites",
   "dotpoint": "Survey: geographical setting, natural features and resources of ancient Sparta; significant sites: Sparta",
   "clues": [
    {"q": "Sparta sat at the head of the Eurotas valley in which region of the south-eastern Peloponnese?",
     "a": "Laconia"},
    {"q": "Name the mountain range (2,407 m) that walled the Eurotas valley on the west and kept invaders out until 370/69 BC.",
     "a": "Mount Taygetus"},
    {"q": "Which rich farming region west of Taygetus did Sparta conquer in the First Messenian War (c. 740–720 BC), turning its people into helots?",
     "a": "Messenia (the Pamisos plain)"},
    {"q": "Name the bronze-sheathed temple on the Spartan acropolis, 'of the Bronze House', in which the regent Pausanias was walled up and starved.",
     "a": "The temple of Athena Chalkioikos"},
    {"q": "Thucydides (1.10) predicted that Sparta's ruins would never suggest its real power. Give TWO features of the site that made his prediction come true.",
     "a": "Any two: no city wall until the late 4th century BC; five separate villages (obai), never synoecised into one town; no monumental temples on the Athenian scale; the classical city now lies under modern Sparta (founded 1834); the royal tombs have never been found"}
   ]
  },
  {
   "name": "The Great Rhetra and the issue of Lycurgus",
   "dotpoint": "The Great Rhetra: the issue of Lycurgus",
   "clues": [
    {"q": "According to Plutarch, Lycurgus brought the Great Rhetra back from which oracle?",
     "a": "The oracle of Apollo at Delphi"},
    {"q": "The Rhetra set up a council of thirty, including the two kings, to prepare business for the assembly. What was this council called?",
     "a": "The gerousia (28 elders plus the two kings)"},
    {"q": "Plutarch says two later kings added a 'rider' letting the elders and kings set aside a 'crooked' decision of the people. Name the two kings.",
     "a": "Theopompos and Polydoros"},
    {"q": "Which 7th-century Spartan poet's fragment 4 (the Eunomia) preserves the Rhetra in verse, giving evidence independent of Plutarch that it is a genuine early document?",
     "a": "Tyrtaeus"},
    {"q": "Plutarch opens his Life of Lycurgus with a famous admission about the lawgiver. What does he say?",
     "a": "That 'nothing can be said about Lycurgus that is not disputed' — his dates, travels, laws and death are all contested (LACTOR F2)"}
   ]
  },
  {
   "name": "The two kings",
   "dotpoint": "Roles and privileges of the two kings; religious role of the kings",
   "clues": [
    {"q": "Name the two royal houses that each supplied one of Sparta's two kings.",
     "a": "The Agiads and the Eurypontids"},
    {"q": "After Kleomenes and Demaratus quarrelled in the field at Eleusis in 506 BC, what rule about kings on campaign was introduced (Herodotus 5.75)?",
     "a": "Only one king could go out with the army at a time"},
    {"q": "Herodotus (6.56) says each king held two priesthoods. Of which god?",
     "a": "Zeus — as Zeus Lakedaimon and Zeus Ouranios"},
    {"q": "Who were the Pythioi?",
     "a": "The two envoys each king appointed to consult the oracle at Delphi; they dined with the king at public expense and shared custody of the oracles (Herodotus 6.57)"},
    {"q": "Before leading the army across the frontier the king sacrificed to Zeus and Athena. What were these crossing-sacrifices called, and which contemporary writer, who marched with King Agesilaus, describes the ritual in chapter 13 of his Constitution of the Lacedaemonians?",
     "a": "The diabateria; Xenophon"}
   ]
  },
  {
   "name": "Government: ephorate, gerousia, ekklesia",
   "dotpoint": "Government: ephorate, gerousia, ekklesia",
   "clues": [
    {"q": "How many ephors were elected each year?",
     "a": "Five"},
    {"q": "How did the Spartan assembly (ekklesia or apella) vote, and what could it NOT do to a proposal?",
     "a": "By shouting (acclamation); it could only accept or reject, not debate or amend"},
    {"q": "Plutarch (Lycurgus 26) says elders were elected by shouting: candidates walked through the assembly while judges shut in a nearby building noted the loudest roar. Which philosopher called this method 'childish'?",
     "a": "Aristotle (Politics 1271a)"},
    {"q": "In 432 BC which ephor, claiming he could not tell which shout was louder, made the citizens divide into two groups — and so carried the vote for war against Athens (Thucydides 1.87)?",
     "a": "Sthenelaidas"},
    {"q": "Xenophon (Lak. Pol. 8) says the ephors had power 'like tyrants'. Give TWO specific powers the ephors held over the kings.",
     "a": "Any two: two ephors accompanied the king on campaign; monthly exchange of oaths with the king; they could fine, arrest or bring a king to trial; every ninth year they watched the sky for a shooting star and could suspend a king (Plutarch, Agis 11)"}
   ]
  },
  {
   "name": "The Spartan army: agoge and composition",
   "dotpoint": "The Spartan army: training (agoge), composition",
   "clues": [
    {"q": "At what age did a Spartan boy leave home to enter the agoge?",
     "a": "Seven"},
    {"q": "What was the title of the magistrate — the 'boy-herder' — who ran the agoge with his whip-bearers?",
     "a": "The paidonomos"},
    {"q": "What was the name of the elite corps of 300 young men, chosen each year from the hebontes, who fought around the king in battle?",
     "a": "The hippeis"},
    {"q": "Thucydides (5.66) said of the Spartan army that 'almost the whole army is officers'. Give the chain of command from the king down (at least three ranks).",
     "a": "King → polemarchs → lochagoi → pentekonteres → enomotarchs"},
    {"q": "At Leuctra in 371 BC Xenophon counts about 700 Spartiates present, of whom some 400 died. Which Theban tactic broke the Spartan phalanx, and which Spartan king was killed?",
     "a": "Epaminondas' deep (50-rank) left wing attacking obliquely; King Kleombrotos"}
   ]
  }
 ],
 "final": {
  "category": "Land ownership: agriculture, kleroi, helots",
  "dotpoint": "Land ownership: agriculture, kleroi, helots",
  "q": "Plutarch (Lycurgus 8) says Lycurgus redistributed the land into 9,000 equal lots for the Spartiates. Name the modern historian whose Property and Wealth in Classical Sparta (2000) argues there never was a Lycurgan redistribution, and give ONE piece of contemporary evidence that supports him.",
  "a": "Stephen Hodkinson. Evidence (any one): Tyrtaeus has helots paying half the crop, not a fixed rent; Xenophon (Lak. Pol. 6.3) speaks of using 'another man's' helots — private ownership; Aristotle (Politics 1270a) says the land had 'passed into the hands of a few' through gifts, bequests and dowries; no 5th- or 4th-century writer mentions equal lots"
 }
},

# =====================================================================
# SPARTA — GAME 2
# =====================================================================
{
 "id": "sparta-2",
 "title": "Sparta II: Society and Culture",
 "subtitle": "Spartan Society to the Battle of Leuctra 371 BC — Game 2 of 2",
 "topic": "Spartan Society to the Battle of Leuctra 371 BC",
 "theme": "sparta",
 "categories": [
  {
   "name": "Social structure and control of the helots",
   "dotpoint": "Social structure and occupations: Spartiates, perioikoi, 'inferiors', helots; control of the helots: the military, syssitia, krypteia",
   "clues": [
    {"q": "What Greek term, meaning 'Similars' or 'Peers', did full Spartan citizens use for themselves?",
     "a": "Homoioi"},
    {"q": "What was the name for the free, non-citizen 'dwellers-around' who lived in their own towns and handled Sparta's crafts, mining and trade?",
     "a": "The perioikoi"},
    {"q": "Which Athenian historian wrote (4.80) that 'most Spartan institutions were designed with a view to security against the helots', and told of 2,000 helots who were crowned as freedmen and then 'disappeared'?",
     "a": "Thucydides"},
    {"q": "What was the krypteia — and according to Aristotle (quoted in Plutarch, Lycurgus 28), what did the ephors do each year so that killing a helot brought no religious pollution?",
     "a": "'The hidden thing': young men sent out with daggers to hide by day and kill helots by night; the ephors formally declared war on the helots every year"},
    {"q": "Herodotus (9.28–29) gives the Spartan force at Plataea in 479 BC as 5,000 Spartiates and 5,000 perioikoi. How many helots came with them, and why does the figure matter to historians?",
     "a": "35,000 — seven helots per Spartiate, the only ratio for helot numbers given by any ancient source"}
   ]
  },
  {
   "name": "Women and marriage customs",
   "dotpoint": "Role and status of women: land ownership, inheritance, education; marriage customs",
   "clues": [
    {"q": "Which Spartan queen — daughter of Kleomenes, wife of Leonidas — is quoted in Plutarch's Sayings of Spartan Women declaring that Spartan women 'alone give birth to men'?",
     "a": "Gorgo"},
    {"q": "According to Xenophon (Lak. Pol. 1), why did the state have girls train in running, wrestling, discus and javelin 'no less than the men'?",
     "a": "So that strong parents would produce strong children — healthy mothers of future soldiers"},
    {"q": "Which royal Spartan woman, sister of King Agesilaus, won the four-horse chariot race at Olympia in 396 and 392 BC?",
     "a": "Kyniska"},
    {"q": "Aristotle (Politics 2.9) claimed that by the 4th century nearly what fraction of Spartan land was in women's hands, blaming heiresses and large dowries?",
     "a": "Two-fifths"},
    {"q": "Describe TWO features of the Spartan wedding ritual as Plutarch tells it (Lycurgus 15).",
     "a": "Any two: the bride was 'captured'; her head was shaved; she was dressed in a man's cloak and sandals; she was left alone on a mattress in the dark; the groom slipped in secretly after dining in the mess and returned to sleep with the young men — some men had children before they saw their wives by daylight"}
   ]
  },
  {
   "name": "The economy: technology, work and exchange",
   "dotpoint": "Technology: weapons, armour, pottery; economic roles of the perioikoi and helots; economic exchange: use of iron bars, trade",
   "clues": [
    {"q": "According to Plutarch and Xenophon, what metal did Sparta use as its money instead of gold and silver coin?",
     "a": "Iron (iron bars or spits — obeloi)"},
    {"q": "Name the port on the Laconian Gulf through which the perioikoi ran Sparta's trade and where the Spartan fleet was built.",
     "a": "Gytheion"},
    {"q": "Plutarch (Lycurgus 9) says the iron money was quenched in what liquid to make it brittle and useless for any other purpose?",
     "a": "Vinegar"},
    {"q": "Name the huge 6th-century Laconian bronze vessel — 1.63 m tall, 208 kg, with a frieze of hoplites and chariots — found in 1953 in a Celtic princess's grave in Burgundy.",
     "a": "The Vix krater"},
    {"q": "Both Bradley and Hurley state that iron was used to make bronze. What is bronze actually made of, and why did this matter for Laconia's economy?",
     "a": "Copper and tin; Laconia had iron ore but no copper or tin, so both had to be imported (through the perioikoi) for its famous bronze industry"}
   ]
  },
  {
   "name": "Religion, death and burial",
   "dotpoint": "Gods and goddesses: Artemis Orthia, Poseidon, Apollo; myths and legends: Lycurgus and the Dioscuri; festivals: Hyakinthia, Gymnopaedia, Karneia; funerary customs and rituals",
   "clues": [
    {"q": "The Hyakinthia, the Gymnopaidiai and the Karneia were all festivals of which god?",
     "a": "Apollo"},
    {"q": "At which goddess's sanctuary in Limnai, beside the Eurotas, did boys endure the cheese-stealing ordeal under the whip (Xenophon, Lak. Pol. 2.9)?",
     "a": "Artemis Orthia"},
    {"q": "Who were the Dioscuri, and how did their cult mirror the dual kingship after 506 BC (Herodotus 5.75)?",
     "a": "Kastor and Polydeukes, twin sons of Zeus and Leda and brothers of Helen; when one king went on campaign, one of the twins was said to stay at home with the other king"},
    {"q": "Herodotus (6.58) describes the funeral of a Spartan king. Give TWO of its features.",
     "a": "Any two: riders carried the news through Laconia; women beat cauldrons through the city; a free man and woman from every household had to go into mourning; perioikoi and helots were compelled to attend and lament; no assembly or elections for ten days; the new king cancelled debts to the crown or treasury"},
    {"q": "According to Xenophon (Hellenica 6.4.16), news of the defeat at Leuctra reached the ephors during which festival — and what did they decide to do?",
     "a": "The Gymnopaidiai (Gymnopaedia); they let the men's chorus finish the performance rather than stop the festival"}
   ]
  },
  {
   "name": "Cultural and everyday life",
   "dotpoint": "Art: sculpture, painted vases, bone and ivory carving; architecture: Amyklaion, Menelaion, Sanctuary of Artemis Orthia; writing and literature: Alcman and Tyrtaeus; leisure activities",
   "clues": [
    {"q": "Which 7th-century Spartan poet wrote maiden-songs (partheneia) for choruses of girls, one of which survives on a papyrus found at Saqqara in Egypt?",
     "a": "Alcman (the Louvre Partheneion)"},
    {"q": "Tyrtaeus' war poems urging men to stand and die in the front rank were written during which war, c. 650 BC?",
     "a": "The Second Messenian War"},
    {"q": "Which hilltop sanctuary about 5 km south of Sparta held the 30-cubit bronze pillar-statue of Apollo enclosed by the Throne of Bathykles?",
     "a": "The Amyklaion"},
    {"q": "Which Laconian painted cup of c. 565–560 BC, found at Vulci, shows a king of Cyrene supervising the weighing of silphium?",
     "a": "The Arkesilas Cup"},
    {"q": "The Damonon stele (c. 400 BC) records dozens of victories won by a Spartiate and his son. In what kind of contest — and what does it reveal about 'equality' among the Peers?",
     "a": "Chariot and horse races at Laconian festivals ('with his own four-horse team'); it shows a super-rich elite spending on horses — the Peers were similar in training and dress but not equal in wealth (Hodkinson's 'agonistic culture')"}
   ]
  }
 ],
 "final": {
  "category": "Greek writers' views of Sparta",
  "dotpoint": "Greek writers' views of Sparta: Herodotus, Thucydides, Xenophon, Aristotle, Pausanias, Plutarch",
  "q": "Name the French scholar and the term he coined in 1933 for the idealised, distorted picture of Sparta built up by non-Spartan writers — and give ONE way the Spartans themselves helped to create that picture.",
  "a": "François Ollier, 'le mirage spartiate' (the Spartan mirage). Spartan contributions (any one): secrecy about their institutions (Thucydides 5.68); the periodic expulsion of foreigners (xenelasia); the cult of Lycurgus as a divine founder; the Sayings of Spartans and Spartan Women"
 }
},

# =====================================================================
# GREEK WORLD — GAME 1
# =====================================================================
{
 "id": "greek-world-1",
 "title": "Greek World I: The Persian Wars",
 "subtitle": "The Greek World 500–440 BC — Game 1 of 2",
 "topic": "The Greek World 500–440 BC",
 "theme": "greek",
 "categories": [
  {
   "name": "Origins: Persian imperialism and the Ionian Revolt",
   "dotpoint": "Survey: chronological and geographical context; Persian Wars — origins: Persian imperialism, Ionian Revolt (ACHAH192)",
   "clues": [
    {"q": "Which Persian king defeated Croesus of Lydia in 546 BC, bringing the Greek cities of Ionia under Persian rule?",
     "a": "Cyrus the Great"},
    {"q": "Which tyrant of Miletus started the Ionian Revolt in 499 BC after his expedition against Naxos ended in failure?",
     "a": "Aristagoras"},
    {"q": "In 498 BC the Ionians and their Athenian and Eretrian allies burned which satrapal capital, destroying the temple of the goddess Cybebe?",
     "a": "Sardis"},
    {"q": "At which naval battle in 494 BC was the Ionian fleet crushed after the Samians and Lesbians deserted, leaving Miletus to be destroyed?",
     "a": "The Battle of Lade"},
    {"q": "Herodotus puts the blame for the revolt on Aristagoras. The modern historian J. A. Fine argues the 'basic cause of discontent' was something structural. What?",
     "a": "The system of Persian-appointed tyrants ruling the Ionian cities (plus the damage to Ionian trade from Persian control of Egypt, the Hellespont and the Bosporus)"}
   ]
  },
  {
   "name": "The invasion of 490 BC: Marathon and Miltiades",
   "dotpoint": "Invasion of 490 BC: Battle of Marathon, role of Miltiades (ACHAH194)",
   "clues": [
    {"q": "After the burning of Sardis, Darius ordered a servant to repeat a phrase to him three times a day before every meal. What was it?",
     "a": "'Sire, remember the Athenians'"},
    {"q": "Name the two commanders of the Persian expedition of 490 BC.",
     "a": "Datis and Artaphernes (the Younger)"},
    {"q": "When the ten Athenian generals were split five to five, which polemarch did Miltiades persuade to cast the deciding vote for battle (Herodotus 6.109)?",
     "a": "Callimachus"},
    {"q": "Describe Miltiades' battle plan at Marathon.",
     "a": "He stretched his line to match the Persians, kept the wings strong (eight deep) and deliberately thinned the centre; the Greeks charged at the run; the wings crushed the Persian flanks and wheeled inward to trap the Persian centre — a double envelopment"},
    {"q": "Historians argue about the 'missing' Persian cavalry at Marathon. Name ONE modern historian and his explanation.",
     "a": "V. Ehrenberg — Miltiades attacked when the cavalry was being re-embarked on the ships (the Ionian deserters' message 'the horsemen are away'); OR R. Sealey — Miltiades attacked out of fear of treachery inside Athens and the cavalry's absence was a coincidence"}
   ]
  },
  {
   "name": "The inter-war period: preparations in Persia and Greece",
   "dotpoint": "Inter-war period: preparation and developments in Persia and Greece (ACHAH195)",
   "clues": [
    {"q": "In what year did Darius die and Xerxes become Great King?",
     "a": "486 BC"},
    {"q": "A rich new vein of silver in which Attic mines paid for Themistocles' 200 triremes in 483 BC?",
     "a": "The Laurion mines"},
    {"q": "The Delphic oracle told the Athenians that only their 'wooden walls' would save them. What did Themistocles convince the assembly the phrase meant?",
     "a": "The new fleet of triremes (not the wooden palisade on the Acropolis)"},
    {"q": "Which engineering project, taking about three years, let Xerxes' fleet avoid the cape where Mardonius' fleet had been wrecked by storms in 492 BC?",
     "a": "The canal cut through the neck of the Mount Athos peninsula"},
    {"q": "About 30 states joined the Hellenic League at Corinth in 481 BC — a minority of the Greek world. Name TWO Greek states or rulers that refused to join or stayed neutral.",
     "a": "Any two: Argos (would not serve under Sparta); Thessaly (medised); Thebes (medised); Gelon of Syracuse (demanded supreme command); Crete; Corcyra (its 60 ships never arrived)"}
   ]
  },
  {
   "name": "The invasion of 480–479 BC",
   "dotpoint": "Invasion of 480–479 BC: Battles of Thermopylae and Artemisium, Salamis, Plataea and Mycale (ACHAH196)",
   "clues": [
    {"q": "In the narrow strait between which island and the Attic mainland did Themistocles force the decisive sea battle of 480 BC?",
     "a": "Salamis"},
    {"q": "The '300 Spartans' are famous, but roughly how many Greeks in total held the pass at Thermopylae on the first two days?",
     "a": "About 7,000 (Spartans, Thespians, Thebans, Phocians, Locrians and others)"},
    {"q": "Recite (or paraphrase) the epitaph attributed to Simonides that Herodotus (7.228) records for the Spartan dead at Thermopylae.",
     "a": "'Go tell the Spartans, traveller passing by, that here, obedient to their laws, we lie'"},
    {"q": "At Plataea in 479 BC, what fatal misreading by the Persian commander handed Pausanias his victory?",
     "a": "Mardonius saw the Greek army strung out mid-way through a night-time realignment, mistook it for a panicked retreat, and ordered an all-out charge into the Spartan phalanx"},
    {"q": "Name the Spartan king and the Athenian commander at Mycale in 479 BC, and explain what the battle did for Ionia.",
     "a": "Leotychides and Xanthippus; the Greeks stormed the stockade and burned the beached Persian fleet, the Ionian troops deserted, and the Ionian cities rose in revolt — Ionia was liberated and the Greeks gained a toehold in Asia Minor"}
   ]
  },
  {
   "name": "Themistocles, Leonidas, Pausanias, Eurybiades",
   "dotpoint": "Role and contribution of Themistocles, Leonidas, Pausanias, Eurybiades (ACHAH196)",
   "clues": [
    {"q": "Which Spartan was made navarch — overall commander of the Hellenic League fleet — at Artemisium and Salamis, even though Sparta contributed only 16 ships?",
     "a": "Eurybiades"},
    {"q": "Pausanias commanded at Plataea as regent, not king. For whom was he regent?",
     "a": "Pleistarchus, the young son of Leonidas"},
    {"q": "What 'excuse' did Themistocles use to persuade ordinary Athenians to spend the Laurion silver on ships rather than take a 10-drachma payment each?",
     "a": "The long-running war with the island of Aegina — not the distant Persian threat"},
    {"q": "Who was Sicinnus, and what message did he carry?",
     "a": "Themistocles' slave; he told Xerxes the Greeks were quarrelling and about to flee, so the Persians should block both ends of the strait — a trap that forced the battle in the narrows"},
    {"q": "Thucydides (1.138) praised Themistocles' 'natural genius', yet he was ostracised c. 471 BC. Where and in whose service did he die?",
     "a": "As Governor of Magnesia in Asia Minor under the Persian king Artaxerxes I (c. 459 BC, possibly by suicide)"}
   ]
  }
 ],
 "final": {
  "category": "Reasons for Greek victory and Persian defeat",
  "dotpoint": "Reasons for Greek victory and Persian defeat",
  "q": "Herodotus (9.62–63) names 'the chief cause' of the Persian defeat at Plataea. What was it — and name ONE 'structural' factor that modern historians such as Lazenby, Green or Holland stress instead of Herodotus' freedom-versus-slavery framing.",
  "a": "Their lack of armour, 'fighting without it against heavily armed infantry'. Structural factors (any one): Greek use of terrain and bottlenecks; Persian logistics and the 'tyranny of distance' — the army depended on the fleet, so Salamis broke the combined-arms strategy; the hoplite-versus-light-infantry mismatch; Athenian naval tactics (ramming, the periplus, the kyklos); the storms that wrecked some 400 Persian ships; the mixed loyalties of the multi-ethnic Persian force"
 }
},

# =====================================================================
# GREEK WORLD — GAME 2
# =====================================================================
{
 "id": "greek-world-2",
 "title": "Greek World II: Athens, Empire and Sparta",
 "subtitle": "The Greek World 500–440 BC — Game 2 of 2",
 "topic": "The Greek World 500–440 BC",
 "theme": "greek",
 "categories": [
  {
   "name": "The Delian League: origins, aims, organisation",
   "dotpoint": "Delian League: origins, aims, organisation and activities to the Battle of the Eurymedon River, role and contribution of Cimon and Aristides the Just (ACHAH197)",
   "clues": [
    {"q": "On which sacred island was the League founded in 478/7 BC, and its treasury first kept in the temple of Apollo?",
     "a": "Delos"},
    {"q": "Which Athenian, nicknamed 'the Just', assessed the first tribute at 460 talents so fairly that the allies felt 'appropriately and satisfactorily dealt with' (Plutarch)?",
     "a": "Aristides"},
    {"q": "What did the founding members drop into the sea, swearing the alliance would last until it floated to the surface?",
     "a": "Lumps of iron"},
    {"q": "What were the Hellenotamiae, and what is significant about who held the post?",
     "a": "The 'Treasurers of the Greeks' who managed the League treasury — they were always Athenian citizens"},
    {"q": "At the Eurymedon River (c. 467 BC) Cimon won at sea and on land in a single day. What modification had he made to his triremes, and what awkward question did the victory raise for the League?",
     "a": "He widened the decks so each ship carried more hoplites for boarding and landing; with the Persian threat removed, why should the allies keep paying tribute — what was the League now for?"}
   ]
  },
  {
   "name": "From League to Empire",
   "dotpoint": "Transformation of the Delian League into the Athenian Empire (ACHAH198)",
   "clues": [
    {"q": "In what year was the League treasury moved from Delos to Athens?",
     "a": "454 BC"},
    {"q": "Which island's attempt to leave the League (c. 470 BC) did Thucydides (1.98) call 'the first case when the original constitution of the League was broken and an allied city lost its independence'?",
     "a": "Naxos"},
    {"q": "Why did Thasos revolt in 465 BC, and how long did the siege last?",
     "a": "A commercial dispute with Athens over its gold mines and trading posts on the Thracian mainland; three years (465–463 BC)"},
    {"q": "How did the Persian general Megabyzus destroy the Athenian expedition in Egypt in 454 BC?",
     "a": "He diverted the canals of the Nile delta, grounding the Athenian fleet on the island of Prosopitis; the trapped force was annihilated and a relief fleet of 50 ships was destroyed too — 'few out of many' returned"},
    {"q": "Give TWO terms of the Thirty Years' Peace of 446/5 BC.",
     "a": "Any two: Sparta recognised Athens' maritime empire; Athens gave up its holdings on the Peloponnese (Nisaea, Pegae, Troezen, Achaea); each side would not interfere with the other's allies; disputes to go to arbitration; neutral states free to join either side"}
   ]
  },
  {
   "name": "The nature of Athenian imperialism",
   "dotpoint": "Nature of Athenian imperialism, changing relations with allies (ACHAH201)",
   "clues": [
    {"q": "What is the Greek word for the annual tribute paid by the allies?",
     "a": "Phoros"},
    {"q": "What was a cleruchy, and how did it differ from an ordinary Greek colony?",
     "a": "A settlement of Athenians on land confiscated from an allied city who kept their full Athenian citizenship — a permanent garrison and surveillance post, not an independent new polis"},
    {"q": "By the 440s BC only three allies still contributed ships instead of money. Name them.",
     "a": "Chios, Lesbos and Samos"},
    {"q": "Which decree of 446 BC made a Euboean city swear loyalty to 'the Athenian demos' rather than to the League — and which decree required allies to use Athenian coins, weights and measures?",
     "a": "The Chalcis Decree; the Coinage Decree (Clearchus' Decree, c. 449 BC)"},
    {"q": "According to Thucydides (1.75–76), the Athenian envoys at Sparta gave three motives for keeping the empire. Name them.",
     "a": "Fear (security), honour and self-interest (wealth) — 'honour, wealth and fear'"}
   ]
  },
  {
   "name": "Key democratic developments",
   "dotpoint": "Key democratic developments: influence of the thetes, ostracism, citizenship law (ACHAH199)",
   "clues": [
    {"q": "Who were the thetes?",
     "a": "The lowest of Solon's four property classes — poor, landless citizens who after 483 BC rowed the Athenian triremes"},
    {"q": "How many votes had to be cast for an ostracism to be valid, and how long was the exile?",
     "a": "6,000; ten years (the man kept his property and citizenship)"},
    {"q": "Which politician stripped the Areopagus of its political powers in 462/1 BC, and what happened to him soon afterwards?",
     "a": "Ephialtes; he was assassinated (reportedly by Aristodicus of Tanagra)"},
    {"q": "State Pericles' citizenship law of 451 BC.",
     "a": "To be an Athenian citizen you now needed BOTH an Athenian father and an Athenian mother"},
    {"q": "Around the mid-450s Pericles introduced state pay for which service — and why does the textbook call this 'the most direct link between empire and democracy'?",
     "a": "Pay for jurors in the popular courts (later also the Council of 500); it came out of the imperial tribute, and without it poor citizens could not afford to take part"}
   ]
  },
  {
   "name": "The Peloponnesian League and Spartan responses",
   "dotpoint": "Nature, composition and activities of the Peloponnesian League: Spartan responses to Athenian imperialism (ACHAH200)",
   "clues": [
    {"q": "Which wealthy commercial ally, with the League's only large fleet, repeatedly pushed a cautious Sparta into action?",
     "a": "Corinth"},
    {"q": "Did members of the Peloponnesian League pay tribute to Sparta? Explain.",
     "a": "No — the League ran on autarky (self-sufficiency): each member supported its own forces, and there was no central treasury"},
    {"q": "Why was Megara's defection to Athens in 460 BC such a dangerous strategic loss for Sparta?",
     "a": "Megara controlled the passes through the Geraneian mountains — the land route from the Peloponnese into central Greece — so Athens could now block any Spartan invasion of Attica"},
    {"q": "Explain the League's 'bicameral' method of deciding on war.",
     "a": "First the Spartan assembly (Apella) voted; then Sparta summoned a Congress of Allies where each state had one vote — both had to agree before the League went to war"},
    {"q": "In 446 BC King Pleistoanax led a Peloponnesian army into Attica but withdrew without a battle. What was rumoured, and what happened to him back in Sparta?",
     "a": "That Pericles had bribed him to withdraw; he was tried and exiled"}
   ]
  }
 ],
 "final": {
  "category": "Impact of the Persian Wars on Athens and Sparta",
  "dotpoint": "Athens and Sparta — impact of Persian Wars (ACHAH200)",
  "q": "Thucydides (1.102) calls the events at Mount Ithome in 462 BC 'the first open quarrel' between Athens and Sparta. What did Sparta do to the 4,000 Athenian hoplites Cimon had brought to help — and name TWO things Athens did in response.",
  "a": "Sparta sent the Athenians (and only the Athenians) home, fearing their 'adventurous and revolutionary spirit'. Athens (any two): renounced the Hellenic League alliance of 481 BC; allied with Argos, Sparta's enemy; allied with Thessaly; ostracised Cimon (461 BC)"
 }
},

# =====================================================================
# XERXES — GAME 1
# =====================================================================
{
 "id": "xerxes-1",
 "title": "Xerxes I: The Empire and the King",
 "subtitle": "Personalities in their Times — Xerxes — Game 1 of 2",
 "topic": "Personalities in their Times — Xerxes",
 "theme": "xerxes",
 "categories": [
  {
   "name": "Geography, resources and expansion of the empire",
   "dotpoint": "Survey: geography, topography and resources of the Persian Empire; expansion of the Persian Empire (ACHAH105, ACHAH171)",
   "clues": [
    {"q": "What was the name of the Persian royal dynasty, from Cyrus the Great until its fall in 330 BC?",
     "a": "The Achaemenids (Achaemenid dynasty)"},
    {"q": "What was the Persian homeland in south-west Iran called (modern Fars)?",
     "a": "Persis (Pārsa)"},
    {"q": "Which Persian king conquered Egypt in 525 BC?",
     "a": "Cambyses"},
    {"q": "Tribute was paid in kind according to what each province produced. Which province paid in gold dust?",
     "a": "India"},
    {"q": "Herodotus (3.89) records a Persian saying that summed up three kings: 'Darius was a ___, Cambyses a ___, and Cyrus a ___.' Complete it.",
     "a": "A tradesman (out for profit), a tyrant (harsh and careless of his subjects), a father (kind, planning for their well-being)"}
   ]
  },
  {
   "name": "Structures of empire and the concept of kingship",
   "dotpoint": "Survey: overview of Persian political, social and military structures; the Persian concept of kingship (ACHAH172)",
   "clues": [
    {"q": "What did the Greeks call the elite 10,000-strong royal infantry guard, always kept at full strength?",
     "a": "The Immortals"},
    {"q": "What does the title 'satrap' mean?",
     "a": "'Protector of the kingdom' — the governor of a province (satrapy)"},
    {"q": "Who were the 'King's Eyes and Ears'?",
     "a": "Royal inspectors who travelled the empire auditing the satraps' accounts and reporting on their loyalty directly to the king"},
    {"q": "Persian kings were NOT worshipped as gods. On what two pillars did Xerxes' right to rule rest?",
     "a": "The favour of Ahuramazda (divine favour) and Achaemenid descent (bloodline)"},
    {"q": "What was proskynesis, and how did the Greeks misread it?",
     "a": "A gesture of respect before the king (bowing, or hand raised to the lips) marking rank; Greeks, who bowed like that only to gods, took it as worship of the king as a god"}
   ]
  },
  {
   "name": "Religion and religious policy",
   "dotpoint": "Survey: overview of religion in the Persian Empire; key features: religious policy (ACHAH172, ACHAH178)",
   "clues": [
    {"q": "Name the supreme creator god of the Persian kings — the 'Wise Lord'.",
     "a": "Ahuramazda"},
    {"q": "On his palace door-jambs Xerxes calmly stabs a lion-monster. It represents the force the king must defeat to uphold Arta (Truth and Order). Name that force.",
     "a": "Drauga — 'the Lie', chaos and rebellion"},
    {"q": "The Elephantine Papyri show Persian religious tolerance in action during Xerxes' reign. Which community in southern Egypt was protected by royal decree?",
     "a": "A Jewish military colony, which kept its own temple and festivals such as Passover"},
    {"q": "What is the scholarly code of the 'Daiva Inscription' found at Persepolis in 1935, and what does 'daiva' mean?",
     "a": "XPh; 'false gods' or demons"},
    {"q": "Briant, Sancisi-Weerdenburg and Wiesehöfer reject the reading of the Daiva Inscription as proof that Xerxes was an intolerant fanatic. Give TWO reasons they read it as a statement of ideology instead.",
     "a": "Any two: it names no country, cult or date; 'daiva' most likely means the patron gods of political rebels, since religion and politics were inseparable; Xerxes' wider policy was tolerant (Elephantine); its structure — titulary, then the daiva passage, then a moral self-portrait — is a statement about ideal kingship, not a campaign record"}
   ]
  },
  {
   "name": "Family background and succession to kingship",
   "dotpoint": "Background and rise to prominence: family background and status; succession to kingship (ACHAH239, ACHAH240)",
   "clues": [
    {"q": "Who was Xerxes' father?",
     "a": "Darius I"},
    {"q": "Who was Xerxes' mother, the daughter of Cyrus the Great?",
     "a": "Atossa"},
    {"q": "Name the older half-brother who claimed the throne as Darius' eldest son.",
     "a": "Artobazanes"},
    {"q": "What argument, suggested by the exiled Spartan king Demaratus, won Xerxes the succession?",
     "a": "That Xerxes was born after Darius had become king ('born in the purple'), whereas Artobazanes was born when Darius was still a private man"},
    {"q": "The 'Harem' Inscription (XPf) gives Xerxes' own account of his succession. What does it credit — and what does it leave out compared with Herodotus?",
     "a": "It says Darius 'made me the greatest after himself' and that he became king 'by the will of Ahuramazda'; it leaves out any dispute, Demaratus' clever argument and his mother's influence ('Atossa had all the power')"}
   ]
  },
  {
   "name": "Administration of the Persian Empire",
   "dotpoint": "Key features and developments: administration of the Persian Empire (ACHAH175)",
   "clues": [
    {"q": "Which city was the empire's working administrative capital, at one end of the Royal Road (Sardis was at the other)?",
     "a": "Susa"},
    {"q": "Name the empire's gold coin and its silver coin.",
     "a": "The daric (gold) and the siglos (silver)"},
    {"q": "What was the dāta?",
     "a": "The 'King's Law' — a supreme layer of imperial law over contracts, property and treason that sat above local laws"},
    {"q": "What do the Persepolis Fortification and Treasury Tablets reveal about the workforce that built Persepolis?",
     "a": "It was a paid workforce receiving rations scaled to rank — including women and children — not simply slave labour"},
    {"q": "Roughly how many days did a royal message take along the Royal Road from Susa to Sardis, and what was the relay courier system called?",
     "a": "About 15 days; the Barid"}
   ]
  }
 ],
 "final": {
  "category": "Revolts in the empire: Egypt and Babylon",
  "dotpoint": "Key features and developments: revolts in the empire — Egypt, Babylon",
  "q": "The traditional account says Xerxes punished Babylon's revolt (c. 484 BC) by destroying the Esagila temple, diverting the Euphrates and melting down the golden statue of Marduk. Name ONE modern historian who disputes this, and ONE piece of evidence they cite.",
  "a": "Amélie Kuhrt or Russel Granger. Evidence (any one): cuneiform tablets show the title 'King of Babylon' continued in use throughout his reign; there is no evidence the Euphrates was ever diverted; no evidence of permanent destruction of the temple or cult; the 'stolen' statue was probably a minor votive offering, not the main cult idol. (The revolt, led by Bel-shimanni and Shamas-eriba, was crushed by Megabyzus.)"
 }
},

# =====================================================================
# XERXES — GAME 2
# =====================================================================
{
 "id": "xerxes-2",
 "title": "Xerxes II: In Stone, in War and in History",
 "subtitle": "Personalities in their Times — Xerxes — Game 2 of 2",
 "topic": "Personalities in their Times — Xerxes",
 "theme": "xerxes",
 "categories": [
  {
   "name": "Building programme: Persepolis",
   "dotpoint": "Key features and developments: building program — Persepolis (ACHAH177)",
   "clues": [
    {"q": "What does the Greek name 'Persepolis' mean, and was it the empire's ceremonial or its administrative capital?",
     "a": "'City of the Persians'; the ceremonial capital"},
    {"q": "Xerxes built the single entrance to the terrace, flanked by colossal winged human-headed bulls (lamassu). Name it.",
     "a": "The Gate of All Nations (Gate of All Lands)"},
    {"q": "The staircase reliefs Xerxes added to the Apadana show an orderly procession of how many subject delegations bringing gifts?",
     "a": "23"},
    {"q": "Which enormous hall — a 'forest of stone' about 70 m square — did Xerxes begin and his son Artaxerxes I complete?",
     "a": "The Hall of a Hundred Columns (Throne Hall)"},
    {"q": "Persepolis combines Assyrian lamassu, Egyptian cornices and Ionian fluted columns. What is this style called, and what political message did it send?",
     "a": "The eclectic style; that Persia was the unifier and successor of all civilisations — every people's achievements now belonged to the Great King"}
   ]
  },
  {
   "name": "Images and representations of Xerxes as king",
   "dotpoint": "Key features and developments: images and representations of Xerxes as king",
   "clues": [
    {"q": "In the Treasury Relief the enthroned king's feet rest on what, so that they never touch the bare earth?",
     "a": "A footstool"},
    {"q": "The king and the crown prince behind him each hold which flower, a symbol of eternity and dynastic continuity?",
     "a": "The lotus"},
    {"q": "Achaemenid royal art is all 'orderly processions, dignity and calm power'. Unlike Assyrian art, what does it never show the king doing?",
     "a": "Fighting in the chaos of battle (or any violence, defeat or specific historical event)"},
    {"q": "At the Hall of a Hundred Columns and on Xerxes' tomb at Naqsh-e Rustam, who is shown lifting up the king's throne — and what is the claim?",
     "a": "Representatives of the subject nations of the empire; that the empire willingly supports the king — what Margaret Cool Root called 'a new vision of hierarchical order and kingship on earth'"},
    {"q": "Emma Bridges (Imagining Xerxes) points out something striking about the Greek campaign in the Persian royal record. What is it?",
     "a": "The Persian inscriptions and sculpture give it 'no place' at all — the war that defines the Greek image of Xerxes is never mentioned; instead they stress the seamless continuity of Darius' and Xerxes' reigns"}
   ]
  },
  {
   "name": "Foreign policy: the invasion of the Greek mainland",
   "dotpoint": "Key features and developments: foreign policy — role in the invasion of the Greek mainland (ACHAH176)",
   "clues": [
    {"q": "In what year did Xerxes cross into Europe and fight at Thermopylae and Salamis?",
     "a": "480 BC"},
    {"q": "How did Xerxes get his army from Asia into Europe across the Hellespont?",
     "a": "On two pontoon bridges — hundreds of boats lashed side by side and joined by cables with a roadway laid on top (the first pair was wrecked by a storm)"},
    {"q": "After a storm destroyed his first bridges, what did Xerxes order done to the Hellespont (Herodotus 7.35–36)?",
     "a": "It was to receive 300 lashes and have a pair of fetters thrown into it, while the whip-men called it a 'salt and bitter stream'"},
    {"q": "At the council of war Mardonius urged invasion. Which relative of Xerxes, commander of the palace guard, argued against it?",
     "a": "His uncle Artabanus"},
    {"q": "Herodotus charges Xerxes with cowardice for leaving Greece after Salamis. Give TWO points revisionist historians use to defend the withdrawal as sound strategy.",
     "a": "Any two: in Persian ideology the survival of the King was paramount; he left Mardonius with a picked force to continue the war in 479 BC; his fear that the Greeks would break the Hellespont bridges and cut his supply line was a real logistical danger; the royal inscriptions present a self-controlled king and 'competent military strategist'"}
   ]
  },
  {
   "name": "Relationships and the death of Xerxes",
   "dotpoint": "Key features and developments: relationship with prominent Persians and non-Persians; manner and impact of his death (ACHAH247)",
   "clues": [
    {"q": "Which general — Xerxes' brother-in-law and the chief promoter of the invasion — was left behind with a picked force after Salamis?",
     "a": "Mardonius"},
    {"q": "Which Carian queen commanded ships for Xerxes at Salamis, had advised him not to fight at sea, and was afterwards trusted to escort his sons to Ephesus?",
     "a": "Artemisia of Halicarnassus"},
    {"q": "Herodotus tells how Xerxes' wife Amestris mutilated the wife of one of Xerxes' brothers after Xerxes' affair with that brother's daughter Artaynta. Name the brother, who then fled to Bactria and was killed.",
     "a": "Masistes"},
    {"q": "Name the two conspirators who murdered Xerxes in his bedchamber in August 465 BC.",
     "a": "Artabanus the chiliarch (captain of the royal bodyguard) and the eunuch chamberlain Aspamitres"},
    {"q": "What structural weakness of the Persian system did the bloody succession of 465 BC expose, and what happened to the crown prince Darius?",
     "a": "There was no formal law of succession; Artabanus tricked the younger son Artaxerxes into believing Darius was the murderer, and Artaxerxes had him killed (then killed Artabanus and ruled for about 40 years)"}
   ]
  },
  {
   "name": "Ancient and modern interpretations; assessment and legacy",
   "dotpoint": "Evaluation: ancient and modern images and interpretations of Xerxes; assessment of his life and reign; legacy (ACHAH248–253)",
   "clues": [
    {"q": "Which Athenian playwright staged The Persians in 472 BC, only eight years after Salamis?",
     "a": "Aeschylus"},
    {"q": "What Greek concept — arrogant pride that overreaches human limits and is punished by the gods — frames both Aeschylus' and Herodotus' portraits of Xerxes?",
     "a": "Hubris"},
    {"q": "Herodotus' story of Pythius the Lydian illustrates which 'charge' against Xerxes' character — and what did Xerxes do?",
     "a": "Sadism; when Pythius begged that his eldest son be spared service, Xerxes had the son cut in half and marched the army out between the two halves"},
    {"q": "Which historian wrote that 'the fine promise of Xerxes' younger years had not been fulfilled' and that his character 'disintegrated' — and which wrote that he 'bequeathed to his heirs an empire whose boundaries were to remain stable for almost 150 years'?",
     "a": "A. T. Olmstead; Richard Stoneman"},
    {"q": "A. R. Burn gives a balanced verdict on Herodotus' portrait of Xerxes as a prince 'born to rule but not to tolerate opposition'. What does Burn call that portrait?",
     "a": "A 'well-conceived literary portrait' that 'may have much truth in it'"}
   ]
  }
 ],
 "final": {
  "category": "Evaluating the sources: Herodotus and Persepolis",
  "dotpoint": "One particular source or type of source: Herodotus Books VII–IX and Persepolis — value and limitations; problems of evidence",
  "q": "Give ONE strength and ONE limitation of Herodotus as a source for Xerxes, and ONE strength and ONE limitation of Persepolis.",
  "a": "Herodotus — strengths (any): the only continuous narrative of the invasion; close in time and drew on eyewitnesses; preserves Persian voices such as Demaratus and Artemisia. Limitations (any): Greek and hostile; shaped by the hubris–nemesis frame; reports private scenes he could not have witnessed. Persepolis — strengths (any): a contemporary Persian voice in the king's own words; reveals royal ideology; the tablets reveal the real economy. Limitations (any): pure ideology with no events or chronology; royal propaganda; never mentions the Greek defeat"
 }
}
]
