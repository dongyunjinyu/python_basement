"""
numpy库是python科学计算的重要库，这个库中包含诸多模块，内容繁多，功能齐全
全学会不实际，只学习主要方法，其他方法需要用到的时候再学习即可
就好比队列（deque）比列表快一样，numpy中的数组（ndarray）也比列表快，快50倍，因为numpy是用c写的
先修内容：列表、矩阵（代数学）、内存
"""
import numpy as np

################################################################
#########################  数组生成  #############################
################################################################
print(np.array([1, 2, 3, 4, 5]))  # [1 2 3 4 5]
print(np.array((1, 2, 3, 4, 5)))  # [1 2 3 4 5]

# numpy.array(object, dtype = None, copy = True, order = 'K', subok = False, ndmin = 0)
# object: 传递数组
# dtype: 指定数据类型
# copy:
# order:
# subok:
# ndmin: 指定生成数组的最小维数

print(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 'a']]))
# [['1' '2' '3']
#  ['4' '5' '6']
#  ['7' '8' 'a']]
# 一个是str型数据，则全变为str型

print(np.array([[1, 2, 3], [4, 5, 6], [7, 8, '1']], dtype=np.int16))
# [[1 2 3]
#  [4 5 6]
#  [7 8 1]]
# 类似于map,不过numpy支持的数据类型要远多于python自带的类型，具体上网找

print(np.array([1, 2, 3], ndmin=2))  # [[1 2 3]] 指定最小维度
print(np.array([[1], [2]]).ndim)  # 2  打印维度
print(np.array([1, 2, 3]).dtype)  # int32  查看数组的数据类型
print(np.array([1, 2, 3]).astype(complex))  # 类型转换

""" 索引 & 切片 """
arr1 = np.array([[1, 2, 3, 4, 5, 6, 7],
                 [8, 9, 10, 11, 12, 13, 14],
                 [15, 16, 17, 18, 19, 20, 21],
                 [22, 23, 24, 25, 26, 27, 28]])
print(arr1[1, 2])  # 10   索引，与数组不同。但仍然从0开始计数
print(arr1[1, 1:3])  # [ 9 10]   切片,留头去尾
print(arr1[0:3:2, 1:6:2])  # 步长，取子式
# [[ 2  4  6]
#  [16 18 20]]


""" 副本 & 视图 """
arr2 = arr1.copy()  # 副本
arr3 = arr1.view()  # 视图，内存类似于浅拷贝
arr4 = arr1  # 但和浅拷贝不同
print(arr1.base)  # None
print(arr2.base)  # None
print(arr3.base)  # arr1的值     用来检查一个array是不是视图
print(arr4.base)  # None

""" 维度变换 """
print(arr1.shape)  # (4, 7)  返回数组形状，这个是从1开始计数的
print(arr1.reshape(2, 14))  # 将数组转换成指定维度的数组
# # [[ 1  2  3  4  5  6  7  8  9 10 11 12 13 14]
# #  [15 16 17 18 19 20 21 22 23 24 25 26 27 28]]
print(arr1.reshape(1, -1))  # 传入-1，会自动计算对应长度，但是必须整除
# [[ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28]]
# print(arr1.reshape(3, -1)  会报错，不整除

arr6 = arr1.reshape(2, 14)
arr6[1, 9] = 0
print(arr1)
# [[ 1  2  3  4  5  6  7]
#  [ 8  9 10 11 12 13 14]
#  [15 16 17 18 19 20 21]
#  [22 23 0 25 26 27 28]]
print(arr6)
# [[ 1  2  3  4  5  6  7  8  9 10 11 12 13 14]
#  [15 16 17 18 19 20 21 22 23 0 25 26 27 28]]
print(arr6.base)
# [[ 1  2  3  4  5  6  7]
#  [ 8  9 10 11 12 13 14]
#  [15 16 17 18 19 20 21]
#  [22 23 0 25 26 27 28]]
# 说明array6是个视图


################################################################
#########################  数组操作  #############################
################################################################
""" 遍历 """
arr11 = np.array([[[1, 2, 3], [1, 2, 3], [1, 2, 3]],
                  [[1, 2, 3], [1, 2, 3], [1, 2, 3]],
                  [[1, 2, 3], [1, 2, 3], [1, 2, 3]]])
# 如果我们要遍历arr11，那就需要用三重循环，这很不方便
# 第一种：
s = 0
for i in np.nditer(arr11):  # 还可用flags参数指定空间，用op_dtypes指定数据类型
    s += i
print(s)  # 54
# 第二种：
for index, x in np.ndenumerate(arr11):
    print(index, x)
# (0, 0, 0) 1
# (0, 0, 1) 2
# (0, 0, 2) 3
# ……………………………


""" 连接 """
arr12 = [[1, 2], [3, 4]]
arr13 = [[5, 6], [7, 8]]
print(np.concatenate((arr12, arr13)))  # 注意这里是两个括号
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]
print(np.concatenate((arr12, arr13), axis=1))  # 指定拼接轴
# [[1 2 5 6]
#  [3 4 7 8]]
# 这两个不好，stack方法也不好，axis参数有毛病，一般三维以内拼接用下面这三个
print(np.hstack((arr12, arr13)))  # 行堆叠
# [[1 2 5 6]
#  [3 4 7 8]]
print(np.vstack((arr12, arr13)))  # 列堆叠
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]
print(np.dstack((arr12, arr13)))  # 深堆叠
# [[[1 5]
#   [2 6]]
#
#  [[3 7]
#   [4 8]]]
# 维度到四维以上才用concatenate和stack方法

""" 分割 """
arr14 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(np.array_split(arr14, 3))
# [array([1, 2, 3]), array([4, 5, 6]), array([7, 8, 9])]


################################################################
#########################  函数  #############################
################################################################
print(np.linspace(1, 3, 5))  # [1.  1.5 2.  2.5 3. ]   等差数列
# 前闭后闭，如果要前开后闭，就指定endpoint=False
print(np.logspace(1, 5, 5, base=2))  # [ 2.  4.  8. 16. 32.]  等比数列
# 前三个参数用于生成成等差的指数，base默认为10
print(np.ones((3, 3)))  # 双括号,dtype默认为float
# [[1. 1. 1.]
#  [1. 1. 1.]
#  [1. 1. 1.]]#
print(np.zeros([2, 3]))
# [[0. 0. 0.]
#  [0. 0. 0.]]
print(np.full((2, 5), 7))
# [[7 7 7 7 7]
#  [7 7 7 7 7]]
print(np.identity(3))  # 单位阵
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]
print(np.eye(3, 4, 1, dtype=int))  # 这个用的更多
# [[0 1 0 0]     第三个参数规定第一个1从第几位开始
#  [0 0 1 0]
#  [0 0 0 1]]
print(np.random.rand(2, 3, 4))  # 2行3列4层，0~1的随机浮点数
print(np.random.randint(3, 6, (2, 3)))
# [[5 5 3]
#  [4 3 3]]
print(np.random.normal(0, 1, (3, 3)))  # 正态分布
# [[-0.78990588  0.30607841 -0.66406824]
#  [ 0.9357701  -0.23777273 -0.40748484]
#  [ 0.76129233 -0.27050911 -0.75081226]]
print(np.random.randn(2, 2))  # 标准正态分布，均值为0，方差为1

""" 排序 """
arr15 = np.array([[[3, 7, 4], [2, 9, 0], [5, 7, 1]],
                  [[2, 1, 1], [6, 6, 9], [3, 4, 5]],
                  [[1, 6, 0], [9, 6, 1], [1, 2, 3]]])
print(np.sort(arr15))  # 默认以最后一个维度为轴进行排序，这里是第i行第j列的三个层进行排序，也就是最里面的中括号进行排序
# [[[3 4 7]
#   [0 2 9]           可以用axis指定轴
#   [1 5 7]]
#
#  [[1 1 2]
#   [6 6 9]
#   [3 4 5]]
#
#  [[0 1 6]
#   [1 6 9]
#   [1 2 3]]]

print(np.sum(arr15))  # 104   也可以指定一个或多个轴求和
print(np.amax(arr15, axis=(0, 1)))  # [9 9 9]  指定多个轴要用括号括起来，这里求的是每一层的最大值
print(arr15.min(-1))  # 也可以通过方法来求最值
# np.mean(array, axis)求均值
# np.average(array, axis, weight)求加权平均值，较复杂，不讲了

# unique函数用于去重并返回索引

print(np.where(arr15 % 3 == 0, True, arr15))  # 一个有意思的函数，相当于一个列表推导式
# 遍历传入矩阵的每一个元素，if第一个参数成立，则把第二个参数赋值给它，否则把第三个元素赋值给它
# [[[1 7 4]
#   [2 1 1]
#   [5 7 1]]
#
#  [[2 1 1]
#   [1 1 1]
#   [1 4 5]]
#
#  [[1 1 1]
#   [1 1 1]
#   [1 2 1]]]


""" 自定义通用函数 """
abs_ufunc = np.frompyfunc(abs, 1, 1)  # 后面两个参数指定传入/传出数组的个数
print(abs_ufunc(np.array([-1, 0, 1])))  # [1 0 1]

################################################################
#########################  运算  ################################
################################################################
# +-*/%//<>!=仍适用，但是是  点运算
# 如果一个矩阵与一个数作算数运算，意为矩阵中所有元素与这个数作算数运算
print(np.array([[1, 2], [3, 4]]) % 2)
# 还有一些点运算：sin、log、exp、exp2、sqrt等用于画图

""" 广播 """
# 当一个矩阵与另一个形状不同的矩阵作点运算时，可能会发生广播
# 只有一个数组的某些维度翻一定整数倍后，两个矩阵形状相同，才能发生广播
# 显然，一个数一定能发生广播
print(np.full((3, 8), 0) + [[1], [1], [1]])
# [[1 1 1 1 1 1 1 1]
#  [1 1 1 1 1 1 1 1]
#  [1 1 1 1 1 1 1 1]]

""" 矩阵运算 """
arr16 = np.array([[1], [2], [3]])
arr17 = np.array([[1, 2, 3]])
print(np.dot(arr16, arr17))  # 矩阵点乘
# [[1 2 3]
#  [2 4 6]
#  [3 6 9]]
print(np.linalg.det(arr15[2]))  # -140.00000000000006   求行列式
print(np.linalg.det(arr15))  # [-111.   -9. -140.]
print(np.linalg.inv(arr15[0]))  # 求逆
print(np.linalg.inv(np.linalg.inv(arr15[0])))  # 求两次逆来检验



################################################################
#########################  数学函数  ################################
################################################################


