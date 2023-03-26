import inspect
import numpy

source = inspect.getsource(numpy.sum)
print(source)
# 查看函数源代码
