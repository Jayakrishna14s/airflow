from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def say_hiii():
    print("hiii")

with DAG(
    dag_id="hiii_dag",  # Changed from hello_dag
    start_date=datetime(2023, 1, 1),
    schedule_interval=None,  # Manual trigger only
    catchup=False,
    tags=["example"],
) as dag:

    task = PythonOperator(
        task_id="print_hiii",
        python_callable=say_hiii,
    )
