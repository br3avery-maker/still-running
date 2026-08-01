# Batch chapter prompt

Use the GitHub repository `br3avery-maker/still-running` as the source of truth. Read and follow `AGENTS.md`.

Write the next `[chapter count; default 3]` complete chapters as one continuous production run.

For each chapter:

1. choose the strongest next movement supported by the current state;
2. write the complete chapter under the next numbered path in `stories/`;
3. update canon, character state, story map, and frontier only for what that chapter establishes;
4. run `scripts/story-check.sh`;
5. commit that chapter and its state changes separately;
6. treat the new commit as source of truth before writing the following chapter.

Do not outline in place of prose and do not ask nonblocking questions. Stop early only if a genuine contradiction or missing author decision would force incompatible stories; otherwise choose and continue.

Do not paste chapters into chat. At completion, return a compact table containing chapter number, title, one-sentence state change, commit link, and validation result.

Optional focus or new idea: `[leave blank and follow the strongest frontier pressure]`
