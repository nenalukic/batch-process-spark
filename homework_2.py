# This code presents homework for question 3
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

# Execute a SQL query using Spark SQL
spark.sql("""
SELECT
    COUNT(1)
FROM 
    fhv_2019_10
WHERE
    to_date(pickup_datetime) = '2019-10-15';
""").show()