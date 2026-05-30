import os
import pandas as pd

RAW_FOLDER = "sample_data/sales"
OUTPUT_FILE = "data/extracted_sales.csv"


def extract_sales():

    os.makedirs("data", exist_ok=True)

    files = [
        os.path.join(RAW_FOLDER, file)
        for file in os.listdir(RAW_FOLDER)
        if file.endswith(".csv")
    ]

    if not files:
        raise Exception("No source files found")

    all_data = []

    for file in files:
        print(f"Reading {file}")

        df = pd.read_csv(file)

        all_data.append(df)

    final_df = pd.concat(all_data, ignore_index=True)

    final_df.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print(
        f"Extracted {len(final_df)} rows"
    )
