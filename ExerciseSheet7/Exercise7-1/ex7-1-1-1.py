'''
Created on 29 may. 2017

@author: Mario
'''
# Imports the PySpark libraries
from pyspark import SparkConf, SparkContext
 
# The 'os' library allows us to read the environment variable SPARK_HOME defined in the IDE environment
import os

# Configure the Spark context to give a name to the application
sparkConf = SparkConf().setAppName("ex7-1-1")
sc = SparkContext(conf = sparkConf)

a = ["spark", "rdd", "python", "context", "create", "class"]
b = ["operation", "apache", "scala", "lambda","parallel","partition"]

c1 = sc.parallelize(a).map(lambda a: (a, 1))
c2 = sc.parallelize(b).map(lambda a: (a, 1))

for i in c1.rightOuterJoin(c2).collect(): print (i)

print("\n")
