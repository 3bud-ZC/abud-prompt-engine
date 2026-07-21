# Token Economy Rules

## Remove First

Delete these unless essential:

- “You are a world-class expert…” introductions.
- Repeated project background.
- Explanations of common technologies the target already uses.
- Multiple phrasings of the same prohibition.
- Broad requests such as “make it professional,” “do your best,” or “ensure high quality.”
- Full file contents when a path or attachment reference is available.
- Long final-report templates.
- Planning instructions for agents expected to execute.
- Repeated success criteria expressed in different words.

## Replace Vague Language

| Vague | Compact measurable replacement |
|---|---|
| Make it responsive | Verify at 375px and 1440px with no overflow |
| Fix all bugs | Fix only failures caused by this milestone |
| Make it professional | Match the supplied reference and existing design system |
| Test everything | Run tests covering changed behavior |
| Do not break anything | Preserve existing public contracts and verify affected regressions |
| Analyze the project first | Inspect relevant files, then execute directly |

## Compression Patterns

Use:

`Preserve unrelated behavior.`

Instead of listing every unrelated feature.

Use:

`No new dependencies unless technically required; document any addition in STATUS.md.`

Instead of multiple dependency warnings.

Use:

`Verify changed behavior and fix regressions introduced by this change.`

Instead of a generic full-system QA request.

## Token Budget Escalation

Increase prompt length only when one of these applies:

- Destructive production operation.
- Multiple systems or repositories.
- Security/authentication/data migration.
- Exact visual reproduction from references.
- Ambiguous failure requiring evidence mapping.
- A new session with no accessible project state.

## Final Compression Test

For every sentence ask:

1. Does it add new executable information?
2. Does it prevent a likely failure?
3. Does it define observable completion?
4. Is it required because the target lacks context?

Delete the sentence if all answers are no.
