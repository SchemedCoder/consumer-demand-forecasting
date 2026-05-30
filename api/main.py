from fastapi import FastAPI
from sqlalchemy import create_engine
import pandas as pd

app = FastAPI(
    title="Consumer Demand API",
    version="1.0.0"
)

engine = create_engine(
    "postgresql://postgres:postgres@localhost:5432/consumer_demand"
)


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/sales")
def sales(limit: int = 100):

    query = f"""
    SELECT *
    FROM sales_clean
    LIMIT {limit}
    """

    df = pd.read_sql(query, engine)

    return df.to_dict(
        orient="records"
    )


@app.get("/top-products")
def top_products():

    query = """
    SELECT
        product_id,
        SUM(total_qty) qty
    FROM daily_product_sales
    GROUP BY product_id
    ORDER BY qty DESC
    LIMIT 10
    """

    df = pd.read_sql(
        query,
        engine
    )

    return df.to_dict(
        orient="records"
    )


@app.get("/late-arrivals")
def late_arrivals():

    query = """
    SELECT *
    FROM late_arrival_audit
    ORDER BY delay_days DESC
    """

    df = pd.read_sql(
        query,
        engine
    )

    return df.to_dict(
        orient="records"
    )


@app.get("/products/{product_id}")
def product(product_id: int):

    query = f"""
    SELECT *
    FROM daily_product_sales
    WHERE product_id={product_id}
    ORDER BY sale_date DESC
    """

    df = pd.read_sql(
        query,
        engine
    )

    return df.to_dict(
        orient="records"
    )
