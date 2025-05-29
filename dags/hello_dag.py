from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def say_hello():
    print("hello")

with DAG(
    dag_id="hello_dag",
    start_date=datetime(2025, 5, 29),
    schedule_interval=None,  
    catchup=False,
    tags=["example"],
) as dag:

    task = PythonOperator(
        task_id="print_hello",
        python_callable=say_hello,
    )
