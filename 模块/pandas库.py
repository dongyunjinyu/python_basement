# pandas基于numpy设计，并加入了更多的高级数据结构以及操作工具，进一步简化了numpy的运算与应用


from pandas import Series, DataFrame
import pandas as pd
import numpy as np

#######################################
##############  高级数据结构  ############
#######################################
obj = Series([2, 5, 7, -2])
print(obj)
# 0    2
# 1    5
# 2    7
# 3   -2
# dtype: int64
print(obj[2])  # 7

obj1 = Series([2, 5, 7, -2], index=['a', 'b', 'c', 'd'])
obj.index = ['a', 'b', 'c', 'd']
print(obj1)
# a    2
# b    5
# c    7
# d   -2
# dtype: int64
print(obj1['b'])  # 5
print(obj['b'])  # 5

data = {
    'name': ['Tom', 'Marry', 'Herry'],
    'year': [1996, 1997, 1998],
    'grade': [86, 79, 93]
}
frame = DataFrame(data)  # 还可以用columns参数指定列顺序，如columns=['year','grade','name']
print(frame)
#     name  year  grade
# 0    Tom  1996     86
# 1  Marry  1997     79
# 2  Herry  1998     93
print(frame['name'])
# 0      Tom
# 1    Marry
# 2    Herry
# Name: name, dtype: object

########################################
############  csv文件  ##################
########################################
df = pd.DataFrame(pd.read_csv('睡眠中的人体压力检测数据集.csv'))
print(df['sl'][3])  # 索引
print(df.shape)  # 查看维度
print(df.info())  # 查看数据表基本信息：维度，列名称，数据格式，所占空间
print(df.dtypes)  # 每一列数据的格式
print(df['sl'].dtype)  # 某一列的格式
print(df.isnull())  # 空值
print(df['sl'].isna())  # 查看某一列空值
print(df['sl'].unique())  # 查看某一列的唯一值
print(df.values)  # 查看数据表的值
print(df.columns)  # 查看列名称
print(df.head(7))  # 查看前n行数据，默认为5行
print(df.tail())  # 查看后n行数据，默认为5行
# 数据表清洗：
print(df.fillna(value=0))  # 用0填充空值
print(df['sl'].fillna(df['sl'].mean()))  # 使用某一列的均值对空值进行填充
print(df['sl'].astype(str))  # 更改数据格式
df['sl'] = df['sl'].map(str.strip)  # 清除某一字段的字符空格，数据需是str
df['sl'] = df['sl'].str.lower()  # 某一字段的数据进行大小写转换
print(df.rename(columns={'某一列原来的名称': '新'}))  # 更改列名称
print(df['sl'].drop_duplicates())  # 删除 后出现的重复值
print(df['sl'].drop_duplicates(keep='last'))  # 删除 先出现的重复值
print(df['sl'].replace('old data', 'new data'))  # 数据替换
# 数据预处理：
print(df.merge(df, df, how='inner'))  # 数据表取交集
print(df.merge(df, df, how='outer'))  # 数据表取并集
print(df.append(df))  # 数据追加
print(df.join(df, on='key'))  # 加入（按特定索引），缺值为NaN
print(pd.concat([df, df, df]))  # 灵活合并
print(df.set_index('sl'))  # 设置某一字段为索引，如日期
print(df)  # 按照特定列的值排序
print(df)  # 按照索引列排序
print(df)  # 新建一个列作标记，如果某一列的某一个数据大于某值，标记列对应变为规定值
print(df)  # 对复合多个条件的数据进行分组标记
print(df)  # 分列，创建数据表
print(df)  # 匹配
print(df[:'xxx'])  # 提取xxx之前的数据，如提取‘2023-01-04’之前的所有数据
print(df.iloc[::])  # 即使数据是字符索引，仍然按位置来索引
print(df.ix[:'3day', :4])  # 混合索引,3day前且前四行
print(df.loc[df['sl'].isin(['beijing', 'shanghai'])])  # 判断一个字段中是否包含某些数据，然后这些数据提取出来
# 数据筛选：
print(df.loc[(df['sl'] > 2) & (df['rr'] == 'beijing')])  # 与
print(df)  # 或
print(df)  # 非
print(df.query('sl == ["xxx"]'))  # 用query函数进行筛选
print(df.query('sl == ["xxx"]').sl.sum())  # 对筛选结果按某一字段进行求和
# 数据汇总：
print(df.groupby('sl').count())  # 对所有列进行计数汇总
print(df.groupby('sl')['rr'].count())  # 按xxx对某一字段进行计数
print(df.groupby(['sl', 'rr'])['rr'].count())  # 对两个字段进行汇总计数
print(df.groupby('sl')['rr'].agg([len, np.sum, np.mean]))  # 对某一字段进行汇总，并计算某一字段的合计和均值
# 数据统计：
print(df.sample(n=3))  # 数据采样
print(df.sample(n=4, weights=[0, 0, 0, 0, 0.5, 0.5]))  # 设置采样权重
print(df.sample(n=6, replace=False))  # 采样后不放回,默认
print(df.sample(n=6, replace=True))  # 采样后放回
print(df.describe().round(2).T)  # 数据表描述性统计
print(df['sl'].std())  # 计算列的标准差
print(df['sl'].cov(df['rr']))  # 计算两个字段间的协方差
print(df.cov())  # 所有字段间的协方差
print(df['sl'].corr(df['rr']))  # 两个字段的相关性分析
print(df.corr())  # 数据表的相关性分析
# 数据输出：
df.to_excel('xxx.xlsx', sheet_name='xxx')  # 写入excel
df.to_csv('xxx.csv') # 写入csv


