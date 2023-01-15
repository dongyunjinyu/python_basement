#列表会预留内存空间，而元组不会，所以如果变量数量确定就尽量用元组
#元组与列表的区别在于：元组比列表的运算速度快，而且元组的数据比较安全。元组是不可改变的，为了保护其内容不被外部接口修改，不具有 append，extend，remove，pop,index这些功能；而列表是可更改的。所有有些时候我们需要两者相互转换，tuple()相当于冻结一个列表，而list（）相当于解冻一个元组。冻结吧~
#元组有序，逗号其实就是一种元组
#比如交换顺序：
#a,b=b,a
#其实就是(a,b)=(b,a)


#定义一个元组：
a=(1,2)
a=1,2
lst=[1,2];a=tuple(lst)
print(a)
print(a,'a',type(a))


#创建字典
dic={'jia':12,'yi':14}
#dic=dict()#这里面放别的容器，但是元素是若干个元组，每个元组有两个元素，第一个是键，第二个是值
#比如
lst=[('a',1),('b',2),('c',3),('d',4)]
dic=dict(lst)
print(dic)
#字典的增删改查都是通过key来索引的，key是可哈希的一个值
dic={'a': 1, 'b': 2, 'c': 3, 'd': 4}

dic['e']=5  #增
print(dic)

print(dic['a'])    #查
key='f'
if key in dic:      #如果键不存在会报错，所以先检查键是否存在
    print(dic[key])
else:print("该键不存在")

dic['e']=5     #改
print(dic)

del dic['e']    #删
print(dic)

for key in dic:    #遍历
    print(dic[key])

print(dic.values())  #值函数，将所有的值放到一个特殊的列表里
print(type(dic.values()))   #    dict_values
for value in dic.values():    #这样就遍历了字典的值
     print(value)

for item in dic.items():   #遍历获取key和value
    print(item)
    #  >>>('a', 1)
    # ('b', 2)
    # ('c', 3)
    # ('d', 4)      #以元组的形式打印出来的
for key,value in dic.items():  #拆开获得的元组
    print(key)
    print(value)