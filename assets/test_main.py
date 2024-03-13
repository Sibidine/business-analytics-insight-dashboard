from fastapi.testclient import TestClient
from fastapi import status,HTTPException
from .main import app

client = TestClient(app)

def test_assets():
    response_assets = client.get('/assets/all')
    assert response_assets.status_code == status.HTTP_200_OK

def test_assets_id():
    response_assets_id = client.get(f'/assets/65e9569d921707a9b1ce0363')
    assert response_assets_id.status_code == status.HTTP_200_OK
    assert response_assets_id.json() == {
    "id": "65e9569d921707a9b1ce0363",
    "asset_name": "test1",
    "asset_type": "big",
    "location": "kol",
    "purchase_date": "24/12/23",
    "initial_cost": 100,
    "operational_status": "not working"
    }
    response_assets_id = client.get(f'/assets/65e9569d925707a9b1ce0363')
    assert response_assets_id.status_code == status.HTTP_404_NOT_FOUND

def tests_metrics():
    response_metrics = client.get('/metrics/all')
    assert response_metrics.status_code == status.HTTP_200_OK

def test_metrics_id():
    response_metrics_id = client.get(f'/metrics/65e9abd50152c15a84a84ad7')
    assert response_metrics_id.status_code == status.HTTP_200_OK
    assert response_metrics_id.json() == {
    "id": "65e9abd50152c15a84a84ad7",
    "asset_id": "65e9569d921707a9b1ce0363",
    "uptime": "08:00:00",
    "downtime": "00:02:30",
    "maintenance_cost": 500,
    "failure_rate": 60,
    "efficiency": 56.67
    }
    response_metrics_id = client.get(f'/metrics/65e9569d925707a9b1ce0363')
    assert response_metrics_id.status_code == status.HTTP_404_NOT_FOUND




