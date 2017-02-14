"""
SparkConf used to configure Spark application
SparkContext used to create a Spark context for application
SQLContext used for working with structured dataframes; e.g. Parquet
"""
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext

"""
This is a standalone Spark application. As a result, make sure you run it using: 
   bin/spark-submit my_script.py from your Spark directory.

Author: Rich H. Inman
email: rinman24@gmail.com
Date Created: 30 Jan. 2017
"""

# Stop any SparkContext currently running
try:
    sc.stop()
    del sc
    print('Default SparkContext stopped and deleted.')
except NameError:
    print('No SparkContext initially running.\n\tCreating one now...')

# Configure the Spark application
CONF = SparkConf().setMaster("local").setAppName("My App")
# Create a Spark Context for application
SC = SparkContext(conf=CONF)

# Create an SQLContext to work with structured data
sqlCtx = SQLContext(SC)

input = sqlCtx.read.parquet('/Users/Rich/out.parquet')

input.show()
