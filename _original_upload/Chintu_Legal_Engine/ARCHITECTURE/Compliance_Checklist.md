# Compliance Checklist – Chintu Legal Engine

---

## HIPAA Administrative Safeguards
- [ ] Business Associate Agreements (Azure, Auth, eSign, SMS, Records)
- [ ] Appointed Privacy & Security Officers
- [ ] Access management policy (RBAC/ABAC)
- [ ] Workforce training on PHI handling
- [ ] Risk analysis & mitigation plan
- [ ] Incident response procedure

---

## HIPAA Physical Safeguards
- [ ] Cloud environment with physical security (Azure certified)
- [ ] Data center redundancy (US region)
- [ ] Offsite backup and disaster recovery tested quarterly

---

## HIPAA Technical Safeguards
- [ ] Encryption at rest (AES-256)
- [ ] Encryption in transit (TLS 1.2+)
- [ ] MFA enforced for all admins
- [ ] Session timeout & device revocation
- [ ] Audit logs for every PHI access
- [ ] DLP filters (no PHI in logs/emails)

---

## SOC-2 Baseline Controls
- [ ] Change management process
- [ ] Continuous monitoring & logging
- [ ] Data retention policy per tenant
- [ ] Vulnerability scans monthly
- [ ] Third-party vendor review (BAA)
- [ ] Annual pen-testing (Phase 3)

---

## Documentation
- [ ] HIPAA Security Policy (to be written Phase 3)
- [ ] Privacy Notice & Terms for law firms
- [ ] Breach Notification Runbook
- [ ] Audit Log format definition (JSON schema)

---

## Azure Security Config Checklist
| Control | Status |
|----------|---------|
| Azure Health Data Services HIPAA BAA | Pending |
| Key Vault with HSM-backed CMKs | ✅ |
| Blob Storage private endpoint only | ✅ |
| Service Bus encryption | ✅ |
| Defender for Cloud on all resources | ✅ |
| Logging to SIEM | ✅ |
