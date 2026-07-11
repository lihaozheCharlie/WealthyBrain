# 冷启来源搜索记录

日期：2026-07-07

检索范围：GitHub、SkillsLLM、SkillsMP、Awesome Agent Skills、OpenAI Agent Skills 公开说明。

## 选入主动使用的前三项

| 来源 | 已核验星标 / 分叉数 | 入选原因 |
| --- | ---: | --- |
| `TauricResearch/TradingAgents` | 91,580 / 17,696 | 最热门的多智能体金融交易研究框架，本机已有 skill 和源码，可做多角色辩论与风险约束。 |
| `ZhuLinsen/daily_stock_analysis` | 55,438 / 47,901 | 热门 LLM 多市场股票分析系统，本机已有 `stock_analyzer` skill，适合个股决策看板。 |
| `myhhub/stock` | 13,269 / 2,751 | A 股/ETF 量化系统，覆盖指标、筹码、形态、综合选股、策略回测，本机已有 skill。 |

## 未主动接入但持续观察

| 来源 | 已核验星标数 | 原因 |
| --- | ---: | --- |
| `HKUDS/AI-Trader` | 20,597 | 热度高，但偏全自动交易执行且未检测到明确许可证；暂不纳入主动 skill。 |
| `AI4Finance-Foundation/FinRobot` | 7,498 | 适合生成专业研报；后续可接入为报告层。 |
| `himself65/finance-skills` | 2,957 | 公开 Agent Skills 财务集合；可作为技能市场扩展。 |
| `tradermonty/claude-trading-skills` | 2,287 | 公开交易 skill 集合；可作为技术图表、经济日历扩展。 |
| `quant-sentiment-ai/claude-equity-research` | 630 | 个股研报 plugin，适合后续补充美股研报流程。 |

## 选择原则

- 先选许可证清晰、能在本机被调用、与记录复盘闭环匹配的能力。
- 自动交易执行能力默认不启用。
- 技能市场里的 prompt-only skill 可以借鉴流程，但不能替代实时数据核验。
