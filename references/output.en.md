# Markdown technical plan structure

[简体中文](output.md)

This is a content contract, not a form to fill mechanically. Keep all six sections and scale subsections, tables, and detail to the problem. Use tables for comparisons and prose for causal reasoning. Explain inapplicable dimensions and consequential gaps; empty tables are not analysis. Use the selected output language throughout headings, prose, tables, and status labels; preserve original source titles, identifiers, and facts.

## Opening

`# <Team/domain> technical plan (<planning horizon>)`

Include version/date, evidence cutoff, scope, and status: draft, pending decision, or confirmed with evidence. Lead with a decision summary: value, key judgment, priorities, the most consequential sacrifice and its cost, and decisions requiring approval.

State mission, parent strategy, team responsibilities, boundaries, and constraints. Distinguish business outcomes, technical capabilities, and quality requirements:

| Goal ID | Beneficiary and value | Baseline/period | Target/acceptance definition | Deadline | Source and certainty |
|---|---|---|---|---|---|

Mark unknowns and how to establish them. Never copy course example numbers as actual team targets.

## 1. Diagnosis: problem diagnosis cards

Connect strategy → opportunity/gap → intervention. For major issues, explain symptoms and impact, data and stakeholder feedback, candidate causes, supporting and contrary evidence, how alternatives were excluded, current judgment, authority boundaries, and validation. For opportunities, specify trend evidence, value hypotheses, and minimal tests rather than inventing incident causes.

| Problem ID | Symptom/opportunity and impact | Cause/value hypothesis | Supporting and contrary evidence | Current judgment and open alternatives | Validation/role |
|---|---|---|---|---|---|

## 2. Trade-offs: decision statements

Compare feasible paths and explain the choice. Use the five technical dimensions where relevant. Identify what is retained, changed, dropped, or deferred.

| Decision ID/goal and problem | Choice and alternatives | Rationale | Dropped/deferred work | Cost and who bears it | Cost of being wrong/reversibility | Stop-loss signal and alternative |
|---|---|---|---|---|---|---|

Expand the most disputed or costly choices: temporary constraints versus principles, resource sensitivity, organizational prerequisites, and long-term correction costs.

## 3. Prioritization: roadmap and capacity checks

State top priorities and ordering rationale, early wins, major challenges, critical dependencies, delay propagation, and why other work is excluded this period.

| Priority/initiative ID | Goal and diagnosis | Value and accepted output | Type | Prerequisite/unlocks | Window/milestone | Effort and scarce skills | Risk and ordering rationale |
|---|---|---|---|---|---|---|---|

| Window/team or scarce role | Capacity and evidence | Prior commitments/support/reserve | Net capacity for this plan | Initiative demand | Conflict and resolution |
|---|---|---|---|---|---|

Provide numbers only with a basis. Distinguish estimates from commitments and use consistent units and periods. Add a textual dependency chain when helpful. Scoring does not resolve capacity conflicts.

## 4. Alignment: commitments, authority, and organizational readiness

Explain value, accountability, and resistance separately for leadership, the team, and adjacent teams. Discuss organizational structure and capability options when useful.

| Stakeholder/accountable role | Benefit/cost borne | Resources/authority/dependent output | What / Why / Standard | Authority and skill gaps | Commitment status and evidence | Disagreement/action/deadline |
|---|---|---|---|---|---|---|

A proposed owner is not an appointment; a requested schedule is not allocated capacity. State which commitments are required to start and what to reduce, replace, defer, or escalate if agreement fails.

## 5. Execution cadence: progression and fallback

| Milestone/batch | Entry conditions and scope | Signals/acceptance and expansion gates | Observation window | Stop conditions and decision role | Rollback/contraction/alternative and recovery objective | Validation/rehearsal status |
|---|---|---|---|---|---|---|

List irreversible decisions, latest decision points, unrecoverable losses, and prerequisites separately. Specify escalation signals, recipients, and options. Non-release initiatives use stage validation and exit strategies rather than invented traffic rollouts.

## 6. Recalibration: indicators, reviews, and replanning triggers

Explain the causal link between outcomes and leading signals and how metrics could mislead or be gamed.

| Goal/assumption | Indicator type or qualitative information | Definition/source | Baseline and target | Threshold/persistence window | Frequency/responsible role | Triggered action | Step to revisit and judgment to reconsider |
|---|---|---|---|---|---|---|---|

Give observable disconfirming signals for major strategic assumptions. If thresholds are unknown, specify how and by whom they will be established rather than “monitor continuously.” Cover execution correction and invalidated judgment: when to change resources/cadence, and when to stop investing and revisit diagnosis, trade-offs, or priorities.

Explain the three review questions, how changes rebalance scope/time/resources, and who decides. Completed milestones do not establish value.

## Closing

- **Near-term actions and open decisions:** action, accountable role, deadline or relative checkpoint, deliverable, and decision blocked. Unknowns include validation methods.
- **Evidence and assumptions:** source locators for key conclusions, unsupported assumptions, source conflicts, and confirmation states.
- For revisions, include a short decision-change log: previous judgment, new evidence, revised decision, affected sections, and commitments needing renewed alignment.

## Acceptance checks

1. Diagnosis separates symptoms from causes; initiatives address the diagnosis. Opportunity investments have testable value hypotheses.
2. Trade-offs identify sacrifices, who bears the cost, and opportunity cost. Priorities respect dependencies, skills, capacity, and portfolio risk.
3. Major initiatives trace to goals, with accountable roles, acceptance criteria, and unresolved commitments. Cross-team costs are visible.
4. The plan identifies when to expand, stop, or exit. Irreversible limits are explicit. Proposed thresholds, commitments, and rehearsal facts remain distinct.
5. Recalibration returns to concrete decisions when value assumptions fail. There is no false precision or unsupported consensus.
6. The six sections form one coherent plan; readers need not derive conclusions from a questionnaire.
