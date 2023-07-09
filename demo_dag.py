# from datetime import datetime

# from airflow import DAG
# from airflow.decorators import task
# from airflow.operators.bash import BashOperator

# # A DAG represents a workflow, a collection of tasks
# with DAG(dag_id="demo", start_date=datetime(2023, 7, 9), schedule="0 0 * * *") as dag:

#     # Tasks are represented as operators
#     hello = BashOperator(task_id="hello", bash_command="echo hello")

#     @task()
#     def airflow():
#         print("airflow")

#     # Set dependencies between tasks
#     hello >> airflow()


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