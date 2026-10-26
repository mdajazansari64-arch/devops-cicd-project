from app.main import app


def test_health():
    client = app.test_client()
    res = client.get("/health")
    assert res.status_code == 200


def test_add_task():
    client = app.test_client()
    res = client.post("/tasks", json={"title": "learn devops"})
    assert res.status_code == 201
    assert res.get_json()["title"] == "learn devops"