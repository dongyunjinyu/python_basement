###########################################################################################################
###############################      排序算法详解与python代码实现      #########################################
###############################      作者:孙海鑫  苏州大学未来学院      #########################################
###########################################################################################################

#########################
### 准备阶段，定义一些函数 ###
#########################

######  生成随机数列，用来实现算法   ######
from random import randint #从random库里导入randit函数，如果是import*就是导入所有函数
#randint(min,max)的返回值为min~max的一个随机数，包括min和max
def randArr(min,max,n): #该函数返回一个列表形式的数列，含有n个整数，范围min~max
    return [randint(min,max)for x in range(n)]

######  生成有序的数列   ######
def orderedArr(min,max):
    return [i for i in range(min,max+1)] #返回一个有序连续数列，如：3456789

######  生成基本有序的数列    ########
def nearlyOrdArr(min,max,swapTime):
    arr=[i for i in range(min,max+1)] #得到一个有序的数列。如：3456789
    for j in range(swapTime): #对换j次
        posix=randint(0,max-min) #随机地得到被对换元素的位置
        posiy=randint(0,max-min)
        arr[posix],arr[posiy]=arr[posiy],arr[posix] #对换
    return arr #返回被对换j次后的数列

########   判断一个数列是否升序排列（是否有序）  #######
def isSorted(lst):
    for i in range(len(lst)-1):  #迭代
        if lst[i]>lst[i+1]:  #一旦出现前一项大于后一项的情况
            return False  #直接判定为无序，返回false结束程序
    return True  #迭代完后，一直没有出现逆序的情况，视为True，13579也是True


#########   判断算法是否排序成功  不成功就报错    ########
def testSort(func, alist):   #func表示要检测的算法函数，alist为传入的数列
    alist=func(alist) #需要定义全局变量alist，在运行时间标准检验阶段，我们定义的全局变量为randArr(0,9,20)
    assert isSorted(alist), "排序算法错误\n"  # assert 后的表示式的值若为False，则报错，并提示报错信息

######### 目标要超越的算法：python自带sort函数  #########
def sort(alist): #成绩：0.1 s
    alist.sort()
    return alist


#########   算法优化   ###########
#索引会拖慢速度，能少索引就少索引


##################################################################################################################
######################################   正式阶段，下面式是经典的排序算法   #############################################
##################################################################################################################


###################################   冒泡排序   ####################################
def bubbleSort(alist): #成绩：1.05 s
    n = len(alist)
    for i in range(n-1, 0, -1): #假设n=10，则 i=9，8，7，6，5，4，3，2，1，0
        for j in range(0, i): #通过遍历，使第i位为数列中最大的数
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
    return alist

def bubbleSort1(alist): #升级版，成绩：0.2 s
    n = len(alist)
    for i in range(n-1, 0, -1):
        xu = True #作为是否正序的标志
        for j in range(0, i):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
                xu=False #发生了一次交换，说明还没有正序
        if xu: #每次排好一个数，都检查一次，如果已经正序，则直接结束
            break
    return alist
####################################################################################


###################################  选择排序  #######################################
def selectionSort(alist): #成绩：0.85 s
    n=len(alist)
    for i in range(n-1): #选出第i位及以后中的最小值放到第i位
        min_value, min_index = alist[i], i #初始化默认第i位为最小位
        for j in range(i+1,n): #遍历第i位之后的数
            if min_value>alist[j]: #如果有数比当前最小值小
                min_value,min_index=alist[j],j #记下这个数的索引，同时把这个数也记下来以减少额外的索引
        alist[i],min_value=min_value,alist[i] #遍历一遍后，找到了最小值，交换
    return alist
#####################################################################################


##################################   插入排序   #######################################
def insertionSort(alist): #成绩：0.22 s
    for i in range(1,len(alist)):
        value=alist[i] #把第i个数先拿出来暂存给value
        pos=i
        while alist[pos-1]>value and pos>0: #倒着找，找到第i位前面第一个不大于value的数；不能用>=,慢
            alist[pos]=alist[pos-1] #把左边的数整体右移一位；不用insert函数，太慢
            pos-=1
        alist[pos]=value #然后用value覆盖目标位置，造成插入效果
    return alist
#############################################################################


#############################  希尔排序  ######################################
def gapInsetionSort\
                (alist,startpos,gap):
    for i in range(startpos+gap,len(alist),gap):
        position=i
        currentvalue=alist[i]
        while position>startpos and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position=position-gap
        alist[position]=currentvalue
def shellSort(alist):
    gap = len(alist) // 2
    while gap > 0:
        for i in range(gap):
            gapInsetionSort(alist, i, gap)
        gap = gap // 2
    return alist



hanshu=shellSort


##############################################################################


##############################   归并排序  #####################################
# 合并有序数列alist[start....mid] 和 alist[mid+1...end]，使之成为有序数列
def merge(alist, start, mid, end):
    # 复制一份
    blist = alist[start:end+1]
    l = start
    k = mid + 1
    pos = start

    while pos <= end:
        if (l > mid):
            alist[pos] = blist[k-start]
            k += 1
        elif (k > end):
            alist[pos] = blist[l-start]
            l += 1
        elif blist[l-start] <= blist[k-start]:
            alist[pos] = blist[l-start]
            l += 1
        else:
            alist[pos] = blist[k-start]
            k += 1
        pos += 1

def insertionSortHelp(alist,l, r):
    for i in range(l+1,r+1):
        currentvalue=alist[i]
        position=i
        while alist[position-1]>currentvalue and position>l:
            alist[position]=alist[position-1]
            position=position-1
        alist[position]=currentvalue
    return alist
def __mergeSort(alist, start, end):
    #当数列的大小比较小的时候，数列近乎有序的概率较大
    if (end-start <= 15):
        insertionSortHelp(alist, start, end)
        return

    if start >= end:
        return
    # 存在风险，start+end可能越界
    mid = (start + end) // 2
    # mid = start + (end - start) // 2
    __mergeSort(alist, start, mid)
    __mergeSort(alist, mid + 1, end)
    #优化
    if alist[mid] > alist[mid+1]:
        merge(alist, start, mid, end)
def mergeSort(alist):
    n = len(alist)
    __mergeSort(alist, 0, n-1)
    return alist

def mergeBU(alist): #非递归
    n = len(alist)
    #表示归并的大小
    size = 1
    while size <= n:
        for i in range(0, n-size, size+size):
            merge(alist, i, i+size-1, min(i+size+size-1, n-1))
        size += size
    return alist
###############################################################################


############################  快速排序  ##################################
# 在alist[l...r]中寻找j,使得alist[l...j] <= alist[l], alist[j+1...r] >alist[l]
def partition(alist, l, r):
    pos = randint(l, r)
    alist[pos], alist[l] = alist[l], alist[pos]
    v = alist[l]
    # v = alist[l]
    j = l
    i = l + 1
    while i <= r:
        if alist[i] <= v:
            alist[j+1],alist[i] = alist[i],alist[j+1]
            j += 1
        i += 1
    alist[l], alist[j] = alist[j], alist[l]
    return j
def __quickSort(alist, l, r):

    #当数列的大小比较小的时候，数列近乎有序的概率较大
    # if (r - l <= 15):
    #     insertionSortHelp(alist, l, r)
    #     return

    if l >= r:
        return
    # p = partition(alist, l, r)
    p = partitionQS(alist, l, r)

    __quickSort(alist, l, p-1)
    __quickSort(alist, p+1, r)



##############################################################################
##########   运行时间标准检验阶段   以一个有20个0~9随机排列的数组为检测基准     ##########
##############################################################################
import timeit
#hanshu=insertSort             #在等号后输入要检测时间的函数名，然后运行
alist=randArr(0,9,20)  # 生成随机数列，用来检测算法运行时间
t=timeit.Timer('testSort(hanshu, alist)', 'from __main__ import testSort, hanshu, alist') #设置计时器
print(f'该排序算法运行时间：{t.timeit(number=100000)} s')  #打印:该排序运行十万次所花费的时间