# Command Line Setup  

This file, annotated-history.md, is the summarized and annotated version of the history.txt file.  Below is an explanation of the necessary commands needed to setup project 2.  
&nbsp;  
Changes the directory.
```
cd w205/project-2-samueljgomez
```  
&nbsp;  
This command starts the containers in the background and leaves them running.  The docker-compose up command builds, creates, starts, and attaches to containers for a service.  The -d option is for detached mode; containers are run in the background.  The docker-compose.yml file contains information regarding the container setup and is the default setup file.  Another file can be specified.
```
docker-compose up -d
```  
&nbsp;  
Docker-compose logs displays the log output from services.  The -f kafka option is used to call the kafka service.
```
docker-compose logs -f kafka
```  
&nbsp;  
The curl command transfers to a URL.  The location is given by -L followed by https://goo.gl/ME6hjp.  The -o command writes the output to a file.  The file is assessment-attempts-20180128-121051-nested.json.
```
curl -L -o assessment-attempts-20180128-121051-nested.json https://goo.gl/ME6hjp
```  
&nbsp;  
This command is used to create a Kafka topic.  Docker-compose exec is a subcommand to run arbitrary commands from a particular service, kafka is selected as the service.  The topic assessments is created with one partition and a replication factor of one.  The zookeeper port is specified as 32181.
```
docker-compose exec kafka kafka-topics --create --topic assessments --partitions 1 --replication-factor 1 --if-not-exists --zookeeper zookeeper:32181
```  
&nbsp;  
This command gives a description of the topic assessments.
```
docker-compose exec kafka kafka-topics --describe --topic assessments --zookeeper zookeeper:32181
```  
&nbsp;  
This command publishes the assessment json file to Kafka.  Docker-compose exec is used to call the mids service.  The service the uses bash to read the json file as strings (-c).  The output of that is sent to jq.  The '.[]' option get the first element of the array (an assessment) and writes it as one object using -c.  Kafkacat writes the messages using -P, for producing, and -b, for broker, and -t, for topic.
```
docker-compose exec mids bash -c "cat /w205/project-2-data/assessment-attempts-nested.json | jq '.[]' -c | kafkacat -P -b kafka:29092 -t assessments"
```  
&nbsp;  
To spin up the pyspark jupyter notebook, the following command is used.  After the execution, a token is generated and used with the virtual machine's external IP address to access the notebook from a webpage.
```
docker-compose exec spark env PYSPARK_DRIVER_PYTHON=jupyter PYSPARK_DRIVER_PYTHON_OPTS='notebook --no-browser --port 8890 --ip 0.0.0.0 --allow-root --notebook-dir=/w205/' pyspark
```  
&nbsp;  
After completing the analysis in the notebook,  the following command stops the containers and removes the containers, networks, volumes, and images created by the docker-compose up -d.
```
docker-compose down
```
&nbsp;  
&nbsp;  
# Notable Mentions  
&nbsp;  
Used to count the number of assessments.
```
docker-compose exec mids bash -c "cat /w205/project-2-data/assessment-attempts-nested.json | jq '.[]' -c | wc -l"
```  
&nbsp;  
Used to display the first assessment as one object.
```
docker-compose exec mids bash -c "cat /w205/project-2-data/assessment-attempts-nested.json | jq '.[]' -c | head -1"
```  
&nbsp;  
Used to view the first one hundred elements.
```
docker-compose exec mids bash -c "cat /w205/project-2-data/assessment-attempts-nested.json | jq '.' | head -100"
```
