# Hello Server

Hello Server is a minimal FastAPI application with one endpoint:
`GET /hello` returns the JSON string `"world"`.

## Install

Install the package and development tools locally:

```bash
python3 -m pip install -e '.[dev]'
```

## Run Locally

Start the FastAPI development server with Uvicorn:

```bash
python3 -m uvicorn hello_server.app:app --reload
```

By default, Uvicorn serves the application at `http://127.0.0.1:8000`.

## Endpoint

| Method | Path | Status | Response body | Content-Type |
| --- | --- | --- | --- | --- |
| GET | `/hello` | `200 OK` | `"world"` | `application/json` |

Example request:

```bash
curl http://127.0.0.1:8000/hello
```

Example response body:

```json
"world"
```

## Quality Gates

Run tests with coverage:

```bash
python3 -m pytest --cov=hello_server --cov-fail-under=80
```

Run lint:

```bash
python3 -m ruff check .
```

Run type checks:

```bash
python3 -m mypy hello_server tests
```

