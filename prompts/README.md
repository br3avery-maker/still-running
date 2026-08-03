# Prompt toolkit

These prompts turn recurring authoring and maintenance jobs into explicit agent workflows. Paste one into a new chat or invoke it by filename.

## Production

- [`next-chapter.md`](next-chapter.md) — write, save, validate, and commit one chapter without pasting prose into chat.
- [`batch-chapters.md`](batch-chapters.md) — produce several sequential chapters with one commit per chapter.
- [`rewrite-arc.md`](rewrite-arc.md) — revise an existing chapter range in place after a plot-health audit.
- [`schedule-release.md`](schedule-release.md) — schedule when an existing chapter appears in the reader and future distribution mirrors.

## Repository maintenance

- [`repo-audit.md`](repo-audit.md) — read-only diagnosis of story state, drift, redundancy, and production risks.
- [`sync-docs.md`](sync-docs.md) — reconcile README, canon, characters, story map, and frontier with accepted prose.
- [`audit-time.md`](audit-time.md) — scan all prose for timestamp-shaped evidence and rebuild uncertainty as sourced `|#####|` ranges.
- [`audit-capabilities.md`](audit-capabilities.md) — trace physical and sensory verbs through established bodies, tools, locations, and communication paths, then minimally repair false embodiment.
- [`cleanup-repo.md`](cleanup-repo.md) — remove or consolidate stale non-prose material without silently deleting accepted fiction.
- [`compress-canon.md`](compress-canon.md) — shrink canon into a high-signal context packet for future chapters.

## Output default

Production prompts save prose to GitHub and return compact status only. Add **“audiobook mode”** or **“post the full prose”** when a readback is wanted.

All production and chronology work that touches age, elapsed time, development, or historical placement follows [`../skills/temporal-continuity.md`](../skills/temporal-continuity.md). A possible chronology with a missing link is logged as an explanation debt; an empty interval is repaired before production continues.
