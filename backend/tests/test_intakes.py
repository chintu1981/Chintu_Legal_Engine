from fastapi.testclient import TestClient
from backend.api.main import app

def test_create_and_list():
    with TestClient(app) as client:
        payload = {
            "client_id": 1,
            "case_type": "Case A",
            "product_or_drug": "ProductX",
            "status": "new",
            "score": 0
        }
        r = client.post("/intakes/", json=payload)
        assert r.status_code == 200
        r = client.get("/intakes/")
        assert r.status_code == 200
        assert isinstance(r.json(), list)
