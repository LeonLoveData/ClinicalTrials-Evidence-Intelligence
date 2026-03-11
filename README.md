# ClinicalTrials Evidence Intelligence

A data-driven evidence intelligence project built on real **ClinicalTrials.gov** data.  
The goal is to demonstrate the ability to search and transform clinical trial information into **actionable insights** for research, regulatory strategy, and medical decision-making.

This project focuses on four core analytical capabilities:

1. **Trial Trend Analysis** – understanding how clinical trial activity evolves over time  
2. **Semantic Search (NLP)** – retrieving relevant trials using embedding-based similarity  
3. **Inclusion Model (ML)** – identifying high-value trials for a research question  
4. **Evidence Gap Analysis** – highlighting where evidence is weak or missing  

The project simulates how a modern evidence intelligence system supports scientific and strategic decisions.

---

## 1. Dataset Overview

The dataset consists of **164 real clinical trials** retrieved from ClinicalTrials.gov, filtered by:

- Cardiovascular-related conditions  
- Device-based interventions  

Each record includes:

- Study design  
- Enrollment  
- Status  
- Eligibility criteria  
- Intervention and condition metadata  
- Start and completion dates  

---

## 2. Trial Trend Analysis

Clinical trial activity often reflects scientific interest, regulatory focus, and investment patterns.  
This module extracts the **start year** of each trial and visualizes the number of trials initiated annually.

### Example Visualization

![Trial Count Trend](figures/trial_count_trend.png)

This helps identify:

- Growth or decline in research activity  
- Shifts in therapeutic focus  
- Potential saturation or emerging opportunities  

---

## 3. Semantic Search (Embedding-Based Retrieval)

A SentenceTransformer model converts each trial into a vector representation.  
This enables natural-language search such as:

> “device-based diagnostic accuracy studies in heart failure”

### Example Output

![Embedding Search Example](figures/embedding_search_example.png)

This capability forms the foundation of an **AI evidence assistant**, enabling rapid retrieval of relevant trials without manual keyword tuning.

---

## 4. Inclusion Model (Machine Learning)

A lightweight ML classifier predicts whether a trial should be **included** for a specific research question.

Features include:

- Enrollment  
- Study type  
- Presence of structured outcome fields  

Labels are generated using a **pseudo-labeling strategy**, simulating expert screening behavior.

### Model Performance

![Inclusion Model Performance](figures/inclusion_model_performance.png)

This demonstrates the ability to automate early-stage trial screening and prioritize high-value evidence.

---

## 5. Evidence Gap Analysis

This module identifies structural weaknesses in the evidence landscape, such as:

- Low enrollment  
- Limited number of completed trials  
- Sparse evidence in specific conditions  

### Example Summary

![Evidence Gap Summary](figures/evidence_gap_summary.png)

These insights support:

- Regulatory planning  
- Portfolio strategy  
- Clinical development prioritization  
- Risk assessment  

---

## 6. Project Highlights

- Uses **real-world clinical trial data**  
- Demonstrates **NLP, ML, and evidence synthesis** capabilities  
- Produces **clear visual insights** suitable for scientific and strategic audiences  
- Organized as a **production-style repository** with modular components  
- Easily extensible into a full **evidence intelligence platform**  

---

## 7. Potential Extensions

- Add PICO extraction  
- Add sponsor-level competitive landscape  
- Build a RAG-based clinical evidence assistant  
- Integrate trial results from additional registries  
- Add device-specific evidence mapping  

---

## 8. Figures

All figures used in this README are located in:

