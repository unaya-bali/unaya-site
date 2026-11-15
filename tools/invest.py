import sys,re; sys.path.insert(0,'/tmp/claude-0/-home-claude/fb21bd82-28de-566e-9e55-058e68a3af45/scratchpad/gen')
from ui import ic
R='/home/claude/unaya-site/src/pages/'
old=open(R+'fr/Investir.html').read()
STYLE=old[old.find('<style>'):old.find('</style>')+8]
HERO_IMG='/assets/images/yuga-drone.jpg'
BUY='https://images.unsplash.com/photo-1693576588461-3ad3dd88371e?w=900&q=80&auto=format&fit=crop'
BUILD='https://images.unsplash.com/photo-1621511075938-f03482369feb?w=900&q=80&auto=format&fit=crop'
CTA='https://images.unsplash.com/photo-1581094488379-6a10d04c0f04?w=2000&q=80&auto=format&fit=crop'
S={ # sources (official first)
 'pp18':('PP n° 18/2021 — droits fonciers, Hak Pakai, HGB (JDIH Kemenko Infrastruktur)','https://jdih.kemenkoinfra.go.id/en/peraturan-pemerintah-republik-indonesia-no-18-tahun-2021'),
 'kep1241':('Kepmen ATR/BPN 1241/SK-HK.02/IX/2022 — prix minimum pour les étrangers (Hukumonline)','https://www.hukumonline.com/klinik/a/foreigners-may-purchase-residential-houses-with-the-following-minimum-prices-lt63eb7faade8c6'),
 'bkpm':('Règlement BKPM n° 5/2025 — capital d\'une PT PMA (analyse Withers)','https://www.withersworldwide.com/en-gb/insight/read/indonesia-eases-foreign-capital-rules-key-takeaways-from-bkpm-regulation-no-5-of-2025'),
 'oss':('OSS — guichet officiel des licences (NIB, KBLI)','https://oss.go.id'),
 'perda':('Bali : Perda contrôle de la conversion des terres productives et interdiction des prête-noms (DPRD Bali, 29/12/2025)','https://barometerbali.com/dprd-bali-resmi-sahkan-perda-pengendalian-alih-fungsi-lahan/'),
 'instr':('Gouvernement de Bali — instruction interdisant la conversion des terres agricoles','https://www.baliprov.go.id/web/gubernur-bali-terbitkan-instruksi-larangan-alih-fungsi-lahan-pertanian'),
 'pbg':('Indonesia.go.id — PBG (permis de construire) et SLF, PP 16/2021','https://indonesia.go.id/kategori/investment/2626/procedures-for-applying-building-approval?lang=2'),
 'kemenpar':('Ministère du Tourisme — mise en règle des hébergements, échéance 31/05/2026 (Bisnis.com, 15/05/2026)','https://ekonomi.bisnis.com/read/20260515/12/1973137/tarik-ulur-penataan-izin-usaha-akomodasi-vila-cs/1'),
 'uu18':('Loi n° 18/2025 sur le tourisme — synthèse (Bali Property Rules)','https://balipropertyrules.com/guides/uu-18-2025-tourism-law-bali-foreigners/'),
 'pbjt':('Loi n° 1/2022 (HKPD) — PBJT services d\'hébergement, villas incluses, 10 % max. (DDTC)','https://news.ddtc.co.id/uu-hkpd-atur-ulang-ketentuan-pajak-atas-jasa-hotel-ini-perinciannya-35111'),
 'pph42':('PP n° 34/2017 — impôt final 10 % sur la location de terrains/bâtiments (DDTC)','https://news.ddtc.co.id/berita/nasional/1802427/pph-final-sewa-tanahbangunan-dipotong-penyewa-begini-aturannya'),
 'pphjual':('DJP (impôts) — impôt final du vendeur 2,5 %, PP n° 34/2016','https://www.pajak.go.id/index.php/en/node/110181'),
 'yield':('Rendements nets observés 2026 — Bali Villa Select (étude de marché)','https://balivillaselect.com/bali-villa-net-yield-2026-what-actually-pays'),
 'kbli18':('Province de Bali — 18 codes d\'activité (KBLI) fermés aux nouvelles PT PMA dans OSS, mai 2026 (NusaBali, 22/07/2026)','https://www.nusabali.com/berita/226314/gubernur-koster-batasi-akses-oss-bagi-pma-lindungi-ruang-usaha-umkm-bali'),
 'cost':('Coûts de construction 2026 — guide Villa Bali Sale (agence immobilière)','https://www.villabalisale.com/blog/-bali-villa-investment-cost-guide-2026'),
}
SEN={'kbli18':'Bali province — 18 business codes (KBLI) closed to new PT PMA in OSS, May 2026 (NusaBali, 22/07/2026)','pp18':'Government Regulation 18/2021 — land rights, Hak Pakai, HGB (JDIH Kemenko Infrastruktur)','kep1241':'ATR/BPN Decree 1241/SK-HK.02/IX/2022 — minimum prices for foreigners (Hukumonline)','bkpm':'BKPM Regulation 5/2025 — PT PMA capital (Withers analysis)','oss':'OSS — official licensing portal (NIB, KBLI)','perda':'Bali bylaw on productive-land conversion and nominee ban (Bali DPRD, 29 Dec 2025)','instr':'Bali Provincial Government — instruction banning conversion of farmland','pbg':'Indonesia.go.id — PBG building approval and SLF, Government Regulation 16/2021','kemenpar':'Ministry of Tourism — accommodation licensing, 31 May 2026 deadline (Bisnis.com, 15 May 2026)','uu18':'Tourism Law 18/2025 — summary (Bali Property Rules)','pbjt':'Law 1/2022 (HKPD) — PBJT accommodation services, villas included, max 10% (DDTC)','pph42':'Government Regulation 34/2017 — 10% final tax on land/building rental (DDTC)','pphjual':'DGT (tax office) — 2.5% final tax for the seller, Government Regulation 34/2016','yield':'Observed net yields 2026 — Bali Villa Select (market study)','cost':'Construction costs 2026 — Villa Bali Sale guide (real-estate agency)'}

def sup(k,lang): 
    keys=list(S); n=keys.index(k)+1
    return f'<a class="iq-src" href="#sources" title="{S[k][0] if lang=="fr" else SEN[k]}">[{n}]</a>'

T={}
T['fr']=dict(
 title='Investir à Bali — Unaya Build',
 h1='Investir à Bali : vos questions, nos réponses',
 sub="Détenir un bien quand on est étranger, zonage, permis, licence de location, taxes, coûts et rendement : l'essentiel, vérifié sur les textes en vigueur.",
 b1='Demander une estimation de revenus', b2='Nous contacter', contact='/fr/contact/',
 verified='Règles vérifiées le 27 octobre 2026 — elles changent souvent, revérifiez avant d\'investir.',
 themes=[
  ('detenir','home','Détenir un bien quand on est étranger',None,[
   ("Un étranger peut-il être pleinement propriétaire d'un terrain à Bali ?","Non. La pleine propriété (<em>Hak Milik</em>) est réservée aux citoyens indonésiens. Un étranger peut en revanche louer un terrain à long terme (leasehold), détenir un droit d'usage (<em>Hak Pakai</em>) sous conditions, ou investir via une société à capitaux étrangers (PT PMA)."+sup('pp18','fr')),
   ("Qu'est-ce que le leasehold (Hak Sewa) ?","Un bail de longue durée signé devant notaire avec le propriétaire indonésien du terrain : souvent 20 à 30 ans, avec une option de prolongation à prévoir dans le contrat. Vous pouvez construire, louer et revendre le bail restant. Points clés à faire écrire : durée, prix de la prolongation, droit de sous-louer et de céder le bail, sort de la construction en fin de bail. Le loyer du bail est soumis à un impôt final de 10 % (PPh 4(2))."+sup('pph42','fr')),
   ("Qu'est-ce que le Hak Pakai pour un étranger ?","Un droit d'usage d'une maison d'habitation, ouvert aux étrangers titulaires d'un titre de séjour, pour y vivre (pas pour en faire une activité commerciale). Il est accordé pour une durée limitée, prolongeable et renouvelable. Un prix minimum s'applique : à Bali, 5 milliards IDR pour une maison individuelle."+sup('pp18','fr')+sup('kep1241','fr')),
   ("Qu'est-ce qu'une PT PMA et peut-elle louer aux touristes ?","Une société indonésienne à capitaux étrangers. Elle peut détenir un droit de construire (<em>Hak Guna Bangunan</em>, HGB) sur un terrain. Depuis le règlement BKPM n° 5/2025, le capital libéré minimum est de 2,5 milliards IDR par activité. <strong>Attention : depuis mai 2026, Bali n'accepte plus dans OSS les nouvelles demandes de PT PMA pour 18 activités</strong>, dont les hôtels de moins de 6 000 m², « l'autre hébergement » et la location de biens immobiliers. Une PT PMA créée aujourd'hui ne peut donc plus obtenir de licence pour louer une villa à Bali. Celles qui avaient déjà leur licence la gardent."+sup('kbli18','fr')+sup('bkpm','fr')+sup('pp18','fr')),
   ("Peut-on acheter au nom d'un ami indonésien (prête-nom) ?","À éviter absolument. Le bien appartient légalement au prête-nom, vous n'avez aucune protection, et Bali a adopté fin 2025 un règlement qui interdit explicitement les montages par prête-nom, avec des sanctions y compris pour les notaires qui les facilitent."+sup('perda','fr')),
  ]),
  ('zonage','map','Terrain et zonage',None,[
   ("Que signifient les couleurs du zonage ?","Chaque parcelle a une destination fixée par le plan d'urbanisme (RTRW / RDTR) : zones agricoles et vertes (souvent en vert / jaune), zones d'habitation, zones touristiques et commerciales. Une villa louée aux touristes doit être sur une zone qui autorise l'hébergement touristique."),
   ("Comment vérifier le zonage d'un terrain ?","Avant tout engagement : demandez le certificat de propriété (SHM, HGB…) et faites-le vérifier au cadastre (BPN) par le notaire, contrôlez la destination de la parcelle dans le plan de détail (RDTR) et la conformité d'usage du terrain (KKPR) via le système OSS."+sup('oss','fr')),
   ("Peut-on encore construire une villa sur une rizière ?","De moins en moins. Bali a interdit la conversion des terres agricoles (instruction du Gouverneur) puis adopté fin 2025 un règlement provincial qui contrôle la conversion des terres productives et interdit les prête-noms. Les exceptions visent surtout les projets publics et l'habitation des propriétaires locaux, pas les villas commerciales."+sup('instr','fr')+sup('perda','fr')),
  ]),
  ('permis','doc','Permis de construire et licence de location',None,[
   ("Quels permis pour construire ?","Le <strong>PBG</strong> (approbation du bâtiment, qui a remplacé l'ancien IMB) avant les travaux, puis le <strong>SLF</strong> (certificat de conformité) une fois le bâtiment terminé, conformément au PP n° 16/2021. Une villa sans PBG et SLF ne peut pas obtenir de licence de location."+sup('pbg','fr')),
   ("Quelle licence pour louer aux touristes ?","Une activité d'hébergement enregistrée dans le système OSS : numéro d'entreprise (NIB) avec le code d'activité (KBLI) adapté, plus les inscriptions fiscales (NPWP, et NPWPD auprès de la régence pour la PBJT). Pour un étranger, la porte s'est fermée : depuis mai 2026, Bali bloque ces codes pour les nouvelles PT PMA, et le <em>pondok wisata</em> (chambres chez l'habitant) est réservé aux Indonésiens. La solution la plus simple : confier la villa à Unaya Villa Management, qui la loue à la nuit pour vous, en règle."+sup('kbli18','fr')+sup('oss','fr')+sup('uu18','fr')),
   ("Que se passe-t-il sans licence ?","Le ministère du Tourisme a lancé en 2026 la mise en règle des villas et hébergements listés sur les plateformes : les annonces sans NIB/KBLI vérifiés peuvent être retirées d'Airbnb, Booking.com, etc. (échéance repoussée au 31 mai 2026). Des villas non autorisées ont aussi été mises sous scellés."+sup('kemenpar','fr')+sup('uu18','fr')),
  ]),
  ('taxes','wallet','Taxes',None,[
   ("Quelle taxe sur les nuitées ?","La <strong>PBJT</strong> (taxe sur les services d'hébergement) : 10 % du prix des nuits dans la régence de Badung (Uluwatu, Canggu, Seminyak…), villas comprises. Elle est généralement incluse dans le prix affiché et reversée chaque mois à la régence."+sup('pbjt','fr')),
   ("Et l'impôt sur les revenus locatifs ?","Il dépend de la structure. Une PT PMA paie l'impôt sur les sociétés sur son bénéfice (taux normal 22 %, régimes réduits possibles pour les petites entreprises), et les dividendes versés à l'étranger subissent une retenue à la source (réduite par les conventions fiscales). Un particulier qui loue un terrain ou un bâtiment est soumis à un impôt final de 10 % sur le loyer."+sup('pph42','fr')+" Faites valider votre cas par un comptable indonésien."),
   ("Quelles taxes à l'achat ?","Le vendeur paie un impôt final de 2,5 % du prix de vente ; l'acheteur paie le droit de mutation (BPHTB), jusqu'à 5 %, fixé par la régence. Ces taxes concernent les transferts de droits (pleine propriété, HGB), pas un simple bail."+sup('pphjual','fr')),
  ]),
  ('couts','calc','Coûts d\'achat et de construction',None,[
   ("Combien coûte la construction d'une villa ?","Ordres de grandeur du marché en 2026 (hors terrain, hors meubles) : environ 850 à 1 100 USD/m² pour une villa standard, 1 200 à 1 600 USD/m² pour du haut de gamme, 1 800 USD/m² et plus pour du luxe. Ce sont des fourchettes d'agences, pas des chiffres officiels : seul un devis détaillé fait foi."+sup('cost','fr')),
   ("Et le terrain en leasehold ?","Les prix varient énormément selon la zone, l'accès et la vue. Dans les quartiers recherchés du sud (Berawa, Bingin…), les annonces affichent souvent 25 à 60 millions IDR par are (100 m²) et par an. Comptez aussi le notaire, la vérification juridique, les permis, la création éventuelle de la PT PMA et l'ameublement."+sup('cost','fr')),
  ]),
  ('rendement','price','Rendement réaliste',None,[
   ("Comment se calcule le revenu net d'une villa ?","Revenu brut = nuits louées × prix moyen par nuit. On retire ensuite les commissions des plateformes (≈ 15 %), la PBJT (10 %), les frais de gestion, le personnel, l'électricité, l'entretien et une réserve pour le mobilier. Il reste en général 40 à 50 % du revenu brut avant impôts."+sup('yield','fr')),
   ("Quel rendement espérer ?","Les études de marché 2026 situent le rendement net d'une villa bien gérée entre 6 et 10 % par an une fois stabilisée (2e-3e année), et nettement moins la première année. Méfiez-vous des promesses de 15-20 % : elles ignorent souvent les commissions, les taxes et les mois creux."+sup('yield','fr')),
  ]),
  ('etapes','check','Les étapes d\'un achat et le rôle du notaire',None,[
   ("Quel est le rôle du notaire ?","Le notaire (<em>Notaris</em>, et <em>PPAT</em> pour les transferts de droits fonciers) vérifie le certificat au cadastre (BPN), rédige et enregistre l'acte (bail notarié ou acte de vente), calcule et encaisse les taxes de transfert. Il ne remplace pas une vérification complète : zonage, permis, accès, voisinage et litiges sont à contrôler en plus, idéalement avec un avocat indépendant."),
  ]),
 ],
 cmp_h='Les 3 façons de détenir', cmp=[('', 'Leasehold','Hak Pakai','PT PMA + HGB'),('Pour qui','Tout étranger','Étranger résident','Société à capitaux étrangers'),('Usage','Habitation ou location (avec licence)','Habitation uniquement','Exploitation commerciale (location)'),('Durée','Selon le bail (souvent 20-30 ans)','Limitée, prolongeable','Limitée, prolongeable'),('Louer aux touristes','Via une PT PMA licenciée','Non','Oui, avec licence')],
 zones=[('#7FA36B','Vert / agricole','Pas de villa commerciale'),('#E8C66A','Habitation','Maison, selon les règles locales'),('#D2A48C','Tourisme / commerce','Hébergement touristique possible')],
 zones_note="Les couleurs exactes varient selon les plans : seul le plan officiel (RDTR) fait foi.",
 costs=[('calc','850 – 1 100','USD/m² — standard'),('home','1 200 – 1 600','USD/m² — haut de gamme'),('star','1 800 +','USD/m² — luxe'),('map','25 – 60 M','IDR/are/an — leasehold, sud de Bali')],
 costs_note="Fourchettes de marché 2026 (agences), à confirmer par devis.",
 ex_h='Exemple chiffré (hypothèses prudentes)', ex_p="Villa de 3 chambres, prix moyen 3 000 000 IDR/nuit (taxe incluse), 65 % d'occupation, gestion complète Unaya à 18 %.",
 ex=[('Nuits louées','≈ 237 nuits'),('Revenu brut','≈ 711 M IDR'),('− Commissions des plateformes (15 %)','≈ 107 M'),('− PBJT 10 % (incluse dans le prix)','≈ 65 M'),('− Honoraires Unaya 18 %','≈ 97 M'),('− Personnel, énergie, entretien, réserve (≈ 20 %)','≈ 142 M'),('= Revenu net avant impôts','≈ 300 M IDR / an')],
 ex_note="Exemple illustratif, pas une promesse : chaque villa est différente. Demandez une estimation personnalisée.",
 steps=[('Projet','Zone, budget, villa existante ou construction'),('Vérifications','Certificat, zonage, permis, accès, litiges'),('Offre','Prix, conditions, durée du bail, prolongation'),('Notaire','Contrat, enregistrement, taxes'),('Licences','NIB/KBLI, PBG/SLF, NPWPD : à vérifier avant l’achat'),('Location','Mise en service et gestion')],
 build_h='Acheter une villa ou faire construire ?', buy=('Acheter une villa existante','Plus rapide : louable presque tout de suite, mais titres, permis et état du bâtiment à vérifier de près.'), build=('Faire construire','Une villa pensée pour la location, souvent le meilleur rendement, mais plus long : terrain, plans, permis, chantier.'),
 acc_h='Notre accompagnement Unaya Build', acc=[('map','Recherche et vérification',"Terrain ou villa, zonage, titres : nous vous aidons à poser les bonnes questions."),('tools','Construction et rénovation',"Suivi du chantier sur place, budget et délais."),('doc','Licences',"PBG, SLF, NIB, NPWPD : nous coordonnons les démarches avec vos conseillers."),('key','Gestion locative',"Unaya Management loue, entretient et vous rend des comptes chaque mois.")],
 form_h='Demander une estimation de revenus', form_p="Décrivez la villa (existante ou en projet) : nous vous envoyons une estimation de revenus réaliste, gratuitement et sans engagement.",
 f=dict(zone='Zone',zones=['Uluwatu / Jimbaran','Tanah Lot / Canggu West','Seminyak / Kerobokan','Autre zone'],etat='Votre villa',etats=['Villa existante','Villa en projet / en construction','Terrain seul'],ch='Nombre de chambres',pool='Piscine',pools=['Oui','Non','Pas encore décidé'],photos='Photos (5 maximum, 10 Mo au total)',email='E-mail',nom='Nom (facultatif)',msg='Message (facultatif)',consent="J'accepte que mes données soient utilisées pour répondre à ma demande (politique de confidentialité).",send='Envoyer ma demande',pick='Choisir'),
 cta_h='Parlons de votre projet', cta_p="Chaque projet est différent. Écrivez-nous : nous vous répondons sous 24 h pour un premier échange, sans engagement.",
 src_h='Sources', disc="Cette page est fournie à titre d'information générale. Elle ne constitue ni un conseil juridique, ni un conseil fiscal, ni un conseil en investissement. Les règles indonésiennes évoluent souvent : faites valider votre projet par un notaire, un avocat et un comptable indonésiens avant tout engagement.",
)
T['en']=dict(
 title='Invest in Bali — Unaya Build',
 h1='Investing in Bali: your questions answered',
 sub="Owning as a foreigner, zoning, permits, rental licence, taxes, costs and returns: the essentials, checked against the rules in force.",
 b1='Request an income estimate', b2='Contact us', contact='/contact/',
 verified='Rules checked on 27 October 2026 — they change often, check again before investing.',
 themes=[
  ('detenir','home','Owning property as a foreigner',None,[
   ("Can a foreigner fully own land in Bali?","No. Freehold (<em>Hak Milik</em>) is reserved for Indonesian citizens. A foreigner can instead lease land long-term (leasehold), hold a right of use (<em>Hak Pakai</em>) under conditions, or invest through a foreign-owned company (PT PMA)."+sup('pp18','en')),
   ("What is leasehold (Hak Sewa)?","A long-term lease signed before a notary with the Indonesian landowner: often 20 to 30 years, with an extension option to be written into the contract. You can build, rent out and resell the remaining lease. Key points to put in writing: term, extension price, right to sublet and assign, what happens to the building at the end. Lease payments are subject to a 10% final tax (PPh 4(2))."+sup('pph42','en')),
   ("What is Hak Pakai for a foreigner?","A right to use a residential house, open to foreigners holding a residence permit, to live in (not to run a business). It is granted for a limited term, extendable and renewable. A minimum price applies: in Bali, IDR 5 billion for a landed house."+sup('pp18','en')+sup('kep1241','en')),
   ("What is a PT PMA and can it rent to tourists?","An Indonesian foreign-owned company. It can hold a right to build (<em>Hak Guna Bangunan</em>, HGB) on land. Since BKPM Regulation 5/2025, the minimum paid-up capital is IDR 2.5 billion per business line. <strong>Note: since May 2026, Bali no longer accepts new PT PMA applications in OSS for 18 business lines</strong>, including hotels under 6,000 m², \"other accommodation\" and renting out real estate. A PT PMA set up today can therefore no longer get a licence to rent out a villa in Bali. Those already licensed keep their licence."+sup('kbli18','en')+sup('bkpm','en')+sup('pp18','en')),
   ("Can I buy in an Indonesian friend's name (nominee)?","Avoid it. The property legally belongs to the nominee, you have no protection, and in late 2025 Bali passed a bylaw explicitly banning nominee arrangements, with sanctions including for notaries who facilitate them."+sup('perda','en')),
  ]),
  ('zonage','map','Land and zoning',None,[
   ("What do the zoning colours mean?","Each plot has a use set by the spatial plan (RTRW / RDTR): agricultural and green zones (often green / yellow), residential zones, tourism and commercial zones. A villa rented to tourists must be in a zone that allows tourist accommodation."),
   ("How do I check a plot's zoning?","Before committing: ask for the land certificate (SHM, HGB…) and have the notary check it at the land office (BPN), check the plot's use in the detailed plan (RDTR) and the land-use conformity (KKPR) through the OSS system."+sup('oss','en')),
   ("Can you still build a villa on a rice field?","Less and less. Bali banned the conversion of farmland (Governor's instruction), then passed a provincial bylaw in late 2025 controlling the conversion of productive land and banning nominees. Exceptions mainly cover public projects and local owners' own homes, not commercial villas."+sup('instr','en')+sup('perda','en')),
  ]),
  ('permis','doc','Building permits and rental licence',None,[
   ("Which permits do I need to build?","The <strong>PBG</strong> (building approval, which replaced the old IMB) before works, then the <strong>SLF</strong> (certificate of worthiness) once the building is finished, under Government Regulation 16/2021. A villa without PBG and SLF cannot get a rental licence."+sup('pbg','en')),
   ("Which licence do I need to rent to tourists?","An accommodation business registered in the OSS system: business ID (NIB) with the right activity code (KBLI), plus tax registrations (NPWP, and NPWPD with the regency for PBJT). For a foreigner the door has closed: since May 2026 Bali blocks these codes for new PT PMA, and <em>pondok wisata</em> (rooms in a local home) is reserved for Indonesians. The simplest solution: entrust the villa to Unaya Villa Management, which rents it out by the night for you, legally."+sup('kbli18','en')+sup('oss','en')+sup('uu18','en')),
   ("What happens without a licence?","In 2026 the Ministry of Tourism started bringing villas and accommodation listed on platforms into line: listings without verified NIB/KBLI can be removed from Airbnb, Booking.com, etc. (deadline pushed back to 31 May 2026). Unlicensed villas have also been sealed off."+sup('kemenpar','en')+sup('uu18','en')),
  ]),
  ('taxes','wallet','Taxes',None,[
   ("What tax applies to nightly stays?","<strong>PBJT</strong> (tax on accommodation services): 10% of the room price in Badung regency (Uluwatu, Canggu, Seminyak…), villas included. It is usually included in the displayed price and paid monthly to the regency."+sup('pbjt','en')),
   ("And income tax on rental income?","It depends on the structure. A PT PMA pays corporate income tax on its profit (standard rate 22%, reduced regimes possible for small companies), and dividends paid abroad bear withholding tax (reduced by tax treaties). An individual renting out land or a building pays a 10% final tax on the rent."+sup('pph42','en')+" Have your case checked by an Indonesian accountant."),
   ("Which taxes apply when buying?","The seller pays a 2.5% final tax on the sale price; the buyer pays transfer duty (BPHTB), up to 5%, set by the regency. These apply to transfers of rights (freehold, HGB), not to a simple lease."+sup('pphjual','en')),
  ]),
  ('couts','calc','Purchase and construction costs',None,[
   ("How much does it cost to build a villa?","Market ranges for 2026 (excluding land and furniture): about USD 850–1,100/m² for a standard villa, USD 1,200–1,600/m² for upscale, USD 1,800/m² and more for luxury. These are agency ranges, not official figures: only a detailed quote counts."+sup('cost','en')),
   ("And leasehold land?","Prices vary hugely with area, access and view. In sought-after southern areas (Berawa, Bingin…), listings often show IDR 25–60 million per are (100 m²) per year. Also budget for the notary, legal due diligence, permits, setting up the PT PMA if needed, and furniture."+sup('cost','en')),
  ]),
  ('rendement','price','Realistic returns',None,[
   ("How is a villa's net income calculated?","Gross income = nights booked × average nightly rate. Then deduct platform commissions (≈ 15%), PBJT (10%), management fees, staff, electricity, maintenance and a furniture reserve. Usually 40 to 50% of gross income remains before income tax."+sup('yield','en')),
   ("What return can I expect?","2026 market studies put the net yield of a well-managed villa at 6 to 10% a year once stabilised (year 2-3), and noticeably less in year one. Be wary of 15-20% promises: they often ignore commissions, taxes and low months."+sup('yield','en')),
  ]),
  ('etapes','check','Buying step by step, and the notary\'s role',None,[
   ("What does the notary do?","The notary (<em>Notaris</em>, and <em>PPAT</em> for land-right transfers) checks the certificate at the land office (BPN), drafts and registers the deed (notarial lease or deed of sale), and calculates and collects transfer taxes. This is not a full due diligence: zoning, permits, access, neighbours and disputes must be checked as well, ideally with an independent lawyer."),
  ]),
 ],
 cmp_h='Three ways to hold property', cmp=[('', 'Leasehold','Hak Pakai','PT PMA + HGB'),('For whom','Any foreigner','Resident foreigner','Foreign-owned company'),('Use','Living or renting (with licence)','Living only','Commercial operation (rental)'),('Term','Per the lease (often 20-30 yrs)','Limited, extendable','Limited, extendable'),('Rent to tourists','Through a licensed PT PMA','No','Yes, with licence')],
 zones=[('#7FA36B','Green / agricultural','No commercial villa'),('#E8C66A','Residential','Home, per local rules'),('#D2A48C','Tourism / commercial','Tourist accommodation possible')],
 zones_note="Exact colours vary between plans: only the official plan (RDTR) counts.",
 costs=[('calc','850 – 1,100','USD/m² — standard'),('home','1,200 – 1,600','USD/m² — upscale'),('star','1,800 +','USD/m² — luxury'),('map','25 – 60 M','IDR/are/year — leasehold, south Bali')],
 costs_note="2026 market ranges (agencies), to be confirmed by quotes.",
 ex_h='Worked example (cautious assumptions)', ex_p="3-bedroom villa, average rate IDR 3,000,000/night (tax included), 65% occupancy, Unaya full management at 18%.",
 ex=[('Nights booked','≈ 237 nights'),('Gross income','≈ IDR 711 M'),('− Platform commissions (15%)','≈ 107 M'),('− PBJT 10% (included in price)','≈ 65 M'),('− Unaya fees 18%','≈ 97 M'),('− Staff, energy, maintenance, reserve (≈ 20%)','≈ 142 M'),('= Net income before income tax','≈ IDR 300 M / year')],
 ex_note="Illustrative example, not a promise: every villa is different. Ask for a personalised estimate.",
 steps=[('Project','Area, budget, existing villa or build'),('Due diligence','Certificate, zoning, permits, access, disputes'),('Offer','Price, terms, lease length, extension'),('Notary','Contract, registration, taxes'),('Licences','NIB/KBLI, PBG/SLF, NPWPD : à vérifier avant l’achat'),('Rental','Launch and management')],
 build_h='Buy a villa or build one?', buy=('Buy an existing villa','Faster: rentable almost straight away, but titles, permits and building condition need close checks.'), build=('Build','A villa designed for rental, often the best return, but longer: land, plans, permits, works.'),
 acc_h='How Unaya Build supports you', acc=[('map','Search and checks',"Land or villa, zoning, titles: we help you ask the right questions."),('tools','Construction and renovation',"On-site project follow-up, budget and timing."),('doc','Licences',"PBG, SLF, NIB, NPWPD: we coordinate the steps with your advisers."),('key','Rental management',"Unaya Management rents, maintains and reports to you every month.")],
 form_h='Request an income estimate', form_p="Describe the villa (existing or planned): we'll send you a realistic income estimate, free and with no obligation.",
 f=dict(zone='Area',zones=['Uluwatu / Jimbaran','Tanah Lot / Canggu West','Seminyak / Kerobokan','Other area'],etat='Your villa',etats=['Existing villa','Planned / under construction','Land only'],ch='Number of bedrooms',pool='Pool',pools=['Yes','No','Not decided yet'],photos='Photos (max 5, 10 MB in total)',email='Email',nom='Name (optional)',msg='Message (optional)',consent='I agree that my data is used to answer my request (privacy policy).',send='Send my request',pick='Choose'),
 cta_h="Let's talk about your project", cta_p="Every project is different. Write to us: we reply within 24 hours for a first, no-obligation conversation.",
 src_h='Sources', disc="This page is provided for general information. It is not legal, tax or investment advice. Indonesian rules change often: have your project checked by an Indonesian notary, lawyer and accountant before committing.",
)
L="font-size: 12px; letter-spacing: 0.16em; text-transform: uppercase; color: #8B5A46; display: flex; flex-direction: column; gap: 6px;"
I="font-family: 'Jost', sans-serif; font-size: 16px; padding: 12px; border: 1px solid #E6DCD4; background: #FFFFFF; color: #2E2429;"
def form(t,lang):
    f=t['f']
    sel=lambda lab,opts: f'<label style="{L}">{lab}<select style="{I}" required><option value="">{f["pick"]}</option>'+''.join(f'<option>{o}</option>' for o in opts)+'</select></label>'
    return (f'<form class="iq-form" enctype="multipart/form-data" style="display: flex; flex-direction: column; gap: 18px;">'
      f'<input type="hidden" name="type_demande" value="estimation">'
      f'<div class="iq-f2">{sel(f["zone"],f["zones"])}{sel(f["etat"],f["etats"])}</div>'
      f'<div class="iq-f2"><label style="{L}">{f["ch"]}<input type="number" min="1" max="20" style="{I}" required></label>{sel(f["pool"],f["pools"])}</div>'
      f'<label style="{L}">{f["photos"]}<input type="file" accept="image/*" multiple data-max="5" style="{I}"></label>'
      f'<div class="iq-f2"><label style="{L}">{f["email"]}<input type="email" style="{I}"></label><label style="{L}">{f["nom"]}<input type="text" style="{I}"></label></div>'
      f'<label style="{L}">{f["msg"]}<textarea rows="4" style="{I}"></textarea></label>'
      f'<label style="display: flex; gap: 10px; align-items: flex-start; font-size: 14px;"><input type="checkbox" style="margin-top: 4px;"><span>{f["consent"]}</span></label>'
      f'<button type="button" class="inv-btn inv-btn--rose" style="align-self:flex-start;border:none;cursor:pointer;font-family:Jost,sans-serif;">{f["send"]}</button></form>')

for lang,t in T.items():
    s=f'<!-- title: {t["title"]} -->\n'+STYLE+'\n<div class="inv">\n'
    chips=''.join(f'<a href="#{k}">{h}</a>' for k,_,h,_,_ in t['themes'])+f'<a href="#estimation">{t["form_h"]}</a>'
    s+=(f'<section class="inv-hero"><img src="{HERO_IMG}" alt="" fetchpriority="high"><div class="inv-hero__in"><p style="font-size:13px;letter-spacing:.2em;text-transform:uppercase;color:#E2C3B2;margin:0 0 14px">Unaya Build</p><h1 style="max-width:16ch">{t["h1"]}</h1><p>{t["sub"]}</p>'
        f'<div style="display:flex;flex-wrap:wrap;gap:14px"><a class="inv-btn inv-btn--rose" href="#estimation">{t["b1"]}</a><a class="inv-btn inv-btn--line" href="{t["contact"]}">{t["b2"]}</a></div><div class="inv-steps">{chips}</div></div></section>\n')
    s+=f'<p class="iq-verified">{ic("shield",22)}<span>{t["verified"]}</span></p>\n<div class="inv-journey">\n'
    for n,(key,icon,h,_,qa) in enumerate(t['themes'],1):
        extra=''
        if key=='detenir':
            rows=''.join('<tr>'+''.join((f'<th>{c}</th>' if i==0 else f'<td>{c}</td>') for i,c in enumerate(r))+'</tr>' for r in t['cmp'][1:])
            extra=f'<h3 class="iq-sub">{t["cmp_h"]}</h3><div style="overflow-x:auto"><table class="inv-cmp iq-cmp"><thead><tr>'+''.join(f'<th>{c}</th>' for c in t['cmp'][0])+f'</tr></thead><tbody>{rows}</tbody></table></div>'
        if key=='zonage':
            extra='<div class="iq-zones">'+''.join(f'<div><span style="background:{c}"></span><strong>{a}</strong><small>{b}</small></div>' for c,a,b in t['zones'])+f'</div><p class="inv-note">{t["zones_note"]}</p>'
        if key=='couts':
            extra=('<div class="inv-duo" style="margin-bottom:28px">'+f'<div class="inv-col"><div class="inv-arch"><img src="{BUY}" alt="" loading="lazy"></div><h3>{t["buy"][0]}</h3><p style="margin:0">{t["buy"][1]}</p></div>'
                   f'<div class="inv-col"><div class="inv-arch"><img src="{BUILD}" alt="" loading="lazy"></div><h3>{t["build"][0]}</h3><p style="margin:0">{t["build"][1]}</p></div></div>'
                   '<div class="inv-tiles">'+''.join(f'<div class="inv-tile">{ic(k,30)}<span class="inv-big" style="font-size:38px">{v}</span><p>{l}</p></div>' for k,v,l in t['costs'])+f'</div><p class="inv-note">{t["costs_note"]}</p>')
        if key=='rendement':
            extra=(f'<div class="iq-ex"><h3>{t["ex_h"]}</h3><p>{t["ex_p"]}</p><table>'+''.join(f'<tr{" class=iq-tot" if i==len(t["ex"])-1 else ""}><td>{a}</td><td>{b}</td></tr>' for i,(a,b) in enumerate(t['ex']))+f'</table><p class="inv-note">{t["ex_note"]}</p><a class="inv-btn inv-btn--rose" href="#estimation">{t["b1"]}</a></div>')
        if key=='etapes':
            extra='<ol class="iq-steps">'+''.join(f'<li><b>{i}</b><strong>{a}</strong><span>{b}</span></li>' for i,(a,b) in enumerate(t['steps'],1))+'</ol>'
        faq=''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in qa)
        first = extra if key in ('etapes',) else ''
        after = '' if key in ('etapes',) else extra
        s+=(f'<section class="inv-step" id="{key}"><div class="inv-num" aria-hidden="true">{n}</div><div><h2>{ic(icon,34)} {h}</h2>{first}<div class="u-faq iq-faq">{faq}</div>{after}</div></section>\n')
    # accompagnement
    s+=(f'<section class="inv-step" id="accompagnement"><div class="inv-num" aria-hidden="true">{len(t["themes"])+1}</div><div><h2>{t["acc_h"]}</h2><div class="iq-acc">'+''.join(f'<div>{ic(k,36)}<h3>{h}</h3><p>{p}</p></div>' for k,h,p in t['acc'])+'</div></div></section>\n</div>\n')
    # form
    s+=(f'<section class="iq-formsec" id="estimation"><div class="iq-formsec__in"><div>{ic("report",48)}<h2>{t["form_h"]}</h2><p>{t["form_p"]}</p></div><div class="iq-formbox">{form(t,lang)}</div></div></section>\n')
    # sources
    src=''.join(f'<li><a href="{u}" target="_blank" rel="noopener">{(n if lang=="fr" else SEN[k])}</a></li>' for k,(n,u) in S.items())
    s+=f'<section class="iq-sources" id="sources"><h2>{t["src_h"]}</h2><ol>{src}</ol><p class="inv-disc" style="margin:24px 0 0">{t["disc"]}</p></section>\n</div>\n'
    open(R+f'{lang}/Investir.html','w').write(s)
print('ok')
