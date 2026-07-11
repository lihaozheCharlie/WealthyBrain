# 决策与复盘字段规范

## 决策记录

必填 frontmatter 字段：

- `id`: `DEC-YYYYMMDD-SYMBOL-NNN`
- `date`: 决策日期。
- `market`: `A股`、`港股`、`美股`、`ETF`、`crypto` 等。
- `symbol`: 股票代码。
- `name`: 股票名称。
- `action`: `watch`、`buy-candidate`、`hold`、`reduce`、`sell-candidate`、`avoid`。
- `horizon`: `days`、`weeks`、`months`、`years`。
- `conviction`: `low`、`medium`、`high`。
- `reference_price`: 决策参考价。
- `currency`: `CNY`、`HKD`、`USD` 等。
- `benchmark`: 复盘基准。
- `status`: `open`、`closed`、`reviewed`。
- `review_due`: 计划复盘日期或触发条件。
- `source_skills`: 使用过的 skill。
- `checklist_version`: 使用的检查清单版本。
- `include_in_batch_review`: 是否纳入全量推荐复盘。

正文必须包含：

- 一句话结论。
- 投资假设。
- 证据。
- 风险。
- 入场条件、失效条件、复盘触发。
- 仓位建议。
- 数据来源。
- 检查清单快照。
- 考虑过但未选择的替代方案。

## 复盘记录

必填 frontmatter 字段：

- `id`: `REV-YYYYMMDD-SYMBOL-DECISIONID`
- `date`: 复盘日期。
- `decision_id`: 对应决策。
- `symbol`: 股票代码。
- `review_price`: 复盘价格。
- `simple_return_pct`: 简单收益率。
- `benchmark`: 基准。
- `benchmark_return_pct`: 基准收益率。
- `excess_return_pct`: 相对基准超额收益。
- `outcome`: `win`、`loss`、`flat`、`invalidated`、`inconclusive`。

正文必须包含：

- 结果摘要。
- 收益计算。
- 投资假设命中情况。
- 错误/正确原因。
- 可沉淀经验。

## 文件路径

- 决策记录：`wiki/40-recommendations/decisions/YYYY-MM-DD_SYMBOL_DECISION.md`
- 个股档案：`wiki/50-stocks/SYMBOL_NAME.md`
- 单只复盘：`wiki/60-reviews/single/YYYY-MM-DD_SYMBOL_REVIEW.md`
- 批量复盘：`wiki/60-reviews/batch/YYYY-MM-DD_ALL_RECOMMENDATIONS_REVIEW.md`

## CSV 事实表

- 全量推荐：`wiki/90-data/recommendations.csv`
- 决策日志：`wiki/90-data/decisions.csv`
- 复盘日志：`wiki/90-data/reviews.csv`
- 批量复盘运行记录：`wiki/90-data/batch_reviews.csv`
- 个股注册表：`wiki/90-data/stock_registry.csv`
- 检查清单评分：`wiki/90-data/checklist_scores.csv`
