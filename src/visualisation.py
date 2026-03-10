import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

SILVER = Path("silver")
VIS = Path("visualizations")

def generate_visualizations():

    VIS.mkdir(exist_ok=True)

    vitals = pd.read_csv(SILVER / "clean_vitals.csv")

    plt.figure()

    for pid, group in vitals.groupby("patient_id"):
        plt.plot(group["timestamp"], group["hr"], label=f"Patient {pid}")

    plt.legend()
    plt.title("Heart Rate Trend")
    plt.savefig(VIS / "hr_trend.png")

    plt.figure()
    plt.hist(vitals["ox"], bins=10)
    plt.axvline(92)
    plt.title("Oxygen Distribution")
    plt.savefig(VIS / "oxygen_distribution.png")

    print("Visualizations created")