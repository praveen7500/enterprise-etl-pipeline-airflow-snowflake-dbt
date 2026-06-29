from airflow import DAG

from airflow.operators.empty import EmptyOperator

from datetime import datetime

with DAG(

    dag_id="pipeline_monitor",

    schedule="@hourly",

    start_date=datetime(2026,1,1),

    catchup=False

) as dag:

    start = EmptyOperator(task_id="start")

    health = EmptyOperator(task_id="health_check")

    finish = EmptyOperator(task_id="finish")

    start >> health >> finish
