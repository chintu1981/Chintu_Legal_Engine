# Developer Environment Guide – Phase 1

### Requirements
- Python 3.11 +
- Node 18 +
- Azure CLI / Terraform / Docker Desktop
- VS Code + extensions (Pylance, ESLint)

### Setup Steps
1. Clone repo.
2. Create `.env` for FastAPI and Next.js.
3. Run `docker compose up --build` (local Postgres + MinIO mock).
4. Push feature branches via PR with lint & tests.
5. Enable pre-commit hooks for secrets scan & formatting.

### Security Reminders
- Never store PHI in logs.
- Use Azure Key Vault for all secrets.
- Follow RBAC least-privilege rules.
