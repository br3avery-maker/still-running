# Publishing

The production system has three ordinary layers:

1. **GitHub manuscript** — accepted Markdown in `stories/` is the source of truth.
2. **Static reader** — the public reading interface presents those files with book navigation, local preferences, and browser-native listening.
3. **Distribution mirrors** — RSS/Atom and Nostr may announce or mirror released chapters without becoming canon authorities.

Do not invent a separate publishing agent, CMS, database, or content format while these layers are sufficient.

## Release schedule

`publishing/schedule.json` is the release manifest. An absent chapter entry means the chapter is available immediately. A future ISO 8601 timestamp hides that chapter from the reader until the timestamp passes:

```json
{
  "scheduled": {
    "stories/12-example.md": "2026-08-07T09:00:00-07:00"
  }
}
```

Scheduling controls presentation, not secrecy. This is a public repository: anyone with the repository URL can read a committed chapter before its reader release. Truly private advance drafts require a private repository, private branch with appropriate access, or uncommitted local work.

Use `prompts/schedule-release.md` to change release timing. The reader consumes the manifest directly, so a rebuild is not required merely for time to pass.

## Nostr later, without replacing Git

- NIP-34 is the established Nostr vocabulary for announcing repositories and conducting Git-adjacent collaboration. Git objects still live on Git-capable servers.
- NIP-23 long-form events are the natural chapter mirror because their content is Markdown and addressable.
- A future scheduled workflow can read the same release manifest, create one NIP-23 event per due chapter, and record the resulting event coordinate so retries remain idempotent.
- Keep signing outside prose and prompts. Use a dedicated publishing key through a supported signer or repository secret when that workflow is deliberately enabled.

Until that workflow exists and has been verified, describe Nostr publishing as planned—not active.
