import os
import json
import pendulum

from dotenv import load_dotenv
from asyncio import tasks
from textwrap import dedent

from airflow import DAG
from airflow.operators.python import PythonOperator

from Threat_Lens.Pipeline.Training_Pipeline import TLTrainingPipeline

load_dotenv()

with DAG(
  'ThreatLens',
  default_args = {'retries' : 2},
  description = 'Threat Lens Pipeline',
  schedule_interval = "@weekly",
  start_date = pendulum.datetime(2024, 9, 17, tz = "UTC"),
  catchup = False,
  tags = ['example']
) as dag:
  
  def Training(**kwargs):
    TrnObj = TLTrainingPipeline()
    TrnObj.Run_Pipeline()

  def Sync_Artifact_to_S3Bucket(**kwargs):
    Bkt_name = os.getenv("BUCKET_NAME")
    os.system(f"aws s3 sync /App/Artifact s3://{Bkt_name}/Artifact")
    os.system(f"aws s3 sync /App/Saved_Moddels s3://{Bkt_name}/Saved_Models")

  Training_PL = PythonOperator(
    task_id = "train_PL",
    python_callable = Training
  )

  Sync_Data = PythonOperator(
    task_id = "sync_data2S3",
    python_callable = Sync_Artifact_to_S3Bucket
  )

  Training_PL >> Sync_Data
    