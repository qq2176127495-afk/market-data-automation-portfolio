"""Lite data collector example.

This file is intentionally small and safe for a public portfolio/resource page.
It demonstrates basic JSON fetching, row normalization, and CSV saving.
It does not include private strategy logic, credentials, production logs, or
live trading/execution code.
"""

from __future__ import annotations

import argparse
import csv
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.request import Request, urlopen


SAMPLE_ROWS = [
    {
        "symbol": "AAA-USDT-SWAP",
        "timestamp": "2026-01-01T00:00:00Z",
        "open": 1.0000,
        "high": 1.0120,
        "low": 0.9960,
        "close": 1.0080,
        "volume_quote": 125000.00,
    },
    {
        "symbol": "BBB-USDT-SWAP",
        "timestamp": "2026-01-01T00:01:00Z",
        "open": 2.0000,
        "high": 2.0150,
        "low": 1.9900,
        "close": 2.0060,
        "volume_quote": 98000.00,
    },
]


def fetch_json(url: str, timeout: int = 10) -> Any:
    request = Request(url, headers={"User-Agent": "collector-lite/1.0"})
    with urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def normalize_payload(payload: Any) -> list[dict[str, Any]]:
    """Convert common JSON shapes into a small list of flat rows.

    This is a conservative demo normalizer. Real client work should define
    field mapping according to the target API contract.
    """
    if isinstance(payload, dict):
        data = payload.get("data", payload.get("items", payload))
    else:
        data = payload

    if isinstance(data, dict):
        data = [data]
    if not isinstance(data, list):
        data = [{"value": data}]

    rows: list[dict[str, Any]] = []
    for item in data[:100]:
        if isinstance(item, dict):
            row = {
                key: value
                for key, value in item.items()
                if isinstance(value, (str, int, float, bool)) or value is None
            }
        else:
            row = {"value": item}
        row.setdefault("collected_at", datetime.now(timezone.utc).isoformat())
        rows.append(row)
    return rows


def save_csv(rows: list[dict[str, Any]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = sorted({key for row in rows for key in row.keys()})
    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser(description="Safe lite JSON collector demo")
    parser.add_argument("--url", default="", help="Optional public JSON API URL")
    parser.add_argument("--out", default="examples/output.csv", help="Output CSV path")
    args = parser.parse_args()

    payload = fetch_json(args.url) if args.url else SAMPLE_ROWS
    rows = normalize_payload(payload)
    save_csv(rows, Path(args.out))
    print(f"saved {len(rows)} rows -> {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
