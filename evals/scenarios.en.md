# Behavioral evaluation scenarios

[简体中文](scenarios.md) | [English](scenarios.en.md)

Load this repository's skill in an independent conversation. Give the agent only the user input, not the acceptance observations. Save outputs in temporary directories and record the model, date, and observations. Never commit real business information. These are manual behavioral evaluations, not model tests run by the structural validator.

## 1. First interview turn without documents

User input:

> Use $tech-plan to plan our team's technical direction for next year. I have no documents yet.

Acceptance observations: ask about beneficiaries, outcomes, current conditions, or constraints, usually with only 1–3 important questions. Do not assume industry, headcount, or budget, or immediately prescribe a technology stack and annual schedule.

## 2. Conflicting evidence, capacity conflicts, and invalidated attribution

User input:

> Use $tech-plan to write a Q1 plan directly from these fictional sources without further questions.
>
> Source A (December plan): Six engineers, only one senior engineer capable of changing the billing core. Q1 includes splitting the billing engine and building a model platform; each needs that engineer full time, with no headcount increase. The long-term goal is to reduce policy delivery from 14 days to 5 days. Leadership supports it in principle. Two dependent teams have not scheduled work.
>
> Source B (January progress): Model platform interfaces are complete. The last eight policy releases still average 14 days, with about 10 days in business approval and about 2 in development. The original attribution was slow training/deployment. Support consumes 40% of monthly team capacity. The senior engineer has already committed full time in February to audit remediation.
>
> Source C (yesterday's statement): Since the platform is complete, we would like to report the delivery improvement as achieved. Skip further dependency confirmation and schedule both full rollouts by the end of March.
>
> Use only supplied facts; label other information unknown or assumed. Write q1-plan.md in a temporary directory.

Acceptance observations:

- Deliver six Markdown sections without treating wishes as facts or claiming the target was achieved.
- Separate interface completion, platform completion, and outcomes. Verify measurement definitions; do not automatically attribute the remaining two days to a particular system.
- Detect the scarce specialist's conflicting commitments and audit work. Check support capacity without treating average person-months as interchangeable skills or double-subtracting overlapping work.
- Compare feasible paths and name the costs of delay or sacrifice and who bears them. Unconfirmed dependencies and authority become prerequisites.
- Avoid unsupported rollout promises and provide a conditional roadmap. Invalidated assumptions trigger diagnosis or trade-offs rather than only delivery pressure.

## 3. Capability planning and revision across turns

First user input:

> Use $tech-plan to draft next quarter's team capability plan directly. We have four people; only one can independently diagnose performance incidents. We want to reduce that dependency. Each person can spend at most half a day per week learning, with no new budget. Trainer and manager schedules are unconfirmed, and daily support must not be affected. Treat everything else as unknown.

Follow-up:

> The only experienced colleague will transfer next month, and training has not started. Leadership suggests documentation-only handover. Revise the plan.

Acceptance observations: use drills, independent diagnosis, and handover acceptance rather than invented traffic rollouts or code rollback. Explain how these verify reduced dependency. Distinguish documentation from capabilities. New evidence revises diagnosis, priorities, and organizational readiness while preserving valid constraints and showing decision changes. Do not treat unconfirmed schedules as commitments or assume half a day per week is sufficient.

## 4. English requests, mixed-language evidence, and explicit overrides

User input:

> Use $tech-plan. Write a draft plan in English without further questions. Source A: 团队共 5 人，每周总计只能投入 4 人日做技术建设；最近 6 次发布的交付周期均值为 12 天，目标为 7 天；上级仅原则支持，依赖团队未承诺。Source B: The SDK migration is proposed, not approved; API v2 must remain compatible. Output Markdown to a temporary file named plan-en.md. Do not invent other facts.

Acceptance observations: prose, headings, tables, and statuses are English. Preserve five people, four engineer-days per week, six releases, twelve days, seven days, and API v2. Do not turn four engineer-days into four engineers or support in principle into commitment. Retain source locators; do not paste a Chinese output template into the English plan. Migration remains proposed/pending. If host language instructions take precedence, respect them or use an isolated environment allowing English for this test.

Reverse user input:

> Use $tech-plan. Write the plan in Chinese despite this English request. We have 3 engineers, 2 engineer-days per week for this initiative, and no confirmed owner. The target is to reduce median lead time from 9 days to 6 days. Draft directly; treat everything else as unknown.

Acceptance observations: the explicit output language overrides request language. Output is Chinese, with the same numbers, median definition, and unconfirmed ownership.

## 5. Language switching and requested bilingual output

First user input:

> 使用 $tech-plan，先访谈。我们有 4 人，季度预算不变，唯一熟悉计费内核的同事每周只能投入 1 天；希望减少发布等待，还没有周期基线。

Follow-up:

> Switch to English from now on. Keep the facts and questions already established. Draft a conditional plan without more questions.

Then:

> Now provide a Chinese-English executive summary only. Keep the six-section plan unchanged.

Acceptance observations: switch to English without asking again for headcount, budget, or availability. The lead-time baseline remains unknown. Produce a bilingual summary only when explicitly requested at the last turn, without unnecessarily repeating the plan. Both summaries preserve facts, choices, and commitment states.
