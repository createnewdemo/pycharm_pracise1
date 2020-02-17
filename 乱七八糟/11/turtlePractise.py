import turtle as t


def run(angle, lenth):  # 方向为angle ，画笔前进length个单位长度
    t.seth(angle)  # 设置当前画笔的方向为angle
    t.fd(lenth)  # 画笔移动distance距离


def change(x, y):  # 将画笔的位置设置在(x, y)
    t.penup()
    t.goto(x, y)
    t.pendown()


def init():
    t.pensize(10)
    t.pencolor("green")


t.speed(100)

t.setup(800, 400, 200, 200)
init()
change(-350, 50)
run(0, 80)
change(-310, 100)
run(-90, 220)
change(-310, 50)
run(235, 120)
change(-310, 20)
run(315, 60)
change(-230, 80)
run(0, 60)
run(225, 90)
run(0, 100)
run(260, 130)
run(135, 30)
change(-210, 10)
run(240, 80)
change(-170, 10)
run(240, 120)
change(50, 50)
run(0, 50)
change(75, 50)
run(-90, 100)
change(50, 0)
run(0, 50)
change(50, -50)
run(0, 50)
change(130, 70)
run(300, 30)
change(190, 70)
run(230, 30)
change(165, 80)
run(250, 80)
change(160, 30)
run(310, 35)
change(120, -5)
run(300, 35)
change(190, -10)
run(230, 35)
change(165, -10)
run(240, 80)
change(155, -50)
run(310, 50)

t.done()
'''turtle.left(45)
turtle.fd(150)
turtle.right(135)
turtle.fd(300)
turtle.left(135)
turtle.fd(150)'''
