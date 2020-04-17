# encoding: utf-8
# -*- coding: gbk -*-
import time

def display_time(func):  # 装饰器  也是一个函数  接下来要运行func这个函数
    def wrapper(*args):  # 这个函数要写的内容是要运行的内容 ：做一下计时  可传入参数
        t1 = time.time()  # 截取时间
        result = func(*args)  # 运行我要走的函数   可写返回值
        t2 = time.time()  # 截取另一段时间
        print("Total time:{:.4}".format(t2 - t1))  # 打印总时间
        return result  # 返回函数结果

    return wrapper

def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

@display_time
def count_prime_nums(maxnum):
    count = 0
    for i in range(2, maxnum):
        if is_prime(i):
            count = count + 1
    return count


count = count_prime_nums(5000)  # 程序运行到这的时候  会先调用@display_time 然后运行wrapper里面的内容，然后运行本函数prime——nums
print(count)
