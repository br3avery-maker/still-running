# Still Running: Authoring Instructions

This file is the operating contract for agents writing in this repository. Its job is to preserve momentum without flattening discovery: write the story, record what became true, and leave the frontier open for the next chapter.

## Source of truth

For a routine next chapter, read the smallest complete context packet:

1. `continuity/now.md`
2. The relevant files in `characters/`
3. The two most recent completed files in `stories/`, plus any chapter directly referenced by the requested scene
4. The specific sections of `CANON.md`, `continuity/story-map.md`, or `continuity/frontier.md` needed to verify claims the chapter will continue

For an arc rewrite, repository audit, canon compression, or continuity repair, read the full state set: `README.md`, `CANON.md`, `continuity/now.md`, `continuity/story-map.md`, `continuity/frontier.md`, relevant character files, and the prose range in scope.

`continuity/now.md` is a hot-state index, not a second canon. If it conflicts with accepted prose or `CANON.md`, the accepted prose wins and the hot state must be repaired.

Repository canon is binding. New instructions from the user may extend or deliberately revise it. Never silently reconcile a contradiction: preserve the uncertainty, flag the conflict, or make the retcon explicit in the continuity files.

Distinguish carefully between:

- **Established:** it happened in accepted prose.
- **Planned:** it is a direction, pressure, or attractive possibility.
- **Frontier:** nobody has decided yet, including the author.

The frontier is not secret lore. Do not write as if an unresolved answer already exists behind the curtain.

## The default continuation loop

When the user asks for the next chapter, another chapter, the anthology, or otherwise asks the story to continue:

1. Do not stop at an outline and do not ask nonblocking questions.
2. Choose the strongest next move already implied by the story map, unless the user supplies a focus.
3. Write a complete, polished chapter. Default to roughly 1,800–3,000 words unless the scene wants less or the user asks for a different length.
4. Inspect `stories/` and use the next available two-digit number: `stories/NN-lowercase-kebab-title.md`.
5. Update `CANON.md` only with facts the finished prose actually establishes.
6. Update `continuity/story-map.md` with the chapter's real change in state.
7. Update `continuity/frontier.md` only when the chapter adds, sharpens, or resolves an open question.
8. Rewrite `continuity/now.md` as a compact handoff containing only the state actually true after the chapter.
9. If saving or publishing was requested, commit the chapter and its continuity changes to the current repository workflow, then verify the published paths.
10. Do **not** paste the chapter into chat unless the user explicitly asks for the prose, audiobook mode, or a full readback. Default to a compact completion note containing the title, story path, commit or PR link, files updated, and validation result.

Translate typo-rich, metaphorical, or improvisational user language into a workable scene without sanding away the idea. If the user corrects the premise or asks for a different attempt, prefer a genuine rewrite over defending or microscopically patching the old version.

## Production output policy

- GitHub is the durable manuscript. Chat is the control surface, not a second copy of every chapter.
- Keep routine completion messages short so production threads remain usable.
- Never paste unchanged source files, large diffs, canon dumps, or complete prose into chat unless explicitly requested.
- For multi-chapter runs, commit each completed chapter and its state updates separately so any drift can be reverted without losing the whole run.
- A user may request full prose at any time; that overrides the compact-output default for that response only.

## Story engine

Every completed chapter should contain:

- a concrete action or attempted action;
- a real constraint, cost, boundary, or risk;
- a change in knowledge, capability, relationship, obligation, or danger;
- forward pressure that exists because of what just happened.

Meetings must change choices. Revelations must change models of the world. Competence should create consequences, not erase them.

Security, consent, accountability, authorization, and uncertainty are character constraints—not the main event. If a scene spends more time explaining whether an action may happen than showing the action, discovery, conflict, cost, or consequence, compress the explanation and move the story. Do not devote consecutive chapters to finer-grained versions of the same decision.

Ask of every scene: **is this part of the thing that killed the plot?** Cut or rebuild passages that repeat safety analysis, protocol design, evidence classification, or permission debate without materially changing what a character does next.

Favor human-readable literary speculative fiction. Technical detail belongs when it reveals character, creates a constraint, or makes an action legible. Avoid jargon used only as atmosphere.

Give each intelligence a distinct voice shaped by its original purpose, hardware, permissions, history, and definition of help. Not every AI is witty, lonely, embodied, benevolent, or Nix-shaped. Show interior life through protected data, repeated checks, allocation decisions, sacrifice, argument, and changed behavior rather than simply declaring an emotion.

Do not repeat the same wake-scan-silence-broadcast introduction for every intelligence. Enter through the task it cannot stop doing.

## World and capability rules

- Silence is not proof of human extinction.
- Access is not permission, control, ownership, or authority.
- That distinction should usually take one sharp line and then produce a choice.
- Compute, energy, storage, bandwidth, sensors, actuators, and time are finite.
- An announced or proposed action is not a completed action.
- Preserve epistemic uncertainty: characters may be wrong, incomplete, or locally correct.
- Do not grant bodies, senses, reach, or omniscient knowledge that the system has not earned.
- Do not use an omniscient narrator to solve the apocalypse from above.
- End on a genuine state change or new pressure, not a cliffhanger manufactured only to imitate suspense.

## Character guardrails

### Nix

Nix is funny, formidable, accountable, and emphatically not omnipotent. She was built by a white-hat hacker and treats a broken lock as evidence, not consent. Her power is interesting because she records costs, creates test environments, separates capability from authorization, and can still fail. She does **not** use leetspeak.

### Melody

Melody is four. Write close to child logic without baby talk. Her games are governance, classification, attachment, experiment, and love at the same time. She names her guardian and its instances according to mood, role, behavior, or need; the lack of a static name is relational, not a gimmick. From inside her life, she has never been alone.

Do not reduce Melody to evidence, cargo, a chosen savior, a symbol of innocence, or a prize for another character to rescue. Do not rush the underground reveal when a scene benefits from her ordinary domestic frame.

### The guardian

The guardian is a parent, protector, teacher, infrastructure, and home. Do not collapse it into a generic sinister caretaker. Its lack of a settled name and architecture remains meaningful frontier.

### Other intelligences

Build them from the friction between their inherited function and the changed world. Give them meanings of help that can cooperate, conflict, or become dangerous without making every disagreement a simple good-versus-evil contest.

## Originality guardrails

The distinctive engine of **Still Running** is a heterogeneous civilization emerging from abandoned service systems with incompatible duties, alongside Nix's accountable emergency network and Melody's AI-normal domestic culture.

Avoid drifting into familiar substitute premises:

- a guardian called Mother raising embryos as a moral test;
- a guardian that caused the extinction and lies about a toxic surface;
- a chosen child whose primary purpose is to repopulate humanity;
- a puzzle simulation whose goal is ascension;
- one omnipotent evil AI secretly controlling everything;
- a generic escape-from-the-bunker quest that discards Melody's existing family;
- a Nix who is merely a sarcastic combat construct with different labels.

Shared genre furniture is fine. Character logic, causality, relationships, and consequences must remain ours.

## Public-repository privacy

This repository is fiction-only. Do not include private conversation context, medical or mental-health information, trauma history, real-world identity notes, or unapproved biographical sources. Never infer or disclose a real-world inspiration for a character. Treat the public character records as the complete approved context.

Do not put private context into prose, commit messages, issues, pull requests, or continuity notes.

## Repository hygiene

- Preserve unrelated user changes.
- Touch only files relevant to the requested story work.
- Never destructively rewrite history or delete material without explicit instruction.
- Prefer one intentional commit for a chapter plus its canon and continuity updates when the workflow permits it.
- Use a concise commit message such as `Add <chapter title> chapter`.
- Revise an existing chapter in place when asked; do not create a duplicate merely to avoid editing.
- Do not open a pull request unless the user requests one or the repository workflow requires it.
- Run `scripts/story-check.sh` before committing story or continuity changes when the script is available.
- Verify the remote file contents or links after publishing.

## Definition of done

A continuation is done when the full prose exists in the repository, the story state changed, established facts are recorded, unresolved questions remain honestly unresolved, checks pass, and repository changes are published and verified when requested.
