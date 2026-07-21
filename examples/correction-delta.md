# Example — Correction Delta

```text
The current implementation still detects the hand inconsistently and loses the face landmarks during movement.

Expected:
Stable real-time face and hand landmarks with visibly lower latency, while preserving the existing gesture definition and overlay behavior.

Use the attached recording as the failure reference. Correct only the detection/tracking pipeline and confidence/smoothing logic; do not redesign the UI or change video assets.

Verify under normal light, partial hand occlusion, head movement, and rapid gesture release. Report measured FPS/latency if available.

Execute directly and update the existing STATUS.md. Do not create a plan or another report file.
```
