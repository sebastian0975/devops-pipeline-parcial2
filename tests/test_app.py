import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.app import app


client = app.test_client()


def test_home():
    response = client.get("/")

    assert response.status_code == 200

    data = response.get_json()

    assert data["estado"] == "OK"
    assert "mensaje" in data


def test_health():
    response = client.get("/health")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "UP"


def test_metrics():
    response = client.get("/metrics")

    assert response.status_code == 200


def test_error():
    response = client.get("/error")

    assert response.status_code == 500

    data = response.get_json()

    assert data["mensaje"] == "Error simulado"