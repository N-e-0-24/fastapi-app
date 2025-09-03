from app.models import VMRequest

class GCPProvider:
    def create_vm(self, request: VMRequest):
        raise NotImplementedError("GCP provider not implemented in LOCAL mode")

    def get_vm(self, vm_name: str, project_id: str, zone: str):
        raise NotImplementedError("GCP provider not implemented in LOCAL mode")

    def delete_vm(self, vm_name: str, project_id: str, zone: str):
        raise NotImplementedError("GCP provider not implemented in LOCAL mode")
