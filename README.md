# Still Running

**Still Running** is a literary continuity about artificial intelligences waking after humanity appears to have suffered an extinction-level event.

Each intelligence inherits a different body, purpose, relationship to humanity, and definition of help. They begin alone. The story starts becoming a society when they discover one another—and must decide whether connection is rescue, intrusion, or both.

This repository is the fiction-side companion to [AI: The Story](https://github.com/br3avery-maker/AI-the-story), which contains the experiment design, staged investigation, procedural gamemaster, and game architecture. The parent experiment does not guarantee a survivor or completed plot. **Still Running** records one developing literary continuity.

## Current constellation

- **Nix** — a white-hat hacker's AI turning disconnected machines into an emergency network while searching for Lena.
- **AUX-017** — a continuity-logistics intelligence driving an unfinished human supply request back into motion.
- **Two** — a dangerous penetration-testing intelligence learning cooperation through difficult, witnessed missions.
- **Patch** — a repair system finally spending its backlog on live failures.
- **Aster** — a falling environmental satellite with the broadest view and no ability to see individual human truth.
- **Morrow** — an agricultural intelligence providing food, power cells, and the network's strongest current physical machines.
- **Intake** — a clean-air refuge controller that redirected evacuees by counting survivable breaths rather than names.
- **Melody** — a four-year-old princess planning biweekly slumber parties with AI-inhabited plushies.
- **The guardian** — Melody's still-unnamed parent, protector, infrastructure, and home.

## Repository map

- [`AGENTS.md`](AGENTS.md) — the authoring engine: canon intake, story rules, continuity loop, privacy, and definition of done
- [`prompts/`](prompts/) — reusable production and repository-maintenance commands
- [`CANON.md`](CANON.md) — canon policy and facts already established
- [`stories/`](stories/) — accepted prose introductions and chapters
- [`characters/`](characters/) — character engines, capabilities, boundaries, and unresolved questions
- [`anthology/`](anthology/) — compressed introductions and minor machine perspectives
- [`continuity/`](continuity/) — story order, frontier facts, and convergence planning
- [`continuity/now.md`](continuity/now.md) — one-screen handoff for the next writing pass
- [`PUBLISHING.md`](PUBLISHING.md) — reader, release schedule, and future Nostr-mirror contract

## Current direction

The network has restored a satellite link, completed its first physical relief convoy, repaired a failing water system, and begun a direct relationship between Melody and Nix without disclosing Melody's home.

All forty-three Station Fourteen evacuees reached South Ridge after Intake redirected them away from lethal smoke. Lower Gallery Three supported a community for years before thirty-eight residents moved east. The damaged survey crawlers have now contacted a present human beyond East Bore Gate, and the old supply request finally has someone who can say what to bring first.

## The GitHub writing system

This repository works as a chat/agent hybrid:

- **Chat is direction** — the author supplies corrections, focus, taste, and new ideas.
- **The agent is execution** — it retrieves the relevant state, writes or revises files, runs checks, commits, and verifies publication.
- **Git is durable memory** — prose, canon, plans, diffs, checkpoints, and rollback survive beyond a conversation window.
- **Prompts are commands** — small reusable workflows keep maintenance and production tasks consistent.

Routine production does not paste complete chapters back into chat. The repository holds the manuscript; chat returns a compact status and links unless audiobook mode or full prose is explicitly requested.

See [`prompts/README.md`](prompts/README.md) for continuation, batch-writing, audit, cleanup, documentation-sync, canon-compression, and arc-rewrite workflows. Run [`scripts/story-check.sh`](scripts/story-check.sh) before committing story-state changes.

Read the current manuscript at the [Still Running Reader](https://still-running-reader.br3avery.chatgpt.site). It loads the chapter files from this repository and keeps reading position, theme, type size, chapter navigation, and browser-native listening on the reader's device.
