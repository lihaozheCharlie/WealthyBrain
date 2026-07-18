# External Skills

冷启日期：2026-07-07。

本目录不是盲目复制大型仓库，而是把公开热门能力整理成本工程可调用、可审计的 Codex 原生 skill wrapper。上游仓库只提供方法论参考，不作为运行依赖。热度与许可证通过 GitHub API 和公开技能目录检索核对。

## Active Top 3

| Rank | Source | Stars checked | License | Role in WealthBrain |
| --- | --- | ---: | --- | --- |
| 1 | `TauricResearch/TradingAgents` | 91,580 | Apache-2.0 | 多智能体投研辩论与风险视角 |
| 2 | `ZhuLinsen/daily_stock_analysis` | 55,438 | MIT | 个股决策看板、新闻、情绪、仓位建议 |
| 3 | `myhhub/stock` | 13,269 | Apache-2.0 | A 股/ETF 指标、筹码、策略筛选、回测 |

## Watchlist

- `HKUDS/AI-Trader`: 2026-07-07 检查为 20,597 stars，热度高，但偏自动交易执行且 GitHub API 未返回明确许可证。本工程暂不把它列为主动执行 skill，只作为观察对象。
- `AI4Finance-Foundation/FinRobot`: 7,498 stars，适合专业报告和金融分析平台，可在未来需要更完整研报时接入。
- `himself65/finance-skills`: 2,957 stars，Agent Skills open standard 财务技能集合，可作为后续扩展来源。
- `tradermonty/claude-trading-skills`: 2,287 stars，交易/图表/日历/screener skill 集合，可作为后续扩展来源。

## Local Wrappers

- `tradingagents/SKILL.md`
- `daily-stock-analysis/SKILL.md`
- `myhhub-stock/SKILL.md`

这些 wrapper 负责告诉未来 Codex 何时使用对应能力、如何用当前公开信息和本地计算执行，以及如何把输出映射到 `wiki/`。

Active Top 3 均已改为 Codex 原生执行：

- `tradingagents`：当前 Codex 顺序执行多视角分析与多空辩论。
- `daily-stock-analysis`：当前 Codex 生成日常决策看板、事件摘要和市场复盘。
- `myhhub-stock`：当前 Codex 组织量化证据，并可用纯 Python 标准库脚本计算已有 OHLCV 数据。

三者都不需要本地上游源码、外部 LLM API key、本地模型服务或其他智能体。公开数据缺失时标记未知，不以收费 API 补洞。
