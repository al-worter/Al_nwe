# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/14 18:46
# @Author   : Jing wen
# @Site     : http://www.cdtest.cn/
# @File     : python task314.py
# @Software : PyCharm
'''
1.定义一个计算类,有两个属性,数字1,数字2,用到init方法，具有 加 减 乘 除 方法,每个方法都返回计算的结果.
创建一个对象,调用上面的属性和方法
'''
import re


class Computers:
    figure = 0
    number = 0

    def __init__(self, figure, number):
        print(self)
        self.figure = figure
        self.number = number

    def add_up(self, now_add1, now_add2):
        self.figure += now_add1
        self.number += now_add2
        print(f'{self.figure}+{self.number}={self.figure + self.number}')

    def reduce_up(self, now_reduce1, now_reduce2):
        self.figure += now_reduce1
        self.number += now_reduce2
        print(f'{self.figure}-{self.number}={self.figure - self.number}')

    def ride(self, now_ride1, now_ride2):
        self.figure += now_ride1
        self.number += now_ride2
        print(f'{self.figure}*{self.number}={self.figure * self.number}')

    def divide(self, now_divide1, now_divide2):
        self.figure += now_divide1
        self.number += now_divide2
        print(f'{self.figure}÷{self.number}={self.figure / self.number}')


# 加
computer1 = Computers(0, 0)
computer1.add_up(6, 4)
# 减1
computer2 = Computers(0, 0)
computer2.reduce_up(6, 4)
# 乘
computer3 = Computers(0, 0)
computer3.ride(6, 4)
# 除
computer4 = Computers(0, 0)
computer4.divide(6, 4)

'''
2. 定义函数,接收两个文件的路径,尝试默认字符集打开第一个文件,如果能正常打开,则读取这个文件的所有内容并返回,
如果出错,则使用utf8的字符集打开该文件,读取所有内容并返回,不管是怎么打开的文件,都把里面的内容写入到当前路径的copy.txt文件下.
使用到try..except..finally
'''
print("--------------------------------")


def files():
    try:
        with open(r"D:\pyworkspace\pythonex\pythonex9\test1.txt", mode='r', encoding='utf8') as file:
            str1 = file.readlines()
            print(str1)
            return
    except:
        with open(r"D:\pyworkspace\pythonex\pythonex9\text2.txt", mode="r", encoding="utf8") as file:
            str2 = file.readlines()
            print(str2)
            return
    finally:
        with open(r"D:\pyworkspace\pythonex\pythonex9\copy文件", mode="r", encoding="utf8") as file:
            str3 = file.readlines()
            print(str3)
            return

if __name__ =="__main__" :

    files()
print("--------------------------------")
'''
3. 从字符串里面匹配出座机号码.
number = '123-6287676 028-2500545 0827-6297696 7654569' 
座机号要求:
1. 区号-号码组成  
2. 区号第一位必须是0 长度3-4位
3. 区号和号码中间必须有-   
4. 号码第一位必须1-9 长度7位
'''

numbers1 = '123-6287676 028-2500545 0827-6297696 7654569'
print(re.findall(r"0\d{2,3}-[1-9]\d{6}", numbers1))

'''
2. 定义函数,接收两个文件的路径,尝试默认字符集打开第一个文件,如果能正常打开,则读取这个文件的所有内容并返回,
如果出错,则使用utf8的字符集打开该文件,读取所有内容并返回,不管是怎么打开的文件,都把里面的内容写入到当前路径的copy.txt文件下.
使用到try..except..finally
'''

def copy_file(file_path):
    all = None
    try:
        with open(file_path) as file:
            all = file.read()
            return all
    except Exception as e:
        print(f"打开文件失败,失败原因为{e},\n正在重新打开...")
        with open(file_path, encoding="utf8") as file:
            file.write(all)

'''
1.定义一个计算类,有两个属性,数字1,数字2,用到init方法，具有 加 减 乘 除 方法,每个方法都返回计算的结果.
创建一个对象,调用上面的属性和方法
'''
class Computer:

    def init(self,no1,no2):

        self.no1 = no1

        self.no2 = no2

    def sum(self):

        return self.no1+self.no2

    def jian(self):

        return self.no1-self.no2


