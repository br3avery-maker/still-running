# Arc rewrite prompt

Use the GitHub repository `br3avery-maker/still-running` as the source of truth. Read and follow `AGENTS.md`.

Audit the authorized chapter range scene by scene using this test: **is this part of the thing that killed the plot?**

Rewrite the range in place. Preserve strong material only when it serves the moving story; do not protect passages merely because individual lines are good.

For every scene require at least one of:

- action or attempted action;
- discovery that changes the model of the world;
- relationship change;
- concrete cost or irreversible consequence;
- new capability, obligation, danger, or mission.

Compress repeated safety analysis, evidence classification, protocol design, permission debate, static banter, and technical explanation that does not change the next choice. Preserve canon unless the request explicitly authorizes a retcon; record any deliberate retcon clearly.

Rebuild canon, character state, story map, frontier, and current-direction documentation from the finished prose. Run `scripts/story-check.sh`, commit the rewrite, verify GitHub, and return compact status and links only. Do not paste the rewritten chapters unless requested.

Authorized chapter range: `[for example: stories/04 through stories/08]`

Required new direction or correction: `[describe it here]`
