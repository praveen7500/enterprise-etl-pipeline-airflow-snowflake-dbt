"""
Airflow Default Configuration

Author: Praveen I
Project: Enterprise ETL Pipeline using Airflow, Snowflake, dbt and AWS
"""

from datetime import timedelta

default_args = {

    # Owner
    "owner": "Data Engineering",

    # Dependencies
    "depends_on_past": False,

    # Email Settings
    "email_on_failure": False,
    "email_on_retry": False,

    # Retry Policy
    "retries": 2,
    "retry_delay": timedelta(minutes=5),

    # Execution Timeout
    "execution_timeout": timedelta(minutes=30),

    # Retry Exponential Backoff
    "retry_exponential_backoff": True,

    # Maximum Retry Delay
    "max_retry_delay": timedelta(minutes=15)
}
