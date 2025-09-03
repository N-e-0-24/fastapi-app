import docker
from app.models import VMRequest

class LocalProvider:
    def __init__(self):
        self.client = docker.from_env()

    def create_vm(self, request: VMRequest):
        container = self.client.containers.run(
            image="ubuntu:22.04",  # maps from image_family
            name=request.vm_name,
            detach=True,
            tty=True,
            stdin_open=True,
            labels={"project_id": request.project_id, "zone": request.zone}
        )
        return f"projects/{request.project_id}/zones/{request.zone}/instances/{request.vm_name}"

    def get_vm(self, vm_name: str, project_id: str, zone: str):
        try:
            container = self.client.containers.get(vm_name)
            return container.status
        except Exception:
            raise Exception("VM not found")

    def delete_vm(self, vm_name: str, project_id: str, zone: str):
        try:
            container = self.client.containers.get(vm_name)
            container.stop()
            container.remove()
        except Exception:
            raise Exception("VM not found")
