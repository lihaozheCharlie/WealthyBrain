# 决策流程

只在“新的推荐”或“当前买入/持有/减仓/卖出/观察/回避判断”中使用本流程。历史推荐复盘请使用 `$wealthbrain-stock-reflector`。

## 推荐流程

1. 明确用户请求：市场、股票代码或股票池、投资周期、用户提到的风险偏好，以及这是筛选任务还是单只股票判断。
2. 读取本地记忆：
   - `wiki/10-policy/investment-policy.md`
   - `wiki/10-policy/risk-and-position-sizing.md`
   - `wiki/20-methodology/checklists/master-investment-checklist.md`
   - `wiki/20-methodology/playbooks/selection-playbook.md`
   - `wiki/20-methodology/factor-library.md`
   - `wiki/70-learning/lessons/lessons-log.md`
   - 如已存在，读取 `wiki/50-stocks/` 下对应个股页
3. 核对当前数据：
   - 最新价格和日期
   - 指数与行业环境
   - 近期公告、新闻、财报
   - 能查到时补充财务和估值背景
4. 选择工具：
   - A 股/ETF：优先 `myhhub-stock` + `daily-stock-analysis`
   - 美股/港股/跨市场：优先 `tradingagents` + 实时公开信息核验
   - 高置信度或复杂判断：组合多个外部能力
   - external-skill 输出只是证据，不是最终权威；如果互相冲突，必须在决策记录里说明如何处理
5. 定性评估证据：
   - 市场环境
   - 流动性
   - 趋势与量价
   - 基本面
   - 估值
   - 催化剂
   - 情绪与新闻
   - 风险
6. 给出研究动作：
   - `buy-candidate`
   - `watch`
   - `hold`
   - `reduce`
   - `sell-candidate`
   - `avoid`
7. 落盘：
   - 创建决策 markdown
   - 更新个股档案 markdown
   - 追加或更新 `decisions.csv`、`recommendations.csv`、`stock_registry.csv`
   - 使用检查清单时追加 `checklist_scores.csv`
   - 具体要求见 `references/persistence_contract.md`

## 面向用户的回答格式

最终回答应包含：

- 结论先行
- 当前数据日期
- 3-6 条关键证据
- 失效条件
- 复盘触发条件
- 已写入的 wiki 文件路径

除非用户询问，不要展开解释工具内部细节。
