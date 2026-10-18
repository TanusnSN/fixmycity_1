# FixMyCity API

FixMyCity is a civic complaint tracking backend designed to automate issue logging and identify duplicate reports across municipal zones.

---

## Tech Stack
- **Framework**: FastAPI (Python 3.13)
- **Containerization**: Docker & Docker Compose
- **IaC**: Terraform (Docker Provider)
- **CI/CD**: GitHub Actions
- **Testing**: Pytest & HTTPX TestClient

---

## Getting Started

### 1. Local Development
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r src/requirements.txt
uvicorn src.main:app --reload --port 8000