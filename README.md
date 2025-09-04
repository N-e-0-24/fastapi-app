Perfect 👍 Let’s create a **detailed `README.md`** for your project that covers setup, local development, Docker, GitHub Actions, and API usage.

Here’s a complete draft:

---

# 🚀 FastAPI GCP VM API (Local Docker Simulation)

This project provides a **FastAPI-based REST API** that simulates **Google Cloud Platform (GCP) VM management** using **Docker containers locally**.

It was built as a DevOps assignment to demonstrate:

* Python API development with **FastAPI**
* Infrastructure simulation using **Docker SDK**
* Containerization with **Dockerfile**
* CI/CD automation with **GitHub Actions**
* Deployment image publishing to **Docker Hub**

---

## 📌 Features

* **POST `/vms`** → Deploy a VM (simulated as a Docker container)
* **GET `/vms/{vm_name}`** → Check VM status
* **DELETE `/vms/{vm_name}`** → Terminate a VM

Supports both:

* **LocalProvider (Docker-based simulation)**
* **GCPProvider (Google Cloud SDK, real VM)** → requires real GCP credentials

---

## ⚙️ Tech Stack

* **Python 3.10+**
* **FastAPI**
* **Docker SDK for Python**
* **Google Cloud Compute SDK**
* **Pytest** (testing)
* **Flake8** (linting)
* **GitHub Actions** (CI/CD)

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/N-e-0-24/fastapi-app.git
cd fastapi-app
```

### 2. Create a virtual environment

```bash
python -m venv .venv
# On Linux / Mac
source .venv/bin/activate
# On Windows (Powershell)
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the FastAPI app locally

```bash
uvicorn app.main:app --reload
```

API will be available at: **[http://127.0.0.1:8000](http://127.0.0.1:8000)**
Docs: **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

---

## 🐳 Run with Docker

### 1. Build the Docker image

```bash
docker build -t fastapi-vm-api .
```

### 2. Run the container

```bash
docker run -d -p 8000:8000 --name fastapi-vm fastapi-vm-api
```

Now visit: **[http://localhost:8000/docs](http://localhost:8000/docs)**

---

## ☁️ CI/CD with GitHub Actions

The project includes `.github/workflows/ci.yml` which:

* Runs **flake8** linting
* Runs **pytest** unit tests
* Builds & pushes Docker image to **Docker Hub**

### Docker Hub Setup

1. Create a Docker Hub account.
2. Add GitHub Secrets in your repository:

   * `DOCKERHUB_USERNAME` → your Docker Hub username
   * `DOCKERHUB_TOKEN` → a personal access token or password

On every push to `main`, GitHub Actions will build & push the image.

---

## 🧪 Testing

Run tests locally:

```bash
pytest -v
```

---

## 📡 API Usage Examples

### Create a VM

```bash
curl -X POST "http://localhost:8000/vms" \
-H "Content-Type: application/json" \
-d '{
  "project_id": "local-project",
  "zone": "us-central1-a",
  "machine_type": "e2-medium",
  "image_family": "debian-11",
  "vm_name": "test-vm"
}'
```

**Response**

```json
{
  "status": "success",
  "vm_id": "projects/local-project/zones/us-central1-a/instances/test-vm"
}
```

---

### Get VM status

```bash
curl -X GET "http://localhost:8000/vms/test-vm?project_id=local-project&zone=us-central1-a"
```

**Response**

```json
{
  "status": "running"
}
```

---

### Delete a VM

```bash
curl -X DELETE "http://localhost:8000/vms/test-vm?project_id=local-project&zone=us-central1-a"
```

**Response**

```json
{
  "status": "terminated"
}
```

---

## 📂 Project Structure

```
.
├── app/
│   ├── main.py          # FastAPI entrypoint
│   ├── deps.py          # Dependency injection
│   ├── gcp_client.py    # Real GCP VM provider
│   ├── local_client.py  # Docker-based local VM provider
│   ├── models.py        # Pydantic models
├── tests/
│   ├── test_main.py     # Unit tests
├── Dockerfile
├── requirements.txt
├── .gitignore
├── .github/workflows/ci.yml
└── README.md
```

---

## 🔮 Future Improvements

* Add support for **multiple VM images** mapping.
* Support **VM metadata & networking simulation**.
* Deploy to **Kubernetes**.
* Author  : Ayush Singh

---


