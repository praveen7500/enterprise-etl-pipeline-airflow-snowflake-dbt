"""
Enterprise ETL Pipeline
Author: Praveen I

Workflow:
Extract CSV
    ↓
Validate Data
    ↓
Transform Data
    ↓
Upload to AWS S3
    ↓
Load to Snowflake
"""

from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

from airflow_config import default_args
from helper import execute_python

from notifications.slack import send_slack
from notifications.sns import send_sns
from notifications.email import send_email


# -------------------------------------------------------
# Failure Notification Callback
# -------------------------------------------------------

def notify_failure(context):
    """
    Trigger Slack, SNS and Email notifications
    whenever a task fails.
    """

    task = context["task_instance"].task_id
    dag = context["dag"].dag_id
    execution_time = context["logical_date"]

    message = f"""
❌ Enterprise ETL Pipeline Failed

DAG : {dag}

Task : {task}

Execution Time : {execution_time}

Please check the Airflow logs.
"""

    try:
        send_slack(message)
    except Exception as e:
        print(f"Slack notification failed: {e}")

    try:
        send_sns(
            "Enterprise ETL Pipeline Failed",
            message
        )
    except Exception as e:
        print(f"SNS notification failed: {e}")

    try:
        send_email(
            "Enterprise ETL Pipeline Failed",
            message
        )
    except Exception as e:
        print(f"Email notification failed: {e}")


# -------------------------------------------------------
# DAG Definition
# -------------------------------------------------------

with DAG(

    dag_id="enterprise_etl_pipeline",

    description="Enterprise ETL Pipeline using Airflow, Snowflake, AWS S3 and dbt",

    default_args=default_args,

    schedule="@daily",

    start_date=datetime(2026, 1, 1),

    catchup=False,

    tags=[
        "ETL",
        "Snowflake",
        "AWS",
        "dbt",
        "Data Engineering"
    ],

    on_failure_callback=notify_failure

) as dag:

    # --------------------------------------------
    # Extract
    # --------------------------------------------

    extract = PythonOperator(

        task_id="extract",

        python_callable=execute_python,

        op_args=["scripts/extract.py"],

        on_failure_callback=notify_failure

    )

    # --------------------------------------------
    # Validate
    # --------------------------------------------

    validate = PythonOperator(

        task_id="validate",

        python_callable=execute_python,

        op_args=["scripts/validate.py"],

        on_failure_callback=notify_failure

    )

    # --------------------------------------------
    # Transform
    # --------------------------------------------

    transform = PythonOperator(

        task_id="transform",

        python_callable=execute_python,

        op_args=["scripts/transform.py"],

        on_failure_callback=notify_failure

    )

    # --------------------------------------------
    # Upload to AWS S3
    # --------------------------------------------

    upload = PythonOperator(

        task_id="upload_to_s3",

        python_callable=execute_python,

        op_args=["scripts/upload_to_s3.py"],

        on_failure_callback=notify_failure

    )

    # --------------------------------------------
    # Load into Snowflake
    # --------------------------------------------

    snowflake = PythonOperator(

        task_id="load_to_snowflake",

        python_callable=execute_python,

        op_args=["scripts/load_to_snowflake.py"],

        on_failure_callback=notify_failure

    )

    # -------------------------------------------------
    # Workflow
    # -------------------------------------------------

    extract >> validate >> transform >> upload >> snowflake
