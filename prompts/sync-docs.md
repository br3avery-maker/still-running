# Documentation sync prompt

Use the GitHub repository `br3avery-maker/still-running` as the source of truth. Read and follow `AGENTS.md`, `skills/temporal-continuity.md` when synchronizing temporal claims, and `skills/capability-continuity.md` when synchronizing bodies, tools, senses, access, and physical reach.

Synchronize repository documentation with accepted prose. Do not change story prose.

Reconcile:

- `README.md` with the actual premise, ensemble, and current direction;
- `CANON.md` with facts established in prose;
- `characters/` with current capabilities, relationships, costs, and pressures;
- `continuity/time-map.md` with every consequential timestamp, age constraint, sequence, and uncertainty range actually supported by prose;
- `continuity/story-map.md` with the real completed sequence and immediate next movement;
- `continuity/frontier.md` with genuinely unresolved questions;
- planning files with the current story rather than abandoned directions.

Remove stale claims and duplicated details. Do not invent lore, promote plans into canon, or preserve an obsolete direction merely because it already has a file. Preserve unresolved chronology as `|#####|` ranges; do not convert overlapping local clocks into a single catastrophe date.

Run `scripts/story-check.sh`, commit the documentation changes, verify the GitHub paths, and return only a compact summary with the commit or PR link and files changed.
