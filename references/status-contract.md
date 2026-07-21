# STATUS.md Contract

## Single Source of Truth

Every continuing AI-agent project uses one file named `STATUS.md`.

The file is created once and updated in place after every agent run.

Do not create:

- `STATUS-2.md`
- `PROGRESS.md`
- `ROADMAP.md`
- `IMPLEMENTATION_PLAN.md`
- duplicate completion reports

## Minimum Content

```markdown
# Project Status

## Progress
- Completed: NN%
- Remaining: NN%

## Completed This Run
- ...

## Files Changed
- `path`: factual change

## Verification
- command/test: result

## Remaining / Blockers
- ...

## Next Milestone
- one exact executable milestone
```

## Update Rules

- Preserve useful prior history in concise form.
- Remove stale claims contradicted by the repository.
- Do not mark work complete without verification.
- Do not store secrets, credentials, or `.env` contents.
- Keep the file concise enough to send back to the prompt generator.

## Prompt Generator Use

When `STATUS.md` is supplied:

1. Extract completed work and omit it from the next prompt.
2. Extract remaining work and select one next milestone.
3. Extract failed verification and target it directly.
4. Preserve active constraints by reference instead of repeating them.
