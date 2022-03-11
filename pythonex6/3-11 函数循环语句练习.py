# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/11 16:07
# @Author   : Jing wen
# @Site     : http://www.cdtest.cn/
# @File     : 3-11 函数循环语句练习.py
# @Software : PyCharm

# 1.# 求 1-100以内所有含6的数
def moths():  # 创建函数 不定义函数 形参
    list1 = []  # 把（1，100）de 的数转换成字符串，创建 列表
    for i in range(1, 101):
        i = str(i)  # i 等于 range（）序列中一个元素 即
        if i.count('6') >= 1:  # 如果i每个元素中含6 的元素count()统计出现次数
            list1.append(i)  # i出现的数，增加到新的 列表 list 中去
    return list1


# 2、Chuck Lucky赢了100W美元，
# 他把它存入一个每年盈利8%的账户。
# 在每年的最后一天，Chuck取出10W美元。
# 编写一个程序，计算需要多少年Chuck就会清空他的账户。
def lucky():  # 创建一个函数计算
    money = 100  # 初始值 本金
    year = 0  # 年份
    while money >= 0:  # 循环条件
        money = money * 1.08
        money = money - 10
        year += 1

    return year


# 3、题目：猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个 第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
# 以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。
# 程序分析：采取逆向思维的方法，从后往前推断。
def monkey():  # 思路是： 一天吃掉前一天的一半再吃掉一个,到第十天后发现只剩下一个了。 即 y 为天数，x 为果 , 每天吃一半减一个： (x/2)-1
    x = []  # 创建列表把第一天的果实转化成元素，化成列表元素 x = []
    x = [1]  # 第十天发现只省一个，那么 x = [1]
    for i in range(9):  # 用for循环语句循环9次 和range（)函数产生一个序列。
        y = 2 * (x[i] + 1)  # 把x[1] 转成变量x[i]
        x.append(y)  # 名.append 是给列表增加元素 ，因为前面添加了空列表。
    # x.reverse()  #把序列反向输出
    return x


# 4、不使用自带函数，写一个函数，用于返回一个数的绝对值
def value1():
    a = int(input('输入任意一个数，可知该值的绝对值：'))
    if a >= 0:
        return a
    else:
        return a * -1


# 5、写一个函数，用来求三个数的最大值
def add(a, b, c):
    # list1 = [a, b, c]
    return max(a, b, c)


# 提升：
# 6、写一个函数，返回输入整数（大于999小于10000）的每位数的数字之和。

# 7.递归实现阶乘：
# n！=nxn-1xn-2x....1
# 5!=5x4！

# 8.实现1！+2！+3！+。。。+n！


print('----------------------------')
if __name__ == "__main__":
    print(moths())
    print(lucky())
    print(monkey())
    print(value1())
    print(add(2, 3, 4))
