import pytest

def request_payload( equipment_id = 2, student_id = "ST-1234" , description = "This is a request for a new computer", priority = 3):

    return{
        "equipment_id": equipment_id,
        "student_id": student_id,
        "description": description,
        "priority": priority,
    }
        
def test_create_and_retrieve_200(client):
    resp = client.post("/api/request", json=request_payload())
    assert resp.status_code == 201
    data = resp.json()
    assert data["id"] == 1
    assert data["description"] == "This is a request for a new computer"

    getResp = client.get("/api/request")
    assert getResp.status_code == 201
    data = getResp.json
    assert len(data) == 1
    assert data["description"] == "This is a request for a new computer"

@pytest.mark.parametrize("bad", ["St1234", "st-13233", "ST123414"],)
def test_bad_id(client):
    response = client.post("/api/request", json=request_payload(student_id=bad))
    assert response.status_code == 422


def test_get_all(client):
    client.post("/api/request").json()
    response = client.get("/api/request/{equipment_id}")
    assert response.status_code == 200

    assert response.json()["student_id"] == "ST-1234"