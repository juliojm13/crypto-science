from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator


def hello():
    print('Lets go Crypto-Science!')


with DAG(dag_id='hello_test_dag',
         start_date=datetime(2021, 1, 1),
         schedule_interval='@hourly',
         catchup=False) as dag:
    task1 = PythonOperator(
        task_id='hello_test_task',
        python_callable=hello)
