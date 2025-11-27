import pandas as pd
import matplotlib.pyplot as plt
import os

PROCESSED_PATH = "data/processed/employee_processed.csv"
OUTPUT_DIR = "outputs/"

def analyze_data():
    print("📊 Loading processed dataset...")
    df = pd.read_csv(PROCESSED_PATH)

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Chart 1: Performance Score
    plt.figure(figsize=(10,5))
    plt.plot(df['employee_id'], df['performance_score'])
    plt.title("Employee Performance Score")
    plt.xlabel("Employee ID")
    plt.ylabel("Performance Score")
    plt.savefig(OUTPUT_DIR + "performance_chart.png")

    # Chart 2: Productivity Index
    plt.figure(figsize=(10,5))
    plt.bar(df['employee_id'], df['productivity_index'])
    plt.title("Productivity Index")
    plt.xlabel("Employee ID")
    plt.ylabel("Index")
    plt.savefig(OUTPUT_DIR + "productivity_chart.png")

    print("✅ Charts saved in 'outputs/' folder")

if __name__ == "__main__":
    analyze_data()
