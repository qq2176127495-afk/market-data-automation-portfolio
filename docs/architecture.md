# Lite Architecture

## Data Flow

```text
Public JSON API or sample rows
  -> collector_lite.py
  -> normalize simple fields
  -> save CSV
  -> inspect sample output
```

## What This Lite Version Shows

- How to request a public JSON endpoint.
- How to normalize simple JSON objects into flat rows.
- How to save data as CSV.
- How to keep credentials and private files out of a public resource package.

## What It Does Not Show

- No account credentials.
- No server deployment.
- No production logs.
- No private business rules.
- No complete commercial data platform.
