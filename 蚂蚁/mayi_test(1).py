

"""算法介绍：
%%①初始化 ：初始化 ： 初始时刻，m只蚂蚁随机放置。
%%②状态转移 ： 蚂蚁k(k = 1,2,...m)按照随机比例规则选择下一步要转移的城市。
%%③禁忌表 ： 为了不让蚂蚁选择已经访问过的地方，采用禁忌表的形式来记录蚂蚁k当前所走过的地方。
%%④信息素更新 ： 信息素挥发+信息素释放
%%⑤蚂蚁完成一次循环后，清空禁忌表，重新回到初始地点，准备下一次周游（循环）。
"""

import random
import time
import copy
import sys
import math
import tkinter # GUI模块
import threading
from functools import reduce

"""
蚁群算法参数【常量全部开头大写】：
-Alpha:信息启发因子
-Beta:期望启发因子
-Rou:信息素消失因子
-AntCount:蚂蚁数量
-CityCount:城市数量
-IterationTimes:迭代次数
"""

Alpha = 1#信息启发因子
Beta = 1#期望启发因子
Rou = 0.2#信息素消失因子
Q = 100#常量，表示信息素浓度
AntCount = 40#蚂蚁数量
CityCount = 50#城市数量
q_random = 0.03#
distance_x = [
    178,272,176,171,650,499,267,703,408,437,491,74,532,
    416,626,42,271,359,163,508,229,576,147,560,35,714,
    757,517,64,314,675,690,391,628,87,240,705,699,258,
    428,614,36,360,482,666,597,209,201,492,294]
distance_y = [
    170,395,198,151,242,556,57,401,305,421,267,105,525,
    381,244,330,395,169,141,380,153,442,528,329,232,48,
    498,265,343,120,165,50,433,63,491,275,348,222,288,
    490,213,524,244,114,104,552,70,425,227,331]
# 城市距离和信息素在图中分布
distance_graph = [[0.0 for col in range(CityCount)] for raw in range(CityCount)]
print(len(distance_graph))
pheromone_graph = [[random.uniform(1.0, 2.0) for col in range(CityCount)] for raw in range(CityCount)]
print(len(pheromone_graph))
open_table_city = [random.randint(1,5) for i in range(CityCount)]
print(open_table_city)

# ----------蚂蚁-------------
class Ant(object):

    """初始化"""
    def __init__(self, ID):
        self.ID = ID
        self.__clean_data()     # 随机初始化出生点


    """初始化数据，并指定初始城市位置"""
    def __clean_data(self):
        self.path = []              # 当前路径
        self.total_distance = 0.0   # 当前路径的总距离
        self.move_count = 0         # 移动次数
        self.current_city = -1      # 当前停留的城市
        self.open_table_city = [random.randint(1,5) for i in range(CityCount)]     # 地图中所有城市的探索状态都被开启
        print(self.open_table_city)
        self.open_table_city[0] = 10

        # city_index = random.randint(0,CityCount-1)  # 随机初始化城市（在CityCount里以下标做切片，0为第一个城市）
        city_index = 0  # 令第一个城市为起点，即仓库位置
        self.current_city = city_index
        self.path.append(city_index)
        # self.open_table_city[0] -= 1
        self.open_table_city[city_index] -= self.open_table_city[city_index]   # 表示这个城市已经被探索过了一次，关闭以免再次被探索
        self.move_count = 1

    """选择下一个城市"""
    def __choice_next_city(self):
        next_city = -1
        select_citys_prob = [0.0 for i in range(CityCount)]     # 前往下一个城市的概率
        total_prob = 0.0
        # 获取前往下一个城市的概率
        for i in range(CityCount):
            if self.open_table_city[i]:
                # pij的计算公式见笔记中的数学表达
                try:
                    # [当前城市][下一个城市]
                    select_citys_prob[i] = pow(pheromone_graph[self.current_city][i], Alpha) \
                                         * pow((1.0/distance_graph[self.current_city][i]), Beta)
                    total_prob += select_citys_prob[i]
                except ZeroDivisionError as e:
                    print('Ant ID:{ID}, current city: {current}, target city:{target}'.format(ID = self.ID,
                                                                                              current = self.current_city,
                                                                                              target = i))
                    sys.exit(1)  # 有错误退出

        # 根据上述计算的概率，【模拟转盘】选择下一个要去的城市
        q_each_random = random.uniform(0, 1)
        if q_each_random >= q_random:
            if total_prob > 0.0:
                # 【模拟转盘】产生一个0~total_prob的随机概率，然后每个可去的城市对其轮次相减，若减后为负数代表落入转盘区间
                temp_prob = random.uniform(0.0, total_prob)
                for i in range(CityCount):
                    if self.open_table_city[i]:
                        # 轮次相减
                        temp_prob -= select_citys_prob[i]
                        if (temp_prob < 0.0):
                            next_city = i
                            break
        # 若无法从转盘概率选出，随机选择一个城市
            if next_city == -1:
                next_city = random.randint(1,CityCount-1)
                # 若该城市已经走过，则再随机选一遍
                while ((self.open_table_city[next_city]) == False):
                    next_city = random.randint(1, CityCount-1)
        elif q_each_random < q_random:
            next_city = 0

        return next_city


    """计算路径总距离"""
    def _cal_total_distance(self):
        temp_distance = 0.0
        for i in range(1, CityCount):
            start, end = self.path[i], self.path[i-1]
            temp_distance += distance_graph[start][end]

        # 终点到原点的回路
        end = self.path[0]
        temp_distance += distance_graph[start][end]
        self.total_distance = temp_distance

    """移动"""
    def _move(self, next_city):
        self.path.append(next_city)
        self.open_table_city[next_city] = False
        self.total_distance += distance_graph[self.current_city][next_city]
        self.current_city = next_city
        self.move_count += 1


    """搜索路径"""
    def _search_path(self):
        # 初始化数据
        self.__clean_data()
        # 搜索路径，直到遍历完所有城市
        while self.move_count < CityCount:
            next_city = self.__choice_next_city()
            self._move(next_city)
        # 计算路径总长度
        self._cal_total_distance()


# ---------TSP----------
class TSP(object):

    def __init__(self, root, width=800, height=600, n=CityCount):

        # 创建画布
        self.root = root
        self.width = width
        self.height = height
        # 城市数目初始化为CityCount
        self.n = n
        # tkinter.Canvas  画布
        self.canvas = tkinter.Canvas(
            root,
            width=self.width,
            height=self.height,
            bg="#EBEBEB",  # 背景白色
            xscrollincrement=1,
            yscrollincrement=1
        )
        self.canvas.pack(expand=tkinter.YES, fill=tkinter.BOTH)
        self.title("蚁群算法(n:初始化 e:开始搜索 s:停止搜索 q:退出程序)")
        self.__r = 4  # 坐标点半径大小
        self.__lock = threading.RLock()  # 线程锁

        self.__bindEvents()
        self.new()

        # 计算城市之间的距离
        for i in range(CityCount):
            for j in range(CityCount):
                temp_distance = pow((distance_x[i] - distance_x[j]), 2) + pow((distance_y[i] - distance_y[j]), 2)
                temp_distance = pow(temp_distance, 0.5)
                distance_graph[i][j] = float(int(temp_distance + 0.5))

    # 按键响应程序
    def __bindEvents(self):

        self.root.bind("q", self.quite)  # 退出程序
        self.root.bind("n", self.new)  # 初始化
        self.root.bind("e", self.search_path)  # 开始搜索
        self.root.bind("s", self.stop)  # 停止搜索

    # 更改标题
    def title(self, s):

        self.root.title(s)

    # 初始化
    def new(self, evt=None):

        # 停止线程
        self.__lock.acquire()
        self.__running = False
        self.__lock.release()

        self.clear()  # 清除信息
        self.nodes = []  # 节点坐标
        self.nodes2 = []  # 节点对象

        # 初始化城市节点
        for i in range(len(distance_x)):
            # 在画布上随机初始坐标
            x = distance_x[i]
            y = distance_y[i]
            self.nodes.append((x, y))
            # 生成节点椭圆，半径为self.__r
            node = self.canvas.create_oval(x - self.__r,
                                           y - self.__r, x + self.__r, y + self.__r,
                                           fill="#ff0000",  # 填充红色
                                           outline="#000000",  # 轮廓白色
                                           tags="node",
                                           )
            self.nodes2.append(node)
            # 显示坐标
            self.canvas.create_text(x, y - 10,  # 使用create_text方法在坐标（302，77）处绘制文字
                                    text='(' + str(x) + ',' + str(y) + ')',  # 所绘制文字的内容
                                    fill='black'  # 所绘制文字的颜色为灰色
                                    )

        # 顺序连接城市
        # self.line(range(CityCount))

        # 初始城市之间的距离和信息素
        for i in range(CityCount):
            for j in range(CityCount):
                pheromone_graph[i][j] = random.uniform(1.0, 2.0)

        self.ants = [Ant(ID) for ID in range(AntCount)]  # 初始蚁群
        self.best_ant = Ant(-1)  # 初始最优解
        self.best_ant.total_distance = 1 << 31  # 初始最大距离
        self.iter = 1  # 初始化迭代次数

    # 将节点按order顺序连线
    def line(self, order):
        # 删除原线
        self.canvas.delete("line")

        def line2(i1, i2):
            p1, p2 = self.nodes[i1], self.nodes[i2]
            self.canvas.create_line(p1, p2, fill="#000000", tags="line")
            return i2

        # order[-1]为初始值
        reduce(line2, order, order[-1])

    # 清除画布
    def clear(self):
        for item in self.canvas.find_all():
            self.canvas.delete(item)

    # 退出程序
    def quite(self, evt):
        self.__lock.acquire()
        self.__running = False
        self.__lock.release()
        self.root.destroy()
        print(u"\n程序已退出...")
        sys.exit()

    # 停止搜索
    def stop(self, evt):
        self.__lock.acquire()
        self.__running = False
        self.__lock.release()

    # 开始搜索
    def search_path(self, evt=None):

        # 开启线程
        self.__lock.acquire()
        self.__running = True
        self.__lock.release()

        while self.__running:
            # 遍历每一只蚂蚁
            for ant in self.ants:
                # 搜索一条路径
                ant._search_path()
                # 与当前最优蚂蚁比较
                if ant.total_distance < self.best_ant.total_distance:
                    # 更新最优解
                    self.best_ant = copy.deepcopy(ant)
            # 更新信息素
            self.__update_pheromone_gragh()
            print(u"迭代次数：", self.iter, u"最佳路径总距离：", int(self.best_ant.total_distance))
            # 连线
            self.line(self.best_ant.path)
            # 设置标题
            self.title("蚁群算法(n:随机初始 e:开始搜索 s:停止搜索 q:退出程序) 迭代次数: %d" % self.iter)
            # 更新画布
            self.canvas.update()
            self.iter += 1

    # 更新信息素
    def __update_pheromone_gragh(self):

        # 获取每只蚂蚁在其路径上留下的信息素
        temp_pheromone = [[0.0 for col in range(CityCount)] for raw in range(CityCount)]
        for ant in self.ants:
            for i in range(1, CityCount):
                start, end = ant.path[i - 1], ant.path[i]
                # 在路径上的每两个相邻城市间留下信息素，与路径总距离反比
                temp_pheromone[start][end] += Q / ant.total_distance
                temp_pheromone[end][start] = temp_pheromone[start][end]

        # 更新所有城市之间的信息素，旧信息素衰减加上新迭代信息素
        for i in range(CityCount):
            for j in range(CityCount):
                pheromone_graph[i][j] = pheromone_graph[i][j] * Rou + temp_pheromone[i][j]

    # 主循环
    def mainloop(self):
        self.root.mainloop()


# ----------- 程序的入口处 -----------

if __name__ == '__main__':
    print()
    #TSP(tkinter.Tk()).mainloop()


