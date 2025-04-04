import sys
import os

# Add the directory where the modules are located
sys.path.append(os.path.join(os.path.dirname(__file__), "Weather-data-pipeline"))

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from extraction import extract_data_from_api
from transformation import clean_and_transform
from loading import load_to_sqlite
from config import API_KEY, API_URL, REQUEST_CITY, DB_PATH

# Define default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 4, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
with DAG(
    'weather_data_pipeline',
    default_args=default_args,
    description='ETL pipeline for weather data using Apache Airflow',
    schedule_interval=timedelta(hours=1),  # Runs every hour
    catchup=False,
) as dag:
    
    extract_task = PythonOperator(
    task_id='extract_data_from_api',
    python_callable=extract_data_from_api,
    op_kwargs={
        'api_url': API_URL,
        'api_key': API_KEY,
        'request_city': REQUEST_CITY
    },
    dag=dag
    )
    
    transform_task = PythonOperator(
        task_id='clean_and_transform',
        python_callable=clean_and_transform,
        provide_context=True,
    dag=dag
    )
    
    load_task = PythonOperator(
        task_id='load_to_sqlite',
        python_callable=load_to_sqlite,
        provide_context=True,
        op_kwargs={
        'db_path': DB_PATH ,
    },
    )
    
    # Define task dependencies
    extract_task >> transform_task >> load_task

