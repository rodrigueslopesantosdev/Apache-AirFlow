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
    'start_date': datetime(2019, 12, 10, tzinfo=timeZone),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'end_date': datetime(2019, 12, 19, tzinfo=timeZone)
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}
#criando DAG
dag_python = DAG(
    'exec_python_script',
    catchup=False,
    schedule_interval='45 17 * * *',
    default_args=default_args
)

#criando taskSyncS3
taskCriarDiretorio = BashOperator(
    task_id='criar_diretorio',
    bash_command="""
        cd /usr/local/airflow/dags/scripts_tasks
        python criarDiretorio.py
    """,
    dag=dag_python
)

#criando taskLoadClientePfCarga
taskCopiarArquivo = BashOperator(
    task_id='copiar_arquivo',
    bash_command="""
        cd /usr/local/airflow/dags/scripts_tasks
        python copiarArquivo.py
    """,
    dag=dag_python
)

#criando relação entre as duas tarefas do DAG.
taskCriarDiretorio >> taskCopiarArquivo