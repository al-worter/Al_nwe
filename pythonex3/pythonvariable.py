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

# 转义字符 以\开头的字符串，表达一些特殊含义
print('人生若只如初见，\t何事秋风悲画扇')

# 3.3.3 非0 ,非空的其他数据类型
# float 浮点型 将其他类型转换成它
a = 1.2
b = '111'
c = 20
print(float(a))
print(float(b))
print(float(c))

print('----------------------------------')
# 3.3.4bool() 转换其他类型
a = 10
b = 0
c = 'a1'
d = ""
print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))

print('----------------------------------------')

# 格式化字符串 ：是为了将字符串和其他数据类型混合输出
# 方法有两种 ： 1. 占位符格式化 ；  2.f函数格式化

# 例如 1-1
name = '汇智动力'
age = 88
print('我的名字是：%s, 我的年龄是:%d。' % (name, age))  # %s 是用 str()函数进行字符转换，%d是转换成有符号的十进制

print('--------------------------------')

# 1-2 拓展 指定输出宽度，在%和s/d/f之间插入数据，默认右对齐
print('我的名字是：%s, 我的年龄是:%10d岁。' % (name, age))

# 1-3 指定宽度，高位补零
print('我的名字是：%s, 我的年龄是:%010d岁。' % (name, age))
# 1-4 指定小数的宽度和小数位数
pi = 3.14223
print('Π的值是：%10f' % (pi))
print("Π的值是：%10.2f" % (pi))  # 参数7位 ，小数2位，小数点占1位
print('Π的值是：%-10.8f' % (pi))  # 左对齐就在%后加-

# f" 函数格式化字符串

name = '汇智动力'
age = 23
print(f'我的名字叫： {name},我的年龄是：{age}岁。')
print('-------------------------------------------------------')
# sd
grade = 143
age = 18
name = "汇智动力"
print(f'我的成绩：{grade},我的年龄是：{age},我的学科：{name}。')
print('--------------------------------------------------------------------------—----')
# 附注  数字类型
a = 443
b = 2.3
c = '22'
print(int(a))
print(int(b))
print(int(c))
print('--------------------------------------------------------------------------—----')
#
# 指定宽度
pi = 3.1415
print(f'Π的值是：{pi:10}')
# 指定宽度和zhid小数位数
print(f'Π的值是：{pi:10.2f}')
# 补零
print(f'Π的值是：{pi:010.2f}')
# 左对齐，低位补零
print(f'Π的值是：{pi:<010.2f}')
print(f'Π的值是：{pi:<10.2f}')