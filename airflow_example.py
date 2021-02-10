from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator

dag = DAG(dag_id="car_factory",
          default_args={"owner": "airflow",
          "start_date": airflow.utils.dates.days_ago(2)},
          schedule_interval="0 * * * *"  # every 0 min on the hour, see https://crontab.guru
          )

# cron
# .------------------------- minute (0 - 59)
# | .----------------------- hour(0 - 23)
# | | .--------------------- day of the month (1 - 31)
# | | | .------------------- month            (1 - 12)
# | | | | .----------------- day of the week  (0 - 6)
# * * * * * <command># Example0 * * * * # Every hour at the 0th minute

# Task definitions
assemble_frame = BashOperator(task_id="assemble_frame", bash_command='echo "Assembling frame"', dag=dag)
place_tires = BashOperator(task_id="place_tires", bash_command='echo "Placing tires"', dag=dag)
assemble_body = BashOperator(task_id="assemble_body", bash_command='echo "Assembling body"', dag=dag)
apply_paint = BashOperator(task_id="apply_paint", bash_command='echo "Applying paint"', dag=dag)

# Complete the downstream flow
assemble_frame.set_downstream(place_tires)
assemble_frame.set_downstream(assemble_body)
assemble_body.set_downstream(apply_paint)



# ex2

from airflow.operators.python_operator import PythonOperator

# Define the ETL function
def etl():
    film_df = extract_film_to_pandas()
    film_df = transform_rental_rate(film_df)
    return load_dataframe_to_film(film_df)

# Define the ETL task using PythonOperator
etl_task = PythonOperator(task_id='etl_film',
                          python_callable=etl,
                          dag=dag)

# Set the upstream to wait_for_table and sample run etl()
etl_task.set_upstream(wait_for_table)
etl()
