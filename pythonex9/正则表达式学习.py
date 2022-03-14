# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/14 16:10
# @Author   : Jing wen
# @Site     : http://www.cdtest.cn/
# @File     : 正则表达式.py
# @Software : PyCharm

'''
标准库: python 自带的模块
第三方库 : 需要下载安装，然后再导入
正则表达式需要使用re标准库
    常用方法:
        1）re.findall() 匹配出所有满足条件的的结果. 里面必须传入两个参数,第一个是正则表达式,第二个是要匹配的字符串.
        2）
        3）
'''
# 标注库正则不需要导入 直接import

import re  # 先导入re标准库

str1 = 'aabaasisfhAabbfdhauabkaekaaaa'
str2 = "isfhjoreit"
str3 = "str3 122aa 45_Altub\n78*哈哈#%aubabc"
print(re.findall(r'abs', str1))  # 匹配出所有的ab以一个列表的格式返回.
print(re.findall(r"a", str2))  # 如果字符串里面没有ab 则返回一个空列表.
print(re.findall(r"^ab", str1))  # #“代表开头瞭这里是匹配字符串是以^ab开头,如果是以ab开头,返回ab,如果不是,则返回一个空列表.
print(re.findall(r"ab$", str3))  # $代表结尾﹑这里是匹配字符串是以ab结尾,如果是,返回ab,如果不是,则返回一个空列表.
print(re.findall(r"^ab$", str1))  # 如果两个符号同时使用,代表必须完全匹配
print(re.findall(r"a[beu]", str1))  # []代表选择匹配括号里面的任意一个内容这里代表匹配ab或者ae或者au
print(re.findall(r"a{1,3}", str1))  # {} 代表控制前一个字符的数量
print(re.findall(r"ba{1,3}", str1))  # 这里代表匹配ba或者baa或者baaa
print(re.findall(r"ba{2}", str1))  # #如果{}里面只写一个数,代表匹配前一个字符的固定个数.这里匹配ba
print(re.findall(r"ba{2,}", str1))  # #如果{}里面只写一个数加逗号,代表匹配最多最多无限个.这里匹配ba
print(re.findall(r"\d", str3))  # \d 匹配数字
print(re.findall(r"\d\d", str3))  # \d\d匹配数字
print(re.findall(r"[0-9]", str3))  # 这样写也是匹配数字
print(re.findall(r"[a-z]", str1))  # 这样写是匹配所有小写字母
print(re.findall(r"[a-zA-Z]", str3))  # 匹配大小写字母
print(re.findall(r"\s", str3))  # \s 匹配空白字符 包含空格 , \n \t
print(re.findall(r"\w", str3))  # \w 匹配数字下划线和汉字.
print(re.findall(r"[a-zA-Z\d_]", str3))  # 匹配字母数字下划线  中括号匹配到
print(re.findall(r".", str3))  # 匹配除了换行符的任意内容
print(re.findall(r"\*", str3))  # 因为*在正则里是有特殊意义的,如果要匹配*需要在前面加\
print(re.findall(r"\.", str3))  # #*+ ?.这些都是有特殊意义的字符.如果要匹配都需要加\
print(re.findall(r"[^0-9]", str3))  # 出现在[] 里面，代表取反的意思，这里代表选择匹配除了数字的任意字符
print(re.findall(r"[^a-z]", str3))  # 匹配除了字母以外的任意字符
print(re.findall(r"[^a]", str3))  # 匹配除了a以外的任意字符
print(re.findall(r"(22|23)", str3))  # | 该符号 是选择匹配整体   [] 中括号是只能选择匹配一个
print(re.findall(r"(aa|bc)", str3))  # 匹配aa 或 bc

print('------------------------------------')
# 练习:从 info = 'my phone number is 123 13566667777 12345678911’里面匹配出电话号码.
info = 'my phone number is 123 13566667777 12345678911 13566667777 12345678911 13899998888'

print(re.findall(r'.',info))
print('------------------------------------')
print(re.findall(r'(123|13566667777|12345678911)',info))

# 匹配出电话号码 ： 要求 : 长度11位, 13,15,17,19 全数字组成
print(re.findall(r'1[35789]\d{9}',info))

