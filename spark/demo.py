#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 17:21
# @Author  : lihanhan
# @Email   : demo1li@163.com
# @File    : demo.py
import os
import sys
# # Path for spark source folder
# os.environ['SPARK_HOME'] = "E:\adasoftware\spark-2.4.5-bin-hadoop2.7"
#
# # Append pyspark to Python Path
# sys.path.append("E:\adasoftware\spark-2.4.5-bin-hadoop2.7\python")
#
from pyspark import SparkContext
sc = SparkContext("local", "count app")
words = sc.parallelize(
    ["scala",
     "java",
     "hadoop",
     "spark",
     "akka",
     "spark vs hadoop",
     "pyspark",
     "pyspark and spark"
     ])
counts = words.count()
print("Number of elements in RDD -> %i" % counts)