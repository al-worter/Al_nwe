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

print(re.findall(r'.', info))
print('------------------------------------')
print(re.findall(r'(123|13566667777|12345678911)', info))

# 匹配出电话号码 ： 要求 : 长度11位, 13,15,17,19 全数字组成
print(re.findall(r'1[35789]\d{9}', info))

'''
控制数量的符号
*  匹配0-无限次
+  匹配1-无限次
?  匹配0-1次
非贪婪模式：
    正则表达式的匹配结果默认都是贪婪模式,贪婪模式就是尽可能的往最多的条件去匹配.
    非贪婪模式就是往最少条件去匹配，在*?+后再加一个? 就是代表非贪婪模式
'''
b = "iuef jabaaaaaaaaabbbbbbdklkc.jharcgf"

print(re.findall(r"ab*", b))  # *代表匹配前一个字符0-无限次.
print(re.findall(r"ab*?", b))  # *后面加?代表非贪婪模式,往最少的条件去匹配，匹配结果为 a
print(re.findall(r"ab{0,}", b))  # 代表匹配结果同上

print(re.findall(r"ab+", b))  # 代表匹配1-无限次
print(re.findall(r"ab+?", b))  # 非贪婪模式，匹配结果为ab
print(re.findall(r"ab{1，}", b))  # 代表匹配结果同上

print(re.findall(r"ab?", b))  # ?代表匹配前一个字符 0-1 次
print(re.findall(r"ab??", b))  # 非贪婪模式??代表匹配 a
print(re.findall(r"ab{0,1}", b))  # ?代表匹配前一个字符 0-1 次

# 圆括号:把圆括号里面的内容作为一个整体
c = '4983659758@qq.com 3097534 98466 746545976@qq.com'
# 匹配出里面所有的号， qq号要求必须是以@qq.com结尾. qq长度为6-11位
print(re.findall(r'(\d{6,11})@qq.com', c))  # 把圆括号里面的内容作为一个整体,只匹配出圆括号里面的内容圆括号外面的内容作为附加条件.
print(re.findall(r'((\d{6,11})@qq.com)', c))  # 匹配结果既包含qq邮籍 也包含qq号.

# search () 匹配字符串第一次出现的满足条件
d = "123python123python123python"
print(re.findall(r"python", d))  # findall 匹配出所有满足条件的内容
info = re.search(r"python", d)
print(info)  # search 返回一个对象
print(info.span())  # 使用这个对象调用span方法去提取索引
print(info.group())  # 使用group 方法提取具体内容

# match()
all = re.match(r"123", d)
print(all)  # 如果匹配到了 返回一个对象，如果没有匹配到，返回一个None
print(all.span())
print(all.group())

print(re.findall(r"python", d, re.I))  # 默认是需要区分大小写 , re.I 可以忽略大小写
print(re.findall(r".", d, re.S))  # 是匹配除了换行符以外的任意字符,加上re.S 则可以真正意义上匹配所有字符

# 从字符串“site sea sue sweet see case sse ssee loses se”中匹配出所有s开头，e结尾的单词
a = 'site sea sue sweet see case sse ssee loses se'
# print(re.findall(r"\ss[a-z]*e\s", a))
# print(re.findall(r"\bs[a-z]*e\b", a))  # \b 意思是匹配空白字符或者是空. 匹配的结果不包含空白字符
# 加上\b 就可以吧 打印出来的[' sue ', ' see ', ' sse '] 中空格 去掉
# 输出新的 ['site', 'sue', 'see', 'sse', 'ssee', 'se']

# 校睑用户输入的账号是否满足6-18位，由数字、字母和下划线组成，字母开头，字母或数字结尾
# username = input("输入账号:")
# result = re.findall(r"[a-z][a-z\d_]{4,16}[a-z\d]$", username, re.I)  # 如果匹配成功 返回一个对象，如果匹配失败 返回None
# # print(result.group())
# if result:  # 判断 result  如果是有内容的，会自动转换为布尔值Ture 如果没有内容，会自动转换为Fase
#     print('ok')
# else:
#     print("faild")
# number = '123-6287676 028-2500545 0827-6297696 7654569'
# # 1.区号- 可以有 也可以没有
# # 2. 区号第一位必须是0 长度为3-4位
# #3.  区号和号码 中间必须有-
# # 4 号码第一位必须是 1-9 长度为7位
#
# all = re.findall(r"((\d{2,3}-))")


# 练习:

# 从字符串“site sea sue sweet see case sse ssee loses se”中匹配出所有s开头，e结尾的单词
u = ' site sea sue sweet see case sse ssee loses se'
print(re.findall(r'\bs[a-z]*e\b', u))  # \b匹配除了空格 以外  ， s开头 [a-z]任意字符  *e 无线个e 结尾   \b

re.match(r'(0\d{2,3}-)?[1-9]\d{6}$',u)

# 校验用户输入的账号是否满足6-18位，由数字、字母和下划线组成，字母开头，字母或数字结尾
ul = input('请您输入账号:')
follow = re.findall(r'[a-z]{a-z\d_}{4,16}{a-z\d}$',ul,re.I)
if follow:
    print('请稍等正在登录....')
else:
    print('输入失败,检查是否满足账号是否满足6-18位，由数字、字母和下划线组成，字母开头，字母或数字结尾')
# 判断用户输入的电话是否满足条件:
# 1.区号- 可以有 也可以没有.
# 2.区号第一位必须是0 长度3 - 4位
# 3.区号和号码中间必须有 -
# 4.号码第一位必须1 - 9 长度7位

phone = input('输入电话号码:')
result = re.match(r'(0\d{2,3}-[1-9]\d{6}$)',phone)
if result:
    print('ok')
else:
    print('fail')