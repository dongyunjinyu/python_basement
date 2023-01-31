# 字符串、列表 方法——> .count(obj)
# 返回obj出现的次数
lst=[1, 2, 3, 1, 2, 1]
print(lst.count(1))
# >>>3


# 字符串、列表 方法——> .index(obj,start,end)
# 返回obj第一次出现的位置，检索范围：start到end-1，如果没出现就报错
lst=[1, 2, 3, 1, 2, 1]
try:
    print(lst.index(1,5,-1))
except ValueError:
    print('not in')
# >>>not in