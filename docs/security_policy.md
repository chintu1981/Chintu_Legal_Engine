# Security & Privacy Policy (v1)
**Project:** Chintu Legal Engine • **Date:** 2025-10-24

## 1. Data Classification
- **Public**: Non-sensitive docs (README, public SOPs)
- **Internal**: Process docs, metrics without PII
- **Confidential (PII/PHI)**: Names, DOB, medical, SSNs — *never* in dev
- **Restricted**: Keys, credentials, private client docs

## 2. Roles & RBAC (Phase 1 baseline)
- **Owner (You)**: Full repo/admin; approve prod secrets
- **PM**: Access to Internal + Confidential (by task), no prod keys
- **Intake**: Access to assigned leads only; no code repo write
- **Paralegal**: Access to assigned cases/doc vault; no prod keys

Principle of least privilege. Access reviews monthly.

## 3. Secrets Handling
- Do not commit `.env` files.
- Use `.env.example` for shape; real values go in local `.env` and (later) a secrets manager.
- Rotate JWT_SECRET and keys every 90 days (min).

## 4. Environments
- **Dev**: Local only; masked fixtures; logging at INFO without PII.
- **Stage**: Sanitized test data; INFO logs; limited external calls.
- **Prod**: Real data; WARNING-level logs; request IDs; centralized audit logs.

## 5. Logging & Telemetry
- No PII in logs. Redact tokens and emails.
- Include `request_id` and timestamp. Store logs for 90 days.

## 6. Data Retention & Right-to-Delete
- Dev fixtures: rotate monthly.
- Prospect leads w/o retainer: purge after 12 months.
- Honor verifiable deletion requests within 30 days.

## 7. Incident Response (baseline)
- Triage owner within 1 hour; classify severity (S0–S3).
- Contain → Eradicate → Recover → Postmortem within 72 hours.

## 8. Vendor/Tooling
- Email & docs: Google Workspace with 2FA.
- E-sign: Use platform with audit trails and HIPAA-ready options when applicable.
- Storage: Encrypted at rest; access scoped by role.

## 9. Physical & Account Security
- 2FA on GitHub, Google, e-sign, and any dashboard.
- Use password manager; disallow shared credentials.

## 10. Compliance Notes
This is not legal advice. For PHI-heavy flows, align with HIPAA best practices and a BAA with vendors where needed.
