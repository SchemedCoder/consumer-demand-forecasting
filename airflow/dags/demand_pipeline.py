from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

from etl.extract import extract_sales
from etl.transform import transform_sales
from etl.load import (
    load_bronze,
    load_silver,
    build_gold
)

default_args = {
    "owner": "navin",
    "depends_on_past": False,
    "email_on_failure": False,
    "retries": 2,
    "retry_delay": timedelta(minutes=2)
}

with DAG(
    dag_id="consumer_demand_pipeline",
    default_args=default_args,
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["retail", "etl", "forecasting"]
) as dag:

    extract_task = PythonOperator(
        task_id="extract_sales",
        python_callable=extract_sales
    )

    transform_task = PythonOperator(
        task_id="transform_sales",
        python_callable=transform_sales
    )

    bronze_task = PythonOperator(
        task_id="load_bronze",
        python_callable=load_bronze
    )

    silver_task = PythonOperator(
        task_id="load_silver",
        python_callable=load_silver
    )

    gold_task = PythonOperator(
        task_id="build_gold",
        python_callable=build_gold
    )

    extract_task >> transform_task >> bronze_task >> silver_task >> gold_task
