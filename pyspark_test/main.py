from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName("SumColumn").getOrCreate()

# Read data from a CSV file
df = spark.read.csv("pyspark_test/data.csv", header=True, inferSchema=True)

# Sum the elements in a specific column (e.g., 'column_name')
sum_x = df.groupBy().sum("x").collect()[0][0]
sum_y = df.groupBy().sum("y").collect()[0][0]

# Stop the Spark session
spark.stop()
