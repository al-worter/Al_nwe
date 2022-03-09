# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/7 11:18
# @Author   : Jing wen
# @Site     : http://www.cdtest.cn/
# @File     : 语句练习.py
# @Software : PyCharm

# 程序设计的三种基本结构： 顺序结构 、选择结构、循环结构
# 5.1.1 基本语句 if
# money = 1
# if money >= 5:
#     print('吃豆浆和包子')
# print('去上课')

# 练习 if 语句
# age = int(input('请输入你的年龄：'))
# if age >= 25:
#     print('小于25站到左边')
# print('请大于25岁的站到右边去')
# if-else 语句
# age = int(input("请输入您的年龄:"))
# if age >= 25:
#     print("站右边")
# else:
#     print("站左边")

# 用户输入一个数，判断这个数是偶数还是奇数s
# num = int(input("请输入一个数："))
# if num % 2 == 0:
#     print("是偶数")
# else:
#     print("是奇数")

# print(3 == 5, end='假的')

# sum1 = 0
# a = 1
# while a <= 100: # 循环条件
#     sum1 += a # 循环体
#     a += 1 # 迭代语句
# print(sum1)

# 1*2*3*4....*10。
a = 1
total = 1
while a <= 10:
    total = total * a
    a += 1
print(total)
#2
