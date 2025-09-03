import os
from app.local_client import LocalProvider
from app.gcp_client import GCPProvider

def get_provider():
    provider_type = os.getenv("PROVIDER", "LOCAL").upper()
    if provider_type == "GCP":
        return GCPProvider()
    return LocalProvider()
