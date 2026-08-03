#!/usr/bin/env python3
"""Conservative guard against giving remote-only intelligences physical bodies."""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1]
MAP_PATH = ROOT / "continuity" / "capability-map.json"

STRONG_PHYSICAL = {
    "wrapped", "wraps", "drilled", "drills", "lifted", "lifts",
    "grasped", "grasps", "tightened", "tightens", "reseated", "reseats",
    "lowered", "lowers",
}

CONTEXTUAL_PHYSICAL = {
    "aligned", "aligns", "attached", "attaches", "installed", "installs",
    "braced", "braces", "built", "builds", "carried", "carries", "cut", "cuts",
    "placed", "places", "removed", "removes", "tested", "tests", "used", "uses",
}

PHYSICAL_OBJECTS = {
    "bolt", "bolts", "brace", "cable", "crawler", "edge", "frame", "joint",
    "offcut", "pair", "paper", "plate", "plates", "steel", "washer", "winch",
}

MEDIATION_MARKERS = {
    "at patch's direction", "under patch's direction", "at nix's direction",
    "under nix's direction", "at two's direction", "under two's direction",
    "instructed", "ordered", "directed",
}


def sentences(text: str):
    for line_number, line in enumerate(text.splitlines(), 1):
        stripped = line.strip()
        if not stripped:
            continue
        for sentence in re.split(r"(?<=[.!?])\s+", stripped):
            if sentence:
                yield line_number, sentence


def verb_is_physical(sentence: str):
    words = re.findall(r"[A-Za-z']+", sentence.lower())
    for index, word in enumerate(words):
        previous = words[index - 1] if index else ""
        if previous in {"was", "were", "is", "are", "been", "being"}:
            continue
        if previous in {"a", "an", "the"}:
            continue
        if word in STRONG_PHYSICAL:
            return word
        if word in CONTEXTUAL_PHYSICAL:
            window = set(words[index + 1:index + 8])
            if window & PHYSICAL_OBJECTS:
                return word
    if re.search(r"\bleft\s+(?:it|the\s+\w+)\s+attached\b", sentence, re.I):
        return "left attached"
    return None


def scan_text(text: str, source: str, remote_actors: list[str]):
    findings = []
    last_subject = None

    for line_number, sentence in sentences(text):
        lowered = sentence.lower()
        explicit_subject = None
        for actor in remote_actors:
            if re.match(rf"^[\"'“”‘’>*+\-\s]*{re.escape(actor)}\b", sentence, re.I):
                explicit_subject = actor
                break

        pronoun_subject = None
        if re.match(r"^[\"'“”‘’>*+\-\s]*(?:it|she|he|they)\b", sentence, re.I):
            pronoun_subject = last_subject

        subject = explicit_subject or pronoun_subject
        physical_verb = verb_is_physical(sentence)

        if subject and physical_verb:
            mediated = any(marker in lowered for marker in MEDIATION_MARKERS)
            if not mediated:
                findings.append({
                    "source": source,
                    "line": line_number,
                    "actor": subject,
                    "verb": physical_verb,
                    "sentence": sentence,
                })

        if explicit_subject:
            last_subject = explicit_subject
        elif not re.match(r"^[\"'“”‘’>*+\-\s]*(?:it|she|he|they)\b", sentence, re.I):
            last_subject = None

    return findings


def load_remote_actors():
    data = json.loads(MAP_PATH.read_text(encoding="utf-8"))
    return list(data["remote_only"].keys())


def scan_repository():
    remote_actors = load_remote_actors()
    paths = set((ROOT / "stories").glob("[0-9][0-9]-*.md"))
    paths.update((ROOT / "characters").glob("*.md"))
    paths.update((ROOT / "continuity").glob("*.md"))
    paths.update([
        ROOT / "CANON.md",
        ROOT / "README.md",
    ])

    findings = []
    for path in sorted(paths):
        findings.extend(scan_text(
            path.read_text(encoding="utf-8"),
            str(path.relative_to(ROOT)),
            remote_actors,
        ))
    return findings


def self_test():
    remote = ["Patch", "Nix", "Two"]
    cases = [
        ("Patch evaluated the telemetry.", 0),
        ("Under Patch's direction, the healthy crawler aligned the plate.", 0),
        ("Patch placed WM-4419-RC2 in the update catalogue.", 0),
        ("Patch wrapped the plate in oil paper.", 1),
        ("Patch installed the brace.", 1),
        ("Patch designed the brace and used the bolts to hold it.", 1),
        ("Patch described the strip that was wrapped around a pipe.", 0),
        ("Patch designed a bridge from the braced crawler's sensor.", 0),
        ("Patch rejected the paper pair. It aligned the reference pair.", 1),
        ("Patch stopped the test, reseated the bolt, and added the washer.", 1),
        ("Patch left the safety line attached until the crawler returned.", 1),
        ("The healthy crawler tightened the bolts in increments supplied by Patch.", 0),
        ("Nix lifted the crawler.", 1),
        ("Nix carried it to the guardian.", 0),
        ("Two cut the steel plate.", 1),
    ]
    failures = []
    for text, expected in cases:
        actual = len(scan_text(text, "self-test", remote))
        if actual != expected:
            failures.append((text, expected, actual))
    if failures:
        for text, expected, actual in failures:
            print(f"SELF-TEST FAIL expected {expected}, got {actual}: {text}", file=sys.stderr)
        return 1
    print(f"OK capability checker self-test ({len(cases)} cases)")
    return 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        return self_test()

    findings = scan_repository()
    if findings:
        print("ERROR unmediated physical actions assigned to remote-only actors:", file=sys.stderr)
        for item in findings:
            print(
                f"{item['source']}:{item['line']}: {item['actor']} -> {item['verb']}: "
                f"{item['sentence']}",
                file=sys.stderr,
            )
        return 1

    print("OK capability provenance: 0 unmediated remote physical actions")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
