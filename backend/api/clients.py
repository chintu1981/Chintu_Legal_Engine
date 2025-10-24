from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select, Session
from typing import List
from backend.models.database import get_session, init_db
from backend.models.intake_models import Client

router = APIRouter(prefix="/clients", tags=["clients"])

@router.post("/", response_model=Client)
def create_client(client: Client, session: Session = Depends(get_session)):
    session.add(client)
    session.commit()
    session.refresh(client)
    return client

@router.get("/", response_model=List[Client])
def list_clients(session: Session = Depends(get_session)):
    return session.exec(select(Client)).all()

@router.get("/{client_id}", response_model=Client)
def get_client(client_id: int, session: Session = Depends(get_session)):
    obj = session.get(Client, client_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Client not found")
    return obj
