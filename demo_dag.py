from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner":"laaziz",
    "retries":5,
    "retry_delay":timedelta(minutes=3)
}

with DAG(
    dag_id="first_dag",
    description="this is my first dag",
    default_args=default_args,
    start_date=datetime(2023, 7, 9), 
    schedule="0 0 * * *"
) as dag:
    t1 = BashOperator(
        task_id="first_task",
        bash_command="echo hello world this is my first task"
    )

    t2 = BashOperator(
        task_id = "second_task",
        bash_command="echo hii agian!! this the second task"
    )

    t1>>t2