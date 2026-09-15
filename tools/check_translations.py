"""Validate translation files against the English source."""
import json
import re
import sys
from pathlib import Path

def placeholders(text):
    found = []
    depth = 0
    current = ""
    for char in text:
        if char == "{":
            if depth == 0:
                current = ""
            else:
                current += char
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                head = re.split(r"[,\s]", current.strip(), maxsplit=1)[0]
                found.append(head)
            else:
                current += char
        elif depth > 0:
            current += char
    return found
def identifiers(text):
    names = set(placeholders(text))
    for match in re.finditer(r"\{([A-Za-z_][A-Za-z0-9_]*)\}", text):
        names.add(match.group(1))
    return sorted(names)
ROOT = Path(__file__).resolve().parent.parent / "flutter"
SOURCE = ROOT / "app_en.arb"


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def main():
    try:
        source = load(SOURCE)
    except Exception as exc:
        print(f"source unreadable: {exc}")
        return 1
    failures = 0
    for path in sorted(ROOT.glob("app_*.arb")):
        if path == SOURCE:
            continue
        try:
            data = load(path)
        except Exception as exc:
            print(f"{path.name}: invalid JSON ({exc})")
            failures += 1
            continue
        for key, value in source.items():
            if key.startswith("@") or not isinstance(value, str):
                continue
            if key not in data:
                print(f"{path.name}: missing key {key}")
                failures += 1
                continue
            if not isinstance(data[key], str):
                print(f"{path.name}: {key} is not a string")
                failures += 1
                continue
            if identifiers(value) != identifiers(data[key]):
                print(f"{path.name}: {key} placeholder mismatch")
                failures += 1
    print("OK" if failures == 0 else f"{failures} problem(s)")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
