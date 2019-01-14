"""
Description

Version: 0.1
Author: Slynxes
Date: 2018-12-28
"""

from pyspark import SparkContext
sc = SparkContext('spark://192.168.0.207:7077', 'test')
logFile = sc.addFile('/home/spark/derby.log');
logData = sc.textFile(logFile, 2).cache()
numAs = logData.filter(lambda line: 'a' in line).count()
numBs = logData.filter(lambda line: 'b' in line).count()
print('Lines with a: %s, Lines with b: %s' % (numAs, numBs))
