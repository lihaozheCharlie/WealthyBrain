# WealthBrain 知识库

这个 wiki 是 agent 的投研记忆系统。它不只保存结论，还保存当时的证据、检查清单、复盘结果、失败原因和逐步升级的方法论。

## 分层结构

| 层级 | 目录 | 用途 |
| --- | --- | --- |
| 系统 | `00-system/` | 架构、字段规范、批量复盘流程、经验沉淀流程 |
| 策略边界 | `10-policy/` | 投资范围、风险边界、仓位规则、组合约束 |
| 方法论 | `20-methodology/` | 投资大师框架、核心检查清单、选股打法、因子库 |
| 研究素材 | `30-research/` | 市场、行业、主题、信息源与研究素材 |
| 推荐记录 | `40-recommendations/` | 每一次推荐/买卖判断的原始决策记录 |
| 个股档案 | `50-stocks/` | 每只股票的长期档案和历史脉络 |
| 复盘 | `60-reviews/` | 单只股票复盘、全量推荐批量复盘 |
| 学习沉淀 | `70-learning/` | 教训、模式、错误库、待验证规则、案例研究 |
| 结构化数据 | `90-data/` | CSV 索引，作为批量检索和统计的事实表 |

## 查询入口

- 全量查询之前推荐的股票：先读 `90-data/recommendations.csv`，再走 `00-system/batch-review-workflow.md`。
- 单只股票复盘：读 `50-stocks/` 个股页和相关 `40-recommendations/decisions/` 决策记录。
- 总结经验：读 `60-reviews/`、`70-learning/` 和 `90-data/`，再更新 `20-methodology/`。
- 推荐新股票：先读 `10-policy/`、`20-methodology/checklists/master-investment-checklist.md`、`70-learning/`，再落盘。

## 技能分工

- 新选股和买卖判断：`skills/wealthbrain-stock-picker/`。
- 历史推荐复盘、收益查询、经验沉淀：`skills/wealthbrain-stock-reflector/`。

## 核心约束

建议必须落盘，复盘必须回写，规律必须有样本支持。检查清单是活的，但每次修改都要能追溯到复盘证据。

## 语言约定

`wiki/` 中面向人阅读的标题、正文、表格字段和说明统一使用中文。为保证脚本和索引兼容，frontmatter 键名、CSV 字段名、股票代码、文件路径、action/status 枚举值、外部工具名可以保留英文。
