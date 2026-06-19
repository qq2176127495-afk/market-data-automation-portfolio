# Python Market Data Collector Lite

Python 行情数据采集与清洗脚本 Lite 版。

> 这是一个可公开展示/售卖的阉割版源码示例，只保留基础数据采集、字段清洗、CSV/JSON 保存和脱敏样例。它不是完整交易系统，不包含私有策略、实盘逻辑、账号信息、服务器配置或生产日志。

## 适用场景

- 学习 Python 接口数据采集
- 快速搭建 REST API 数据落盘脚本
- 将 JSON 数据整理为 CSV
- 给接单平台展示数据采集与清洗能力
- 作为二次开发的最小模板

## Lite 版包含

- `src/collector_lite.py`：基础 HTTP JSON 采集与本地保存示例
- `examples/sample_market_rows.csv`：合成样例数据
- `examples/sanitized_report_sample.md`：脱敏报告样例
- `docs/architecture.md`：简化数据流说明
- `docs/programinn-copy.md`：程序员客栈填写文案

## Lite 版不包含

- API Key、`.env`、服务器/VPS 信息
- 真实账户、订单、余额、仓位
- 完整策略源码、入场/出场规则、核心参数
- 实盘执行、自动下单、风控执行模块
- 生产环境日志和历史原始数据

## 使用方式

不传 URL 时运行内置合成样例：

```bash
python src/collector_lite.py --out examples/output.csv
```

传入公开 JSON API 时，可保存原始响应摘要：

```bash
python src/collector_lite.py --url "https://example.com/api/data" --out output.csv
```

## 目录结构

```text
.
├── README.md
├── src/
│   └── collector_lite.py
├── docs/
│   ├── architecture.md
│   ├── programinn-copy.md
│   └── screenshot-guide.md
└── examples/
    ├── sample_market_rows.csv
    └── sanitized_report_sample.md
```

## 说明

这个仓库适合做作品展示或源码资源示例。如果需要完整业务采集、定时任务、代理池、数据库入库、异常告警、后台页面或部署服务，需要基于实际需求另行开发。
