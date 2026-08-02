# Chronology audit prompt

Use the GitHub repository `br3avery-maker/still-running` as the source of truth. Read and follow `AGENTS.md`.

Read and follow `skills/temporal-continuity.md`. Scan every accepted chapter for timestamp-shaped evidence: calendar dates, clock readings, ages, births, deaths, seasons, elapsed durations, maintenance histories, repeated schedules, relative words such as *before* and *after*, and role-based constraints that imply growth or training time.

Rebuild `continuity/time-map.md` from the prose and reconcile `continuity/temporal-debts.md`.

For every item:

1. classify it as a hard calendar anchor, local clock, relative duration, sequence constraint, conditional derivation, or unresolved inference;
2. cite the chapter that establishes it;
3. plot uncertainty as `LEFT |#####| RIGHT`, `|#|`, or `|#####→` rather than a point or dot;
4. keep clocks from different systems separate unless prose explicitly joins them;
5. intersect every applicable range against the fixed anchors;
6. log a non-empty but unexplained intersection as **POSSIBLE — EXPLANATION OWED**;
7. mark an empty intersection **SPACETIME BREAK** and repair the lowest-authority conflicting claim before continuing.

Lock `T0_BLACKOUT` to Nix's remembered power loss while Lena is still at the desk. Lock `T1_NIX_WAKE` three years, eight months, eleven days, and four-to-nineteen hours later. Treat July 31, 2026 as the last shared boundary of reliable human record, not an automatic catastrophe, disappearance, birth, or evacuation date. Do not promote AUX-017's 1,406 Tuesdays into a current year or a duration of post-blackout human absence.

Prefer repairing summaries, maps, and prompts when accepted prose remains logically consistent. If accepted prose itself creates an empty interval and temporal repair is authorized, revise the smallest conflicting passage without moving the fixed anchor.

Run `scripts/story-check.sh`, commit the chronology changes, verify the GitHub paths, and return a compact summary of the fixed anchors, explanation debts, spacetime breaks repaired, and commit link. Do not paste the complete time map into chat.
