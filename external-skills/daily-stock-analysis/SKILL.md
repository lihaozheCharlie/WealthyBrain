---
name: wealthbrain-daily-stock-analysis
description: Use daily_stock_analysis / stock_analyzer for multi-market stock dashboards, real-time news, sentiment scoring, operation advice, position suggestions, and market reviews.
---

# WealthBrain Daily Stock Analysis Wrapper

Use this wrapper for fast stock-level dashboards, news/sentiment checks, operation advice, and market review.

## Source

- Upstream: `https://github.com/ZhuLinsen/daily_stock_analysis`
- Local source: `/Users/lihaozhe/.codex/vendor/daily_stock_analysis`
- Local Codex skill: `/Users/lihaozhe/.codex/skills/stock_analyzer/SKILL.md`
- Checked on: 2026-07-07
- License: MIT

## Capabilities To Reuse

- `analyze_stock(stock_code)`
- `analyze_stocks(stock_codes)`
- `perform_market_review()`

Key output areas to map into WealthBrain:

- core conclusion
- trend and price position
- volume and chip/cost structure
- news risks and positive catalysts
- battle plan: entry/exit targets, position strategy, risk checklist

## Workflow

1. Inspect config and data-source readiness before running.
2. Run narrow single-stock analysis before broad batch analysis.
3. Cross-check important price/news facts with live sources.
4. Save conclusions in the decision template; do not leave analysis only in chat.

## Guardrails

- Do not send notifications or scheduled pushes unless explicitly requested.
- Do not treat a single model score as sufficient evidence for a buy decision.
