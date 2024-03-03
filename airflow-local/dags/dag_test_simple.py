from airflow.models import DAG
from datetime import datetime
from datetime import timedelta
from airflow.operators.bash_operator import BashOperator
from airflow.models import Variable

weather_dir = Variable.get("weather_dir")

default_args = {
    'owner': 'Fidias',
    'depends_on_past': False,
    'email': ['fidiasierides@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'start_date': datetime(2024, 1, 1),  # If you set a datetime previous to the curernt date, it will try to backfill
    'retry_delay': timedelta(minutes=5),
    'end_date': datetime(2025, 1, 1),
}
with DAG(dag_id='test_dag',
         default_args=default_args,
         schedule_interval='*/1 * * * *',
         catchup=False,
         tags=['test']
         ) as dag:
    # Define the tasks. Here we are going to define only one bash operator
    test_task = BashOperator(
        task_id='write_date_file',
        bash_command=f'cd {weather_dir} && date >> ai_core.txt',
        dag=dag)
