# coding = utf-8
"""
网络上下载一张图片
"""

import re
import requests
import os
from bs4 import BeautifulSoup

url = 'https://pixabay.com/'
html = requests.get(url).text  # 获取网页内容
print(html)
# 这里由于有些图片可能存在网址打不开的情况，加个5秒超时控制。
# data-objurl="http://pic38.nipic.com/20140218/17995031_091821599000_2.jpg"获取这种类型链接
soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
# ^abc.*?qwe$
pic_url = soup.find_all('img', src=re.compile(r'^https://cdn.pixabay.com/photo/.*?jpg$'))
# pic_url = pic_node.get_text()
# pic_url = re.findall('"https://cdn.pixabay.com/photo/""(.*?)",',html,re.S)
print(pic_url)
i = 0
# 判断image文件夹是否存在，不存在则创建
if not os.path.exists('image'):
    os.makedirs('image')
for url in pic_url:
    img = url['src']
    try:
        pic = requests.get(img, timeout=5)  # 超时异常判断 5秒超时
    except requests.exceptions.ConnectionError:
        print('当前图片无法下载')
        continue
    file_name = "image/" + str(i) + ".jpg"  # 拼接图片名
    print(file_name)
    # 将图片存入本地
    fp = open(file_name, 'wb')
    fp.write(pic.content)  # 写入图片
    fp.close()
    i += 1
