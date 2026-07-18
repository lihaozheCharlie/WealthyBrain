#!/usr/bin/env python3
"""Compute keyless OHLCV evidence with the Python standard library."""

from __future__ import annotations

import argparse
import csv
import json
import math
import statistics
from pathlib import Path
from typing import Any, Dict, List, Optional


REQUIRED_COLUMNS = ("date", "open", "high", "low", "close", "volume")


def parse_number(value: str) -> float:
    return float(value.strip().replace(",", ""))


def load_rows(path: Path) -> List[Dict[str, Any]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames:
            raise ValueError("CSV has no header")
        normalized = {name.strip().lower(): name for name in reader.fieldnames}
        missing = [name for name in REQUIRED_COLUMNS if name not in normalized]
        if missing:
            raise ValueError(f"missing columns: {', '.join(missing)}")

        by_date: Dict[str, Dict[str, Any]] = {}
        for line_number, raw in enumerate(reader, start=2):
            date = (raw.get(normalized["date"]) or "").strip()
            if not date:
                raise ValueError(f"line {line_number}: empty date")
            try:
                row = {"date": date}
                for key in REQUIRED_COLUMNS[1:]:
                    row[key] = parse_number(raw.get(normalized[key]) or "")
            except ValueError as exc:
                raise ValueError(f"line {line_number}: invalid numeric value") from exc

            if min(row["open"], row["high"], row["low"], row["close"]) <= 0:
                raise ValueError(f"line {line_number}: prices must be positive")
            if row["volume"] < 0:
                raise ValueError(f"line {line_number}: volume must be non-negative")
            if row["high"] < max(row["open"], row["low"], row["close"]):
                raise ValueError(f"line {line_number}: high is inconsistent with OHLC")
            if row["low"] > min(row["open"], row["high"], row["close"]):
                raise ValueError(f"line {line_number}: low is inconsistent with OHLC")
            if date in by_date:
                raise ValueError(f"line {line_number}: duplicate date {date}")
            by_date[date] = row

    rows = [by_date[date] for date in sorted(by_date)]
    if len(rows) < 2:
        raise ValueError("at least two valid rows are required")
    return rows


def sma(values: List[float], period: int, end: Optional[int] = None) -> Optional[float]:
    end = len(values) if end is None else end
    if end < period:
        return None
    return sum(values[end - period : end]) / period


def ema_series(values: List[float], period: int) -> List[float]:
    alpha = 2.0 / (period + 1.0)
    result = [values[0]]
    for value in values[1:]:
        result.append(alpha * value + (1.0 - alpha) * result[-1])
    return result


def rsi_wilder(values: List[float], period: int = 14) -> Optional[float]:
    if len(values) <= period:
        return None
    gains: List[float] = []
    losses: List[float] = []
    for current, previous in zip(values[1:], values[:-1]):
        change = current - previous
        gains.append(max(change, 0.0))
        losses.append(max(-change, 0.0))
    avg_gain = sum(gains[:period]) / period
    avg_loss = sum(losses[:period]) / period
    for gain, loss in zip(gains[period:], losses[period:]):
        avg_gain = ((period - 1) * avg_gain + gain) / period
        avg_loss = ((period - 1) * avg_loss + loss) / period
    if avg_loss == 0:
        return 100.0 if avg_gain > 0 else 50.0
    rs = avg_gain / avg_loss
    return 100.0 - 100.0 / (1.0 + rs)


def atr_wilder(rows: List[Dict[str, Any]], period: int = 14) -> Optional[float]:
    true_ranges: List[float] = []
    for index, row in enumerate(rows):
        if index == 0:
            true_ranges.append(row["high"] - row["low"])
        else:
            previous_close = rows[index - 1]["close"]
            true_ranges.append(
                max(
                    row["high"] - row["low"],
                    abs(row["high"] - previous_close),
                    abs(row["low"] - previous_close),
                )
            )
    if len(true_ranges) < period:
        return None
    value = sum(true_ranges[:period]) / period
    for item in true_ranges[period:]:
        value = ((period - 1) * value + item) / period
    return value


def kdj(rows: List[Dict[str, Any]], period: int = 9) -> Dict[str, Optional[float]]:
    if len(rows) < period:
        return {"k": None, "d": None, "j": None}
    k_value = 50.0
    d_value = 50.0
    for end in range(period, len(rows) + 1):
        window = rows[end - period : end]
        highest = max(row["high"] for row in window)
        lowest = min(row["low"] for row in window)
        close = window[-1]["close"]
        rsv = 50.0 if highest == lowest else 100.0 * (close - lowest) / (highest - lowest)
        k_value = 2.0 * k_value / 3.0 + rsv / 3.0
        d_value = 2.0 * d_value / 3.0 + k_value / 3.0
    return {"k": k_value, "d": d_value, "j": 3.0 * k_value - 2.0 * d_value}


def obv(rows: List[Dict[str, Any]]) -> float:
    value = 0.0
    for current, previous in zip(rows[1:], rows[:-1]):
        if current["close"] > previous["close"]:
            value += current["volume"]
        elif current["close"] < previous["close"]:
            value -= current["volume"]
    return value


def period_return(values: List[float], period: int) -> Optional[float]:
    if len(values) <= period:
        return None
    return values[-1] / values[-1 - period] - 1.0


def max_drawdown(values: List[float]) -> float:
    peak = values[0]
    worst = 0.0
    for value in values:
        peak = max(peak, value)
        worst = min(worst, value / peak - 1.0)
    return worst


def ma_cross_backtest(closes: List[float], fast: int, slow: int) -> Dict[str, Any]:
    if fast <= 0 or slow <= 0 or fast >= slow:
        raise ValueError("backtest requires 0 < fast < slow")
    if len(closes) <= slow:
        return {"status": "unavailable", "reason": f"requires more than {slow} rows"}

    positions: List[int] = []
    for end in range(1, len(closes) + 1):
        fast_ma = sma(closes, fast, end)
        slow_ma = sma(closes, slow, end)
        positions.append(1 if fast_ma is not None and slow_ma is not None and fast_ma > slow_ma else 0)

    start = slow - 1
    equity = 1.0
    curve = [equity]
    changes = 0
    invested_days = 0
    for index in range(start + 1, len(closes)):
        prior_position = positions[index - 1]
        if positions[index - 1] != positions[index - 2]:
            changes += 1
        if prior_position:
            invested_days += 1
            equity *= closes[index] / closes[index - 1]
        curve.append(equity)

    return {
        "status": "ok",
        "rule": f"long when SMA{fast} > SMA{slow}; use prior-day signal",
        "transaction_costs_included": False,
        "strategy_return": equity - 1.0,
        "buy_hold_return_same_window": closes[-1] / closes[start] - 1.0,
        "max_drawdown": max_drawdown(curve),
        "position_changes": changes,
        "invested_days": invested_days,
        "evaluation_days": len(closes) - 1 - start,
    }


def round_floats(value: Any) -> Any:
    if isinstance(value, float):
        if math.isnan(value) or math.isinf(value):
            return None
        return round(value, 6)
    if isinstance(value, dict):
        return {key: round_floats(item) for key, item in value.items()}
    if isinstance(value, list):
        return [round_floats(item) for item in value]
    return value


def analyze(rows: List[Dict[str, Any]], include_backtest: bool, fast: int, slow: int) -> Dict[str, Any]:
    closes = [row["close"] for row in rows]
    volumes = [row["volume"] for row in rows]
    ema12 = ema_series(closes, 12)
    ema26 = ema_series(closes, 26)
    diffs = [short - long for short, long in zip(ema12, ema26)]
    dea = ema_series(diffs, 9)
    boll_mid = sma(closes, 20)
    boll_std = statistics.pstdev(closes[-20:]) if len(closes) >= 20 else None
    atr14 = atr_wilder(rows, 14)
    ma20 = sma(closes, 20)
    ma60 = sma(closes, 60)

    if ma20 is None or ma60 is None:
        ma_structure = "unavailable"
    elif closes[-1] > ma20 > ma60:
        ma_structure = "bullish"
    elif closes[-1] < ma20 < ma60:
        ma_structure = "bearish"
    else:
        ma_structure = "mixed"

    result: Dict[str, Any] = {
        "mode": "local-standard-library",
        "data": {
            "rows": len(rows),
            "start": rows[0]["date"],
            "end": rows[-1]["date"],
            "latest_close": closes[-1],
        },
        "indicators": {
            "sma5": sma(closes, 5),
            "sma10": sma(closes, 10),
            "sma20": ma20,
            "sma60": ma60,
            "ma_structure": ma_structure,
            "return_20d": period_return(closes, 20),
            "return_60d": period_return(closes, 60),
            "max_drawdown_60d": max_drawdown(closes[-60:]) if len(closes) >= 60 else None,
            "macd_dif": diffs[-1] if len(closes) >= 26 else None,
            "macd_dea": dea[-1] if len(closes) >= 26 else None,
            "macd_hist_dif_minus_dea": diffs[-1] - dea[-1] if len(closes) >= 26 else None,
            "rsi14": rsi_wilder(closes, 14),
            "boll20_mid": boll_mid,
            "boll20_upper": boll_mid + 2.0 * boll_std if boll_mid is not None and boll_std is not None else None,
            "boll20_lower": boll_mid - 2.0 * boll_std if boll_mid is not None and boll_std is not None else None,
            "atr14": atr14,
            "atr14_pct_close": atr14 / closes[-1] if atr14 is not None else None,
            "kdj9": kdj(rows, 9),
            "obv": obv(rows),
            "volume_ratio_5": volumes[-1] / (sum(volumes[-5:]) / 5.0)
            if len(volumes) >= 5 and sum(volumes[-5:]) > 0
            else None,
        },
        "limitations": [
            "input data is not fetched or verified by this script",
            "corporate-action adjustment must be documented by the caller",
            "indicator thresholds are evidence, not trade instructions",
        ],
    }
    if include_backtest:
        result["backtest"] = ma_cross_backtest(closes, fast, slow)
    return round_floats(result)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--csv", required=True, type=Path, help="OHLCV CSV path")
    parser.add_argument("--backtest", action="store_true", help="run a simple MA cross backtest")
    parser.add_argument("--fast", type=int, default=20, help="fast SMA period")
    parser.add_argument("--slow", type=int, default=60, help="slow SMA period")
    args = parser.parse_args()

    try:
        payload = analyze(load_rows(args.csv), args.backtest, args.fast, args.slow)
    except (OSError, ValueError) as exc:
        raise SystemExit(f"error: {exc}") from exc
    print(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
