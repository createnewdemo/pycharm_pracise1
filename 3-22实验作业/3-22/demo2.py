#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/22 10:19
# @Author  : lihanhan
# lis_score = []
# n = int(input("输入评委人数："))
# while n < 2:
#     print("评委人数需大于2")
#     n = int(input("输入评委人数："))
# player = int(input("比赛人数："))
# while player < 3:
#     print("比赛人数需大于4")
#     player = int(input("比赛人数："))
#
# def check_score(score):
#     if score >= 0 and score <= 100:
#         return score
#     else:
#         print("分数不合法，重新输入！")
#         score = int(input("输入分数："))
#         score = check_score(score)
# j = player
# name_list = []
# while j > 0:
#     name = input("输入选手姓名：")
#     name_list.append(name)
#     i = n
#     a = []
#     while i > 0:
#         score = check_score(int(input("输入分数：")))
#         a.append(score)
#         i -= 1
#     avg_score = (sum(a) - min(a) - max(a)) / (n - 2)
#     lis_score.append([name, avg_score])
#     j -= 1
#
# print(lis_score)
# # res_list = sorted(lis_score, key=lambda d: d[1], reverse=True)
# for i in range(player):
#     print("姓名：", name_list[i])
#     print("平均分：", lis_score[i][1])
#
# ll = []
# for i in range(player):
#     ll.append(lis_score[i][1])
#
#     ll.sort(reverse=True)
# print(ll)
def get_score():
    score_list = []
    n = int(input("输入评委人数："))
    while n < 2:
        n = int(input("输入大于2的评委人数："))
    for i in range(n):
        score = int(input("输入分数："))
        if score >= 0 and score <= 100:
            score_list.append(score)
        else:
            print("分数在0-100以内，请重新输入")
            return
    return score_list
def cucl():
    score_list = get_score()
    score_list.sort(reverse=True)
    s = score_list[-(len(score_list)-1):-1]
    print("去掉最高和最低的分数以后的数组为：",s)
    avg_score = sum(s) / len(s)
    print("平均数为：",avg_score)



cucl()
