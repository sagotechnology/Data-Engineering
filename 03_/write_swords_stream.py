#!/usr/bin/env python
"""Extract events from kafka and write them to hdfs
"""
# Import packages
import json
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, from_json
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# I am setting up the schema definition for the purchase sword event.
# Notice I added the sword type and sword cost fields to track specific event data.
def purchase_sword_event_schema():

    return StructType([
        StructField("Accept", StringType(), True),
        StructField("Host", StringType(), True),
        StructField("User-Agent", StringType(), True),
        StructField("event_type", StringType(), True),
        StructField("sword_type", StringType(), True),
        StructField("sword_cost", IntegerType(), True)
    ])

# This is used for filtering the event type in the main() function.
@udf('boolean')
def is_sword_purchase(event_as_json):
    """udf for filtering events
    """
    event = json.loads(event_as_json)
    if event['event_type'] == 'purchase_sword':
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
    # The purchase a sword event is created as strings with components raw_event, timestamp, and any json data included in the event.
    # The schema is infered from purchase_sword_event_schema() (see above).
    sword_purchases = raw_events \
        .filter(is_sword_purchase(raw_events.value.cast('string'))) \
        .select(raw_events.value.cast('string').alias('raw_event'),
                raw_events.timestamp.cast('string'),
                from_json(raw_events.value.cast('string'),
                          purchase_sword_event_schema()).alias('json')) \
        .select('raw_event', 'timestamp', 'json.*')

    # I am defining a sink for the data and I am writing in a stream to HDFS using a parquet format.
    # A checkpoint location is setup to prevent losing data in case of a failure.
    # The path for this table is specified in option two--"/tmp/sword_purchases".
    # The sink time is set for ten seconds.
    sink = sword_purchases \
        .writeStream \
        .format("parquet") \
        .option("checkpointLocation", "/tmp/checkpoints_for_sword_purchases") \
        .option("path", "/tmp/sword_purchases") \
        .trigger(processingTime="10 seconds") \
        .start()

    sink.awaitTermination()


if __name__ == "__main__":
    main()
