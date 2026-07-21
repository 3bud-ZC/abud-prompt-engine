# Compact Output Templates

Use the smallest matching template. Omit unused headings.

## Continuation Delta — Coding Agent

```text
Treat the current repository and STATUS.md as the source of truth. Preserve completed work and existing constraints unless overridden below.

Objective now:
[one milestone]

Observed issue:
[only new or unresolved failure]

Change:
[precise requested behavior]

Scope:
[allowed area and essential do-not-touch boundary]

Verify:
[smallest observable checks]

Execute directly; do not create a plan. Update the existing STATUS.md after completion.
```

## Correction Delta

```text
The latest result still [failure].
Expected: [behavior].
Evidence: [screenshot/log/file].
Correct only [scope]; preserve [regression-sensitive behavior].
Verify with [test].
Update the existing STATUS.md. Do not create a plan.
```

## New Session — Coding Agent

```text
Objective:
[outcome]

Source of truth:
[repository, STATUS.md, references]

Scope:
[allowed area]

Non-negotiables:
[only active critical constraints]

Done when:
[observable criteria]

Inspect the project and execute directly. Do not create a plan, roadmap, unrelated features, or duplicate status files. Run relevant verification and update the existing STATUS.md.
```

## Image Edit

```text
Edit the supplied image, preserving [identity/composition/background/lighting].
Change only [requested edit].
Result: [realism/style/framing].
Avoid: [specific failure modes].
```

## Video From Image

```text
Animate the supplied image for [duration].
Motion: [subject/environment].
Camera: [movement or locked].
Preserve: [identity/composition/details].
Avoid: [morphing/drift/new objects/text/cuts].
End: [loop/hold/final action].
```
