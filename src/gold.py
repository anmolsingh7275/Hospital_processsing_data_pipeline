import pandas as pd
from pathlib import Path

SILVER = Path("silver")
GOLD = Path("gold")

def detect_anomalies():

    GOLD.mkdir(exist_ok=True)

    df = pd.read_csv(SILVER / "patient_master.csv")

    anomalies = []

    for _, row in df.iterrows():

        if row["hr"] > 120:
            anomalies.append((row["patient_id"], "High Heart Rate"))

        if row["ox"] < 92:
            anomalies.append((row["patient_id"], "Low Oxygen"))

        if row["sys"] > 160 or row["dia"] > 100:
            anomalies.append((row["patient_id"], "High Blood Pressure"))

    anomalies_df = pd.DataFrame(anomalies, columns=["patient_id","anomaly"])

    anomalies_df.to_csv(GOLD / "anomalies.csv", index=False)

    print("Gold layer anomaly detection complete")