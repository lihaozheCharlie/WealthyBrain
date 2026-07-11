---
name: wealthbrain-tradingagents
description: Use TradingAgents for multi-agent public-market stock, ETF, crypto, or cross-market research memos with fundamental, technical, news, sentiment, bull/bear, trader, and risk-management perspectives.
---

# WealthBrain TradingAgents Wrapper

Use this wrapper when a decision needs multi-perspective debate, especially for US/HK stocks, ETFs, cross-market themes, or high-conviction recommendations.

## Source

- Upstream: `https://github.com/TauricResearch/TradingAgents`
- Local source: `/Users/lihaozhe/.codex/vendor/TradingAgents`
- Checked on: 2026-07-07
- License: Apache-2.0

## Workflow

1. Read the upstream/local README before running commands if setup details are needed.
2. Verify current prices, news, filings, macro context, and model/data credentials before relying on live conclusions.
3. Use the smallest safe command or source-level import first; do not trigger broker/execution integrations.
4. Extract these sections for the WealthBrain decision record:
   - fundamentals analyst view
   - sentiment/news view
   - technical analyst view
   - bull case and bear case
   - trader action
   - risk manager / portfolio manager constraints
5. Save final decision and future review under `wiki/` according to `AGENTS.md`.

## Guardrails

- Treat outputs as research, not personalized financial advice.
- Never place trades or connect accounts.
- If data or API keys are missing, record the limitation and use public data sources where possible.
