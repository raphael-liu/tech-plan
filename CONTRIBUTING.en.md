# Contributing

[简体中文](CONTRIBUTING.md) | [English](CONTRIBUTING.en.md)

## Scope of changes

- Keep triggers, core decisions, and shared constraints in `SKILL.md`. Put detailed input, output, and provenance guidance in `references/` and avoid duplicating the same rule within a language.
- Preserve the chain of diagnosis, trade-offs, prioritization, alignment, execution cadence, and recalibration. Improve observable decision behavior rather than simply adding questions or length.
- Respect user goals, permissions, and output format. Planning recommendations do not authorize execution.
- Use relative paths. Do not commit personal paths, real business plans, personnel data, secrets, or unauthorized source material. Use fictional data in examples and evaluations.
- Attribute methods and explain applicability. Do not add third-party materials or assume MIT rights over them.

## Bilingual maintenance

- `SKILL.md` is the only discovery entrypoint. `SKILL.en.md` is the complete English workflow loaded when relevant; do not add a second discovery entry or skill frontmatter to it.
- Update both language workflows and relevant references when changing behavior. Usage documentation, contribution guides, and evaluation scenarios use matching `.en.md` files. Preserve original source titles and explain their meaning without inventing official English titles.
- Use consistent terms: Diagnosis, Trade-offs, Prioritization, Alignment, Execution cadence, and Recalibration. Distinguish leading/lagging indicators, execution deviation/invalidated judgment, and proposed/committed/verified states.
- Translation must preserve facts, numbers, periods, units, costs, and commitment levels. Language selection follows higher-priority instructions, then explicit user requests and conversation preferences, rather than source language alone.
- The validator checks counterpart files and links, not semantic equivalence. Exercise cross-language sources and outputs, mixed-language evidence, and language switching when changing language behavior.

## Local checks

Install development dependencies as described in the README, then run:

```bash
python scripts/validate.py
git diff --check
```

For behavior changes, use the repository skill in an independent conversation with relevant [evaluation scenarios](evals/scenarios.en.md). Distinguish structural validation from behavioral validation. Matching headings or keywords does not establish planning quality.

## Change descriptions

Explain the problem, changed behavior, validation, and unverified boundaries. Include anonymized or fictional inputs and observed results for behavioral changes. Do not upload model output containing real team information.
