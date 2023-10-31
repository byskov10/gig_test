from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner' : 'airflow',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='our_first_dag',
    default_args=default_args,
    start_date=datetime(2023, 11, 1),
    schedule_interval='@hourly'
) as dag:
    task1 = BashOperator(
        task_id = 'first_task',
        bash_command = "ecco hello world, this is the first task!"
    )
    task1