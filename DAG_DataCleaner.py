#bibliotecas do Apache AirFlow
import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
#biblioteca para configurar o timezone
import pendulum

#fuso horário Brasil/Sao Paulo
timeZone = pendulum.timezone("America/Sao_Paulo")

#parâmetros padrões do DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2019, 12, 9, tzinfo=timeZone),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}
#criando DAG
dag_python = DAG(
    'exec_python_script',
    catchup=False,
    schedule_interval='15 16 * * *',
    default_args=default_args
)

#executando DataCleaner
taskDataCleaner = BashOperator(
    task_id='executando_Data_Cleaner',
    bash_command="""
        cd /usr/local/airflow/dags/scripts_tasks
        python executaDataCleaner.py
    """,
    dag=dag_python
)

#criando relação entre as duas tarefas do DAG.
taskDataCleaner