# Project 3: Understanding User Behavior

## Scope

For this project, I am a data scientist at a game development company.  The game that I developed has two events: purchase a sword and join a guild.  Each event has metadata that can be quieried to gain business insights.  


## Tasks

I am tasked with the following to setup a data streaming pipeline:  

- Instrument your API server to log events to Kafka

- Assemble a data pipeline to catch these events: use Spark streaming to filter
  select event types from Kafka, land them into HDFS/parquet to make them
  available for analysis using Presto

- Use Apache Bench to generate test data for your pipeline

- Produce an analytics report where you provide a description of your pipeline
  and some basic analysis of the events


## Repository Breakdown

- Events folder: contains the event streaming code.  

- version-control folder: used to keep last known working files.

- docker-compose.yml: file used to setup docker cluster.

- game_api.py: file that contains the game functionality.

- write_guild_stream.py: spark job for streaming join guild events.

- write_sword_stream.py: spark job for streaming purchase a sword events.

- report_notebook.ipynd: the final report that contains step-by-step instructions for setting up the data pipeline and discussion about the business insights derived for user events.
