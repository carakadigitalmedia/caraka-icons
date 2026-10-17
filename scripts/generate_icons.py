
#!/usr/bin/env python3
"""Generate Caraka Icons CSS and JSON manifest from WebP files."""

from __future__ import annotations

import json
import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
ICONS = ROOT / "icons"
CSS = ROOT / "caraka-icons.css"
MANIFEST = ROOT / "icons.json"

EXTS = {".webp"}

CATEGORIES = {
    "siaga": "Siaga",
    "penggalang": "Penggalang",
    "penegak": "Penegak",
    "umum": "Umum",
    "lainnya": "Lainnya",
}


def slugify(value: str) -> str:
    value = unicodedata.normalize("NFKD", value)
    value = "".join(
        char for char in value
        if not unicodedata.combining(char)
    )
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")

    if not value:
        raise ValueError(
            "Nama file tidak dapat dijadikan class CSS."
        )

    return value


def humanize(value: str) -> str:
    value = re.sub(r"[-_]+", " ", value).strip()
    return value.title()


def get_category(path: Path) -> str:
    relative = path.relative_to(ICONS)
    parts = relative.parts

    if len(parts) == 1:
        return "Umum"

    folder = parts[0].casefold()
    return CATEGORIES.get(folder, "Lainnya")


def get_category_slug(category: str) -> str:
    return slugify(category)


def main() -> int:
    if not ICONS.is_dir():
        raise SystemExit(
            "ERROR: folder icons/ tidak ditemukan."
        )

    paths = sorted(
        (
            path for path in ICONS.rglob("*")
            if path.is_file()
            and path.suffix.lower() in EXTS
        ),
        key=lambda path: path.as_posix().casefold(),
    )

    if not paths:
        raise SystemExit(
            "ERROR: tidak ada file WebP di folder icons/."
        )

    records = []
    seen_classes: dict[str, str] = {}
    rules = [
        "/*! Caraka Icons — generated file; do not edit manually. */",
        ":root{--ci-icon-size:1em}",
        (
            ".ci{display:inline-block;"
            "width:var(--ci-icon-size);"
            "height:var(--ci-icon-size);"
            "flex:0 0 auto;"
            "vertical-align:-.125em;"
            "background-repeat:no-repeat;"
            "background-position:center;"
            "background-size:contain;"
            "line-height:1}"
        ),
        (
            ".ci-xs{--ci-icon-size:.75em}"
            ".ci-sm{--ci-icon-size:.875em}"
            ".ci-lg{--ci-icon-size:1.333em}"
            ".ci-xl{--ci-icon-size:1.75em}"
            ".ci-2x{--ci-icon-size:2em}"
            ".ci-3x{--ci-icon-size:3em}"
        ),
        ".ci-middle{vertical-align:middle}.ci-top{vertical-align:top}",
        "",
    ]

    for path in paths:
        relative = path.relative_to(ICONS).as_posix()
        category = get_category(path)
        category_slug = get_category_slug(category)
        file_slug = slugify(path.stem)

        slug = f"{category_slug}-{file_slug}"
        class_name = f"ci ci-{slug}"

        if slug in seen_classes:
            raise SystemExit(
                f"ERROR: class duplikat ci-{slug}: "
                f"{seen_classes[slug]} dan {relative}. "
                "Ubah nama salah satu file."
            )

        seen_classes[slug] = relative

        name = humanize(path.stem)
        encoded_path = "/".join(
            quote(part, safe="-._~")
            for part in relative.split("/")
        )

        keywords = sorted(
            set(
                (
                    f"{name} {file_slug.replace('-', ' ')} "
                    f"{category} pramuka tkk"
                ).lower().split()
            )
        )

        record = {
            "name": name,
            "slug": slug,
            "className": class_name,
            "file": f"icons/{relative}",
            "category": category,
            "keywords": keywords,
        }

        records.append(record)

        image_rule = (
            f'.ci-{slug}{{'
            f'background-image:url("./icons/{encoded_path}")'
            f'}}'
        )
        rules.append(image_rule)

        # Compatibility alias for icons previously stored
        # directly inside icons/, such as tkk-berkemah.webp.
        if path.parent == ICONS:
            alias_slug = file_slug

            if alias_slug not in seen_classes:
                seen_classes[alias_slug] = relative
                rules.append(
                    f".ci-{alias_slug}{{"
                    f'background-image:url("./icons/{encoded_path}")'
                    f"}}"
                )

    CSS.write_text(
        "\n".join(rules) + "\n",
        encoding="utf-8",
    )

    MANIFEST.write_text(
        json.dumps(records, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    category_counts = {
        category: sum(
            1 for record in records
            if record["category"] == category
        )
        for category in CATEGORIES.values()
    }

    print(
        f"OK: {len(records)} ikon berhasil dibuat."
    )
    print(f"CSS: {CSS.name}")
    print(f"Manifest: {MANIFEST.name}")

    for category, total in category_counts.items():
        print(f"  {category}: {total} ikon")

    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
