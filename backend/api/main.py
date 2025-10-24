from fastapi import FastAPI

app = FastAPI(title="Chintu Legal Engine API", version="0.1.0")

@app.get("/health")
def health():
    return {"status": "ok", "service": "legal-engine", "version": "0.1.0"}
