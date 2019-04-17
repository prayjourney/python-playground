# encoding : utf-8
'''
基本语法
一般字符       匹配自身
.             除了换行符之外的任意一个字符
\             转意字符
^             取反, 在方括号之中使用, 如[^\d], 表示非数字 
[...]         方括号之中的范围, 如[a-z], 表示从a-z的一个字符, 也可以是数字
\d            数字
\D            非数字
\s            空白字符
\S            非空白字符
\w            单词字符,[A-Za-z0-9]
\W            非单词字符[^\w]
*             匹配0个或者无限个字符
+             匹配1个或者无限个字符
?             匹配0个或者1个字符
{m}           匹配1个字符m次
{m, n}        匹配1个字符m次至n次, 如果n省略, 则从m次到无限次
^             匹配字符串开头, 多行则每一行都匹配
$             匹配字符串末尾, 多行则每一行都匹配
|             匹配|号左右的任意一个
'''

import re, os, random
import requests

# 打印一个随机数
print(random.randint(1,1000))
print(random.random())


## 正则表达式
# 字符完全匹配
txt = "123 hello world"
regex = "hello"
ss = re.findall(regex, txt)
print(ss)

# 使用简单正则匹配
txt2 = "123 hmmmmello world"
regex2 = "\d{1,4}.*l{2}"
ss = re.findall(regex2, txt2)
print(ss)



txt3 ="100.值十大风口浪尖222.44,你好阿什顿飞1aa156"
regex3 ="\d{1,3}"
result =re.findall(regex3, txt3)
print(result)


# request获取网页源码
# html =requests.get("http://exercise.kingname.info/exercise_requests_get.html")
# html_bytes = html.content
# html_str =html_bytes.decode()
# print(html_str)

# request获取网页源码
# html2 =requests.get("https://www.baidu.com/")
# html_bytes2 = html2.content
# html_str2 =html_bytes.decode()
# print(html_str2)

res = requests.get("https://github.com/timeline.json") 
print(res.text)

# Python包中__init__.py作用
'''
[Python包中__init__.py作用](https://www.cnblogs.com/AlwinXu/p/5598543.html)
总结：
__init__.py的主要作用是:
1. Python中package的标识, 不能删除
2. 定义__all__用来模糊导入
3. 编写Python代码(不建议在__init__中写python模块, 可以在包中在创建另外的模块来写, 尽量保证__init__.py简单)
'''

# 格式化文本或者字符串
# %s是字符串, %d是数字
s123 = "nihoa %s, dsfafdsafasf %s , %d" %("123dsfasf", "ffff", 10)
print(s123)

# 打印一个随机数
print(random.randint(1, 1000))
print(random.random())