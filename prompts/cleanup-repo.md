# Repository cleanup prompt

Use the GitHub repository `br3avery-maker/still-running` as the source of truth. Read and follow `AGENTS.md`.

Clean redundant, obsolete, or unnecessary repository material while preserving accepted prose and useful history.

Look for:

- duplicate or superseded planning files;
- instructions repeated across README, AGENTS, canon, prompts, and continuity notes;
- stale references to deleted or renamed chapters;
- empty directories, dead templates, generated clutter, and files no current workflow reads;
- continuity notes that merely restate canon without adding sequence or frontier value;
- character files containing long historical summaries instead of current writing constraints.

Consolidate before deleting when information remains useful. You may delete clearly obsolete non-prose files. Do not delete or substantially rewrite accepted story prose unless I explicitly include a story range in this request.

Run `scripts/story-check.sh`, commit the cleanup, verify the GitHub paths, and return a concise list of what was removed, merged, or retained and why. Do not paste file contents.

Optional story range authorized for cleanup or revision: `[leave blank for no prose changes]`
