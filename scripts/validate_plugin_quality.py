#!/usr/bin/env python3
"""Repository-local quality checks for the journalism-core-tw plugin."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_VERSION = "1.0.1"
EXPECTED_SKILL_COUNT = 13

PROHIBITED_PHRASES = {
    "4 大 IFCN 認證": "Do not describe all four LINE fact-checking sources as IFCN-certified.",
    "將來會在地化": "The plugin README should not contain a stale future-localization section.",
    "待翻譯/改寫中": "The repo is complete; contribution docs should not point to old TODO status.",
    "journalism-core-tw v0.4.1": "The manual test suite title should track the current release.",
    "永久 5xx 拒絕": "Gmail enforcement wording should not overstate all failures as permanent 5xx.",
    "DMARC `p=quarantine` 或 `p=reject` 成為大量發信實質必要": (
        "Gmail's baseline bulk-sender DMARC requirement is still p=none."
    ),
    "本 plugin 將來在地化": "Cross-skill references should not describe completed skills as future work.",
    "已知尚待後續校對": "Released skills should use boundary guidance instead of stale TODO headings.",
    "Initial Pulitzer": "Story-pitch funding references should not contain this typo.",
}


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # pragma: no cover - diagnostic path
        raise AssertionError(f"{path}: invalid JSON: {exc}") from exc


def parse_frontmatter(path: Path, text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise AssertionError(f"{path}: missing opening frontmatter")
    try:
        end = text.index("\n---\n", 4)
    except ValueError as exc:
        raise AssertionError(f"{path}: missing closing frontmatter") from exc

    data: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            raise AssertionError(f"{path}: malformed frontmatter line: {line}")
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()
    return data


def main() -> int:
    errors: list[str] = []

    marketplace = load_json(ROOT / ".claude-plugin" / "marketplace.json")
    plugin = load_json(ROOT / "journalism-core-tw" / ".claude-plugin" / "plugin.json")

    if marketplace.get("version") != EXPECTED_VERSION:
        errors.append(f"marketplace version is {marketplace.get('version')!r}, expected {EXPECTED_VERSION}")
    if plugin.get("version") != EXPECTED_VERSION:
        errors.append(f"plugin version is {plugin.get('version')!r}, expected {EXPECTED_VERSION}")

    entries = [entry for entry in marketplace.get("plugins", []) if entry.get("name") == plugin.get("name")]
    if len(entries) != 1:
        errors.append(f"expected one marketplace entry for {plugin.get('name')!r}, found {len(entries)}")
    elif entries[0].get("version") != plugin.get("version"):
        errors.append("marketplace plugin entry version does not match plugin.json")

    skill_files = sorted((ROOT / "journalism-core-tw" / "skills").glob("*/SKILL.md"))
    if len(skill_files) != EXPECTED_SKILL_COUNT:
        errors.append(f"expected {EXPECTED_SKILL_COUNT} skills, found {len(skill_files)}")

    for path in skill_files:
        text = path.read_text(encoding="utf-8")
        try:
            frontmatter = parse_frontmatter(path, text)
        except AssertionError as exc:
            errors.append(str(exc))
            continue

        expected_name = path.parent.name
        name = frontmatter.get("name")
        if name != expected_name:
            errors.append(f"{path}: frontmatter name {name!r} does not match directory {expected_name!r}")
        if not name or not name.endswith("-tw"):
            errors.append(f"{path}: skill name must end with -tw")
        if not frontmatter.get("description"):
            errors.append(f"{path}: missing description")

        version = re.search(r"^- 版本:([^\n]+)", text, re.MULTILINE)
        if not version:
            errors.append(f"{path}: missing version line")
        elif EXPECTED_VERSION not in version.group(1):
            errors.append(f"{path}: version line should include {EXPECTED_VERSION}, got {version.group(1).strip()!r}")

    prohibited_paths = [
        ROOT / "README.md",
        ROOT / "journalism-core-tw" / "README.md",
        ROOT / "TEST_SUITE.md",
        *skill_files,
    ]
    for path in prohibited_paths:
        text = path.read_text(encoding="utf-8")
        for phrase, reason in PROHIBITED_PHRASES.items():
            if phrase in text:
                errors.append(f"{path}: prohibited phrase {phrase!r}: {reason}")

    test_suite = (ROOT / "TEST_SUITE.md").read_text(encoding="utf-8")
    if f"journalism-core-tw v{EXPECTED_VERSION}" not in test_suite:
        errors.append("TEST_SUITE.md title must include current plugin version")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print("plugin quality checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
