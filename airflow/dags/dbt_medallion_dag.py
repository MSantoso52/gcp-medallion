# dags/dbt_medallion_dag.py

import os
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

DBT_PROJECT_DIR = os.getenv('DBT_PROJECT_DIR', '/opt/airflow/dbt_project')
DBT_CMD = f'docker compose -f /home/mulyo/Docker/gcp_dbt/docker-compose.yml run --rm dbt'

default_args = {
    'owner': 'mulyo',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='dbt_medallion_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    start_date=datetime(2026, 4, 1),
    catchup=False,
    tags=['dbt', 'medallion'],
) as dag:

    # ✅ Always run deps first to ensure packages are installed
    dbt_deps = BashOperator(
        task_id='dbt_deps',
        bash_command=f'{DBT_CMD} deps',
    )

    run_stg_sales = BashOperator(
        task_id='run_stg_sales',
        bash_command=f'{DBT_CMD} run --select stage_sales',
    )

    test_stg_sales = BashOperator(
        task_id='test_stage_sales',
        bash_command=f'{DBT_CMD} test --select stage_sales',
    )

    run_fact_daily = BashOperator(
        task_id='run_category_sales_daily',
        bash_command=f'{DBT_CMD} run --select category_sales_daily',
    )

    test_fact_daily = BashOperator(
        task_id='test_category_sales_daily',
        bash_command=f'{DBT_CMD} test --select category_sales_daily',
    )

    dbt_deps >> run_stg_sales >> test_stg_sales >> run_fact_daily >> test_fact_daily
