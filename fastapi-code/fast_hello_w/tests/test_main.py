from fastapi.testclient import TestClient
from fast_hello_w.main import app


def test_index_path():
    client =  TestClient(app=app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"hello" : "World now"}

    def test_piaic_path():
        client = TestClient(app=app)
        response = client.get("/piaic")
        assert response.status_code == 200
        assert response.json() == {"batch":"panaverse"}
