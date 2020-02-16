from random import random


def printIntro():
    print("此程序模拟AB选手的某种竞技比赛")
    print("运行需要AB的能力值")


def getInputs():
    a = eval(input("A的能力值（0-1）："))
    b = eval(input("B的能力值（0-1）："))
    n = eval(input("比赛的场次："))
    return a, b, n


def printSummary(winsA, winsB):
    n = winsA + winsB
    print("竞技分析开始，共模拟{}场比赛".format(n))
    print("选手A获胜{}场比赛，占比{:.1%}".format(winsA, winsA / n))
    print("选手B获胜{}场比赛，占比{:.1%}".format(winsB, winsB / n))


def gameOver(a, b):
    return a == 15 or b == 15


def simOneGame(probA, probB):
    scoreA, scoreB = 0, 0
    serving = "A"
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA += 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB += 1
            else:
                serving = "A"
    return scoreA, scoreB


def simNGames(n, probA, probB):
    winsA, winsB = 0, 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA, winsB


def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)


main()
