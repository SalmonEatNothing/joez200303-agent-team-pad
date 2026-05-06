from fastapi.testclient import TestClient

from hello_server.app import app


client = TestClient(app)


def test_v3_smoke_status_ok() -> None:
    response = client.get("/v3-smoke")

    assert response.status_code == 200


def test_v3_smoke_body_has_three_fields() -> None:
    response = client.get("/v3-smoke")

    body = response.json()
    assert set(body) == {"v3", "started_at", "commit"}
    assert body["v3"] == "ok"


def test_v3_smoke_commit_is_seven_chars() -> None:
    response = client.get("/v3-smoke")

    commit = response.json()["commit"]
    assert len(commit) == 7
    assert all(character in "0123456789abcdef" for character in commit)


def test_v3_smoke_started_at_stable_across_requests() -> None:
    first_response = client.get("/v3-smoke")
    second_response = client.get("/v3-smoke")

    assert first_response.json()["started_at"] == second_response.json()["started_at"]
