import json
import shutil
from pathlib import Path

from PIL import Image, ImageSequence

PICS = Path(r"C:\Users\AAA\Pictures")
OUT = Path(__file__).resolve().parent.parent / "packs"

def square_logo(src: Path, dest: Path, size: int = 512, frame: str = "first"):
    im = Image.open(src)
    if getattr(im, "is_animated", False):
        frames = [f.convert("RGBA") for f in ImageSequence.Iterator(im)]
        im = frames[0] if frame == "first" else frames[-1]
    im = im.convert("RGBA")
    w, h = im.size
    s = min(w, h)
    im = im.crop(((w - s) // 2, (h - s) // 2, (w + s) // 2, (h + s) // 2)).resize((size, size), Image.LANCZOS)
    im.save(dest, optimize=True)

PACKS = {
    "unity-legacy": {
        "name": "Unity Legacy",
        "description": "Serveur RP Unity Legacy",
        "discord": "discord.gg/unitylegacy",
        "colors": {"accent": "#9B5CFF", "accent2": "#D46BFF", "background": "#0D0916"},
        "fivem": {"windowTitleContains": ["UNITY Legacy", "Unity Legacy"]},
        "logo_src": ("unitylegacytwitch/a_41eb3b56247125427186b5a047f09301.gif", "first"),
        "assets": {
            "banniere-discord.gif": "unitylegacytwitch/legacy.gif",
            "fond-anime.gif": "unitylegacytwitch/a_87716714f863db921a93e1b869d8e407.gif",
            "blason-anime.gif": "unitylegacytwitch/a_41eb3b56247125427186b5a047f09301.gif",
            "fond-fixe.png": "unitylegacytwitch/Header-discord.png",
            "banniere-twitch.png": "unitylegacytwitch/Header-Twitch.png",
        },
    },
    "fratworld": {
        "name": "FratWorld",
        "description": "Serveur RP FratWorld",
        "discord": "",
        "colors": {"accent": "#FF7A1A", "accent2": "#FFB347", "background": "#100B07"},
        "fivem": {"windowTitleContains": ["FratWorld", "Frat World"]},
        "logo_src": ("fratworldtwitch/logo.png", "first"),
        "assets": {
            "banniere-discord.gif": "fratworldtwitch/banniere-discord.gif",
            "banniere-animee.gif": "fratworldtwitch/banniere-animee.gif",
            "fond-anime.mp4": "fratworldtwitch/fond-anime.mp4",
            "fond-fixe.png": "fratworldtwitch/fond-splash.png",
            "logo-halo.png": "fratworldtwitch/logo-halo.png",
        },
    },
    "night-fa": {
        "name": "Night FA",
        "description": "Serveur RP Night FA",
        "discord": "discord.gg/vzaD3s6PBS",
        "colors": {"accent": "#D63AF9", "accent2": "#FFAA50", "background": "#0C0712"},
        "fivem": {"windowTitleContains": ["NightFA", "Night FA"]},
        "logo_src": ("nightfatwitch/icone-animee.gif", "last"),
        "assets": {
            "banniere-discord.gif": "nightfatwitch/banniere-discord.gif",
            "blason-anime.gif": "nightfatwitch/NightFA.gif",
            "fond-anime.mp4": "nightfatwitch/fond-anime.mp4",
            "fond-fixe.png": "nightfatwitch/fond-fixe.png",
            "banniere.png": "nightfatwitch/banniere.png",
        },
    },
}

for pid, p in PACKS.items():
    d = OUT / pid
    d.mkdir(parents=True, exist_ok=True)
    src, frame = p["logo_src"]
    square_logo(PICS / src, d / "logo.png", frame=frame)
    for name, rel in p["assets"].items():
        shutil.copy2(PICS / rel, d / name)
    meta = {
        "id": pid,
        "name": p["name"],
        "version": "1.0.0",
        "description": p["description"],
        "discord": p["discord"],
        "author": "yns_bnl",
        "colors": p["colors"],
        "fivem": p["fivem"],
        "logo": "logo.png",
        "assets": {
            "logo": "logo.png",
            "bannerDiscord": "banniere-discord.gif",
            "background": next((n for n in p["assets"] if n.startswith("fond-anime")), ""),
            "backgroundStill": "fond-fixe.png",
        },
    }
    (d / "pack.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(pid, sorted(x.name for x in d.iterdir()))
