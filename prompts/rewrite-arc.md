# Arc rewrite prompt

Use the GitHub repository `br3avery-maker/still-running` as the source of truth. Read and follow `AGENTS.md`.

Audit the authorized chapter range in two separate sandboxes.

First, read each chapter as if no canon packet exists and ask: **what is this assuming the reader already knows?** Classify every unexplained name, system, callback, causal jump, timeline jump, and technical consequence as either:

- deliberate literary mystery that creates tension, foreshadowing, or a useful question; or
- missing connective tissue that exists only in authoring notes or the editor's memory.

Preserve the first. Restore, move, or dramatize the second. Do not summarize an important scene before the reader experiences it unless the displacement itself creates a deliberate effect. Compare every age, elapsed duration, historical callback, and sequence claim with `continuity/time-map.md`; preserve uncertainty as `|#####|` ranges rather than silently choosing an exact date.

Second, audit scene by scene using this test: **is this part of the thing that killed the plot?**

Rewrite the range in place. Preserve strong material only when it serves the moving story; do not protect passages merely because individual lines are good.

For every scene require at least one of:

- action or attempted action;
- discovery that changes the model of the world;
- relationship change;
- concrete cost or irreversible consequence;
- new capability, obligation, danger, or mission.

Compress repeated safety analysis, evidence classification, protocol design, permission debate, static banter, and technical explanation that does not change the next choice. Preserve canon unless the request explicitly authorizes a retcon; record any deliberate retcon clearly.

Compression is not automatically improvement. Preserve atmosphere, physical description, character-forming delay, jokes, failed attempts, and operational detail when they let the reader build the world that later investigation depends upon.

Rebuild canon, character state, story map, frontier, time ranges, and current-direction documentation from the finished prose. Run `scripts/story-check.sh`, commit the rewrite, verify GitHub, and return compact status and links only. Do not paste the rewritten chapters unless requested.

Authorized chapter range: `[for example: stories/04 through stories/08]`

Required new direction or correction: `[describe it here]`
