# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/9 17:45
# @Author   : Jing wen
# @Site     : http://www.cdtest.cn/
# @File     : 序列元组练习.py
# @Software : PyCharm

# 0. 解决千年虫问题，以前的电脑为了节省存储空间，通常年份都是用的两位数字，这样跨过2000年后，
# 2000年和1900都会被表示为00，造成计算机系统故障，编写程序将以下序列中年份转换为4位，并升序
# 输出。
# 当前序列:[89,98,00,75,68,37,58,90]
# 输出序列:[1937,1958,1968,1975,1989,1990,1998,2000]
# years = [89,98,00,75,68,37,58,90]
# years_new = []
# for year in years:
#     if year ==00:
#         year
#


# xl1 = [89, 98, 00, 75, 68, 37, 58, 90]
# for x in range(len(xl1)):
#     xl1[x] += 2000 - 100
#     xl1[2] = 2000
# print(sorted(xl1))
# 1. 练习：将列表[45,23,2,5,3,2,6,45,43,21,66,2,3,2]进行从小到大排序，不能用sort()函数，
# erp = [45, 23, 2, 5, 3, 2, 6, 45, 43, 21, 66, 2, 3, 2]
# # list.sort(erp)
# 使用DEL 操作符
list1 = [-99,100,6]
del list1[0]
print(list1)

# print(sorted(erp))
# 冒泡排序 算法
erp = [45, 23, 2, 5, 3, 2, 6, 45, 43, 21, 66, 2, 3, 2]
for i in range(len(erp)-1):  # 外层循环决定比较次数
    for j in range(len(erp)-i-1): # 内层循环决定每次比较哪些数
        if erp[j]>erp[j+1]:
            # temp = erp[j]
            # erp[j] = erp[j+1]
            # erp[j+1]=temp
            erp[j],erp[j+1] = erp[j+1],erp[j]
        print(f'第{i}:{j}循环：{erp}')
    print(f'------------------第{i:2}循环,erp：{erp}')
print('最后排序------------')
print(erp)

# 2、求 100-200以内同时能被7、8整除的数
# 方法一：
# i = 0  # 定义 计数变量为b，初始值为1
# for i in range(100, 201):  # 遍历1-100取值，定义为变量 i
#     if i % 7 == 0 and i % 8 == 0:
#         print(i, end=' ')

# 方法二：
# list1 = []
# for i in range(100,201):
#     if i%7 == 0 and i% 8 ==0:
#         list1.append(i)
# print(list1)

# 3.找出一个列表中，只出现了一次的数字，并且保持原来的次序，例如[1,2,1,3,2,5]结果为[3,5]
# def 函数名(参数1, 参数2, ……, 参数N):
# 执行语句
import random

print('\n----------------------------------------------')
# list2 = [1,2,1,3,2,5]
# list3 = []
# for i in list2:
#     if list2


# lgy = [1, 2, 1, 3, 2, 5]
# tmp_1 = [3, 5]
# for i in lgy:
#     count = lgy.count(1)
#     if count >= 2:
#         continue
#     tmp_1.append(1)
# print(tmp_1)

# 提升
# 4、求 0 -1 + 2 - 3 + 4 - 5 + 6 -7.... + 100
print('----------------------------------------------')
# total = 0
# for i in range(0,101):
#     if i %2 ==0:
#         total +=i
#     else:
#         total -= i
# print(total)



# def sum_go(sum_to):
#     sum_all = 0
#     for i in range(1, sum_to + 1):
#         sum_all += i * (-1) ** (1 + i)
#     return sum_all
#
#
# if __name__ == '__main__':
#     result = sum_go(sum_to=100)
#     print(result)
# list1 =list (range(0,101,2))
# list2 =list (range(0,101,2))
# total = sum(list1)-sum(list2)
# print(total)
# 5.求100以内的素数：>1整数，只能被1和自己整除
print('----------------------------------------------')
i = 2
while (i < 100):
    j = 2
    while (j <= (i / j)):
        if not (i % j): break
        j = j + 1
    if (j > i / j):
        print(i, "是素数")
    i = i + 1
print("GOOD BYE")

primes = []
for num in range(2,101):
    time = 0
    for i in range(1,num +1 ):
        if num % i ==0:
            time += 1
    if time == 2:
        primes.append(num)
print(primes)

# for i in range(2,101):
#     for j in range(2,i):
#         if i%j ==0:
#             break
#     else:
#         print(i,end=' ')

# 6. 水仙花数：水仙花数是指一个 n 位数 ( n 大于等于 3 )，它的每个位上的数字的 n 次幂之和等于它本身。
# # （例如：1的3次方 + 5的三次方 + 3三次方 = 153）。根据这个要求，打印所有三位数的水仙花数。
print('----------------------------------------------')
# 方法一 用列表进行
# list1 = []
# for num in range(100,1000):
#     a = num // 100
#     b = (num -a * 100) // 10
#     c = num % 10
#     if a**3 + b**3 + c**3 ==num:
#         list1.append(num)
# print(list1)

# 方法二 用FOR多重嵌套循环
# list5 = []
# for a in range(1,10):
#     for b in range(0,10):
#         for c in range(0,10):
#             if a**3 + b**3 + c**3 == a**100+b*10+c:
#                 list5.append(a**100+b*10+c)
# print(list5)

# 7.一球从100米高度自由落下，每次落地后反跳回原高度的一半；
# # 再落下，求它在 第10次落地时，共经过多少米？第10次反弹多高？
print('----------------------------------------------')
height= 100
total1 = height
for i in range(9):
    height = height/2
    total1 += 2*height
print(f'总共经过：{total1}米,第10次反弹高度为:{height/2}')


# 8. 随机产生20个100-200之间的正整数存放到列表中，
# 并求列表中的所有元素最大值、最小值、平均值，然后将各元素的与平均值的差组成一个列表
print('----------------------------------------------')
list5 = []
for i in range(20):
    num = random.randint(100,200)
    list5.append(num)
print(list5)
max = max(list5)
min = min(list5)
avg = sum(list5)/len(list5)
print(f'最大值：{max},最小值：{min},平均值：{avg}')
list6=[]
for i in list5:
    list6.append(i-avg)
print(list6)