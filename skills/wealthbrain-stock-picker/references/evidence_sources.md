# 证据来源

每次选股决策都使用三层证据：external-skills、当前公开信息、WealthBrain wiki 记忆。

## 外部技能

把 external-skills 当作专门分析师使用：

- `external-skills/myhhub-stock/SKILL.md`：A 股/ETF 指标、筹码分布、K 线形态、策略筛选和回测。
- `external-skills/daily-stock-analysis/SKILL.md`：个股看板、新闻/情绪、操作建议、作战计划、市场复盘。
- `external-skills/tradingagents/SKILL.md`：多智能体基本面、技术面、新闻、情绪、多空辩论、交易员和风险视角。

external-skill 的输出不是最终答案，只是分析证据。若不同来源冲突，必须在决策文件中说明冲突和取舍。

## 当前公开信息

决策前必须核验当前事实：

- 最新价格和日期
- 指数与行业环境
- 近期公告、财报、新闻
- 估值和财务指标
- 流动性与交易约束
- 相关公司行为

如果当前数据缺失，降低置信度，或使用 `watch` / `avoid`。

## Wiki 记忆

形成判断前读取本地记忆：

- `wiki/10-policy/` 中的投资政策和仓位规则
- `wiki/20-methodology/` 中的主检查清单和选股 playbook
- `wiki/70-learning/` 中的历史教训、错误模式、待验证规则
- 如存在，读取 `wiki/50-stocks/` 中的个股页
- 如果该股票曾被讨论过，读取 `wiki/90-data/recommendations.csv` 中的历史推荐记录

## 综合顺序

1. 判断是否符合投资政策。
2. 判断业务或交易是否在当前能力圈内。
3. 收集当前公开事实。
4. 运行或检查相关 external-skill 分析。
5. 套用主检查清单，并记录通过、失败、未知项。
6. 对照历史教训和待验证规则。
7. 决定动作和置信度。
8. 落盘，为未来反思保留证据。

## 冲突处理

证据冲突时：

- 已核验的当前事实优先于模型评论。
- 原始公告/财报优先于摘要。
- external-skill 分歧本身就是风险信号。
- 核心检查项未知时降低置信度。
- 说明需要什么数据才能解决分歧。
