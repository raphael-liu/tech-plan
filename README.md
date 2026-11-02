# tech-plan

[简体中文](README.md) | [English](README.en.md)

面向技术负责人和部门总监的技术规划 Agent Skill。通过多轮访谈、历史技术进展与规划材料，理解现状、目标、约束和取舍，生成可审阅、可执行、可校准的 Markdown 技术规划。

## 规划内容

| 环节 | 核心产出 |
|---|---|
| 诊断 | 战略与机会分析、问题诊断卡、竞争根因与验证动作 |
| 取舍 | 替代方案、明确放弃、机会成本与承担方、止损策略 |
| 排序 | 优先举措、关键依赖、资源核对、阶段路线图 |
| 对齐 | 权责边界、能力缺口、跨团队代价、承诺与待决事项 |
| 节奏 | 进入与放大门槛、观测窗口、中止条件、退路 |
| 校准 | 引领与结果指标、执行与判断偏差、重规划触发器 |

支持年度、季度、专项及架构演进规划，也支持修订既有规划。普通周报合并、单点技术实现和纯排期不属于本技能的主要用途。

## 安装

本仓库根目录就是技能目录，`SKILL.md` 为入口。运行技能不需要 Python、API Key 或专用 MCP；读取输入材料所需的文档工具由使用环境提供。

### Codex

将整个仓库克隆到 Codex 用户技能目录下的 `tech-plan` 文件夹：

```bash
# 将 <REPOSITORY_URL> 替换为发布后的仓库地址。
git clone <REPOSITORY_URL> "${CODEX_HOME:-$HOME/.codex}/skills/tech-plan"
```

如果目标目录已经存在，先检查并备份自己的内容，避免重复克隆或覆盖。自定义安装目录时保留 `references/` 的相对位置。

### 其他支持 Agent Skills 的工具

将仓库放入对应工具的技能发现目录，或按其本地技能加载方式指定本仓库。核心指令不绑定某个文档服务。其他工具的发现和调用方式以其支持能力为准。

## 语言支持

- 支持中文和英文访谈、材料理解与 Markdown 输出。明确指定语言优先，否则跟随对话语言，并遵循使用环境的上级指令。
- 中文材料可以输出英文规划，英文材料也可以输出中文规划；原始数字、单位、日期、技术标识符和来源定位保持一致。
- 中途切换语言时延续已有判断，不重新访谈；仅在要求时生成双语对照。
- [英文工作流](SKILL.en.md)、英文参考资料及 [英文贡献指南](CONTRIBUTING.en.md) 与中文版本配套维护。`SKILL.md` 仍是唯一发现入口。

```text
Use $tech-plan to review these Chinese progress reports.
Ask any necessary follow-up questions in English and write the plan in English.
```

## 使用

从访谈开始：

```text
使用 $tech-plan，帮我规划明年团队技术方向。
先通过多轮交流理解业务目标、现状与约束，再形成 Markdown 规划。
```

结合历史材料：

```text
使用 $tech-plan，阅读我提供的上一年度规划和最近三个季度的技术进展。
区分原计划、已交付和已验证收益，识别变化的假设，形成下一季度规划。
输出到 docs/next-quarter-tech-plan.md。
```

直接形成草案：

```text
使用 $tech-plan，根据这些材料直接成稿，不再追问。
缺失信息标注为假设、待验证或待决事项，不虚构数字、负责人或共识。
```

访谈通常每轮提出 1–3 个关键问题；材料足够时直接成稿。输出保留六个核心章节，并附近期行动、待决事项及关键证据。有关联但未获确认的排期、资源、收益和支持，不会被写成承诺事实。

## 工程结构

```text
tech-plan/
├── SKILL.md                    # Agent 入口与核心工作流
├── SKILL.en.md                 # 完整英文工作流，由入口按需引用
├── README.en.md                # 英文使用说明
├── references/
│   ├── intake.md               # 输入理解与多轮访谈
│   ├── intake.en.md            # 英文参考（同样配套 output、source-notes）
│   ├── output.md               # Markdown 规划内容契约
│   └── source-notes.md         # 方法来源、蒸馏与校勘
├── evals/scenarios.md          # 手动行为回归场景与验收标准
├── scripts/validate.py         # 可独立运行的工程校验
├── .github/workflows/validate.yml
├── CONTRIBUTING.md
├── CONTRIBUTING.en.md
├── requirements-dev.txt
└── LICENSE
```

## 开发与验证

校验环境：Python 3.10+。开发依赖仅用于工程校验，不参与技能运行。

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python scripts/validate.py
git diff --check
```

CI 检查入口、双语文件是否齐全、内部文档链接、个人绝对路径以及意外加入的二进制资料；存在可选界面元数据时也会检查。结构检查不能证明翻译语义或规划质量；修改核心行为后，应按 [行为回归场景](evals/scenarios.md) 在独立会话中验证。

维护约定见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 来源与许可

方法由两份技术管理课程资料蒸馏，并增加适用于 Agent 的输入理解、访谈、证据管理和输出工作流。来源映射及指标示例校勘见 [source-notes.md](references/source-notes.md)。仓库不附原课程 PDF、扫描件或完整转录。

本项目原创贡献采用 [MIT License](LICENSE)。第三方课程资料的权利保留于原权利人，不属于本仓库的授权范围。
