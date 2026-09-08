PharmaGuide - Pharmacogenomics Risk Assessment
=============================================

This project provides a simple fullstack demo application for pharmacogenomic risk assessment from VCF files.

### Features

- Backend API that accepts:
  - A VCF file upload (`.vcf`, Variant Call Format v4.2, up to 5 MB)
  - One or more drug names (comma-separated), supporting:
    - `CODEINE`, `WARFARIN`, `CLOPIDOGREL`, `SIMVASTATIN`, `AZATHIOPRINE`, `FLUOROURACIL`
- Returns structured JSON for each drug with this schema:

```json
{
  "patient_id": "PATIENT_XXX",
  "drug": "DRUG_NAME",
  "timestamp": "ISO8601_timestamp",
  "risk_assessment": {
    "risk_label": "Safe|Adjust Dosage|Toxic|...",
    "confidence_score": 0.0,
    "severity": "none|low|moderate|high|critical"
  },
  "pharmacogenomic_profile": {
    "primary_gene": "GENE_SYMBOL",
    "diplotype": "*X/*Y",
    "phenotype": "PM|IM|NM|RM|URM|Unknown",
    "detected_variants": [
      {
        "rsid": "rsXXXX"
      }
    ]
  },
  "clinical_recommendation": {},
  "llm_generated_explanation": {
    "summary": ""
  },
  "quality_metrics": {
    "vcf_parsing_success": true
  }
}
```

- Simple React frontend:
  - Drag & drop / file picker for `.vcf`
  - Drug selection (multi-select or comma-separated)
  - Color-coded risk labels:
    - Green = Safe
    - Yellow = Adjust
    - Red = Toxic / Ineffective
  - Expandable sections for details
  - Download JSON and copy-to-clipboard

### Tech Stack

- Backend: Python, FastAPI, Uvicorn
- Frontend: React + TypeScript + Vite

### Running the Project

From the `pharamaguide` folder:

```bash
# Backend (Python + FastAPI)
cd backend
python -m venv venv
venv\Scripts\activate   # On Windows PowerShell: .\venv\Scripts\Activate
pip install -r requirements.txt
uvicorn main:app --reload --port 3000

# In a new terminal, start frontend
cd ../frontend
npm install
npm run dev
```

Then open the frontend URL printed by Vite (typically `http://localhost:5173`) and it will call the backend at `http://localhost:3000`.


