# 严格的讲，分治，分而治之，是一种思想、策略，而非算法
# 其英文：divide and conquer    简称：D&C
# 分治算法使用递归，递归中基线条件和递归条件，其中满足基线条件就return，满足递归条件就递归
# 递归的核心思想是：数学归纳
# 思想：
# 1.找出简单得基线条件
# 2.确定如何缩小问题的规模，使其符合基线条件


# 例1：
# 已知一个 a*b 的长方形，如何将其分成若干大小相等的正方形，并且使正方形尽可能大？
# 确定基线条件：当a与b其中一个整除另一个时
# 方法：欧几里得算法
def square(a, b):
    return square(b % a, a) if b % a else a


print(square(640, 1680))


# 例2：重写sum()函数
# 基线条件：sum的对象没有元素
def my_sum(arr):
    return arr[0] + my_sum(arr[1:]) if arr else 0


print(my_sum([1, 2, 3, 4, 5, 6]))


# 例3：二分查找
def second_search(arr, item):
    low = 0
    high = len(arr)

    def inner(arr, item, low, high):
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == item:
                return mid
            elif item < arr[mid]:
                return inner(arr, item, low, mid - 1)
            elif item > arr[mid]:
                return inner(arr, item, mid + 1, high)
            return None

    return inner(arr, item, low, high)


print(second_search([1, 5, 6, 99, 511, 644, 755], 511))


# 例4:阶乘
def fac(n):
    return n * fac(n - 1) if n else 1


print(fac(5))


# 例5:最小数
def find_min(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] < arr[1] else arr[1]
    else:
        return arr[0] if arr[0] < find_min(arr[1:]) else find_min(arr[1:])


print(find_min([9, 1, 2, 5, 7, 9, 0]))


