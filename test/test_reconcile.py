import pandas as pd


def test_late_arrival_detection():

    df = pd.DataFrame(
        {
            "sale_date": ["2026-05-01"],
            "ingest_time": ["2026-05-05"]
        }
    )

    df["sale_date"] = pd.to_datetime(
        df["sale_date"]
    )

    df["ingest_time"] = pd.to_datetime(
        df["ingest_time"]
    )

    delay = (
        df["ingest_time"]
        - df["sale_date"]
    ).dt.days

    assert delay.iloc[0] == 4


def test_on_time_record():

    df = pd.DataFrame(
        {
            "sale_date": ["2026-05-01"],
            "ingest_time": ["2026-05-01"]
        }
    )

    df["sale_date"] = pd.to_datetime(
        df["sale_date"]
    )

    df["ingest_time"] = pd.to_datetime(
        df["ingest_time"]
    )

    delay = (
        df["ingest_time"]
        - df["sale_date"]
    ).dt.days

    assert delay.iloc[0] == 0
