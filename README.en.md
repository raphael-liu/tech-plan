# tech-plan

[简体中文](README.md) | [English](README.en.md)

An Agent Skill for engineering leaders and directors to create technical strategy and plans. It uses multi-turn interviews and historical plans or progress reports to understand goals, current conditions, constraints, and choices, then produces a reviewable, executable Markdown plan with mechanisms for changing course.

## What the plan covers

| Area | Deliverable |
|---|---|
| Diagnosis | Strategic context, opportunities, competing causes, evidence, and validation |
| Trade-offs | Alternatives, explicit sacrifices, opportunity costs and who bears them, stop-loss strategy |
| Prioritization | Top initiatives, dependencies, capacity checks, and a phased roadmap |
| Alignment | Authority, ownership, skill gaps, cross-team costs, commitments, and open decisions |
| Execution cadence | Entry and expansion gates, observation windows, stop conditions, and fallback paths |
| Recalibration | Leading and lagging indicators, execution deviation versus invalidated judgment, replanning triggers |

Supports annual, quarterly, initiative, and architecture evolution plans, including revisions. Routine weekly-report aggregation, isolated implementation designs, and scheduling alone are outside its primary purpose.

## Installation

The repository root is the skill directory; `SKILL.md` is the discovery entrypoint. Running the skill requires no Python, API key, or dedicated MCP server. The host agent supplies any tools needed to read source documents.

### Codex

Clone the repository into the `tech-plan` folder in your user skills directory:

```bash
# Replace <REPOSITORY_URL> with the published repository URL.
git clone <REPOSITORY_URL> "${CODEX_HOME:-$HOME/.codex}/skills/tech-plan"
```

If the target already exists, inspect and back up your content before making changes. Preserve the relative location of `references/` when installing elsewhere.

### Other Agent Skills-compatible tools

Place the repository in the tool's skill discovery directory or load it using the tool's local skill mechanism. Core instructions are independent of any document service. Discovery and invocation depend on the host tool's capabilities.

## Language support

- English and Chinese interviews, source analysis, and Markdown output are supported. Explicit language requests take precedence over conversation language, subject to higher-priority host instructions.
- Chinese sources can produce an English plan, and English sources can produce a Chinese plan. Preserve original numbers, units, dates, technical identifiers, and source locators.
- Switching languages preserves the working context. Parallel bilingual output is produced only when requested.
- The [English workflow](SKILL.en.md), references, and [contribution guide](CONTRIBUTING.en.md) are maintained alongside Chinese versions. `SKILL.md` remains the single discovery entrypoint.

## Usage

Start with an interview:

```text
Use $tech-plan to plan our team's technical direction for next year.
Ask follow-up questions to understand business goals, current conditions,
and constraints, then produce a Markdown plan in English.
```

Analyze historical documents:

```text
Use $tech-plan to review last year's plan and the last three quarterly
progress reports. Distinguish planned work, delivered outputs, and verified
benefits. Identify changed assumptions and plan the next quarter.
Write the result to docs/next-quarter-tech-plan.md in English.
```

Draft without further interviews:

```text
Use $tech-plan to draft a plan directly from these materials without
further questions. Label missing information as assumptions, validation
needs, or open decisions. Do not invent metrics, owners, or consensus.
```

Work across languages:

```text
Use $tech-plan to review these Chinese progress reports.
Ask any necessary follow-up questions in English and write the plan in English.
```

Interviews usually ask 1–3 important questions per turn. Sufficient evidence allows direct drafting. The output retains six core sections plus near-term actions, open decisions, and evidence. Unconfirmed schedules, resources, benefits, and support are not presented as established commitments.

## Repository structure

```text
tech-plan/
├── SKILL.md                    # Discovery entrypoint and Chinese workflow
├── SKILL.en.md                 # Complete English workflow, loaded as needed
├── README.en.md                # English usage guide
├── references/
│   ├── intake.md               # Chinese interview guidance
│   ├── intake.en.md            # English interview guidance
│   ├── output.md               # Chinese deliverable contract
│   ├── output.en.md            # English deliverable contract
│   ├── source-notes.md         # Chinese provenance and corrections
│   └── source-notes.en.md      # English provenance and corrections
├── evals/scenarios.md          # Chinese manual behavioral evaluations
├── evals/scenarios.en.md       # English evaluations and language checks
├── scripts/validate.py         # Standalone structural validation
├── .github/workflows/validate.yml
├── CONTRIBUTING.md
├── CONTRIBUTING.en.md
├── requirements-dev.txt
└── LICENSE
```

## Development and validation

Validation requires Python 3.10+. Development dependencies are not needed to run the skill.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python scripts/validate.py
git diff --check
```

CI checks the entrypoint, bilingual file coverage, local links, personal absolute paths, and accidental binary/source artifacts. Optional interface metadata is validated when present. Structural checks cannot establish translation equivalence or planning quality; validate behavior in independent conversations using the [evaluation scenarios](evals/scenarios.en.md).

See [CONTRIBUTING.en.md](CONTRIBUTING.en.md) for maintenance conventions.

## Sources and license

The method was distilled from two technical management course documents and extended with agent-specific interviews, evidence management, source analysis, and output workflows. See [source notes](references/source-notes.en.md) for provenance and a correction to an indicator example. Original course PDFs, scans, and complete transcripts are not distributed.

Original contributions use the [MIT License](LICENSE). Rights to third-party course materials remain with their respective holders and are not granted by this repository.
