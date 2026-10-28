import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PACKS = ROOT / "packs"
MAX_FILE = 95 * 1024 * 1024
ALLOWED = {".md", ".png", ".jpg", ".jpeg", ".webp", ".gif", ".mp4", ".webm", ".mp3", ".ogg", ".wav", ".json", ".ttf", ".otf"}
ID_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
HEX_RE = re.compile(r"^#[0-9A-Fa-f]{6}$")

def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

def check_pack(d: Path) -> tuple[dict, list[str]]:
    errors = []
    meta_path = d / "pack.json"
    if not meta_path.exists():
        return {}, [f"{d.name}: pack.json manquant"]
    try:
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return {}, [f"{d.name}: pack.json invalide ({e})"]

    if meta.get("id") != d.name:
        errors.append(f"{d.name}: l'id doit être égal au nom du dossier")
    if not ID_RE.match(d.name):
        errors.append(f"{d.name}: nom de dossier en minuscules-avec-tirets uniquement")
    for key in ("name", "version", "logo", "colors"):
        if key not in meta:
            errors.append(f"{d.name}: champ obligatoire manquant : {key}")
    for k, v in meta.get("colors", {}).items():
        if not HEX_RE.match(str(v)):
            errors.append(f"{d.name}: couleur {k} invalide ({v}), format #RRGGBB")
    if meta.get("logo") and not (d / meta["logo"]).exists():
        errors.append(f"{d.name}: logo introuvable ({meta['logo']})")

    files = []
    for f in sorted(d.rglob("*")):
        if not f.is_file() or f.name == "pack.json":
            continue
        rel = f.relative_to(d).as_posix()
        if f.suffix.lower() not in ALLOWED:
            errors.append(f"{d.name}: type de fichier refusé : {rel}")
            continue
        if f.stat().st_size > MAX_FILE:
            errors.append(f"{d.name}: fichier trop lourd (>95 Mo) : {rel}")
            continue
        files.append({"path": rel, "sha256": sha256(f), "size": f.stat().st_size})

    entry = {
        "id": meta.get("id"),
        "name": meta.get("name"),
        "version": meta.get("version"),
        "description": meta.get("description", ""),
        "discord": meta.get("discord", ""),
        "author": meta.get("author", ""),
        "colors": meta.get("colors", {}),
        "fivem": meta.get("fivem", {}),
        "logo": meta.get("logo"),
        "files": files,
    }
    return entry, errors

def build_common(errors: list[str]) -> dict:
    d = ROOT / "communs"
    meta_path = d / "communs.json"
    if not meta_path.exists():
        return {}
    try:
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        errors.append(f"communs.json invalide ({e})")
        return {}
    files = []
    for f in sorted(d.rglob("*")):
        if not f.is_file() or f.name == "communs.json":
            continue
        rel = f.relative_to(d).as_posix()
        if f.suffix.lower() not in ALLOWED:
            errors.append(f"communs: type de fichier refusé : {rel}")
            continue
        files.append({"path": rel, "sha256": sha256(f), "size": f.stat().st_size})
    for key, m in meta.get("music", {}).items():
        if not (d / m.get("file", "")).exists():
            errors.append(f"communs: musique {key} introuvable ({m.get('file')})")
    return {"version": meta.get("version", "1.0.0"), "music": meta.get("music", {}), "files": files}

def main() -> int:
    check_only = "--check" in sys.argv
    entries, errors = [], []
    for d in sorted(p for p in PACKS.iterdir() if p.is_dir()):
        entry, errs = check_pack(d)
        errors += errs
        if entry:
            entries.append(entry)
    if errors:
        print("Erreurs :\n  " + "\n  ".join(errors))
        return 1
    common = build_common(errors)
    if errors:
        print("Erreurs :\n  " + "\n  ".join(errors))
        return 1
    print(f"{len(entries)} pack(s) valides.")
    if not check_only:
        index = {"schema": 1, "common": common, "packs": entries}
        (ROOT / "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print("index.json généré.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
