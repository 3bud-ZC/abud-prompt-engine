# Example — Continuation Delta

## Context

The previous prompt built face and hand tracking. The user reports delayed detection and an incorrectly persistent video overlay. The agent has the repository and `STATUS.md`.

## Output

```text
Treat the current repository and STATUS.md as the source of truth. Preserve completed work and existing constraints.

Objective now:
Make face/hand tracking responsive and show the overlay video only while the live gesture is valid.

Observed issue:
Detection is delayed and unstable. The video starts independently and remains visible after the hand leaves the required pose.

Change:
Use continuous landmark tracking with temporal smoothing. The valid gesture is hand touching the nose while moving right. Start/show the video only during that state; pause and hide it immediately when the gesture stops. Do not let playback state control visibility.

Verify:
Test gesture entry, sustained hold, rightward movement, release, false positives, and repeated activation. Confirm no new runtime errors.

Execute directly; do not create a plan. Update the existing STATUS.md with changed files and test results.
```

Why it is compact: it does not repeat setup, stack, deleted web files, or previously completed milestones.
