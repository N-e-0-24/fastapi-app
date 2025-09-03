import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


@pytest.fixture
def vm_request():
    return {
        "project_id": "test-project",
        "zone": "local-a",
        "machine_type": "e2-medium",
        "image_family": "debian-11",
        "vm_name": "test-vm",
    }


def test_create_vm(vm_request):
    response = client.post("/vms", json=vm_request)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "vm_id" in data


def test_get_vm_status(vm_request):
    # Ensure VM exists first
    client.post("/vms", json=vm_request)

    response = client.get(
        f"/vms/{vm_request['vm_name']}",
        params={"project_id": vm_request["project_id"], "zone": vm_request["zone"]},
    )
    assert response.status_code == 200
    assert response.json() in ["created", "running", "exited"]


def test_delete_vm(vm_request):
    # Ensure VM exists first
    client.post("/vms", json=vm_request)

    response = client.delete(
        f"/vms/{vm_request['vm_name']}",
        params={"project_id": vm_request["project_id"], "zone": vm_request["zone"]},
    )
    assert response.status_code == 200
    assert response.json()["status"] == "deleted"
