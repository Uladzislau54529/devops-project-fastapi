from fastapi.testclient import TestClient
from main import main

client = TestClient(main)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Project 2 is running"}

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
