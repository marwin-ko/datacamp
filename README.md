# DC

## Terms
- Directed Acyclic Graph (DAG): has a sect of nodes, directed edges, and no cycles.
- Application Programmable Interface (API): 
- Online Transaction Process (OLTP): row oriented 
- Online Analytical Process (OLTP): column oriented, stored in data warehouse
- Extract Transform Load (ETL)
  - Extract: get data from 1+ sources
  - Transform: perform transforms using parallel computing
  - Load: load data into target database


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


## Other Learning Objectives
- Git
  - how to resolve merge conflicts
  - review fundamentals
- Scheduling
  - cron jobs


# Functional Programming
- DRY (don't repeat yourself)
- Do one thing
- Pass by assignment! (google for formal definition)



