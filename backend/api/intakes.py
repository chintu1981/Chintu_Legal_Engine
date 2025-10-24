from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlmodel import select, Session
from backend.models.database import get_session
from backend.models.intake_models import Intake

router = APIRouter(prefix="/intakes", tags=["intakes"])

@router.post("/", response_model=Intake)
def create_intake(item: Intake, session: Session = Depends(get_session)):
    session.add(item)
    session.commit()
    session.refresh(item)
    return item

@router.get("/", response_model=List[Intake])
def list_intakes(session: Session = Depends(get_session)):
    return session.exec(select(Intake)).all()

@router.get("/{intake_id}", response_model=Intake)
def get_intake(intake_id: int, session: Session = Depends(get_session)):
    obj = session.get(Intake, intake_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return obj
