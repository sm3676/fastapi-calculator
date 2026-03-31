from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200

def test_add():
    response = client.get("/add?a=2&b=3")
    assert response.status_code == 200
    assert response.json()["result"] == 5

def test_subtract():
    response = client.get("/subtract?a=5&b=3")
    assert response.json()["result"] == 2

def test_multiply():
    response = client.get("/multiply?a=2&b=4")
    assert response.json()["result"] == 8

def test_divide():
    response = client.get("/divide?a=6&b=3")
    assert response.json()["result"] == 2.0

def test_divide_zero():
    response = client.get("/divide?a=5&b=0")
    assert response.status_code == 400