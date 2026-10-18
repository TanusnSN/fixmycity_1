from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import datetime

app = FastAPI(title="FixMyCity API", version="1.0.0")

complaints_db = []

class ComplaintCreate(BaseModel):
    category: str
    location: str
    description: str
    reported_by: str

class ComplaintResponse(BaseModel):
    id: int
    category: str
    location: str
    description: str
    reported_by: str
    status: str
    duplicate_count: int
    created_at: str

@app.get("/")
def read_root():
    return {"message": "Welcome to FixMyCity API. System Operational."}

@app.get("/complaints", response_model=List[ComplaintResponse])
def get_complaints():
    return complaints_db

@app.post("/complaints", response_model=ComplaintResponse)
def submit_complaint(complaint: ComplaintCreate):
    norm_loc = complaint.location.strip().lower()
    norm_cat = complaint.category.strip().lower()

    for existing in complaints_db:
        if (
            existing["category"].strip().lower() == norm_cat
            and existing["location"].strip().lower() == norm_loc
            and existing["status"] != "Resolved"
        ):
            existing["duplicate_count"] += 1
            return existing

    new_ticket = {
        "id": len(complaints_db) + 1,
        "category": complaint.category,
        "location": complaint.location,
        "description": complaint.description,
        "reported_by": complaint.reported_by,
        "status": "Pending",
        "duplicate_count": 1,
        "created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    complaints_db.append(new_ticket)
    return new_ticket