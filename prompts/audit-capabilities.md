# Capability continuity audit prompt

Use the GitHub repository `br3avery-maker/still-running` as the source of truth. Read and follow `AGENTS.md` and `skills/capability-continuity.md`.

Audit every accepted chapter for physical, sensory, access, movement, and tool-use claims. Do not search only for named capability terms. Resolve grammatical subjects, pronouns, shorthand, ownership language, and implied action.

For every consequential verb:

1. identify the intelligence making the decision;
2. identify the communication path carrying instructions and telemetry;
3. identify the sensor observing the result;
4. identify the body, tool, or installed actuator physically performing the action;
5. verify that every link is established, present, and within its current damage and load limits.

If provenance is missing, repair the smallest conflicting sentence. Preserve remote intellectual authorship while assigning the physical verb to an already-present actuator. Do not invent a body, drone, local instance, manipulator, sensor, or travel event to protect shorthand. Repair downstream canon and continuity copies of the same false capability.

Run `scripts/capability-check.py --self-test`, then `scripts/story-check.sh`. Commit and verify the repairs. Return a compact table of each capability break, its physical actuator, files repaired, validation result, and commit link. Do not paste complete chapters into chat.
