#!/usr/bin/env python3

from pathlib import Path

replacements = {
    "jakarta.xml.bind": "javax.xml.bind",
    "jakarta.activation": "javax.activation",
}

root = Path("src")

for path in root.rglob("*.java"):
    text = path.read_text()
    newtext = text

    for old, new in replacements.items():
        newtext = newtext.replace(old, new)

    if newtext != text:
        path.write_text(newtext)
        print("updated:", path)
