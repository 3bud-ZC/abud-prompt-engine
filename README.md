<div align="center">
  <h1>Abud Prompt Engine 🚀</h1>
  <p>A compact, highly disciplined prompt-generation skill designed for AI-agent workflows.</p>
</div>

## 📖 Overview
The Abud Prompt Engine is designed to create compact, production-ready prompts for coding agents, AI tools, image/video models, research systems, and deployment workflows. It uses **delta prompting** to avoid repeating prior commands, minimizes token usage, executes user intent directly, and preserves one `STATUS.md` as the project's source of truth.

## ✨ Key Features
- **Delta Prompts:** Generates only what changed (new objectives, constraints, fixes) instead of repeating unchanged context.
- **Token Economy:** Aggressive token budget discipline to reduce cost and context-window bloat.
- **Direct Execution:** Instructs coding agents to execute immediately without generating redundant plans or roadmaps.
- **Single Source of Truth:** Enforces the use of exactly one `STATUS.md` file for project state.
- **Versatile Tool Profiles:** Contains optimized profiles for coding agents (Antigravity, Cursor, Claude Code), image/video tools, workflow automation, and VPS deployment.
- **Built-in Audit Tool:** Includes a local Python script to audit prompts for token cost, redundancy, and forbidden planning patterns.

## 📁 Directory Structure
- `SKILL.md`: The core prompt engine instructions.
- `examples/`: Sample scenarios (New Session, Continuation Delta, Correction Delta).
- `references/`: Deep-dive instructions on delta protocol, tool profiles, output templates, and token economy.
- `scripts/`: Utility scripts, including `prompt_audit.py`.

## 🚀 Installation

### As an AI Agent Skill (e.g., Claude Code, Gemini)
You can install this directly into your AI agent's skills directory.
```bash
mkdir -p ~/.claude/skills
cp -R abud-prompt-engine ~/.claude/skills/abud-prompt-engine
```
*Or place the folder in the skill directory supported by your specific AI tool.*

## 💡 Usage

Activate the skill by asking your AI to generate or improve a prompt.

**Natural Language Examples:**
> *"Write the next Antigravity prompt from this STATUS.md without repeating the previous prompt."*

> *"Turn this bug report into a compact correction prompt for Claude Code."*

> *"Write a standalone Gemini image-edit prompt and preserve everything except the requested change."*

### Recommended Continuation Input
When working on a continuous project, provide the following to the prompt engine:
1. The newest `STATUS.md`.
2. The latest agent result.
3. Any new screenshots, errors, or requested changes.
4. The previous prompt (if exact repetition auditing is required).

The engine will produce *only* the necessary delta.

## 🛠️ Local Audit Script

You can locally audit your generated prompts to ensure they meet the engine's strict standards.
```bash
python scripts/prompt_audit.py current_prompt.txt previous_prompt.txt
```
The audit will report on:
- Approximate token cost.
- Duplicate lines and overlap with the previous prompt.
- Detection of forbidden planning patterns.

## 🔒 Design Constraints
No prompt can be both fully standalone and contain zero repeated context. 
- **New Sessions:** The engine repeats only active, critical constraints.
- **Continuing Sessions:** When the target agent has access to the repository and `STATUS.md`, the engine emits *only* the delta.

---
<div align="center">
  <i>Maintained by <a href="https://github.com/3bud-ZC">Abdullah</a></i>
</div>
