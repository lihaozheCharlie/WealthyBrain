# WealthBrain Agent Protocol

本文件是 WealthBrain 目录下所有股票研究任务的全局协议。它只定义工作方式、任务路由和全局约束；具体选股流程写在 `$wealthbrain-stock-picker`，具体复盘反思流程写在 `$wealthbrain-stock-reflector`。

## Skill 路由

- 选股、推荐股票、分析某个股票是否值得关注、判断买入/持有/减仓/卖出、加入观察名单：使用 `$wealthbrain-stock-picker`，读取 `skills/wealthbrain-stock-picker/SKILL.md`。
- 查询之前推荐股票的现状、计算收益、单只或批量复盘、总结历史建议表现、沉淀经验、升级检查清单：使用 `$wealthbrain-stock-reflector`，读取 `skills/wealthbrain-stock-reflector/SKILL.md`。
- 同一任务同时包含“复盘旧建议”和“给出新建议”时，先使用 `$wealthbrain-stock-reflector` 更新历史经验，再使用 `$wealthbrain-stock-picker` 做新决策。

## 全局原则

- 只做研究、记录、复盘和知识沉淀；不要自动下单、连接券商、提交交易或改动真实账户。
- 涉及最新价格、新闻、财报、公告、监管、指数环境、利率、汇率时，必须查询实时或足够新的公开数据，并说明数据日期。
- 输出必须区分事实、数据源、Codex 原生 skill 分析、agent 最终判断和未知项。Codex 原生 skill 的角色视角和派生指标不是独立外部证据。
- 没有足够证据时给出“观察/等待条件”，不要硬凑买点。
- 所有日期使用绝对日期。当前工程冷启日期为 2026-07-07，工作时以实际当前日期为准。
- 每次推荐、复盘、经验沉淀都必须落盘到 `wiki/`，不要只停留在聊天里。
- `wiki/` 中面向人阅读的正文、标题、表格字段和说明统一使用中文；代码、股票代码、CSV 字段名、frontmatter 键名、action/status 枚举值可保留英文以保证工具兼容。
- 不保留旧版兼容占位目录；目录结构按下方最新文件约定执行。

## 本地能力

优先使用本工程冷启选定的三套专业能力：

- `external-skills/tradingagents/SKILL.md`：由当前 Codex 原生执行，不依赖上游源码、外部 LLM API、本地模型或其他智能体。
- `external-skills/daily-stock-analysis/SKILL.md`：由当前 Codex 原生生成日常决策看板，不依赖模型、搜索或行情 API key。
- `external-skills/myhhub-stock/SKILL.md`：由当前 Codex 原生生成量化证据；本地脚本只使用 Python 标准库和已有 OHLCV 数据。

三套能力都由当前 Codex 执行，只提供派生证据或结构化分析视角，不直接替代最终判断。最终判断必须结合当前公开信息和 `wiki/` 中已经沉淀的方法论、复盘经验、检查清单。公开数据不可用时，应缩小分析范围、标记未知项并说明需要的输入，不得转向要求用户提供密钥的外部模型或数据服务。

## 文件约定

- 推荐决策：`wiki/40-recommendations/decisions/YYYY-MM-DD_SYMBOL_DECISION.md`
- 个股档案：`wiki/50-stocks/SYMBOL_NAME.md`
- 单只复盘：`wiki/60-reviews/single/YYYY-MM-DD_SYMBOL_REVIEW.md`
- 批量复盘：`wiki/60-reviews/batch/YYYY-MM-DD_ALL_RECOMMENDATIONS_REVIEW.md`
- 经验沉淀：`wiki/70-learning/`
- 方法论与检查清单：`wiki/20-methodology/`
- 结构化索引：`wiki/90-data/`

股票代码中不要使用路径分隔符；市场后缀可写作 `600519.SH`、`AAPL.US`、`0700.HK`。

## 输出要求

最终回答用户时，先给结论，再给关键证据、风险、记录位置。不要把所有落盘内容全文贴出；只给高信号摘要和文件路径。
