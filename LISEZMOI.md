# Écran d'accueil pour locations haut de gamme

Une seule app pour tous les iPad. Chaque écran est identifié par un **code d'installation**, par exemple `CM-0001`. Tout se règle à distance, depuis ce dépôt.

## Organisation

| Dossier ou fichier | Rôle |
|---|---|
| `index.html` | L'app, identique pour tous les écrans |
| `devices/<CODE>.json` | La **fiche d'un écran** : station, agence, logement, logo, couleur, langue, conciergerie (WhatsApp, services) |
| `resorts/<station>.json` | Le **contenu d'une station** : météo, agenda, remontées, route, restaurants. Mis à jour chaque matin, commun à tous les écrans de la station. |
| `sw.js`, `manifest.webmanifest`, icônes | Mode app plein écran et fonctionnement hors ligne |
| `qrcode.js` | Génération des QR codes, sans dépendre d'Internet |
| `outils/nouvel_ecran.py` | Crée la fiche d'un nouvel écran |

## Installer un iPad (sur place, sans compétence technique)

1. Ouvrir dans **Safari** : `https://misterdbma.github.io/ecran-crans-montana/`
2. Bouton Partager, puis **Sur l'écran d'accueil**.
3. Ouvrir l'app depuis l'icône et **taper le code de l'écran** (ex. `CM-0001`). Le code est mémorisé.
4. Réglages, Luminosité et affichage, Verrouillage auto : **Jamais**.
5. Réglages, Accessibilité, **Accès guidé** : activer. Ouvrir l'app, puis triple-clic sur le bouton latéral.
6. Laisser l'iPad branché.

Pour changer le code d'un écran déjà installé : toucher **5 fois de suite** la ligne sous la date, puis confirmer.

## Piloter à distance

- **Modifier un écran** : éditer `devices/<CODE>.json` sur GitHub. L'iPad prend le changement dans les 30 minutes, tout seul.
- **Ajouter un écran** :
  ```
  python3 outils/nouvel_ecran.py CM-0002 --agency "Nom agence" --place "Chalet X · Crans" --whatsapp "+41 79 123 45 67"
  ```
  Publier le fichier créé, puis taper `CM-0002` sur le nouvel iPad.
- **Ajouter une station** (Verbier, Andermatt…) : ajouter `resorts/verbier.json`, puis mettre `"resort": "verbier"` dans les fiches des écrans concernés.
- **Mettre à jour l'app** : publier un nouvel `index.html`. Tous les iPad le récupèrent tout seuls.

## Références dans les demandes

Chaque message WhatsApp envoyé depuis un écran se termine par sa référence, par exemple :

```
Réf. CM-0001 · TRANSFERT
```

Elle indique de quel écran et de quel service vient la demande. C'est la base du comptage et de la facturation.

## Champs d'une fiche écran

- `resort` : station, par exemple `crans-montana`.
- `agency` : nom affiché en bas de l'écran.
- `place` : ligne sous la date.
- `logo` : chemin d'une image, par exemple `logos/agence.png`.
- `accent` : couleur, par exemple `#c9a96e`.
- `lang` : `fr`, `en` ou `de`.
- `concierge.whatsapp` : numéro WhatsApp. Avec `demo: true`, le numéro n'est pas affiché.
- `concierge.services` : la liste des services. Pour chacun : `id` (utilisé dans la référence), nom, sous-titre et message pré-rédigé, en FR, EN et DE.

Tout ce dépôt est public : n'y mettez que des informations destinées aux clients.

## À venir

- Comptage serveur des demandes, signe de vie des iPad et statistiques. Il faudra un petit serveur, par exemple Supabase.
- Espace agence avec identifiant, et paiement mensuel (Stripe).
