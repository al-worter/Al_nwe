# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/6 下午 10:23
# @Author   : liang yuyu
# @Site     : http://www.cdtest.cn/
# @File     : 练习.py
# @Software : PyCharm

# 1 # 1.画图说明以下代码的执行的内存指向和b的值是多少，并说明为什么
a = 10
b = a
# a = 100
print(id(a))
print(id(b))
# print('----------------------------------------------------------')
# # # 2.将以下数据转换为其它三种类型，并观察结果
# # # 整数
a = 1
print(int(a))
print(type(a))
print('------------------------------')
# # # 浮点数
b = 1.1
print(float(b))
print(type(b))
print('----------------------------')
# # # 布尔值
c = True
d = False
print(type(c))
print(type(d))
print('--------------------------------')
# # # 字符串
e = 'a'
f = '123'
g = "abc"
print(type(e))
print(type(f))
print(type(g))
print('--------------------------------------')
# # 3.使用input函数，输出类似"我是xxx，我今年xx岁。"
name = input('我的名字是：')
age = input('我的年龄是：')
print('我的名字叫：', name)
print('我的年龄是：', age)
print('----------------')
# # 4.获取多个用户输入的名字、年龄、身高和体重，连成一句话打印出来。
# # 要求：用几种不同的字符串格式化 方式打印，并且要求对齐  格式化 有 % /
name = input('请输入您的名字：')
age = input('您的年龄是：')
height = input('您的身高是：')
weight = input('您的体重是：')
print('其名字是：%s,其年龄是：%s ,其身高是：%s ,其体重是：%s ' % (name, age, height, weight))
#
print(f'我名字叫:{name},我的年龄是:{age},我的身高是:{height},我的体重是:{weight}')

# # 5.将4.3 逻辑运算符中的运算表，写成代码，并检查结果是否与表中一致
a = True
b = False
print(a and b)
print(a or b)
print(not (a and b))
# # 6. 华氏温度转换为摄氏温度,英语国家大多采用华氏温度，
# # 华氏温度转设置温度转换公式为C=(F-32)*5/9，摄氏温度转华氏温度公式 为：F=(C*9/5)+32
# # 编写一个程序将用户输入的华氏温度抓换为摄氏温度，输入如下：
# # 请输入华氏温度：68 # 摄氏温度为：20
a = float(input('请输入摄氏温度：'))
b = float(input('请输入华氏温度：'))
c = (a * 9 / 5) + 32
d = (b - 32) * 5 / 9
print(f'摄氏温度转华氏温度：{c},华氏温度转摄氏温度:{d}')
# 方法二 用format
a = float(input('请输入摄氏温度：'))
b = float(input('请输入华氏温度：'))
c = (a * 9 / 5) + 32
d = (b - 32) * 5 / 9
print("摄氏温度{}转换为华氏温度为：{}".format(a, c))
print("华氏温度{}转换为摄氏温度为：{}".format(b, d))
