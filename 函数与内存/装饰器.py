###################################
#  学习这一块知识，请先学习函数相关知识

"""
请先尝试理解：python中一切皆变量。并且试图将函数理解成为“变量——值”的形式（也即“引用——对象”）
如果你充分理解了，那么以下预备知识想必难不倒你：
    1.函数可以作为参数进行传递
    2.函数可以作为返回值进行返回
    3.函数可以进行赋值
"""
#装饰器代码：
#创建装饰器：
"""
def 装饰器名(function):
    def inner(*args,**kwargs):
        pass
        ret=function(*args,**kwargs)
        pass
        return ret
    return inner
"""
#使用装饰器：
"""
@装饰器名
def 被装饰函数名(自定义参数)
    pass
"""


