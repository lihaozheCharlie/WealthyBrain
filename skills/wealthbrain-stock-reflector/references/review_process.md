# 单只复盘流程

用于复盘单条历史推荐，或某只股票的历史决策。

## 流程

1. 从以下来源确定目标决策或股票：
   - 用户请求
   - `wiki/90-data/recommendations.csv`
   - `wiki/90-data/decisions.csv`
   - `wiki/40-recommendations/decisions/` 中的相关文件
2. 读取原始决策文件和个股页。
3. 查询当前价格、数据日期、公司行为、近期关键新闻。
4. 计算：
   - 简单收益
   - 能计算时补充复权收益
   - 基准收益
   - 超额收益
   - 跟踪天数
5. 评估原始 thesis：
   - 哪些按预期发生
   - 哪些失败
   - 哪些仍未验证
   - 是否触发失效条件或复盘条件
6. 做结果归因：
   - 市场 beta
   - 行业波动
   - 个股催化
   - 估值变化
   - 买入/推荐时点
   - 运气或数据缺口
7. 创建复盘文件：
   - `wiki/60-reviews/single/YYYY-MM-DD_SYMBOL_REVIEW.md`
8. 更新：
   - `wiki/90-data/reviews.csv`
   - `wiki/90-data/recommendations.csv`
   - 相关 `wiki/50-stocks/` 个股页
   - 如果确实有经验，更新 `wiki/70-learning/lessons/lessons-log.md`

## 复盘判断

把过程和结果分开判断：

- 好过程 / 好结果
- 好过程 / 坏结果
- 坏过程 / 好结果
- 坏过程 / 坏结果

即使赚钱，只要过程有问题，也要进入错误库或待验证规则流水线。
