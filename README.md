# Market Data Automation Portfolio

金融行情数据采集与自动化分析系统的脱敏作品集仓库。

> This is a sanitized portfolio repository. It demonstrates architecture, data flow, reporting format, and engineering practices without exposing private strategy logic, credentials, account data, or production logs.

## Overview

This project showcases a Python-based data automation workflow for collecting, cleaning, analyzing, and reporting market data.

The original private system includes:

- REST API historical data collection
- paginated candle fetching and deduplication
- JSON/CSV persistence
- feature extraction
- sample labeling
- Markdown report generation
- observe-only safety flow
- parameter evaluation records

This public repository only contains high-level documentation and synthetic examples.

## What It Demonstrates

- API data collection workflow design
- robust pagination and timeout handling
- structured data persistence
- automated Markdown reports
- data quality and sample-size awareness
- portfolio-safe project documentation

## Tech Stack

- Python
- Requests
- JSON / CSV
- Markdown reports
- Shell / PowerShell automation
- REST API integration

## Public Scope

Included:

- architecture overview
- sanitized report sample
- screenshot checklist
- portfolio copy for client platforms

Not included:

- API keys
- `.env` files
- VPS or SSH information
- production logs
- account data
- full strategy source code
- exact private trading parameters

## Portfolio Summary

Built a Python automation system that collects historical and real-time market data, normalizes local datasets, computes analysis features, and generates Markdown research reports. The private version processed hundreds of thousands of 1-minute market samples and produced segmented summaries by symbol, hour, and feature range.

## Repository Structure

```text
.
├── README.md
├── docs/
│   ├── architecture.md
│   ├── programinn-copy.md
│   └── screenshot-guide.md
└── examples/
    ├── sanitized_report_sample.md
    └── sample_market_rows.csv
```

## License

MIT License for documentation and synthetic examples only. Private production code and strategy logic are not part of this repository.
