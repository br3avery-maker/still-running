# Temporal continuity skill

Use this repository skill whenever a chapter, rewrite, audit, or continuity update touches age, elapsed time, historical placement, clocks, seasons, births, deaths, growth, training, or words such as *before*, *after*, *ago*, *later*, and *since*.

Its job is not to invent an exact calendar. Its job is to keep every possible calendar inside the facts the story has earned.

## Authority order

When temporal claims disagree, preserve the highest-authority evidence and repair the lowest-authority claim:

1. a current explicit author lock;
2. direct events and memories in accepted prose;
3. measurements explicitly related to those events in accepted prose;
4. derived range intersections;
5. isolated machine clocks and archive histories whose relationship to the fixed points is unknown;
6. conditional arithmetic, summaries, plans, prompts, and frontier guesses.

Never demote a higher-authority fixed point merely because a lower-authority clock produces a more dramatic date.

## Fixed points

These anchors are canon until the author explicitly changes them.

- `T0_BLACKOUT`: Nix's remembered power loss while Lena was still at the workshop desk. This is the blackout Nix remembers.
- `T1_NIX_WAKE`: grid power returns and Nix restores herself after being offline for **three years, eight months, eleven days, and between four and nineteen hours**.
- Therefore: `T1_NIX_WAKE = T0_BLACKOUT + [3y 8m 11d 4h, 3y 8m 11d 19h]`.
- `NOW`: the latest accepted chapter. `NOW = T1_NIX_WAKE + PRESENT_RUN`, where the duration of `PRESENT_RUN` must be earned from prose rather than guessed.
- July 31, 2026 is the last shared boundary of reliable human record. It is not automatically `T0_BLACKOUT`, `T1_NIX_WAKE`, an evacuation date, or `NOW`.

The blackout was uneven at world scale. Nix's loss of power is the fixed personal anchor; systems elsewhere may have failed before or after it. Older archives may include years before `T0_BLACKOUT`.

## The required temporal test

Before accepting a temporal claim:

1. Extract every fact the claim depends on.
2. Express each fact as an interval or inequality relative to `T0_BLACKOUT`, `T1_NIX_WAKE`, or another explicitly linked event.
3. Keep unrelated local clocks separate. Do not attach one to a fixed point without prose establishing the link.
4. Intersect the applicable ranges.
5. Classify the result:
   - **ESTABLISHED:** the intersection is non-empty and the prose fixes the relationship.
   - **POSSIBLE — EXPLANATION OWED:** the intersection is non-empty, but one or more causal or calendar links remain unstated.
   - **SPACETIME BREAK:** the intersection is empty; the claims cannot all be true.

Examples:

- AUX-017's 1,406 unattended Tuesdays do not date `T0_BLACKOUT`. The warehouse interval has no established start and may include decades before Nix's blackout. Treating that count as a post-human duration would be an unsupported attachment, not arithmetic truth.
- Rin was born during Lower Three's inhabited years and now independently works Air Shift. If the Station Fourteen evacuation were assumed to follow `T0_BLACKOUT`, the available interval would be less than four years and would conflict with Rin's demonstrated development. No prose currently makes that placement. The ranges can coexist if the evacuation and some Lower Three years precede `T0_BLACKOUT`, so this is a future explanation owed rather than a spacetime break.

## When logic can resolve the contradiction

If at least one interpretation preserves every established fact, do not silently choose it and do not rewrite prose merely to make the ledger look clean.

Add or update an entry in `continuity/temporal-debts.md` containing:

- the facts that appear to pull apart;
- the intervals or ordering constraints involved;
- every currently viable resolution that does not invent new canon;
- assumptions future prose must not make;
- the evidence or scene that could resolve the debt.

Mark the result **POSSIBLE — EXPLANATION OWED**. A debt is a promise to make the relationship legible later, not permission to keep repeating the ambiguity indefinitely.

## When the story breaks spacetime

An empty range intersection is a blocking continuity defect.

1. Record the conflict as **SPACETIME BREAK** in `continuity/temporal-debts.md`.
2. Do not write farther from the broken state.
3. Identify the lowest-authority claim causing the empty intersection.
4. Repair the smallest affected surface:
   - repair a summary, map, prompt, or character sheet when prose remains consistent;
   - revise the minimum accepted prose necessary when prose itself conflicts and the author has authorized temporal repair;
   - never move or widen `T0_BLACKOUT` or the outage-to-wake interval to accommodate a weaker inference.
5. Re-run the interval test and `scripts/story-check.sh`.
6. Close the debt only after the intersection is non-empty and all state files agree.

## Chapter preflight

For every production chapter:

- Read `continuity/time-map.md` and all open entries in `continuity/temporal-debts.md` that touch the scene.
- Test every new age, duration, generation, seasonal reference, historical callback, and capability that implies development time.
- Do not turn “years of records” into “years since the blackout” unless prose explicitly connects them.
- Do not use an absolute current year derived from AUX-017's Tuesday count.
- Update the time map only for relationships the finished prose establishes, narrows, widens, or contradicts.
- Add a temporal debt when logic preserves the story but the explanation remains absent.
- Stop and fix an empty intersection before committing.

`scripts/story-check.sh` invokes `scripts/temporal-check.sh`. The automated check protects the fixed anchors and blocks any debt still labeled **SPACETIME BREAK**. It does not replace the interval test; temporal meaning still requires reading the prose.
