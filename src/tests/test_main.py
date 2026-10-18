from fastapi.testclient import TestClient
from src.main import app, complaints_db

client = TestClient(app)

def setup_function():
    complaints_db.clear()

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to FixMyCity API. System Operational."}

def test_create_complaint():
    payload = {
        "category": "Pothole",
        "location": "NIE College Road",
        "description": "Deep pothole near entrance",
        "reported_by": "Ravi"
    }
    response = client.post("/complaints", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["status"] == "Pending"
    assert data["duplicate_count"] == 1

def test_duplicate_detection():
    payload1 = {
        "category": "Pothole",
        "location": "NIE College Road",
        "description": "Deep pothole near entrance",
        "reported_by": "Ravi"
    }
    payload2 = {
        "category": "Pothole",
        "location": "NIE College Road",
        "description": "Damaged road surface",
        "reported_by": "Ananya"
    }
    client.post("/complaints", json=payload1)
    response2 = client.post("/complaints", json=payload2)
    assert response2.status_code == 200
    data2 = response2.json()
    assert data2["id"] == 1
    assert data2["duplicate_count"] == 2