# Proposer un pack serveur

Tu ne connais pas Git ? Utilise le formulaire [« Proposer un serveur »](https://github.com/ybyns2/slayer-kit-packs/issues/new?template=serveur.yml) : le pack sera créé pour toi. Sinon, ouvre une pull request en suivant ce guide.

## Structure

```
packs/
  mon-serveur/            ← minuscules et tirets uniquement
    pack.json
    logo.png              ← carré, 512×512 conseillé
    banniere-discord.gif  ← bandeau affiché en live
    fond-anime.mp4        ← ou .gif / .webm : fond des écrans d'attente
    fond-fixe.png         ← 1920×1080
```

## pack.json

```json
{
  "id": "mon-serveur",
  "name": "Mon Serveur",
  "version": "1.0.0",
  "description": "Serveur RP …",
  "discord": "discord.gg/xxxxx",
  "author": "ton pseudo",
  "colors": { "accent": "#9B5CFF", "accent2": "#D46BFF", "background": "#0D0916" },
  "fivem": { "windowTitleContains": ["Mon Serveur"] },
  "logo": "logo.png",
  "assets": {
    "logo": "logo.png",
    "bannerDiscord": "banniere-discord.gif",
    "background": "fond-anime.mp4",
    "backgroundStill": "fond-fixe.png"
  }
}
```

- `fivem.windowTitleContains` contient un morceau du titre de la fenêtre FiveM quand on est connecté au serveur. Il permet la détection automatique.
- Les couleurs doivent être au format `#RRGGBB`.
- Quand tu modifies un pack existant, augmente `version` : tout le monde reçoit la mise à jour.

## Règles

- Formats acceptés : png, jpg, webp, gif, mp4, webm, mp3, ogg, wav, json, ttf, otf.
- 95 Mo maximum par fichier.
- Visuels **avec l'accord du staff du serveur** uniquement.
- Musiques : libres de droits uniquement, avec la licence indiquée dans la PR.

## Vérifier en local

```
python tools/build_index.py --check
```

## Validation

Chaque pull request est vérifiée automatiquement (`build_index.py --check`), puis relue par le mainteneur. Une fois fusionnée, `index.json` est régénéré et le pack est disponible dans l'application.
