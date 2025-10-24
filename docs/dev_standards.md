# Development Standards

## Branching
- `main`: protected, stable
- `dev`: integration branch
- Feature branches: `feat/<slug>`
- Fix branches: `fix/<slug>`

## Commits (Conventional)
- `feat:`, `fix:`, `docs:`, `refactor:`, `chore:`, `test:`, `ci:`

## Code Style
- Python: black, isort, flake8 (Phase 2)
- Type hints required for backend public interfaces
- 1 file = 1 responsibility; avoid god-modules

## Reviews
- Require PR + 1 approval for merging to `dev`
- CI must pass lint + tests

## Secrets
- Never commit `.env`; use secret managers later (Phase 2/3)
