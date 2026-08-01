# Chronology audit prompt

Use the GitHub repository `br3avery-maker/still-running` as the source of truth. Read and follow `AGENTS.md`.

Scan every accepted chapter for timestamp-shaped evidence: calendar dates, clock readings, ages, births, deaths, seasons, elapsed durations, maintenance histories, repeated schedules, relative words such as *before* and *after*, and role-based constraints that imply growth or training time.

Rebuild `continuity/time-map.md` from the prose.

For every item:

1. classify it as a hard calendar anchor, local clock, relative duration, sequence constraint, conditional derivation, or unresolved inference;
2. cite the chapter that establishes it;
3. plot uncertainty as `LEFT |#####| RIGHT`, `|#|`, or `|#####→` rather than a point or dot;
4. keep clocks from different systems separate unless prose explicitly joins them;
5. flag contradictions instead of silently stretching a range to absorb them.

Treat July 31, 2026 as the last shared boundary of reliable human record, not an automatic catastrophe, disappearance, birth, or evacuation date. Do not promote the conditional calendar reading derived from AUX-017's 1,406 Tuesdays into a settled current year.

Do not change story prose. Update `CANON.md`, `continuity/now.md`, character guardrails, and production prompts only when a temporal constraint established in prose is missing or dangerously easy to misread.

Run `scripts/story-check.sh`, commit the chronology changes, verify the GitHub paths, and return a compact summary of the strongest anchors, widest unresolved ranges, contradictions found, and commit link. Do not paste the complete time map into chat.
