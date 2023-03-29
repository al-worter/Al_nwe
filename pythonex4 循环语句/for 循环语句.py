# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/7 16:14
# @Author   : Jing wen
# @Site     : http://www.cdtest.cn/
# @File     : for 循环语句.py
# @Software : PyCharm

# 5.3 for 循环语句 本质是对一个序列进行递归扫描，循环次数由系列元素个数决定
#
# 5.3.1 range()产生一个序列
# 格式 ：range （start,end,step）
# a = range(10) # 意思是一个产生参数是end， 默认 start=0,step=1,产生1-10序列
# print(list(a))
# print(a)
# b = range(0,10)
# print(list(b))
# c = range(0,10,2)  # 三个参数 ： 0 是起点， 10 终点，2 是步长。
# print(list(c))
#
# for 循环实现1——100
# print(list(range(1,101)))
# total = 0
# for d in range(1,101):
#     total += d
#     print(total)
#
# 练习 1 累乘：100！5!=5x4x3x2x
# sum = 1
# for k in range(1,101):
#     sum =sum * k
# print(sum)
#
# 练习 2s
# for i in range(6):
#     print('*')
# for l in range(6):
#     print("*",end = " ")
# 练习 3
# for m in range(6):
#     for n in range(6):
#         print("*",end = ' ')
#     print('')
# 练习 4
# for m in range(6):
#     for n in range(6):
#         print("6",end= " ")
#     print("")
# 练习 5KL
# for m in range(6):
#     for n in range(m + 1):
#         print('*', end=" ")
#     print(" ")
#
# 练习 6 乘法表
# 方法一：
# for t in range(1, 10):
#     for y in range(1, t + 1):
#         print('{}x{}={}'.format(t, y, t * y), end=' ')
#     print(" ")
# 方法儿：
# for e in range(1,10):
#     for r in range(1,e+1):
#         print(f"{e:<2}x{r:<2}={e*r:<2}" , end = ' ')
#  print()