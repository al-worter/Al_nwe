# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/12 11:01
# @Author   : Jing wen
# @Site     : http://www.cdtest.cn/
# @File     : 3-12 进阶.py
# @Software : PyCharm

# 10.1 文件创建和打开  看源代码 按ctrl + 一光标 到代码上
def foo1():
    # 打开 /创建文件
    # ffl = open(".test1.txt", mode='r',encoding='utf8')
    file1 = open(r"D:\pyworkspace\pythonex\pythonex7\test1.txt", mode='r')  # 绝对路径最好前面加r 禁止转义

    # 文件的关闭
    file1.close()


# 文件打开 自动关闭 with open()
def foo2():
    with open(r"D:\pyworkspace\pythonex\pythonex7\test1.txt", mode='r') as file:
        pass


# 10.2 文件读取 ： 有三种
# read()
# readline() 单行   一次读取一行
# readlines() 多行   重点掌握
def foo3():
    with open("./test1.txt", mode='r', encoding='utf8') as file:
        str1 = file.read(7)
        print(str1)
        str1 = file.read(7)
        print(str1)


# read(n) 第二次的时候是接着它的尾部开始读#
def foo4():
    with open("./test1.txt", mode='r', encoding='utf8') as file:
        list1 = file.readline(4)
        print(list1)


def foo5():
    with open("./test1.txt", mode='r', encoding='utf8') as file:
        str1 = file.readlines(4)
        print(str1)


# 10.3 文件的写入
# 1.write()  将字符串内容写入文件，文件不存在会创建，存在就会覆盖"w" w模式会覆盖并追加写入一次内容
# 2.writelines()
def foo6():
    with open("./test2.txt", mode='w', encoding='utf8') as file:
        str2 = "panda\n汇智动力\n2022\n白白白啊"
        file.write(str2)


def foo7():
    with open("./test3.txt", mode='w', encoding='utf8') as file:
        list3 = ["哈数啥是\n", '汇智动力呀\n', '哈哈哈哈\n']
        file.writelines(list3)


if __name__ == "__main__":
    print(foo1())
    print(foo2())
    print(foo3())
    print(foo4())
    print(foo5())
    print(foo6())
    print(foo7())
