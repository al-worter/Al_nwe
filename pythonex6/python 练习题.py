# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/11 14:34
# @Author   : Jing wen
# @Site     : http://www.cdtest.cn/
# @File     : python 练习题.py
# @Software : PyCharm

# 一、打印九、九、乘法表
# 方法1
# for i in range(1, 10):
#     for j in range(i):
#         j = j + 1
#         print("%d*%d=%-3d" % (i, j, i * j), end="")
#     print("")
#
# # 方法2
# i = 1
# while i < 10:
#     j = 1
#     while j <= i:
#         print("%d*%d=%d\t" % (j, i, j * i), end="")
#         j += 1
#     print()
#     i += 1
#
# # 方法3
# def multiplication_table(n):
#     if n < 1:
#         return
#     multiplication_table(n - 1)
#     for m in range(1, n + 1):
#         print("%d*%d=%d" % (m, n, m * n), end="\t")
#     print()
# multiplication_table(9)

#  判断是否闰年
'''
用函数实现一个判断用户输入的年份是否是闰年的程序
1.能被400整除的年份
2.能被4整除，但是不能被100整除的年份
以上2种方法满足一种即为闰年
'''
# def leapyear(year):
#     if year%400==0 or (year%4==0 and year%100!=0):
#         print("%d是闰年"%year)
#     else:
#         print("%d不是闰年"%year)
#
# leapyear(int(input("请输入年份：")))

# 闰年：能被4整除不能被100整除或者能被400整除
# 口诀：4年一闰，百年不闰，400年又闰
import random

# year = int(input('请输入一个年份：'))
# while year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print(str(year), '该年份是闰年')
# else:
#     print(str(year),'该年份是平年')

# 方法二： if
# year = int(input('请输入一个年份：'))
# if (year %4) == 0:
#     if (year% 100) == 0:
#         if (year% 400 ) == 0:
#             print(f'该年份是闰年：{year}年') #整 百年能被400整除的事实闰年
#         else:
#             print(f'该年份是平年：{year}年')
#     else:
#         print(f'该年份是闰年：{year}年') # 非整百能被4整除的为闰年
# else:
#     print(f'该年份是平年:{year}年')

# 方法三： while -if 结合
# 三中情况 为负数的时候，为零的时候，大于零的情况
# Year = int(input('请输入年份：'))
# while str(Year) != 'over':
#     year = int(Year)
#     if year > 0:
#         if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#             print(str(year) + '年是闰年')
#         else:
#             print(str(year) + '年是平年')
#     elif year < 0:
#         if (year + 1) % 4 == 0 and (year + 1) % 100 != 0 or (year + 1) % 400 == 0:
#             print('公元前' + str(-year) + '年是闰年')
#         else:
#             print('公元前' + str(-year) + '年是平年')
#     else:
#         print('年份不能为零，请重新输入')
#     print('------------')
#     Year = input('请输入年份(over退出)：')
#     print('退出，已结束！')

# '''
# 根据第18位校验码判断身份证是否输入正确
# 1、将前面的身份证号码17位数分别乘以不同的系数。从第一位到第十七位的系数分别为：7－9－10－5－8－4－2－1－6－3－7－9－10－5－8－4－2。
# 2、将这17位数字和系数相乘的结果相加。
# 3、用加出来和除以11，看余数是多少？
# 4、余数只可能有0－1－2－3－4－5－6－7－8－9－10这11个数字。其分别对应的最后一位身份证的号码为1－0－X－9－8－7－6－5－4－3－2。
# 5、通过上面得知如果余数是2，就会在身份证的第18位数字上出现罗马数字的Ⅹ。如果余数是10，身份证的最后一位号码就是2。
# 例如：某男性的身份证号码是34052419800101001X。我们要看看这个身份证是不是合法的身份证。
# 首先我们得出前17位的乘积和是189，然后用189除以11得出的结果是17+2/11，也就是说其余数是2。最后通过对应规则就可以知道余数2对应的数字是x。所以，可以判定这是一个合格的身份证号码。
# '''
# lis = list(input('请输入身份证号码：'))
# ten = ['X', 'x', 'Ⅹ']
# ID = ["10" if x in ten else x for x in lis]     #将罗马数字Ⅹ和字母X替换为10
# W = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
# Checkcode = [1, 0, 'X', 9, 8, 7, 6, 5, 4, 3, 2]
# sum = 0
# for i in range(17):     #https://blog.zeruns.tech
#     sum = sum + int(ID[i]) * W[i]
# if Checkcode[sum % 11] == int(ID[17]):
#     print('输入正确')
# else:
#     print('输入错误')


# 质数又称素数。一个大于1的自然数，除了1和它自身外，不能被其他自然数整除的数叫做质数;否则称为合数。

# 方法1
# def primeNUM(min,max):
#     if min==1:
#         print('')
#         min += 1
#     for i in range(min, max+1):
#         for j in range(2, i + 1):
#             if i % j == 0:          #判断i能不能被整除
#                 break               #退出for循环
#         if j == i:                  #若j等于i，说明i是素数
#             print(i,end=" ")
#     print('')
# primeNUM(1,200)
#
# #方法2
# def test(num):
#     list = []              #定义一个列表 用于存储计算的数
#     i = num -1             # 去除本身
#     while i > 1:           # 去除1
#         if num %i == 0 :   #判断是否有余数
#             list.append(i) # 将所有的能整除i的数加入列表
#         i -= 1
#     if len(list) == 0 and num != 1:     # 如果列表为空 就是表示除了1和它本身能整除
#         print(num,end=' ')
#
# def primeNUM2(min,max):
#     j = min
#     while j < max:
#         test(j)
#         j += 1
#     print('')
# primeNUM2(1,100)

'''
统计字符串中，各个字符的个数
比如："hello world" 字符串统计的结果为： h:1 e:1 l:3 o:2 d:1 r:1 w:1
'''

# a="hello world"
# b=[]
# for i in a.replace(" ",""):
#     if i in b:
#         pass
#     else:
#         b.append(i)
# for i in b:
#     print("%s:%s"%(i,a.count(i)))


# 用函数实现输入某年某月某日，判断这一天是这一年的第几天，闰年情况也考虑进去

# month31 = [1, 3, 5, 7, 8, 10, 12]  # 一个月有31天的月份
# month30 = [4, 6, 9, 11]  # 一个月有30天的月份
#
#
# def leap_year(year):  # 判断闰年，如果是闰年就返回1，不是就返回0
#     if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):  # 判断条件：能被400整除的年份 或者 能被4整除，但是不能被100整除的年份
#         return 1
#     else:
#         return 0
#
#
# def shuru():  # 获取用户输入
#     i = 1
#     while i == 1:
#         time = input("请输入年月日(以/为分隔符，例如2020/01/30)：")  # 将输入的字符串放入time变量中
#         time2 = time.split('/')  # 将time字符串以"/"为分隔符进行分隔，将分隔后的字符串放入列表time2中
#         year = int(time2[0])  # 将列表time2中下标为0的字符串转为整数类型放入变量year中
#         month = int(time2[1])
#         day = int(time2[2])
#         if len(time2) == 3 and (
#                 (month in month31 and day in range(1, 32)) or (month in month30 and day in range(1, 31)) or (
#                 month == 2 and day in range(1, 30) and leap_year(year)) or (
#                         month == 2 and day in range(1, 29) and leap_year(
#                     year) == 0)):  # 判断输入的年月日是否符合规范，如果符合规范就使i等于0使循环结束，否则就打印“输入错误”然后继续重新输入
#             i = 0
#         else:
#             print('输入错误')
#     year = int(time2[0])
#     month = int(time2[1])
#     day = int(time2[2])
#     return year, month, day, time
#
#
# def js(year, month, day, time):  # 计算第几天
#     day_sum = 0
#     for x in range(1, month + 1):
#         if x in month31 and month > 1:
#             day_sum += 31
#         elif x in month30 and month > 1:
#             day_sum += 30
#         elif x == 2 and leap_year(year) and month > 2:
#             day_sum += 29
#         elif x == 2 and month > 2:
#             day_sum += 28
#     day_sum += day
#     print("%s是%d年的第%d天" % (time, year, day_sum))
#
#
# year, month, day, time = shuru()
# js(year, month, day, time)

# name = "Eric"
# print("Hello ", end=','"would you like to learn some python?")
# print("Hello "+name.title()+",would you like to learn some python?")

# num = 5
# # str()将num转变为字符串
# message = str(num)+" is my favorite number"
# print(message)