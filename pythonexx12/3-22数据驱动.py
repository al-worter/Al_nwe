# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/22 10:49
# @Author   : Jing wen
# @Site     : http://www.cdtest.cn/
# @File     : 3-22数据驱动.py
# @Software : PyCharm
#
''''''
'''
 学习要义:
    1.数据保存的方式:
        1) 保存在py文件中,使用全局变量引用.
        2)保存文本文档中,使用with open()方法打开文件
        3) 保存在表格中
            1.excel表格
            2.csv表格:可以理解为低配版的excel,不支持函数公式等功能,只是一个单一的储存数据的能力,可以说是表格版的文本文件.
                1).打开一个新的记事本,文件另存为-文件名后缀必须是csv，编码设置为utf-8 ,点击保存
                2).双击打开csv文件,编辑数据,保存-保存的时候提示框选择’是’
    2.
    
    
    3.
'''
'''保存在py文件中的测试数据'''
import test_data #import 后面是加python文件名.并且同一目录下的文件可以直接import导入.

print(test_data.right_data)   # 使用模块名调用变量
print(test_data.right_data(0))  # 取出第一组测试数据
print(test_data.right_data[0]["username"])   # 取出第一组测试数据的账号

'''保存在文档中的'''
with open('test_data.text',"r") as file:
    all = file.readlines()
    print(all)


'''保存在表格中的数据'''
import pandas
file = pandas.read_csv('test_hailey.csv')












