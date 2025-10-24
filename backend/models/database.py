import os
from sqlmodel import SQLModel, create_engine, Session

DB_URL = os.getenv("DB_URL", "sqlite:///./data/dev.db")

# SQLite needs this when using a file path
connect_args = {"check_same_thread": False} if DB_URL.startswith("sqlite") else {}

# Ensure ./data exists when using sqlite:///./data/dev.db
if DB_URL.startswith("sqlite:///"):
    db_path = DB_URL.replace("sqlite:///", "")
    os.makedirs(os.path.dirname(db_path), exist_ok=True)

engine = create_engine(DB_URL, echo=False, connect_args=connect_args)

def get_session():
    with Session(engine) as session:
        yield session

def init_db():
    # Import models here so SQLModel sees them before create_all
    from backend.models import intake_models  # noqa: F401
    SQLModel.metadata.create_all(engine)
