# Picker 落盘契约

每次新的推荐，或当前买入/持有/减仓/卖出/观察/回避判断之后，都必须遵守本契约。

## 必须写入

1. 创建决策文件：
   - `wiki/40-recommendations/decisions/YYYY-MM-DD_SYMBOL_DECISION.md`
   - 使用 `wiki/40-recommendations/decisions/_decision-template.md`
2. 更新或创建个股页：
   - `wiki/50-stocks/SYMBOL_NAME.md`
   - 新股票使用 `wiki/50-stocks/_stock-template.md`
3. 追加或更新 CSV 索引：
   - `wiki/90-data/decisions.csv`
   - `wiki/90-data/recommendations.csv`
   - `wiki/90-data/stock_registry.csv`
   - 记录检查清单时写入 `wiki/90-data/checklist_scores.csv`

## 决策 frontmatter 必填字段

- `id`
- `date`
- `market`
- `symbol`
- `name`
- `action`
- `horizon`
- `conviction`
- `reference_price`
- `currency`
- `benchmark`
- `status`
- `review_due`
- `source_skills`
- `checklist_version`
- `include_in_batch_review`

## 决策正文必填内容

- 结论
- thesis / 投资假设
- 分维度证据
- 计划：入场条件、失效条件、复盘触发、仓位建议
- 检查清单快照
- 认真考虑过但未选择的替代方案
- 带日期的数据来源

## 交接给 Reflector

除非用户明确要求不跟踪，否则设置 `include_in_batch_review=true`。`$wealthbrain-stock-reflector` 依赖这个索引来找到历史推荐。
