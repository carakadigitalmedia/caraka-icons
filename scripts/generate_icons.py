#!/usr/bin/env python3
"""Build Caraka Icons CSS and JSON manifest from WebP files."""
from __future__ import annotations
import json, re, sys, unicodedata
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
ICONS = ROOT / "icons"
CSS = ROOT / "caraka-icons.css"
MANIFEST = ROOT / "icons.json"
EXTS = {".webp"}

def slugify(value: str) -> str:
    value = unicodedata.normalize("NFKD", value)
    value = "".join(c for c in value if not unicodedata.combining(c))
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    if not value:
        raise ValueError("Nama file tidak dapat dijadikan class CSS.")
    return value

def humanize(value: str) -> str:
    return re.sub(r"[-_]+", " ", value).strip().title()

def main() -> int:
    if not ICONS.is_dir():
        raise SystemExit("ERROR: folder icons/ tidak ditemukan.")
    paths = sorted((p for p in ICONS.rglob("*") if p.is_file() and p.suffix.lower() in EXTS),
                   key=lambda p: p.as_posix().casefold())
    if not paths:
        raise SystemExit("ERROR: tidak ada file WebP di folder icons/.")
    records, seen, rules = [], {}, []
    rules.extend([
        "/*! Caraka Icons — generated file; do not edit manually. */",
        ":root{--ci-icon-size:1em}",
        ".ci{display:inline-block;width:var(--ci-icon-size);height:var(--ci-icon-size);flex:0 0 auto;vertical-align:-.125em;background-repeat:no-repeat;background-position:center;background-size:contain;line-height:1}",
        ".ci-xs{--ci-icon-size:.75em}.ci-sm{--ci-icon-size:.875em}.ci-lg{--ci-icon-size:1.333em}.ci-xl{--ci-icon-size:1.75em}.ci-2x{--ci-icon-size:2em}.ci-3x{--ci-icon-size:3em}",
        ".ci-middle{vertical-align:middle}.ci-top{vertical-align:top}",
        ""
    ])
    for p in paths:
        rel = p.relative_to(ICONS).as_posix()
        slug = slugify(p.stem)
        if slug in seen:
            raise SystemExit(f"ERROR: class duplikat ci-{slug}: {seen[slug]} dan {rel}. Ubah nama salah satu file.")
        seen[slug] = rel
        category = p.parent.relative_to(ICONS).as_posix()
        if category == ".":
            category = "Umum"
        else:
            category = humanize(category.split("/")[-1])
        name = humanize(p.stem)
        encoded = "/".join(quote(part, safe="-._~") for part in rel.split("/"))
        keywords = sorted(set((name + " " + slug.replace("-", " ") + " pramuka tkk " + category).lower().split()))
        records.append({
            "name": name, "slug": slug, "className": f"ci ci-{slug}",
            "file": f"icons/{rel}", "category": category,
            "keywords": keywords
        })
        rules.append(f'.ci-{slug}{{background-image:url("./icons/{encoded}")}}')
    CSS.write_text("\n".join(rules) + "\n", encoding="utf-8")
    MANIFEST.write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"OK: {len(records)} ikon dibuat ke caraka-icons.css dan icons.json.")
    return 0

if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
