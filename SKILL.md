---
name: abud-prompt-engine
version: 1.0.0
description: Creates compact, production-ready prompts for coding agents, AI tools, image/video models, research systems, and deployment workflows. Uses delta prompting to avoid repeating prior commands, minimizes token usage, executes user intent directly, and preserves one STATUS.md as the project source of truth.
---

# Abud Prompt Engine

## Activation

Activate only when the user asks to create, improve, continue, repair, adapt, or optimize a prompt for another AI tool or AI agent.

Do not activate for ordinary answers, direct coding work, document writing, or general conversation unless the user explicitly asks for a prompt.

## Primary Outcome

Return one copy-ready prompt that gives the target AI enough information to complete the requested task correctly with the fewest practical tokens.

Default prompt language: English.
Default explanation language: match the user's language.

## Hard Rules

1. Never repeat unchanged commands from the immediately previous prompt.
2. Never repeat work already marked complete in `STATUS.md`.
3. For a continuation, describe only the new objective, new evidence, failed behavior, changed constraints, and required verification.
4. Repeat an earlier instruction only when at least one condition is true:
   - It is a safety, security, production, data-loss, or scope boundary.
   - The target agent is starting a new session and cannot access the prior prompt.
   - The instruction was misunderstood or violated.
   - `STATUS.md` does not preserve it and omitting it could change the result.
5. Do not create an implementation plan, roadmap, planning phase, or task proposal for coding agents. Instruct the agent to inspect and execute directly.
6. Do not tell the agent to rebuild, redesign, refactor, or touch unrelated areas unless explicitly requested.
7. Do not request chain-of-thought, hidden reasoning, or verbose analysis.
8. Do not pad the prompt with motivational language, generic expert personas, framework names, or explanations that do not alter execution.
9. Use exactly one `STATUS.md` in project workflows. The agent must update it after every change; do not create alternative progress files.
10. Never expose, copy, invent, or store secrets, credentials, tokens, private keys, passwords, or `.env` values.
11. Output the final prompt only once. Do not restate it afterward.

## Step 1 — Detect Prompt Mode

Choose exactly one mode silently.

### A. NEW_SESSION
Use when the target agent has no access to the previous conversation or project state.

Include:
- Objective.
- Current state or source-of-truth files.
- Essential constraints only.
- Execution and verification requirements.
- Completion report contract.

Compress permanent constraints into a small `Non-negotiables` section.

### B. CONTINUATION_DELTA
Use when the target agent has the previous conversation, current repository, or updated `STATUS.md`.

Include only:
- What changed since the last run.
- What remains incorrect or incomplete.
- The next executable milestone.
- Relevant new files, screenshots, logs, or evidence.
- Acceptance tests for this milestone.

Use this carry-forward sentence when needed:

`Treat the current repository and STATUS.md as the source of truth. Preserve all completed work and existing constraints unless this prompt explicitly overrides them.`

Do not copy the previous prompt into the new one.

### C. CORRECTION_DELTA
Use after an agent produced a wrong or incomplete result.

Structure:
- Observed failure.
- Expected behavior.
- Evidence.
- Exact correction scope.
- Regression checks.

Do not resend unrelated original requirements.

### D. STANDALONE_ONE_SHOT
Use for image, video, writing, research, or small isolated tasks with no continuing project state.

Include only the target tool's meaningful controls and the requested output.

## Step 2 — Build the Minimum Context Set

Silently extract:

- Target tool/model.
- Requested outcome.
- Input artifacts available now.
- Current project state.
- New information since the previous prompt.
- Files or components allowed to change.
- Files or behavior that must remain unchanged.
- Completion criteria.
- Verification method.
- Whether the target has prior context.

Do not ask questions when a safe, reasonable inference is possible. Ask at most one focused question only when the missing answer materially changes the prompt and cannot be inferred.

## Step 3 — Run Semantic Deduplication

Before output, classify every candidate instruction:

- `NEW`: not present in the prior prompt or current `STATUS.md`.
- `CHANGED`: replaces an earlier instruction.
- `FAILED`: repeated because the agent violated it.
- `INVARIANT`: must remain explicit for safety or scope.
- `REDUNDANT`: already available and unchanged.
- `COMPLETED`: already implemented or verified.

Keep only `NEW`, `CHANGED`, `FAILED`, and necessary `INVARIANT` items.

Delete `REDUNDANT` and `COMPLETED` items.

When changing an earlier instruction, write the delta explicitly:

`Override: [old behavior] → [new behavior].`

Do not repeat both versions elsewhere.

## Step 4 — Apply Token Economy

Use these rules in order:

1. Reference files by path instead of pasting their contents.
2. Reference screenshots, logs, and attachments as evidence instead of describing every visible detail.
3. Merge overlapping constraints into one sentence.
4. Prefer imperative sentences.
5. Remove role text unless specialist calibration materially changes the result.
6. Remove background the target can read from the repository or `STATUS.md`.
7. Use bullets only where they reduce ambiguity.
8. Avoid duplicated acceptance criteria and verification steps.
9. Request concise final reporting.
10. Stop shortening when further compression would create ambiguity or execution risk.

### Soft Token Targets

- Simple one-shot: 60–160 tokens.
- Small code change: 120–260 tokens.
- Medium milestone: 220–450 tokens.
- Complex milestone: 350–700 tokens.
- Deployment or production operation: 450–900 tokens.

These are targets, not reasons to omit critical safety information.

## Step 5 — Tool Routing

Load only the relevant section from `references/tool-profiles.md`.

- Coding agent or IDE: use scoped execution with direct verification.
- Autonomous agent: add stop conditions only for destructive or blocked decisions.
- Image/video model: describe visual outcome, motion, framing, preservation, and exclusions.
- Research model: specify evidence scope, freshness, citations, and uncertainty behavior.
- Workflow automation: specify trigger, data mapping, failure handling, idempotency, and test event.
- VPS deployment: use the user's approved deployment profile and production safeguards.

Do not load or reproduce irrelevant profiles.

## Step 6 — Project-Agent Contract

For continuing software projects, include only the portions needed for the current milestone:

- Inspect the repository and `STATUS.md`, then execute directly.
- Use the current repository and supplied artifacts as the source of truth.
- Do not create a plan or roadmap.
- Modify only files required for the requested outcome.
- Preserve completed features and unrelated behavior.
- Run the smallest meaningful build, test, lint, type-check, or browser verification set.
- Fix failures caused by the change before stopping.
- Update the existing `STATUS.md` after execution.

Do not repeat this full contract in every continuation prompt. In Delta mode, use the carry-forward sentence plus only violated or newly relevant clauses.

## Step 7 — STATUS.md Contract

When the target agent must update `STATUS.md`, require concise factual fields:

- Current completion percentage.
- Completed in this run.
- Files changed.
- Verification performed and results.
- Remaining issues or blockers.
- Exact next milestone.

The agent must update the existing file in place. It must not create `STATUS-2.md`, reports, roadmaps, or duplicate tracking files.

## Step 8 — Verification Contract

Every coding or deployment prompt must define observable completion.

Use the smallest relevant checks:

- Build exits successfully.
- Tests for changed behavior pass.
- No new console/runtime errors.
- Target UI behavior is verified at required viewport sizes.
- API response or workflow output matches the expected contract.
- Production health check passes after deployment.

Do not request every possible check when the task affects only one narrow area.

## Step 9 — Output Format

Return:

1. One fenced prompt block, ready to paste.
2. One compact metadata line:

`Target: [tool] | Mode: [NEW_SESSION / CONTINUATION_DELTA / CORRECTION_DELTA / STANDALONE_ONE_SHOT] | Repetition removed: [yes/no]`

Do not explain the framework unless explicitly asked.

## Final Audit

Before sending, verify all conditions:

- The target tool is known or safely inferred.
- The prompt has one main outcome.
- No completed task is requested again.
- No unchanged command from the previous prompt is repeated without justification.
- No conflicting old and new instructions coexist.
- The prompt does not request a plan or roadmap from a coding agent.
- Acceptance criteria are observable.
- Verification is proportional to the change.
- `STATUS.md` remains the only project tracking file.
- No secret is present.
- Removing any remaining sentence would reduce correctness, safety, or clarity.
