"""
python重要的绘图库，用于数据分析中的数据可视化
先修内容：numpy库
"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

""" 两点确定一条直线 """
# px = [1, 2]
# py = np.array([3, 4])
# # 注意，两点坐标分别为(1,3),(2,4)
# plt.plot(px, py)
# plt.show()  # 画一条直线
# plt.plot(py, px)
# plt.show()  # 两条直线先后画在两张图上

""" 折线 """
# px=[1, 8, 2, 6]
# py = np.array([1, 0, 3, 4])
# # 四点坐标分别为(19,1),(8,2)(27,3)(6,4)
# plt.plot(px, py)
# plt.plot(py) # 横坐标默认为1,2,3,……
# plt.show()  # 两条折线画在同一张图上

""" 点 """
# px = [1, 8, 2, 6]
# py = [1, 0, 3, 4]
# plt.plot(px, py, 'o') # o可换成.
# plt.show()

""" 标记 """
# px = [1, 8, 2, 6]
# py = [1, 0, 3, 4]
# plt.plot(px, py, linestyle=':', marker='*', color='r', linewidth=5)
# plt.plot(px, ls='-.',  marker='H', c='g')
# plt.show()

""" 一次绘制多条折线 """
# px = [1, 8, 2, 6]
# py = [1, 0, 3, 4]
# # 两两结合，前一个是x横坐标后一个是纵坐标，单个的以1,2,3,4……为横坐标
# plt.plot(px, py, px, ls='--',  marker='o', c='b')
# plt.show()

""" 标签 """
matplotlib.rcParams['font.sans-serif'] = ['KaiTi']  # 设置字体为楷体
# font1 = {'family': 'sans-serif', 'color': 'blue', 'size': 20}  # 定义一种字体
# x = [80, 85, 90, 95, 100, 105, 110, 115, 120, 125]
# y = [240, 250, 260, 270, 280, 290, 300, 310, 320, 330]
# plt.plot(x, y, marker='o')
# plt.xlabel('平均心率', fontdict=font1)  # 指定字体
# plt.ylabel('卡路里消耗量', fontdict={'family': 'sans-serif', 'color': 'g', 'size': 15})  # 一次性设置字体
# plt.title('某运动手表 数据（2023）', fontdict={'size': 20}, loc='left')  # 设置标题左中右对齐
# plt.grid(linestyle='-.')  # 绘制网格线，如只要竖线，则传 axis='x' ; 还可指定color,linewidth,
# plt.show()

""" 多子图 """
# px = [1, 8, 2, 6]
# py = [1, 0, 3, 4]
# plt.subplot(2, 1, 1)  # 两行一列，两个子图中的第一个
# plt.title('子图1')
# plt.plot(px)
# plt.subplot(2, 1, 2)  # 两个子图中的第二个
# plt.title('子图2')
# plt.plot(py)
# plt.suptitle('总标题')  # 所有子图共同的标题
# plt.show()

""" 散点图 """
# x = [2, 8, 3, 4, 8, 9, 3, 8, 4, 6, 8, 7, 0, 9, 2, 5, 3, 1]
# y = [1, 2, 3, 6, 7, 8, 9, 3, 4, 7, 9, 2, 6, 7, 9, 0, 1, 9]
# plt.scatter(x, y, color='r', s=150)  # s就是size
# plt.scatter(x, y[::-1], color='b', alpha=0.5)  # alpha是透明度
# plt.show()
# # 散点图还有一些功能，不常用，此处不介绍

""" 柱状图 """
# # 柱状图类似于折线图，不过它的横坐标可以是字符串，但纵坐标仍然得是数
# x = ['baidu', 'alibaba', 'tencent']
# y = [15, 25, 20]
# plt.subplot(1, 2, 1)
# plt.bar(x, y, width=0.4)
# plt.subplot(1, 2, 2)
# plt.barh(x, y, color='r', height=0.5)  # 水平柱状图
# plt.show()

""" 直方图 """
# x = np.random.normal(170, 10, 250)
# plt.hist(x)
# plt.show()

""" 饼图 """
# y = [25, 20, 15, 30]
# mylabel = ['alibaba', 'tencent', 'baidu', 'other']
# myexplode = [0, 0, 0, 0.2]  # 设置弹出距离
# # 还可以指定颜色，阴影shadow
# plt.pie(y, labels=mylabel, explode=myexplode)
# plt.legend(title='internet')  # 设置图例
# plt.show()


""" 等高图 """  # 有bug
func1 = lambda x, y: (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)
x = np.linspace(-3, 3, 256)
y = np.linspace(-3, 3, 256)
X, Y = np.meshgrid(x, y)
plt.contour(X, Y, func1(X, Y), 8, alpha=0.75, cmap=plt.cm.hot)
C = plt.contour(X, Y, func1(X, Y), 8, colors='black', linewidths=0.5)
# plt.clabel(C, inline=True, fontsize=10)
plt.xticks()
plt.yticks()
plt.show()
