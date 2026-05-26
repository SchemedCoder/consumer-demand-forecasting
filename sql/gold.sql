INSERT INTO daily_product_sales
(
    sale_date,
    product_id,
    total_qty,
    total_revenue
)
SELECT
    sale_date,
    product_id,
    SUM(qty),
    SUM(revenue)
FROM sales_clean
GROUP BY
    sale_date,
    product_id;
