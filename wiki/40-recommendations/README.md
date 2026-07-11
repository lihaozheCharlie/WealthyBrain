# 推荐记录

本层是决策日志。每次类似推荐的回答都必须在 `decisions/` 创建文件，并追加更新 `wiki/90-data/` 中的索引。

## 事实来源

- 面向人阅读的决策文件：`decisions/YYYY-MM-DD_SYMBOL_DECISION.md`
- 机器可读索引：`../90-data/recommendations.csv`

## 哪些内容算推荐

以下内容都要记录：

- 推荐买入候选
- 加入观察名单
- 持有/减仓/卖出判断
- 用户询问某只股票时给出的明确回避结论

如果用户之后询问“之前推荐股票”，使用 `recommendations.csv`，不要依赖记忆。
