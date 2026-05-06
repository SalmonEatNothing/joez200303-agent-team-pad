# Hello Server

Hello Server is a minimal FastAPI application.

## v3 endpoint

`GET /v3-smoke` is available as a v3 deployment smoke test.

Example request:

```bash
curl http://127.0.0.1:8000/v3-smoke
```

Example response body:

```json
{
  "v3": "ok",
  "started_at": "2026-05-06T00:00:00+00:00",
  "commit": "abc1234"
}
```
