# Evaluation Protocol

This protocol standardizes quality evaluation for generated 6-week LinkedIn series.

## 1) Purpose

Ensure repeatable and comparable scoring across runs by using:
- Fixed rubric dimensions
- Clear scoring anchors
- Documented rater workflow

## 2) Unit of Evaluation

Evaluate one completed 6-week series (Weeks 1-6) after:
- HITL 5a content review
- HITL 6a benchmark pass

## 3) Rubric Dimensions (1-5)

Score each dimension from **1 (poor)** to **5 (excellent)**.

### A) Actionability
- **1**: Mostly abstract, no practical next steps.
- **3**: Some specific advice, uneven execution.
- **5**: Concrete, immediately usable guidance throughout.

### B) Voice Consistency
- **1**: Generic AI tone, inconsistent persona.
- **3**: Mixed voice; some sections feel authentic.
- **5**: Strong, coherent, human voice across all posts.

### C) Strategic Depth
- **1**: Surface-level ideas only.
- **3**: Moderate insight but limited nuance.
- **5**: High-signal, nuanced reasoning with meaningful perspective.

### D) Narrative Cohesion
- **1**: Disconnected weekly posts.
- **3**: Partial arc with weak transitions.
- **5**: Clear progressive arc across all six weeks.

### E) LinkedIn Optimization
- **1**: Poor hooks/formatting/CTA fit.
- **3**: Adequate platform fit.
- **5**: Strong hooks, scannability, CTA quality, and platform-native structure.

## 4) Rater Instructions

1. Read the full 6-week set first (no scoring).
2. Re-read and score each rubric dimension using anchors above.
3. Add short rationale (1-3 bullets per dimension).
4. Compute overall score = mean of five dimensions.
5. Record confidence (High/Medium/Low).

## 5) Multi-Rater Procedure (Recommended)

- Minimum 2 independent raters.
- Raters score blind to each other.
- Compute per-dimension variance.
- If any dimension differs by >1.0 points:
  - Hold reconciliation discussion.
  - Record both pre- and post-reconciliation values.

## 6) Reporting Template

Use this template in benchmark notes:

```markdown
## Evaluation Record: <topic/run-id>

- Rater: <name/alias>
- Date: <yyyy-mm-dd>
- Confidence: <High|Medium|Low>

| Dimension | Score (1-5) | Notes |
|-----------|-------------|-------|
| Actionability |  |  |
| Voice Consistency |  |  |
| Strategic Depth |  |  |
| Narrative Cohesion |  |  |
| LinkedIn Optimization |  |  |

- Overall Score (mean):
- Key strengths:
- Key weaknesses:
- Recommended revisions:
```

## 7) Acceptance Thresholds

Default benchmark gate:
- No dimension below **3.0**
- Overall mean at or above **4.0** for target-quality publish readiness

If below threshold, route back to Skills 3-5 for revision and re-evaluate.
