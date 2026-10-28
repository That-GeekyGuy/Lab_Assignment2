import pytest

from app import add, app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


def test_add_function():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_add_route(client):
    response = client.get("/add?a=2&b=3")
    assert response.status_code == 200
    assert response.get_json() == {"result": 5.0}


def test_add_route_missing_param(client):
    response = client.get("/add?a=2")
    assert response.status_code == 400


def test_add_route_invalid_param(client):
    response = client.get("/add?a=x&b=3")
    assert response.status_code == 400
