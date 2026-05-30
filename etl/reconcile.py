import pandas as pd
from sqlalchemy import create_engine

DB_USER = "postgres"
DB_PASSWORD = "postgres"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "consumer_demand"

engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

REPROCESS_WINDOW_DAYS = 7


def identify_late_arrivals():

    query = """
    SELECT
        sale_id,
        sale_date,
        ingest_time,
        (ingest_time::date - sale_date) AS delay_days
    FROM sales_raw
    WHERE
        (ingest_time::date - sale_date) > 1
    """

    df = pd.read_sql(query, engine)

    df.to_sql(
        "late_arrival_audit",
        engine,
        if_exists="replace",
        index=False
    )

    print(
        f"Found {len(df)} late-arriving records"
    )

    return len(df)


def reconcile_last_7_days():

    query = f"""
    DELETE FROM daily_product_sales
    WHERE sale_date >= CURRENT_DATE - INTERVAL '{REPROCESS_WINDOW_DAYS} day'
    """

    with engine.begin() as conn:
        conn.execute(query)

    rebuild_query = f"""
    SELECT
        sale_date,
        product_id,
        SUM(qty) total_qty,
        SUM(revenue) total_revenue
    FROM sales_clean
    WHERE sale_date >= CURRENT_DATE - INTERVAL '{REPROCESS_WINDOW_DAYS} day'
    GROUP BY sale_date, product_id
    """

    gold_df = pd.read_sql(
        rebuild_query,
        engine
    )

    gold_df.to_sql(
        "daily_product_sales",
        engine,
        if_exists="append",
        index=False
    )

    print(
        "Gold layer reconciled"
    )
