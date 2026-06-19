# Architecture

## Data Flow

```text
Public API
  -> paginated collector
  -> local JSON/CSV storage
  -> cleaning and deduplication
  -> feature extraction
  -> sample labeling
  -> segmented statistics
  -> Markdown report
```

## Engineering Notes

- Use public API endpoints only for portfolio demonstration.
- Keep credentials outside source control.
- Persist raw and normalized data separately.
- Make report generation reproducible.
- Keep production trading or private decision logic out of public repositories.

## Safety Boundary

The private project used observe-only flows and explicit safety guards. Public documentation intentionally omits any complete trading rule set or deployable execution logic.
