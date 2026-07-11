#!/usr/bin/env python3
"""为 WealthBrain 复盘计算简单收益率。"""

from __future__ import annotations

import argparse
import json


def main() -> None:
    parser = argparse.ArgumentParser(description="计算股票简单收益率。")
    parser.add_argument("--entry", type=float, required=True, help="推荐参考价或买入价。")
    parser.add_argument("--current", type=float, required=True, help="复盘现价。")
    parser.add_argument("--dividend", type=float, default=0.0, help="每股分红。")
    parser.add_argument("--fees", type=float, default=0.0, help="每股往返费用。")
    args = parser.parse_args()

    if args.entry <= 0:
        raise SystemExit("--entry 必须大于 0")

    absolute = args.current - args.entry + args.dividend - args.fees
    pct = absolute / args.entry * 100
    print(
        json.dumps(
            {
                "entry": args.entry,
                "current": args.current,
                "dividend": args.dividend,
                "fees": args.fees,
                "absolute_return": round(absolute, 6),
                "simple_return_pct": round(pct, 4),
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
