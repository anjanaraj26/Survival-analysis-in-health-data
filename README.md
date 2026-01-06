# Survival Analysis in Health Data

A small, well-documented survival analysis project demonstrating both
**classical biostatistics (Cox PH)** and **machine learning (Random Survival Forest)**
for time-to-event outcomes in healthcare-style datasets.

## What this project shows
- Clean project structure (data / notebooks)
- Survival modeling workflow (EDA → Modeling → Evaluation)
- Ethical handling of health data (no raw patient-level data shared)

## Methods
- Kaplan–Meier exploration (EDA notebook)
- Cox Proportional Hazards (interpretable hazard ratios)
- Random Survival Forest (non-linear ML survival model)

## Evaluation (planned / included as data allows)
- Concordance Index (C-index)
- Risk stratification and survival curves
- Calibration (optional)

## Repository structure
```text
Survival-analysis-in-health-data/
├── data/        # Data description and access instructions (no raw data uploaded)
├── notebooks/   # 01_eda.ipynb, 02_modeling.ipynb (+ evaluation later)
├── README.md
└── .gitignore
