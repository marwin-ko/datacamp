# DC

## Terms
- Directed Acyclic Graph (DAG): has a sect of nodes, directed edges, and no cycles.

## Parallel Computation Frameworks
- Spark
  - avoids disk writes (as opposed to Hadoop)
  - relies on resilient distributed datasets (RDD)
    - list of tuples 
    - transformation methods: .map(), .filter()
    - actions: .count(), first()


## Workflow scheduling Frameworks
- Linux's cron
- Luigi
- Apache Airflow
- Nextflow (for scientific workflows)






