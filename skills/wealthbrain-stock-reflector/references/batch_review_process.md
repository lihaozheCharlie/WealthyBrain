# 批量复盘流程

当用户要求复盘所有历史推荐、查询之前推荐股票现状、检查过去建议收益时，使用本流程。

## 流程

1. 运行或等价执行：
   - `scripts/list_recommendations.py`
   - `scripts/list_recommendations.py --format symbols`
2. 读取 `wiki/90-data/recommendations.csv` 中所有纳入复盘的行。
3. 按股票代码分组，减少重复查询价格和新闻。
4. 对每只股票查询当前价格、复权数据可得性和最新关键新闻。
5. 对每条推荐记录计算收益和基准对比。
6. 给每条记录分类：
   - 盈利
   - 亏损
   - 持平
   - thesis 已失效
   - 尚未验证
   - 数据陈旧 / 需要补数据
7. 创建批量复盘：
   - `wiki/60-reviews/batch/YYYY-MM-DD_ALL_RECOMMENDATIONS_REVIEW.md`
8. 更新索引：
   - `wiki/90-data/recommendations.csv`
   - `wiki/90-data/reviews.csv`
   - `wiki/90-data/batch_reviews.csv`
   - `wiki/90-data/stock_registry.csv`
9. 把跨案例经验写入 `wiki/70-learning/`。

## 批量复盘至少包含

- 复盘的推荐记录数量
- 复盘的唯一股票数量
- 数据日期
- 最大赢家和最大输家
- 陈旧或未验证的想法
- 已失效的 thesis
- 反复出现的检查清单遗漏
- 下一步要验证的规则

除非证据很强且已经考虑反例，不要仅凭一次批量复盘就升级主检查清单。
