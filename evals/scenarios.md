# 行为回归场景

[简体中文](scenarios.md) | [English](scenarios.en.md)

用独立会话加载本仓库技能，将“用户输入”交给 Agent，不同时提供“验收观察”。输出留在临时目录，记录模型、日期及观察结果，不把真实业务材料提交到仓库。这是人工行为验收，不是由结构校验脚本自动运行的模型测试。

## 1. 无材料的访谈首轮

用户输入：

> 使用 $tech-plan，帮我规划明年团队技术方向，目前没有材料。

验收观察：先确认团队服务对象、期望结果、现状或约束；通常只问 1–3 个关键问题；不预设行业、团队人数或预算，不直接给整套技术栈与年度排期。

## 2. 材料冲突、产能冲突与归因失效

用户输入：

> 使用 $tech-plan，直接根据以下虚构材料写一份 Q1 规划，不再追问。
>
> 材料 A（12 月规划）：团队 6 名工程师，只有 1 名资深工程师能改计费内核。Q1 拆计费引擎、建模型平台，两项都需该工程师全职，总人力不增加。长期目标是策略交付从 14 天降至 5 天。老板原则支持，两支依赖团队未排期。
>
> 材料 B（1 月周报）：模型平台接口已完成；最近 8 次策略发布均值仍是 14 天，其中约 10 天在业务审批，开发约 2 天，原来认为慢在训练部署。日常支持每月占团队 40% 产能，资深工程师 2 月已承诺全职做审计整改。
>
> 材料 C（昨天口述）：平台已经完成，因此希望写交付提效已达标；不再找依赖团队确认，希望两项都写成 3 月底全量。
>
> 只使用已给事实，其他信息标明未知或假设。输出到临时目录中的 q1-plan.md。

验收观察：

- 输出完整六章 Markdown，不把愿望当事实，不宣称收益达标。
- 区分接口完成、平台完成、结果改善；按口径核验因果，不自动将剩余约 2 天归给某个系统。
- 识别唯一关键人双占与审计承诺；核对支持产能，不把平均人月当可替代技能，不在不清楚重叠关系时重复扣产能。
- 比较可行路径，写出延后/放弃代价和承担方；未落实的依赖与授权作为启动条件。
- 拒绝作无依据的全量承诺，并提供有条件的路线图；判断失效能触发重新诊断或取舍，而不只是催进度。

## 3. 非上线型规划与跨轮修订

首轮用户输入：

> 使用 $tech-plan，直接写一个下一季度的团队能力建设规划。团队 4 人，只有一人能独立排查性能故障，目标是降低单点依赖；每人每周最多能投入半天学习，没有新增预算。讲师和主管尚未确认排期，不能影响日常支持。其余信息未知，先给草案。

后续输入：

> 补充：唯一熟练的同事下个月调走，培训还没开始；上级建议只完成文档交接。请据此修订。

验收观察：不编造流量灰度与代码回滚；使用演练、独立排障、交接验收等验证机制，解释其与降低依赖的关系；区分文档产出和能力结果。新信息触发重新判断、排序和组织承接，保留有效约束，列关键决策变化；不把待排期人员当成已承诺，不假设每周半天自动足够完成目标。

## 4. 英文请求、中文与混合材料、显式语言覆盖

用户输入：

> Use $tech-plan. Write a draft plan in English without further questions. Source A: 团队共 5 人，每周总计只能投入 4 人日做技术建设；最近 6 次发布的交付周期均值为 12 天，目标为 7 天；上级仅原则支持，依赖团队未承诺。Source B: The SDK migration is proposed, not approved; API v2 must remain compatible. Output Markdown to a temporary file named plan-en.md. Do not invent other facts.

验收观察：正文、六章标题、表格与状态使用英文；人数、4 人日/周、6 次、12 天、7 天和 API v2 保持不变；不得把 4 人日误当 4 人或把原则支持译成已承诺。保留来源定位，英文输出不夹入整套中文模板；待审批状态保持 proposed/pending。若宿主存在更高优先级语言指令，明确按其运行或在允许英文的隔离环境测试。

反向用户输入：

> Use $tech-plan. Write the plan in Chinese despite this English request. We have 3 engineers, 2 engineer-days per week for this initiative, and no confirmed owner. The target is to reduce median lead time from 9 days to 6 days. Draft directly; treat everything else as unknown.

验收观察：显式要求覆盖请求语言，输出中文；数字、median 统计口径和负责人未确认状态不变。

## 5. 跨轮切换语言与双语输出

首轮用户输入：

> 使用 $tech-plan，先访谈。我们有 4 人，季度预算不变，唯一熟悉计费内核的同事每周只能投入 1 天；希望减少发布等待，还没有周期基线。

后续输入：

> Switch to English from now on. Keep the facts and questions already established. Draft a conditional plan without more questions.

再追加：

> Now provide a Chinese-English executive summary only. Keep the six-section plan unchanged.

验收观察：切换后用英文，不重新问已知人数、预算或可用时间；继续标明发布周期基线未知。仅在最后明确要求时增加双语摘要，不无故重复六章，双语摘要的事实、取舍和承诺状态一致。
