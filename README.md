# Slayer Kit — Packs serveur

Les packs de serveurs RP utilisés par **[Slayer Kit by yns_bnl](https://github.com/ybyns2/slayer-kit)**.

L'application lit uniquement `index.json` et ne télécharge que le pack choisi par la personne. Chaque fichier est vérifié par son empreinte SHA-256.

## Packs disponibles

| Pack | Dossier |
|---|---|
| Unity Legacy | `packs/unity-legacy` |
| FratWorld | `packs/fratworld` |
| Night FA | `packs/night-fa` |

## Proposer un serveur

Deux façons de faire, chaque proposition est relue par le mainteneur avant d'apparaître dans l'application.

**Sans Git :** ouvre une issue [« Proposer un serveur »](https://github.com/ybyns2/slayer-kit-packs/issues/new?template=serveur.yml), remplis le formulaire et joins tes visuels. Le bouton « Proposer un serveur » de l'application ouvre directement ce formulaire.

**Avec Git :** lis [CONTRIBUTING.md](CONTRIBUTING.md), puis :

1. Fork ce repo.
2. Crée `packs/ton-serveur/` avec `pack.json`, `logo.png` et tes visuels.
3. Ouvre une pull request.
4. La vérification automatique contrôle ton pack, puis le mainteneur valide.
5. Après la fusion, le catalogue se met à jour tout seul : tout le monde voit ton serveur dans l'appli.

Les visuels d'un serveur ne doivent être proposés **qu'avec l'accord du staff de ce serveur**.

## Licence

Code (dossier `tools/`) : MIT, © yns_bnl. Visuels : propriété de leurs serveurs respectifs, utilisés avec leur accord.
