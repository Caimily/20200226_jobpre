# encoding:utf-8
# 爬取链家二手房（租房）信息，并以表格的形式打印出来
# from Ruby in 20200226 17:36 for study

import requests
import bs4
import re
import pandas as pd

url = r'https://sz.lianjia.com/zufang/kejiyuan/'
Headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'
}
response = requests.get(url, headers=Headers)
# print(response.text)

soup = bs4.BeautifulSoup(response.text)
# <a target="_blank" href="/zufang/SZ2396519582631198720.html">
#            整租·万科蛇口公馆 1室1厅 南        </a>
# name = [i.text for i in soup.findAll(name= 'a',attrs={'data-el':'region'})]
region = re.findall('<a title=".*?" href=".*?" target="_blank">(.*?)</a>', response.text)
regionset = []
# 对结果去重
for i in range(len(region)):
    if region[i] in regionset:
        continue
    else:
        regionset.append(region[i])

# <span class="content__list--item-price"><em>2200</em> 元/月</span>
price = [i.text.strip() for i in soup.findAll(name='span', attrs={'class': 'content__list--item-price'})]
print(len(price),len(regionset),regionset,price)
# pd.DataFrame({'regionset':regionset,'price':price})

