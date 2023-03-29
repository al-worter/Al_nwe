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
                 读取CSV表格用pandas.read_csv()
                 读取xls表格用pandas.read_excel()
'''
'''保存在py文件中的测试数据'''
# import test_data #import 后面是加python文件名.并且同一目录下的文件可以直接import导入.
#
# print(test_data.right_data)   # 使用模块名调用变量
# print(test_data.right_data(0))  # 取出第一组测试数据
# print(test_data.right_data[0]["username"])   # 取出第一组测试数据的账号
#
# '''保存在文档中的'''
# with open('test_data.text',"r") as file:
#     all = file.readlines()
#     print(all)
#
#
'''保存在表格中的数据 如csv/xls表格'''
import pandas
file = pandas.read_csv('test_hailey.csv')  #调用read_csv方法读取文件

# print(file)
# print(type(file)) #读取出来的类型是一个pandas对象.
#
# print(file.index.values) #返回数据的索引号.索引从第一行数据开始计算.自动忽略表头.
# print(file.loc[0]) # loc方法可以读取对应索引号的文件内容.返回一个对象#loc方法可以读取对应索引号的文件内容.
# print(file.loc[1]) # loc方法可以读取对应索引号的文件内容.
# print(file.loc[1].to_dict()) # to_dict)可以把用loc方法读取出来的单行对象转换为一个字典.

# 读取整个表格csv(excel)的文件,并且转为列表嵌套字典的格式
infor_list = []  # 定义一个空列表,用来接收下面读取出来的字典
for i in file.index.values:   # for i in [0 1]
    print(i)
    infor = file.loc[i].to_dict()   # 意思是每一次循环,都读取当前索引号的内容,并且转换为一个字典
    print(infor)
    infor_list.append(infor) # 每次循环都把这个字典添加到上面定义的列表
print(infor_list)






