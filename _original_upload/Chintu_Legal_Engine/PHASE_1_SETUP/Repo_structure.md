# Repo Structure – Chintu Legal Engine

root/
├── backend/               # FastAPI
│   ├── main.py
│   ├── app/
│   │   ├── models/
│   │   ├── routes/
│   │   ├── services/
│   │   └── utils/
│   └── requirements.txt
│
├── frontend/              # Next.js dashboard
│   ├── pages/
│   ├── components/
│   ├── hooks/
│   └── package.json
│
├── infra/                 # Terraform or Bicep
│   ├── main.tf
│   └── variables.tf
│
├── docs/
│   ├── architecture.md
│   ├── api_contracts.md
│   └── compliance_checklist.md
│
└── .github/
    └── workflows/
        └── ci.yml
