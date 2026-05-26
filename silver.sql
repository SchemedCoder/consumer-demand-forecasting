INSERT INTO sales_clean
(
    sale_id,
    product_id,
    store_id,
    qty,
    revenue,
    sale_date,
    ingest_time
)
SELECT
    sale_id,
    product_id,
    store_id,
    qty,
    qty * unit_price,
    sale_date,
    ingest_time
FROM sales_raw
WHERE qty > 0;
