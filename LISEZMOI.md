# Site Unaya Management — code source

Site statique (HTML + CSS + un peu de JavaScript), sans dépendance à installer.
Langues : anglais à la racine (`/`), français sous `/fr/`.

## Structure
| Dossier / fichier | Rôle |
|---|---|
| `src/pages/fr/` et `src/pages/en/` | Le contenu de chaque page (un fichier par page). La 1re ligne donne le titre de la page. |
| `src/routes.json` | L'adresse (URL) de chaque page, en FR et en EN |
| `build.py` | Génère le site : en-tête, menu, pied de page, formulaires, réservation, SEO (titres, descriptions, sitemap) |
| `assets/` | Styles (`css/site.css`), script (`js/site.js`), photos (`images/`), logos (`logos/`) |
| `dist/` | **Le site prêt à mettre en ligne** (généré par `build.py`, ne pas modifier à la main) |
| `functions/` | Petites fonctions Cloudflare : envoi des formulaires par e-mail (Resend) et redirection des visiteurs francophones vers /fr/ |
| `tools/convert_mockups.py` | Script utilisé une seule fois pour transformer les maquettes en pages |

## Modifier le site
1. Modifier le texte dans `src/pages/fr/…` et/ou `src/pages/en/…` (ou demander à Claude).
2. Lancer `python3 build.py` → le dossier `dist/` est régénéré.
3. Remettre en ligne (voir ci-dessous).

## Fonctionnement
- **Réservation** : sur chaque page villa, le bloc « Vérifier les disponibilités » ouvre le moteur de réservation Beds24 de la propriété **Unaya** (Suma 359817, Yuga 359816, Rumah Jambu 359818) avec les dates et le nombre de voyageurs.
- **Formulaires** (Contact, Confier ma villa, Services voyageurs) : envoyés à la fonction Cloudflare `functions/api/form.js`, qui transmet la demande par e-mail via **Resend** à info@unayabali.com (anti-spam intégré, réponse directe possible à l'expéditeur), puis affiche la page « Merci ».
- **Menu mobile**, **visionneuse photos** des villas, **FAQ** dépliable.

## Mise en ligne (Cloudflare Pages + GitHub)
1. Mettre ce dossier dans un dépôt GitHub (ex. `unaya-site`).
2. Cloudflare → Workers & Pages → Create → Pages → « Connect to Git » → choisir le dépôt.
3. Réglages de build : **Build command** `python3 build.py` · **Build output directory** `dist`.
4. Settings → Environment variables : `RESEND_API_KEY` (clé Resend, à saisir vous-même), `FORM_TO` = `info@unayabali.com`, `FORM_FROM` = `Site Unaya <site@unayabali.com>` (domaine vérifié dans Resend).
5. Custom domains → ajouter `unayabali.com` et `www.unayabali.com`.
6. Ensuite, chaque modification envoyée sur GitHub met le site à jour automatiquement.
