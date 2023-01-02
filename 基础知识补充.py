"""python入门后，对基础知识进行地毯式补充
                                            作者：苏州大学未来学院 孙海鑫"""
###########################
###### is 与 == 的区别 ######
###########################

'''任何变量都具有三个基本要素：id（地址）、type（类型）、value（值）'''
# a=1
# print(id(a))
'''    >>140731672168112  << 地址'''
# print(type(a))
'''    >><class 'int'>    <<类型'''
# print(a)
'''    >>1      << 值'''

'''"=="比较运算符，用来判断两个变量的值（value）是否相等
"is"同一运算符，用来判断两个变量的地址（id）是否相等
a=1;b=2   或   a='a';b='A'
print(a is b)
    >>False
不能print(1 is 1)会报错，对象得是变量而不是常量'''

'''二者运算结果不尽相同'''
# a=[1,2,3]
# b=[1,2,3]
# print(a is b)
'''    >>False      '''
# print(a==b)
'''    >>True       '''
'''因为python把元组、整型数据、字符数据、字符串数据、浮点数、None 判定为不可变对象，地址固定
而列表、包含列表的元组、字典、包含字典的元组  每次运行程序都会被判定为新对象，地址不固定'''
# a=({'a':(1,)},)
# b=({'a':(1,)},)
# print(a is b)
'''    >>False      '''
# print(a == b)
'''    >>True       '''

# a=1
# b=True
# print(a is b)
'''    >>False      '''
# print(a == b)
'''    >>True       '''

#################################
#########      None     #########
#################################

"""非 是not而不是！
优先级：not > and > or

认识None："""
# if 1==True :
#     print(111)
'''    >>111    '''

# print(not None)
'''    >>True   '''
    
"""判断一个数是否为None
当 x=None，观察以下几种if语句"""
# if x is None:
#     print(111)
'''    >>111    '''
# if not x:
#     print(111)
'''    >>111    '''
# if not x is None:      """is的优先级大于not"""
#     pass
# else:
#     print(111)
'''    >>111    '''
    
'''当x=[]，再观察下列if语句'''
# if x is None:
#     print(111)
'''    >>   '''
# if not x:
#     print(111)
'''    >>111    '''
# if not x is None:
#     pass
# else:
#     print(111)
'''   >>   '''
################
"""第一种if语句最好，为什么？看下面来理解"""
################
# x=None
# y=[]
# print(not y)
'''      >>True     '''        """尤其注意这个"""
# print(not x)
'''      >>True     '''
# print(y is x)
"""      >>False    """
# print(x is x)
"""      >>True     """
# print(y is y)
"""      >>False    """
# print(x == y)
"""      >>False    """
##################    
"""not和in组合表示：不属于"""
# a = 5
# b = [1, 2, 3]
# if a not in b:
#    print(123)
"""     >> 123      """
##################
"""假值：0 [] {} () "" False
认识 and 和 or:
从左到右计算表达式
and若所有的都为真值，则返回最后一个真值; 若存在假值，返回第一个假值
or若所有的都为假值，则返回最后一个假值; 若存在真值，返回第一个真值"""
# print(1 and 2 and 3 and True)
"""    >>True            """
# print(1 and 2 and 3 and 4)
"""   >>4                """
# print([[]] and {} and 1)
"""    >>{}                    [[]] 为真值，长度为零的假值嵌套就成真值了"""

###############################
############ else #############
###############################
"""
# 认识else：
# else除了与if搭配，还可与for、while、try……except搭配
# for、while：当循环顺利地全部执行后，执行一次else，如果全部执行前被break、return，则不执行else
# try..except：是在try中无异常产生时（try完了）执行
# 对比if..else语句，if语句没有执行才执行else，if执行了就不执行else与其他三个相反
# 如：检索一个列表中是否含有至少一个目标元素,返回最前的目标元素所在位置
"""
# def listFind(alist,target):
#     index=0
#     while index<len(alist):
#         if alist[index]==target:
#             break
#         else:
#             index+=1
#     else:
#         index=-1
#     return index
# a=[1,2,3,4,5,6]
# print(listFind(a,9))
'''     >>-1    '''
# print(listFind(a,3))
'''     >>2    '''
