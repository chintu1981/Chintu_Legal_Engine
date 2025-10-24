from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field

class Client(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    full_name: str
    phone: Optional[str] = None
    email: Optional[str] = None
    state: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)

class Intake(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    client_id: int = Field(foreign_key="client.id")
    case_type: str
    product_or_drug: Optional[str] = None
    incident_date: Optional[str] = None
    notes: Optional[str] = None
    status: str = "new"  # new|eligible|edge|ineligible
    score: int = 0
    created_at: datetime = Field(default_factory=datetime.utcnow)
