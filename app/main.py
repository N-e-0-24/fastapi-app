from fastapi import FastAPI, HTTPException
from app.models import VMRequest, VMResponse, VMStatus
from app import deps

app = FastAPI(title="GCP VM API", version="1.0.0")

provider = deps.get_provider()


@app.post("/vms", response_model=VMResponse)
def create_vm(request: VMRequest):
    try:
        vm_id = provider.create_vm(request)
        return {"status": "success", "vm_id": vm_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/vms/{vm_name}", response_model=VMStatus)
def get_vm(vm_name: str, project_id: str, zone: str):
    try:
        status = provider.get_vm(vm_name, project_id, zone)
        return {"vm_name": vm_name, "status": status}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@app.delete("/vms/{vm_name}")
def delete_vm(vm_name: str, project_id: str, zone: str):
    try:
        provider.delete_vm(vm_name, project_id, zone)
        return {"status": "deleted", "vm_name": vm_name}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@app.get("/health")
def health_check():
    return {"status": "ok"}

