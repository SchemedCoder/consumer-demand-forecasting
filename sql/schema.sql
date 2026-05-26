CREATE TABLE dim_product (
    product_id BIGINT PRIMARY KEY,
    product_name VARCHAR(255),
    category VARCHAR(100),
    brand VARCHAR(100)
);

CREATE TABLE dim_store (
    store_id BIGINT PRIMARY KEY,
    store_name VARCHAR(255),
    city VARCHAR(100),
    region VARCHAR(100)
);

CREATE TABLE sales_raw (
    sale_id BIGINT,
    product_id BIGINT,
    store_id BIGINT,
    qty INTEGER,
    unit_price NUMERIC(10,2),
    sale_date DATE,
    ingest_time TIMESTAMP
);

CREATE TABLE sales_clean (
    sale_id BIGINT PRIMARY KEY,
    product_id BIGINT,
    store_id BIGINT,
    qty INTEGER,
    revenue NUMERIC(10,2),
    sale_date DATE,
    ingest_time TIMESTAMP
);

CREATE TABLE late_arrival_audit (
    sale_id BIGINT,
    sale_date DATE,
    ingest_time TIMESTAMP,
    delay_days INTEGER
);

CREATE TABLE daily_product_sales (
    sale_date DATE,
    product_id BIGINT,
    total_qty INTEGER,
    total_revenue NUMERIC(12,2)
);
