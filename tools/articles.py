# Articles « Guides » (FR/EN) + page d'index. Génère src/pages/{fr,en}/Guide*.html et Guides.html.
# Les chiffres reprennent ceux du site (guide Investir, simulateur, tarifs) ; sources citées en bas d'article.
import os, json
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.abspath(os.path.join(HERE, '..', 'src', 'pages'))
ROUTES = json.load(open(os.path.join(SRC, '..', 'routes.json')))
def R(p, l): return ROUTES[p][l]
DATE = {'fr': '16 novembre 2026', 'en': '16 November 2026'}
ISO = '2026-11-16'

A = {}
# ---------------------------------------------------------------- 1. Leasehold
A['GuideLeasehold'] = dict(img='arawa-allee.jpg', min=7, fr=dict(
 title='Leasehold à Bali : comment ça marche et que vérifier avant de signer | Unaya',
 desc="Le leasehold à Bali expliqué simplement : durée, prolongation, taxes, rôle du notaire, ce qu’il faut faire écrire dans le bail et les pièges à éviter en 2026.",
 kick='Acheter à Bali', h1='Leasehold à Bali : comment ça marche, et que vérifier avant de signer',
 lead="La plupart des étrangers qui « achètent » une villa à Bali signent en réalité un leasehold : un bail de longue durée sur le terrain. C’est légal, courant et solide, à condition de savoir ce qu’on signe. Voici l’essentiel, sans jargon.",
 body=[
  ('Le leasehold, c’est quoi exactement ?', [
   "Un étranger ne peut pas être pleinement propriétaire d’un terrain en Indonésie. Le leasehold (<em>hak sewa</em>) contourne la question de façon légale : vous louez le terrain au propriétaire indonésien pour une longue durée, par un bail signé chez le notaire, et vous êtes propriétaire de ce que vous construisez dessus pendant toute cette durée.",
   "Le loyer du bail est payé en une fois, au début. C’est pour ça qu’on parle « d’acheter » un leasehold : en pratique, on achète le droit d’occuper, de louer et de revendre le terrain jusqu’à la fin du bail."]),
  ('Combien de temps dure un leasehold ?', [
   "Le plus souvent entre 20 et 30 ans, parfois plus. Ce qui compte n’est pas seulement la durée, mais ce qui se passe à la fin : une bonne option de prolongation vaut parfois plus que cinq années de plus.",
   "Exemple concret : le bail du terrain d’Arawa Villas, à Balangan, court jusqu’au 21 mars 2055, avec une option de 30 ans supplémentaires au prix du marché du moment. Quand on achète une villa existante, on achète les années qui restent : une villa avec 28 ans de bail ne vaut pas une villa avec 12 ans."]),
  ('Ce qu’il faut faire écrire dans le bail', [
   "<strong>La durée et la date de fin</strong>, noir sur blanc.",
   "<strong>La prolongation</strong> : est-elle prévue ? À quel prix (fixé à l’avance, indexé, ou « au prix du marché ») ? Avec quel préavis ?",
   "<strong>Le droit de sous-louer</strong> aux voyageurs et <strong>le droit de céder</strong> le bail : sans eux, vous ne pouvez ni louer ni revendre facilement.",
   "<strong>Le sort de la construction</strong> en fin de bail : en général elle revient au propriétaire du terrain, sauf accord contraire.",
   "<strong>Qui signe</strong> : le titulaire du certificat de propriété, et souvent sa famille. Un bail signé par une seule personne alors que le terrain appartient à plusieurs héritiers est une source classique de litiges."]),
  ('Les vérifications avant de signer', [
   "Le notaire vérifie le certificat au cadastre (BPN), rédige et enregistre l’acte. Mais il ne remplace pas une vérification complète. Avant de signer, il faut contrôler :",
   "<strong>Le zonage</strong> : le terrain doit être dans une zone qui autorise ce que vous voulez faire. Pour louer aux voyageurs, on cherche en général la zone rose (tourisme) sur le plan officiel (RDTR).",
   "<strong>L’accès</strong> : une vraie route d’accès, pas un passage toléré par le voisin.",
   "<strong>Les permis</strong> (PBG, SLF) si la villa est déjà construite, et le respect des règles de construction.",
   "<strong>Les litiges</strong> en cours sur le terrain ou dans la famille du propriétaire. Un avocat indépendant est utile pour ça."]),
  ('Les taxes', [
   "Le loyer d’un bail est soumis à un impôt final de 10 % côté propriétaire du terrain (PPh 4(2)), souvent retenu au moment du paiement : vérifiez dans le contrat qui le paie. Les droits de mutation (BPHTB, jusqu’à 5 %) et l’impôt de 2,5 % du vendeur concernent les transferts de propriété (pleine propriété, HGB), pas un simple bail.",
   "Ensuite, si la villa est louée aux voyageurs, la taxe sur les nuitées (PBJT) est de 10 % dans la régence de Badung."]),
  ('Et pour louer la villa aux voyageurs ?', [
   "C’est le point qui a changé en 2026. Depuis mai, Bali n’accepte plus dans le système OSS les nouvelles demandes de PT PMA (sociétés à capitaux étrangers) pour l’hébergement touristique. Une PT PMA créée aujourd’hui ne peut donc plus obtenir de licence pour louer une villa à la nuit.",
   "La solution la plus simple : confier la villa à une société de gestion déjà en règle, comme Unaya Villa Management, qui la loue pour vous et vous reverse les revenus chaque mois. Et à éviter absolument : acheter au nom d’un ami indonésien (prête-nom). Le bien lui appartient légalement, et ces montages sont interdits."]),
 ],
 key=('À retenir', ['Un leasehold, c’est un bail long (souvent 20-30 ans) signé chez le notaire.', 'La prolongation, le droit de sous-louer et le droit de céder doivent être écrits.', 'Vérifiez zonage, accès, permis et litiges : le notaire ne fait pas tout.', 'Pour louer à la nuit en 2026, passez par une société de gestion licenciée.']),
 links=['Investir', 'VillasAVendre', 'GuideRendement'],
 src=[('Guide Unaya : investir à Bali (sources officielles citées)', '/fr/investir-a-bali/#sources'), ('NusaBali — 18 codes d’activité fermés aux nouvelles PT PMA (22/07/2026)', 'https://www.nusabali.com/berita/226314/gubernur-koster-batasi-akses-oss-bagi-pma-lindungi-ruang-usaha-umkm-bali')]),
 en=dict(
 title='Leasehold in Bali: How It Works and What to Check Before Signing | Unaya',
 desc="Leasehold in Bali explained simply: length, extension, taxes, the notary’s role, what to put in the lease and the pitfalls to avoid in 2026.",
 kick='Buying in Bali', h1='Leasehold in Bali: how it works, and what to check before signing',
 lead="Most foreigners who “buy” a villa in Bali actually sign a leasehold: a long lease on the land. It is legal, common and solid, as long as you know what you are signing. Here are the essentials, without jargon.",
 body=[
  ('What exactly is a leasehold?', [
   "A foreigner cannot fully own land in Indonesia. A leasehold (<em>hak sewa</em>) solves this legally: you lease the land from the Indonesian owner for a long period, through a lease signed before a notary, and you own what you build on it for that whole period.",
   "The lease is paid upfront, in one go. That is why people talk about “buying” a leasehold: in practice, you buy the right to occupy, rent out and resell the land until the lease ends."]),
  ('How long does a leasehold last?', [
   "Usually 20 to 30 years, sometimes more. What matters is not only the length but what happens at the end: a good extension option can be worth more than five extra years.",
   "A real example: the land lease of Arawa Villas, in Balangan, runs until 21 March 2055, with an option for 30 more years at the market price at that time. When you buy an existing villa you buy the remaining years: a villa with 28 years left is not worth the same as one with 12."]),
  ('What to put in the lease', [
   "<strong>The length and the end date</strong>, in black and white.",
   "<strong>The extension</strong>: is there one? At what price (fixed in advance, indexed, or “market price”)? With how much notice?",
   "<strong>The right to sublet</strong> to guests and <strong>the right to transfer</strong> the lease: without them you can neither rent out nor resell easily.",
   "<strong>What happens to the building</strong> at the end: it usually goes to the landowner, unless agreed otherwise.",
   "<strong>Who signs</strong>: the holder of the land certificate, and often their family. A lease signed by one person when the land belongs to several heirs is a classic source of disputes."]),
  ('Checks before signing', [
   "The notary checks the land certificate at the land office (BPN), drafts and registers the deed. But that is not a full due diligence. Before signing, check:",
   "<strong>Zoning</strong>: the plot must be in a zone that allows what you plan. To rent to guests, you usually look for the pink (tourism) zone on the official plan (RDTR).",
   "<strong>Access</strong>: a real access road, not a path the neighbour tolerates.",
   "<strong>Permits</strong> (PBG, SLF) if the villa is already built, and compliance with building rules.",
   "<strong>Disputes</strong> over the land or within the owner’s family. An independent lawyer is useful here."]),
  ('Taxes', [
   "Lease payments carry a 10% final tax on the landowner’s side (PPh 4(2)), often withheld at payment: check in the contract who pays it. Transfer duty (BPHTB, up to 5%) and the seller’s 2.5% tax apply to ownership transfers (freehold, HGB), not to a simple lease.",
   "Then, if the villa is rented to guests, the tax on nightly stays (PBJT) is 10% in Badung regency."]),
  ('And renting the villa to guests?', [
   "This is what changed in 2026. Since May, Bali no longer accepts new PT PMA (foreign-owned company) applications for tourist accommodation in the OSS system. A PT PMA set up today can no longer get a licence to rent out a villa by the night.",
   "The simplest solution: hand the villa to a management company that is already licensed, such as Unaya Villa Management, which rents it out for you and pays you the income every month. And avoid at all costs buying in an Indonesian friend’s name (nominee): the property legally belongs to them, and these arrangements are banned."]),
 ],
 key=('Key points', ['A leasehold is a long lease (often 20–30 years) signed before a notary.', 'Extension, the right to sublet and the right to transfer must be in writing.', 'Check zoning, access, permits and disputes: the notary does not do it all.', 'To rent by the night in 2026, go through a licensed management company.']),
 links=['Investir', 'VillasAVendre', 'GuideRendement'],
 src=[('Unaya guide: investing in Bali (official sources listed)', '/invest-in-bali/#sources'), ('NusaBali — 18 business codes closed to new PT PMA (22/07/2026)', 'https://www.nusabali.com/berita/226314/gubernur-koster-batasi-akses-oss-bagi-pma-lindungi-ruang-usaha-umkm-bali')]))

# ---------------------------------------------------------------- 2. Rendement
A['GuideRendement'] = dict(img='suma-piscine.jpg', min=6, fr=dict(
 title='Combien rapporte une villa à Bali ? Le calcul honnête, chiffre par chiffre | Unaya',
 desc="Combien rapporte vraiment une villa à Bali : revenu brut, commissions, taxe de 10 %, gestion, charges, rendement net. Un exemple chiffré et les pièges à éviter.",
 kick='Investir à Bali', h1='Combien rapporte une villa à Bali ? Le calcul honnête',
 lead="On lit souvent « 15 à 20 % de rendement par an ». La réalité est plus modeste, mais reste intéressante quand la villa est bien placée et bien gérée. Voici le calcul complet, avec un exemple réel de prix, sans rien oublier.",
 body=[
  ('Le revenu brut : nuits louées × prix moyen', [
   "Tout part de deux chiffres : le prix moyen par nuit et le nombre de nuits louées dans l’année. Prenons une villa de 2 ou 3 chambres bien située dans le sud de Bali, louée en moyenne IDR 3 000 000 la nuit, occupée 65 % de l’année : 237 nuits.",
   "Revenu brut : 237 × 3 000 000 = <strong>IDR 711 millions</strong> par an."]),
  ('Ce qui part avant d’arriver chez vous', [
   "<strong>Les plateformes</strong> (Airbnb, Booking…) prennent en moyenne autour de 15 % : environ IDR 107 millions. Moins si une partie des réservations se fait en direct sur votre site.",
   "<strong>La taxe sur les nuitées (PBJT)</strong> : 10 % dans la régence de Badung, comprise dans le prix affiché. Environ IDR 65 millions.",
   "<strong>La gestion</strong> : chez Unaya, 18 % calculés sur ce qui reste après plateformes et taxe, soit environ IDR 97 millions. Attention : certaines sociétés calculent leur commission sur le brut, ce qui change beaucoup le résultat.",
   "<strong>Les charges</strong> : personnel, électricité, eau, internet, entretien de la piscine et du jardin, linge, petites réparations, et une réserve pour remplacer le mobilier. Comptez environ 20 % du brut : IDR 142 millions."]),
  ('Le résultat : le revenu net', [
   "711 − 107 − 65 − 97 − 142 = <strong>environ IDR 300 millions</strong> par an, soit IDR 25 millions par mois, ou à peu près 16 500 USD par an.",
   "Si la villa a coûté 250 000 USD, le rendement net est d’environ <strong>6,6 % par an</strong>, avant impôt sur le revenu. C’est dans la fourchette que donnent les études de marché pour une villa bien gérée une fois lancée : 6 à 10 %."]),
  ('Les pièges à éviter', [
   "<strong>Les promesses de 15-20 %</strong> : elles oublient souvent les commissions, la taxe et les mois creux.",
   "<strong>La première année</strong> : il faut le temps d’avoir des avis et de bien se placer. Le rendement est en général plus bas au début.",
   "<strong>La durée du bail</strong> : en leasehold, la villa perd de la valeur au fil des années qui restent. Un bon rendement sur un bail court peut être un mauvais investissement.",
   "<strong>La licence</strong> : depuis 2026, les annonces sans licence peuvent être retirées des plateformes. Une villa non louable ne rapporte rien."]),
  ('Ce qui fait vraiment monter les revenus', [
   "L’emplacement (près d’une plage, d’un spot de surf, d’une zone animée), les photos, des prix ajustés chaque jour selon la demande, la vitesse de réponse aux voyageurs et les avis. Une villa notée 9,8/10 se loue plus cher et plus souvent qu’une villa à 8,5.",
   "Pour faire le calcul avec vos propres chiffres, utilisez <a href='/fr/investir-a-bali/#simulateur'>notre simulateur</a>, ou demandez-nous une estimation gratuite pour votre villa."]),
 ],
 key=('À retenir', ['Revenu net ≈ 40 à 50 % du brut, avant impôts.', 'Rendement réaliste d’une villa bien gérée : 6 à 10 % par an.', 'Regardez sur quelle base est calculée la commission de gestion.', 'Le bail restant et la licence comptent autant que le prix par nuit.']),
 links=['ProprietairesTarifs', 'Investir', 'GuideGestion'],
 src=[('Guide Unaya : investir à Bali, rendement et revenu net', '/fr/investir-a-bali/#sources'), ('Simulateur de rendement Unaya', '/fr/investir-a-bali/#simulateur')]),
 en=dict(
 title='How Much Does a Villa in Bali Earn? An Honest Calculation | Unaya Bali',
 desc="What a villa in Bali really earns: gross income, commissions, 10% tax, management, running costs, net yield. A worked example and the pitfalls to avoid.",
 kick='Investing in Bali', h1='How much does a villa in Bali earn? An honest calculation',
 lead="You often read “15 to 20% yield a year”. The reality is more modest, but still attractive when the villa is well located and well run. Here is the full calculation, with a real price example, leaving nothing out.",
 body=[
  ('Gross income: nights booked × average rate', [
   "Everything starts with two numbers: the average nightly rate and the number of nights booked in the year. Take a well-located 2- or 3-bedroom villa in south Bali, rented at IDR 3,000,000 a night on average, booked 65% of the year: 237 nights.",
   "Gross income: 237 × 3,000,000 = <strong>IDR 711 million</strong> a year."]),
  ('What goes out before it reaches you', [
   "<strong>Platforms</strong> (Airbnb, Booking…) take around 15% on average: about IDR 107 million. Less if some bookings come direct through your website.",
   "<strong>Tax on nightly stays (PBJT)</strong>: 10% in Badung regency, included in the displayed rate. About IDR 65 million.",
   "<strong>Management</strong>: at Unaya, 18% calculated on what remains after platforms and tax, about IDR 97 million. Careful: some companies calculate their commission on gross, which changes the result a lot.",
   "<strong>Running costs</strong>: staff, electricity, water, internet, pool and garden upkeep, linen, small repairs, and a reserve to replace furniture. Allow about 20% of gross: IDR 142 million."]),
  ('The result: net income', [
   "711 − 107 − 65 − 97 − 142 = <strong>about IDR 300 million</strong> a year, i.e. IDR 25 million a month, or roughly USD 16,500 a year.",
   "If the villa cost USD 250,000, the net yield is about <strong>6.6% a year</strong>, before income tax. That is within the range market studies give for a well-run villa once established: 6 to 10%."]),
  ('Pitfalls to avoid', [
   "<strong>Promises of 15–20%</strong>: they often forget commissions, tax and the low months.",
   "<strong>The first year</strong>: it takes time to build reviews and find your place. Yield is usually lower at the start.",
   "<strong>Lease length</strong>: on a leasehold, the villa loses value as the remaining years shrink. A good yield on a short lease can be a poor investment.",
   "<strong>The licence</strong>: since 2026, listings without a licence can be removed from platforms. A villa you cannot rent earns nothing."]),
  ('What really lifts income', [
   "Location (near a beach, a surf spot, a lively area), photos, prices adjusted every day to demand, how fast you reply to guests, and reviews. A villa rated 9.8/10 rents for more, and more often, than one at 8.5.",
   "To run the numbers with your own figures, use <a href='/invest-in-bali/#simulateur'>our simulator</a>, or ask us for a free estimate for your villa."]),
 ],
 key=('Key points', ['Net income ≈ 40–50% of gross, before taxes.', 'Realistic yield for a well-run villa: 6–10% a year.', 'Check what base the management commission is calculated on.', 'Remaining lease and licence matter as much as the nightly rate.']),
 links=['ProprietairesTarifs', 'Investir', 'GuideGestion'],
 src=[('Unaya guide: investing in Bali, yield and net income', '/invest-in-bali/#sources'), ('Unaya yield simulator', '/invest-in-bali/#simulateur')]))

# ---------------------------------------------------------------- 3. Gestion
A['GuideGestion'] = dict(img='suma-chambre-1.jpg', min=6, fr=dict(
 title='Gestion de villa à Bali : ce que fait une société de gestion, et combien ça coûte',
 desc="Gestion de villa à Bali : ce que fait une société de gestion, les commissions du marché (souvent 15 à 20 %), la base de calcul et les points à vérifier dans le contrat.",
 kick='Propriétaires', h1='Gestion de villa à Bali : ce que fait une société de gestion, et combien ça coûte',
 lead="Louer une villa à Bali depuis l’étranger, c’est un vrai métier : voyageurs à toute heure, équipe à encadrer, taxes, pannes. Une société de gestion s’en occupe à votre place. Voici ce qu’elle fait, ce que ça coûte vraiment et comment comparer les offres.",
 body=[
  ('Ce que fait une société de gestion', [
   "<strong>Le marketing</strong> : les annonces sur Airbnb, Booking, Expedia et le site de la villa, les photos, les textes, et surtout les prix, ajustés chaque jour selon la saison et la demande.",
   "<strong>Les voyageurs</strong> : les réponses avant le séjour, l’arrivée, l’assistance 24h/24, le départ, et les avis.",
   "<strong>La villa</strong> : le personnel (ménage, jardin, piscine), le linge, les courses de base, l’entretien et les réparations.",
   "<strong>Les chiffres</strong> : l’encaissement, le paiement de la taxe sur les nuitées (PBJT), les dépenses avec justificatifs et un rapport chaque mois."]),
  ('Combien ça coûte ?', [
   "La plupart des sociétés se paient par une commission sur les revenus locatifs. Pour une gestion complète à Bali, on voit souvent autour de 20 % ; certaines offres en ligne plus légères sont autour de 15 %.",
   "Chez Unaya : <strong>gestion complète à partir de 18 %</strong>, ou <strong>marketing seul à 11 %</strong> si vous gérez la villa sur place. Aucun frais fixe, aucun frais d’entrée."]),
  ('Le piège : la base de calcul', [
   "Deux sociétés à 18 % ne coûtent pas la même chose. Sur IDR 10 000 000 de réservations, une commission calculée sur le brut fait IDR 1 800 000. Calculée après les plateformes (≈ 15 %) et la taxe de 10 %, comme chez Unaya, elle fait environ IDR 1 366 000.",
   "Demandez toujours : la commission est-elle calculée sur le brut, ou après plateformes et taxe ? Et qu’est-ce qui est facturé en plus (linge, photos, petits travaux) ?"]),
  ('Les points à vérifier dans le contrat', [
   "<strong>La durée et le préavis</strong> : pouvez-vous arrêter facilement si ça ne vous convient pas ?",
   "<strong>Le rapport mensuel</strong> : réservations, revenus, dépenses avec justificatifs, et l’accès à un espace en ligne.",
   "<strong>Qui fixe les prix</strong>, et votre droit d’utiliser la villa vous-même.",
   "<strong>Les dépenses</strong> : à partir de quel montant la société doit vous demander votre accord.",
   "<strong>La licence</strong> : qui loue la villa officiellement ? Depuis mai 2026, une nouvelle PT PMA ne peut plus obtenir de licence d’hébergement touristique à Bali, et passer par une société de gestion déjà en règle devient souvent la solution."]),
  ('Gérer seul, ou avec une société ?', [
   "Gérer seul, c’est garder la commission, mais aussi répondre aux voyageurs la nuit, en plusieurs langues, fixer les prix au jugé, recruter et encadrer l’équipe, payer les taxes et gérer la pompe de piscine en panne un samedi soir. Depuis l’étranger, c’est rarement tenable.",
   "Une bonne société de gestion se paie en général par de meilleurs revenus : plus de nuits louées, de meilleurs prix et de meilleurs avis."]),
 ],
 key=('À retenir', ['Gestion complète : souvent 15 à 20 % du marché ; Unaya dès 18 %.', 'Vérifiez la base de calcul de la commission.', 'Exigez un rapport mensuel avec justificatifs.', 'En 2026, la licence pour louer est un point essentiel.']),
 links=['ProprietairesServices', 'ProprietairesTarifs', 'GuideRendement'],
 src=[('Own Property Abroad — Property management costs in Indonesia', 'https://ownpropertyabroad.com/indonesia/property-management-cost-and-pricing'), ('Tarifs Unaya', '/fr/proprietaires/tarifs/')]),
 en=dict(
 title='Villa Management in Bali: What a Manager Does and What It Costs | Unaya',
 desc="Villa management in Bali: what a management company does, market commissions (often 15–20%), the calculation base and what to check in the contract.",
 kick='Owners', h1='Villa management in Bali: what a manager does, and what it costs',
 lead="Renting out a villa in Bali from abroad is a real job: guests at any hour, staff to supervise, taxes, breakdowns. A management company does it for you. Here is what it does, what it really costs and how to compare offers.",
 body=[
  ('What a management company does', [
   "<strong>Marketing</strong>: listings on Airbnb, Booking, Expedia and the villa’s website, photos, copy, and above all pricing, adjusted every day to season and demand.",
   "<strong>Guests</strong>: replies before the stay, check-in, 24/7 support, check-out, and reviews.",
   "<strong>The villa</strong>: staff (cleaning, garden, pool), linen, basic supplies, maintenance and repairs.",
   "<strong>The numbers</strong>: collecting payments, paying the tax on nightly stays (PBJT), expenses with receipts and a report every month."]),
  ('How much does it cost?', [
   "Most companies charge a commission on rental income. For full management in Bali you often see around 20%; some lighter online offers are around 15%.",
   "At Unaya: <strong>full management from 18%</strong>, or <strong>marketing only at 11%</strong> if you run the villa on site. No fixed fees, no set-up fee."]),
  ('The trap: the calculation base', [
   "Two companies at 18% do not cost the same. On IDR 10,000,000 of bookings, a commission on gross is IDR 1,800,000. Calculated after platforms (≈ 15%) and the 10% tax, as at Unaya, it is about IDR 1,366,000.",
   "Always ask: is the commission on gross, or after platforms and tax? And what is billed on top (linen, photos, small works)?"]),
  ('What to check in the contract', [
   "<strong>Length and notice</strong>: can you stop easily if you are not happy?",
   "<strong>The monthly report</strong>: bookings, income, expenses with receipts, and access to an online portal.",
   "<strong>Who sets prices</strong>, and your right to use the villa yourself.",
   "<strong>Expenses</strong>: above what amount the company must ask for your approval.",
   "<strong>The licence</strong>: who officially rents out the villa? Since May 2026 a new PT PMA can no longer get a tourist-accommodation licence in Bali, so going through an already licensed management company often becomes the solution."]),
  ('Manage it yourself, or with a company?', [
   "Doing it yourself saves the commission, but means answering guests at night in several languages, guessing prices, hiring and supervising staff, paying taxes and dealing with a broken pool pump on a Saturday night. From abroad, it rarely works.",
   "A good management company usually pays for itself through better income: more nights booked, better rates and better reviews."]),
 ],
 key=('Key points', ['Full management: often 15–20% in the market; Unaya from 18%.', 'Check the commission’s calculation base.', 'Insist on a monthly report with receipts.', 'In 2026, the licence to rent out is a key point.']),
 links=['ProprietairesServices', 'ProprietairesTarifs', 'GuideRendement'],
 src=[('Own Property Abroad — Property management costs in Indonesia', 'https://ownpropertyabroad.com/indonesia/property-management-cost-and-pricing'), ('Unaya pricing', '/owners/pricing/')]))

# ---------------------------------------------------------------- 4. Où louer
A['GuideOuLoger'] = dict(img='suma-g1.jpg', min=5, fr=dict(
 title='Où louer une villa à Bali : Uluwatu, Canggu, Seminyak ou Tanah Lot ? | Unaya',
 desc="Où louer une villa à Bali ? Uluwatu, Jimbaran, Canggu, Seminyak, Tanah Lot : le style de chaque quartier, pour qui, et nos conseils pour bien choisir sa villa.",
 kick='Voyageurs', h1='Où louer une villa à Bali : Uluwatu, Canggu, Seminyak ou Tanah Lot ?',
 lead="Bali est plus grande qu’on ne le pense, et la circulation peut transformer 20 km en une heure de route. Choisir le bon quartier compte autant que choisir la bonne villa. Voici les principaux secteurs pour louer une villa, et pour qui ils sont faits.",
 body=[
  ('Uluwatu et Jimbaran : falaises, surf et plages', [
   "Tout au sud, sur la péninsule de Bukit. Des plages de sable blanc entre les falaises (Balangan, Bingin, Padang Padang, Melasti), le temple d’Uluwatu au coucher du soleil, et Jimbaran avec sa baie et ses restaurants de poisson sur le sable.",
   "Pour qui : couples, familles, surfeurs, et tous ceux qui veulent du calme près de l’aéroport (30 à 50 minutes). Nos villas ici : SUMA Bali et Rumah Jambu, à Balangan."]),
  ('Canggu : cafés, surf et vie de quartier', [
   "Le secteur le plus animé de la côte ouest : cafés, coworkings, restaurants, beach clubs et plages de surf. Idéal si vous voulez tout faire à pied ou en scooter, moins si vous cherchez le silence.",
   "Pour qui : jeunes voyageurs, nomades digitaux, groupes d’amis."]),
  ('Tanah Lot et Nyanyi : rizières et sable noir', [
   "Juste à l’ouest de Canggu, la côte devient campagne : rizières, plages de sable noir, et le temple de Tanah Lot sur son rocher. Les restaurants de Canggu et de Pererenan restent à 15-25 minutes.",
   "Pour qui : familles, longs séjours, ceux qui veulent le Bali des rizières. Notre villa ici : YUGA Bali, à Nyanyi, qui se loue à la chambre ou en entier."]),
  ('Seminyak et Kerobokan : restaurants et beach clubs', [
   "Seminyak et Petitenget, ce sont les restaurants, les boutiques et les beach clubs au bord de la plage. Kerobokan et Umalas, juste derrière, sont plus calmes, avec de grandes villas familiales.",
   "Pour qui : ceux qui veulent sortir le soir, faire du shopping, et rester à 30-45 minutes de l’aéroport."]),
  ('Nos conseils pour bien choisir sa villa', [
   "<strong>Regardez le trajet</strong> entre la villa et ce que vous voulez faire, pas seulement la distance.",
   "<strong>Vérifiez que la villa est en règle</strong> : depuis 2026, les annonces sans licence peuvent être retirées des plateformes, parfois après la réservation.",
   "<strong>Réservez en direct</strong> quand c’est possible : vous parlez à l’équipe qui vous accueille, et c’est souvent moins cher (chez Unaya, −15 % dès 7 nuits).",
   "<strong>Pensez au transfert</strong> depuis l’aéroport et à un scooter ou un chauffeur sur place : à Bali, on ne se déplace pas à pied."]),
 ],
 key=('En bref', ['Calme, plages et surf près de l’aéroport : Uluwatu et Jimbaran.', 'Animation et cafés : Canggu.', 'Rizières et grands espaces : Tanah Lot et Nyanyi.', 'Restaurants et beach clubs : Seminyak.']),
 links=['Villas', 'ZoneUluwatu', 'ZoneTanahLot'],
 src=[('Nos villas à Bali', '/fr/villas/'), ('Services voyageurs : transfert, chauffeur, scooter', '/fr/services-voyageurs/')]),
 en=dict(
 title='Where to Rent a Villa in Bali: Uluwatu, Canggu, Seminyak or Tanah Lot?',
 desc="Where to rent a villa in Bali? Uluwatu, Jimbaran, Canggu, Seminyak, Tanah Lot: the feel of each area, who it suits, and our tips for choosing your villa.",
 kick='Guests', h1='Where to rent a villa in Bali: Uluwatu, Canggu, Seminyak or Tanah Lot?',
 lead="Bali is bigger than you think, and traffic can turn 20 km into an hour’s drive. Choosing the right area matters as much as choosing the right villa. Here are the main areas to rent a villa, and who they suit.",
 body=[
  ('Uluwatu & Jimbaran: cliffs, surf and beaches', [
   "At the very south, on the Bukit peninsula. White-sand beaches between the cliffs (Balangan, Bingin, Padang Padang, Melasti), Uluwatu temple at sunset, and Jimbaran with its bay and seafood restaurants on the sand.",
   "Who it suits: couples, families, surfers, and anyone wanting calm close to the airport (30–50 minutes). Our villas here: SUMA Bali and Rumah Jambu, in Balangan."]),
  ('Canggu: cafés, surf and neighbourhood life', [
   "The liveliest area on the west coast: cafés, coworking, restaurants, beach clubs and surf beaches. Great if you want to do everything on foot or by scooter, less so if you want silence.",
   "Who it suits: young travellers, digital nomads, groups of friends."]),
  ('Tanah Lot & Nyanyi: rice fields and black sand', [
   "Just west of Canggu, the coast turns to countryside: rice fields, black-sand beaches, and Tanah Lot temple on its rock. Canggu and Pererenan restaurants are 15–25 minutes away.",
   "Who it suits: families, long stays, anyone after rice-field Bali. Our villa here: YUGA Bali, in Nyanyi, rented by the room or as a whole."]),
  ('Seminyak & Kerobokan: restaurants and beach clubs', [
   "Seminyak and Petitenget are restaurants, boutiques and beach clubs by the sea. Kerobokan and Umalas, just behind, are quieter, with big family villas.",
   "Who it suits: those who want nights out, shopping, and to stay 30–45 minutes from the airport."]),
  ('Our tips for choosing your villa', [
   "<strong>Look at travel time</strong> between the villa and what you want to do, not just distance.",
   "<strong>Check the villa is licensed</strong>: since 2026, unlicensed listings can be removed from platforms, sometimes after you have booked.",
   "<strong>Book direct</strong> when you can: you talk to the team that welcomes you, and it is often cheaper (at Unaya, −15% from 7 nights).",
   "<strong>Plan the airport transfer</strong> and a scooter or driver on site: in Bali you don’t get around on foot."]),
 ],
 key=('In short', ['Calm, beaches and surf near the airport: Uluwatu & Jimbaran.', 'Buzz and cafés: Canggu.', 'Rice fields and space: Tanah Lot & Nyanyi.', 'Restaurants and beach clubs: Seminyak.']),
 links=['Villas', 'ZoneUluwatu', 'ZoneTanahLot'],
 src=[('Our villas in Bali', '/villas/'), ('Guest services: transfer, driver, scooter', '/guest-services/')]))

ORDER = ['GuideLeasehold', 'GuideRendement', 'GuideGestion', 'GuideOuLoger']
LBL = {'fr': dict(min='min de lecture', toc='Dans cet article', rel='À lire aussi', src='Sources', upd='Mis à jour le', by='Par l’équipe Unaya',
                  cta=('Une question sur votre projet ?', 'Écrivez-nous : on vous répond sous 24 h, en français.', 'Nous contacter'), more='Lire l’article',
                  idx_t='Guides : gestion de villa, location et achat à Bali | Unaya', idx_d="Nos guides pratiques sur Bali : leasehold, rendement d’une villa, gestion de villa et où louer une villa. Écrits par l’équipe Unaya, sur place à Jimbaran.",
                  idx_k='Le journal Unaya', idx_h='Guides pratiques sur Bali', idx_p='Acheter, louer, faire gérer : ce qu’on explique tous les jours à nos clients, écrit noir sur blanc.'),
       'en': dict(min='min read', toc='In this article', rel='Read next', src='Sources', upd='Updated', by='By the Unaya team',
                  cta=('A question about your project?', 'Write to us: we reply within 24 hours.', 'Contact us'), more='Read the article',
                  idx_t='Guides: Villa Management, Rentals & Buying in Bali | Unaya', idx_d="Our practical guides to Bali: leasehold, villa rental income, villa management and where to rent a villa. Written by the Unaya team, on the ground in Jimbaran.",
                  idx_k='The Unaya journal', idx_h='Practical guides to Bali', idx_p='Buying, renting, getting a villa managed: what we explain to clients every day, written down.')}
TITLE_OF = {}

def rel_card(p, lang):
    if p in A:
        a = A[p]; t = a[lang]
        return f'<a class="gd-rel" href="{R(p, lang)}"><img src="/assets/images/{a["img"]}" alt="" loading="lazy"><span><small>{t["kick"]}</small><strong>{t["h1"]}</strong></span></a>'
    names = {'Investir': ('arawa-facade.jpg', {'fr': 'Le guide pour investir à Bali', 'en': 'The guide to investing in Bali'}),
             'VillasAVendre': ('arawa-piscine.jpg', {'fr': 'Nos villas à vendre', 'en': 'Our villas for sale'}),
             'ProprietairesTarifs': ('suma-terrasse.jpg', {'fr': 'Nos tarifs de gestion', 'en': 'Our management fees'}),
             'ProprietairesServices': ('yuga-terrasse.jpg', {'fr': 'Nos services de gestion', 'en': 'Our management services'}),
             'Villas': ('suma-piscine-2.jpg', {'fr': 'Nos villas à louer', 'en': 'Our villas for rent'}),
             'ZoneUluwatu': ('zone-uluwatu-jimbaran.jpg', {'fr': 'Uluwatu et Jimbaran', 'en': 'Uluwatu & Jimbaran'}),
             'ZoneTanahLot': ('zone-tanah-lot-canggu.jpg', {'fr': 'Tanah Lot et Canggu', 'en': 'Tanah Lot & Canggu'})}
    img, n = names[p]
    return f'<a class="gd-rel" href="{R(p, lang)}"><img src="/assets/images/{img}" alt="" loading="lazy"><span><small>Unaya</small><strong>{n[lang]}</strong></span></a>'

def page(key, lang):
    a = A[key]; t = a[lang]; l = LBL[lang]
    toc = ''.join(f'<li><a href="#s{i}">{h}</a></li>' for i, (h, _) in enumerate(t['body'], 1))
    secs = ''
    for i, (h, ps) in enumerate(t['body'], 1):
        lst = [p for p in ps if p.startswith('<strong>')]
        txt = [p for p in ps if not p.startswith('<strong>')]
        secs += f'<h2 id="s{i}">{h}</h2>' + ''.join(f'<p>{p}</p>' for p in txt) + (('<ul class="gd-list">' + ''.join(f'<li>{p}</li>' for p in lst) + '</ul>') if lst else '')
    kh, kl = t['key']
    s = f'<!-- title: {t["title"]} -->\n<div class="hm">\n'
    s += (f'<section class="hm-hero hm-hero--sm gd-hero"><img src="/assets/images/{a["img"]}" alt="" fetchpriority="high"><div class="hm-hero__in"><p class="hm-hero__k"><a href="{R("Guides", lang)}">{l["idx_k"]}</a> · {t["kick"]}</p>'
          f'<h1 class="gd-h1">{t["h1"]}</h1><p class="gd-meta">{l["by"]} · {l["upd"]} <time datetime="{ISO}">{DATE[lang]}</time> · {a["min"]} {l["min"]}</p></div></section>\n')
    s += (f'<section class="u-sec hm-sec gd-sec"><div class="gd-wrap"><article class="gd-art"><p class="gd-lead">{t["lead"]}</p>'
          f'<nav class="gd-toc" aria-label="{l["toc"]}"><strong>{l["toc"]}</strong><ol>{toc}</ol></nav>{secs}'
          f'<aside class="gd-key"><strong>{kh}</strong><ul>' + ''.join(f'<li>{x}</li>' for x in kl) + '</ul></aside>'
          f'<div class="gd-src"><strong>{l["src"]}</strong><ul>' + ''.join(f'<li><a href="{u}"{" target=_blank rel=noopener" if u.startswith("http") else ""}>{n}</a></li>' for n, u in t['src']) + '</ul></div></article></div></section>\n')
    s += (f'<section class="u-sec u-sec--white hm-sec"><div class="u-wrap"><div class="u-head u-head--c"><h2>{l["rel"]}</h2></div><div class="gd-rels">' + ''.join(rel_card(p, lang) for p in t['links']) + '</div></div></section>\n')
    s += (f'<section class="u-cta"><img src="/assets/images/{a["img"]}" alt="" loading="lazy"><div class="u-cta__in"><h2>{l["cta"][0]}</h2><p>{l["cta"][1]}</p>'
          f'<div class="u-btns"><a class="u-btn u-btn--rose" href="{R("Contact", lang)}">{l["cta"][2]}</a></div></div></section>\n</div>\n')
    return s

def index(lang):
    l = LBL[lang]
    s = f'<!-- title: {l["idx_t"]} -->\n<div class="hm">\n'
    s += (f'<section class="hm-hero hm-hero--sm"><img src="/assets/images/yuga-terrasse.jpg" alt="" fetchpriority="high"><div class="hm-hero__in"><p class="hm-hero__k">{l["idx_k"]}</p>'
          f'<h1 class="gd-h1">{l["idx_h"]}</h1><p class="hm-hero__sub">{l["idx_p"]}</p></div></section>\n')
    s += '<section class="u-sec hm-sec"><div class="u-wrap"><div class="gd-grid">'
    for k in ORDER:
        a = A[k]; t = a[lang]
        s += (f'<a class="gd-card" href="{R(k, lang)}"><div class="gd-card__img"><img src="/assets/images/{a["img"]}" alt="" loading="lazy"><span>{t["kick"]}</span></div>'
              f'<div class="gd-card__b"><h2>{t["h1"]}</h2><p>{t["desc"]}</p><em>{a["min"]} {l["min"]} · {l["more"]} →</em></div></a>')
    s += '</div></div></section>\n</div>\n'
    return s

META = {}
for k in ORDER:
    for lang in ('fr', 'en'):
        META[(lang, k)] = (A[k][lang]['title'], A[k][lang]['desc'])
for lang in ('fr', 'en'):
    META[(lang, 'Guides')] = (LBL[lang]['idx_t'], LBL[lang]['idx_d'])

if __name__ == '__main__':
    for lang in ('fr', 'en'):
        for k in ORDER:
            open(os.path.join(SRC, lang, f'{k}.html'), 'w').write(page(k, lang))
        open(os.path.join(SRC, lang, 'Guides.html'), 'w').write(index(lang))
    print('ok')
