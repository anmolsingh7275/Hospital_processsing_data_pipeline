import streamlit as st
import pandas as pd
from pathlib import Path

st.title("🏥 Hospital Analytics Dashboard")

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Page",
    ["Patient Data","Anomalies","Visualizations"]
)

if page == "Patient Data":

    path = Path("silver/patient_master.csv")

    if path.exists():
        df = pd.read_csv(path)
        st.dataframe(df)
    else:
        st.warning("Run pipeline first to generate data")

if page == "Anomalies":

    path = Path("gold/anomalies.csv")

    if path.exists():
        df = pd.read_csv(path)
        st.dataframe(df)
    else:
        st.warning("Run pipeline first")

if page == "Visualizations":

    if Path("visualizations/hr_trend.png").exists():
        st.image("visualizations/hr_trend.png")

    if Path("visualizations/oxygen_distribution.png").exists():
        st.image("visualizations/oxygen_distribution.png")