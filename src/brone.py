import pandas as pd
from pathlib import Path

DATA_PATH = Path("data")
BRONZE_PATH = Path("bronze")

def ingest_raw_data():

    BRONZE_PATH.mkdir(exist_ok=True)

    files = ["ehr.csv", "vitals.csv", "labs.csv"]

    for file in files:

        df = pd.read_csv(DATA_PATH / file)

        df.to_csv(BRONZE_PATH / file, index=False)

        print(f"Bronze layer created for {file}")