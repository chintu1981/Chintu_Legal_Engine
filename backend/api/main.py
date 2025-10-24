from fastapi import FastAPI
from backend.models.database import init_db
from backend.api.clients import router as client_router
from backend.api.intakes import router as intake_router

app = FastAPI(title="Chintu Legal Engine API", version="0.2.1")

@app.on_event("startup")
def _startup():
    init_db()

app.include_router(client_router)
app.include_router(intake_router)

@app.get("/health")
def health():
    return {"status": "ok", "service": "legal-engine", "version": "0.2.1"}
