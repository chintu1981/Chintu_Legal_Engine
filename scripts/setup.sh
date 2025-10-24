#!/usr/bin/env bash
set -euo pipefail

python3 -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
echo "Environment ready. Run: uvicorn backend.api.main:app --reload"
