from datetime import timedelta

default_args = {

    "owner": "Data Engineering",

    "depends_on_past": False,

    "email_on_failure": False,

    "email_on_retry": False,

    "retries": 2,

    "retry_delay": timedelta(minutes=5)
}
