# This code presents homework for question 4
# Import necessary libraries
import pyspark
from pyspark.sql import SparkSession
import pandas as pd
from pyspark.sql import types
from pyspark.sql import functions as F

# Create a SparkSession
spark = SparkSession.builder \
    .master("local[*]") \
    .appName('test') \
    .getOrCreate()

# Read Parquet data into a DataFrame
df = spark.read.parquet('fhv/2019/10/')

# Register the DataFrame as a temporary table
df.registerTempTable('fhv_2019_10')

# Perform DataFrame transformations and aggregations by adding two new columns duration_hours and pickup_date
df \
    .withColumn('duration_hours', (df.dropOff_datetime.cast('long') - df.pickup_datetime.cast('long')) / 3600) \
    .withColumn('pickup_date', F.to_date(df.pickup_datetime)) \
    .groupBy('pickup_date') \
        .max('duration_hours') \
    .orderBy('max(duration_hours)', ascending=False) \
    .limit(5) \
    .show()