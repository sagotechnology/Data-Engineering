# Tracking User Activity
&nbsp;  
## Project Description

I work at an ed tech firm.  I've created a service that delivers assessments, and now several different customers (e.g., Pearson) want to publish their assessments on it.  In this project I prepare the assessment data for data scientists who work for these customers to run queries. 

## Tasks

Prepare the infrastructure to land in the assessment data and structure it to be queried.
- Publish and consume messages with Kafka
- Use Spark to transform the messages. 
- Use Spark to transform the messages so that you can land them in HDFS.
- Query the dataset to answer the following:  
&nbsp;1. How many assesstments are in the dataset?  
&nbsp;2. What's the name of your Kafka topic? How did you come up with that name?  
&nbsp;3. How many people took *Learning Git*?  
&nbsp;4. What is the least common course taken? And the most common?  
&nbsp;5. Add any query(ies) you think will help the data science team



## Repository Contents

1. docker-compose.yml - used to setup the infrastructure and services.

2. annotated-history.md - a summarized and annotation version of history.txt.  The file includes an explanation of each command critical to preparing the environment for landing in data and analyzing.

3. project2-pyspark.ipynb - notebook that contains the project report.

4. history.txt - contains the full history of the virtual machine.

5. derby.log file and metastore_db folder created when the Spark shell launch.
