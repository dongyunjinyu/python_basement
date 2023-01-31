"""
迭代器的整体作用就是：把可迭代对象（某些容器、和其他一些东西）中的对象一个个拿出来
迭代器就是可迭代对象 内置的一种属性

可以区分 个体 的 集合  叫做一个可迭代对象，比如一个列表，列表里的元素都是相互独立的，没有粘连在一起，列表就是一种可迭代对象
字符串，字典，集合，元组 都是可迭代对象，因为他们里面的元素都是相互独立的
但是一个数字就不是，比如32这个数字就不是可迭代对象，因为没法把它分成3和2，因为他在计算机里是以00100000来储存的，明白？

怎么确定一个对象是不是可迭代的? 比如我们要看一个字符串'hello world'是不是可迭代的
我们可以使用dir函数，这个函数的返回值是其参数的属性和方法，形如'__   __'的就是属性，其他的都是方法
而'__iter__' 就是迭代器属性，我们打印它的属性看看能不能找到'__iter__'
"""
s='hello wrld'
print(dir(s))
# >>>['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
# 我们看到得到一个列表，在里面确实能找到'__iter__'，说明他其中一个属性是迭代，说明他包含迭代器，那么他就是一个可迭代对象
# 嫌眼花找不到，就换个写法
print('__iter__' in dir(s))
# >>>True

func=lambda x,y:x+y*x
print('__iter__' in dir(func))
# >>>False
# 你看，这个函数就不是一个可迭代对象

# 还记得 for 循环怎么写吗？
# for item in iterable object:
# 显然我们不能 for i in 32:    但是可以 for i in range(32):
print('__iter__' in dir(range(32)))
# >>>True
# 果然，range函数的返回值是一个可迭代对象，那么range函数就内置了一个迭代器
r=range(3)
object=r.__iter__()  # 这样object就是range（3）的迭代器
print(object)  # >>> <range_iterator object at 0x0000022799F8F690>      #iterator就是迭代器的意思
print(object.__next__()) # >>> 0
print(object.__next__()) # >>> 1
print(object.__next__()) # >>> 2
# 这就是单步执行迭代器，也可以用内置函数实现这些操作:
object=iter(r)  # 这样object就是range（3）的迭代器
print(next(object)) # >>> 0
print(next(object)) # >>> 1
print(next(object)) # >>> 2
# 如果继续next，那么将会没有对象进行迭代就会报错：StopIteration
# for循环的实质就是先拿到可迭代对象的迭代器，然后进行迭代
# 下面这两段代码是等价的：
######
lst=[0,1,2,3]
for i in lst:
    print(i)
######
lst=[0,1,2,3]
iterator = lst.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
######
# 他们的运行结果都是0\n1\n2\n3\n