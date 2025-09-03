from pydantic import BaseModel

class VMRequest(BaseModel):
    project_id: str
    zone: str
    machine_type: str
    image_family: str
    vm_name: str

class VMResponse(BaseModel):
    status: str
    vm_id: str

class VMStatus(BaseModel):
    vm_name: str
    status: str
