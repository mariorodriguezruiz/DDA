'''
Created on 29 may. 2017

@author: Mario
'''
# Imports the PySpark libraries
from pyspark import SparkConf, SparkContext
 
# The 'os' library allows us to read the environment variable SPARK_HOME defined in the IDE environment
import os

# Configure the Spark context to give a name to the application
sparkConf = SparkConf().setAppName("ex7-1-2")
sc = SparkContext(conf = sparkConf)

a = ["spark", "rdd", "python", "context", "create", "class"]
b = ["operation", "apache", "scala", "lambda","parallel","partition"]

c1 = sc.parallelize(a)
c2 = sc.parallelize(b)

char = 's'

print("\nHow many times the character \"s\" appears in a")

seqOp = (lambda x: x['s'])
combOp = (lambda x,y: (x + y))
# how many times the character "s" appears in a
var = c1.aggregate((0, 0), seqOp, combOp)
# for i in var: print (i)

# var = c1.flatMap(lambda x: x).map(lambda x: (x==char, 1)).reduceByKey(lambda x, y: x + y).collect()
 
# for i in var: print (i)

# print("\nHow many times the character \"s\" appears in b")
# # how many times the character "s" appears in b
# var = c2.flatMap(lambda x: x).map(lambda x: (x==char, 1)).reduceByKey(lambda x, y: x + y).collect()
#  
# for i in var: print (i)
# 
# print("\nHow many times the character \"s\" appears in all a and b")
# # how many times the character "s" appears in all a and b
# c3 = c1.union(c2)
# var = c3.flatMap(lambda x: x).map(lambda x: (x==char, 1)).reduceByKey(lambda x, y: x + y).collect()
#  
# for i in var: print (i)


print("\n")
