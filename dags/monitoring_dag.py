"""
Enterprise ETL Pipeline Monitoring DAG

Author: Praveen I

Description:
-------------
This DAG periodically checks the health of the ETL pipeline.

Current Checks
--------------
✔ Pipeline log availability

Future Enhancements
-------------------
✔ Snowflake connectivity
✔ AWS S3 health check
✔ dbt project validation
✔ Slack notifications
✔ AWS SNS notifications
✔ Email alerts
"""

from datetime import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator

from monitoring.health_check import pipeline_status


# -------------------------------------------------------
# Default Arguments
# -------------------------------------------------------

default_args = {

    "owner": "Data Engineering",

    "depends_on_past": False,

    "retries": 1

}


# -------------------------------------------------------
# DAG Definition
# -------------------------------------------------------

with DAG(

    dag_id="pipeline_monitor",

    description="Monitor Enterprise ETL Pipeline",

    default_args=default_args,

    schedule="@hourly",

    start_date=datetime(2026, 1, 1),

    catchup=False,

    tags=[
        "Monitoring",
        "Health Check",
        "ETL"
    ]

) as dag:

    # ---------------------------------------------------
    # Start
    # ---------------------------------------------------

    start = EmptyOperator(

        task_id="start"

    )

    # ---------------------------------------------------
    # Pipeline Health Check
    # ---------------------------------------------------

    health_check = PythonOperator(

        task_id="pipeline_health_check",

        python_callable=pipeline_status

    )

    # ---------------------------------------------------
    # Finish
    # ---------------------------------------------------

    finish = EmptyOperator(

        task_id="finish"

    )

    # ---------------------------------------------------
    # Workflow
    # ---------------------------------------------------

    start >> health_check >> finish
