from fastapi.testclient import TestClient

from kwg_api.main import app

client = TestClient(app)
