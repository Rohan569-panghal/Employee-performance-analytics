import pandas as pd
from datetime import datetime
import os

# CSV file path
RAW_PATH = "data/raw/employee_data.csv"
PROCESSED_PATH = "data/processed/employee_processed.csv"

def process_data():
    print("🔄 Loading raw dataset...")
    df = pd.read_csv(RAW_PATH)   # <-- FIXED

    # Convert dates
    df['hire_date'] = pd.to_datetime(df['hire_date'])
    df['exit_date'] = pd.to_datetime(df['exit_date'], errors='coerce')

    # Add new columns
    today = datetime.today()
    df['tenure_years'] = ((df['exit_date'].fillna(today)) - df['hire_date']).dt.days / 365
    df['tenure_years'] = df['tenure_years'].round(1)
    df['is_active'] = df['exit_date'].isna().astype(int)

    os.makedirs("data/processed", exist_ok=True)
    df.to_csv(PROCESSED_PATH, index=False)

    print("✅ Processed data saved to:", PROCESSED_PATH)

if __name__ == "__main__":
    process_data()
