# Schedule chapter release

Use the GitHub repository `br3avery-maker/still-running` as the source of truth. Read and follow `AGENTS.md` and `PUBLISHING.md`.

Schedule an existing `stories/NN-*.md` chapter by setting `scheduled[story_path]` in `publishing/schedule.json` to an ISO 8601 timestamp. If I gave a local date or time, resolve it using the manifest timezone and write the explicit UTC offset. If I asked for immediate release, remove that chapter's schedule entry instead of writing a timestamp in the past.

Do not edit story prose, canon, character files, or continuity state. Validate the JSON, run `scripts/story-check.sh`, commit the manifest change, verify the GitHub file and commit links, and return compact status only.

Scheduling controls visibility in the reader, not access to a chapter already committed in this public repository. Do not claim that a scheduled chapter is private. Do not claim a Nostr release occurred unless a configured publishing workflow produced and verified the event.

Chapter: `[stories/NN-title.md]`

Release time: `[date, time, and timezone—or "now"]`
