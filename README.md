🏥 Hospital Data Pipeline

A Python-based data engineering pipeline that processes hospital data using a Bronze → Silver → Gold architecture and generates analytics dashboards and visualizations.

This project demonstrates data ingestion, cleaning, transformation, anomaly detection, and visualization using a structured pipeline similar to modern data lake architectures used by companies like Uber, Netflix, and Amazon.

📌 Project Overview

Hospitals generate large amounts of data including:

Electronic Health Records (EHR)

Patient vital signs

Lab test results

However, this data is often:

messy

inconsistent

stored in different formats

difficult to analyze

This pipeline processes the raw data and produces clean analytics-ready datasets and visual insights.

🧱 Pipeline Architecture

The project follows a 3-layer data pipeline architecture.

Raw Data
   ↓
Bronze Layer (Raw ingestion)
   ↓
Silver Layer (Data cleaning & standardization)
   ↓
Gold Layer (Analytics & anomaly detection)
   ↓
Visualizations & Dashboard
📂 Project Structure
hospital_data_pipeline/
│
├── data/                  # Raw input files
│   ├── ehr.csv
│   ├── vitals.csv
│   └── labs.csv
│
├── bronze/                # Raw ingested data
├── silver/                # Cleaned datasets
├── gold/                  # Analytics results
│
├── visualizations/        # Generated charts
│
├── src/                   # Pipeline modules
│   ├── bronze.py
│   ├── silver.py
│   ├── gold.py
│   ├── visualize.py
│   └── utils.py
│
├── frontend/              # Streamlit dashboard
│   └── dashboard.py
│
├── main.py                # Pipeline orchestrator
├── requirements.txt
└── README.md
📊 Data Sources

The pipeline processes three input datasets.

1️⃣ ehr.csv

Electronic Health Records.

patientId,name,age,gender
101,John,45,M
102,Sarah,38,F

Contains basic patient information.

2️⃣ vitals.csv

Patient vital signs recorded over time.

patientId,timestamp,hr,ox,sys,dia
101,1712000000,80,97,120,80
102,1712001000,130,88,170,110
Column	Description
hr	Heart Rate
ox	Oxygen Level
sys	Systolic Blood Pressure
dia	Diastolic Blood Pressure
3️⃣ labs.csv

Lab test results.

patientId,timestamp,test,value
101,1712002000,glucose,120
101,1712003000,cholesterol,200
🥉 Bronze Layer (Raw Data Ingestion)

Purpose:

Store exact copies of raw data

Preserve original data for auditing

No transformations applied

Example:

data/ehr.csv → bronze/ehr.csv
🥈 Silver Layer (Data Cleaning & Standardization)

The silver layer prepares data for analytics.

Key Transformations

✔ Rename inconsistent columns

patientId → patient_id
test → lab_test
value → lab_value

✔ Convert timestamps

UNIX timestamp → datetime

✔ Ensure numeric data types

hr, ox, sys, dia, lab_value

✔ Select latest records per patient

✔ Create patient_master table

patient_id | name | hr | ox | sys | glucose | cholesterol
🥇 Gold Layer (Anomaly Detection)

Detects potential health issues using predefined rules.

Detection Rules

High Heart Rate

HR > 120 bpm

Low Oxygen

OX < 92%

High Blood Pressure

SYS > 160 OR DIA > 100

Detected anomalies are stored in:

gold/anomalies.csv
📈 Visualizations

The pipeline generates three charts automatically.

1️⃣ Heart Rate Trend
visualizations/hr_trend.png

Shows heart rate trends over time for each patient.

2️⃣ Oxygen Distribution
visualizations/oxygen_distribution.png

Histogram showing oxygen level distribution with a 92% risk threshold.

3️⃣ Anomaly Counts
visualizations/anomaly_counts.png

Bar chart showing counts of detected anomalies.

🖥 Streamlit Dashboard

The project includes a Streamlit dashboard for interactive analytics.

Dashboard features:

View patient master dataset

Display anomaly records

Show generated visualizations

Explore hospital data insights

Run dashboard:

streamlit run frontend/dashboard.py
⚙️ Installation

Clone the repository:

git clone https://github.com/yourusername/hospital-data-pipeline.git
cd hospital-data-pipeline

Create virtual environment:

python -m venv .venv

Activate environment:

Windows

.venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt
▶️ Running the Pipeline

Run the full pipeline:

python main.py

Pipeline steps:

1️⃣ Bronze ingestion
2️⃣ Silver data cleaning
3️⃣ Gold anomaly detection
4️⃣ Visualization generation

📊 Running the Dashboard
streamlit run frontend/dashboard.py

Open in browser:

http://localhost:8501
🔁 Re-runnable Pipeline

The pipeline is fully idempotent.

Running multiple times will:

read fresh data

overwrite outputs

regenerate visualizations

produce consistent results

👥 Team Collaboration

Project development follows modular ownership.

Module	Responsible
bronze.py	Member 1
silver.py	Member 2
gold.py	Member 3
visualize.py	Member 4
frontend & integration	Project Lead

Each member works on separate Git branches and creates Pull Requests.

🛠 Tech Stack

Python

Pandas

NumPy

Matplotlib

Streamlit

Git & GitHub

🚀 Future Improvements

Possible upgrades:

Real-time streaming pipeline

Airflow orchestration

PostgreSQL data warehouse

Interactive Plotly dashboards

ML-based health prediction models