# Chintu Legal Engine – Architecture v0.1

> Core blueprint for the stealth legal-intake and compliance platform (HIPAA / SOC-2 ready).

---

## 1. Overview
A modular, cloud-native system providing AI-driven intake, compliance, medical record retrieval, and case scoring for law firms and agencies.

**Core Modules:**
1. AI Intake & Consent Chat
2. Firm Dashboard (multi-tenant SaaS)
3. Medical Retrieval Integration
4. Compliance & Audit Layer
5. Human Verification Desk (optional)

---

## 2. Tech Stack (HIPAA-Ready)

| Layer | Technology | Notes |
|-------|-------------|-------|
| Cloud | **Azure** | Health Data Services, BAA, full encryption |
| Backend | **FastAPI (Python)** | Core API + background jobs |
| Frontend | **Next.js (React)** | SaaS dashboard |
| Database | **PostgreSQL (Azure)** | Encrypted at rest |
| Storage | **Azure Blob + CMK** | For PHI & documents |
| Messaging | **Azure Service Bus** | Async jobs, event handling |
| Auth | **Auth0 HIPAA Plan / Azure AD B2C** | MFA + SSO + BAA |
| AI/LLM | **OpenAI GPT API (Azure endpoint)** | Lead scoring, summaries |
| eSign | **Dropbox Sign / DocuSign HIPAA** | Retainers & consents |
| Telephony | **Twilio (BAA)** | SMS/chat outreach |
| Infra | **Terraform/Bicep** | Reproducible IaC |
| Monitoring | **Azure Monitor / App Insights** | Security & audit |

---

## 3. System Flow

User (Client)
↓
AI Chat Intake → Consent (eSign)
↓
Lead Record (Postgres)
↓
Medical Record Request (API)
↓
AI Scoring (LLM + Rules)
↓
Dashboard → View → Export / Verify


---

## 4. Data Model Highlights
**Entities:**
- Tenant (law firm)
- User (staff, attorney)
- Lead (intake data)
- Consent (HIPAA / Retainer)
- MedicalRequest (vendor status)
- Summary (AI case score)
- AuditLog (immutable access record)

All PHI encrypted (AES-256 at rest), access logged, redacted for non-privileged roles.

---

## 5. Security & Compliance
- Azure HIPAA BAA in place
- Role-based access control
- End-to-end TLS + CMK
- Full audit trail
- Redaction middleware
- DLP rules (no PHI in logs)
- Data retention policies per tenant
- Annual risk assessment planned for Phase 3

---

## 6. Deployment
- **Environments:** Dev / Stage / Prod
- **CI/CD:** GitHub Actions → Azure Web App
- **IaC:** Terraform for full stack (network, DB, storage, service bus)
- **Monitoring:** Application Insights, Security Center

---

## 7. Future Expansion
- API marketplace for agencies
- White-label dashboards
- Predictive analytics on case outcomes
- Cross-docket performance metrics
