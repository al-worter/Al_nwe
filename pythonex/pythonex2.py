# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/4 上午 12:28
# @Author   : liang yuyu
# @Site     : http://www.cdtest.cn/
# @File     : python ex2.py
# @Software : PyCharm
import keyword

print('生活', '生存')
#  查看关键字 有哪些
print(keyword.kwlist)

print('........................................')

# 变量的命名变更
name = 6
print(name)
#  type 可以看到是什么类型的变量
a = 5
print(type(a))
a = '二百五'
print(type(a))
# 给变量 进行赋值的过程实际上是赋予内存地址 ID（） 变量改变时重新 也会重新变更内存地址
a = 10
print(id(a))
a = 100
print(id(a))
# 变量赋值给变量  A的存放地址就赋予了B
a = 10
b = a
print(id(a))
print(id(a))
# 数据类型 基本的有如下
