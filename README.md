# DC

## Parallel Computation Frameworks
- Spark
  - avoids disk writes (as opposed to Hadoop)
  - relies on resilient distributed datasets (RDD)
    - list of tuples 
    - transformation methods: .map(), .filter()
    - actions: .count(), first()
