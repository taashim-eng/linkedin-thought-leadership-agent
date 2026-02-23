# Contributing

Thanks for contributing to this project.

## Development Scope

This repository is documentation- and skills-driven. Most contributions will touch:
- skill definitions under `skills/`
- benchmark/evaluation docs
- setup and workflow documentation

## Doc Update Conventions

When changing docs (`*.md`), follow these conventions:

1. **Keep a single source of truth**
   - If benchmark numbers change, update `benchmark/BENCHMARK_APPENDIX.md` first, then sync references in `README.md`.

2. **Prefer additive, traceable edits**
   - Use explicit headings and short sections.
   - Preserve existing section structure unless a reorganization is necessary.

3. **Cross-link related docs**
   - New process docs should be linked from `README.md` or another obvious entry point.

4. **Avoid environment-specific secrets/config in docs**
   - Never commit access tokens or personal credentials.
   - Use placeholders and local configuration guidance.

5. **Preserve portability**
   - Provide platform-neutral commands where possible.
   - If OS-specific guidance is needed, clearly label it.

## Skill File Conventions

- Keep each skill narrowly scoped and named by role.
- Include expected inputs, outputs, workflow, constraints, and failure modes.
- Any behavior-affecting changes should be accompanied by updates to `scripts/check_skill_regressions.py` when appropriate.

## Validation Before PR

Run these checks before opening a pull request:

```bash
python3 scripts/check_skill_regressions.py
```

Optionally run local markdown lint:

```bash
npx markdownlint-cli2 "**/*.md" "#node_modules"
```

CI will enforce markdown linting, markdown link validation, and the skill regression check script.

## Pull Request Expectations

- Keep PRs focused and reasonably small.
- Describe what changed, why, and how it was validated.
- Include command outputs/check summaries in the PR description.
