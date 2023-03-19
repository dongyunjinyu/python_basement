"""
图（graph）是一种重要的数据结构，本节讲述图的相关算法
先修知识：内存，列表，链表，哈希表，集合，队列，图结构，邻接表，邻接矩阵，分治算法
主要包括：深度优先搜索，广度优先搜索，dijkstra算法，bellman-ford算法，prim算法，kruskal算法，ford-fulkerson算法，edmonds-krap算法，dinic算法
数据结构：可以使用面向对象的知识，建立图的抽象类，实现图的一些方法，如顶点和边的增删、遍历，为直观显示代码原理，本文不使用抽象类
"""
from collections import *
####################################
############  图的表示  ##############
####################################
# 图有两种记录形式，一种是邻接表，一种是邻接矩阵，邻接表适合记录稀疏图，而邻接矩阵适合记录稠密图
# 邻接表有：链表和哈希表 两种表示方式，分别称之为邻接表表示和邻接字典表示
# 邻接表和邻接矩阵可以互相转化，下面看一个例子，将这个邻接字典转化为邻接矩阵
graph_1 = {'v1': [['v2', 2], ['v4', 1]],
           'v2': [['v4', 3], ['v5', 10]],
           'v3': [['v1', 4], ['v6', 5]],
           'v4': [['v3', 2], ['v5', 2], ['v6', 8], ['v7', 4]],
           'v5': [['v7', 1]],
           'v6': [],
           'v7': [['v6', 1]]}
# 比如，'v5': [['v7', 1]]表示：向量V5->V7,模长为1
# n个节点生成n阶矩阵,根据需要可将矩阵初始化为全0或全无穷矩阵，这里初始化为无穷阵
"""
n = len(graph_1)
a = []
for i in range(n):
    a.append(float('inf'))
graph_2 = []
for i in range(n):
    graph_2.append(a.copy())  # 必须用copy后的列表来追加，否则每一行实际上是is的，内存知识
# 以每个起始点的序号作为行数i，以这个点指向的点的序号作为列数j，以模长作为这一行这一列的值
for key, item in graph_1.items():
    i = int(key[1:])
    for v in item:
        graph_2[i - 1][int(v[0][1:]) - 1] = v[1]
# print(graph_2)
"""

################################################
##############  深度优先搜索   ####################
################################################
# 深度优先搜索，简称DPS（Depth First Search），又叫深度优先遍历
# 是一种用来遍历整个图的算法。图不像列表那样的线性结构容易遍历，图的遍历是比较复杂的
# 我们用深度优先搜索,选择一个起点，然后遍历整个连通图
graph_3 = {'v0': [['v1'], ['v5']],
           'v1': [['v0'], ['v2']],
           'v2': [['v1'], ['v3'], ['v5']],
           'v3': [['v2']],
           'v4': [['v5'], ['v6'], ['v8']],
           'v5': [['v0'], ['v2'], ['v4'], ['v6'], ['v7']],
           'v6': [['v4'], ['v5'], ['v7']],
           'v7': [['v5'], ['v6']],
           'v8': [['v4']]}


def dfs(graph, start, traversed=None):
    if traversed is None:
        traversed = []
    if len(traversed) == len(graph):
        return traversed
    else:
        if start not in traversed:
            traversed.append(start)
        _bool = 1
        for ver in graph[start]:
            ver = ver[0]
            if ver not in traversed:
                _bool = 0
                return dfs(graph, ver, traversed)
        if _bool:
            return dfs(graph, traversed[traversed.index(start) - 1], traversed)


# print(dfs(graph_3, 'v0'))
# print(dfs(graph_1, 'v1'))


################################################
##############  广度优先搜索   ####################
################################################
# 广度优先搜索，简称BFS（Breadth First Search），又叫广度优先遍历
# 用处：求 无权图 各点的优先级（即：最短路径）
# 得到的是：起点到任意节点的最短路径，可以以一颗树来表示，称之为广度优先搜索生成树
# 对下面这张图以某个点为起点进行广度优先搜索
graph_4 = {'v1': ['v2', 'v4'],
           'v2': ['v4', 'v5'],
           'v3': ['v1', 'v6'],
           'v4': ['v3', 'v5', 'v6', 'v7'],
           'v5': ['v7'],
           'v6': [],
           'v7': ['v6']}


def bfs(graph, start, hashlist=None, dq=None):
    if hashlist is None:  # 第一次递归，初始化哈希表
        hashlist = {}
        for key in graph.keys():
            if key == start:  # 初始化起点
                hashlist[key] = [True, 0, 0]  # 第一个值代表这个点是否被遍历过，第三个值代表到达这个点的上一个点
                continue
            hashlist[key] = [False, float("inf"), 0]  # 第二个代表优先级（即：离起点的最短距离）
    if dq is None:  # 第一次递归，初始化队列
        dq = deque([start])
    if not dq:  # 基线条件：队列为空，遍历完成
        return hashlist
    else:  # 开始递归：
        v = dq.popleft()  # 弹出队列中的第一个元素v
        for ver in graph[v]:  # 遍历v所能到达的点
            if not hashlist[ver][0]:  # 如果这个点已被visit，什么也不干；若没有被visit就：
                hashlist[ver] = [True, hashlist[v][1] + 1, v]  # visit它，并更新它的数据
                dq.append(ver)  # 把它加到队列的末尾
        return bfs(graph, None, hashlist, dq)  # 递归，不需要传start参数


# print(bfs(graph_4, 'v3'))


def bfs_tree(hashlist, tree=None, queue=None):  # 生成一颗广度优先搜索生成树
    if queue is None:  # 第一次递归，初始化队列
        queue = []
    if tree is None:  # 第一次递归，初始化生成树
        tree = {}
        for key, item in hashlist.items():
            tree[key] = []
            if item[1] == 0:
                queue.append(key)
    if not queue:  # 基线条件：队列为空，遍历完成
        return tree
    else:  # 开始递归：
        last = queue.pop(0)  # 从队列弹出一个点作为起点last
        for key, item in hashlist.items():  # 遍历哈希表
            if item[2] == last:  # 找到所有以last作为起点的点
                tree[last].append(key)  # 把它加到生成树中
                queue.append(key)  # 并将其加入队列
        return bfs_tree(hashlist, tree, queue)


# print(bfs_tree(bfs(graph_4, 'v3')))


################################################
##############  Dijkstra算法   ##################
################################################
# 用处：求 正权图 的最短路径
# 求graph_1的最短路径:
def dijkstra(graph, start, queue=None, hashlist=None):
    if queue is None:  # 第一次递归，初始化队列
        queue = [start]
    if hashlist is None:  # 第一次递归，初始化哈希图
        hashlist = {}
        for key, item in graph.items():
            hashlist[key] = [float('inf'), 0]  # 第一个值代表这一点到起点的距离，第二个代表父节点
        hashlist[start] = [0, 0]
    if not queue:  # 基线条件：队列为空
        return hashlist
    else:  # 开始递归：
        this = queue.pop(0)  # 弹出队列的第一个节点，作为this
        for next_ in graph[this]:  # 遍历this节点的邻接点next_
            next_ver = next_[0]
            if next_[1] + hashlist[this][0] < hashlist[next_ver][0]:  # 如果通过this节点到达next节点的路径短于哈希表中记录的从起点到next的最短距离
                hashlist[next_ver][0] = next_[1] + hashlist[this][0]  # 那么更新哈希表中next节点的最短距离
                hashlist[next_ver][1] = this  # 同时更新哈希表中next节点的父节点
                queue.append(next_ver)  # 把next节点追加到队列中
        return dijkstra(graph, None, queue, hashlist)
# print(dijkstra(graph_1, 'v3'))


################################################
############  Bellman-Ford算法   ################
################################################











################################################
################  Prim算法   ####################
################################################
