---
name: wealthbrain-stock-reflector
description: "用于 WealthBrain 的复盘、反思和学习：复盘历史股票推荐、查询当前价格、计算简单或复权收益、比较基准、生成单只或批量复盘、更新推荐索引、把经验和规则写入 wiki，并改进选股检查清单。不要用于新的股票推荐；新推荐使用 wealthbrain-stock-picker。"
---

# WealthBrain Stock Reflector

## 概览

这个 skill 负责复盘 WealthBrain 之前的选股决策，并把结果转化为更好的投资知识。它负责查价格与状态、计算收益、生成复盘、提取经验、升级方法论。

## 必读文件

- `AGENTS.md`
- `wiki/00-system/batch-review-workflow.md`
- `wiki/00-system/experience-distillation-workflow.md`
- `wiki/00-system/wiki-architecture.md`
- `wiki/20-methodology/checklists/review-checklist.md`
- `wiki/20-methodology/checklists/master-investment-checklist.md`
- `wiki/90-data/recommendations.csv`

## 任务路由

- 复盘单条历史推荐：读取 `references/review_process.md`。
- 批量复盘所有历史推荐：读取 `references/batch_review_process.md`。
- 经验沉淀或检查清单升级：读取 `references/learning_pipeline.md`。
- 更新 CSV / 索引：读取 `references/wiki_schema.md`。

## 脚本

- `scripts/list_recommendations.py`：从 `wiki/90-data/recommendations.csv` 列出全部推荐记录或唯一股票代码。
- `scripts/return_calc.py`：根据参考价、现价、分红和费用计算简单收益率。

## 数据规则

- 复盘时必须用实时或足够新的公开数据核验当前价格和数据日期。
- 如果能获得可靠的拆股/分红复权数据，优先使用复权收益。
- 如果只能获得未复权价格，必须在复盘中说明这是未复权简单收益。
- 每条推荐都要对比 `recommendations.csv` 中记录的基准；没有基准时选择并说明默认基准。

## 输出约束

每次复盘都必须更新 wiki 状态。反思不只是报告结果；只要证据支持，就要改进未来选股流程。
