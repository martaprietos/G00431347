from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import Select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.database import engine, get_db
from app.models import Base, RequestDB
from app.schemas import RequestCreate, RequestRead

app = FastAPI(title="Lab Exam Marta Prieto")

@app.get("/health")
def health():
    return{"status": "ok"}

@app.post(
    "/api/request",
    response_model=RequestRead,
)
def add_request(
    new_request: RequestCreate,
    db: Session = Depends(get_db),
):
    db_request = RequestDB(**new_request.model_dump())
    db.add(db_request)
    try:
        db.commit()
        db.refresh(db_request)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Request already exists")
    return db_request

@app.get(
    "/api/request",
    response_model=list[RequestRead],
)
def get_requests(db: Session = Depends(get_db)):
    statement = select(RequestDB).order_by(RequestDB.id)
    return db.execute(statement).scalars().all()

@app.get(
    "/api/request/{equipment_id}",
    response_model=RequestDB,
)
def get_request(equipment_id: int, db: Session = Depends(get_db)):
    db_request = db.get(RequestDB, equipment_id)
    if db_request is None:
        raise HTTPException(
            status_code=404,
            detail="Request not found",
 )
    return db_request
