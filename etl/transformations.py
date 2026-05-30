import pandas as pd
import numpy as np

SOURCE_FILE = "data/extracted_sales.csv"
OUTPUT_FILE = "data/transformed_sales.csv"


def transform_sales():

    df = pd.read_csv(SOURCE_FILE)

    print(f"Rows before cleaning: {len(df)}")

    df = df.drop_duplicates(
        subset=["sale_id"]
    )

    df = df[df["qty"] > 0]

    df = df[
        df["product_id"].notnull()
    ]

    df["sale_date"] = pd.to_datetime(
        df["sale_date"]
    )

    df["ingest_time"] = pd.to_datetime(
        df["ingest_time"]
    )

    df["unit_price"] = (
        df["unit_price"]
        .astype(float)
    )

    df["qty"] = (
        df["qty"]
        .astype(int)
    )

    df["revenue"] = (
        df["qty"]
        * df["unit_price"]
    )

    today = pd.Timestamp.now()

    df = df[
        df["sale_date"] <= today
    ]

    df["arrival_delay_days"] = (
        df["ingest_time"]
        - df["sale_date"]
    ).dt.days

    df["is_late_arrival"] = np.where(
        df["arrival_delay_days"] > 1,
        True,
        False
    )

    print(
        f"Rows after cleaning: {len(df)}"
    )

    df.to_csv(
        OUTPUT_FILE,
        index=False
    )
