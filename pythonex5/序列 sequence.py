# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/9 16:52
# @Author   : Jing wen
# @Site     : http://www.cdtest.cn/
# @File     : 序列 sequence.py
# @Software : PyCharm

# 序列操作
# 6.1 index 操作
# list1 = [ 1, 2,3,4,5]
# tuple1 = (1,2,3,4,5)
# print(list1[-1])
# print(tuple1[-len(tuple1)])
# 序列的index索引可以是数值，也可以是数值变量表达式
# 序列中包含序列
list2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(list2[0][0])
print(list2[2][1])
print(list2[1][2])
# 多层数据结构： 左边是外层高维，右边是内层低维
for i in list2:
    print(i)
    for j in i:
        print(j)

#

# 6.2  序列的切片
# list [start:end:step]： start 默认为0 ；end默认为n ；包左不包右，step 默认 1
list4 = [1, 2, 3, 4, 5, 6, 7]
print(list4[1:3])
print(list4[1:5:2])
print(list4[1:])
print(list4[:5])  #
print(list4[::3])  # 双冒号间隔3
# 6.3 序列相加
# 相同类型的序列可以相加，拼接在一起
list5 = [2, 3]
list6 = [4, 5]
list7 = list5 + list6
print(list7)

# 6.4 操作序列的函数。
str1 = 'abcdef'
print(list(str1))