# Repository audit prompt

Use the GitHub repository `br3avery-maker/still-running` as the source of truth. Read and follow `AGENTS.md`.

Perform a read-only audit of the repository. Do not rewrite prose, change files, commit, or open a pull request.

Inspect:

- whether README, canon, character records, story map, frontier, and accepted prose agree;
- established facts accidentally presented as planned, and planned ideas accidentally presented as canon;
- stale links, obsolete planning files, abandoned branches of story logic, duplicated instructions, and redundant context;
- missing character or capability records needed for the next chapter;
- repeated scene engines, pacing stalls, unresolved contradictions, and anything that is part of the thing that killed the plot;
- repository structure or workflow problems that waste agent context or production time.

Return a compact audit with:

1. current story frontier in one paragraph;
2. blocking contradictions or breakage;
3. the five highest-value fixes in priority order;
4. exact files each fix would touch;
5. a recommendation: continue, sync docs, compress canon, clean repository, or rewrite an arc.

Do not paste source files or large excerpts. Cite repository paths precisely.
