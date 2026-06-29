from airflow import DAG

from airflow.operators.python import PythonOperator

from datetime import datetime

from airflow_config import default_args

from helper import execute_python

with DAG(

    dag_id="enterprise_etl_pipeline",

    default_args=default_args,

    schedule="@daily",

    start_date=datetime(2026,1,1),

    catchup=False,

    tags=["ETL","Snowflake","AWS"]

) as dag:

    extract = PythonOperator(

        task_id="extract",

        python_callable=execute_python,

        op_args=["scripts/extract.py"]

    )

    validate = PythonOperator(

        task_id="validate",

        python_callable=execute_python,

        op_args=["scripts/validate.py"]

    )

    transform = PythonOperator(

        task_id="transform",

        python_callable=execute_python,

        op_args=["scripts/transform.py"]

    )

    upload = PythonOperator(

        task_id="upload_s3",

        python_callable=execute_python,

        op_args=["scripts/upload_to_s3.py"]

    )

    snowflake = PythonOperator(

        task_id="load_snowflake",

        python_callable=execute_python,

        op_args=["scripts/load_to_snowflake.py"]

    )

    extract >> validate >> transform >> upload >> snowflake
