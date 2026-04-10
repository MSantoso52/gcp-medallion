from airflow import DAG
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from datetime import datetime

with DAG(
    'ingest_sales_to_bronze',
    start_date=datetime(2026, 1, 1),
    schedule_interval=None,
    catchup=False
) as dag:

    load_csv_to_bronze = GCSToBigQueryOperator(
        task_id='load_sales_csv',
        bucket='landing-data-lake',
        source_objects=['sales_data.csv'],
        destination_project_dataset_table='gcp-medallion.bronze_layer.raw_sales',
        write_disposition='WRITE_APPEND', # Append new data
        source_format='CSV',
        skip_leading_rows=1,
        autodetect=True
    )

