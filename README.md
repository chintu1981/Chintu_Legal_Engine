# Chintu Legal Engine — Phase 1

**Phase:** Setup • Hiring Kit • Repo Structure  
**Date:** 2025-10-24

This repository standardizes the Phase 1 deliverables:
- Unified repo structure
- Hiring Kit (job descriptions, NDA, onboarding checklist)
- Project Charter & Dev Standards
- FastAPI backend skeleton
- Scripts and environment samples

## Quick Start

```bash
# 1) Set up a virtual environment
python3 -m venv .venv && source .venv/bin/activate

# 2) Install backend dependencies
pip install -r backend/requirements.txt

# 3) Run API (dev)
uvicorn backend.api.main:app --reload
```

## Layout
```
backend/               # FastAPI skeleton
configs/               # Config files & templates
data/                  # Sample data & fixtures
docs/                  # Charter and development standards
hiring/                # Hiring kit: JDs, NDA, onboarding
scripts/               # Helper scripts
_original_upload/      # Preserved upload from Phase 1
```

## Environment
Copy `.env.example` to `.env` and update values as needed.
