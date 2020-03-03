# encoding:utf-8
# 爬取红牛分公司信息，并以表格的形式打印出来
# from Ruby in 20200226 17:22 for study

import requests
import re
import pandas as pd
import bs4

url = r'http://www.redbull.com.cn/about/branch'
response = requests.get(url)

info = {}
# print(response.text)
# 标签清洗 第一种用法，直接用字符串的匹配函数去获取结果
# name = re.findall("data-title='(.*?)'", response.text)
# add = re.findall("data-describe='(.*?)'", response.text)
# mailIco = re.findall("<p class='mailIco'>(.*?)</p>", response.text)
# telIco = re.findall("<p class='telIco'>(.*?)</p>", response.text)

# 第二种 使用bs4包处理 先转换成指定对象，然后使用findAll方法 指定name属性和attrs字典
soup = bs4.BeautifulSoup(response.text)

# telIco = soup.findAll(name='p',attrs={'class':'telIco'})
print(soup.findAll(name='p', attrs={'class': 'telIco'}))
tel = [i.text for i in soup.findAll(name='p', attrs={'class': 'telIco'})]
print(tel, type(tel))
# info = {
#     'name': name,
#     'add': add,
#     'mailIco': mailIco,
#     'telIco': telIco
# }
# print(info)
# info = pd.DataFrame({
#     'add': add,
#     'mailIco': mailIco,
#     'telIco': telIco,
#     'name': name
#
# })
# print(info)
