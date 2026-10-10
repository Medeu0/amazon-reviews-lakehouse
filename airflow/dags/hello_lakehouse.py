from datetime import datetime

from airflow.sdk import DAG, task


with DAG(
    dag_id="hello_lakehouse",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["learning"],
):

    @task
    def hello():
        print("Hello from the Amazon Reviews Lakehouse project!")

    hello()
