# dags/salary_pipeline_dag.py
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from scripts.preprocess import run_preprocessing
from scripts.train import run_training

default_args = {
    'owner': 'kavya',
    'start_date': datetime(2025, 7, 1),
    'retries': 1,
}

with DAG("salary_prediction_pipeline",
         default_args=default_args,
         schedule_interval="@daily",
         catchup=False,
         tags=["ml", "salary", "pipeline"]) as dag:

    task_preprocess = PythonOperator(
        task_id="preprocess_data",
        python_callable=run_preprocessing
    )

    task_train = PythonOperator(
        task_id="train_model",
        python_callable=run_training
    )

    task_preprocess >> task_train
