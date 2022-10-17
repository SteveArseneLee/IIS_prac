from pyspark.sql import SparkSession
# import pandas as pd

spark = SparkSession.builder.appName("uber-date-trips-sql").getOrCreate()

directory = "/home/steve/Capstone/Stock"
filename = "AAPL.csv"

data = spark.read.csv(f"file:///{directory}/{filename}", inferSchema = True, header = True)

print(data)