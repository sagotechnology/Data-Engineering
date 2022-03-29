#!/usr/bin/env python
"""Extract events from kafka and write them to hdfs
"""
# Import packages
import json
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, from_json
from pyspark.sql.types import StructType, StructField, StringType

# I am setting up the schema definition for the join guild event.
# Notice I added the guild field to track the guild the user is in.
def join_guild_event_schema():

    return StructType([
        StructField("Accept", StringType(), True),
        StructField("Host", StringType(), True),
        StructField("User-Agent", StringType(), True),
        StructField("event_type", StringType(), True),
        StructField("guild", StringType(), True)
    ])

# This is used for filtering the event type in the main() function.
@udf('boolean')
def is_guild_join(event_as_json):
    """udf for filtering events
    """
    event = json.loads(event_as_json)
    if event['event_type'] == 'join_guild':
        return True
    return False

# This is the main function of the program.
def main():
    """main
    """
    # This block of code creates a spark session.  In order to submit a job to spark we need a spark context.
    # Spark Session provides convenience and flexibility when setting up a spark context.
    # The name of the spark session is ExtractEventsJob.  The last bit of code creates the session.
    spark = SparkSession \
        .builder \
        .appName("ExtractEventsJob") \
        .getOrCreate()

    # Read from kafka using the spark readStream command.  The format is Kafka and the name of the topic is events.
    raw_events = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "kafka:29092") \
        .option("subscribe", "events") \
        .load()

    # This block of code is doing the event filtering and casting it to strings in one step.
    # The join guild event is created as strings with components raw_event, timestamp, and any json data included in the event.
    # The schema is infered from join_guild_event_schema() (see above).
    guild_joins = raw_events \
        .filter(is_guild_join(raw_events.value.cast('string'))) \
        .select(raw_events.value.cast('string').alias('raw_event'),
                raw_events.timestamp.cast('string'),
                from_json(raw_events.value.cast('string'),
                          join_guild_event_schema()).alias('json')) \
        .select('raw_event', 'timestamp', 'json.*')

    # I am defining a sink for the data and I am writing in a stream to HDFS using a parquet format.
    # A checkpoint location is setup to prevent losing data in case of a failure.
    # The path for this table is specified in option two--"/tmp/guild_joins".
    # The sink time is set for ten seconds.
    sink = guild_joins \
        .writeStream \
        .format("parquet") \
        .option("checkpointLocation", "/tmp/checkpoints_for_guild_joins") \
        .option("path", "/tmp/guild_joins") \
        .trigger(processingTime="10 seconds") \
        .start()

    # Sink will continue to run unless stopped by sink.stop() or by exception.
    sink.awaitTermination()


if __name__ == "__main__":
    main()
