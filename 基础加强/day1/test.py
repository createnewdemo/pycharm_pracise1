#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/29 23:59
# @Author  : lihanhan
# @Email   : demo1li@163.com
# @File    : test.py
def main():
    names = ['关羽', '张飞', '赵云', '马超', '黄忠']
    subjs = ['语文', '数学', '英语']
    scores = [[]] * 5
    for row, name in enumerate(names):
        print('请输入%s的成绩' % name)
        scores[row] = [0] * 3
        for col, subj in enumerate(subjs):
            scores[row][col] = float(input(subj + ': '))
    print(scores)


if __name__ == '__main__':
    main()
