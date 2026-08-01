# Canon compression prompt

Use the GitHub repository `br3avery-maker/still-running` as the source of truth. Read and follow `AGENTS.md`.

Compress `CANON.md` into the smallest high-signal context packet that still protects future writing from contradiction.

Keep:

- established world facts that can affect future scenes;
- each active character's current capabilities, limitations, relationships, obligations, and location or body when known;
- irreversible events and unresolved consequences;
- temporal constraints that can change character age, sequence, capability, or causality, while detailed evidence remains in `continuity/time-map.md`;
- facts needed to understand the immediate story frontier.

Move or remove:

- repeated scene summaries;
- implementation detail that no longer constrains future writing;
- plans and possibilities, which belong in the story map or frontier;
- resolved questions;
- duplicated character information better maintained in `characters/`;
- prose commentary, justification, and historical audit trails already preserved by Git.

Do not change established facts, invent lore, or edit story prose. Do not compress a range into an exact date. Update related continuity files only when needed to keep classifications correct.

Run `scripts/story-check.sh`, commit the compression, verify GitHub, and return the before/after word count, commit or PR link, and a short description of what categories were removed. Do not paste the compressed canon into chat.
