# coding:utf-8
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Map
import jieba
import re
from wordcloud import WordCloud

plt.rcParams['font.sans-serif'] = 'SimHei'

""" 数据预处理 """
data = pd.read_csv('中国大学数据集.csv')
# print(data.columns.tolist())  # 查看数据字段信息（列名称）
# print(data.shape)
print(data.head())
# print(data.loc[data['大学'] == '苏州大学'])
# print(data.info())  # 查看数据的基本信息
# print(data.isnull().sum())  # 查看空值数
data['双一流'] = data['双一流'].fillna('非')
data['隶属于'] = data['隶属于'].fillna('缺失')  # 缺失值处理
data['地址'] = data['地址'].fillna('缺失')
# print(data.isnull().sum())  # 查看空值数
# print(data.duplicated().sum())  # 查看重复值，如果有，可用drop_duplicates()删除，这里没有

""" 可视化分析 """
# 用柱状图分析各大学在中国各个省份分布，并绘制地图

data_province = data['省份'].value_counts().to_frame()  # 对’省份‘字段进行唯一值计数，并将生成的series转换为dataframe
# print(data_province)
# plt.figure(figsize=(12, 8.5))  # 设置图例大小
# plt.bar(x=data_province.index,  # 设置横坐标
#         height=data_province['省份'],  # 设置纵坐标
#         width=0.8,  # 设置柱宽
#         color=['r', 'g', 'b'],  # 设置柱颜色
#         edgecolor='black')  # 设置柱描边颜色
# plt.tick_params(labelsize=13)  # 设置标度字号
# plt.xlabel('省份', size=25)  # 设置横轴名字及其字号
# plt.xticks(rotation=45)  # 设置横轴标度的倾斜度
# plt.ylabel('学校数量', size=25)  # 设置纵轴名字及其字号
# plt.title('中国大学在各个省份分布柱状图', size=15)  # 设置标题
# for a, b in zip(data_province.index, data_province['省份']):
#     plt.text(a, b, '%.0f' % b, ha='center', va='bottom', fontsize=15)  # 显示每个柱体的值
# plt.show()

data_province_series = data['省份'].value_counts()
China_province = ['北京市', '天津市', '上海市', '重庆市', '河北省', '山西省', '辽宁省', '吉林省', '黑龙江省', '江苏省', '浙江省', '安徽省', '福建省', '江西省',
                  '山东省', '河南省', '湖北省', '湖南省', '广东省', '海南省', '四川省', '贵州省', '云南省', '陕西省', '甘肃省', '青海省', '台湾省', '内蒙古自治区',
                  '广西壮族自治区', '西藏自治区', '宁夏回族自治区', '新疆维吾尔自治区', '香港特别行政区', '澳门特别行政区']
province = []
for i in data_province_series.index:
    for j in China_province:
        if i in j:
            province.append(j)
# print(len(province))
data_province_list = []
for i, j in zip(province, data_province_series.tolist()):
    data_province_list.append(([i, j]))
# print(data_province_list)
data_province_map = Map()
data_province_map.add(series_name='学校数量',
                      data_pair=data_province_list,
                      maptype='china',
                      is_map_symbol_show=False)
data_province_map.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
data_province_map.set_global_opts(title_opts=opts.TitleOpts(title='中国大学在各个省份分布地图'),
                                  visualmap_opts=opts.VisualMapOpts(pieces=[{'min': 140, 'color': '#800000'},
                                                                            {'min': 120, 'max': 139,
                                                                             'color': '#B22222'},
                                                                            {'min': 90, 'max': 119, 'color': '#CD5C5C'},
                                                                            {'min': 60, 'max': 89, 'color': '#BC8F8F'},
                                                                            {'min': 1, 'max': 59, 'color': '#FFE4E1'}], is_piecewise=True))
data_province_map.render_notebook()

# 中国大学类型占比饼状图
data_university_type = data['类型'].value_counts()  # 对类型计数
plt.figure(figsize=(10, 10))  # 设置图例大小
plt.pie(data_university_type, labels=data_university_type.index, autopct='%.1f%%')  # 显示值
plt.title('中国大学类型占比', size=25)
plt.show()
