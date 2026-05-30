import pandas as pd

from api.database import engine


def get_top_products():

    query = """
    SELECT
        product_id,
        SUM(total_qty) qty
    FROM daily_product_sales
    GROUP BY product_id
    ORDER BY qty DESC
    LIMIT 10
    """

    return pd.read_sql(
        query,
        engine
    )


def get_product(product_id):

    query = f"""
    SELECT *
    FROM daily_product_sales
    WHERE product_id={product_id}
    """

    return pd.read_sql(
        query,
        engine
    )
