# Import the necessary modules
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Create a SparkSession
spark = SparkSession.builder \
   .appName("pull-kafka-data") \
   .getOrCreate()

df = spark \
  .readStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "kafka-broker:29092") \
  .option("subscribe", "delivery-dev.public.heartbeat") \
  .load() 
df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")

query = df.writeStream \
  .outputMode("append") \
  .format("console") \
  .start()

# Wait for the termination of the query
query.awaitTermination()