from src.bronze import ingest_raw_data
from src.silver import process_silver
from src.gold import detect_anomalies
from src.visualize import generate_visualizations

def run_pipeline():

    print("Starting pipeline")

    ingest_raw_data()
    process_silver()
    detect_anomalies()
    generate_visualizations()

    print("Pipeline completed")

if __name__ == "__main__":
    run_pipeline()