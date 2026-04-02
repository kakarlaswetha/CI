import os
import sys

import pytest

# Ensure the repo root is on `sys.path` so `app/app.py` is importable in pytest.
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

from app.app import app as flask_app


@pytest.fixture
def client():
    flask_app.config.update(TESTING=True)
    with flask_app.test_client() as c:
        yield c


def test_health_endpoint(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json() == {"status": "ok"}


def test_hello_endpoint(client):
    resp = client.get("/hello")
    assert resp.status_code == 200
    assert resp.get_data(as_text=True) == "Hello world"

