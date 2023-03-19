"""
python具有大量的第三方库（library），或者叫模块（module）,或者叫包（package）
如何安装？
1.使用集成工具自带安装器安装
2.使用pip，有的人第一次用会遇见各种坑，解决起来比较复杂；如果没有遇见坑那自然很简单
3.官网下载，我不会

现在我们选用第一种安装方法安装，以pycharm为例，左上角  文件（file）—— 设置（setting）—— 项目（project） —— python解释器
点击“+”，搜索想要安装的库，由于库很多，一定要输入正确
在右边指定安装版本，一般安装最新的三版
然后在“选项”内，输入：-i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com
这一步是将下载地址改到了国内，否则不是下不了就是下的慢
pycharm界面最下方读条完成后即安装成功
"""
#记录本项目已经安装的包：numpy，matplotlib，torch，paddlepaddle-gpu，scipy，ipython，sympy

############### 使用 #############
"""
我们要使用库里的函数，需要通过语法来实现

如果你在你的项目中暂时不确定要使用 库 里的哪个函数，语法：
import 库名
如 import numpy
之后要使用里面的函数就用“numpy.函数（参数）”的格式来使用
如print(numpy.zeros(10)),打印一个十维零向量

用as关键字可以给numpy起个别名，语法：
import 库名 as 别名
如 import numpy as np
这样我们再使用库函数就能少输一些字
如 print(np.zeros(10))

如果你还觉得麻烦，就用：
from 库名 import *
如 from numpy import *
这样就可以不加前缀直接用库里的函数
如 print(zeros(10))
但是要注意，这样做会污染命名空间，如果你只导入了一个库做一个小工程那是可以的
但是加入你要做一个大工程，你会导入很多库，你还这样做，这时你想，如果两个库里有同名的函数怎么办？
或者库里的函数跟你自己def的函数重名了怎么办？因为你记不住你导入的库里所有函数的名字
所以这时就不要这样做

为了防止命名空间被污染，我们一般这么做：
from 库名 import 函数名
比如我现在要做一个项目，这个项目要用到numpy库，但是我不知道接下来我要用到哪些函数
那我可以先 import numpy as np
然后进行编程，这个文件写完之后，我把里面用到的所有np函数名记下来，然后把上面这个import换成：
from numpy import zeros，ones，empty

导入多个模块:
import numpy as np, matplotlib as plt,……

"""
# 此外，库的学习目前建议在交互式python控制台进行，ipython也不错
# ipython也是一个库，用上面的方法下载就行，下载完成，打开下方”python 控制台“看见In的字样就是
# 所谓控制台，我的理解就是启用一大块内存，并且这块内存一直分配给控制台，只要你不关控制台内存就一直是它的
# 和.py文件不一样，py文件所占内存的生命周期是 从开始运行到运行结束，就唰的一下子就没了
