# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/11 10:57
# @Author   : Jing wen
# @Site     : http://www.cdtest.cn/
# @File     : 函数创建 function包.py
# @Software : PyCharm

# 8.1 函数的定义和调用  pass 是空语句，  在创建函数时，不想使用的时候可以在其函数体放入pass
# def add(a,b): # def 函数名(形参):
#     c = a/b     # 函数体块
#     return c    # 结束函数调用，并返回值  . 没有返回值，即显示NONE
#     # print('return之后的语句是多余的') # return 之后语句不会执行。是多余的，储存后台等待调用。
# x = add(1,99)
# print(x) # 即调用 上面函数名 体 1 =a , 99 = b  ，给予实参 即可输出

# 练习： 编写一个函数，必须参数a,b,c，函数计算a的平方、b的立方、c三者的和，并返回。
# def baby(a, b, c):
#     a = a ** 2  # 可无
#     b = b ** 3  # 可无
#     c = a + b  # 可无 直接在return 后 加表达式
#     return a, b, c
#
#
# L = baby(1, 4, 6)
# print(L)
print('---------------------------')

# 9.2 函数的参数传递
# 9.2.1位置参数、必须参数： 必须按照行参的数量和顺序传递参数值
# def fool(a, b):
#     print(f'a={a},b={b}')
#
#
# fool(1, 2)

print('---------------------------')

# 9.2.2 关键字参数： 在调用的实参中使用赋值语句，将会按照名字传递值，而不是顺序。
# def fool1(a, b):
#     print(f'a={a},b={b}')
#
#
# fool1(b=1, a=2)

print('---------------------------')

# 9.2.3 默认值参数  是指在函数的形参列表中为形参设置默认值，如果形参没有实参传入会默认使用默认值
# def fool2(a, b=10):
#     print(f'a={a},b={b}')
#
#
# fool2(1, 2)
# fool2(1)
# 注意： 默认值的形参必须放最后
print('---------------------------')

# 9.2.4 可变形参


# 9.3 函数中局部变量和全局变量
# 9.3.1 局部变量  定义在函数内部，只能在函数内部访问    变量
# def foo():
#     num = 6
#     print(f'函数内的局部变量内部num = {num}')
#
#
# foo()

print('---------------------------')


# 9.3.2 全局变量
# num1 = 101
#
#
# def foo1():
#     print(f'函数内部的num1= {num1}')
#
#
# foo1()
# print(f'函数外部num1= {num1}')
# print('---------------------------')


#  global 关键字  将函数内部的变量定义为全局变量。
def foo2():
    global num2  # 定义该变量为全局变量
    num2 = 8
    print(f'函数内部的变量num2= {num2}')


foo2()
print(f'外部函数的num2={num2}')
#

# 9.4 函数的返回值
# 函数必有返回值 ，没有return 语句，会自动加return 返回None
# return 除了返回值外，并结束函数的调用
# return 的返回值可以理解为函数的值
# def foo3(a, b) -> None:
#     c = a ** b
#     return c
#
#
# d = foo3(8, 8)
# print(d)

# 9.6 函数的递归调用
# 递归函数： 函数自己调用自己，将一个复杂或大的问题不断简化变小，知道由一个确定答案
# def dy1(n):  # 递归函数1.必须是有形参
#     if n == 1:  # 递归函数2.必须是有选择语句 if 是停止递归的条件
#         return 1
#     else:  # else 即变成了递归的算法
#         return n + dy1(n - 1)
#
#
# print(dy1(997))


# 编写一个函数，用来接收正整数n, 返回1~n的平方和
def square_sum(n):
    result = 0
    for i in range(1, n + 1):
        result += i ** 2
    return result


print(square_sum(9))
# 调试性 语句
# if __name__ == "__main__":
