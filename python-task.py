from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from math import factorial

def PascalTriangle():
    rows = 10
    for i in range(rows):
        for j in range(i+1):
            print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
        print()

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 8, 21),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'pascal',
    default_args=default_args,
    description='Pascal Triangle',
    schedule_interval='44 11 * * *',
    catchup=False,
)

task = PythonOperator(
    task_id='pascaltriangle',
    python_callable=PascalTriangle,
    dag=dag,
)
