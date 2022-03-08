# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/8 下午 11:14
# @Author   : liang yuyu
# @Site     : http://www.cdtest.cn/
# @File     : while和for循环语句练习.py
# @Software : PyCharm

# 1、闰年问题（输入一个年份，判断是否为闰年）
# 闰年：能被4整除不能被100整除或者能被400整除
# 口诀：4年一闰，百年不闰，400年又闰
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
Year = int(input('请输入年份：'))
while str(Year) != 'over':
    year = int(Year)
    if year > 0:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            print(str(year) + '年是闰年')
        else:
            print(str(year) + '年是平年')
    elif year < 0:
        if (year + 1) % 4 == 0 and (year + 1) % 100 != 0 or (year + 1) % 400 == 0:
            print('公元前' + str(-year) + '年是闰年')
        else:
            print('公元前' + str(-year) + '年是平年')
    else:
        print('年份不能为零，请重新输入')
    print('------------')
    Year = input('请输入年份(over退出)：')
    print('退出，已结束！')

# 2、小明身高1.75，体重80kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
# （1）低于18.5：过轻
# （2）18.5-25：正常
# （3）25-28：过重
# （4）28-32：肥胖
# （5）高于32：严重肥胖
# eval()函数是用来执行一个字符串表达式，并返回表达式的值。
print('hello-wellcome-to-磬苑')
name = str(input('请键入您的姓名:'))
height = eval(input('请键入您的身高(m):'))
weight = eval(input('请键入您的体重(kg):'))
gender = str(input('请键入你的性别(F/M)：'))
BMI = float(float(weight) / (float(height) ** 2))
if BMI <= 18.5:
    print(f'姓名：{name},{gender},身体状态：正常')
elif BMI <= 28.5:
    print(f'姓名：{name},{gender},身体状态：过重')
elif BMI <= 32.5:
    print(f'姓名：{name},{gender},身体状态：超重')
elif BMI > 32.5:
    print(f'姓名：{name},{gender},身体状态：严重肥胖')
# import time  # time模块
# nowtime = (time.asctime(time.localtime(time.time())))
# if gender == 'F':
#     print('感谢', name, '女士在', nowtime, '光临该店,祝您身体健康!')
# if gender == 'M':
#     print('感谢', name, '先生在', nowtime, '光临该店,祝您身体健康!')
# # 3.猜数字：系统给出一个1-10之间的整数，用户输入猜测的数字，系统给出相应的提示
import random
number = random.randint(1, 10)  # 产生1-10之间的随机整数
a = 1
b = 0
print('玩一个小游戏')
print('1-10的整数中猜')
while a != number and b < 6:
    a = input("来猜个数字吧：")
    if int(a) < number:
        print("太低了哦")
    elif int(a) > number:
        print("太高了哦")
    b = b + 1
    if int(a) == number:
        print("猜中了,恭喜你，猜对了")
        break
else:
    print("你没有机会了，你输了")
    print("这个数字就是————", number)

# 4.猜数字游戏，增加游戏次数限制，最多只能猜5次。如果5次都没猜正确，给出提示，游戏结束从
# num= 2
# a = 1
# b = 0
# print('玩一个小游戏')
# print('1-10的整数中猜')
# while a != num and b < 3:
#     a = input("来猜个数字吧：")
#     if int(a) < num:
#         print("太低了哦")
#     elif int(a) > num:
#         print("太高了哦")
#     b = b + 1
#     if int(a) == num:
#         print("猜中了,恭喜你，猜对了")
#         break
# else:
#     print("你没有机会了，你输了")
#     print("这个数字就是————", num)
# 5.打印以下图形
# * * * * *
# * * * *
# * * *
# * *
# *

# 6.打印以下图形
# * * * * *
#   * * * *
#     * * *
#       * *
#         *

# 7.打印以下图形
#         *
#       * *
#     * * *
#   * * * *
# * * * * *

# 8.打印以下图形
#       *
#     * * *
#   * * * * *
# * * * * * * *
#   * * * * *
#     * * *
#       *
