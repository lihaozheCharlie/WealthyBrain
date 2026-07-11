# Reflector Wiki Schema

## 输入

- `wiki/90-data/recommendations.csv`
- `wiki/90-data/decisions.csv`
- `wiki/40-recommendations/decisions/*.md`
- `wiki/50-stocks/*.md`

## 复盘输出

- 单只复盘：`wiki/60-reviews/single/YYYY-MM-DD_SYMBOL_REVIEW.md`
- 批量复盘：`wiki/60-reviews/batch/YYYY-MM-DD_ALL_RECOMMENDATIONS_REVIEW.md`
- 复盘索引：`wiki/90-data/reviews.csv`
- 批量复盘索引：`wiki/90-data/batch_reviews.csv`

## 学习输出

- 经验日志：`wiki/70-learning/lessons/lessons-log.md`
- 经验索引：`wiki/90-data/lessons.csv`
- 模式：`wiki/70-learning/patterns/`
- 错误：`wiki/70-learning/mistakes/`
- 待验证规则：`wiki/70-learning/rules-under-test/`
- 规则索引：`wiki/90-data/rules.csv`

## 收益计算

简单收益：

`(review_price - reference_price + dividends - fees) / reference_price * 100`

超额收益：

`stock_return_pct - benchmark_return_pct`

可靠复权价格可用时，使用复权价格序列。不可用时，明确标注为未复权简单收益。

## CSV 字段

推荐记录：

`rec_id,decision_id,date,market,symbol,name,action,horizon,conviction,reference_price,currency,benchmark,review_due,status,include_in_batch_review,last_price,last_price_date,simple_return_pct,benchmark_return_pct,excess_return_pct,review_count,decision_file,stock_file,source_skills`

复盘记录：

`id,date,review_type,batch_id,decision_id,rec_id,symbol,name,review_price,currency,simple_return_pct,benchmark,benchmark_return_pct,excess_return_pct,outcome,review_file`

批量复盘：

`batch_id,date,scope,recommendations_reviewed,symbols_reviewed,winners,losers,flat,invalidated,batch_file,data_source_date`
