---
name: wealthbrain-myhhub-stock
description: Use myhhub/stock InStock for A-share and ETF indicators, chip distribution, K-line pattern recognition, comprehensive stock screening, strategy screening, and backtests.
---

# WealthBrain myhhub/stock Wrapper

Use this wrapper for A 股 and ETF quantitative evidence: indicators, patterns, strategy screens, chip distribution, and backtesting.

## Source

- Upstream: `https://github.com/myhhub/stock`
- Local source: `/Users/lihaozhe/.codex/vendor/myhhub-stock`
- Local Codex skill: `/Users/lihaozhe/.codex/skills/myhhub_stock/SKILL.md`
- Checked on: 2026-07-07
- License: Apache-2.0

## Best Fit

- A 股/ETF 综合选股
- 技术指标：MACD、KDJ、BOLL、RSI、CCI、ATR、OBV、SAR、Supertrend
- 筹码分布/持仓成本
- K 线形态识别
- 策略筛选和回测

## Workflow

1. Read config/database assumptions before running jobs that write data.
2. Prefer narrow single-stock or single-strategy checks before full-market jobs.
3. For recommendations, export only the relevant evidence into `wiki/40-recommendations/decisions/`.
4. For reviews, compare original screened signal with later price behavior and record whether the signal decayed, persisted, or inverted.

## Guardrails

- Do not start auto-trading services.
- Do not run long full-market jobs unless the user asks for them or the local environment is clearly prepared.
