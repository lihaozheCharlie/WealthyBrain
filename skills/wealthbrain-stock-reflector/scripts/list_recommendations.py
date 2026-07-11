#!/usr/bin/env python3
"""列出需要复盘的 WealthBrain 推荐记录。"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


def truthy(value: str) -> bool:
    return value.strip().lower() in {"1", "true", "yes", "y"}


def main() -> None:
    parser = argparse.ArgumentParser(description="从 WealthBrain CSV 中列出推荐记录。")
    parser.add_argument(
        "--csv",
        default="wiki/90-data/recommendations.csv",
        help="recommendations.csv 的路径。",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="包含已归档或不纳入批量复盘的记录。",
    )
    parser.add_argument(
        "--format",
        choices=["json", "symbols"],
        default="json",
        help="输出格式。",
    )
    args = parser.parse_args()

    path = Path(args.csv)
    if not path.exists():
        raise SystemExit(f"找不到 CSV: {path}")

    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    if not args.all:
        rows = [
            row
            for row in rows
            if truthy(row.get("include_in_batch_review", ""))
            and row.get("status", "").strip().lower() != "archived"
        ]

    if args.format == "symbols":
        symbols = sorted({row.get("symbol", "").strip() for row in rows if row.get("symbol", "").strip()})
        print("\n".join(symbols))
        return

    print(json.dumps(rows, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
