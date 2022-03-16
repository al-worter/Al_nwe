# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/10 13:55
# @Author   : Jing wen
# @Site     : http://www.cdtest.cn/
# @File     : 字符串study.py
# @Software : PyCharm

# 7.1 字符串
# 字符串是不可变序列，也是一种数据结构。
#7.1.1字符串
# str1 = 'hello,朋友友潘佳梅'
# print(str1[0])
# for i in str1:
#     print(i,end=' ')
# print(len(str1))
# 字符串的 切片是 以冒号 ： ： 为标志。
# print(str1[::4])
# print(str1[6:10])
# print(str1[::5])

# 字符串的拼接
# str1 = '您好'
# str2 = '潘佳梅'
# str3 = str1 + str2
# print(str3)

# 字符串的分割与拼接
# 意思是L:将字符串根据指定符号分割为列表
str1 = '汇智动力官网： http://www.hzdledu.com'
list1 = str1.split()
print(list1)
list2 = str1.split('/')
print(list2)
list3 = str1.split('.')
print(list3)
print('-------------------------------')
# # 拼接 ：是将元素为字符串的列表拼接为字符串，是split的反向操作  例如：list = [] ;str = str.split('') 分割
# list1 = ['汇智动力官网：', 'http://www.hzdledu.com']
# str1  = ' '.join(list1)     #例如：list = [] ;str = ''.join(list1) 拼接分割的列表
# print(str1)
# list2 = ['汇智动力官网： http:', '', 'www.hzdledu.com']
# list2 = '/'.join(list2)
# print(list2)
#
# # 字符串的 检索 有三种
# # str: 原字符串 ；
# # 1.count() 查看有该字符串有几个。  2.find() 查询并返回该字符串首字母的index值  3.index()
# str1 = '汇智动力官网: http://www.hzdledu.com'
# print(str1.count(':'))
# print(str1.count(':',0,5))
# print(len(str1))
# print(str1.find('www')) # 返回字符串首字母的index
# print(str1.find('www',0,6)) # 没有找到的时候返回 -1
# print(str1.index('.'))
#
# # 7.1.4 去除字符串两边的特殊字符串
# str1 = '...http://www.hzdledu.com...'
# print(str1.lstrip('.'))
# print(str1.rstrip('.'))
# print(str1.strip('.'))
