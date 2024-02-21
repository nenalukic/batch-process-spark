# This code presents homework for question 2
# Import necessary libraries
import pyspark
from pyspark.sql import SparkSession
import pandas as pd
from pyspark.sql import types

# Create a SparkSession
spark = SparkSession.builder \
    .master("local[*]") \
    .appName('test') \
    .getOrCreate()

# Read a CSV file into a DataFrame
df = spark.read \
    .option("header", "true") \
    .csv('fhv_tripdata_2019-10.csv')

# Define a custom schema for the DataFrame with specific fields and data types.
schema = types.StructType([
    types.StructField('dispatching_base_num', types.StringType(), True),
    types.StructField('pickup_datetime', types.TimestampType(), True),
    types.StructField('dropOff_datetime', types.TimestampType(), True),
    types.StructField('PULocationID', types.IntegerType(), True),
    types.StructField('DOLocationID', types.IntegerType(), True),
    types.StructField('SR_Flag', types.StringType(), True),
    types.StructField('Affiliated_base_number', types.StringType(), True)
])

# Re-reads the CSV file with the specified schema
df = spark.read \
    .option("header", "true") \
    .schema(schema) \
    .csv('fhv_tripdata_2019-10.csv')

# Repartitions the DataFrame
df = df.repartition(6)

# Write the DataFrame to Parquet format
df.write.parquet('fhv/2019/10/')

# Read the Parquet data back into a DataFrame
df = spark.read.parquet('fhv/2019/10/')

# Print the schema
df.printSchema()

df.show()
