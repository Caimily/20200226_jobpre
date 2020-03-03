# https://sz.zufang.zhuge.com/
# encoding:utf-8
# 爬取链家二手房（租房）信息，并以表格的形式打印出来
# from Ruby in 20200226 18:48 for study

import requests
import bs4
import re
import pandas as pd

url = r'https://sz.zufang.zhuge.com/'
Headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36',
    'Referer': 'https://sz.zufang.zhuge.com/',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Cookie': '_WEB_houseType=zufang; _WEB_token=Rod51ubHcHV-Cqt797APxi7SFDnjgOyhifffBTxKr24czjv6aX2__TIJCOkGcXoVQm8ZKHaMDtQBksLcgJtHLg%3D%3D; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22170811b15587f9-0a09441446b37a-4e450d28-1764000-170811b155973a%22%2C%22%24device_id%22%3A%22170811b15587f9-0a09441446b37a-4e450d28-1764000-170811b155973a%22%2C%22props%22%3A%7B%7D%7D; _ga=GA1.2.1803018455.1582714001; _gid=GA1.2.957986112.1582714001; Hm_lvt_8d409b931bc5e2ac53a0cea966f06d99=1582714004; acw_tc=2760822215827140097457183ec1b3b0409d21312cafa9bb802c3e8bc9043f; acw_sc__v2=5e564c991be89c18d608e9774b06426d7629ea2c; acw_sc__v3=5e564c9b30c39f9111e389d209c83e8e47ab8372; _WEB_city_code=sz; _WEB_cityid=3; _WEB_city_name=%E6%B7%B1%E5%9C%B3; TY_SESSION_ID=629f3851-c4de-41cc-b4ca-0bca7ffd3098; Hm_lpvt_8d409b931bc5e2ac53a0cea966f06d99=1582714015; SERVERID=08fd1ed0c068bbe9ddab22f50cdfb52d|1582714014|1582714011'
}
response = requests.get(url, headers=Headers)
print(response.text.decode('utf-8'))

soup = bs4.BeautifulSoup(response.text)
# <a href="//sz.zufang.zhuge.com/q1016366/" class="area_class">中粮祥云广场</a>
region = [i.text for i in soup.findAll(name='a', attrs={'class': 'area_class'})]
price = [i.text.strip() for i in soup.findAll(name='span', attrs={'class': 'list-table-price-box'})]
# class="list-table-price-box"
print(region, price)
