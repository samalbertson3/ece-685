from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize Spark session
spark = SparkSession.builder.appName("SumColumn").getOrCreate()

# Read data from a CSV file
df = spark.read.csv("pyspark_test/data.csv", header=True, inferSchema=True)

# Multiply the elements of columns 'x' and 'y' and create a new column 'z'
df = df.withColumn("z", col("x") * col("y"))

# Select only the 'z' column
z_df = df.select("z")

# Write the 'z' column to a new CSV file
z_df.write.csv("s3://your-bucket-name/output/z_column", header=True, mode="overwrite"

# Stop the Spark session
spark.stop()
