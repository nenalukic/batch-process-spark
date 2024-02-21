# This code presents homework for question 6
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

# Read Parquet data into a DataFrames
df_zones = spark.read.parquet('zones')
df_fhv = spark.read.parquet('fhv/2019/10/')

# Register the DataFrame as a temporary tables
df_zones.registerTempTable('zones')
df_fhv.registerTempTable('fhv_2019_15')

# Execute a SQL query using Spark SQL
spark.sql("""
SELECT
    COUNT(fhv.PULocationID), z.Zone
FROM 
    fhv_2019_15 fhv INNER JOIN zones z ON fhv.PULocationID = z.LocationID
GROUP BY 
    z.Zone 
ORDER BY 1     
LIMIT 5;
""").show()