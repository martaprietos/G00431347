import pytest

def request_payload( equipment_id = 2, student_id = "ST-1234" , description = "This is a request for a new computer", priority = 3, status = "OPEN"):

    return{
        "equipment_id": equipID,
        "student_id": sid,
        "description": desc,
        "priority": priority,
        "status": stat
    }
        
def test_create_and_retrieve_200(client):
    created = client.post("/api/request", json=request_payload)
    req_id = created["id"]
    response = client.get("/api/request")
    assert response.status_code == 200

    data = response.json
    assert len(data) == 1
    assert data[0]["equipment_id"] == 2

@pytest.mark.parametrize("bad", "st-13233", "ST123414")
def test_bad_id(client):
    response = client.post("/api/request", json=request_payload)
    assert response.status_code == 422
