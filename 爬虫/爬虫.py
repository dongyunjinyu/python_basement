"本项目用于本人学习python爬虫使用，任何对网站的违法爬取均由使用者个人承担法律责任，与本人没有法律关系"
from urllib.request import urlopen
url='https://www.bilibili.com/'
response=urlopen(url)
with open('bili.html',mode='w',encoding='utf-8') as f:
    f.write(response.read().decode('utf-8'))
    print('over')