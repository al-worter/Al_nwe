# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/4 上午 10:02
# @Author   : liang yuyu
# @Site     : http://www.cdtest.cn/
# @File     : invariable.py
# @Software : PyCharm

# 3.1 标识符
# 1. 标识符可以用字母、数字、下划线，数字不可以开头
# 2. python 是大小写敏感的语言，a和A是两个不同的标识符
# 3. 下划线开头的标识符有特殊含义
# 4. 关键字不可以用作标识符： 如IF

# 关键字 3.2
import keyword

print(keyword.kwlist)

# 3.3 变量
# 变量的定义： 变量保存内存中的数据地址，简单可以理解为一个容器。
a = 10
print(id(a))  # 用ID() 来看变量内存地址  type（） 是看类型
print(type(a))

a = '汇总'
print(id(a))
print(type(a))

# jin进阶 关于变量的内存地址

a = 10
b = a
print(id(b))

# 数据类型 有三种 数值类型  布尔值类型  字符串类型
# 浮点数float 就是有小数的数值; 需要 高精度的数值的时候用 文本进行记忆
b = 1.1
print(type(b))
# 布尔类型 Bool  的数值只有两个 TRUE false 两个
c = True
d = False
print(type(c))
print(type(d))

e = 'a'
f = '123'
g = 'asd'
# 多行字符串用''' 或者'''
h = '''123asd'''
print(type(e))
print(type(f))
print(type(g))

ranking1 = 'He sai I love you:', "i need respond"
