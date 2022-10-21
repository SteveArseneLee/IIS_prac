# Airflow
```py
from datetime import datetime

from airflow import DAG
from airflow.providers.apache.spark.operators.spark_sql import SparkSqlOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

default_args = {
  'start_date': datetime(2021, 1, 1),
}

filepath = "파일경로"

with DAG(dag_id='spark-example',
         schedule_interval='@daily',
         default_args=default_args,
         tags=['spark'],
         catchup=False) as dag:
  
  # sql_job = SparkSqlOperator(sql="SELECT * FROM bar", master="local", task_id="sql_job")

  submit_job = SparkSubmitOperator(
      application=filepath,
      # 먼저 airflow webserver에서 conn_id를 생성해주고 Type은 알맞게 지정해준다
      task_id="submit_job", conn_id="spark_local"
  )
```

```sh
airflow webserver
airflow scheduler
```
후 **localhost:8080**으로 접속

