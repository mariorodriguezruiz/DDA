'''
Created on 29 may. 2017

@author: Mario
'''
import json, re
# Imports the PySpark libraries
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext, Row
from datetime import datetime, date
from pyspark.sql.functions import col,when, mean, udf, datediff, to_date, lit, unix_timestamp, stddev
from pyspark.sql.types import StringType, IntegerType
import matplotlib.pyplot as plt
 
# The 'os' library allows us to read the environment variable SPARK_HOME defined in the IDE environment
import os

# Configure the Spark context to give a name to the application
sparkConf = SparkConf().setAppName("ex7-1-2")
sc = SparkContext(conf = sparkConf)
sqlContext = SQLContext(sc)

data = sqlContext.read.json("../datasets/students.json")

# ------------------------ Replace the null value(s) in column points by the mean of all points ----------------------------

mean_points = round(data.select([mean('points')]).head()[0], 3)

# data.show()

ch_null_points = data.withColumn("points", 
          when(col("points").isNull(), mean_points).
          otherwise(col("points")))
# ch_null_points.show()

# ------------------------ end ----------------------------

# ------------------------ Replace the null value(s) in column dob and column last name by "unknown" and "--" ----------------------------

ch_null_dob = ch_null_points.withColumn("dob", 
          when(col("dob").isNull(), "unknown").
          otherwise(col("dob")))

ch_null_lastName = ch_null_dob.withColumn("last_name", 
          when(col("last_name").isNull(), "--").
          otherwise(col("last_name")))

# ------------------------ end ----------------------------

# ------------------------ Let's convert all the dates into DD-MM-YYYY ----------------------------

# Returns the number of the month that corresponds to a character string
def monthToNumber(string):
    m = {
        'jan': 1,
        'feb': 2,
        'mar': 3,
        'apr': 4,
        'may': 5,
        'jun': 6,
        'jul': 7,
        'aug': 8,
        'sep': 9,
        'oct': 10,
        'nov': 11,
        'dec': 12
        }
    s = string.strip()[:3].lower()
    out = m[s]
    return out

# Changes the way a date is represented (DD-MM-YYYY)
def dateFormatChange(dat):
    # Return all non-overlapping matches of pattern in string, as a list of strings
    line = re.findall(r"[\w']+", dat)
    if "unknown" not in line:
        for i in line:
            # If the string is a digit
            # otherwise it is the month
            if i.isdigit():
                # If the number of elements of the digit is greater 
                # than two is that it is a year, otherwise it is the day
                if len(i)>2:
                    y = i
                else:
                    d = i
            else:
                m = str(monthToNumber(i))
        line = d + "-" + m + "-" + y
    else:
        line = ''.join(line)
    return line

def newDateValues(value):
    return dateFormatChange(value)

udfValueToCategory = udf(newDateValues, StringType())
new_dates = ch_null_lastName.withColumn("dob", udfValueToCategory("dob"))
# new_dates.show()
# ------------------------ end ----------------------------

# ------------------------ Insert a new column age and calculate the current age of all students ----------------------------

date_fmt = '%Y-%m-%d'
# Current date
today = datetime.today()  
today = today.strftime(date_fmt)

# Converts the days into years and returns them as integers
def ageValues(value):
    if(value == None):
        return value
    else:
        return int(value/365)

udfValue = udf(ageValues, IntegerType())

# Difference of days between the current date and the student's date
age = new_dates.withColumn("age", 
              datediff(to_date(lit(today)),
                       to_date(unix_timestamp('dob', "dd-MM-yyyy").cast("timestamp"))))

# Update age to years
age = age.withColumn("age", udfValue("age"))

# age.show()
# ------------------------ end  ----------------------------


# ------------------------ standard deviation ----------------------------

# Calculation of the standard deviation
sdv = round(age.select([stddev('points')]).head()[0], 3)
# Calculation of the standard average or mean
mean_points = round(age.select([mean('points')]).head()[0], 3)
# if his point is larger than 1 standard deviation of all points, 
# then we update his current point to20,
dev = age.withColumn("points", 
          when(col("points")> (mean_points+sdv+1), 20).
          otherwise(col("points")))
# dev.show()

# ------------------------ end  ----------------------------


# ------------------------ Create a histogram on the new points created in the task 5 ----------------------------

sqlContext.registerDataFrameAsTable(dev, "bb")
columns_num = [2, 4]
# Extract the columns that interest (points and names)
df2 = dev.select(*(dev.columns[i] for i in columns_num))

# Compute histogram
def histogram(par):
    points = list(map(lambda x: x[0], par))
    name = map(lambda x: x[1], par)
    plt.xlabel('Points')
    plt.ylabel('Names')
    plt.title('Task-6 Histogram')
    plt.barh(range(len(points)), points, color = 'blue')
    plt.yticks(range(len(points)), name)
    plt.show()

# Put in RDD format to work with the histogram
par = df2.rdd.map(lambda x: (x[1], x[0]))
histogram(par.take(20))

# ------------------------ end  ----------------------------


