from pyspark.sql import SparkSession

filepath = "fetal_health.csv"

# Create a Spark session
spark = SparkSession.builder.appName("WriteToHDFS").getOrCreate()

# Create a DataFrame
df = spark.read.format("csv").option("header", "true").load(filepath)