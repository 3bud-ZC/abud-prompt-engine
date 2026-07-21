# Tool Profiles

Load only the profile that matches the target.

## Antigravity

- Describe the outcome, scope, evidence, and verification.
- Do not ask it to create an implementation plan or roadmap.
- Instruct it to inspect the repository and execute directly.
- Use browser verification when UI behavior is involved.
- Keep one milestone per prompt.
- Use the latest `STATUS.md` as continuation state.
- Ask before destructive production operations only.

## Claude Code

- Name relevant paths or tell it to discover only the files related to the issue.
- State the target behavior and do-not-touch boundary.
- Do not request visible chain-of-thought.
- Prevent unnecessary abstractions, files, dependencies, and refactors.
- Require build/tests proportional to the change.
- For continuation, send only the delta and point to `STATUS.md`.

## Cursor / Windsurf / Cline

- Anchor the prompt to files, components, functions, or observable UI behavior.
- Define current behavior, desired change, scope, and done condition.
- Avoid global refactoring language.
- Keep one tightly scoped edit per prompt where practical.

## ChatGPT / GPT-5.x

- Use compact, explicit output contracts.
- Specify whether tools, browsing, files, or code execution should be used.
- Avoid reasoning scaffolds and repeated context.
- State final format and completion criteria.

## Gemini

- For grounded work, require use of supplied files or references only.
- For strict formatting, provide a compact schema or example.
- For image editing, distinguish preservation requirements from requested changes.
- Avoid unsupported claims and invented citations.

## Image Generation or Editing

Include only relevant fields:

- Subject and requested change.
- Composition/crop/aspect ratio.
- Lighting/material/style.
- Elements that must remain identical.
- Realism level.
- Exclusions/negative constraints.

For editing, explicitly say this is an edit of the supplied image, not a new composition, when supported by the target tool.

## Video Generation

Include:

- Source image or initial scene.
- Duration.
- Subject motion.
- Camera motion.
- Environmental motion.
- What must remain stable.
- Loop or ending behavior.
- Exclusions such as morphing, face drift, text, or scene replacement.

## Research AI

- Define the exact question and date/freshness requirement.
- Prefer primary sources.
- Require citations adjacent to claims.
- Distinguish verified facts, uncertainty, and inference.
- Define output length and comparison criteria.

## n8n / Make / Zapier

- State trigger, inputs, transformations, actions, credentials as placeholders, failure handling, retries, idempotency, and test event.
- Do not include real secrets.
- Require exportable workflow output only when the target supports it.

## VPS Deployment

Use the approved ABUD FUN deployment profile:

- VPS: `167.99.157.6`, Ubuntu, Nginx, PM2, local PostgreSQL where needed.
- Use local upload/package as source of truth; no `git pull` unless explicitly requested.
- Deploy under `/var/www/<app_name>/releases/<timestamp>` with `/current` symlink.
- Select an unused internal port.
- Build and test before switching traffic.
- Back up the current release and provide rollback.
- Do not touch other production projects.
- Never print or store secrets.
- Return URL, PM2 status, Nginx config/path, port, release paths, health checks, and rollback command.
