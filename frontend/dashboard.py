import streamlit as st
import pandas as pd

st.title("🏥 Hospital Analytics Dashboard")

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Page",
    ["Patient Data","Anomalies","Visualizations"]
)

if page == "Patient Data":

    df = pd.read_csv("silver/patient_master.csv")

    st.dataframe(df)

if page == "Anomalies":

    df = pd.read_csv("gold/anomalies.csv")

    st.dataframe(df)

if page == "Visualizations":

    st.image("visualizations/hr_trend.png")
    st.image("visualizations/oxygen_distribution.png")