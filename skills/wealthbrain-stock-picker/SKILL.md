---
name: wealthbrain-stock-picker
description: "用于 WealthBrain 的选股和推荐决策：筛选股票、分析单只股票或股票池、给出买入/持有/减仓/卖出/观察/回避等研究建议，并结合 external-skills、实时公开信息和本地 wiki 知识记录决策。不要用于复盘历史推荐或计算收益；这些任务使用 wealthbrain-stock-reflector。"
---

# WealthBrain Stock Picker

这个 skill 负责“做新的选股决策”。它把 external-skills、当前公开信息和 WealthBrain wiki 记忆合在一起，形成可复盘、可追踪的推荐记录。

## 必读文件

- `AGENTS.md`
- `wiki/00-system/wiki-architecture.md`
- `wiki/10-policy/investment-policy.md`
- `wiki/20-methodology/checklists/master-investment-checklist.md`
- `wiki/20-methodology/playbooks/selection-playbook.md`
- `wiki/20-methodology/factor-library.md`
- `wiki/70-learning/lessons/lessons-log.md`

## 任务路由

- 推荐股票、分析股票池、判断买入/持有/减仓/卖出/观察/回避：读取 `references/decision_process.md`。
- 选择证据来源、综合 external-skills/公开信息/wiki 经验：读取 `references/evidence_sources.md`。
- 落盘推荐记录和更新索引：读取 `references/persistence_contract.md`。
- 如果用户要求复盘历史推荐、计算收益、查询所有之前推荐、总结经验，停止使用本 skill，改用 `$wealthbrain-stock-reflector`。

## 外部能力

按需使用这些本地 wrapper：

- `external-skills/tradingagents/SKILL.md`
- `external-skills/daily-stock-analysis/SKILL.md`
- `external-skills/myhhub-stock/SKILL.md`

## 输出约束

每次推荐都必须创建或更新 wiki 记录。不要下单，不要连接券商，不要把研究结论包装成个性化投资顾问意见。

所有输出都是研究和教育用途，不是自动交易指令。
