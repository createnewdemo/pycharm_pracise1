#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/16 17:17
# @Author  : lihanhan
# @Email   : demo1li@163.com
# @File    : demo2.py
import sys
from pyspark import SparkContext
from operator import add
import  re

def main():
    sc = SparkContext(appName= "wordsCount")
    x = sc.parallelize([1, 3, 2])
    print(x.count())
if __name__ =="__main__":
    main()