# WealthBrain Stock Research System

这是一个给投研 agent 使用的本地知识工程。目标不是自动下单，而是让每一次股票研究、建议、收益跟踪、复盘和策略沉淀都能落盘，逐步形成你自己的选股 skill。

## 目录

- `AGENTS.md`: agent 必须遵守的工作协议。
- `external-skills/`: 冷启选定的公开炒股/股票分析能力索引与本地 wrapper。
- `skills/wealthbrain-stock-picker/`: 选股决策 skill，负责使用 external skills、外部信息和 wiki 知识生成推荐。
- `skills/wealthbrain-stock-reflector/`: 复盘反思 skill，负责查询现价、计算收益、复盘建议、沉淀经验并升级 wiki。
- `wiki/`: 投资政策、方法论、推荐记录、个股档案、复盘和经验库。
- `wiki/90-data/`: 结构化索引表，方便以后统计和复盘。

## 使用方式

以后当你让我推荐股票、判断是否买入/持有/卖出，agent 都应使用 `$wealthbrain-stock-picker`。当你让我查询历史推荐现状、计算收益、复盘或总结经验，agent 都应使用 `$wealthbrain-stock-reflector`。两者都必须把结果写回 `wiki/`。

查询“之前推荐股票的现状”时，agent 应从 `wiki/90-data/recommendations.csv` 找到全部推荐记录，查询现价，生成 `wiki/60-reviews/batch/` 下的批量复盘，并更新收益、状态和经验库。

所有结论都应被视为研究与教育用途，不是个性化投资顾问意见；真实交易前需要你自行判断风险。
