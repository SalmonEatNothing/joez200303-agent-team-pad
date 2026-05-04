from fastapi.testclient import TestClient

from hello_server.app import app


client = TestClient(app)


def test_hello_status_ok() -> None:
    response = client.get("/hello")

    assert response.status_code == 200


def test_hello_body_is_world() -> None:
    response = client.get("/hello")

    assert response.json() == "world"


def test_hello_content_type_json() -> None:
    response = client.get("/hello")

    assert response.headers["content-type"].startswith("application/json")

