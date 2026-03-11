# ClinicalTrials Evidence Intelligence

An AI-assisted analytics pipeline for **clinical trial discovery, evidence search, and research insight generation** using public ClinicalTrials.gov data.

This project demonstrates how modern data science and natural language embedding models can support **clinical research intelligence workflows**, including:

- Clinical trial trend analysis
- Semantic search across trial descriptions
- Machine learning–based study inclusion screening
- Evidence gap identification

The system integrates **data analysis, semantic search, and predictive modeling** into a reproducible Python pipeline.

---

# Project Overview

Clinical research teams often need to analyze large collections of clinical trials to identify:

- emerging therapeutic areas
- relevant studies for systematic reviews
- evidence gaps in clinical research
- trends in clinical trial activity

This project simulates a **research intelligence workflow** using structured ClinicalTrials.gov data.

The pipeline performs four main analyses:

1. Clinical trial trend analysis
2. Semantic trial search using embeddings
3. Machine learning–based inclusion prediction
4. Evidence gap detection

All analyses automatically generate figures for interpretation.

---

# Repository Structure
```
ClinicalTrials-Evidence-Intelligence
│
├── data
│ └── raw
│ └── clinicaltrials_real_data.csv
│
├── figures
│ ├── trial_count_trend.png
│ ├── embedding_search_example.png
│ ├── inclusion_model_performance.png
│ └── evidence_gap_summary.png
│
├── clinical_trials_evidence_pipeline.py
└── README.md
```

---

# Data Source

The project uses a structured dataset derived from **ClinicalTrials.gov public trial records**.

Example fields include:

- `nct_id`
- `conditions`
- `interventions`
- `study_type`
- `enrollment`
- `primary_outcomes`
- `start_date`

These variables enable both **structured analytics and semantic search across trial metadata**.

---

# Analytical Pipeline

The pipeline performs four analytical modules.

## 1. Clinical Trial Trend Analysis

The system extracts trial **start years** from ClinicalTrials.gov data and calculates the number of trials initiated each year.

Output:


figures/trial_count_trend.png


This visualization highlights **changes in research activity over time**.

---

## 2. Semantic Trial Search (Embedding-Based)

Trial conditions and interventions are combined into a searchable text field.

A sentence embedding model is used:


sentence-transformers/all-MiniLM-L6-v2


The pipeline performs **semantic similarity search** between a query and trial records.

Example query used in the script:


diagnostic accuracy device trials in heart failure


Top matching trials are returned and visualized.

Output:


figures/embedding_search_example.png


This demonstrates how **embedding search can support clinical evidence discovery**.

---

## 3. Study Inclusion Prediction Model

A simple machine learning model simulates **automated screening of clinical trials**.

Pseudo-labels are generated using three criteria:

- Enrollment size
- Presence of primary outcomes
- Study type (interventional vs observational)

Features used:


enrollment
has_primary
is_interventional


Model:


Logistic Regression


Performance is visualized using a **confusion matrix**.

Output:


figures/inclusion_model_performance.png


This module demonstrates how machine learning can assist **systematic review study selection**.

---

## 4. Evidence Gap Analysis

The pipeline analyzes **median enrollment sizes across clinical conditions**.

Conditions with the **lowest median enrollment** may indicate potential evidence gaps or under-studied areas.

Output:


figures/evidence_gap_summary.png


This analysis highlights **therapeutic areas where additional research may be needed**.

---

# Example Outputs

The pipeline automatically generates four visual outputs:
```
| Analysis | Output Figure |
|---|---|
| Trial Trend Analysis | `trial_count_trend.png` |
| Semantic Search Results | `embedding_search_example.png` |
| Inclusion Model Performance | `inclusion_model_performance.png` |
| Evidence Gap Analysis | `evidence_gap_summary.png` |
```
All outputs are saved to:


/figures


---

# Technology Stack

Python

Core libraries:

- pandas
- numpy
- matplotlib
- scikit-learn
- sentence-transformers

Machine learning components:

- Logistic Regression
- StandardScaler
- Sentence embeddings for semantic search

---

##Example Research Questions Supported

This pipeline can support questions such as:
- How has clinical trial activity changed over time?
- Which trials are most relevant to a specific research topic?
- Can machine learning help prioritize trials for systematic review?
- Which disease areas may have limited clinical evidence?

##Purpose of This Project

This project demonstrates how AI-assisted analytics and semantic search can support biomedical research intelligence workflows.

The goal is to illustrate practical applications of:
- clinical trial data analysis
- semantic evidence retrieval
- machine learning–assisted research screening
- evidence gap identification
within a reproducible data science pipeline.
