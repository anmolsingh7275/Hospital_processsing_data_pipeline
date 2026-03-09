import pandas as pd
from pathlib import Path

BRONZE = Path("bronze")
SILVER = Path("silver")

def process_silver():

    SILVER.mkdir(exist_ok=True)

    ehr = pd.read_csv(BRONZE / "ehr.csv")
    vitals = pd.read_csv(BRONZE / "vitals.csv")
    labs = pd.read_csv(BRONZE / "labs.csv")

    vitals = vitals.rename(columns={"patientId":"patient_id"})
    labs = labs.rename(columns={
        "patientId":"patient_id",
        "test":"lab_test",
        "value":"lab_value"
    })

    vitals["timestamp"] = pd.to_datetime(vitals["timestamp"], unit="s")
    labs["timestamp"] = pd.to_datetime(labs["timestamp"], unit="s")

    vitals_latest = (
        vitals.sort_values("timestamp")
        .groupby("patient_id")
        .tail(1)
    )

    labs_latest = (
        labs.sort_values("timestamp")
        .groupby(["patient_id","lab_test"])
        .tail(1)
    )

    patient_master = ehr.merge(vitals_latest, on="patientId", how="left")

    vitals_latest.to_csv(SILVER / "clean_vitals.csv", index=False)
    labs_latest.to_csv(SILVER / "clean_labs.csv", index=False)
    patient_master.to_csv(SILVER / "patient_master.csv", index=False)

    print("Silver layer created")