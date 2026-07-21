# Delta Prompting Protocol

## Purpose

Continuation prompts should transmit state changes, not replay history.

## Source Priority

Use this priority when resolving conflicts:

1. The user's newest explicit instruction.
2. Newly supplied screenshots, logs, files, or test results.
3. Current repository state.
4. Current `STATUS.md`.
5. Previous prompt.
6. Older assumptions.

## Delta Record

A continuation prompt may contain these fields only when relevant:

```text
Objective now:
Observed issue:
Expected result:
New evidence:
Scope:
Override:
Verify:
Update STATUS.md:
```

Omit empty fields.

## Repetition Decision Table

| Earlier instruction | Repeat? | Treatment |
|---|---:|---|
| Completed and verified | No | Omit |
| Unchanged and present in STATUS.md | No | Reference source of truth |
| Unchanged but target has no context | Yes | Compress into New Session baseline |
| Violated by the agent | Yes | State once as a correction |
| Production safety boundary | Usually | Keep concise |
| New exception or override | Yes | Use `Override: old → new` |
| Generic quality request | No | Replace with measurable acceptance criterion |

## Safe Carry-Forward

Preferred sentence:

`Treat the current repository and STATUS.md as the source of truth. Preserve completed work and existing constraints unless explicitly overridden below.`

This sentence can replace long repeated sections when the target agent can access those sources.

## Correction Pattern

```text
The latest implementation still [observable failure].
Change only [scope] so that [observable expected behavior].
Use [new evidence] as the reference.
Do not alter [specific regression-sensitive behavior].
Verify by [test].
Update the existing STATUS.md with the result.
```

## New Session Compression

When prior context is unavailable, reconstruct only active state:

- Current objective.
- Relevant completed foundation.
- Active constraints.
- Current blocker.
- Required verification.

Never include the full chronological history.
