# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/9 13:31
# @Author   : Jing wen
# @Site     : http://www.cdtest.cn/
# @File     : 循环嵌套 结束循环.py
# @Software : PyCharm

# 数据结构 ：为了保存多个数据的一种存储结构，叫容器 container
# 可理解为一排 整齐物品

# 分类： 序列（列表,元组，字符串）和 非序列（字典\ 集合）
# list = ['red','green','blue','yellow','white','black']
# print(list[2])

# kap= [10,20,30,40,50,60,70,80,100]
# print(kap[1:4])

# pop = [1,1.1,'abc',True,False,2,6]
# # len () 获取列表的长度
# print(len(pop))

# max() 获取列表的元素中最大值，并只针对所有元素都是数值类型的列表
# pop1 = [22,334,453,34,-32,-2]
# print(pop1[0:4])
# print(max(pop1))
# print(min(pop1))
# # min() 获取列表的元素中最小值
# print(min(pop1))
##
# 增加列表元素 使用 append() ,该元素默认添加到末尾。
# pop2 = [22,334,453,34,-32,-2]
# pop2.append(203)
# print(pop2)
# 指定增加到某元素位置前， list.index()

# 删除列表元素
# pop3 = [22,334,453,34,-32,-2]
# # 用 pop()
# pop3.pop() # 为空即表示默认删除最后一个
# pop3.pop(-2) # 为指定某元素位置

# del pop(2)
# print(pop3)

# 根据 元素值删除元素 , 调用list对象的remove方法
# list.remove(元素值)：根据元素值删除元素，如果有多个元素，则删除第一个
# list = [2,1,3,4,123,44,6,1,2,4]
# list.remove(4)
# list.append(520)
# print(list)
# print([520]*4)
# for x in [2,1,3]:
#     print(x,end=' ')

# # # 修改元素
# list1 = [2, 1, 3, 4, 123, 44, 6, 1, 2, 4]
# # 对列表的指定index 重新赋值
# list1[4] = 999
# print(list1)
# print(list1[3:6])
# # 6.1遍历列表元素  ： 1、直接遍历列表的元素    2、使用range()产生列表index 进行赋值
# # 1. 直接使用for循环遍历
# list2 = [2, 1, 3, 4, 123, 2, 4]
# for x in list2:
#     x += 1  # 如果再for 当中进行增加条件，那么 x 变量 就会改变储存地址， 需要用到range（）
#     print(x)
# print(id(list2))
# # 2.通过range()产生列表的index序列
# list3 = [1, 2, 3, 4, 5, 6]
# for c in range(len(list3)):
#     list3[c] += 1
# print(list3)
#
#
# # 6.2 元组 Tuple
# # 6.2.1  元组的定义
# tuple1 = (1,1.1,'abc',True)
# print(tuple1[0])
# print(tuple1[len(tuple1)-1])
# # 操作元组函数
# tuple2 = (-11,0,99,22)
# print(len(tuple2))
# print(max(tuple2))
# print(min(tuple2))
# 元组 不可以增删改 所有的序列下表都是[]

# 元组的遍历查询。
# tuple2 = (22, 44, 55, 6, 77, 2)
# for e in tuple2:
#     print(e)
# for r in range(len(tuple2)):
#     print(tuple2[r])
#
#
# i = 2
# while (i < 6):
#     j = 2
#     while (j <= (i / j)):
#         if not (i % j): break
#         j = j + 1
#     if (j > i / j): print(i, "是素数")
#     i = i + 1
# print("GOOD BYE")

#coding=utf-8
#python - 列表分组技巧
#请写出一段 Python 代码实现分组一个 list 里面的元素,如 [1,2,3,...100]变成 [[1,2,3],[4,5,6]....]

# a = [x for x in range(1,101)]
#
# b = [a[i:i+3] for i in range(0, len(a),3)]
#
# print(b)
