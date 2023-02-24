from fastapi.testclient import TestClient
from src.main import app
from src.main import primeNumbersFunc

client = TestClient(app)


def test_read_main() -> None:
    response = client.get("/prime_numbers/35")
    assert response.status_code == 200
    assert response.json()["num"] == 5702887


def test_functional() -> None:
    result = primeNumbersFunc(35)
    assert result == 5702887
