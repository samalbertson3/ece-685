from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import boto3
import os

# Initialize Spark session
spark = (
    SparkSession.builder.appName("SumColumn")
    .config("spark.driver.extraJavaOptions", "-Djava.security.manager=allow")
    .config("spark.executor.extraJavaOptions", "-Djava.security.manager=allow")
    .getOrCreate()
)

# Read data from a CSV file
df = spark.read.csv("pyspark_test/data.csv", header=True, inferSchema=True)

# Multiply the elements of columns 'x' and 'y' and create a new column 'z'
df = df.withColumn("z", col("x") * col("y"))

# Write the 'z' column to a new CSV file
df.write.csv("pyspark_test/calc_data", header=True, mode="append")

# Upload to S3
s3 = boto3.client("s3")
for fn in os.listdir("pyspark_test/calc_data"):
    s3.upload_file(
        "pyspark_test/calc_data/" + fn,
        "samalbertson3-test",
        "pyspark/calc_data/" + fn,
    )

# Stop the Spark session
spark.stop()
