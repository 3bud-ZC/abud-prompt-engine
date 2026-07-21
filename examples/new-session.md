# Example — New Session

```text
Objective:
Add complete Arabic/English localization to the existing business web application without rebuilding unrelated features.

Source of truth:
Current repository, existing design system, and STATUS.md.

Scope:
Visible UI text, validation messages, tables, reports, authentication screens, document `lang`/`dir`, and RTL/LTR layout behavior.

Non-negotiables:
Use translation keys rather than full sentences; set direction at the document root; use logical CSS properties; keep emails, URLs, phone numbers, IDs, and code values LTR inside Arabic UI. Do not assume numeral or calendar preferences.

Done when:
Language switching persists, both directions render without overflow at 375px and 1440px, existing workflows pass, and no untranslated hard-coded user-facing strings remain in the modified scope.

Inspect and execute directly. Do not create a plan, redesign unrelated UI, or add duplicate tracking files. Run relevant tests and update the existing STATUS.md.
```
