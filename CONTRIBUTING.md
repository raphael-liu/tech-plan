# 贡献指南

[简体中文](CONTRIBUTING.md) | [English](CONTRIBUTING.en.md)

## 修改边界

- `SKILL.md` 保留触发范围、核心判断和共用约束；详细输入、输出与来源说明放在 `references/`，避免重复维护。
- 保持诊断、取舍、排序、对齐、节奏、校准的完整链路。改动应改善具体决策行为，不只增加提问数量或文档篇幅。
- 保留用户的目标、授权和格式要求，不把规划建议转化为自动执行权限。
- 使用相对路径，不提交个人路径、真实业务规划、人员信息、密钥或未经授权的资料。示例与回归场景使用虚构数据。
- 引入方法时注明来源和适用边界。不要将第三方资料直接加入项目或默认纳入 MIT 授权。

## 双语维护

- `SKILL.md` 是唯一技能发现入口，`SKILL.en.md` 是按需加载的完整英文工作流。不要创建第二个同名技能或在英文工作流中添加另一份技能 frontmatter。
- 行为变更同时维护中英文工作流和相关参考；使用说明、贡献指南、回归场景也按 `.en.md` 配套。原始来源标题可保留中文，英文说明提供释义，不伪造官方英文名称。
- 六环节统一为 Diagnosis、Trade-offs、Prioritization、Alignment、Execution cadence、Recalibration。区分 leading indicators / lagging indicators、execution deviation / invalidated judgment、proposed / committed / verified。
- 译文不得改变事实、数值、时间窗、单位、取舍代价或承诺程度。语言选择服从上级指令，其次用户明确要求与对话偏好，不能仅根据材料语言决定。
- 校验器只检查配套文件存在及链接有效，不能证明语义等价。涉及语言行为时运行中英互换、混合材料和跨轮切换场景，核对事实与状态是否保持。

## 本地检查

按 README 安装开发依赖后运行：

```bash
python scripts/validate.py
git diff --check
```

修改行为时，在独立会话使用仓库技能执行 `evals/scenarios.md` 的相关场景。区分“结构校验通过”和“行为验证通过”；不要把匹配标题或关键词作为规划质量的证明。

## 提交说明

说明改动解决的问题、行为变化、相关验证结果及尚未验证的边界。行为变更附匿名或虚构输入及观察结果；不要上传包含真实团队信息的模型输出。
