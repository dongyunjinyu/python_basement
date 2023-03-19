"""
 collections库提供了一种数据类型的实现——队列（queue）
 我们经常用的是双端队列（deque）
 队列是一种先进先出的容器，双端队列从两端出元素，集合了栈和列表的优势，从左右两端 增添改查 的时间复杂度都是〇（1）
 而列表从左端 增删的时间复杂度都是〇（n）
 下面介绍deque的一些方法:
"""
from collections import *

dq = deque([1, 2, 3, 4])  # 创建一个deque对象
print(dq)  # >> deque([1, 2, 3, 4])
dq0 = deque([1, 2, 3, 4], maxlen=10)  # 指定队列最大长度，节省内存
print(dq0)  # >> deque([1, 2, 3, 4], maxlen=10)

dq.append(5)  # 在右端追加
print(dq)  # >> deque([1, 2, 3, 4, 5])

dq.appendleft(6)  # 在左端追加
print(dq)  # >> deque([6, 1, 2, 3, 4, 5])

right = dq.pop()  # 在右端弹出元素，没有就报错
print(right)  # >> 5
print(dq)  # >> deque([6, 1, 2, 3, 4])

left = dq.popleft()  # 在左端弹出元素，没有就报错
print(left)  # >> 6
print(dq)  # >> deque([1, 2, 3, 4])

dq.extend([11, 22, 33, 44])  # 在右端合并一个可迭代对象
print(dq)  # >> deque([1, 2, 3, 4, 11, 22, 33, 44])

dq.extendleft([11, 22, 33, 44])  # 在左端合并一个可迭代对象，这里注意，是用迭代器一个个拿元素出来，所以倒叙拼接
print(dq)  # >> deque([44, 33, 22, 11, 1, 2, 3, 4, 11, 22, 33, 44])

dq.rotate(2)  # 把deque当成一个环，向右移动n位
print(dq)  # >> deque([33, 44, 44, 33, 22, 11, 1, 2, 3, 4, 11, 22])

# 其他还有一些方法：clear、remove、index、copy、reverse、insert、count
# 这些方法的用法规则及其效果与列表相同，在此不再赘述
